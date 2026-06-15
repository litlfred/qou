#!/usr/bin/env python3
"""
Test the Kashaev integration identity claimed in `prop:mass-endomorphism-tower`:

  ∫_0^V (ln_q(1+t)/t) dt  ?=  Φ_q(V)

vs the alternative reconciliation candidate:

  ∫_0^V (ln_q(1+t)/t) dt  ?=  α · ln|V|

where α = m_e · 8G ≈ 3.7445 MeV (Catalan binding scale, but
here we'll factor it out — the integration itself is dimensionless).

The dispute: paper_six_term_isotope_sweep.py uses
  T2 = Σ_i Φ_q(|V̂_i|)
which gives 10^6 Hecke-units (broken at q_0).  But
prop:atomic-braid-mass.md uses
  T_correction = α · Σ_i ln|V̂_i|
which gives 0.19% mean atomic-mass error (works).  Both stem from
the same Briggs-Klein chart integration; one of them is the wrong
Kashaev specialisation step.

ln_q(1+t) is the q-deformed natural log; standard q-calculus form:
  ln_q(1+t) = log(1+t) when q → 1
  ln_q(1+t) = Σ_{n≥1} (-1)^(n+1) t^n / [n]_q   (q-deformation of log series)

with [n]_q = (q^n - q^{-n})/(q - q^{-1}) the q-integer.

This script:
  1. Computes ∫_0^V (ln_q(1+t)/t) dt numerically for several V
  2. Compares to Φ_q(V) and to α·ln|V|
  3. Reports which side of the identity matches

If the integration ≈ ln(V) (up to a multiplicative factor):
  -> the boxed theorem's `Φ_q(|V|)` form is WRONG;
     correct form is `α · ln|V|` (the atomic-braid-mass form)
If the integration ≈ Φ_q(V):
  -> boxed theorem is correct; atomic-braid-mass is the wrong form
If neither:
  -> need to look at the integration kernel more carefully

Output: kashaev-integration-identity.witness.json
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from q_parameter import Q as Q0_FLOAT, Q_MP  # noqa: E402

Q0 = Q_MP


def q_integer(n: int, q: mp.mpf = Q0) -> mp.mpf:
    """[n]_q = (q^n - q^{-n}) / (q - q^{-1}). Symmetric q-integer.

    At q = 1, returns n (the classical limit).
    """
    if n == 0:
        return mp.mpf(0)
    if abs(q - 1) < mp.mpf("1e-30"):
        return mp.mpf(n)
    return (q ** n - q ** (-n)) / (q - 1 / q)


def ln_q(x: mp.mpf, q: mp.mpf = Q0, max_n: int = 200) -> mp.mpf:
    """q-deformed natural log: ln_q(1 + t) = Σ_n (-1)^(n+1) t^n / [n]_q.

    For x = 1 + t, this gives the q-log of x.  Convergence requires
    |t| < radius (depends on q).  At q = 1 this reduces to standard
    log series.
    """
    t = x - 1
    if abs(t) >= 1:
        # Series diverges; fall back to integral or expansion around different point
        return mp.mpf("nan")
    total = mp.mpf(0)
    for n in range(1, max_n + 1):
        qint_n = q_integer(n, q)
        if abs(qint_n) < mp.mpf("1e-300"):
            continue
        term = (-1) ** (n + 1) * t ** n / qint_n
        total += term
        if abs(term) < mp.mpf("1e-40"):
            break
    return total


def integrand_kashaev(t: mp.mpf, q: mp.mpf = Q0) -> mp.mpf:
    """ln_q(1+t) / t — the Briggs-Klein integrand."""
    if abs(t) < mp.mpf("1e-50"):
        # Limit as t → 0: ln_q(1+t)/t → t/[1]_q ÷ t = 1/[1]_q = 1 (since [1]_q = 1)
        return mp.mpf(1)
    return ln_q(1 + t, q) / t


def integrate_kashaev(V: mp.mpf, q: mp.mpf = Q0, n_steps: int = 1000) -> mp.mpf:
    """∫_0^V (ln_q(1+t)/t) dt via mpmath quadrature."""
    return mp.quad(lambda t: integrand_kashaev(mp.mpf(t), q), [0, V])


def phi_q_product(V: mp.mpf, q: mp.mpf = Q0, K: int = 200) -> mp.mpf:
    """Φ_q(V) = Π_{k≥1} (1 - q^{-k} V)^{-1}."""
    prod = mp.mpf(1)
    qi = 1 / q
    for k in range(1, K + 1):
        factor = 1 - qi ** k * V
        if abs(factor) < mp.mpf("1e-300"):
            return mp.inf
        prod /= factor
        if abs(qi ** k * V) < mp.mpf("1e-60"):
            break
    return prod


def main() -> int:
    print("=" * 90)
    print("  Kashaev integration identity probe")
    print(f"  q_0 = {float(Q0):.10f}")
    print(f"  α = m_e · 8G = {float(mp.mpf('0.51099895') * 8 * mp.catalan):.6f} MeV")
    print("=" * 90)

    # Sanity: ln_q at q=1 should be log
    print("\n  Sanity check ln_q at q=1:")
    for x in (mp.mpf("1.5"), mp.mpf("0.8")):
        ln_q_val = ln_q(x, mp.mpf(1))
        log_val = mp.log(x)
        print(f"    ln_{{q=1}}({float(x):.2f}) = {float(ln_q_val):.6f}  "
              f"vs log(x) = {float(log_val):.6f}  "
              f"{'✓' if abs(ln_q_val - log_val) < 1e-6 else '✗'}")

    # Integration vs Φ_q vs ln|V| at q_0
    print("\n  Test points |V| ∈ (0, 1):  integral vs Φ_q vs ln|V|")
    print(f"  {'V':>8}  {'∫ kashaev':>14}  {'Φ_q(V)':>14}  {'ln(V)':>14}  "
          f"{'integral/ln(V)':>14}  {'integral/Φ_q':>14}")
    print("  " + "-" * 100)
    rows = []
    for V_float in (0.1, 0.3, 0.5, 0.7, 0.85, 0.95, 0.989):
        V = mp.mpf(str(V_float))
        try:
            integral = integrate_kashaev(V)
        except Exception as e:
            print(f"    V={V_float}: integration failed: {e}")
            continue
        phi = phi_q_product(V)
        ln_V = mp.log(V)
        ratio_ln = float(integral / ln_V) if abs(ln_V) > mp.mpf("1e-30") else float("nan")
        ratio_phi = float(integral / phi) if abs(phi) > mp.mpf("1e-30") else float("nan")
        print(f"  {V_float:>8.3f}  {float(integral):>+14.6e}  "
              f"{float(phi):>+14.4e}  {float(ln_V):>+14.6e}  "
              f"{ratio_ln:>+14.6f}  {ratio_phi:>+14.6e}")
        rows.append({
            "V": V_float,
            "integral": float(integral),
            "phi_q": float(phi),
            "log_V": float(ln_V),
            "integral_over_log_V": ratio_ln,
            "integral_over_phi_q": ratio_phi,
        })

    # Verdict
    print("\n  Interpretation:")
    print("    if integral / ln(V) ≈ constant: integration ~ const · ln(V), supports atomic-braid-mass form")
    print("    if integral / Φ_q   ≈ constant: integration ~ const · Φ_q,  supports six-term theorem form")

    # Assess which is more constant
    ln_ratios = [r["integral_over_log_V"] for r in rows if not (r["integral_over_log_V"] != r["integral_over_log_V"])]
    phi_ratios = [r["integral_over_phi_q"] for r in rows if not (r["integral_over_phi_q"] != r["integral_over_phi_q"])]

    if ln_ratios and len(ln_ratios) > 1:
        ln_min = min(ln_ratios)
        ln_max = max(ln_ratios)
        ln_spread = (ln_max - ln_min) / abs(ln_min) if ln_min else float("nan")
        print(f"\n    integral/ln(V) range: [{ln_min:.4e}, {ln_max:.4e}], spread = {ln_spread*100:.2f}%")
    if phi_ratios and len(phi_ratios) > 1:
        phi_min = min(phi_ratios)
        phi_max = max(phi_ratios)
        phi_spread = (phi_max - phi_min) / abs(phi_min) if phi_min else float("nan")
        print(f"    integral/Φ_q   range: [{phi_min:.4e}, {phi_max:.4e}], spread = {phi_spread*100:.2f}%")

    witness = {
        "computation": "kashaev-integration-identity",
        "description": (
            "Numerical test of the Kashaev integration identity from "
            "prop:mass-endomorphism-tower. Compares ∫_0^V (ln_q(1+t)/t) dt "
            "to Φ_q(V) and to ln|V| to determine which form the "
            "integration evaluates to.  Resolves the conflict between "
            "prop:atomic-braid-mass (uses α·Σ ln|V_i|) and "
            "thm:knot-mass-formula-unified (uses Σ Φ_q(|V_i|)) at q_0."
        ),
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "rows": rows,
    }
    out = HERE / "kashaev-integration-identity.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
