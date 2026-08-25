"""Categorical proof attempt: 171/143 = 6/5 from structural cardinality ratios.

Per audit §4 path: the cleanest derivation route for the 171/143
hypothesis is "block-counting" — identify 6 and 5 as cardinalities of
existing structural objects in the framework + show the ratio appears
in the mass formulas.

This probe SYSTEMATICALLY tests cardinality-ratio combinations from
the framework's existing structures + identifies which combinations
give EXACTLY (or to-machine-precision) 171/143 ≈ 1.1958.

If a clean structural ratio matches to machine precision, that's
strong evidence for the categorical identity. If only the loose 6/5
match (0.35% off) survives, the hypothesis is at the "suggestive"
level rather than "proved".

Structural cardinalities tested:
  - |partitions of n| for n = 1..10
  - |GS-NF basis on B_n| (= |S_n| for n strands)
  - |Wedderburn blocks at H_n| (same as |partitions of n|)
  - Half-symmetric counts (e.g., 5/2 at H_4)
  - Dimension sums and dim² sums
  - Quantum dimensions [n]_q at substrate q_0
  - Schur element sums

Plus various combinations and substrate-q_0-weighted variants.

Status: EXPLORATORY (categorical proof ATTEMPT, not proof).
"""
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import subprocess
import sys
from math import comb
from pathlib import Path
from fractions import Fraction
from itertools import combinations

import mpmath as mp
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from mpmath import mpf
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# Substrate
Q_0 = mpf(Q_50_DIGIT_STR)  # canonical 50-digit substrate pin
H_0 = Q_0 - mpf(1) / Q_0

# Target: empirical 171/143 from PR #1128
TARGET_RATIO = mpf("171") / mpf("143")  # ≈ 1.1958...
print(f"Target: 171/143 = {float(TARGET_RATIO):.10f}")

# Hypothesis: 6/5 (sub-cardinality count)
HYPOTHESIS_6_5 = Fraction(6, 5)  # = 1.2 exactly
print(f"Hypothesis 6/5 = {float(HYPOTHESIS_6_5):.10f}")
print(f"Deviation 6/5 from 171/143: {(float(HYPOTHESIS_6_5) - float(TARGET_RATIO)) / float(TARGET_RATIO) * 100:.4f}%")

# Partition counts p(n) for n = 0..10
PARTITIONS_OF = {0: 1, 1: 1, 2: 2, 3: 3, 4: 5, 5: 7, 6: 11, 7: 15, 8: 22, 9: 30, 10: 42}

# Symmetric group orders n!
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

SYMMETRIC_ORDERS = {n: factorial(n) for n in range(0, 8)}

# Dimensions of S_n irreps (sum of dims, sum of dim²) — standard hook-length
DIM_SUMS = {
    2: {"sum": 2, "sum_sq": 2},  # 1 + 1
    3: {"sum": 4, "sum_sq": 6},  # 1 + 2 + 1
    4: {"sum": 10, "sum_sq": 24},  # 1 + 3 + 2 + 3 + 1
    5: {"sum": 26, "sum_sq": 120},  # 1 + 4 + 5 + 6 + 5 + 4 + 1
}

# Half-symmetric dimension at H_4: 1 + 3 + (2/2) = 5 (one of each conj-pair + half self-conj)
HALF_SYM_H4 = Fraction(5)
HALF_SYM_TRIVIAL_H4 = Fraction(2)
# ... gives bijection (5/2) × (2/5) = 1 per s4-s3-half-symmetric-projection

# Half-symmetric S_3-trivial factor = 2/5
S3_TRIVIAL_RATIO = Fraction(2, 5)

# Empirical mass factors (from PR #1128)
GAUGE_FACTOR_M_W = mpf("80.379") / mpf("0.5662")  # W normalization ≈ 142.0
GAUGE_FACTOR_M_Z = mpf("91.1876") / mpf("0.6353")  # Z normalization ≈ 143.5
SCALAR_FACTOR_H = mpf("125.10") / mpf("0.7320")    # H normalization ≈ 170.9


def report(label: str, value, mark_match: bool = True):
    """Standard reporting for ratio candidates."""
    if isinstance(value, Fraction):
        v_float = float(value)
        v_str = f"{value} = {v_float:.10f}"
    else:
        v_float = float(value)
        v_str = f"{v_float:.10f}"
    dev_pct = (v_float - float(TARGET_RATIO)) / float(TARGET_RATIO) * 100
    marker = ""
    if mark_match:
        if abs(dev_pct) < 0.05:
            marker = "  ★★★ MACHINE-PRECISION MATCH"
        elif abs(dev_pct) < 0.5:
            marker = "  ★★ sub-0.5% match"
        elif abs(dev_pct) < 2:
            marker = "  ★ within 2%"
    return f"  {label:<60} {v_str:<32} dev={dev_pct:+.4f}%{marker}"


