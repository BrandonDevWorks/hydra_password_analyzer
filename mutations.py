from .dictionary import normalize, COMMON_WORDS

COMMON_SUFFIXES = ["1","12","123","1234","!","!!","!!!","2023","2024","2025"]

def detect_suffix(password: str):
    for s in COMMON_SUFFIXES:
        if password.endswith(s):
            return s
    return None

def detect_capitalization_trick(password: str):
    normalized = normalize(password)
    return any(normalized.startswith(w) for w in COMMON_WORDS)

def detect_symbol_swaps(password: str):
    return normalize(password) in COMMON_WORDS

def analyze_mutations(password: str) -> dict:
    suffix = detect_suffix(password)
    cap = detect_capitalization_trick(password)
    swap = detect_symbol_swaps(password)

    issues = []
    if suffix: issues.append(f"Predictable suffix detected: '{suffix}'")
    if cap: issues.append("Capitalization trick detected")
    if swap: issues.append("Symbol-swapped dictionary word detected")

    return {
        "node": "Mutation Analysis",
        "suffix": suffix,
        "capitalization_trick": cap,
        "symbol_swap": swap,
        "classification": "Clean" if not issues else "Mutation Weakness",
        "diagnostic": issues if issues else ["No mutation weaknesses detected"]
    }
