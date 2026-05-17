#!/bin/bash

set -e

echo "======================================"
echo " USBGuard CLI Dashboard Installer"
echo "======================================"

# Detect OS (basic safety check)
if ! command -v pacman &> /dev/null; then
    echo "[ERROR] This installer is designed for Arch Linux."
    exit 1
fi

echo "[1/4] Installing system dependencies..."

sudo pacman -S --noconfirm usbguard usbutils python python-pip

echo "[2/4] Installing Python dependencies..."

pip install --user rich

echo "[3/4] Enabling USBGuard service..."

sudo systemctl enable --now usbguard

echo "[4/4] Setting permissions..."

chmod +x usbguard_cli.py

echo ""
echo "======================================"
echo " Installation complete!"
echo "======================================"
echo ""
echo "Run the tool with:"
echo "  sudo python usbguard_cli.py"
echo ""
echo "Or:"
echo "  sudo ./usbguard_cli.py"
echo ""
echo "GitHub: https://github.com/enzohyperx"
echo "======================================"
