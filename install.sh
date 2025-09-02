#!/bin/bash

# SnowCracker installer
echo "[*] Installing SnowCracker..."

# Make the main script executable
chmod +x snowcracker.py

# Check for rockyou.txt in wordlists folder
if [ ! -f "wordlists/rockyou.txt" ]; then
    echo "[!] Default wordlist rockyou.txt not found in wordlists/"
    echo "[*] You can download it from https://github.com/danielmiessler/SecLists"
fi

# Ask for global or local installation
echo "[*] Do you want to install SnowCracker globally? (y/n)"
read install_global

if [[ "$install_global" == "y" || "$install_global" == "Y" ]]; then
    if [ "$EUID" -ne 0 ]; then
        echo "[!] Global installation requires sudo privileges. Please run: sudo ./install.sh"
        exit 1
    fi
    echo "[*] Installing globally in /usr/local/bin"
    cp snowcracker.py /usr/local/bin/snowcracker
else
    echo "[*] Installing locally in ~/bin"
    mkdir -p ~/bin
    cp snowcracker.py ~/bin/snowcracker
    # Ensure ~/bin is in PATH
    if ! grep -q 'export PATH=$PATH:~/bin' ~/.bashrc; then
        echo 'export PATH=$PATH:~/bin' >> ~/.bashrc
        source ~/.bashrc
    fi
fi

echo "[+] Installation complete! Run SnowCracker with: snowcracker"
