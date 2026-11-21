#!/usr/bin/env python3
"""
alpha_shift_torus.py — α_shift(T_{p,k}) via symbolic seminormal traces.

For a torus knot T_{p,k} represented as the closure of the p-strand braid
β_{p,k} = (σ_1 σ_2 ⋯ σ_{p-1})^k in B_p, computes:

  • The per-irrep symbolic character χ_λ(β_{p,k}) ∈ ℚ(q) for every λ ⊢ p.
  • The pole order at q = 0 of each χ_λ.
  • The maximizer:  α_shift(T_{p,k}) := max_λ ord_{q=0}^{(-)} χ_λ(β_{p,k}).
  • The empirical claim: the maximizer is V_{(1^p)}, with closed-form
    pole order = k(p-1).  Verified at the test bench (p, k) ∈ {
    (2, 3), (2, 5), (2, 9), (3, 4), (3, 5), (3, 7) }.

Witness: alpha-shift-torus.witness.json

References:
  prop:em-coupling-projection                        (1/α_EM = q[9]_q[10]_q)
  prop:alpha-em-categorical-trace-ratio              (δ_q form)
  conj:force-carrier-intertwining-correspondence    (V_{(p,1^{n-p})} channel)
  def:delta-q-decoration

The bridge claim formalised by this script:
  α_EM⁻¹ = q · [α_shift(T_{2,9})]_q · [α_shift(T_{3,5})]_q
         = q · [9]_q · [10]_q.

@module computations/alpha_shift_torus
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

import sys
from math import gcd
from pathlib import Path
from typing import Dict, List, Tuple

import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from hecke_characters import partitions_of, standard_young_tableaux  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


# ──────────────────────────────────────────────────────────────────────
# Symbolic seminormal Hoefsmit matrices in q (sympy)
# ──────────────────────────────────────────────────────────────────────

q_sym = sp.symbols("q", positive=True)
h_sym = q_sym - 1 / q_sym


def build_seminormal_matrices_sym(shape: Tuple[int, ...]) -> Tuple[List[sp.Matrix], int]:
    """Build symbolic Hoefsmit seminormal matrices σ_1..σ_{n-1} for partition `shape`.

    Returns (sigmas, dim) where each σ_i is a sympy Matrix in q.
    Mirrors hecke_characters.build_seminormal_matrices but with q symbolic.
    """
    n = sum(shape)
    syts, _, contents = standard_young_tableaux(shape)
    dim = len(syts)
    if dim == 0:
        return [], 0

    sigmas: List[sp.Matrix] = []
    for k_gen in range(1, n):  # σ_{k_gen} swaps entries k_gen and k_gen+1
        rows: List[List[sp.Expr]] = [[sp.S.Zero] * dim for _ in range(dim)]
        processed: set[int] = set()
        for i in range(dim):
            if i in processed:
                continue
            ci_k = syts[i][k_gen]
            ci_k1 = syts[i][k_gen + 1]
            rho = contents[ci_k1] - contents[ci_k]
            a = h_sym / (1 - q_sym ** (-2 * rho))

            # Find swap partner in the SYT list
            swap_map = dict(syts[i])
            swap_map[k_gen] = ci_k1
            swap_map[k_gen + 1] = ci_k
            j = None
            for jj in range(dim):
                if jj == i:
                    continue
                if syts[jj] == swap_map:
                    j = jj
                    break

            if j is None:
                # 1×1 block — eigenvalue is q (rho = +1) or -q⁻¹ (rho = -1)
                rows[i][i] = a
                processed.add(i)
            else:
                a_prime = h_sym / (1 - q_sym ** (2 * rho))  # = a_{-rho}
                # b² = a·a' + 1  (det = -1 normalisation of seminormal block)
                b_sq = sp.together(a * a_prime + 1)
                b = sp.sqrt(b_sq)
                rows[i][i] = a
                rows[j][j] = a_prime
                rows[i][j] = b
                rows[j][i] = b
                processed.add(i)
                processed.add(j)
        sigmas.append(sp.Matrix(rows))
    return sigmas, dim


def torus_braid_matrix(p: int, k: int, lam: Tuple[int, ...]) -> Tuple[sp.Expr, int]:
    """Return (χ_λ(β_{p,k}), dim V_λ) where β_{p,k} = (σ_1 ⋯ σ_{p-1})^k in B_p."""
    sigmas, dim = build_seminormal_matrices_sym(lam)
    if dim == 0:
        return sp.S.Zero, 0
    if p == 1:
        # B_1 is trivial, no generators; (empty product)^k = identity.
        # The only partition is (1) with dim 1, χ = 1.
        return sp.S.One, 1
    # σ_1 σ_2 ⋯ σ_{p-1} (matrices act left-to-right; convention matches hecke_wedderburn)
    base = sp.eye(dim)
    for i in range(p - 1):
        base = sigmas[i] * base
    # k-th power
    full = base ** k
    chi = sp.cancel(full.trace())
    return chi, dim


# ──────────────────────────────────────────────────────────────────────
# Pole order at q = 0
# ──────────────────────────────────────────────────────────────────────

def pole_order_at_zero(expr: sp.Expr) -> int:
    """Return the pole order of `expr` (a rational function in q_sym) at q = 0.

    Pole order = max(0, -valuation_q(expr)).  Computed by writing
    expr = N(q)/D(q), expanding into ℚ[q, q⁻¹], and taking
    (deg of pole of D at 0) - (deg of zero of N at 0).
    """
    if expr.equals(0):
        return 0
    e = sp.cancel(expr)
    n_expr, d_expr = sp.fraction(e)
    n_poly = sp.Poly(sp.expand(n_expr * q_sym ** 0), q_sym)
    d_poly = sp.Poly(sp.expand(d_expr * q_sym ** 0), q_sym)
    # Order at 0 = lowest degree of monomial term
    n_ord = min(n_poly.monoms(), key=lambda m: m[0])[0] if n_poly.terms() else 0
    d_ord = min(d_poly.monoms(), key=lambda m: m[0])[0] if d_poly.terms() else 0
    pole = d_ord - n_ord
    return max(0, int(pole))


def laurent_lowest_power(expr: sp.Expr) -> int:
    """Return the lowest power of q in expr written as a Laurent polynomial.
    Negative => true pole at q = 0; non-negative => regular at q = 0.
    """
    if expr.equals(0):
        return 0
    e = sp.cancel(expr)
    n_expr, d_expr = sp.fraction(e)
    n_poly = sp.Poly(sp.expand(n_expr), q_sym)
    d_poly = sp.Poly(sp.expand(d_expr), q_sym)
    n_low = min(m[0] for m in n_poly.monoms()) if n_poly.terms() else 0
    d_low = min(m[0] for m in d_poly.monoms()) if d_poly.terms() else 0
    return int(n_low - d_low)


# ──────────────────────────────────────────────────────────────────────
# Test bench: (p, k) pairs
# ──────────────────────────────────────────────────────────────────────

TEST_BENCH: List[Tuple[int, int, int]] = [
    # (p, k, expected_alpha_shift_via_kpminus1)
    (2, 3, 3),
    (2, 5, 5),
    (2, 9, 9),
    (3, 4, 8),
    (3, 5, 10),
    (3, 7, 14),
]


def all_column_partition(p: int) -> Tuple[int, ...]:
    """Return the all-anti-symmetric (single column) partition (1, 1, ..., 1) ⊢ p."""
    return tuple([1] * p)


def alpha_shift_per_irrep(p: int, k: int) -> Dict[Tuple[int, ...], Dict[str, object]]:
    """Compute, for every λ ⊢ p, the symbolic χ_λ(T_{p,k}) and its pole order at q=0."""
    out: Dict[Tuple[int, ...], Dict[str, object]] = {}
    for lam in partitions_of(p):
        chi, dim = torus_braid_matrix(p, k, tuple(lam))
        pole = pole_order_at_zero(chi)
        low = laurent_lowest_power(chi)
        out[tuple(lam)] = {
            "chi_symbolic": str(sp.cancel(chi)),
            "dim_V_lambda": int(dim),
            "pole_order_q0": int(pole),
            "lowest_power_q": int(low),
        }
    return out


def alpha_shift(p: int, k: int) -> Tuple[int, Tuple[int, ...], Dict[Tuple[int, ...], Dict[str, object]]]:
    """Return (α_shift(T_{p,k}), maximizer λ, full per-irrep table)."""
    table = alpha_shift_per_irrep(p, k)
    maximizer = max(table.items(), key=lambda kv: kv[1]["pole_order_q0"])
    return int(maximizer[1]["pole_order_q0"]), maximizer[0], table


# ──────────────────────────────────────────────────────────────────────
# Main: produce witness
# ──────────────────────────────────────────────────────────────────────

def main() -> None:
    w = WitnessBuilder("alpha-shift-torus", engine="sympy")
    w.set_description(
        "α_shift(T_{p,k}) := max_{λ⊢p} pole-order at q=0 of χ_λ((σ_1⋯σ_{p-1})^k). "
        "Computed symbolically via Hoefsmit seminormal matrices in q. "
        "Tests the empirical claim α_shift(T_{p,k}) = k(p-1) and that the "
        "maximizer is the all-column irrep V_{(1^p)} for gcd(p,k)=1. "
        "Bridge identity: α_EM⁻¹ = q · [α_shift(T_{2,9})]_q · [α_shift(T_{3,5})]_q."
    )
    w.set_content_block("prop:alpha-shift-torus-knot")
    w.add_caveat(
        "The maximizer-is-V_{(1^p)} statement is verified case-by-case at the "
        "test bench but is not formally proved here; it is the content of "
        "prop:alpha-shift-torus-knot. The equality α_shift = k(p-1) is "
        "asserted as a witness check on each (p,k) below."
    )

    table_dump: Dict[str, Dict[str, object]] = {}
    print("=" * 78)
    print(" α_shift(T_{p,k})  via symbolic Hoefsmit seminormal traces")
    print("=" * 78)
    for (p, k, expected) in TEST_BENCH:
        if gcd(p, k) != 1:
            print(f"  (p, k) = ({p}, {k}) — gcd ≠ 1, skipping")
            continue
        print(f"\n  T_{{{p},{k}}}  in B_{p}")
        a_shift, maximizer, table = alpha_shift(p, k)
        col_part = all_column_partition(p)
        col_pole = int(table[col_part]["pole_order_q0"])
        for lam, row in table.items():
            tag = "  ←  V_{(1^p)}" if lam == col_part else ""
            tag2 = "  ★ MAX" if lam == maximizer else ""
            print(
                f"    λ={lam}: dim={row['dim_V_lambda']:>3}, "
                f"pole_order(q=0)={row['pole_order_q0']:>3}, "
                f"low_power(q)={row['lowest_power_q']:>+3}{tag}{tag2}"
            )
        print(f"    α_shift(T_{{{p},{k}}}) = {a_shift}   (expected k(p-1) = {expected})")
        # Witness-key uses underscores so it round-trips cleanly through JSON.
        key = f"T_{p}_{k}"
        table_dump[key] = {
            "p": p,
            "k": k,
            "alpha_shift": a_shift,
            "maximizer_lambda": list(maximizer),
            "all_column_lambda": list(col_part),
            "all_column_pole_order": col_pole,
            "expected_k_times_p_minus_1": expected,
            "per_irrep": {
                "|".join(map(str, lam)): row for lam, row in table.items()
            },
        }
        # Assertions: (i) α_shift matches k(p-1); (ii) maximizer is V_{(1^p)}.
        w.add_assertion(
            name=f"alpha_shift[{key}]_equals_k_p_minus_1",
            computed=a_shift,
            expected=expected,
        )
        w.add_assertion(
            name=f"maximizer[{key}]_is_V_1_to_p",
            computed=str(list(maximizer)),
            expected=str(list(col_part)),
        )

    w.add_data("torus_knots", table_dump)

    # Final α_EM bridge check at the (2,9) and (3,5) values
    a29 = table_dump.get("T_2_9", {}).get("alpha_shift")
    a35 = table_dump.get("T_3_5", {}).get("alpha_shift")
    bridge_consistent = (a29 == 9 and a35 == 10)
    w.add_data("alpha_em_bridge", {
        "alpha_shift_T_2_9": a29,
        "alpha_shift_T_3_5": a35,
        "claim": "alpha_em_inv = q * [alpha_shift(T_2_9)]_q * [alpha_shift(T_3_5)]_q",
        "matches_em_coupling_projection": bridge_consistent,
    })
    w.add_assertion(
        name="alpha_em_bridge_T29_eq_9",
        computed=int(a29) if a29 is not None else -1,
        expected=9,
    )
    w.add_assertion(
        name="alpha_em_bridge_T35_eq_10",
        computed=int(a35) if a35 is not None else -1,
        expected=10,
    )

    w.add_parameter("test_bench", [list(t) for t in TEST_BENCH])
    out = w.save()
    print(f"\nWitness written: {out}")
    print(f"All passed: {all(a.passed for a in w.assertions)}")


if __name__ == "__main__":
    main()
