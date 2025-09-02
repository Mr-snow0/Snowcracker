 #!/usr/bin/env bash

# SnowCracker installer
echo "[*] Installing SnowCracker..."

# Ensure Python is installed
if ! command -v python3 >/dev/null 2>&1; then
    echo "[!] Python3 is not installed. Please install it before using SnowCracker."
    exit 1
fi

# Make the main script executable
chmod +x snowcracker.py

# Check for rockyou.txt in wordlists folder
if [ ! -f "wordlists/rockyou.txt" ]; then
    echo "[!] Default wordlist rockyou.txt not found in wordlists/"
    echo "[*] On Kali Linux, you can extract it with:"
    echo "    sudo gunzip /usr/share/wordlists/rockyou.txt.gz -c > wordlists/rockyou.txt"
    echo "[*] Or download more from: https://github.com/danielmiessler/SecLists"
fi

# Ask for global or local installation
echo "[*] Do you want to install SnowCracker globally? (y/n)"
read -r install_global

if [[ "$install_global" =~ ^[Yy]$ ]]; then
    if [ "$EUID" -ne 0 ]; then
        echo "[!] Global installation requires sudo privileges."
        echo "    Please run again with: sudo ./install.sh"
        exit 1
    fi
    echo "[*] Installing globally in /usr/local/bin"
    cp snowcracker.py /usr/local/bin/snowcracker
    chmod +x /usr/local/bin/snowcracker
else
    echo "[*] Installing locally in ~/bin"
    mkdir -p ~/bin
    cp snowcracker.py ~/bin/snowcracker
    chmod +x ~/bin/snowcracker
    # Ensure ~/bin is in PATH
    if ! grep -q 'export PATH=.*~/bin' ~/.bashrc; then
        echo 'export PATH=$PATH:~/bin' >> ~/.bashrc
    fi
    source ~/.bashrc
fi

echo "[+] Installation complete! Run SnowCracker with: snowcracker"
