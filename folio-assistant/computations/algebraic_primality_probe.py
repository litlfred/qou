#!/usr/bin/env python3
# polynomial_q_not_applicable: library / no own witness output; sympy used internally by callers.
"""Symbolic algebraic-primality probe — uses candidate-B demand
(self-conjugate-block indicator) and a Wedderburn-block scalar
LP relaxation to decide whether n is "magic" at symbolic q.

For each n in a small range, computes:
  1. Self-conjugate partitions of n.
  2. Wedderburn weight w_lambda(q) = dim_q(V_lambda)^2 / [n]_q!
     for each self-conjugate lambda.
  3. Argmax (cheapest) self-conjugate block at q symbolic — the
     "active block" lambda*(n, q) under candidate-B demand.
  4. Whether the active block is unique (rank-1, hence magic per
     conj:sdp-rank-collapse-magic-shell), or tied with multiple
     blocks (rank > 1, non-magic).

Candidate-B demand: b_lambda = 1 iff lambda = lambda', else 0.
The LP minimizes sum c_lambda T_lambda subject to T concentrated
on self-conj blocks. Optimum: T* concentrates on argmax-weight
self-conj. Magic = unique argmax.

Usage:
    python3 algebraic_primality_probe.py [n ...]
"""

import sys
import time
from typing import List, Tuple, Optional

import sympy as sp

sys.path.insert(0, ".")
from enumerate_self_conjugate_partitions import (  # noqa: E402
    all_self_conjugate_partitions,
    conjugate_partition,
    content_sum,
)
from symbolic_qdim_argmax import (
    q,
    q_dim,
    q_factorial,
    q_integer,
    partitions_of,
)


def wedderburn_weight(partition: List[int]) -> sp.Expr:
    """w_lambda(q) = dim_q(V_lambda)^2 / [n]_q!"""
    if not partition:
        return sp.Integer(0)
    n = sum(partition)
    return sp.together(q_dim(partition) ** 2 / q_factorial(n))


def argmax_self_conj(n: int, q_value: float) -> Tuple[List[List[int]], List[float]]:
    """For n at numeric q_value, return:
    - List of self-conj partitions sorted by Wedderburn weight (descending).
    - Numerical weights at q_value.
    """
    self_conjs = all_self_conjugate_partitions(n)
    if not self_conjs:
        return ([], [])
    weights = []
    for lam in self_conjs:
        w_expr = wedderburn_weight(lam)
        w_val = float(w_expr.subs(q, q_value))
        weights.append((lam, w_val))
    weights.sort(key=lambda x: -x[1])
    return ([w[0] for w in weights], [w[1] for w in weights])


def is_active_block_unique(weights: List[float], rel_tol: float = 1e-9) -> bool:
    """At candidate-B demand, the LP picks the argmax weight.
    Returns True if the argmax is unique (single rank-1 active block),
    False if multiple weights tie at the max.
    """
    if len(weights) <= 1:
        return len(weights) == 1
    return weights[0] > weights[1] * (1 + rel_tol)


def algebraic_primality_at_q(
    n: int, q_value: float
) -> dict:
    """Test algebraic primality of n at numeric q_value via the
    candidate-B Wedderburn-LP relaxation."""
    sc_sorted, weights = argmax_self_conj(n, q_value)
    if not sc_sorted:
        return {
            "n": n,
            "q": q_value,
            "self_conj_count": 0,
            "active_block": None,
            "active_unique": False,
            "magic_predicate": False,
            "reason": "degenerate (no self-conjugate)",
        }
    active = sc_sorted[0]
    weight_top = weights[0]
    unique = is_active_block_unique(weights)
    return {
        "n": n,
        "q": q_value,
        "self_conj_count": len(sc_sorted),
        "active_block": active,
        "active_block_weight": weight_top,
        "second_block": sc_sorted[1] if len(sc_sorted) > 1 else None,
        "second_block_weight": weights[1] if len(weights) > 1 else None,
        "active_unique": unique,
        "magic_predicate": unique,
        "reason": "rank-1 unique self-conj"
        if unique
        else "rank-{} multiple self-conj tied".format(len(sc_sorted)),
    }


MAGIC_LADDER = {1, 2, 8, 20, 28, 50, 82, 126}


def main(argv: List[str]) -> int:
    if len(argv) > 1:
        targets = [int(a) for a in argv[1:]]
    else:
        targets = list(range(1, 17))

    # Test at q_0 and at a few neighbouring q values.
    q_test_points = [1.001, 1.05, 1.10974, 1.2, 1.5, 2.0]

    print(f"{'n':>4} {'magic?':>8} {'q':>9} {'#SC':>5}"
          f" {'unique?':>8} {'top λ':<25} {'2nd λ':<25}")
    print("-" * 100)
    results = {}
    for n in targets:
        is_magic_empirical = n in MAGIC_LADDER
        for q_val in q_test_points:
            r = algebraic_primality_at_q(n, q_val)
            results.setdefault(n, []).append(r)
            magic_emp = "★" if is_magic_empirical else " "
            unique = "rank-1" if r["active_unique"] else "rank>1"
            top = str(r["active_block"]) if r["active_block"] else "(none)"
            second = (
                str(r.get("second_block", "(none)"))
                if r.get("second_block")
                else "(none)"
            )
            print(
                f"{n:>4} {magic_emp:>8} {q_val:>9.4f} {r['self_conj_count']:>5}"
                f" {unique:>8} {top:<25} {second:<25}"
            )

    # Summary — at q_0, for each n, does the LP predict magic?
    print()
    print("=" * 80)
    print("Summary at q_0 = 1.10974:")
    print("=" * 80)
    print(f"{'n':>4} {'empirical_magic?':>18} {'LP_predicts_magic?':>22}"
          f" {'agrees?':>9}")
    print("-" * 80)
    for n in targets:
        for r in results[n]:
            if abs(r["q"] - 1.10974) < 1e-5:
                emp = n in MAGIC_LADDER
                pred = r["magic_predicate"]
                agrees = "✓" if emp == pred else "✗"
                print(
                    f"{n:>4} {str(emp):>18} {str(pred):>22} {agrees:>9}"
                )
                break

    # Count agreements
    agreements = sum(
        1
        for n in targets
        for r in results[n]
        if abs(r["q"] - 1.10974) < 1e-5 and (n in MAGIC_LADDER) == r["magic_predicate"]
    )
    print()
    print(f"Agreements at q_0: {agreements}/{len(targets)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
