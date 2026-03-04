"""
GSContext: Collects GS_STRING fragments and merges them into a single proof.

Usage:
    ctx = GSContext(crs)

    # Add @gsfy decorated functions with optional aliases
    lit.verify.gs_add(ctx, vk=vk, m=m, signature=tag,
                      aliases={'signature': 'tag'})

    rpsps.z_is_zero_or_verify.gs_add(ctx, vk=vk1, ...,
                                      aliases={'R_tilde': 'R_tilde_attr1', ...})

    # Finalize: merge, parse, type-check
    gs_node = ctx.finalize()

    # Compile
    proof_code = gs_node.compile_proof(ctx.definitions, crs_dict, "elements")

Reserved Constants:
    The following names are reserved and auto-available from CRS:
    - g: G1 (generator of G1, same as crs.g1)
    - h: G2 (generator of G2, same as crs.g2)
    - zp_zero: ZP (identity element in ZP)
    - zp_one: ZP (one element in ZP)
    - zp_minus_one: ZP (minus one element in ZP)
    - g1_zero: G1 (identity element in G1)
    - g2_zero: G2 (identity element in G2)
    - gt_zero: GT (identity element in GT)

    These can be used in equations without declaring them. Attempting to
    declare these as variables or constants will raise an error.
"""
from typing import Dict, List, Any, Optional
from gskit.framework import CRS
from gskit.parser import GSParser
from gskit.ast_builder import ASTTransformer
from gskit.elements import G1Element, G2Element, GTElement, ZpElement

# Reserved constant names and their types
RESERVED_CONSTANTS = {
    'g': 'G1',
    'h': 'G2',
    'zp_zero': 'ZP',
    'zp_one': 'ZP',
    'zp_minus_one': 'ZP',
    'g1_zero': 'G1',
    'g2_zero': 'G2',
    'gt_zero': 'GT',
}


