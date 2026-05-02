def analyze_patterns(password: str) -> dict:
    repeats = any(password[i] == password[i-1] for i in range(1, len(password)))

    return {
        "node": "Pattern Analysis",
        "repeated_characters": repeats
    }
