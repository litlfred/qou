#!/usr/bin/env python3
# polynomial_q_not_applicable: library / no own witness output; sympy used internally by callers.
"""Symbolic computation of q-dimensions and argmax-stability across q.

For each partition lambda |- n, compute:
  dim_q(V_lambda) = [n]_q! / prod_{x in lambda} [h(x)]_q

as a rational function of q via SymPy. The "argmax" partition (= the
LR-dominant Hecke module = the LP optimum at strand count n) is
piecewise constant in q, switching at critical q* values where two
q-dimensions tie. Identify these critical q* and check whether
q_0 ~ 1.10974 falls in a regime that selects self-conjugate lambda
at magic n.

Theorem to test (parametric LP):
  T1: argmax_lambda dim_q(V_lambda) is well-defined for all q > 0,
      q != 1.
  T2: As a function of q, argmax is piecewise constant on open
      intervals, separated by finitely many critical q* > 0 where
      two partition q-dims tie.
  T3 (conjecture): At q_0, argmax is self-conjugate iff n is on the
      magic ladder.

Run as:
    python3 symbolic_qdim_argmax.py [n ...]
"""

import sys
from fractions import Fraction
from typing import List, Tuple, Optional

import sympy as sp
from sympy import Symbol, Rational, simplify, Poly, expand, sympify

sys.path.insert(0, ".")
from enumerate_self_conjugate_partitions import (  # noqa: E402
    conjugate_partition,
    content_sum,
)


q = Symbol("q", positive=True, real=True)


def q_integer(k: int):
    """[k]_q = (q^k - q^{-k}) / (q - q^{-1}) as SymPy rational."""
    if k == 0:
        return sp.Integer(0)
    if k == 1:
        return sp.Integer(1)
    # Equivalent to q^{k-1} + q^{k-3} + ... + q^{-(k-1)}, k terms.
    return sum(q ** (k - 1 - 2 * j) for j in range(k))


def q_factorial(n: int):
    """[n]_q! = [1]_q [2]_q ... [n]_q."""
    out = sp.Integer(1)
    for k in range(1, n + 1):
        out = out * q_integer(k)
    return sp.together(out)


def hook_lengths(partition: List[int]) -> List[int]:
    """Hook lengths h(i,j) = lambda_i - j + lambda'_j - i + 1 for
    each cell (i, j) of the Young diagram."""
    if not partition:
        return []
    conj = conjugate_partition(partition)
    out = []
    for i, length in enumerate(partition, start=1):
        for j in range(1, length + 1):
            h = (length - j) + (conj[j - 1] - i) + 1
            out.append(h)
    return out


def q_dim(partition: List[int]):
    """Quantum dimension dim_q(V_lambda) for Iwahori-Hecke H_n(q),
    equal to [n]_q! / prod [h(x)]_q."""
    if not partition:
        return sp.Integer(1)
    n = sum(partition)
    numerator = q_factorial(n)
    denominator = sp.Integer(1)
    for h in hook_lengths(partition):
        denominator = denominator * q_integer(h)
    return sp.together(numerator / denominator)


def partitions_of(n: int, max_first: Optional[int] = None) -> List[List[int]]:
    if max_first is None:
        max_first = n
    out = []

    def go(remaining: int, max_part: int, current: List[int]) -> None:
        if remaining == 0:
            out.append(list(current))
            return
        for k in range(min(max_part, remaining), 0, -1):
            current.append(k)
            go(remaining - k, k, current)
            current.pop()

    go(n, max_first, [])
    return out


def evaluate_at(q_value: float, expr) -> float:
    """Numerically evaluate a SymPy q-expression at the given q."""
    return float(expr.subs(q, q_value))


def argmax_at(q_value: float, dims: dict) -> Tuple[List[int], float]:
    """Given dict { partition: dim_expr }, return argmax and value."""
    best = None
    best_val = -float("inf")
    for part, d in dims.items():
        val = evaluate_at(q_value, d)
        if val > best_val:
            best = part
            best_val = val
    return best, best_val


def find_critical_q(d1, d2, q_min: float = 0.001, q_max: float = 10.0) -> List[float]:
    """Find positive real q where d1(q) = d2(q), in (q_min, q_max).
    Equivalent to finding roots of (d1 - d2)."""
    diff = sp.cancel(d1 - d2)
    try:
        roots = sp.solve(diff, q)
        out = []
        for r in roots:
            try:
                val = float(r)
                if q_min < val < q_max:
                    out.append(val)
            except (TypeError, ValueError):
                continue
        return sorted(set(out))
    except Exception:
        return []


def analyze(n: int, q_test_points: List[float]) -> dict:
    """Compute q-dim for all lambda |- n, find argmax at each test
    q value, identify regime structure."""
    print(f"\n{'='*60}")
    print(f"  n = {n}")
    print(f"{'='*60}")

    parts = partitions_of(n)
    print(f"  Partitions of {n}: {len(parts)}")

    dims = {tuple(p): q_dim(p) for p in parts}
    print(f"  Computing q-dim for {len(parts)} partitions...")

    # Argmax at each test q
    table = []
    for q_val in q_test_points:
        best, val = argmax_at(q_val, dims)
        is_sc = list(best) == conjugate_partition(list(best))
        table.append((q_val, list(best), val, is_sc))
        print(
            f"    q={q_val:7.4f}: argmax={list(best)}"
            f" (dim={val:.4g}, self-conj={is_sc})"
        )

    # Detect regime changes
    regime_changes = []
    for i in range(1, len(table)):
        if table[i][1] != table[i - 1][1]:
            regime_changes.append((table[i - 1][0], table[i][0]))
    if regime_changes:
        print(f"  Regime changes between test points: {regime_changes}")
    else:
        print("  No regime changes detected at test points.")

    return {
        "n": n,
        "n_partitions": len(parts),
        "argmax_table": table,
        "regime_changes": regime_changes,
    }


def main(argv: List[str]) -> int:
    if len(argv) > 1:
        targets = [int(a) for a in argv[1:]]
    else:
        targets = [4, 6, 8, 10, 12, 14, 16]

    # Test q values: span (1.001, 5) with q_0 ~ 1.10974 included.
    q_test = [1.001, 1.05, 1.10974, 1.2, 1.5, 2.0, 3.0, 5.0]

    report = {}
    magic = {2, 8, 20, 28, 50, 82, 126}
    for n in targets:
        report[n] = analyze(n, q_test)
        report[n]["magic"] = n in magic

    # Summary: at q_0, is the argmax self-conjugate?
    print()
    print("=" * 60)
    print(f"  Summary at q_0 = 1.10974")
    print("=" * 60)
    print(f"  {'n':>4} {'magic':>6} {'argmax':<30} {'self-conj':>10}")
    print("  " + "-" * 60)
    for n, r in report.items():
        # Extract row at q=1.10974
        for q_val, best, val, is_sc in r["argmax_table"]:
            if abs(q_val - 1.10974) < 1e-5:
                magic_tag = "★" if r["magic"] else ""
                print(
                    f"  {n:>4} {magic_tag:>6} {str(best):<30} {is_sc!s:>10}"
                )
                break

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
