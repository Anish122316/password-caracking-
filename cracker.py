# cracker.py
import bcrypt
from tqdm import tqdm
import time

# Load target hashes from file
with open("hashes.txt", "r") as f:
    target_hashes = [line.strip() for line in f]

# Load wordlist from file
with open("wordlist.txt", "r") as f:
    wordlist = [line.strip() for line in f]

print("🔑 Starting password cracking...\n")

# Start timer
start_time = time.time()

# Open results file (UTF-8 encoding to support emojis)
with open("results.txt", "w", encoding="utf-8") as results:
    for guess in tqdm(wordlist, desc="Trying passwords"):
        guess_bytes = guess.encode()
        for th in target_hashes:
            if bcrypt.checkpw(guess_bytes, th.encode()):
                msg = f"✅ Password found: {guess}"
                print(msg)
                results.write(msg + "\n")

# End timer
end_time = time.time()
print(f"\n⏱️ Cracking finished in {end_time - start_time:.2f} seconds")
print("📄 Results saved to results.txt")
