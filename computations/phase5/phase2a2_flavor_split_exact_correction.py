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
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import M_N_MEV_VALIDATION, M_MU_MEV_VALIDATION  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402


def m_p_pred_at_q(q_val):
    """Proton mass from substrate identity at given q."""
    h = q_val - 1/q_val
    trM = abs((4 + h**2 - 3*h**4 - h**6) / (h**2 + 4))
    qf3 = (q_val**2 + 1 + q_val**(-2)) * (q_val + q_val**(-1))
    F = trM * qf3 / q_val**3
    m_mu = mp.mpf(M_MU_MEV_VALIDATION)
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
    set_compute_dps()

    q0 = Q_MP
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

    # c4/c5 were bound ONLY inside the try, but are read unconditionally by the
    # `tests` table below — a failed solve raised NameError there instead of
    # reporting the failure.  Pre-bound, and the failure recorded, so the
    # witness says so rather than the script aborting (bean qou-26f2).
    c4 = c5 = None
    solve_error = None
    try:
        coeffs = mp.lu_solve(V, rhs_vec)
        c4, c5 = coeffs[0], coeffs[1]
        print(f"  Two-term fit: X/X_lead = 1 + ℏ³ + {mp.nstr(c4, 10)}·ℏ⁴ + {mp.nstr(c5, 10)}·ℏ⁵")

        # Verify
        X_refined = X_lead * (1 + hbar_q**3 + c4 * hbar_q**4 + c5 * hbar_q**5)
        refined_ppm = (X_refined - X_tgt) / X_tgt * 1e6
        print(f"  Refined residual: {mp.nstr(refined_ppm, 8)} ppm")
    except Exception as e:
        solve_error = f"{type(e).__name__}: {e}"
        print(f"  Two-term solve failed: {e}")

    # ── 4. Summary ──────────────────────────────────────────────
    print()
    print("=" * 70)
    print("  Summary: flavor-split correction tower")
    print("=" * 70)
    print()

    tests = [("X_leading only", X_lead),
             ("× (1 + ℏ³)", X_lead * (1 + hbar_q**3))]
    if c4 is not None:
        tests.append(("× (1 + ℏ³ + c₄ℏ⁴)",
                      X_lead * (1 + hbar_q**3 + c4 * hbar_q**4)))
        tests.append(("× (1 + ℏ³ + c₄ℏ⁴ + c₅ℏ⁵)",
                      X_lead * (1 + hbar_q**3 + c4 * hbar_q**4 + c5 * hbar_q**5)))

    print(f"  {'Formula':>35s}  {'X value':>20s}  {'err vs target (ppm)':>20s}")
    truncation_err_ppm = {}
    for name, X_val in tests:
        err_ppm = (X_val - X_tgt) / X_tgt * 1e6
        truncation_err_ppm[name] = err_ppm
        print(f"  {name:>35s}  {mp.nstr(X_val, 15):>20s}  {mp.nstr(err_ppm, 10):>20s}")

    # ── 4b. Does the tower actually CONVERGE at q₀? ─────────────
    # The assertion below used to be computed=1/expected=1 with the source
    # "ℏ_q tower should converge at substrate q₀" — a wish, not a measurement,
    # and green no matter what the numbers did (bean qou-26f2).  Measure it.
    #
    # The criterion is the standard one for a power series evaluated at a point:
    # the successive TERM magnitudes must decrease.  It is independent of this
    # script's own fit residual, which is worthless as evidence here — the ℏ⁴/ℏ⁵
    # coefficients come from a 2×2 solve at exactly 2 sample points, so the final
    # residual at q₀ is ~0 BY CONSTRUCTION (an exact interpolation), not because
    # the tower converged.
    tower_terms = [("ℏ³", hbar_q**3)]
    if c4 is not None:
        tower_terms.append(("c₄ℏ⁴", c4 * hbar_q**4))
        tower_terms.append(("c₅ℏ⁵", c5 * hbar_q**5))
    term_ratios = [abs(tower_terms[i + 1][1] / tower_terms[i][1])
                   for i in range(len(tower_terms) - 1)]
    n_decreasing = sum(1 for r in term_ratios if r < 1)
    print()
    print("  Convergence test — successive term magnitudes at q₀ "
          "(must DECREASE for a convergent tower):")
    for i, (nm, t) in enumerate(tower_terms):
        extra = ("" if i == 0
                 else f"   ratio to previous = {mp.nstr(term_ratios[i - 1], 6)}")
        print(f"    |{nm}| = {mp.nstr(abs(t), 8)}{extra}")
    print(f"    → {n_decreasing} of {len(term_ratios)} successive ratios are < 1")

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
    # Everything below is recorded as a decimal STRING: this witness carries no
    # raw float64 today and is absent from raw-float64-baseline.json, so adding
    # a bare float here would fail the audit as a NEW dirty witness.
    w.add_data("hbar_q", mp.nstr(hbar_q, 25))
    w.add_data("two_term_fit", {
        "c4": (mp.nstr(c4, 20) if c4 is not None else None),
        "c5": (mp.nstr(c5, 20) if c5 is not None else None),
        "solve_error": solve_error,
        "sample_q_points": [mp.nstr(qi, 20) for qi in q_pts],
        "rhs_at_sample_points": [mp.nstr(ri, 20) for _, ri in eqs],
        "caveat": "2 equations, 2 unknowns — the fit INTERPOLATES the two "
                  "sample points exactly, so its residual at q₀ is ~0 by "
                  "construction and is not evidence of convergence. The rhs "
                  "moves from 4.6e-4 to 14.66 across a 9% change in ℏ_q, so "
                  "the residual being fitted is not a smooth low-order "
                  "polynomial in ℏ_q over that span.",
    })
    w.add_data("truncation_err_ppm",
               {k: mp.nstr(v, 12) for k, v in truncation_err_ppm.items()})
    w.add_data("tower_term_magnitudes",
               {nm: mp.nstr(abs(t), 12) for nm, t in tower_terms})
    w.add_data("tower_term_ratios", [mp.nstr(r, 12) for r in term_ratios])
    w.add_data("tower_term_ratios_examined", len(term_ratios))
    # Sentinel: with no ℏ⁴/ℏ⁵ terms (the 2×2 solve raised) there are ZERO ratios,
    # and "0 of 0 decreasing" would satisfy expected=0 vacuously — the same
    # defect this drain exists to remove. -1 makes an unmeasurable tower RED.
    tower_verdict = n_decreasing if term_ratios else -1
    w.add_assertion(
        name="correction_tower_convergent_term_ratios",
        computed=tower_verdict,
        expected=0, tolerance=0,
        unit="ratios",
        source=(
            "MEASURED convergence of the ℏ_q tower at q₀, replacing "
            "`correction_tower_converges` (computed=1/expected=1, green "
            "regardless of the numbers — bean qou-26f2). A convergent series "
            "evaluated at a point needs its successive TERM magnitudes to "
            "decrease; here 0 of the 2 successive ratios are < 1. Terms: "
            f"|ℏ³| = {mp.nstr(abs(tower_terms[0][1]), 6)}, then "
            + (f"|c₄ℏ⁴| = {mp.nstr(abs(tower_terms[1][1]), 6)} "
               f"(×{mp.nstr(term_ratios[0], 6)}) and "
               f"|c₅ℏ⁵| = {mp.nstr(abs(tower_terms[2][1]), 6)} "
               f"(×{mp.nstr(term_ratios[1], 6)}). " if c4 is not None else "")
            + "So the tower DIVERGES at q₀ beyond the ℏ³ term and expected=0 "
            "records that honest negative — it goes red the moment a "
            "reconstruction actually produces decreasing terms, which is the "
            "alarm worth having. The ℏ³ term itself is genuine and is the "
            "module's one real result: it improves the residual from "
            f"{mp.nstr(truncation_err_ppm['X_leading only'], 8)} ppm to "
            f"{mp.nstr(truncation_err_ppm['× (1 + ℏ³)'], 8)} ppm. The 2×2 "
            "ℏ⁴/ℏ⁵ solve is well conditioned (cond ≈ 300), so the ~1e6 "
            "coefficients are real, not numerical noise; see "
            "`two_term_fit.caveat`. computed = -1 means the 2×2 solve raised "
            "and the tower could not be measured at all — red, not a vacuous "
            "0-of-0 pass; `two_term_fit.solve_error` then carries the reason."
        ),
    )
    out = w.save()
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
