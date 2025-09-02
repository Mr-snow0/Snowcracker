#!/usr/bin/env python3
import hashlib
import sys
import time
import random
import os
import tempfile

# ----------------- COLORS -----------------
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
RESET = "\033[0m"
BOLD = "\033[1m"

# ----------------- BANNER -----------------
banner = f"""
{CYAN}{BOLD}
   _____ _   _  ___  __        __            _               
  / ____| \ | |/ _ \ \ \      / /           | |              
 | (___ |  \| | | | | \ \ /\ / /__  _ __ ___| |__   ___ _ __ 
  \___ \| . ` | | | |  \ V  V / _ \| '__/ __| '_ \ / _ \ '__|
  ____) | |\  | |_| |   \_/\_/ (_) | | | (__| | | |  __/ |   
 |_____/|_| \_|\___/             |_|  \___|_| |_|\___|_|   
{RESET}
{YELLOW}SnowCracker - Created by Mr snow | Cybersecurity Enthusiast{RESET}
"""

# ----------------- DEFAULT WORDLIST -----------------
DEFAULT_WORDLIST = "rockyou.txt"  # place rockyou.txt in the same folder
TOP_PASSWORDS = [
    "123456", "password", "123456789", "12345678", "12345",
    "qwerty", "abc123", "111111", "123123", "admin"
]

# ----------------- SNOW BANNER EFFECT -----------------
def snow_banner(banner):
    os.system("clear")
    cols = 50
    for _ in range(10):
        snow_line = "".join(random.choice([" ", "*"]) for _ in range(cols))
        print(snow_line)
        time.sleep(0.05)
    print(banner)

# ----------------- HASH FUNCTIONS -----------------
def hash_password(password):
    return {
        "MD5": hashlib.md5(password.encode()).hexdigest(),
        "SHA1": hashlib.sha1(password.encode()).hexdigest(),
        "SHA256": hashlib.sha256(password.encode()).hexdigest(),
        "SHA512": hashlib.sha512(password.encode()).hexdigest()
    }

# ----------------- SNOW SPINNER -----------------
def snow_spinner():
    while True:
        for cursor in '|/-\\':
            snow = "*" if random.random() < 0.1 else " "
            yield f"{cursor}{snow}"

spin = snow_spinner()

# ----------------- HASH TYPE DETECTION -----------------
def detect_hash_type(hash_value):
    length = len(hash_value)
    if length == 32:
        return "MD5"
    elif length == 40:
        return "SHA1"
    elif length == 64:
        return "SHA256"
    elif length == 128:
        return "SHA512"
    else:
        return "Unknown"

# ----------------- HASH VALIDATION -----------------
def is_valid_hash(hash_value):
    hash_value = hash_value.lower().strip()
    if all(c in "0123456789abcdef" for c in hash_value):
        if len(hash_value) in [32, 40, 64, 128]:
            return True
    return False

# ----------------- COUNT WORDS -----------------
def count_words_in_wordlists(wordlist_paths):
    wordlists = [w.strip() for w in wordlist_paths.split(",")]
    total = 0
    for path in wordlists:
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                total += sum(1 for _ in f)
        except FileNotFoundError:
            pass
    return total

# ----------------- USE FALLBACK PASSWORDS -----------------
def use_default_passwords():
    temp = tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8")
    for pwd in TOP_PASSWORDS:
        temp.write(pwd + "\n")
    temp.close()
    return temp.name

# ----------------- CRACK FUNCTION -----------------
def crack_hash(hash_value, wordlist_paths):
    wordlists = [w.strip() for w in wordlist_paths.split(",")]
    total_words = count_words_in_wordlists(wordlist_paths)
    if total_words == 0:
        total_words = len(TOP_PASSWORDS)
    checked = 0

    try:
        for path in wordlists:
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                for word in file:
                    word = word.strip()
                    checked += 1
                    percent = (checked / total_words) * 100
                    sys.stdout.write(f"\r{YELLOW}[{percent:6.2f}%] Checking: {word} {next(spin)}{RESET}")
                    sys.stdout.flush()
                    time.sleep(0.005)

                    # check all hashes
                    if hashlib.md5(word.encode()).hexdigest() == hash_value:
                        sys.stdout.write("\r" + " " * 80 + "\r")
                        return word, "MD5"
                    if hashlib.sha1(word.encode()).hexdigest() == hash_value:
                        sys.stdout.write("\r" + " " * 80 + "\r")
                        return word, "SHA1"
                    if hashlib.sha256(word.encode()).hexdigest() == hash_value:
                        sys.stdout.write("\r" + " " * 80 + "\r")
                        return word, "SHA256"
                    if hashlib.sha512(word.encode()).hexdigest() == hash_value:
                        sys.stdout.write("\r" + " " * 80 + "\r")
                        return word, "SHA512"
        sys.stdout.write("\r" + " " * 80 + "\r")
        return None, None
    except FileNotFoundError as e:
        print(f"{RED}[-] Wordlist not found: {e.filename}{RESET}")
        return None, None

# ----------------- MAIN -----------------
def main():
    snow_banner(banner)
    try:
        while True:
            print(f"{GREEN}1.{RESET} Hash a password")
            print(f"{GREEN}2.{RESET} Crack a hash using a wordlist")
            print(f"{GREEN}3.{RESET} Exit")
            choice = input(f"{YELLOW}Choose an option: {RESET}")

            if choice == "1":
                password = input(f"{CYAN}Enter password to hash: {RESET}")
                results = hash_password(password)
                print(f"\n{MAGENTA}Hashes for '{password}':{RESET}")
                for algo, value in results.items():
                    print(f"{CYAN}[+] {algo}: {value}{RESET}")

            elif choice == "2":
                hash_value = input(f"{CYAN}Enter the hash to crack: {RESET}").strip()
                if not is_valid_hash(hash_value):
                    print(f"{RED}[-] Invalid hash entered! Make sure it is MD5, SHA1, SHA256, or SHA512.{RESET}")
                    continue

                hash_type = detect_hash_type(hash_value)
                print(f"{YELLOW}[i] Detected hash type: {hash_type}{RESET}")

                wordlist_input = input(f"{CYAN}Enter path to wordlist(s) (comma-separated, Enter for default): {RESET}")
                if wordlist_input.strip():
                    wordlist_paths = wordlist_input
                else:
                    if os.path.exists(DEFAULT_WORDLIST):
                        wordlist_paths = DEFAULT_WORDLIST
                    else:
                        wordlist_paths = use_default_passwords()

                result, algo = crack_hash(hash_value, wordlist_paths)
                if result:
                    if algo == "MD5":
                        color = CYAN
                    elif algo == "SHA1":
                        color = MAGENTA
                    elif algo == "SHA256":
                        color = GREEN
                    elif algo == "SHA512":
                        color = BLUE
                    print(f"{color}[+] Found! Hash matches '{result}' using {algo}{RESET}")
                else:
                    print(f"{RED}[-] No match found in wordlist.{RESET}")

            elif choice == "3":
                print(f"{YELLOW}Exiting SnowCracker. Stay frosty! ❄{RESET}")
                break
            else:
                print(f"{RED}[!] Invalid choice, try again.{RESET}")

    except KeyboardInterrupt:
        print(f"\n{YELLOW}[*] Exiting SnowCracker gracefully. Stay frosty! ❄{RESET}")
        sys.exit(0)

if __name__ == "__main__":
    main()
