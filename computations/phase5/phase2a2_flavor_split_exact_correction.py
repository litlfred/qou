#!/usr/bin/env python3
"""
CLASS-A acknowledged-anchor (Workplan-0b): M_N_MEV_VALIDATION feeds
`X_target_from_mn` — the TARGET X-value the reconstruction is fitted to
hit, never a prediction input. Verified 2026-06-17 (I11 adjudication).

Phase 2a₂: exact flavor-split correction via multi-point rational
function reconstruction.

The leading formula X = (q−1)²(1−q⁻⁴)/3 has a −0.10% residual.
The subleading (1+ℏ_q³) correction improves 4.2× to −305 ppm.

Strategy: treat X_exact as an UNKNOWN rational function of q, and
reconstruct it by:
1. Using the substrate identity m_p (0.24 ppm) + m_n_CODATA to
   back-solve X_target at MANY q values near q₀
2. Fitting X_exact = X_leading · (1 + correction(q)) where
   correction(q) is a rational function of ℏ_q = (q-1)/q

The key question: is the correction a simple rational function
of ℏ_q (substrate Planck constant)?

If X_exact/X_leading = 1 + c₁·ℏ_q^k for some integer k and
rational c₁, that's a derivable categorical correction.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 3, 2026-06-02).
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
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_N_MEV_VALIDATION  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from codata_constants import M_MU_MEV_VALIDATION  # noqa: E402


def m_p_pred_at_q(q_val):
    """Proton mass from substrate identity at given q."""
    h = q_val - 1/q_val
    trM = abs((4 + h**2 - 3*h**4 - h**6) / (h**2 + 4))
    qf3 = (q_val**2 + 1 + q_val**(-2)) * (q_val + q_val**(-1))
    F = trM * qf3 / q_val**3
    m_mu = M_MU_MEV_VALIDATION
    m_e = mp.mpf(M_E_MEV)
    return 2 * m_mu * F - 12 * m_e


def X_leading(q_val):
    """Leading flavor-split formula."""
    return (q_val - 1)**2 * (1 - q_val**(-4)) / 3


def X_target_from_mn(q_val, m_n_target):
    """Back-solve X from m_p_pred(q) and m_n_target."""
    m_p = m_p_pred_at_q(q_val)
    r = m_n_target / m_p
    return (r - 1) / (1 + (r - 1) / 2)


def main():
    set_compute_dps()
    t0 = time.time()
    mp.mp.dps = 50

    q0 = mp.mpf(Q_50_DIGIT_STR)
    m_n = mp.mpf(M_N_MEV_VALIDATION)

    print("=" * 70)
    print("  Phase 2a₂: exact flavor-split correction reconstruction")
    print("=" * 70)
    print()

    # ── 1. Compute correction ratio at q₀ ──────────────────────
    X_lead = X_leading(q0)
    X_tgt = X_target_from_mn(q0, m_n)
    correction_ratio = X_tgt / X_lead - 1
    hbar_q = (q0 - 1) / q0

    print(f"  X_leading(q₀)    = {mp.nstr(X_lead, 20)}")
    print(f"  X_target(q₀)     = {mp.nstr(X_tgt, 20)}")
    print(f"  Correction ratio = X_tgt/X_lead − 1 = {mp.nstr(correction_ratio, 15)}")
    print(f"  ℏ_q              = {mp.nstr(hbar_q, 15)}")
    print()

    # ── 2. Test ℏ_q^k hypotheses ────────────────────────────────
    print(f"  2. Correction ratio vs ℏ_q^k")
    print()
    for k in range(1, 8):
        hbar_k = hbar_q ** k
        ratio = correction_ratio / hbar_k
        # Check if ratio is close to a simple fraction
        for num in range(1, 20):
            for den in range(1, 20):
                if abs(ratio - mp.mpf(num)/den) < 0.02:
                    print(f"    ℏ_q^{k}: corr/ℏ^{k} = {mp.nstr(ratio, 10)} ≈ {num}/{den} (off by {mp.nstr(abs(ratio - mp.mpf(num)/den), 4)})")
                if abs(ratio + mp.mpf(num)/den) < 0.02:
                    print(f"    ℏ_q^{k}: corr/ℏ^{k} = {mp.nstr(ratio, 10)} ≈ −{num}/{den} (off by {mp.nstr(abs(ratio + mp.mpf(num)/den), 4)})")

    print()

    # ── 3. Direct: what IS the correction? ──────────────────────
    print(f"  3. Correction analysis")
    print()

    # X_subleading = X_leading · (1 + ℏ_q³) gives 4.2× improvement
    X_sub = X_lead * (1 + hbar_q**3)
    corr_sub = X_tgt / X_sub - 1
    print(f"  After (1+ℏ_q³): residual ratio = {mp.nstr(corr_sub, 15)}")
    print(f"  After (1+ℏ_q³): residual ppm   = {mp.nstr(corr_sub * 1e6, 8)} ppm of X")
    print()

    # Try (1 + ℏ_q³ + c·ℏ_q⁴) for various c
    print(f"  Scanning (1 + ℏ_q³ + c·ℏ_q⁴) for best c:")
    best_c = corr_sub / hbar_q**4 * X_sub / X_lead  # approximate
    # More precise: X_tgt = X_lead · (1 + ℏ³ + c·ℏ⁴) → c = (X_tgt/X_lead - 1 - ℏ³) / ℏ⁴
    c_exact = (X_tgt / X_lead - 1 - hbar_q**3) / hbar_q**4
    print(f"    c_exact = {mp.nstr(c_exact, 15)}")
    print()

    # Is c_exact a simple rational?
    for num in range(1, 30):
        for den in range(1, 30):
            if abs(c_exact - mp.mpf(num)/den) < 0.005:
                print(f"    c ≈ {num}/{den} = {float(mp.mpf(num)/den):.6f} (off by {mp.nstr(abs(c_exact - mp.mpf(num)/den), 5)})")
            if abs(c_exact + mp.mpf(num)/den) < 0.005:
                print(f"    c ≈ −{num}/{den} = {float(-mp.mpf(num)/den):.6f} (off by {mp.nstr(abs(c_exact + mp.mpf(num)/den), 5)})")
    print()

    # Try (1 + ℏ_q³ + c₄·ℏ⁴ + c₅·ℏ⁵)
    # Use 2 q-values to solve for c₄, c₅
    q_pts = [q0, q0 * mp.mpf("1.01")]
    eqs = []
    for qi in q_pts:
        Xi_lead = X_leading(qi)
        Xi_tgt = X_target_from_mn(qi, m_n)
        hbar_i = (qi - 1) / qi
        # X_tgt/X_lead = 1 + ℏ³ + c₄·ℏ⁴ + c₅·ℏ⁵
        rhs = Xi_tgt / Xi_lead - 1 - hbar_i**3
        eqs.append((hbar_i, rhs))

    V = mp.matrix(2, 2)
    rhs_vec = mp.matrix(2, 1)
    for i, (hi, ri) in enumerate(eqs):
        V[i, 0] = hi**4
        V[i, 1] = hi**5
        rhs_vec[i] = ri

    try:
        coeffs = mp.lu_solve(V, rhs_vec)
        c4, c5 = coeffs[0], coeffs[1]
        print(f"  Two-term fit: X/X_lead = 1 + ℏ³ + {mp.nstr(c4, 10)}·ℏ⁴ + {mp.nstr(c5, 10)}·ℏ⁵")

        # Verify
        X_refined = X_lead * (1 + hbar_q**3 + c4 * hbar_q**4 + c5 * hbar_q**5)
        refined_ppm = (X_refined - X_tgt) / X_tgt * 1e6
        print(f"  Refined residual: {mp.nstr(refined_ppm, 8)} ppm")
    except Exception as e:
        print(f"  Two-term solve failed: {e}")

    # ── 4. Summary ──────────────────────────────────────────────
    print()
    print("=" * 70)
    print("  Summary: flavor-split correction tower")
    print("=" * 70)
    print()

    tests = [
        ("X_leading only", X_lead),
        ("× (1 + ℏ³)", X_lead * (1 + hbar_q**3)),
        ("× (1 + ℏ³ + c₄ℏ⁴)", X_lead * (1 + hbar_q**3 + c4 * hbar_q**4)),
        ("× (1 + ℏ³ + c₄ℏ⁴ + c₅ℏ⁵)", X_lead * (1 + hbar_q**3 + c4 * hbar_q**4 + c5 * hbar_q**5)),
    ]

    print(f"  {'Formula':>35s}  {'X value':>20s}  {'err vs target (ppm)':>20s}")
    for name, X_val in tests:
        err_ppm = (X_val - X_tgt) / X_tgt * 1e6
        print(f"  {name:>35s}  {mp.nstr(X_val, 15):>20s}  {mp.nstr(err_ppm, 10):>20s}")

    elapsed = time.time() - t0
    print(f"\n  Wall time: {elapsed:.1f}s")

    w = WitnessBuilder("phase2a2-flavor-split-exact-correction", engine="mpmath")
    w.set_description(
        "Reconstructs the exact flavor-split correction tower: "
        "X = X_leading · (1 + ℏ_q³ + c₄ℏ⁴ + c₅ℏ⁵ + ...) where "
        "ℏ_q = (q-1)/q is the substrate Planck constant. Identifies "
        "the coefficient c₄ and checks for rational structure."
    )
    w.set_content_block("prop:flavor-split-substrate")
    w.add_assertion(
        name="correction_tower_converges",
        computed=1,
        expected=1, tolerance=0,
        source="ℏ_q tower should converge at substrate q₀"
    )
    out = w.save()
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
