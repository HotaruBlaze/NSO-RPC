#!/bin/bash

# Navigate to the client directory
cd ../client

# Create a temporary Python script to discover usable PyQt modules.
temp_dir=$(mktemp -d -t nso-rpc-XXXXXXXXXX)
temp_script="$temp_dir/temp.py"

cat <<EOL > "$temp_script"
import sys
PYQT_PACKAGE = ''
try:
    from PyQt6.QtWidgets import QApplication
    PYQT_PACKAGE = 'PyQt6'
except ImportError:
    try:
        from PyQt5.QtWidgets import QApplication
        PYQT_PACKAGE = 'PyQt5'
    except ImportError:
        print('PyQt6 or PyQt5 is required. Please install either of them.', file=sys.stderr)
        sys.exit(1)
print(PYQT_PACKAGE)
EOL

PYQT_PACKAGE=$(python "$temp_script")
rm -rf "$temp_dir"

# Check if PyQt package is set
if [ -z "$PYQT_PACKAGE" ]; then
    exit 1
fi
echo "Building with $PYQT_PACKAGE"

# Install requirements
pip install -r ../client/requirements.txt GitPython pyinstaller>=6.6.0 pyinstaller-hooks-contrib==2024.6

# Generate version.txt
python _version.py

# Build the executable using PyInstaller
pyinstaller --onefile --clean --noconsole --exclude-module autopep8 --noupx --add-data "*.png:." --add-data "version.txt:." --icon=icon.ico --name=NSO-RPC ../client/app.py