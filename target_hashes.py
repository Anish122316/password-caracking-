# target_hashes.py
import bcrypt

# Fake passwords we will later try to crack
passwords = ["apple123", "letmein", "Qwerty!@#", "MyStrongPass99"]

hashes = []
for pw in passwords:
    h = bcrypt.hashpw(pw.encode(), bcrypt.gensalt(12))
    hashes.append(h)

# Save hashes to a file
with open("hashes.txt", "wb") as f:
    for h in hashes:
        f.write(h + b"\n")

print("✅ Saved", len(hashes), "hashes to hashes.txt")
