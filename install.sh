#!/bin/bash

set -e

echo "Installing USBGuard CLI Dashboard..."

if ! command -v pacman >/dev/null 2>&1; then
    echo "This installer is for Arch Linux only."
    exit 1
fi

sudo pacman -S --noconfirm usbguard usbutils python python-pip

python -m venv venv

./venv/bin/pip install --upgrade pip >/dev/null
./venv/bin/pip install rich >/dev/null

sudo systemctl enable --now usbguard

echo "Done."
echo "Run with: sudo ./venv/bin/python usbguard_cli.py"
