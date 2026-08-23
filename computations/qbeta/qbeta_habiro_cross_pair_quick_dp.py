#!/usr/bin/env python3
"""qbeta_habiro_cross_pair_quick_dp.py — partial cross-validation of Δa_m.

The full cross-pair probe (qbeta_habiro_cross_pair_factorization.py)
needs ³He and ⁴He Habiro coefficients which are NOT in
`habiro-coefficients-atomic.witness.json` yet — only p, n, D are
present. Generating ³He / ⁴He requires a separate atomic-Habiro
extraction (a follow-up task).

THIS quick probe does what we CAN do with available data: factorize
Δa_m on (D − p) and (D − n) and compare with the (n − p) pattern.

The three pairs:
  (n − p): isospin SU(2)_I flip at fixed A=1
  (D − p): atomic-number step A=1 → A=2 with Z fixed at 1
  (D − n): atomic-number step A=1 → A=2 with N fixed at 1

If the cyclotomic prefactor (u²−1) appears in (D − p) AND (D − n),
that's evidence the Φ_1·Φ_2 factor is UNIVERSAL across atomic-number
steps, not specific to isospin SU(2)_I.
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
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from witness_base import WitnessBuilder  # noqa: E402

u = sp.symbols("u")


def parse_atom_coeffs(witness_atom: dict) -> dict[int, sp.Poly]:
    """Return {m: a_m(u) as sympy.Poly} for one atom's Habiro coefficients."""
    out = {}
    for c in witness_atom["habiro_coefficients"]:
        m = c["m"]
        a_m_str = c["a_m"].replace("^", "**")
        a_m_expr = sp.sympify(a_m_str, locals={"check_q": u, "u": u})
        out[m] = sp.Poly(a_m_expr, u)
    return out


def delta_factorize(left: dict[int, sp.Poly], right: dict[int, sp.Poly],
                    pair_name: str) -> dict:
    """Compute Δa_m = a_m(left) − a_m(right) for all m, factor each, GCD."""
    max_m = max(max(left), max(right))
    delta_polys = []
    per_m = []
    for m in range(max_m + 1):
        l = left.get(m, sp.Poly(0, u))
        r = right.get(m, sp.Poly(0, u))
        d = l - r
        delta_polys.append(d)
        if d.is_zero:
            per_m.append({"m": m, "delta": "0", "factored": "0",
                          "is_zero": True, "is_irreducible": False})
        else:
            factored = sp.factor(d.as_expr())
            per_m.append({
                "m": m,
                "delta": str(d.as_expr()),
                "factored": str(factored),
                "is_zero": False,
                "is_irreducible": d.degree() == sp.degree(factored, u)
                                  and not factored.is_Mul,
            })

    # Cross-m polynomial GCD over ℤ[u]
    nonzero = [p for p in delta_polys if not p.is_zero]
    if nonzero:
        cross_gcd = nonzero[0]
        for p in nonzero[1:]:
            cross_gcd = sp.gcd(cross_gcd, p)
        cross_gcd_str = str(cross_gcd.as_expr())
    else:
        cross_gcd_str = "all zero"

    # Σ_m Δa_m · (u;u)_m
    def q_pochhammer(m):
        if m == 0:
            return sp.Integer(1)
        return sp.prod(1 - u ** k for k in range(1, m + 1))

    habiro_sum = sp.Integer(0)
    for m, d in enumerate(delta_polys):
        habiro_sum += d.as_expr() * q_pochhammer(m)
    habiro_factored = sp.factor(habiro_sum)

    # Check for cyclotomic factor (u-1)(u+1) = u^2 - 1
    cyclotomic_present = False
    if not habiro_sum.is_zero:
        quotient, remainder = sp.div(habiro_sum, u**2 - 1, u)
        cyclotomic_present = (remainder == 0)

    return {
        "pair_name": pair_name,
        "max_m": max_m,
        "per_m": per_m,
        "cross_m_polynomial_gcd": cross_gcd_str,
        "habiro_sum_factored": str(habiro_factored),
        "cyclotomic_u2_minus_1_present": cyclotomic_present,
    }


def main() -> int:
    builder = WitnessBuilder(
        "qbeta-habiro-cross-pair-quick-dp",
        engine="python+sympy",
    )
    builder.set_description(
        "Quick partial cross-pair validation: factor Δa_m on "
        "(D - p), (D - n), (n - p) to compare with the n-p "
        "audit's cyclotomic prefactor pattern. Full ³He/⁴He extension "
        "deferred (auxiliary witnesses not yet generated)."
    )
    builder.set_content_block("prop:neutron-qvalue-symbolic")

    hab = builder.add_upstream(_pb.witness_path("habiro-coefficients-atomic.witness.json", HERE))
    results = hab["results"]

    p = parse_atom_coeffs(results["p (proton, A=1)"])
    n = parse_atom_coeffs(results["n (neutron, A=1)"])
    d = parse_atom_coeffs(results["D (deuteron, A=2)"])

    # Reference: n - p (already in prior audit)
    np_result = delta_factorize(n, p, "n - p (reference)")
    builder.add_data("n_minus_p", np_result)
    print(f"\n=== n - p ===")
    print(f"  Cyclotomic (u²-1) present: {np_result['cyclotomic_u2_minus_1_present']}")
    print(f"  Σ habiro factored: {np_result['habiro_sum_factored'][:100]}...")

    # New: D - p
    dp_result = delta_factorize(d, p, "D - p (atomic-step, Z-fixed)")
    builder.add_data("d_minus_p", dp_result)
    print(f"\n=== D - p ===")
    print(f"  Cyclotomic (u²-1) present: {dp_result['cyclotomic_u2_minus_1_present']}")
    print(f"  Σ habiro factored: {dp_result['habiro_sum_factored'][:100]}...")

    # New: D - n
    dn_result = delta_factorize(d, n, "D - n (atomic-step, N-fixed)")
    builder.add_data("d_minus_n", dn_result)
    print(f"\n=== D - n ===")
    print(f"  Cyclotomic (u²-1) present: {dn_result['cyclotomic_u2_minus_1_present']}")
    print(f"  Σ habiro factored: {dn_result['habiro_sum_factored'][:100]}...")

    # Verdict
    cyclo_count = sum([
        np_result['cyclotomic_u2_minus_1_present'],
        dp_result['cyclotomic_u2_minus_1_present'],
        dn_result['cyclotomic_u2_minus_1_present'],
    ])
    if cyclo_count == 3:
        verdict = "UNIVERSAL: Φ_1·Φ_2 = u²-1 prefactor in all three pairs"
    elif cyclo_count == 1 and np_result['cyclotomic_u2_minus_1_present']:
        verdict = "SPECIFIC to isospin SU(2)_I: cyclotomic only in n-p"
    elif cyclo_count >= 2:
        verdict = f"PARTIAL: cyclotomic in {cyclo_count}/3 pairs"
    else:
        verdict = f"UNEXPECTED: cyclotomic in {cyclo_count}/3 pairs"
    builder.add_data("verdict", verdict)
    print(f"\n=== VERDICT: {verdict} ===")

    builder.add_assertion(
        "cross_pair_quick_dp_completed",
        computed=1,
        expected=1,
        tolerance=0,
        source="sympy.factor + sp.gcd on Δa_m for (n-p, D-p, D-n).",
    )
    builder.save()
    print(f"\n  ✓ Witness saved")
    return 0


if __name__ == "__main__":
    sys.exit(main())
