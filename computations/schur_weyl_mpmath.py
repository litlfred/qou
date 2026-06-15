#!/usr/bin/env python3
"""
P2.2b-MN — direct mpmath path for Schur-Weyl at high A.

The sympy-based fast path (`schur_weyl_optimised.py`) hits two
bottlenecks at A=12:

  schur_weyl_weight_fast (61s):  sp.cancel on s_λ/H_q(λ) for
    length-≤-2 partitions of 36.  H_q(λ) has 36 hook factors;
    cancelling against s_λ is expensive.

  sp.N(subs(q, q_0), 50) (34s):  evalf with q_0 as a Rational
    against a complex symbolic expression.

This module computes the Schur-Weyl sum **directly at q_0 in
mpmath** — no symbolic intermediate.  Each q_integer evaluates
to a real number; the per-partition contribution is a finite
product of reals; the sum is ~ms.

For the polynomial form (P2.5 Tier B), use the sympy path
(`schur_weyl_optimised.py`); for production numerical evaluation
at q_0 (mass-tower compute, P2.2a wiring, etc.), use this module.

Witness: docs/audits/2026-05-01-p2-2b-mn-mpmath.witness.json
"""
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from murnaghan_nakayama import (
    atomic_braid_word,
    cycle_type_of_permutation,
    hook_lengths,
    mn_character,
    permutation_from_braid_word,
)
from q_parameter import Q as Q0_FLOAT


def q_int_mp(k, q):
    """[k]_q = (q^k - q^{-k}) / (q - q^{-1}) in mpmath."""
    if k == 0:
        return mpmath.mpf(0)
    if k == 1:
        return mpmath.mpf(1)
    return (q ** k - q ** (-k)) / (q - 1 / q)


def q_factorial_mp(n, q):
    """[n]_q! = ∏_{k=1}^n [k]_q in mpmath."""
    result = mpmath.mpf(1)
    for k in range(1, n + 1):
        result *= q_int_mp(k, q)
    return result


def q_hook_product_mp(partition, q):
    """H_q(λ) = ∏ [h_x(λ)]_q in mpmath."""
    hooks = hook_lengths(partition)
    result = mpmath.mpf(1)
    for h in hooks:
        result *= q_int_mp(h, q)
    return result


def schur_two_var_mp(partition, q):
    """s_λ(q, q⁻¹) for length-≤-2 partitions in mpmath."""
    length = len(partition)
    if length > 2:
        return mpmath.mpf(0)
    if length == 0:
        return mpmath.mpf(1)
    if length == 1:
        n = partition[0]
        result = mpmath.mpf(0)
        for k in range(n + 1):
            result += q ** (n - 2 * k)
        return result
    a, b = partition
    numer = q ** (a + 1) * q ** (-b) - q ** b * q ** (-(a + 1))
    denom = q - q ** (-1)
    return numer / denom


def schur_weyl_weight_mp(partition, q):
    """w_λ = s_λ(q, q⁻¹) / H_q(λ) in mpmath."""
    s = schur_two_var_mp(partition, q)
    if s == 0:
        return mpmath.mpf(0)
    H = q_hook_product_mp(partition, q)
    return s / H


def length_le_2_partitions_of(n):
    """All partitions of n with at most 2 parts. ⌊n/2⌋ + 1 of them."""
    yield (n,)
    for b in range(1, n // 2 + 1):
        a = n - b
        if a >= b:
            yield (a, b)


def markov_trace_mpmath(Z, N, *, q_val=None, precision=50,
                         include_inter=True):
    """tr_M of an atomic braid via length-≤-2 Schur-Weyl sum, mpmath path.

    Returns (value, partitions_used).  precision = mpmath dps.
    """
    if q_val is None:
        q_val = Q0_FLOAT
    mpmath.mp.dps = precision
    q = mpmath.mpf(str(q_val))

    A = Z + N
    n_strands = 3 * A
    word = atomic_braid_word(Z, N, include_inter=include_inter)
    perm = permutation_from_braid_word(word, n_strands)
    cyc = cycle_type_of_permutation(perm)

    total = mpmath.mpf(0)
    partitions_used = []
    for lam in length_le_2_partitions_of(n_strands):
        chi = mn_character(lam, cyc)
        if chi == 0:
            continue
        w = schur_weyl_weight_mp(lam, q)
        if w == 0:
            continue
        contrib = w * mpmath.mpf(chi)
        total += contrib
        partitions_used.append({
            "partition": list(lam),
            "weight": str(w),
            "character": chi,
            "contribution": str(contrib),
        })
    return total, partitions_used, cyc


# ─── Witness + comparison ─────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 80)
    print("P2.2b-MN — direct mpmath Schur-Weyl path")
    print("=" * 80)

    ATOMS = [
        ("D", 1, 1, 2),
        ("3He", 2, 1, 3),
        ("4He", 2, 2, 4),
        ("12C", 6, 6, 12),
        ("16O", 8, 8, 16),
        ("40Ca", 20, 20, 40),
    ]

    results = []
    for name, Z, N, A in ATOMS:
        print(f"\n=== {name} (Z={Z}, N={N}, A={A}, n=3A={3*A}) ===")
        t0 = time.time()
        try:
            total, parts, cyc = markov_trace_mpmath(Z, N, precision=50)
            t = time.time() - t0
            mag = abs(total)
            print(f"  cycle type: {cyc}")
            print(f"  |Σ_λ w_λ χ^λ| = {mag}")
            print(f"  {len(parts)} non-zero partitions")
            print(f"  time: {t:.3f}s")
            q0_f = float(Q0_FLOAT)
            convergent = float(mag) < q0_f
            print(f"  Φ_q convergence (|·| < q_0={q0_f:.4f}):  → {'✅' if convergent else '🔴'}")
            results.append({
                "atom": name,
                "Z": Z, "N": N, "A": A,
                "n_strands": 3 * A,
                "cycle_type": list(cyc),
                "n_partitions_used": len(parts),
                "abs_value_at_q0": str(mag),
                "phi_q_convergent": convergent,
                "time_seconds": t,
                "partitions": parts,
            })
        except Exception as e:
            t = time.time() - t0
            import traceback
            traceback.print_exc()
            results.append({"atom": name, "error": str(e), "time_seconds": t})

    witness = {
        "audit": "P2.2b-MN — direct mpmath Schur-Weyl path",
        "generated": datetime.now(timezone.utc).isoformat(),
        "q_0": str(Q0_FLOAT),
        # P2.5 marker — pure mpmath numerical path (no symbolic q),
        # so polynomial exposure does not apply. The sibling
        # schur_weyl_optimised.py is the symbolic-q path.
        "polynomial_q_not_applicable": True,
        "atoms": results,
        "interpretation": (
            "Bypasses sympy's symbolic GCD path entirely by computing "
            "the Schur-Weyl sum directly at q_0 in mpmath. Per-atom "
            "time drops from ~minutes (sympy) to ~ms (mpmath). For the "
            "polynomial-in-q form (P2.5 Tier B), use the sympy path "
            "(schur_weyl_optimised.py). For mass-tower production "
            "compute at q_0, use this module."
        ),
    }

    out_path = Path(__file__).parent.parent.parent / "docs/audits/2026-05-01-p2-2b-mn-mpmath.witness.json"
    out_path.write_text(json.dumps(witness, indent=2, default=str))
    print()
    print(f"Witness: {out_path.relative_to(Path(__file__).parent.parent.parent)}")
