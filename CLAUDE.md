# CLAUDE.md - GSKit

## Project Overview

GSKit (Groth-Sahai Proof System Toolkit) is a Python framework for generating and verifying Groth-Sahai (GS) cryptographic zero-knowledge proofs using pairing-based cryptography. It provides a DSL for specifying proofs and compiles them to executable Python code.

## Build & Development

### Prerequisites

**Recommended: Nix Flakes**
```bash
nix develop              # Enter development shell with all dependencies
python -m pip install -e .  # Install GSKit in editable mode
```

**Alternative: Docker**
```bash
docker-compose up -d
docker exec -it gskit bash
```

### Testing

```bash
python test.py           # Basic test
pytest                   # Full test suite

# Verify installation
python -c "from charm.toolbox.pairinggroup import PairingGroup; print('Charm works')"
python -c "import gskit; print('GSKit works')"
```

### CLI Usage

```bash
gskit crs -t sound -c crs.json              # Generate CRS (sound or wi)
gskit prove -i proof.gs -d defs.json -c crs.json -o proof.py
gskit verify -i proof.gs -d defs.json -c crs.json -o verify.py
```

## Architecture

### Core Modules

| File | Purpose |
|------|---------|
| `elements.py` | Cryptographic element wrappers (Zp, G1, G2, GT) |
| `framework.py` | CRS, equation types, proof compilation |
| `gsfy.py` | `@gsfy` decorator for embedded proof generation |
| `gs_context.py` | Context for modular multi-function proofs |
| `parser.py` + `ast_builder.py` | DSL parsing |
| `nodes.py` | AST node definitions |
| `grammar.lark` | Lark grammar for GS DSL |

### Element Types

- **Zp**: Scalar field elements
- **G1, G2**: Elliptic curve groups (additive notation)
- **GT**: Target group (pairing output)

### Equation Types

| Type | Name | Operation |
|------|------|-----------|
| 0 | QE (Quadratic) | `Zp * Zp = Zp` |
| 1 | MS1 | `G1 * Zp = G1` |
| 2 | MS2 | `G2 * Zp = G2` |
| 3 | PPE (Pairing Product) | `e(G1, G2) = GT` |

## Key Patterns

### DSL Syntax (GS_STRING)

```
variables:
    signature: G1

constants:
    g2: G2
    rhs: GT

equations:
    signature * g2 = rhs
```

### @gsfy Decorator

```python
from gskit.gsfy import gsfy

@gsfy(witness=['signature'])
def verify(self, vk, m, signature):
    GS_STRING = """
    variables:
        signature: G1
    constants:
        g2: G2
        rhs: GT
    equations:
        signature * g2 = rhs
    """
    return lhs == rhs
```

- `witness=[]` specifies hidden variables
- `GS_STRING` contains the DSL specification
- Function body provides runtime implementation

### CRS (Common Reference String)

```python
from gskit.framework import CRS

crs = CRS.new_sound()  # For general proofs
crs = CRS.new_wi()     # For privacy (witness indistinguishability)
```

## Dependencies

- **Charm-Crypto** (git submodule): Pairing-based cryptography
- **PBC Library**: Underlying C library for pairings (BN254 curve)
- **NumPy**: Array operations on cryptographic elements
- **Lark**: Parser generator for DSL

## File Locations

- Main package: `gskit/`
- Examples: `gskit/examples/` (BLS signature, ABSUCL attribute-based signatures)
- Generated output: `src/`
- Charm submodule: `charm/`

## Notes

- Uses additive notation for group operations throughout
- All elements JSON-serializable via custom `ElementEncoder`
- Supports x86_64 and aarch64 architectures
- macOS (Darwin) and Linux supported via Nix Flakes
