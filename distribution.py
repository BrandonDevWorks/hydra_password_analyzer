def analyze_distribution(password: str) -> dict:
    digits = sum(c.isdigit() for c in password)
    lowers = sum(c.islower() for c in password)
    uppers = sum(c.isupper() for c in password)
    symbols = sum(not c.isalnum() for c in password)

    return {
        "node": "Distribution Analysis",
        "lowercase": lowers,
        "uppercase": uppers,
        "digits": digits,
        "symbols": symbols
    }
