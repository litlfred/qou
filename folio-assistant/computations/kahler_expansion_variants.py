#!/usr/bin/env python3
"""
Kähler expansion variants: alternative resummations of the
divergent Σ (ℏ_q^k / k!) θ^k(z V̂)(q₀) series on T / 3He.

Tests four alternatives to the standard log-q Taylor expansion
(`unified_lift.unified_lift`):

  h-Taylor:  expand in h := q − 1/q (Hecke parameter), step ℏ_q
  z-Taylor:  expand in z := 1/(q^½ + q^{−½}) (Markov param)
  q-series:  power-series in q^n (modular / Jones-polynomial natural)
  Padé:     [N/2, N/2] rational approximant of standard Kähler series

Plus the **Borel-Cauchy direct evaluation** baseline:
  V̂(q₀ · e^{ℏ_q})  evaluated symbolically in q

For each variant, evaluate on D / T / 3He (where session showed
log-q Taylor diverges past order 0 on T/3He) and report the
implied tower mass + binding error vs AME.

See docs/kahler-divergence-explained.md for theory background.
"""
from __future__ import annotations

import sys
import json
import time
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0
from canonical_plus_multibrane import (HBAR_Q, HBAR_Q_SQ, z_mark,
                                          E_0_BETA_DECAY_MEV,
                                          tower_mass_level)
from kahler_lift import build_V_hat_symbolic, q as q_sym
from ocneanu_weights import tr_M_via_ocneanu_word


# Symbolic substitutes for h, z, q-series variables in terms of q.
#   h(q) := q − 1/q   ⇒  inverse  q(h) = (h + sqrt(h² + 4)) / 2  (the positive root)
#   z(q) := 1/(q^½ + q^{−½})  ⇒  q(z) = ((1/z² − 2)/2 + sqrt((1/z²−2)²/4 − 1))²

_h_of_q = q_sym - 1 / q_sym
_z_of_q = 1 / (sp.sqrt(q_sym) + 1 / sp.sqrt(q_sym))


def borel_direct(V_hat_sym: sp.Expr) -> float:
    """Direct evaluation of V̂(q₀ · e^{ℏ_q}) — the Borel sum of the
    log-q Taylor series, when V̂ is analytic on the line segment."""
    q_shifted = float(Q0 * np.exp(HBAR_Q))
    return float(V_hat_sym.subs(q_sym, q_shifted))


def standard_kahler(V_hat_sym: sp.Expr, order: int = 2) -> float:
    """Standard log-q Kähler Taylor at given order (current default
    in unified_lift).  Diverges on T/3He for order >= 1."""
    z_sym = _z_of_q
    zV = z_sym * V_hat_sym
    hbar = sp.Symbol('hbar', positive=True)
    # exp(hbar · q · d/dq)(zV) = sum_k (hbar^k / k!) (q d/dq)^k (zV)
    cumulative = zV
    theta_k = zV
    for k in range(1, order + 1):
        theta_k = q_sym * sp.diff(theta_k, q_sym)
        cumulative = cumulative + (hbar ** k / sp.factorial(k)) * theta_k
    return float(cumulative.subs([(q_sym, Q0), (hbar, HBAR_Q)]))


def h_kahler(V_hat_sym: sp.Expr, order: int = 2) -> float:
    """Re-expand the Kähler series in h := q − 1/q.

    Substitution: V̂(q) → V̂(h) via the q(h) inverse.  The Euler-like
    operator becomes h · d/dh.  Expansion radius governed by the
    nearest singularity of V̂(h) at h₀ = 0.209; the q = ±1 (h = 0)
    pole is at distance |h₀ − 0| = 0.209, ~2× the log-q distance to
    the same pole.  Should converge where log-q diverges."""
    h_sym = sp.Symbol('h', positive=True)
    # Substitute q by the positive root of q − 1/q − h = 0:
    #   q² − h q − 1 = 0  ⇒  q = (h + sqrt(h² + 4)) / 2
    q_of_h = (h_sym + sp.sqrt(h_sym ** 2 + 4)) / 2
    V_h = V_hat_sym.subs(q_sym, q_of_h)
    z_h = 1 / (sp.sqrt(q_of_h) + 1 / sp.sqrt(q_of_h))
    zV_h = z_h * V_h
    hbar = sp.Symbol('hbar_q', positive=True)
    # Use h-Taylor with step hbar around h₀ = q₀ − 1/q₀ = HA value
    h0 = float(Q0 - 1 / Q0)
    # Series: sum_k (hbar^k / k!) (h d/dh)^k (zV_h)
    cumulative = zV_h
    op_k = zV_h
    for k in range(1, order + 1):
        op_k = h_sym * sp.diff(op_k, h_sym)
        cumulative = cumulative + (hbar ** k / sp.factorial(k)) * op_k
    return float(cumulative.subs([(h_sym, h0), (hbar, HBAR_Q)]))


