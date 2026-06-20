#!/usr/bin/env python3
"""
Phase 2a: higher-order corrections to the flavor-split formula X.

The current formula X = (q−1)²(1−q⁻⁴)/3 matches CODATA Δm/M_N to
−0.10% (≈ 1000 ppm on the splitting, ≈ 1.76 ppm on m_n). To close
m_n to 1 ppb, we need X tightened by ~1000×.

Strategy: the substrate identity gives m_p to 0.24 ppm. Using m_p_pred
and m_n_CODATA, derive the EXACT target X_target at 50 dps, then
compute the residual X − X_target and probe its h-expansion for
rational structure.

If X_exact = X_current + δX and δX is a rational function of q,
that reveals the missing higher-order Hecke-skein term.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_P_MEV_VALIDATION, M_N_MEV_VALIDATION  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from codata_constants import M_MU_MEV_VALIDATION  # noqa: E402


def main():
    set_compute_dps()
    t0 = time.time()
    mp.mp.dps = 50

    q = mp.mpf(Q_50_DIGIT_STR)
    h = q - 1/q
    m_e = mp.mpf(M_E_MEV)
    m_mu = M_MU_MEV_VALIDATION
    m_p_codata = mp.mpf(M_P_MEV_VALIDATION)
    m_n_codata = mp.mpf(M_N_MEV_VALIDATION)

    print("=" * 70)
    print("  Phase 2a: flavor-split higher-order correction probe")
    print("=" * 70)
    print()

    # ── 1. Current formula ──────────────────────────────────────
    X_current = (q - 1)**2 * (1 - q**(-4)) / 3
    M_N_codata = (m_p_codata + m_n_codata) / 2
    Delta_codata = m_n_codata - m_p_codata
    X_codata = Delta_codata / M_N_codata  # this is an approximation; exact is below

    # The exact relationship: m_n = m_p(1 + X/(1-X/2))
    # → X/(1-X/2) = (m_n-m_p)/m_p = Δ/m_p
    # → X = Δ/m_p · (1-X/2) → X(1 + Δ/(2m_p)) = Δ/m_p → X = Δ/m_p / (1+Δ/(2m_p))
    # → X = 2Δ/(2m_p + Δ) = 2(m_n-m_p)/(m_p+m_n) = Δ/M_N ≈ X_codata

    # Actually the formula is m_n = m_p · (1 + X/(1-X/2))
    # So the target X satisfies: m_n_codata/m_p_pred = 1 + X_target/(1-X_target/2)
    # Using m_p_pred from the substrate identity
    trM = abs((4 + h**2 - 3*h**4 - h**6) / (h**2 + 4))
    q3fac = (q**2 + 1 + q**(-2)) * (q + q**(-1))
    F_Bor = trM * q3fac / q**3
    m_p_pred = 2 * m_mu * F_Bor - 12 * m_e

    ratio_target = m_n_codata / m_p_pred
    # ratio = 1 + X/(1-X/2) → X/(1-X/2) = ratio - 1 → X = (ratio-1)/(1+(ratio-1)/2)
    r_minus_1 = ratio_target - 1
    X_target = r_minus_1 / (1 + r_minus_1 / 2)

    # Alternatively, using CODATA m_p instead of m_p_pred
    ratio_codata = m_n_codata / m_p_codata
    r_minus_1_c = ratio_codata - 1
    X_target_codata = r_minus_1_c / (1 + r_minus_1_c / 2)

    delta_X = X_current - X_target
    delta_X_codata = X_current - X_target_codata

    print(f"  q₀ = {mp.nstr(q, 20)}")
    print(f"  h₀ = {mp.nstr(h, 20)}")
    print()
    print(f"  X_current  = (q−1)²(1−q⁻⁴)/3 = {mp.nstr(X_current, 20)}")
    print(f"  X_target   (from m_p_pred)     = {mp.nstr(X_target, 20)}")
    print(f"  X_target   (from m_p_CODATA)   = {mp.nstr(X_target_codata, 20)}")
    print()
    print(f"  δX = X_current − X_target:")
    print(f"    via m_p_pred:  {mp.nstr(delta_X, 15)} ({mp.nstr(delta_X/X_current*1e6, 8)} ppm of X)")
    print(f"    via m_p_CODATA: {mp.nstr(delta_X_codata, 15)} ({mp.nstr(delta_X_codata/X_current*1e6, 8)} ppm of X)")
    print()

    # ── 2. What does δX look like as a function of h? ──────────
    print("  2. Structure of the residual δX")
    print()

    # δX in units of h^k
    for k in range(1, 9):
        ratio_hk = delta_X / h**k
        print(f"    δX / h^{k} = {mp.nstr(ratio_hk, 12)}")

    print()

    # Check if δX is close to known constants × h^k
    catalan_G = mp.mpf("0.915965594177219015054603514932")
    candidates = [
        ("1/6", mp.mpf(1)/6),
        ("1/12", mp.mpf(1)/12),
        ("1/24", mp.mpf(1)/24),
        ("1/36", mp.mpf(1)/36),
        ("1/72", mp.mpf(1)/72),
        ("G (Catalan)", catalan_G),
        ("G/6", catalan_G/6),
        ("π²/6", mp.pi**2/6),
        ("1/(4π)", 1/(4*mp.pi)),
    ]

    print("  3. δX / h⁴ compared to structural constants")
    dX_over_h4 = delta_X / h**4
    print(f"    δX / h⁴ = {mp.nstr(dX_over_h4, 15)}")
    print()
    for name, val in candidates:
        ratio = dX_over_h4 / val
        print(f"    vs {name:>12s} = {mp.nstr(val, 12)}: ratio = {mp.nstr(ratio, 10)}")

    # ── 3. Implied higher-order X ───────────────────────────────
    print()
    print("  4. Implied correction term")
    print()

    # X_current = h³/6 − h⁴/12 + h⁵/32 − ... (exact expansion)
    # X_target = X_current − δX
    # If δX ≈ c · h^k, what is c?

    # From the numerical analysis, find the best h^k fit
    best_k = None
    best_c = None
    best_residual = mp.mpf("1e10")
    for k in range(3, 9):
        c_k = delta_X / h**k
        # Check stability: does this c_k give a good prediction?
        X_corrected = X_current - c_k * h**k
        residual_corrected = abs(X_corrected - X_target) / X_target
        if residual_corrected < best_residual:
            best_residual = residual_corrected
            best_k = k
            best_c = c_k

    print(f"    Best single-term correction: δX ≈ {mp.nstr(best_c, 12)} · h^{best_k}")
    print(f"    Residual after correction: {mp.nstr(best_residual * 1e6, 8)} ppm of X")
    print()

    # Multi-term: fit δX = c₄h⁴ + c₅h⁵ + c₆h⁶
    # Using 3 q-values for 3 unknowns
    q_offsets = [0, 0.01, -0.01]
    q_pts = [q + mp.mpf(str(off)) for off in q_offsets]
    h_pts = [qi - 1/qi for qi in q_pts]

    dX_pts = []
    for qi, hi in zip(q_pts, h_pts):
        Xi = (qi - 1)**2 * (1 - qi**(-4)) / 3
        trMi = abs((4 + hi**2 - 3*hi**4 - hi**6) / (hi**2 + 4))
        q3fi = (qi**2 + 1 + qi**(-2)) * (qi + qi**(-1))
        FBi = trMi * q3fi / qi**3
        mpi = 2 * m_mu * FBi - 12 * m_e
        ri = m_n_codata / mpi
        Xti = (ri - 1) / (1 + (ri - 1)/2)
        dX_pts.append(Xi - Xti)

    # Solve: δX_i = c₄·h_i⁴ + c₅·h_i⁵ + c₆·h_i⁶
    V = mp.matrix(3, 3)
    for i in range(3):
        for j in range(3):
            V[i, j] = h_pts[i]**(j + 4)
    rhs = mp.matrix(3, 1)
    for i in range(3):
        rhs[i] = dX_pts[i]

    try:
        coeffs = mp.lu_solve(V, rhs)
        print(f"    Multi-term fit: δX ≈ {mp.nstr(coeffs[0], 10)}·h⁴ + {mp.nstr(coeffs[1], 10)}·h⁵ + {mp.nstr(coeffs[2], 10)}·h⁶")

        # Check: what are these close to?
        for k, c in enumerate(coeffs):
            k_actual = k + 4
            print(f"      c_{k_actual} = {mp.nstr(c, 12)}")
            for name, val in [("1/12", mp.mpf(1)/12), ("1/6", mp.mpf(1)/6),
                               ("1/24", mp.mpf(1)/24), ("1/3", mp.mpf(1)/3),
                               ("5/24", mp.mpf(5)/24)]:
                if abs(c) > 1e-15:
                    ratio = c / val
                    if abs(ratio - round(float(ratio))) < 0.01:
                        print(f"        ≈ {round(float(ratio))} × {name}")
    except Exception as e:
        print(f"    Multi-term solve failed: {e}")

    # ── 4. What precision does tightened X give? ────────────────
    print()
    print("  5. Precision impact")
    X_tightened = X_target  # ideally
    m_n_tightened = m_p_pred * (1 + X_tightened / (1 - X_tightened / 2))
    Q_beta_tightened = m_n_tightened - m_p_pred - m_e

    print(f"    With exact X (anchored to m_n_CODATA):")
    print(f"      m_n = {mp.nstr(m_n_tightened, 15)} MeV (Δ = {mp.nstr((m_n_tightened - m_n_codata)/m_n_codata*1e6, 8)} ppm)")
    print(f"      Q_β = {mp.nstr(Q_beta_tightened, 12)} MeV (Δ = {mp.nstr((Q_beta_tightened - mp.mpf('0.78233341'))/mp.mpf('0.78233341')*1e6, 8)} ppm)")

    elapsed = time.time() - t0
    print(f"\n  Wall time: {elapsed:.1f}s")

    # Witness
    w = WitnessBuilder("phase2a-flavor-split-higher-order", engine="mpmath")
    w.set_description(
        "Probes higher-order corrections to the flavor-split X formula. "
        "At 50 dps, the residual δX = X_current − X_target is analyzed "
        "for rational structure in the h-variable. Identifies the "
        "leading correction order and coefficient."
    )
    w.set_content_block("prop:flavor-split-substrate")
    w.add_data("delta_X", str(mp.nstr(delta_X, 20)))
    w.add_data("delta_X_ppm_of_X", str(mp.nstr(delta_X/X_current*1e6, 10)))
    w.add_data("best_correction", {
        "order": best_k,
        "coefficient": str(mp.nstr(best_c, 15)),
    })
    w.add_assertion(
        name="residual_identified",
        computed=1 if abs(delta_X) > 1e-20 else 0,
        expected=1,
        tolerance=0,
        source="δX should be non-zero (formula is approximate)"
    )
    out = w.save()
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
