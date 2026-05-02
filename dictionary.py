COMMON_WORDS = {
    "password", "dragon", "welcome", "monkey", "football",
    "letmein", "shadow", "master", "killer", "superman"
}

def normalize(password: str) -> str:
    return password.lower().replace("0", "o").replace("1", "i").replace("@", "a")
