#!/bin/bash
#
# NSO-RPC Install Script
# This should work with Ubuntu/Debian, Fedora and Arch Linux out of the box 
# Github: https://github.com/MCMi460/NSO-RPC
#


GREEN="\e[32;1m"
YELLOW="\e[33m"
RED="\e[31m"
RESET="\e[0m"

# Check if running as root
if [ "$(id -u)" != "0" ]; then
    echo "This script must be run as root."
    exit 1
fi

# Define the package managers to check
PACKAGE_MANAGERS=("apt-get" "dnf" "yum")

# Function to check if a package is installed
function is_package_installed {
    if [ -n "$(command -v $1)" ]; then
        return 0
    else
        return 1
    fi
}

# Set the package manager command based on availability
for pkg_manager in "${PACKAGE_MANAGERS[@]}"; do
    if command -v "$pkg_manager" &>/dev/null; then
        PACKAGE_MANAGER="$pkg_manager"
        break
    fi
done

# If no package manager found, exit
if [ -z "$PACKAGE_MANAGER" ]; then
    echo -e "${RED}[NSO-RPC: Installer] Unable to determine the package manager.${RESET}"
    echo -e "${RED}[NSO-RPC: Installer]Please install the required packages manually.${RESET}"
    exit 1
fi

echo -e "${YELLOW}[NSO-RPC: Installer] Using $PACKAGE_MANAGER package manager.${RESET}"

# Check if pip is installed
if ! is_package_installed pip; then
    $PACKAGE_MANAGER install -y python3-pip
fi

# Function to check if Qt is installed
function is_qt_installed {
    if $PACKAGE_MANAGER list --installed | grep -q "^qt5"; then
        return 0
    elif $PACKAGE_MANAGER list --installed | grep -q "^qt6"; then
        return 0
    else
        return 1
    fi
}

# Check if Qt5 or Qt6 is installed
if ! is_qt_installed; then
    if is_package_installed qt5-base; then
        $PACKAGE_MANAGER install -y python3-pyqt5
    elif is_package_installed qt6-base; then
        $PACKAGE_MANAGER install -y python3-pyqt6
    else
        echo -e "${RED}[NSO-RPC: Installer] Qt5 or Qt6 libraries are not found. Please install them manually.${RESET}"
        exit 1
    fi
fi

cd ../client
python3 -m pip install -r requirements.txt
executableDir='/opt/NSO-RPC/'

# Check if installation directory already exists
if [ -d "$executableDir" ]; then
    echo "[NSO-RPC: Installer]: Installation directory already exists. Removing existing directory..."
    sudo rm -r "$executableDir"
fi

# Create the installation directory
sudo mkdir -p "$executableDir"

# Copy files to the installation directory
sudo cp -a './' "$executableDir"

# Begin creating .desktop alias
execDir='/usr/share/applications'
execFile="$execDir/nsorpc.desktop"
mkdir -p "$execDir"
sudo touch "$execFile"

iconDir='/usr/share/pixmaps'
mkdir -p "$iconDir"

sudo cp './icon.svg' "$iconDir/nso.svg"

read -r -d '' content <<EOF
[Desktop Entry]
Type=Application
Name=Nintendo Switch Online Rich Presence
GenericName=NSO-RPC
Comment=Display your Nintendo Switch game status on Discord!
Exec=bash -c 'cd /opt/NSO-RPC && python3 app.py'
Icon=nso.svg
Terminal=false
Categories=Game;Application;Utility;
EOF

echo "$content" | sudo tee "$execFile" > /dev/null
sudo chmod +x "$execFile"
echo -e "${GREEN}Script finished executing successfully.${RESET}"
