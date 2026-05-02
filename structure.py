def analyze_structure(password: str) -> dict:
    return {
        "node": "Structure Analysis",
        "starts_with_digit": password[0].isdigit(),
        "ends_with_digit": password[-1].isdigit()
    }
