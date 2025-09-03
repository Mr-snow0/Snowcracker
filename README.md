 # ❄️ SnowCracker

![Python](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)

**SnowCracker** is a professional CLI tool to hash passwords and crack hashes using wordlists.  
Created by **Mr Snow**, Cybersecurity Enthusiast.  

---

## 🚀 Features
- 🔑 Hash passwords (**MD5, SHA1, SHA256, SHA512**)  
- 🛠 Crack hashes with wordlists (**rockyou.txt support**)  
- 🎨 Colored output for better readability  
- ⏳ Progress bar & spinner during cracking  
- 🖐 Graceful **Ctrl+C** handling  
- 🤖 Auto-detect hash type  
- 💻 Professional and easy-to-use CLI interface  

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Mr-Snow0/Snowcracker.git
cd Snowcracker
```

Make the installer executable and run it:

chmod +x install.sh
./install.sh

    ⚠️ Note: Default wordlist rockyou.txt is not included due to GitHub size limits.
    You can download it from SecLists

    and place it in wordlists/.

▶️ Usage

After installation, run the tool:

snowcracker

You will see the interactive menu:

    Hash a password – enter a password to get MD5, SHA1, SHA256, SHA512 hashes

    Crack a hash using a wordlist – provide a hash and a wordlist to try to recover the plaintext

    Exit – quit the program

    💡 Tip: Keep your wordlists in the wordlists/ folder for easy access.

📜 License

This project is licensed under the MIT License

.
🤝 Contributing

Contributions are welcome! Feel free to:

    Open issues for bugs or feature requests

    Submit pull requests for improvements

📢 Support & Share

If you enjoy using SnowCracker, give it a ⭐ on GitHub and share it with friends and colleagues!

