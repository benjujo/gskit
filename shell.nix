{ pkgs ? import <nixpkgs> {} }:

let
  python310 = pkgs.python310;
  pythonEnv = python310.withPackages (ps: with ps; [
    numpy
    pip
    setuptools
    wheel
    # Add lark explicitly
    lark
    # From charm requirements
    (pyparsing.overridePythonAttrs (old: { version = "2.1.5"; }))
    hypothesis
    pytest
  ]);
in
pkgs.mkShell {
  buildInputs = [
    # Python environment
    pythonEnv
    
    # System dependencies
    pkgs.gmp
    pkgs.openssl
    pkgs.flex
    pkgs.bison
    
    # Build tools
    pkgs.gcc
    pkgs.gnumake
    pkgs.autoconf
    pkgs.automake
    pkgs.libtool
    pkgs.pkg-config
  ];

  shellHook = ''
    # Set Python to 3.10
    export PYTHONPATH=${pythonEnv}/${python310.sitePackages}:$PYTHONPATH
    
    # Create local directories for installation without sudo
    mkdir -p $HOME/.local/lib
    mkdir -p $HOME/.local/include
    mkdir -p $HOME/.local/lib/python3.10/site-packages
    
    # Build and install charm without sudo
    buildCharm() {
      # Navigate to charm directory
      cd charm
      
      # Install requirements
      python -m pip install -r requirements.txt --user
      
      # Configure charm with local prefix to avoid sudo
      ./configure.sh --prefix=$HOME/.local
      
      # Patch any Makefiles that might be using sudo
      # This is a common fix for sudo in Makefiles
      find . -name "Makefile" -exec sed -i 's/sudo //g' {} \;
      
      # For pbc specifically - we need to build it without trying to use sudo
      cd deps/pbc
      
      # If the Makefile tries to use sudo for the PBC build, we need to handle that
      # Check if pbc-0.5.14 directory exists, and if it doesn't, extract it
      if [ ! -d "pbc-0.5.14" ] && [ -f "pbc-0.5.14.tar.gz" ]; then
        tar xzf pbc-0.5.14.tar.gz
      fi
      
      if [ -d "pbc-0.5.14" ]; then
        # Go into the PBC directory and build manually
        cd pbc-0.5.14
        ./configure --prefix=$HOME/.local
        make
        make install PREFIX=$HOME/.local
        cd ..
        # Create .built file manually to mark as built
        touch pbc-0.5.14/.built
      else
        # Otherwise build in the current directory
        ./configure --prefix=$HOME/.local
        make
        # Manual installation to avoid sudo
        find . -name "*.h" -exec cp {} $HOME/.local/include/ \;
        find . -name "*.so*" -exec cp {} $HOME/.local/lib/ \;
        find . -name "*.a" -exec cp {} $HOME/.local/lib/ \;
      fi
      
      # Return to charm root
      cd ../..
      
      # Build charm
      make
      
      # Manually install charm instead of using make install
      SITE_PACKAGES=$HOME/.local/lib/python3.10/site-packages
      mkdir -p $SITE_PACKAGES
      
      # Find and copy charm Python package
      if [ -d "charm" ]; then
        cp -r charm $SITE_PACKAGES/
      fi
      
      # Find and copy any relevant libraries
      find . -name "*.so*" -exec cp {} $HOME/.local/lib/ \;
      
      # Return to original directory
      cd ..
      
      echo "Charm has been built and installed to $HOME/.local"
      echo "Make sure to add $HOME/.local/lib to your LD_LIBRARY_PATH"
    }
    
    # Set up environment variables for local installation
    export LD_LIBRARY_PATH=$HOME/.local/lib:$LD_LIBRARY_PATH
    export LIBRARY_PATH=$HOME/.local/lib:$LIBRARY_PATH
    export C_INCLUDE_PATH=$HOME/.local/include:$C_INCLUDE_PATH
    export CPLUS_INCLUDE_PATH=$HOME/.local/include:$CPLUS_INCLUDE_PATH
    export PYTHONPATH=$HOME/.local/lib/python3.10/site-packages:$PYTHONPATH
    export PATH=$HOME/.local/bin:$PATH
    
    # Print help message
    echo "Nix development shell for gskit with Python 3.10"
    echo "Run 'buildCharm' to build and install the charm library"
  '';

  # Make sure we use Python 3.10
  PYTHON = "${pythonEnv}/bin/python";
}