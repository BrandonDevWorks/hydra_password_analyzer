from hydra.fusion import hydra_analyze

# -----------------------------
# HYDRA OUTPUT FORMATTERS
# -----------------------------

def format_report(result, password):
    return f"""
==============================
 HYDRA PASSWORD ANALYSIS
==============================

Password: {password}

[1] Entropy Analysis
    • Length: {result['entropy']['length']} characters
    • Character Set Size: {result['entropy']['charset_size']}
    • Estimated Entropy: {result['entropy']['entropy_bits']} bits

[2] Character Distribution
    • Lowercase: {result['distribution']['lowercase']}
    • Uppercase: {result['distribution']['uppercase']}
    • Digits: {result['distribution']['digits']}
    • Symbols: {result['distribution']['symbols']}

[3] Mutation Analysis
    • Capitalization Trick: {result['mutations']['capitalization_trick']}
    • Common Suffix: {result['mutations']['suffix']}
    • Symbol Swap: {result['mutations']['symbol_swap']}
    • Classification: {result['mutations']['classification']}
    • Notes: {", ".join(result['mutations']['diagnostic'])}

[4] Pattern Analysis
    • Repeated Characters: {result['patterns']['repeated_characters']}

[5] Semantic Analysis
    • Dictionary Word Detected: {result['semantics']['dictionary_word_detected']}

[6] Structural Analysis
    • Starts With Digit: {result['structure']['starts_with_digit']}
    • Ends With Digit: {result['structure']['ends_with_digit']}
"""


def format_json(result):
    import json
    return json.dumps(result, indent=4)


def calculate_score(result):
    score = 0

    # Length
    if result['entropy']['length'] >= 12:
        score += 25
    elif result['entropy']['length'] >= 8:
        score += 15
    else:
        score += 5

    # Character diversity
    dist = result['distribution']
    diversity = sum([
        dist['lowercase'] > 0,
        dist['uppercase'] > 0,
        dist['digits'] > 0,
        dist['symbols'] > 0
    ])
    score += diversity * 10

    # Penalties
    if result['semantics']['dictionary_word_detected']:
        score -= 15
    if result['mutations']['capitalization_trick']:
        score -= 10

    score = max(0, min(score, 100))

    if score >= 80:
        level = "Strong"
    elif score >= 60:
        level = "Moderate"
    else:
        level = "Weak"

    return score, level


def format_score(result, password):
    score, level = calculate_score(result)
    return f"""
HYDRA SCORE: {score} / 100
Strength Level: {level}

Key Findings:
• Dictionary Word: {result['semantics']['dictionary_word_detected']}
• Capitalization Trick: {result['mutations']['capitalization_trick']}
• Symbols Used: {result['distribution']['symbols']}
• Length: {result['entropy']['length']}

Recommendations:
• Add symbols
• Avoid dictionary words
• Mix uppercase throughout
• Add random characters
"""


# -----------------------------
# HYDRA SUGGESTION ENGINE
# -----------------------------

def generate_suggestions(password):
    import random
    import string

    # Stronger variants (same theme)
    stronger = [
        password.replace(password[0], password[0].upper()) + "!" + str(random.randint(10, 99)),
        password[:2] + "@" + password[2:] + "#" + str(random.randint(100, 999)),
        "".join(random.choice((c.upper(), c.lower(), c)) for c in password) + "$"
    ]

    # Completely different alternatives
    alternatives = [
        "Vortex!" + str(random.randint(10, 99)),
        "IronPeak#" + str(random.randint(100, 999)),
        "ShadowRun_" + str(random.randint(10, 99))
    ]

    # Structural recommendations
    recommendations = [
        "Break dictionary words with random inserts.",
        "Add 2–3 symbols in unpredictable positions.",
        "Mix uppercase throughout instead of only first letter."
    ]

    return stronger, alternatives, recommendations


def format_suggestions(password):
    stronger, alternatives, recommendations = generate_suggestions(password)

    return f"""
==============================
 HYDRA SUGGESTIONS (3×3 SYSTEM)
==============================

Stronger Variants:
1. {stronger[0]}
2. {stronger[1]}
3. {stronger[2]}

Alternative Passwords:
1. {alternatives[0]}
2. {alternatives[1]}
3. {alternatives[2]}

Structural Recommendations:
1. {recommendations[0]}
2. {recommendations[1]}
3. {recommendations[2]}
"""


# -----------------------------
# MAIN PROGRAM
# -----------------------------

if __name__ == "__main__":
    pwd = input("Enter a password to analyze: ")
    result = hydra_analyze(pwd)

    print("\nChoose output mode:")
    print("1. Full Report")
    print("2. JSON Only")
    print("3. Score Only")
    print("4. Suggestions Only")
    print("5. EVERYTHING (Full Package)\n")

    mode = input("Select mode (1-5): ")

    if mode == "1":
        print(format_report(result, pwd))
    elif mode == "2":
        print(format_json(result))
    elif mode == "3":
        print(format_score(result, pwd))
    elif mode == "4":
        print(format_suggestions(pwd))
    elif mode == "5":
        print(format_report(result, pwd))
        print(format_json(result))
        print(format_score(result, pwd))
        print(format_suggestions(pwd))
    else:
        print("Invalid selection.")
