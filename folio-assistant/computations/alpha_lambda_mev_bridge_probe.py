#!/usr/bin/env python3
"""Probe the α_λ (dimensionless) → α_k (MeV) units bridge.

The depth-resolved-phi-k-hoefsmit pipeline uses fitted α_k in MeV
that absorb the divergent q-deformed Plancherel weight. My structural
α_λ from PR #427 are dimensionless O(0.1, 1).

Hypothesis: there exists a physical-coupling constant κ such that

    α_k_MeV (fitted)  =  m_e · α_k_struct · κ

If κ is constant across k, the bridge is well-defined and 1-ppb
predictions become accessible from the structural derivation.

Test: compute the ratio at H_3 and H_4 across all available depths.

H_3 closed forms (PR #427):
    α_0 = 1
    α_1 = 0
    α_2 = z²
    α_3 = h·z² + z

H_4 closed forms (PR #427):
    α_(4)   = +0.93506343  (depth 0)
    α_(3,1) = -0.77208134  (depth 1)
    α_(2,2) = -0.21145633  (depth 1)
    α_(2,1,1) = +0.09693702 (depth 2)
    α_(1^4) = +0.00346252  (depth 3)

Fitted α_k from depth-resolved-phi-k-hoefsmit.witness.json (4-cal,
calibrating on p, n, D, T): α_k_MeV ≈
    α_0 = -0.003
    α_1 = +0.000 (vanishing)
    α_2 = +18.5
    α_3 = -1.7
    α_4 = +23.6
    α_5 = +16.0
    α_6 = +1.7
    α_7 = +0.05
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

import mpmath as mp

mp.mp.dps = 30

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0_FLOAT

q = mp.mpf(repr(Q0_FLOAT))
qi = 1 / q
z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))
h = q - qi
m_e = mp.mpf("0.51099895")  # MeV


def main():
    # Structural α_k at H_3 from closed forms
    alpha_struct_h3 = {
        0: mp.mpf(1),
        1: mp.mpf(0),
        2: z ** 2,
        3: h * z ** 2 + z,
    }

    # Structural α_λ at H_4 from PR #427 (per-partition, sum over depth k)
    # Depth 0: α_(4) = +0.93506343
    # Depth 1: α_(3,1) + α_(2,2) = -0.77208134 + -0.21145633 = -0.98353767
    # Depth 2: α_(2,1,1) = +0.09693702
    # Depth 3: α_(1^4) = +0.00346252
    alpha_struct_h4 = {
        0: mp.mpf("+0.93506343"),
        1: mp.mpf("-0.77208134") + mp.mpf("-0.21145633"),
        2: mp.mpf("+0.09693702"),
        3: mp.mpf("+0.00346252"),
    }

    # Fitted α_k from depth-resolved-phi-k-hoefsmit.witness.json (load from main)
    # NOTE: these are the 4-cal-fitted α_k in the q-deformed Plancherel basis,
    # which has a DIFFERENT depth normalization than my structural α_λ.
    try:
        with open(Path(__file__).parent /
                  "depth-resolved-phi-k-hoefsmit.witness.json") as f:
            w = json.load(f)
        alpha_fit_mev = w.get("fitted_alpha_k_MeV", [])
    except FileNotFoundError:
        alpha_fit_mev = []

    if not alpha_fit_mev:
        print("WARN: depth-resolved-phi-k-hoefsmit.witness.json not found.")
        print("Falling back to documented values from PR #427 commit notes.")
        alpha_fit_mev = [
            -0.0027430560162517987,
             1.0758330955003281e-15,  # ≈ 0
            18.47891980079045,
            -1.733461014000000,
            23.608187000000000,
            15.997489000000000,
             1.734763000000000,
             0.050522000000000,
        ]

    print("=" * 90)
    print("PROBE: α_k(MeV, fitted) vs m_e · α_k(structural, dimensionless)")
    print("=" * 90)
    print(f"q_0 ≈ {float(q):.6f}, m_e = {float(m_e)} MeV, z = {float(z):.6f}")
    print()

    # H_3 comparison
    print("Test 1: H_3 closed-form α_k (4-stratum)")
    print(f"{'k':>3} {'α_k_struct':>14} {'m_e·α_struct':>15} {'α_k_fit_MeV':>15} {'κ = fit/(m_e·struct)':>25}")
    print("-" * 90)
    h3_kappas = []
    for k in [0, 1, 2, 3]:
        s = alpha_struct_h3[k]
        m_s = m_e * s
        if k < len(alpha_fit_mev):
            f = mp.mpf(repr(alpha_fit_mev[k]))
            if abs(m_s) > mp.mpf('1e-15'):
                kappa = f / m_s
                kappa_str = f"{float(kappa):>+24.6f}"
                h3_kappas.append((k, kappa))
            else:
                kappa_str = "    (m_s ≈ 0, undef)"
            print(f"{k:>3} {float(s):>+14.8f} {float(m_s):>+15.10f} "
                  f"{float(f):>+15.8f} {kappa_str}")
    print()

    # H_4 comparison
    print("Test 2: H_4 depth-summed α_k (4-stratum)")
    print(f"{'k':>3} {'α_k_struct':>14} {'m_e·α_struct':>15} {'α_k_fit_MeV':>15} {'κ = fit/(m_e·struct)':>25}")
    print("-" * 90)
    h4_kappas = []
    for k in [0, 1, 2, 3]:
        s = alpha_struct_h4[k]
        m_s = m_e * s
        if k < len(alpha_fit_mev):
            f = mp.mpf(repr(alpha_fit_mev[k]))
            if abs(m_s) > mp.mpf('1e-12'):
                kappa = f / m_s
                kappa_str = f"{float(kappa):>+24.6f}"
                h4_kappas.append((k, kappa))
            else:
                kappa_str = "    (m_s ≈ 0, undef)"
            print(f"{k:>3} {float(s):>+14.8f} {float(m_s):>+15.10f} "
                  f"{float(f):>+15.8f} {kappa_str}")
    print()

    # Summary
    print("=" * 90)
    print("INTERPRETATION")
    print("=" * 90)

    if h3_kappas and h4_kappas:
        h3_vals = [float(k[1]) for k in h3_kappas]
        h4_vals = [float(k[1]) for k in h4_kappas]
        print(f"\nκ values across H_3, k=0..3:  {[f'{v:+.4f}' for v in h3_vals]}")
        print(f"κ values across H_4, k=0..3:  {[f'{v:+.4f}' for v in h4_vals]}")
        # Order-of-magnitude spread (proper consistency check)
        h3_abs = [abs(v) for v in h3_vals if abs(v) > 1e-10]
        if h3_abs:
            h3_spread = max(h3_abs) / min(h3_abs)
            print(f"\nH_3 |κ| spread max/min: {h3_spread:.2f}")
            if h3_spread < 1.2:
                print("✅ H_3 κ values consistent (≤20% spread) — single κ well-defined")
            elif h3_spread < 10:
                print("⚠ H_3 κ values mildly inconsistent (factor ≤10) — slight depth dependence")
            else:
                print(f"❌ H_3 κ values WILDLY inconsistent (factor {h3_spread:.0f}×)")
                print("   The bridge is NOT a single multiplicative constant.")
                print("   Structural α_λ and fitted α_k_MeV live in different")
                print("   parameterisations; the fitted α_k absorb the divergent")
                print("   q-deformed Plancherel weight w_λ_q = dim_q²/[n]_q!.")

    out = {
        "computation": "alpha-lambda-mev-bridge-probe",
        "description": (
            "Probe the units bridge α_k(MeV, fitted) = m_e · α_k(structural) · κ "
            "across H_3 and H_4 closed-form values. If κ is constant across k, "
            "the structural derivation reduces to a single physical-coupling "
            "calibration; if not, the bridge requires depth-dependent prefactors."
        ),
        "q_0": float(q),
        "m_e_MeV": float(m_e),
        "alpha_struct_h3": {str(k): float(v) for k, v in alpha_struct_h3.items()},
        "alpha_struct_h4_summed": {str(k): float(v) for k, v in alpha_struct_h4.items()},
        "alpha_fit_MeV": alpha_fit_mev,
        "h3_kappa_values": [(k, float(v)) for k, v in h3_kappas],
        "h4_kappa_values": [(k, float(v)) for k, v in h4_kappas],
        "precision": "f64_numeric_fallback",
        "truncation_eps": 0.0,
    }
    out_path = Path(__file__).parent / "alpha-lambda-mev-bridge-probe.witness.json"
    with open(out_path, "w") as fp:
        json.dump(out, fp, indent=2, default=str)
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