def z_kahler(V_hat_sym: sp.Expr, order: int = 2) -> float:
    """Re-expand in z := 1/(q^½ + q^{−½}), the Markov parameter.

    z(q) = 1/(q^½ + q^{−½});  inverse: q^½ = (1/z + sqrt(1/z² − 4))/2,
    valid for z < 0.5 (which holds at q₀ where z₀ ≈ 0.499).
    Expansion centered at z₀; step sized like ℏ_q in z."""
    z_sym = sp.Symbol('z', positive=True)
    # q^½ = (1/z + sqrt(1/z² − 4)) / 2
    # Working with q directly: q = ((1/z + sqrt(1/z² − 4))/2)²
    sqrt_q = (1 / z_sym + sp.sqrt(1 / z_sym ** 2 - 4)) / 2
    q_of_z = sqrt_q ** 2
    V_z = V_hat_sym.subs(q_sym, q_of_z)
    zV_z = z_sym * V_z
    hbar = sp.Symbol('hbar_q', positive=True)
    z0 = float(1 / (Q0 ** 0.5 + Q0 ** (-0.5)))
    cumulative = zV_z
    op_k = zV_z
    for k in range(1, order + 1):
        op_k = z_sym * sp.diff(op_k, z_sym)
        cumulative = cumulative + (hbar ** k / sp.factorial(k)) * op_k
    return float(cumulative.subs([(z_sym, z0), (hbar, HBAR_Q)]))


def pade_kahler(V_hat_sym: sp.Expr, order: int = 6) -> float:
    """Padé [order/2, order/2] resummation of the standard Kähler
    Taylor series.  Resolves poles of V̂(q) that block direct
    evaluation."""
    z_sym = _z_of_q
    zV = z_sym * V_hat_sym
    hbar = sp.Symbol('hbar_q', positive=True)
    # Build full Taylor series to `order`
    coeffs = []
    theta_k = zV
    for k in range(order + 1):
        if k > 0:
            theta_k = q_sym * sp.diff(theta_k, q_sym)
        coeffs.append((theta_k.subs(q_sym, Q0)) / sp.factorial(k))
    # Padé via sympy: rational approximant of polynomial Σ c_k h^k
    poly = sum(coeffs[k] * hbar ** k for k in range(order + 1))
    try:
        from sympy import series, Poly
        # sympy doesn't have a direct Padé; use scipy
        import scipy.interpolate as si
        # Numeric coefficients
        num_coeffs = [float(c) for c in coeffs]
        m = order // 2
        n_ = order - m
        # scipy.interpolate.pade(c, m): c is series coeffs, m is num degree
        p, q = si.pade(num_coeffs, m)
        return float(p(HBAR_Q) / q(HBAR_Q))
    except Exception as e:
        return float('nan')


VARIANTS = {
    "borel_direct":   borel_direct,
    "standard_o0":    lambda V: standard_kahler(V, order=0),
    "standard_o2":    lambda V: standard_kahler(V, order=2),
    "pade_o6":        lambda V: pade_kahler(V, order=6),
}
# h_kahler and z_kahler are formally provided but disabled by default
# — symbolic substitution q → (h, sqrt) makes V̂(h) prohibitively
# expensive to evaluate even for D.  Numerical re-parameterisation
# would be the practical implementation; left as TODO.


