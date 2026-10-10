#!/usr/bin/env python3
"""
Cup-product tower probe: does tr_M(σ_0^k) match Φ_q Cauchy expansion?

Per prop:terms-2-6-higher-operations, Term 2's Cauchy Φ_q kernel
is proposed to arise from the cup-product tower

    Σ_{k≥1} (q^{-k}/(q;q)_k) · [σ_i]^{∪ k}

paired with tr_M.  The simplest concrete check:

  Compute tr_M(σ_0^k) for k = 1..N  using Hecke relation
  σ_0² = h·σ_0 + 1 (h = q - q⁻¹).

  Compare to Φ_q Cauchy series coefficients Σ z^k / (q;q)_k.

Symbolic sympy throughout (q kept as symbol).

Witness: cup-product-tower.witness.json
"""
import json
import sys
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction

import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0_FLOAT

q = sp.Symbol('q', positive=True, real=True)
q0 = sp.Rational(int(Q0_FLOAT * 10 ** 16), 10 ** 16)
h = q - 1/q  # Hecke deformation


def q_pochhammer(n):
    """(q; q)_n = Π_{k=1}^n (1 - q^k)."""
    r = sp.Integer(1)
    for k in range(1, n + 1):
        r *= 1 - q ** k
    return sp.expand(r)


def sigma_0_power_reduction(k):
    """Reduce σ_0^k to a·σ_0 + b using Hecke relation σ_0² = h·σ_0 + 1.
    Returns (a, b) as sympy expressions in q."""
    if k == 0:
        return (sp.Integer(0), sp.Integer(1))  # identity
    if k == 1:
        return (sp.Integer(1), sp.Integer(0))
    a_prev, b_prev = sigma_0_power_reduction(k - 1)
    # σ_0^k = σ_0 · σ_0^{k-1} = σ_0 · (a_prev σ_0 + b_prev)
    #       = a_prev · σ_0² + b_prev · σ_0
    #       = a_prev · (h σ_0 + 1) + b_prev · σ_0
    #       = (a_prev · h + b_prev) · σ_0 + a_prev
    a_new = sp.expand(a_prev * h + b_prev)
    b_new = sp.expand(a_prev)
    return a_new, b_new


def markov_trace_sigma_0_power(k):
    """tr_M(σ_0^k) in H_3(q): with σ_0^k = a σ_0 + b,
    tr_M = a · z + b · 1 where z = 1/(q^{1/2} + q^{-1/2})."""
    a, b = sigma_0_power_reduction(k)
    z = 1 / (q ** sp.Rational(1, 2) + q ** sp.Rational(-1, 2))
    return sp.expand(a * z + b)


def phi_q_taylor_coeff(k):
    """k-th Taylor coefficient of Φ_q(z) in the Cauchy expansion:
      Φ_q(z) = Σ_{k≥0} z^k / (q; q)_k.
    Returns 1/(q; q)_k."""
    if k == 0:
        return sp.Integer(1)
    return 1 / q_pochhammer(k)


if __name__ == "__main__":
    print("CUP-PRODUCT TOWER PROBE — tr_M(σ_0^k) vs Φ_q Cauchy expansion")
    print("=" * 80)
    print(f"q_0 = {float(Q0_FLOAT)}")
    print(f"h = q - q⁻¹")
    print()

    print(f"{'k':>3}  {'tr_M(σ_0^k) symbolic':<50}  {'value @ q_0':>14}")
    print('-' * 80)
    results = []
    for k in range(1, 6):
        tr = markov_trace_sigma_0_power(k)
        tr_simpl = sp.simplify(tr)
        tr_q0 = float(tr.subs(q, q0).evalf(30))
        tr_q0_polynomial_q = expose_polynomial(tr, q)
        print(f"{k:>3}  {str(tr_simpl)[:48]:<50}  {tr_q0:>14.6f}")
        results.append({
            "k": k,
            "tr_M_symbolic": str(tr_simpl),
            "tr_M_at_q0": tr_q0,
        })

    print()
    print("Φ_q Cauchy Taylor coefficients 1/(q;q)_k at q_0:")
    for k in range(0, 6):
        pq = q_pochhammer(k)
        coeff = sp.Rational(1) if k == 0 else 1 / pq
        coeff_q0 = float(coeff.subs(q, q0).evalf(30))
        coeff_q0_polynomial_q = expose_polynomial(coeff, q)
        print(f"  k={k}:  1/(q;q)_{k} = {str(sp.simplify(coeff))[:40]:<40}  "
              f"@ q_0 = {coeff_q0:.6f}")
        if k > 0 and results[k-1]['k'] == k:
            results[k-1]["phi_q_coeff_at_q0"] = coeff_q0
            results[k-1]["ratio_trM_over_phi_coeff"] = (
                results[k-1]["tr_M_at_q0"] / coeff_q0
            )

    print()
    print("Ratio tr_M(σ_0^k) / (1/(q;q)_k) at q_0:")
    print(f"{'k':>3}  {'tr_M':>12}  {'1/(q;q)_k':>12}  {'ratio':>14}")
    print('-' * 60)
    for r in results:
        if "phi_q_coeff_at_q0" in r:
            print(f"{r['k']:>3}  {r['tr_M_at_q0']:>12.6f}  "
                  f"{r['phi_q_coeff_at_q0']:>12.6f}  "
                  f"{r['ratio_trM_over_phi_coeff']:>14.6f}")

    # Check: does tr_M(σ_0^k) form a geometric series related to Φ_q at z = z_markov?
    print()
    print("Comparing to Φ_q(z_markov) expansion:")
    z_m = 1 / (q ** sp.Rational(1, 2) + q ** sp.Rational(-1, 2))
    phi_q_at_zm_taylor = sum(z_m ** k / q_pochhammer(k) for k in range(0, 6))
    print(f"  Φ_q(z)[partial sum k=0..5] = {phi_q_at_zm_taylor}")
    print(f"  Φ_q(z)[partial sum @ q_0] = "
          f"{float(phi_q_at_zm_taylor.subs(q, q0).evalf(30))}")
    print()

    # Alternative hypothesis: tr_M(σ_0^k) ~ z · q^{k(k-1)/2} (q-deformation)
    # or tr_M(σ_0^k) ~ z · [k]_q (linear in q-integer)
    print("Alternative hypothesis tests:")
    print("  Ratios of consecutive tr_M values:")
    for k in range(2, 6):
        ratio = results[k-1]["tr_M_at_q0"] / results[k-2]["tr_M_at_q0"]
        print(f"    tr_M(σ_0^{k}) / tr_M(σ_0^{k-1}) = {ratio:.6f}")

    witness = {
        "computation": "cup-product-tower-probe",
        "description": (
            "Tests whether Markov traces of σ_0 powers match the "
            "Φ_q Cauchy Taylor expansion (the proposed cup-product "
            "tower identification for Term 2)."
        ),
        "reference_blocks": [
            "prop:terms-2-6-higher-operations",
            "prop:mass-endomorphism-tower",
            "prop:gb-spectral-sequence",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q_0": float(Q0_FLOAT)},
        "results": results,
    }
    out = Path(__file__).parent / "cup-product-tower.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
