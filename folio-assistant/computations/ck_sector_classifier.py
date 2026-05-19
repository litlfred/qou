"""ck_sector_classifier.py — sector classification utility for Q_β precision-ladder c_k.

Wires the averaging-resonance rule from `prop:averaging-resonance-rule`
into a reusable compute-infra primitive that other scripts can call.

Two classification methods:

1. **Empirical (silver-ratio Pell-Lucas test)**: given a c_k closed
   form as a function of q, evaluate at q = 1+√2, reduce to rational,
   test if numerator is in Pell-Lucas. If yes → pure-σ; if no → averaging-resonant.

2. **Predictive (combinatorial argmax-binomial — currently FALSIFIED)**:
   given typed-B_3 crossing distribution (n_σ, n_σ⁻¹, n_avg) and rung k,
   compute m_k = argmax binomial product. If m_k ≥ 1 → predicted averaging.
   NOTE: this naive rule fails for k ∈ {4, 6, 7, 9}; retained for future refinement.

The empirical method is currently the authoritative classifier. The
predictive method is for testing refinements of the combinatorial rule.

Used by:
- `qbeta_decay_sdp_extended_ck.py` (to classify newly-extracted c_k)
- `qbeta_silver_ratio_pell_lucas_ck.py` (to validate existing c_k closed forms)
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb
from typing import Literal


# Pell-Lucas sequence a_n (companion to Pell P_n), satisfying a_{n+1} = 2 a_n + a_{n-1}
# with a_0 = a_1 = 1: 1, 1, 3, 7, 17, 41, 99, 239, 577, 1393, ...
PELL_LUCAS = [1, 1, 3, 7, 17, 41, 99, 239, 577, 1393, 3363]
PELL = [0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378]

Sector = Literal["pure_sigma", "averaging_resonant"]


@dataclass(frozen=True)
class TypedB3Distribution:
    """Typed-B_3 braid crossing distribution.

    Default: proton braid distribution from neutron-qvalue-symbolic.md
    (n_sigma=6, n_sigma_inv=3, n_avg=2, n_total=11).
    """
    n_sigma: int = 6
    n_sigma_inv: int = 3
    n_avg: int = 2

    @property
    def n_total(self) -> int:
        return self.n_sigma + self.n_sigma_inv + self.n_avg

    @property
    def n_non_avg(self) -> int:
        return self.n_sigma + self.n_sigma_inv


PROTON_DIST = TypedB3Distribution()
NEUTRON_DIST = TypedB3Distribution(n_sigma=5, n_sigma_inv=4, n_avg=2)


def is_pell_lucas_clean(value: Fraction) -> bool:
    """Test if a rational value is Pell-Lucas-clean at silver ratio.

    The value is considered clean if its reduced numerator (in absolute
    value) is a Pell-Lucas number, a power of 2, a Pell-Lucas number
    times a power of 2, or a Pell-Lucas number squared.

    Examples:
      -2          → True (power of 2)
      -49/32      → True (49 = 7² = a_3²)
      -11/8       → False (11 is not in Pell-Lucas)
      7/2         → True (7 = a_3)
      -8          → True (-8 = -2³)
      49/16       → True (49 = a_3²)
      -7          → True (a_3)
      343/128     → True (343 = 7³ = a_3³; clean Pell-Lucas-power)
    """
    num = abs(value.numerator)
    if num == 0:
        return True
    # Power of 2 (covers num = 1 = 2^0 as well)
    if (num & (num - 1)) == 0:
        return True
    # (Pell-Lucas number)^j times (power of 2), for j in 1..4.
    # Use a set to deduplicate the leading 1 in PELL_LUCAS.
    for pl in {p for p in PELL_LUCAS if p > 1}:
        p_pow = 1
        for _j in range(1, 5):
            p_pow *= pl
            if num % p_pow == 0:
                quotient = num // p_pow
                if quotient != 0 and (quotient & (quotient - 1)) == 0:
                    return True
    return False


def classify_sector_empirical(c_k_at_silver: Fraction) -> Sector:
    """Empirical classification via silver-ratio Pell-Lucas test.

    This is the AUTHORITATIVE sector classifier — based on the
    empirical pattern verified at k ∈ {3, ..., 10}:
      Pell-Lucas-clean at silver ratio → pure_sigma
      Pell-Lucas-incompatible (1/2 fingerprint) → averaging_resonant
    """
    if is_pell_lucas_clean(c_k_at_silver):
        return "pure_sigma"
    return "averaging_resonant"


def classify_sector_predictive(dist: TypedB3Distribution, k: int) -> Sector:
    """Predictive classification via argmax-binomial combinatorial rule.

    WARNING: this rule is currently FALSIFIED at k ∈ {4, 6, 7, 8, 9, 10}
    (25% accuracy — correct only at k = 3 and k = 5). Use for refinement
    R&D; do NOT use for production classification.

    Returns the sector predicted by m_k ≥ 1 (averaging dominance) or
    m_k = 0 (pure-σ dominance).
    """
    n_avg = dist.n_avg
    n_non_avg = dist.n_non_avg
    best_m = 0
    best_weight = comb(n_non_avg, k) if 0 <= k <= n_non_avg else 0
    for m in range(1, n_avg + 1):
        if 0 <= k - m <= n_non_avg:
            w = comb(n_avg, m) * comb(n_non_avg, k - m)
            # Use >= to match the spec in averaging-resonance-rule.md:
            # m_k = max {m : binomial product >= pure-σ baseline}
            if w >= best_weight:
                best_weight = w
                best_m = m
    return "averaging_resonant" if best_m >= 1 else "pure_sigma"


# Empirical sector assignment (refined under authoritative Pell-Lucas test).
# c_8 = 49/16 = a_3²/2^4 and c_10 = 343/128 = a_3³/2^7 are Pell-Lucas-clean
# (49 = 7² = a_3², 343 = 7³ = a_3³), so they classify as pure-σ.
# c_5 = -11/8 is the UNIQUE outlier: 11 ∉ Pell-Lucas, not a power of 2.
EMPIRICAL_SECTOR: dict[int, Sector] = {
    3: "pure_sigma",
    4: "pure_sigma",
    5: "averaging_resonant",   # UNIQUE outlier: 11 ∉ Pell-Lucas
    6: "pure_sigma",
    7: "pure_sigma",
    8: "pure_sigma",   # 49 = a_3² Pell-Lucas square
    9: "pure_sigma",
    10: "pure_sigma",  # 343 = a_3³ Pell-Lucas cube
}


def validate_predictive_rule(dist: TypedB3Distribution = PROTON_DIST) -> dict:
    """Validate the predictive rule against empirical data.

    Returns dict with:
      matches: rungs where prediction == empirical
      mismatches: rungs where prediction != empirical
      accuracy: matches / total
    """
    matches = []
    mismatches = []
    for k, emp in EMPIRICAL_SECTOR.items():
        pred = classify_sector_predictive(dist, k)
        if pred == emp:
            matches.append(k)
        else:
            mismatches.append({"k": k, "predicted": pred, "empirical": emp})
    return {
        "matches": matches,
        "mismatches": mismatches,
        "accuracy": len(matches) / len(EMPIRICAL_SECTOR),
    }


# Self-test if invoked directly
if __name__ == "__main__":
    print("=" * 70)
    print("c_k sector classifier — empirical + predictive")
    print("=" * 70)
    print()
    print(f"Proton typed-B_3 distribution: {PROTON_DIST}")
    print(f"  n_total = {PROTON_DIST.n_total}")
    print()

    # Test empirical classifier on known c_k values at silver ratio
    test_cases = [
        (3, Fraction(-2), "pure_sigma"),
        (4, Fraction(-49, 32), "pure_sigma"),
        (5, Fraction(-11, 8), "averaging_resonant"),
        (6, Fraction(7, 2), "pure_sigma"),
        (7, Fraction(-8), "pure_sigma"),
        (8, Fraction(49, 16), "pure_sigma"),  # 49 is a_3² → CLEAN at silver
        (9, Fraction(-7), "pure_sigma"),
        (10, Fraction(343, 128), "pure_sigma"),  # 343 = 7³ → CLEAN
    ]

    print("Empirical (silver-ratio Pell-Lucas) classification:")
    for k, val, expected in test_cases:
        got = classify_sector_empirical(val)
        marker = "✓" if got == expected else "✗"
        print(f"  k={k}: c_k(silver) = {val}, classified as {got}  {marker}")
    print()

    # Validate predictive rule
    validation = validate_predictive_rule()
    print(f"Predictive (argmax-binomial) rule validation:")
    print(f"  accuracy: {validation['accuracy']:.0%}")
    print(f"  matches: {validation['matches']}")
    print(f"  mismatches: {validation['mismatches']}")
    print()
    if validation['accuracy'] < 1.0:
        print("⚠ Predictive rule is INCOMPLETE — see prop:averaging-resonance-rule")
        print("  for refinement directions (σ-eigenvalue weighting, cyclicity, per-block).")