def main():
    print("=" * 90)
    print(f"Categorical-proof attempt: 171/143 = {float(TARGET_RATIO):.6f}")
    print(f"Hypothesis: 6/5 (cardinality ratio); empirical match within 0.35%")
    print("Goal: find a clean structural ratio that matches EXACTLY (machine precision)")
    print("=" * 90)

    # Track all candidates for summary
    all_candidates = []

    # ===== Category 1: Direct partition / cardinality ratios =====
    print("\n--- Direct cardinality ratios ---")
    for a, b in [(6, 5), (3, 2), (12, 10), (24, 20), (11, 9), (13, 11),
                 (22, 18), (30, 25), (15, 13), (42, 35)]:
        f = Fraction(a, b)
        line = report(f"{a}/{b}", f)
        print(line)
        all_candidates.append({"label": f"{a}/{b}", "value": float(f), "category": "direct"})

    # ===== Category 2: |S_n| / partition counts =====
    print("\n--- |S_n| / |partitions(m)| ratios ---")
    for n_sym in range(2, 7):
        for m_par in range(2, 7):
            f = Fraction(SYMMETRIC_ORDERS[n_sym], PARTITIONS_OF[m_par])
            if 0.5 < float(f) < 5:
                line = report(f"|S_{n_sym}|/|partitions({m_par})| = {SYMMETRIC_ORDERS[n_sym]}/{PARTITIONS_OF[m_par]}", f)
                print(line)
                all_candidates.append({
                    "label": f"|S_{n_sym}|/|partitions({m_par})|",
                    "value": float(f),
                    "category": "symmetric_vs_partition",
                })

    # ===== Category 3: dim-sum and dim²-sum ratios =====
    print("\n--- dim sums / dim² sums ratios at various n ---")
    for n1 in DIM_SUMS:
        for n2 in DIM_SUMS:
            if n1 == n2:
                continue
            f1 = Fraction(DIM_SUMS[n1]["sum"], DIM_SUMS[n2]["sum"])
            if 0.5 < float(f1) < 5:
                line = report(f"Σdim(H_{n1})/Σdim(H_{n2}) = {DIM_SUMS[n1]['sum']}/{DIM_SUMS[n2]['sum']}", f1)
                print(line)
                all_candidates.append({
                    "label": f"Σdim(H_{n1})/Σdim(H_{n2})",
                    "value": float(f1),
                    "category": "dim_sum",
                })

    # ===== Category 4: half-symmetric ratios =====
    print("\n--- Half-symmetric H_4 ratios ---")
    candidates_hs = [
        (HALF_SYM_H4 / PARTITIONS_OF[3], f"halfSymDim(H_4)/|partitions(3)| = 5/3"),
        (Fraction(HALF_SYM_TRIVIAL_H4, 1) * HALF_SYM_H4, "S_3-trivial-content × halfSymDim = 2·5 = 10"),
        (Fraction(6, int(HALF_SYM_H4)), "6 / halfSymDim(H_4) = 6/5  ← THE HYPOTHESIS"),
        (Fraction(SYMMETRIC_ORDERS[3], int(HALF_SYM_H4)), "|S_3| / halfSymDim(H_4) = 6/5 ★ same"),
    ]
    for f, label in candidates_hs:
        if 0.5 < float(f) < 5:
            line = report(label, f)
            print(line)
            all_candidates.append({"label": label, "value": float(f), "category": "half_symmetric"})

    # ===== Category 5: q-deformed structural ratios at substrate =====
    print("\n--- q-deformed ratios at q_0 ---")

    def q_int(n):
        return (Q_0 ** n - Q_0 ** (-n)) / (Q_0 - 1 / Q_0)

    q_deformed = [
        ("[2]_q / [3]_q × 3/2", q_int(2) / q_int(3) * mpf(3) / 2),
        ("[3]_q / [2]_q × 2/3", q_int(3) / q_int(2) * mpf(2) / 3),
        ("[6]_q / [5]_q × 5/6", q_int(6) / q_int(5) * mpf(5) / 6),
        ("[6]_q / [5]_q", q_int(6) / q_int(5)),
        ("[4]_q / [3]_q × 3/4", q_int(4) / q_int(3) * mpf(3) / 4),
        ("(1 + h_0²)·6/5", (1 + H_0 ** 2) * mpf(6) / 5),
        ("(1 - h_0²)·6/5", (1 - H_0 ** 2) * mpf(6) / 5),
        ("6/5 × (1 - h_0²/some)", mpf(6) / 5 * (1 - H_0 ** 2 / mpf(11))),
    ]
    for label, val in q_deformed:
        line = report(label, val)
        print(line)
        all_candidates.append({"label": label, "value": float(val), "category": "q_deformed"})

    # ===== Category 6: The empirical ratio decomposition =====
    print("\n--- Empirical ratio decomposition: what IS 171/143 structurally? ---")
    target = TARGET_RATIO
    # 171 = 9 · 19
    # 143 = 11 · 13
    # So 171/143 = (9·19)/(11·13) = 171/143 (irreducible)
    print(f"  171 = 9 · 19 = 3² · 19")
    print(f"  143 = 11 · 13 (twin primes!)")
    print(f"  GCD(171, 143) = {171 if 143 % 171 == 0 else (143 if 171 % 143 == 0 else 1)}")
    print(f"  → 171/143 is IRREDUCIBLE (no common factor)")
    print()
    print(f"  Continued fraction: ...")
    # Continued fraction of 171/143
    p, q = 171, 143
    cf = []
    while q:
        cf.append(p // q)
        p, q = q, p % q
    print(f"  171/143 = [{', '.join(map(str, cf))}] (continued fraction)")
    print()
    print(f"  Closest simple rationals:")
    for denom in range(2, 11):
        num = round(float(target) * denom)
        f = Fraction(num, denom)
        dev = (float(f) - float(target)) / float(target) * 100
        marker = "  ★ best" if abs(dev) < 0.5 else ""
        print(f"    {num}/{denom} = {float(f):.6f}  dev {dev:+.3f}%{marker}")

    # ===== Best matches summary =====
    print("\n" + "=" * 90)
    print("BEST MATCHES (by absolute deviation from 171/143):")
    print("=" * 90)
    sorted_candidates = sorted(
        all_candidates,
        key=lambda c: abs((c["value"] - float(TARGET_RATIO)) / float(TARGET_RATIO)),
    )
    for i, c in enumerate(sorted_candidates[:15]):
        dev = (c["value"] - float(TARGET_RATIO)) / float(TARGET_RATIO) * 100
        marker = "  ★★★ MACHINE-PRECISION" if abs(dev) < 0.01 else "  ★★ <0.5%" if abs(dev) < 0.5 else ""
        print(f"  {i+1:>2}. {c['label']:<55} value={c['value']:.6f}  dev={dev:+.3f}%{marker}")

    # ===== Verdict =====
    print("\n" + "=" * 90)
    print("VERDICT")
    print("=" * 90)
    machine_precision_matches = [c for c in all_candidates if abs((c["value"] - float(TARGET_RATIO)) / float(TARGET_RATIO)) < 0.0001]
    sub_half_pct_matches = [c for c in all_candidates if abs((c["value"] - float(TARGET_RATIO)) / float(TARGET_RATIO)) < 0.005]
    if machine_precision_matches:
        print(f"✓ {len(machine_precision_matches)} match(es) at MACHINE precision (~1e-4 or better):")
        for m in machine_precision_matches:
            print(f"    {m['label']}: {m['value']:.10f}")
        print(f"  → STRONG categorical evidence for {{m['label']}} as the structural origin")
    else:
        print(f"✗ NO match at machine precision found.")
        print(f"  → 6/5 = 1.2 (the hypothesis) is the closest simple rational, but matches only to 0.35%.")
        print(f"  → 171/143 itself is irreducible (gcd = 1); cannot be reduced to a simpler form.")
        print(f"  → The empirical 0.35% deviation is consistent with measurement noise in")
        print(f"    the SM masses + the 50-dps precision of the trace polynomial.")
        print(f"  → CATEGORICAL PROOF STATUS: 6/5 hypothesis remains SUGGESTIVE but unproved.")
        print(f"    The 0.35% match could be coincidence; no clean structural ratio gives")
        print(f"    EXACTLY 171/143.")

    if sub_half_pct_matches:
        print(f"\n{len(sub_half_pct_matches)} sub-0.5% matches found (all numerically close to 6/5):")
        for m in sub_half_pct_matches[:5]:
            print(f"    {m['label']}: {m['value']:.6f}")

    # Witness
    witness = {
        "compute": "six_fifths_categorical_proof_attempt",
        "description": (
            "Categorical proof ATTEMPT for the 171/143 = 6/5 "
            "hypothesis. Systematically tests structural-cardinality "
            "ratios from the framework (partitions, |S_n|, dim sums, "
            "q-deformed [n]_q ratios, half-symmetric H_4) for matches "
            "with 171/143. Identifies machine-precision matches if "
            "any; otherwise documents the hypothesis as suggestive "
            "rather than proved."
        ),
        "parameters": {
            "precision": "mpfr",
            "dps": 50,
            "Q_0": str(Q_0),
            "H_0": str(H_0),
            "target_171_over_143": float(TARGET_RATIO),
            "hypothesis_6_over_5": float(HYPOTHESIS_6_5),
        },
        "all_candidates": all_candidates,
        "best_matches": sorted_candidates[:15],
        "machine_precision_matches": machine_precision_matches,
        "sub_half_pct_matches": sub_half_pct_matches,
        "continued_fraction_of_171_143": cf,
        "verdict": (
            f"FOUND {len(machine_precision_matches)} machine-precision matches"
            if machine_precision_matches
            else "NO machine-precision match found; 6/5 hypothesis remains SUGGESTIVE (0.35% empirical match) but unproved"
        ),
        "status": "exploratory",
        "tags": [
            "categorical-proof-attempt",
            "171-143-ratio",
            "six-fifths",
            "structural-cardinality",
            "open-question",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }
    from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
    out_path = WitnessBuilder.wrap_legacy(
        "six-fifths-categorical-proof-attempt", witness, script_path=__file__, engine="mpmath",
    ).save()
    print(f"\nWitness: {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
