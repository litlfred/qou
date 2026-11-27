#!/usr/bin/env python3
"""R&D 1: Geometric (Yekutieli-Stokes) family — does adding a
Vol(B_3)-derived h² correction to Family A give the empirical
λ_p = 5/2 − h²·G match?

ANSATZ:
  λ_geom(q) = π_alg(q) − Σ_geom(q)

where:
  π_alg(q) = (1/4) Σ_λ dim_q V_λ = 5/2 + (3/4)·h² (Family A)
  Σ_geom(q) = geometric contribution from the Borromean surface
              ↪ h²-leading, with prefactor involving G = Vol(B_3)/8

For the empirical h² match (-G total):
  Σ_geom should have h² coefficient = (3/4) − (−G) = 3/4 + G

We need (3/4 + G) ≈ 1.666 ≈ 5/3 (the canonical Markov-trace value
at q=1). Interesting coincidence — investigate.

TEST: compute Σ_geom = (5/3)·h² + O(h⁴) (the candidate) and check if
  λ_geom(q) = π_alg(q) − (5/3)·h²
matches λ_p_target to better than 5.6 ppm.
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json, sys
from pathlib import Path
import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from witness_base import WitnessBuilder
from q_parameter import Q_50_DIGIT_STR, Q_MP
from experimental_constants import M_E_MEV, M_P_MEV

mp.mp.dps = 80
Q = Q_MP
H = Q - 1/Q
HBAR = (Q - 1) / Q
G = mp.catalan
VOL_B3 = 8 * mp.catalan  # = Vol(Borromean rings complement), 8·G via Adams 1985
M_E = mp.mpf(M_E_MEV)
M_P = mp.mpf(M_P_MEV)
LAM_P_TARGET = (M_P / M_E) * HBAR**2 / VOL_B3


def main() -> int:
    w = WitnessBuilder("lambda-scale-rd1-geometric", engine="mpmath+sympy")
    w.set_description(
        "R&D 1: Yekutieli-Stokes geometric family — λ_geom = π_alg − Σ_geom. "
        "Tests if Family A's +3h²/4 minus a geometric Σ_geom = (5/3)·h² + ... "
        "matches the empirical λ_p with negative h² coefficient."
    )
    w.set_content_block("conj:lambda-scale-substrate-form")
    w.add_parameter("dps", 80)

    # π_alg at q_0
    pi_alg = (3*Q**2 + 4 + 3*Q**(-2)) / 4
    # Various Σ_geom ansätze for the h² coefficient
    print(f"λ_p_target (CODATA m_p/m_e · ℏ²/Vol) = {mp.nstr(LAM_P_TARGET, 25)}")
    print(f"π_alg(q_0) (Family A) = {mp.nstr(pi_alg, 25)}")
    print(f"Diff: {mp.nstr(pi_alg - LAM_P_TARGET, 12)}")
    print()

    print("h² coefficient required to flip Family A → target:")
    delta_h2 = (pi_alg - LAM_P_TARGET) / H**2
    print(f"  (π_alg - target) / h² = {mp.nstr(delta_h2, 15)}")
    print(f"  Compare: G = {mp.nstr(G, 12)}")
    print(f"  Compare: 5/3 = {mp.nstr(mp.mpf(5)/3, 12)}")
    print(f"  Compare: 3/4 + G = {mp.nstr(mp.mpf(3)/4 + G, 12)}")
    print()

    # Test specific Σ_geom ansätze
    candidates = {
        "(5/3) h²": mp.mpf(5)/3 * H**2,
        "(3/4 + G) h²": (mp.mpf(3)/4 + G) * H**2,
        "Vol(B_3)/8 · h² + (3/4) h²": (VOL_B3/8 + mp.mpf(3)/4) * H**2,
        "(3/4 + G) h² + O(h^4)_correction": (mp.mpf(3)/4 + G) * H**2,
    }
    print("Testing Σ_geom ansätze:")
    for name, sigma in candidates.items():
        pred = pi_alg - sigma
        diff_ppm = float((pred - LAM_P_TARGET) / LAM_P_TARGET * mp.mpf("1e6"))
        print(f"  Σ_geom = {name:35s} → λ_pred = {float(pred):.10f}  ({diff_ppm:+.3f} ppm)")
    print()

    # Try the FULL implicit Σ_geom: solve for it
    sigma_implied = pi_alg - LAM_P_TARGET
    sigma_h2_coeff = sigma_implied / H**2
    print(f"Implied Σ_geom = π_alg - target = {mp.nstr(sigma_implied, 15)}")
    print(f"Implied Σ_geom/h² coefficient: {mp.nstr(sigma_h2_coeff, 15)}")
    print(f"  = 3/4 + G + small correction:")
    print(f"  delta from (3/4 + G) = {mp.nstr(sigma_h2_coeff - (mp.mpf(3)/4 + G), 12)}")
    print(f"  This delta · h^{-2} = {mp.nstr((sigma_h2_coeff - (mp.mpf(3)/4 + G))/H**2, 12)}")
    print()

    # PSLQ for the implied Σ_geom h² coefficient
    basis = {
        "1": mp.mpf(1),
        "G": G,
        "3/4": mp.mpf(3)/4,
        "Vol(B_3)/8": VOL_B3 / 8,
        "5/3": mp.mpf(5)/3,
        "G^2": G**2,
        "h^2": H**2,
        "1/G": 1/G,
        "ln(2)": mp.log(2),
    }
    keys = list(basis.keys())
    vec = [sigma_h2_coeff] + [basis[k] for k in keys]
    try:
        rel = mp.pslq(vec, tol=mp.mpf("1e-50"), maxcoeff=10**6)
        if rel:
            terms = [(rel[i+1], keys[i]) for i in range(len(keys)) if rel[i+1] != 0]
            print(f"PSLQ for Σ_geom h² coeff: c_x · {int(rel[0])} + {len(terms)} terms")
            for c, t in terms[:6]:
                print(f"  {int(c)} · {t}")
        else:
            print("PSLQ: no integer relation found")
    except Exception as e:
        print(f"PSLQ error: {e}")

    w.add_data("pi_alg_at_q0", float(pi_alg))
    w.add_data("lambda_p_target", float(LAM_P_TARGET))
    w.add_data("Sigma_geom_implied_h2_coeff", mp.nstr(sigma_h2_coeff, 25))
    w.add_data("Sigma_geom_minus_3_4_minus_G", mp.nstr(sigma_h2_coeff - mp.mpf(3)/4 - G, 25))
    w.add_caveat("R&D probe — Σ_geom structural origin is still open.")

    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