class GSContext:
    """
    Collects GS_STRING fragments and their values from multiple @gsfy calls.
    Merges them into a single AST for proof generation.
    """

    def __init__(self, crs: CRS):
        self.crs = crs
        self.fragments: List[Dict] = []  # List of {gs_string, values, aliases}

        # Pre-compute reserved constant values from CRS
        self._reserved_values = {
            'g': crs.g1,
            'h': crs.g2,
            'zp_zero': ZpElement.zero(),
            'zp_one': ZpElement.init(1),
            'zp_minus_one': ZpElement.init(-1),
            'g1_zero': G1Element.zero(),
            'g2_zero': G2Element.zero(),
            'gt_zero': GTElement.zero(),
        }

    def add(self, gs_string: str, values: Dict[str, Any], aliases: Optional[Dict[str, str]] = None):
        """
        Add a GS_STRING fragment with its values.

        Args:
            gs_string: The GS_STRING defining variables, constants, equations
            values: Dict mapping names to Element values
            aliases: Optional dict mapping original names to new names
                     e.g., {'signature': 'tag'} renames 'signature' to 'tag'
        """
        self.fragments.append({
            'gs_string': gs_string,
            'values': values,
            'aliases': aliases or {}
        })

    def _apply_aliases(self, gs_string: str, aliases: Dict[str, str]) -> str:
        """Apply name aliases to a GS_STRING."""
        result = gs_string
        for old_name, new_name in aliases.items():
            # Replace whole words only (simple approach)
            # This replaces in variable declarations, constant declarations, and equations
            import re
            result = re.sub(r'\b' + re.escape(old_name) + r'\b', new_name, result)
        return result

    def _apply_aliases_to_values(self, values: Dict[str, Any], aliases: Dict[str, str]) -> Dict[str, Any]:
        """Apply name aliases to values dict."""
        result = {}
        for name, value in values.items():
            new_name = aliases.get(name, name)
            result[new_name] = value
        return result

    def _validate_reserved_names(self, name: str, decl_type: str):
        """
        Check if a name conflicts with reserved constants.

        Args:
            name: The variable or constant name
            decl_type: 'variable' or 'constant' for error messages

        Raises:
            ValueError: If name is a reserved constant
        """
        if name in RESERVED_CONSTANTS:
            raise ValueError(
                f"Cannot declare '{name}' as a {decl_type}. "
                f"'{name}' is a reserved CRS-level constant (type: {RESERVED_CONSTANTS[name]}). "
                f"Reserved constants are automatically available and cannot be redeclared."
            )

    def _merge_gs_strings(self) -> tuple:
        """
        Merge all GS_STRING fragments into one.

        Returns:
            tuple: (merged_gs_string, used_reserved_names)
        """
        if not self.fragments:
            raise ValueError("No GS_STRING fragments to merge")

        parser = GSParser()
        all_vars = {}   # name -> type_str
        all_consts = {} # name -> type_str
        all_eqs = []    # equation strings
        all_referenced_names = set()  # Track all names used in equations

        for fragment in self.fragments:
            gs_string = self._apply_aliases(fragment['gs_string'], fragment['aliases'])

            # Parse to extract components
            try:
                parsed = parser.parse(gs_string)
                transformer = ASTTransformer()
                ast = transformer.transform(parsed)

                # Collect variables with their types
                for var in ast.vars:
                    # Check for reserved name conflicts
                    self._validate_reserved_names(var.name, 'variable')

                    var_type = self._get_type_str(var)
                    if var.name in all_vars:
                        if all_vars[var.name] != var_type:
                            raise TypeError(
                                f"Variable '{var.name}' declared with conflicting types: "
                                f"{all_vars[var.name]} vs {var_type}"
                            )
                    else:
                        all_vars[var.name] = var_type

                # Collect constants with their types
                for const in ast.consts:
                    # Check for reserved name conflicts
                    self._validate_reserved_names(const.name, 'constant')

                    const_type = self._get_type_str(const)
                    if const.name in all_consts:
                        if all_consts[const.name] != const_type:
                            raise TypeError(
                                f"Constant '{const.name}' declared with conflicting types: "
                                f"{all_consts[const.name]} vs {const_type}"
                            )
                    else:
                        all_consts[const.name] = const_type

                # Collect equations and track referenced names
                for eq in ast.eqs:
                    eq_str = self._equation_to_string(eq)
                    all_eqs.append(eq_str)
                    # Extract names from equation
                    all_referenced_names.update(self._extract_names_from_equation(eq))

            except Exception as e:
                raise RuntimeError(f"Error parsing GS_STRING: {e}\n{gs_string}")

        # Find which reserved constants are used in equations but not declared
        used_reserved = set()
        for name in all_referenced_names:
            if name in RESERVED_CONSTANTS:
                if name not in all_consts:
                    used_reserved.add(name)

        # Build merged GS_STRING with reserved constants included
        var_lines = [f"    {name}: {typ}" for name, typ in all_vars.items()]

        # Add reserved constants that are used
        const_lines = [f"    {name}: {typ}" for name, typ in all_consts.items()]
        for reserved_name in sorted(used_reserved):
            const_lines.append(f"    {reserved_name}: {RESERVED_CONSTANTS[reserved_name]}")

        eq_lines = [f"    {eq}" for eq in all_eqs]

        merged = "variables:\n"
        merged += "\n".join(var_lines) if var_lines else "    # none"
        merged += "\n\nconstants:\n"
        merged += "\n".join(const_lines) if const_lines else "    # none"
        merged += "\n\nequations:\n"
        merged += "\n".join(eq_lines) if eq_lines else "    # none"
        merged += "\n"

        return merged, used_reserved

    def _extract_names_from_equation(self, eq) -> set:
        """Extract all variable/constant names referenced in an equation."""
        names = set()
        for mul in eq.eq_muls:
            names.add(mul.left)
            names.add(mul.right)
            if mul.gamma:
                names.add(mul.gamma)
        names.add(eq.target)
        return names

    def _get_type_str(self, node) -> str:
        """Get type string from a node."""
        class_name = type(node).__name__
        if 'G1' in class_name:
            return 'G1'
        elif 'G2' in class_name:
            return 'G2'
        elif 'GT' in class_name:
            return 'GT'
        elif 'Zp' in class_name or 'ZP' in class_name:
            return 'ZP'
        return 'ZP'  # default

    def _equation_to_string(self, eq) -> str:
        """Convert an equation AST node back to string."""
        parts = []
        for mul in eq.eq_muls:
            if mul.gamma:
                parts.append(f"{mul.left} * {mul.right} * {mul.gamma}")
            else:
                parts.append(f"{mul.left} * {mul.right}")
        return " + ".join(parts) + f" = {eq.target}"

    def _collect_values(self, used_reserved: set = None) -> Dict[str, Any]:
        """
        Collect all values, applying aliases and checking for conflicts.

        Args:
            used_reserved: Set of reserved constant names that are used.
                          If provided, their values will be added from CRS.
        """
        all_values = {}

        for fragment in self.fragments:
            values = self._apply_aliases_to_values(fragment['values'], fragment['aliases'])

            for name, value in values.items():
                # Skip reserved names - they come from CRS, not user values
                if name in RESERVED_CONSTANTS:
                    continue

                if name in all_values:
                    # Check if same value (by comparison)
                    if not self._values_equal(all_values[name], value):
                        raise ValueError(
                            f"Name '{name}' used with different values"
                        )
                else:
                    all_values[name] = value

        # Add reserved constant values that are used
        if used_reserved:
            for name in used_reserved:
                all_values[name] = self._reserved_values[name]

        return all_values

    def _values_equal(self, v1, v2) -> bool:
        """Check if two Element values are equal."""
        try:
            return v1 == v2
        except:
            # If comparison fails, assume different
            return False

    @property
    def definitions(self) -> Dict[str, str]:
        """Get definitions dict (name -> JSON serialized value) for compilation."""
        # Get merged string to find used reserved constants
        _, used_reserved = self._merge_gs_strings()
        values = self._collect_values(used_reserved)
        return {name: val.__json__() for name, val in values.items()}

    def finalize(self):
        """
        Merge all fragments, parse, and type-check.

        Returns:
            GSNode ready for compile_proof() or compile_verify()
        """
        # Merge and parse (also validates reserved names)
        merged_string, used_reserved = self._merge_gs_strings()

        # Validate values (also adds reserved values)
        self._collect_values(used_reserved)

        parser = GSParser()
        parsed = parser.parse(merged_string)
        transformer = ASTTransformer()
        ast = transformer.transform(parsed)

        # Type check (this validates equation types, etc.)
        ast.type_check()

        return ast

    def get_merged_string(self) -> str:
        """Get the merged GS_STRING (for debugging)."""
        merged, _ = self._merge_gs_strings()
        return merged
