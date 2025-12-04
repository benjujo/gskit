{
  description = "GSKit - Cryptographic toolkit with PBC and Charm";

  inputs = {
    nixpkgs-linux.url = "github:NixOS/nixpkgs/nixos-23.11";
    nixpkgs-darwin.url = "github:NixOS/nixpkgs/nixpkgs-23.11-darwin";
    flake-utils.url = "github:numtide/flake-utils";
    
    # PBC from GitHub as separate flake
    pbc-src = {
      url = "github:blynn/pbc";
      flake = false;
    };
    
    # Charm from GitHub
    charm-src = {
      url = "github:JHUISI/charm/dev";
      flake = false;
    };
  };

  outputs = { self, nixpkgs-linux, nixpkgs-darwin, flake-utils, pbc-src, charm-src }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs =
          let
            nixpkgsForSystem =
              if builtins.elem system [ "x86_64-darwin" "aarch64-darwin" ]
              then nixpkgs-darwin
              else nixpkgs-linux;
          in
            nixpkgsForSystem.legacyPackages.${system};
        python = pkgs.python310;

        # Build PBC library from GitHub source
        pbc = pkgs.stdenv.mkDerivation rec {
          pname = "pbc";
          version = "1.0.0";
          
          src = pbc-src;
          
          nativeBuildInputs = with pkgs; [
            autoconf
            automake
            libtool
            pkg-config
            m4
            autoconf-archive
          ];
          
          buildInputs = with pkgs; [
            gmp
            flex
            bison
          ];
          
          preConfigure = ''
            # Create m4 directory if it doesn't exist
            mkdir -p m4
            
            # Run autoreconf to generate configure script
            autoreconf -fiv
          '';
          
          configureFlags = [
            "--enable-shared"
            "--disable-static"
            "--with-pic"
          ];
          
          # Create pkg-config file
          postInstall = ''
            mkdir -p $out/lib/pkgconfig
            cat > $out/lib/pkgconfig/pbc.pc << EOF
prefix=$out
exec_prefix=\''${prefix}
libdir=\''${exec_prefix}/lib
includedir=\''${prefix}/include

Name: pbc
Description: Pairing-Based Cryptography Library
Version: ${version}
Libs: -L\''${libdir} -lpbc -lgmp
Cflags: -I\''${includedir}
EOF
          '';
          
          doCheck = false; # Skip tests for faster builds
          
          meta = with pkgs.lib; {
            description = "Pairing-Based Cryptography Library";
            homepage = "https://crypto.stanford.edu/pbc/";
            license = licenses.lgpl3;
          };
        };

        # Charm library package using our PBC
        charm = python.pkgs.buildPythonPackage rec {
          pname = "charm-crypto";
          version = "dev";
          
          src = charm-src;
          format = "other";
          
          nativeBuildInputs = with pkgs; [
            gcc
            gnumake
            pkg-config
            autoconf
            automake
            libtool
            flex
            bison
            which
            wget
          ];
          
          buildInputs = with pkgs; [
            gmp
            openssl
            pbc
          ] ++ (with python.pkgs; [
            setuptools
            wheel
            pip
          ]);
          
          propagatedBuildInputs = with python.pkgs; [
            numpy
            pyparsing
            hypothesis
          ];
          
          # Skip dependency resolution during install
          postPatch = ''
            # Remove the problematic dependency resolution
            substituteInPlace setup.py \
              --replace "install_requires=requires," "install_requires=[]," \
              --replace "dependency_links=dep_links," "dependency_links=[],"
          '';
          
          preConfigure = ''
            # Set up build environment with PBC paths
            export CC=gcc
            export CXX=g++
            export LDFLAGS="-L${pkgs.gmp}/lib -L${pkgs.openssl}/lib -L${pbc}/lib"
            export CPPFLAGS="-I${pkgs.gmp}/include -I${pkgs.openssl}/include -I${pbc}/include"
            export PKG_CONFIG_PATH="${pkgs.gmp}/lib/pkgconfig:${pkgs.openssl}/lib/pkgconfig:${pbc}/lib/pkgconfig"
            export LD_LIBRARY_PATH="${pbc}/lib:$LD_LIBRARY_PATH"
            
            # Configure Charm
            chmod +x configure.sh
            ./configure.sh --python=python3 --enable-pairing-pbc --enable-integer-gmp --disable-docs
          '';
          
          # Custom build phase since Charm uses Make + Python setup
          buildPhase = ''
            runHook preBuild
            
            # Build the C extensions using Make
            make
            
            # Then build the Python package
            python setup.py build
            
            runHook postBuild
          '';
          
          # Use standard Python install without dependency resolution
          installPhase = ''
            runHook preInstall
            
            # Install using standard setup.py without dependency resolution
            python setup.py install --prefix=$out --single-version-externally-managed --root=/
            
            runHook postInstall
          '';
          
          # Skip tests initially
          doCheck = false;
          
          meta = with pkgs.lib; {
            description = "Charm: A Framework for Rapidly Prototyping Cryptosystems";
            homepage = "https://github.com/JHUISI/charm";
            license = licenses.gpl3;
          };
        };

        # GSKit package
        gskit = python.pkgs.buildPythonPackage rec {
          pname = "gskit";
          version = "0.1.0";
          
          src = ./.;
          format = "setuptools";
          
          nativeBuildInputs = with python.pkgs; [
            setuptools
            wheel
          ];
          
          propagatedBuildInputs = with python.pkgs; [
            numpy
            lark
            charm
          ];
          
          # Make sure Charm is available during build
          preBuild = ''
            export PYTHONPATH="${charm}/${python.sitePackages}:$PYTHONPATH"
          '';
          
          # Skip tests initially
          doCheck = false;
          
          meta = with pkgs.lib; {
            description = "Groth-Sahai utilities toolkit";
            license = licenses.mit;
          };
        };

      in
      {
        # Main packages
        packages = {
          default = gskit;
          gskit = gskit;
          charm = charm;
          pbc = pbc;
        };

        # Development shell
        devShells.default = pkgs.mkShell {
          buildInputs = [
            python
          ] ++ (with pkgs; [
            gcc
            gnumake
            gmp
            openssl
            flex
            bison
            autoconf
            automake
            libtool
            pkg-config
            which
            wget
            m4
          ]) ++ (with python.pkgs; [
            numpy
            lark
            pyparsing
            setuptools
            wheel
            pip
            pytest
          ]);

          shellHook = ''
            echo "🔧 GSKit Development Environment"
            echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            echo "📦 PBC: ${pbc} (from GitHub)"
            echo "📦 Charm: ${charm} (with PBC support)"
            echo "📦 GSKit: Available for development"
            echo "🐍 Python: $(python --version)"
            echo ""
            echo "📋 Build commands:"
            echo "  • nix build .#pbc    - Build PBC library"
            echo "  • nix build .#charm  - Build Charm library"
            echo "  • nix build .#gskit  - Build GSKit (default)"
            echo "  • nix build          - Build everything"
            echo ""
            echo "🧪 Test installation:"
            echo "  • python -c 'from charm.toolbox.pairinggroup import PairingGroup; print(\"Charm works!\")'"
            echo "  • python -c 'import gskit; print(\"GSKit works!\")'"
            echo ""
            echo "🛠️  Development workflow:"
            echo "  1. Edit code"
            echo "  2. nix develop (you're here)"
            echo "  3. python -m pip install -e . (for live development)"
            echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            
            # Set up environment for PBC and Charm libraries
            export LD_LIBRARY_PATH="${pbc}/lib:$LD_LIBRARY_PATH"
            export C_INCLUDE_PATH="${pbc}/include:$C_INCLUDE_PATH"
            export PKG_CONFIG_PATH="${pbc}/lib/pkgconfig:$PKG_CONFIG_PATH"
            
            if [ -n "${charm}" ]; then
              export PYTHONPATH="${charm}/${python.sitePackages}:$PYTHONPATH"
              export LD_LIBRARY_PATH="${charm}/${python.sitePackages}/charm/core:$LD_LIBRARY_PATH"
            fi
          '';
        };

        # Apps for easy execution
        apps = {
          default = flake-utils.lib.mkApp {
            drv = gskit;
            exePath = "/bin/gskit";
          };
        };
      });
}