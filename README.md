# GSKit

**Groth-Sahai Proof System Toolkit** - A Python framework for generating and verifying Groth-Sahai proofs using pairing-based cryptography.

Tested on `x86_64` and `aarch64` architectures.

## Quick Start

### Recommended: Nix Flakes (Clean & Reproducible)

The **cleanest and most reproducible** way to use GSKit is with Nix flakes. All dependencies (PBC, Charm, Python packages) are automatically managed.

**Prerequisites:**
- Nix with flakes enabled ([Install Nix](https://nixos.org/download.html))

**Usage:**

```bash
# Clone the repository
git clone <your-repo-url>
cd gskit

# Enter development environment (first time will build everything)
nix develop

# Inside the shell, install GSKit for development
python -m pip install -e .

# Test that everything works
python -c "from charm.toolbox.pairinggroup import PairingGroup; print('✓ Charm works!')"
python -c "import gskit; print('✓ GSKit works!')"

# Run your scripts
python src/bls_gsfy.py
```

**Build standalone packages:**
```bash
# Build everything (GSKit + dependencies)
nix build

# Build specific packages
nix build '.#pbc'    # PBC library v1.0.0
nix build '.#charm'  # Charm with PBC support
nix build '.#gskit'  # GSKit package
```

---

### Alternative: Docker (For Docker Users)

If you prefer Docker or can't use Nix, the Docker setup is still available.

**Prerequisites:**
- Docker and Docker Compose installed
- Git submodules initialized

**Setup:**

```bash
# Clone and initialize submodules
git clone <your-repo-url>
cd gskit
git submodule update --init --recursive

# Build and start the container
docker-compose up -d

# Enter the container
docker exec -it gskit bash

# Inside the container, run your scripts
python /src/bls_gsfy.py
```

**Note:** The `src/` folder is mounted as a volume, so you can edit files on your host and run them in the container without rebuilding.

**Dockerfile details:**
- Base: Ubuntu 22.04
- Python: 3.7
- Builds Charm from submodule with PBC support
- Installs GSKit package

---

## Usage Examples

### Example: BLS Signature Verification

```python
from charm.toolbox.pairinggroup import PairingGroup
from gskit import GSProof

# Initialize pairing group
group = PairingGroup('SS512')

# Your proof logic here...
```

See `src/bls_gsfy.py` for a complete example.

---

## References

- [PBC Library](https://crypto.stanford.edu/pbc/)
- [Charm-Crypto](https://github.com/JHUISI/charm)
- [Groth-Sahai Proofs Paper](https://eprint.iacr.org/2007/155)
- [Nix Flakes](https://nixos.wiki/wiki/Flakes)
