from .dictionary import normalize, COMMON_WORDS

def analyze_semantics(password: str) -> dict:
    normalized = normalize(password)
    contains_word = any(w in normalized for w in COMMON_WORDS)

    return {
        "node": "Semantic Analysis",
        "dictionary_word_detected": contains_word
    }
