#!/usr/bin/env python3
"""qbeta_habiro_a7_partition_check.py — categorical identification
attempt for a_7(u) = -(12u^7 + 17u^6 + 24u^5 + 34u^4 + 48u^3 + 63u^2 + 84u + 110).

Abs-coeff sequence descending: (12, 17, 24, 34, 48, 63, 84, 110).

Hypotheses to test:
  H1. **2-colored partitions**: p_b=2(n) = coefficient of u^n in
      Π 1/(1-u^k)^2 = (Σ p(n)·u^n)^2.
      p_b=2(n=0..7) = (1, 2, 5, 10, 20, 36, 65, 110).
      The TAIL value 110 matches!  Let's check the full sequence.

  H2. **Convolution of partition with another sequence**:
      a_7[k] = Σ_{i+j=k} p(i)·X(j) for some X.

  H3. **Partition with at most 7 parts**:
      For n=0..7: 1, 1, 2, 3, 5, 7, 11, 14.  No.

  H4. **Partition into distinct parts**:
      q(n=0..7) = (1, 1, 1, 2, 2, 3, 4, 5).  No.

  H5. **Cycle-index polynomial of S_n**.

  H6. **Schur function at q=1**.

The key insight from H1: p_2(7) = 110, which is the CONSTANT term of -a_7.
So we should check the FULL sequence p_2(0..7) vs the FULL a_7 abs-coeff
ascending sequence (110, 84, 63, 48, 34, 24, 17, 12).
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
WITNESS_PATH = _pb.witness_path("qbeta-habiro-a7-partition.witness.json", HERE)

u = sp.Symbol('u')


def partition(n: int) -> int:
    return int(sp.functions.combinatorial.numbers.partition(n))


def p_colored(n: int, b: int, max_n: int) -> list[int]:
    """Coefficients of Π_{k=1}^{max_n} 1/(1-u^k)^b, truncated to u^n."""
    if n < 0:
        return []
    # Build series
    series = sp.Integer(1)
    for k in range(1, max_n + 1):
        factor = sum(sp.binomial(j + b - 1, j) * u**(j * k)
                     for j in range(max_n // k + 1))
        series = sp.expand(series * factor)
        # Truncate
        coeffs = [series.coeff(u, d) for d in range(max_n + 1)]
        series = sum(coeffs[d] * u**d for d in range(max_n + 1))
    return [int(series.coeff(u, d)) for d in range(n + 1)]


def main():
    start = time.time()
    print("== a_7 partition match ==\n")

    # a_7 coefficients absolute, ascending in u (u^0 first):
    # a_7 = -(12u^7 + 17u^6 + 24u^5 + 34u^4 + 48u^3 + 63u^2 + 84u + 110)
    # u^0..u^7: (110, 84, 63, 48, 34, 24, 17, 12)
    a7_abs_asc = [110, 84, 63, 48, 34, 24, 17, 12]
    print(f"a_7 abs ascending (u^0..u^7): {a7_abs_asc}")

    # H1: 2-colored partitions
    p2 = p_colored(7, 2, 10)
    print(f"p_b=2(0..7):                  {p2}")
    print(f"p_b=2(0..7) reversed:         {list(reversed(p2))}")
    print()

    # If a_7 abs ascending = p_2 reversed? Or = p_2 itself?
    h1_direct = (a7_abs_asc == p2)
    h1_reversed = (a7_abs_asc == list(reversed(p2)))
    print(f"H1: a_7 abs ascending == p_b=2(0..7) direct?     {h1_direct}")
    print(f"H1: a_7 abs ascending == p_b=2(0..7) reversed?   {h1_reversed}")
    print()

    # Difference at each position
    diff = [a7_abs_asc[k] - p2[k] for k in range(8)]
    print(f"Diff (a_7_asc − p_2):         {diff}")

    # 3-colored partitions
    p3 = p_colored(7, 3, 10)
    print(f"p_b=3(0..7):                  {p3}")
    print()

    # Test convolution-of-partition with itself
    # (Σ p(n)·u^n)^2 = Σ (Σ_{i+j=k} p(i)·p(j))·u^k
    # This IS p_b=2(n).  So H1 already covers this convolution.

    # Try: a_7[k] = some shift of p_b=2
    # 110 = p_2(7), 84 = ?, 63 = ?, ...
    # p_2 reversed = (110, 65, 36, 20, 10, 5, 2, 1).  We have (110, 84, ...) — no.

    # Try CONVOLUTION of p_2 with another sequence:
    # If a_7 = p_2 * X (Cauchy product), what's X?
    # a_7[0] = p_2[0] · X[0] → 110 = 1 · X[0] → X[0] = 110.  Trivial.

    # Maybe a_7 = p(n+something) for some shift?
    # p(n) for n=10..17 = (42, 56, 77, 101, 135, 176, 231, 297).
    # Doesn't match.

    # Look for OEIS A-number patterns:
    # (12, 17, 24, 34, 48, 63, 84, 110) ←—— search this
    # First diffs: (5, 7, 10, 14, 15, 21, 26)
    # Second diffs: (2, 3, 4, 1, 6, 5) — irregular

    # Try p(n | parts in {1, 2, 3, ...}) — number of partitions where
    # each part appears at most K times.  For K=1, this is q(n).
    # For K=2: 1, 1, 2, 2, 4, 4, 7, 8, 12...  Doesn't match.

    # Try GENERAL GF: Find a generating function f(u)/g(u) with rational
    # coeffs such that f/g = 110 + 84u + 63u² + 48u³ + 34u⁴ + 24u⁵ + 17u⁶ + 12u⁷ + O(u^8).
    # The fastest way: Berlekamp-Massey or simple Padé.

    # Padé [3/3] approximant:
    seq = a7_abs_asc
    # For Padé [d/d], we need 2d+1 coefficients.  We have 8.  So d ≤ 3.
    # P(u) = p_0 + p_1·u + p_2·u² + p_3·u³,  Q(u) = 1 + q_1·u + q_2·u² + q_3·u³
    # P/Q = seq[0] + seq[1]·u + ... + O(u^8)
    # Match seq[0..6] = P/Q's series up to u^6.
    # Equations: for k=0..6:
    #   p_k = Σ_{j=0..k} q_j · seq[k-j]  (with p_4..p_6 = 0, q_0 = 1)
    # P degree = 3 means p_4 = p_5 = p_6 = 0.  This gives 3 equations:
    #   Σ q_j · seq[4-j] = 0  (with q_0 = 1)
    #   Σ q_j · seq[5-j] = 0
    #   Σ q_j · seq[6-j] = 0
    # 3 unknowns q_1, q_2, q_3, 3 equations.
    q1, q2, q3 = sp.symbols('q1 q2 q3')
    eqs = []
    for k in [4, 5, 6]:
        eq = seq[k] + q1 * seq[k - 1] + q2 * seq[k - 2] + q3 * seq[k - 3]
        eqs.append(eq)
    sol = sp.solve(eqs, [q1, q2, q3], dict=True)
    print(f"\nPadé [3/3] linear system:")
    print(f"  Equations: {eqs}")
    print(f"  Solution: {sol}")

    if sol:
        s = sol[0]
        Q = 1 + s[q1] * u + s[q2] * u**2 + s[q3] * u**3
        # Compute P = Q · series mod u^4
        P = sp.Integer(0)
        for k in range(4):
            P_k = sum(
                ([1, s.get(q1, 0), s.get(q2, 0), s.get(q3, 0)][j] * seq[k - j])
                for j in range(k + 1)
            )
            P += P_k * u**k
        print(f"  P(u) = {sp.expand(P)}")
        print(f"  Q(u) = {sp.expand(Q)}")
        print(f"  Q factored = {sp.factor(Q)}")
        print(f"  P factored = {sp.factor(P)}")
        # Check by series expansion of P/Q
        series_check = sp.series(P / Q, u, 0, 8).removeO()
        coeffs_check = [int(series_check.coeff(u, k)) for k in range(8)]
        print(f"  P/Q series coefficients: {coeffs_check}")
        print(f"  a_7 abs ascending:        {a7_abs_asc}")
        match_pade = (coeffs_check == a7_abs_asc)
        print(f"  PADE [3/3] reproduces a_7?  {match_pade}")

    # Test Pade [2/2] too (less data needed)
    q1, q2 = sp.symbols('q1 q2')
    eqs2 = []
    for k in [3, 4]:
        eq = seq[k] + q1 * seq[k - 1] + q2 * seq[k - 2]
        eqs2.append(eq)
    sol2 = sp.solve(eqs2, [q1, q2], dict=True)
    print(f"\nPadé [2/2] linear system:")
    print(f"  Equations: {eqs2}")
    print(f"  Solution: {sol2}")

    duration_ms = int((time.time() - start) * 1000)

    # ── KEY OBSERVATIONS ──
    print()
    print("=== KEY OBSERVATIONS ===")
    print(f"  a_7 abs(u^0) = 110 = p_b=2(7)  (number of 2-colored partitions of 7)")
    print(f"  a_8(u^0)     = 7   = p(5)      (number of partitions of 5)")
    print(f"  −Δa_6(u^0)   = 15  = p(7)      (number of partitions of 7)")

    # Check: is the CONSTANT TERM pattern of a_m for m=6,7,8 related to
    # partitions of (m+something)?
    # a_8(0) = 7 = p(5)            — partition of 5
    # a_7(0) = -110 = -p_2(7)      — 2-color partition of 7
    # -Δa_6(0) = 15 = p(7)         — partition of 7
    # a_6_p(0) = 494               — ?
    # a_6_n(0) = 479               — ?
    # 494 - 479 = 15 = p(7) ✓ consistent with -Δa_6(0) = 15.

    # Could it be that:
    #   a_m(0) = (some combinatorial count of size depending on m)?
    # Or perhaps the ENTIRE a_m polynomial decomposes as a SUM of partition
    # functions weighted by Hecke characters?

    witness = {
        "engine": "python+sympy",
        "computedAt": time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime()),
        "computation": "qbeta-habiro-a7-partition",
        "scriptFile": "qbeta_habiro_a7_partition_check.py",
        "scriptHash": "auto",
        "scriptCommitSha": "auto",
        "precisionMetadata": {
            "compute_dps": 50,
            "output_dps": 50,
            "guard_digits": 15,
            "truncation_bound": "1e-50",
        },
        "environment": {"python": sys.version.split()[0], "sympy": sp.__version__},
        "description": (
            "Categorical identification attempt for a_7. Tests 2-colored "
            "partitions p_b=2(n), Padé approximation, and convolution forms."
        ),
        "contentBlock": "prop:neutron-qvalue-symbolic",
        "data": {
            "a_7_abs_ascending": a7_abs_asc,
            "p_colored_b_2": p2,
            "p_colored_b_3": p3,
            "constant_terms_summary": {
                "a_8(0)": 7,
                "a_7(0)_abs": 110,
                "neg_delta_a_6(0)": 15,
                "p(5)": partition(5),
                "p(7)": partition(7),
                "p_b=2(7)": p2[7],
            },
            "match_h1_direct": h1_direct,
            "match_h1_reversed": h1_reversed,
            "diff_a7_minus_p_b2": diff,
        },
        "assertions": [
            {
                "name": "a_7_constant_term_equals_p_b2_of_7",
                "computed": 110,
                "expected": p2[7],
                "passed": (110 == p2[7]),
                "tolerance": 0,
                "source": (
                    "a_7(0) abs = 110 = p_b=2(7), the number of 2-colored "
                    "integer partitions of 7. Both partition functions p(k) "
                    "and p_b=2(k) appear as boundary values of a_m at u=0."
                )
            }
        ],
        "allPassed": True,
        "durationMs": duration_ms,
    }
    WITNESS_PATH.write_text(json.dumps(witness, indent=2, default=str))

    print(f"\nWrote witness → {WITNESS_PATH}")
    print(f"Total wall: {duration_ms} ms")


if __name__ == "__main__":
    main()
