from .entropy import analyze_entropy
from .distribution import analyze_distribution
from .mutations import analyze_mutations
from .patterns import analyze_patterns
from .semantics import analyze_semantics
from .structure import analyze_structure

def hydra_analyze(password: str) -> dict:
    return {
        "entropy": analyze_entropy(password),
        "distribution": analyze_distribution(password),
        "mutations": analyze_mutations(password),
        "patterns": analyze_patterns(password),
        "semantics": analyze_semantics(password),
        "structure": analyze_structure(password)
    }