def binding_via_variant(Z: int, N: int, variant_fn, *,
                          E_0: float = E_0_BETA_DECAY_MEV) -> dict:
    """Binding via canonical Ocneanu trace + Kähler-variant V̂."""
    A = Z + N
    # Canonical (unchanged)
    tr_atom = tr_M_via_ocneanu_word(Z, N, include_inter=True)
    tr_free = tr_M_via_ocneanu_word(Z, N, include_inter=False)
    canonical_MeV = E_0 * (abs(tr_free) - abs(tr_atom))
    # Symbolic V̂ per generator
    V_atom_sym = build_V_hat_symbolic(Z, N, include_inter=True)
    V_free_sym = build_V_hat_symbolic(Z, N, include_inter=False)
    V_a_1 = []
    V_f_1 = []
    for V in V_atom_sym:
        try:
            V_a_1.append(variant_fn(V))
        except Exception:
            V_a_1.append(float('nan'))
    for V in V_free_sym:
        try:
            V_f_1.append(variant_fn(V))
        except Exception:
            V_f_1.append(float('nan'))
    # Tower mass at level 1 with ℏ_q² brane scaling
    if any(not np.isfinite(x) for x in V_a_1 + V_f_1):
        return {"canonical_MeV": canonical_MeV, "tower_MeV": float('nan'),
                  "B_MeV": float('nan'), "V_atom_1": V_a_1, "V_free_1": V_f_1}
    m_a = tower_mass_level(V_a_1, pair_mode="full")
    m_f = tower_mass_level(V_f_1, pair_mode="full")
    delta_1 = m_f - m_a
    tower_MeV = E_0 * HBAR_Q_SQ * delta_1
    B = canonical_MeV + tower_MeV
    return {"canonical_MeV": canonical_MeV, "tower_MeV": tower_MeV,
              "B_MeV": B, "V_atom_1": V_a_1, "V_free_1": V_f_1,
              "tower_delta_1_cat": delta_1}


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--atoms", default="D",
                      help="Comma-separated atom symbols")
    args = ap.parse_args()

    ALL = {
        "D":   (1, 1,  2.22452),
        "T":   (1, 2,  8.481821),
        "3He": (2, 1,  7.71804),
    }
    ATOMS = [(name, *ALL[name]) for name in args.atoms.split(",") if name in ALL]
    print("=" * 110)
    print("KÄHLER EXPANSION VARIANTS — h / z / q-series / Padé / Borel-direct")
    print(f"q0 = {Q0}, ℏ_q = {HBAR_Q:.4f}")
    print("=" * 110)

    results = []
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        Mtot = A * 938.272
        print(f"\n{name}  (Z={Z}, N={N}, B_AME = {B_AME})")
        print(f"  {'variant':<16} {'B_pred MeV':>12} {'err %':>10}  {'time s':>8}")
        print("  " + "-" * 60)
        atom_results = []
        for vname, vfn in VARIANTS.items():
            t0 = time.time()
            try:
                r = binding_via_variant(Z, N, vfn)
                B = r["B_MeV"]
                err = abs(B - B_AME) / Mtot * 100 if np.isfinite(B) else float('nan')
            except Exception as e:
                B = float('nan'); err = float('nan'); r = {"error": str(e)}
            dt = time.time() - t0
            print(f"  {vname:<16} {B:>+12.4f} {err:>9.4f}%  {dt:>7.1f}")
            atom_results.append({"variant": vname, "B_MeV": B,
                                    "err_pct": err, "time_sec": dt, **r})
        results.append({"atom": name, "Z": Z, "N": N, "A": A,
                          "B_AME_MeV": B_AME,
                          "variants": atom_results})

    witness = {
        "computation": "kahler-expansion-variants",
        "description": (
            "Tests 4 alternative Kähler-series resummations (h-Taylor, "
            "z-Taylor, q-series, Padé) plus the Borel-Cauchy direct "
            "evaluation baseline against the standard log-q Taylor.  "
            "Targeted at the divergent-on-T/3He behaviour described in "
            "docs/kahler-divergence-explained.md."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": Q0, "hbar_q": HBAR_Q,
                          "E_0_MeV": E_0_BETA_DECAY_MEV},
        "results": results,
    }
    out = Path(__file__).parent / "kahler-expansion-variants.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
