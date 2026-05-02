#!/usr/bin/env python3
"""Cohomology-class probe for conj:magic-requires-higher-cohomology.

Tests the hypothesis: at magic n, the SDP-active knot operator is
non-Hopf-decomposable (lives in E_inf^{p, q >= 1}); at non-magic n,
it's Hopf-decomposable (purely E_inf^{0, *}).

Approach:
  1. For each n, identify the canonical (most-square-like) self-conj
     partition lambda_n.
  2. Map lambda_n to a candidate knot operator via the Bring-shell-
     binding correspondence (six torus knots T_{p,q} for magic;
     Hopf links for non-magic).
  3. Classify: T_{2,2} (Hopf) -> "purely descended"; T_{2,n>=3} or
     T_{3,4}/T_{3,5} -> "higher cohomology".

This is a SHAPE PROBE, not a full SDP solve. The full empirical
verification requires running the SDP at q_0 and decomposing the
optimum across the spectral-sequence basis.

Bring's six embeddable torus knots (per prop:torus-knot-shell-binding):
  T_{2,3}, T_{2,5}, T_{2,7}, T_{2,9}, T_{3,4}, T_{3,5}

Cumulative shell sizes (per descartes-universe/torus-knot-shell-binding):
  shell 1: T_{2,3}      ->  2 cumulative
  shell 2: + T_{2,5}    ->  8 cumulative
  shell 3: + T_{2,7}    -> 20 cumulative
  shell 4: + T_{3,4}    -> 28 cumulative
  shell 5: + T_{2,9}    -> 50 cumulative
  shell 6: + T_{3,5}    -> 82 cumulative
  shell 7: + (next)     -> 126 cumulative

Usage:
    python3 cohomology_class_probe.py
"""

import json
import sys
from typing import List, Tuple, Optional

sys.path.insert(0, ".")
from enumerate_self_conjugate_partitions import (  # noqa: E402
    canonical_self_conjugate,
    conjugate_partition,
)


# Bring's six embeddable torus knots and the magic shell they generate.
# Source: descartes-universe/torus-knot-shell-binding.md (per agent survey).
BRING_TORUS_KNOTS = [
    {"name": "T_{2,3}", "p": 2, "q": 3, "shell_index": 1, "magic_n": 2},
    {"name": "T_{2,5}", "p": 2, "q": 5, "shell_index": 2, "magic_n": 8},
    {"name": "T_{2,7}", "p": 2, "q": 7, "shell_index": 3, "magic_n": 20},
    {"name": "T_{3,4}", "p": 3, "q": 4, "shell_index": 4, "magic_n": 28},
    {"name": "T_{2,9}", "p": 2, "q": 9, "shell_index": 5, "magic_n": 50},
    {"name": "T_{3,5}", "p": 3, "q": 5, "shell_index": 6, "magic_n": 82},
    # T_{?,?} for shell 7 -> 126: not explicitly identified in the
    # current Bring-surface analysis. Recorded as TBD.
]

MAGIC_LADDER = [2, 8, 20, 28, 50, 82, 126]
MAGIC_SET = set(MAGIC_LADDER)


def crossing_number(torus_knot: dict) -> int:
    """Crossing number of T_{p, q}: c(T_{p,q}) = min(p(q-1), q(p-1))
    when gcd(p, q) = 1."""
    p, q = torus_knot["p"], torus_knot["q"]
    return min(p * (q - 1), q * (p - 1))


def is_hyperbolic_class(torus_knot: dict) -> bool:
    """Torus knots are NEVER hyperbolic; they're Seifert-fibered.
    Used here for cohomology-grade tagging — Hopf is the simplest
    Seifert-fibered, lives in E^{0, *}; T_{p, q} for higher (p, q)
    are still Seifert-fibered but sit in E^{p, q >= 1}."""
    return False  # All torus knots are Seifert-fibered.


def cohomology_class(torus_knot: Optional[dict]) -> str:
    """Map a knot to a coarse cohomology-class label."""
    if torus_knot is None:
        return "unmapped"
    p, q = torus_knot["p"], torus_knot["q"]
    if p == 2 and q == 2:
        return "E^{0, *} (Hopf)"
    if p == 2 and q == 3:
        return "E^{1, *} (trefoil; lowest non-Hopf)"
    if (p, q) in [(2, 5), (2, 7), (2, 9), (3, 4), (3, 5)]:
        return f"E^{{p, q >= 1}} ({torus_knot['name']}; Bring torus knot)"
    return f"E^{{?, ?}} (unclassified torus knot {torus_knot['name']})"


def magic_to_torus_knot(n: int) -> Optional[dict]:
    """If n is a magic number, return the corresponding Bring torus
    knot. Otherwise return None."""
    for tk in BRING_TORUS_KNOTS:
        if tk["magic_n"] == n:
            return tk
    return None


def classify(n: int) -> dict:
    canonical, count = canonical_self_conjugate(n)
    is_magic = n in MAGIC_SET
    knot = magic_to_torus_knot(n) if is_magic else None
    cohom = cohomology_class(knot)
    if not is_magic:
        cohom = "E^{0, *} (Hopf-decomposable; non-magic)"
    return {
        "n": n,
        "is_magic": is_magic,
        "canonical_self_conj": canonical,
        "self_conj_count": count,
        "candidate_torus_knot": knot["name"] if knot else None,
        "crossing_number": crossing_number(knot) if knot else None,
        "cohomology_class": cohom,
    }


def main(argv: List[str]) -> int:
    if len(argv) > 1:
        targets = [int(a) for a in argv[1:]]
    else:
        targets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20,
                   24, 28, 36, 50, 60, 82, 100, 126]

    print(f"{'n':>4} {'magic?':>7} {'#SC':>5} {'canonical':<22}"
          f" {'torus knot':>12} {'cross':>5} {'cohomology class':>40}")
    print("-" * 110)

    rows = []
    for n in targets:
        r = classify(n)
        rows.append(r)
        magic = "★" if r["is_magic"] else " "
        canon_str = str(r["canonical_self_conj"]) if r["canonical_self_conj"] else "(none)"
        knot = r["candidate_torus_knot"] or "—"
        cross = str(r["crossing_number"]) if r["crossing_number"] else "—"
        print(
            f"{r['n']:>4} {magic:>7} {r['self_conj_count']:>5}"
            f" {canon_str:<22} {knot:>12} {cross:>5}"
            f" {r['cohomology_class']:>40}"
        )

    # Summary
    print()
    print("Summary:")
    print()
    print("  Magic shells (predicted to have higher-cohomology operator):")
    for r in rows:
        if r["is_magic"] and r["candidate_torus_knot"]:
            print(
                f"    n={r['n']}: {r['candidate_torus_knot']}"
                f" (crossing={r['crossing_number']})"
                f" -> {r['cohomology_class']}"
            )
    print()
    print("  Magic shells without explicit Bring torus knot:")
    for r in rows:
        if r["is_magic"] and not r["candidate_torus_knot"]:
            print(f"    n={r['n']}: TBD")
    print()
    print("  Non-magic shells (predicted Hopf-decomposable):")
    nonmagic = [r["n"] for r in rows if not r["is_magic"]]
    print(f"    {nonmagic}")

    # Save report
    with open("cohomology_class_report.json", "w") as f:
        json.dump(rows, f, indent=2)
    print()
    print("Full report saved to cohomology_class_report.json")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
