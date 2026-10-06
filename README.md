# 🔑 Optimized Password Cracker

## Overview

**Optimized Password Cracker** is a Python educational project that demonstrates how bcrypt-hashed passwords can be checked against candidate guesses (wordlists). It illustrates hashing, verification, and simple optimizations (progress reporting and multithreading) for learning and defensive security research.

**Disclaimer:** This repository is for educational and authorized testing only. Do **not** use this tool for unauthorized access or malicious activity.

---

## Features

* Loads bcrypt hashes from `hashes.txt`.
* Tests candidate passwords from `wordlist.txt`.
* Shows realtime progress with `tqdm`.
* Optionally uses multithreading to speed up cracking.
* Writes found passwords to `results.txt`.
* Includes `target_hashes.py` to generate sample bcrypt hashes for testing.

---

## Project structure

```
optimized-password-cracker/
│
├─ cracker.py            # Main cracker (supports wordlist, logging, timer, multithreading)
├─ target_hashes.py      # Generates sample bcrypt hashes into hashes.txt
├─ hashes.txt            # Input: one bcrypt hash per line
├─ wordlist.txt          # Input: one password guess per line
├─ results.txt           # Output: cracked passwords (created by cracker.py)
├─ requirements.txt      # Python dependencies (bcrypt, tqdm, colorama)
├─ .gitignore            # Should include: venv/
└─ venv/                 # (optional local virtual environment — not included in repo)
```

---

## Quick Start (Windows — step by step)

1. Open PowerShell and go to the project folder:

   ```powershell
   cd "C:\Users\<YourUser>\OneDrive\Desktop\optimized password cracker"
   ```

2. (If you don't have a venv here) Create and activate a virtual environment:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

   If you don't have `requirements.txt`, install manually:

   ```powershell
   pip install bcrypt tqdm colorama
   ```

4. (Optional) Generate sample hashes:

   ```powershell
   python target_hashes.py
   ```

   This will create/overwrite `hashes.txt` with sample bcrypt hashes.

5. Run the cracker:

   ```powershell
   python cracker.py
   ```

6. View cracked results:

   ```powershell
   type .\results.txt
   ```

---

## How it works (brief)

* `target_hashes.py` hashes example plaintext passwords with bcrypt and writes them to `hashes.txt`.
* `cracker.py` reads `hashes.txt` and `wordlist.txt`, then for each candidate guess it calls `bcrypt.checkpw()` to test matches.
* Matched passwords are printed and appended to `results.txt`. The script also measures runtime and can use multithreading for faster performance on large wordlists.

---

## Recommendations & best practices

* Use **strong, unique** passwords and a password manager — bcrypt slows attacks, but weak passwords are still vulnerable.
* For experiments use **your own** generated hashes (via `target_hashes.py`) only.
* Do **not** upload real users' hashes or use this on systems you do not own/authorize.

---

## Recreating the environment (for others)

After cloning:

```bash
python -m venv venv
# Windows
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python cracker.py
```

---

## Author & License

**Author:** Dipali Rawat
