# 🔐 USBGuard CLI Dashboard

A professional Linux USB security control tool built with Python.

This project provides a clean and modern terminal-based dashboard to manage USB device access using USBGuard.

It allows users to view connected USB devices, and quickly block or allow them with a simple keyboard-driven interface.

---

## 🚀 Features

- Live USB device listing
- Block / allow USB devices instantly
- Clean terminal dashboard UI
- Fast keyboard-based control
- Color-coded device status (allowed / blocked)
- System-level USB protection via USBGuard

---
## 🚀 Quick Install & Run

```bash
git clone https://github.com/enzhyperx/USBguard.git
cd USBguard

sudo pacman -S usbguard usbutils python python-pip

python -m venv venv
./venv/bin/pip install rich

sudo systemctl enable --now usbguard

sudo ./venv/bin/python usbguard_cli.py
