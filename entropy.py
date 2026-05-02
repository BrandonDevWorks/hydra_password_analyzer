import math

def analyze_entropy(password: str) -> dict:
    length = len(password)
    charset = 0

    if any(c.islower() for c in password): charset += 26
    if any(c.isupper() for c in password): charset += 26
    if any(c.isdigit() for c in password): charset += 10
    if any(not c.isalnum() for c in password): charset += 32

    entropy = length * math.log2(charset) if charset else 0

    return {
        "node": "Entropy Analysis",
        "length": length,
        "charset_size": charset,
        "entropy_bits": round(entropy, 2)
    }
