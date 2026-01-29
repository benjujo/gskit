from charm.toolbox.msp import MSP as CMSP
from gskit.elements import ZpElement, group
from typing import List
import json

class MSP:
    def __init__(self, index:List[str], msp: List[List[int]]):
        self.index = index
        self._msp = msp
    
    @property
    def width(self):
        return len(self.msp[0])

    @property
    def msp(self) -> List[List[ZpElement]]:
        return [[ZpElement.init(i) for i in j] for j in self._msp]

    @classmethod
    def from_policy_str(cls, policy_str: str):
        cmsp = CMSP(group)
        tree = cmsp.createPolicy(policy_str)

        dict_msp = cmsp.convert_policy_to_msp(tree)

        index = list(map(cmsp.strip_index, dict_msp.keys()))
        width = len(max(dict_msp.values(), key=len))
        #matrix = [list(map(ZpElement.init, i)) + [ZpElement.zero()] * (width - len(i)) for i in dict_msp.values()]
        matrix = [list(i) + [0] * (width - len(i)) for i in dict_msp.values()]

        return cls(index, matrix)

    def serialize(self):
        return json.dumps({
            'index': self.index,
            'msp': self._msp
        })

    @classmethod
    def from_json(cls, json_str):
        msp_dict = json.loads(json_str)
        index = msp_dict['index']
        msp = msp_dict['msp']
        return cls(index, msp)

    def gs_string_and_values(self) -> tuple:
        """
        Generate GS_STRING for MSP equations and the values dict.

        MSP equations prove that the user has a valid combination of attributes
        satisfying the policy. For each column j:
        - Column 0: sum(M[i,0] * z_i) = 1  (must equal 1)
        - Column j>0: sum(M[i,j] * z_i) = 0  (must equal 0)

        Where z_i = 1 if attribute i is owned, 0 otherwise.

        Returns:
            (gs_string, values_dict) tuple
        """
        # Build variable declarations (z_attr for each attribute)
        var_lines = []
        for attr_name in self.index:
            var_lines.append(f"    z_{attr_name}: ZP")

        # Build constant declarations (MSP matrix entries + targets)
        const_lines = []
        const_lines.append("    z_one: ZP")
        const_lines.append("    z_zero: ZP")
        for col in range(self.width):
            for i, attr_name in enumerate(self.index):
                const_lines.append(f"    msp_{i}_{col}: ZP")

        # Build equations
        eq_lines = []

        # Column 0: sum = 1
        terms = [f"msp_{i}_0 * z_{attr}" for i, attr in enumerate(self.index)]
        eq_lines.append(f"    {' + '.join(terms)} = z_one")

        # Columns 1+: sum = 0
        for col in range(1, self.width):
            terms = [f"msp_{i}_{col} * z_{attr}" for i, attr in enumerate(self.index)]
            eq_lines.append(f"    {' + '.join(terms)} = z_zero")

        gs_string = "variables:\n"
        gs_string += "\n".join(var_lines)
        gs_string += "\n\nconstants:\n"
        gs_string += "\n".join(const_lines)
        gs_string += "\n\nequations:\n"
        gs_string += "\n".join(eq_lines)
        gs_string += "\n"

        # Build values dict
        values = {
            'z_one': ZpElement.init(1),
            'z_zero': ZpElement.init(0),
        }
        for col in range(self.width):
            for i, attr_name in enumerate(self.index):
                values[f"msp_{i}_{col}"] = self.msp[i][col]

        return gs_string, values
