#!/usr/bin/env python3
"""Reading A vs Reading B vs closure-target — h² λ_scale comparison.

The Yekutieli per-cell curvature audit
(`docs/audits/2026-05-22-yekutieli-percell-conjecture-formalized.md`)
identifies two readings of the audit's structural argument:

  Reading A:  λ = 5/2 − G · h²           (Yekutieli REPLACES Family A)
  Reading B:  λ = 5/2 + (3/4 − G) · h²   (Yekutieli ADDED to Family A)

The audit explicitly chose Reading B per "2026-05-23 user direction
add, not replace".  [PR #976](https://github.com/litlfred/qou/pull/976)
implemented Reading B and lands m_p at 950 MeV (1.26 % vs CODATA).

This script empirically shows:

  - Reading A matches CODATA to ~0.07 % at q_0 at h² truncation
    (since κ_required ≈ −G).
  - Reading B leaves the 1.26 % gap.
  - The choice is therefore a STRUCTURAL preference (canonical
    Wedderburn theorem must contribute) at the cost of NUMERICAL
    fit.

Output: research-grade comparison column.  NOT a production
replacement for `m_p_borromean_verification_50dps.py`.

See [`docs/audits/2026-05-23-yekutieli-bijection-natural-reading-
negative.md`](../../docs/audits/2026-05-23-yekutieli-bijection-
natural-reading-negative.md) §"Addendum 2: Reading A vs Reading B"
for full discussion.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV as _M_E_MEV,
    M_P_MEV_VALIDATION as _M_P_MEV_VALIDATION,
    M_N_MEV_VALIDATION as _M_N_MEV_VALIDATION,
)

set_compute_dps()

Q_PIN = HERE / "q-pinning-50-digit.witness.json"
Q = mp.mpf(json.load(Q_PIN.open())["derived_50_digit"]["q"])
Q_INV = mp.mpf(1) / Q
HBAR_Q = (Q - mp.mpf(1)) / Q
H = Q - Q_INV  # h = q - q⁻¹

VOL_B3 = 8 * mp.catalan
G = mp.catalan
M_E = _M_E_MEV
M_P_CODATA = _M_P_MEV_VALIDATION
M_N_CODATA = _M_N_MEV_VALIDATION
M_AVG_CODATA = (M_P_CODATA + M_N_CODATA) / 2


def main() -> int:
    # Three λ readings + closure-target
    lam_family_a = mp.mpf(5) / 2 + mp.mpf(3) * H ** 2 / 4
    lam_reading_a = mp.mpf(5) / 2 - G * H ** 2
    lam_reading_b = mp.mpf(5) / 2 + (mp.mpf(3) / 4 - G) * H ** 2
    # Closure-target: M_PE · ℏ_q² / (8G)
    M_PE = M_P_CODATA / M_E
    lam_closure = M_PE * HBAR_Q ** 2 / (8 * G)

    # m_p predictions (no flavor split, baryon-class m_avg layer)
    factor = VOL_B3 / HBAR_Q ** 2 * M_E

    def m_p_from(lam):
        return factor * lam

    m_p_family_a = m_p_from(lam_family_a)
    m_p_reading_a = m_p_from(lam_reading_a)
    m_p_reading_b = m_p_from(lam_reading_b)
    m_p_closure = m_p_from(lam_closure)  # = M_P_CODATA by construction

    print("=" * 92)
    print("λ_scale: Reading A vs Reading B vs Family A vs Closure")
    print("=" * 92)
    print()
    print(f"  q_0   = {mp.nstr(Q, 15)}")
    print(f"  h_0   = q - 1/q = {mp.nstr(H, 12)}")
    print(f"  h²    = {mp.nstr(H**2, 12)}")
    print(f"  G     = {mp.nstr(G, 12)} (Catalan)")
    print()
    print("  Reading      λ form                         λ at q_0       m_p pred    m_p err")
    print("  " + "-" * 92)
    for label, formula, lam, m_p in [
        ("Family A    ", "5/2 + (3/4) h²",         lam_family_a,  m_p_family_a),
        ("Reading A   ", "5/2 − G h² (replace)",   lam_reading_a, m_p_reading_a),
        ("Reading B   ", "5/2 + (3/4−G) h² (add)", lam_reading_b, m_p_reading_b),
        ("Closure     ", "M_PE · ℏ_q² / (8G)",     lam_closure,   m_p_closure),
    ]:
        err_pct = float((m_p - M_P_CODATA) / M_P_CODATA * 100)
        print(f"  {label}  {formula:<26}  "
              f"{mp.nstr(lam, 10):>12}  "
              f"{float(m_p):>10.4f}    {err_pct:>+8.4f} %")

    # Recompute cleanly
    rows = []
    for label, formula, lam in [
        ("family_a",  "5/2 + (3/4) h²",          lam_family_a),
        ("reading_a", "5/2 − G h² (replace)",    lam_reading_a),
        ("reading_b", "5/2 + (3/4−G) h² (add)",  lam_reading_b),
        ("closure",   "M_PE · ℏ_q² / (8G)",       lam_closure),
    ]:
        m_p = m_p_from(lam)
        err = (m_p - M_P_CODATA) / M_P_CODATA
        rows.append({
            "label": label,
            "lambda_formula": formula,
            "lambda_value": mp.nstr(lam, 20),
            "m_p_pred_MeV": mp.nstr(m_p, 15),
            "rel_err_pct": float(err * 100),
            "rel_err_ppm": float(err * 1e6),
        })

    print()
    print()
    print("  Findings:")
    print()
    r_a_err_ppm = abs(rows[1]["rel_err_ppm"])
    r_b_err_ppm = abs(rows[2]["rel_err_ppm"])
    fa_err_ppm = abs(rows[0]["rel_err_ppm"])
    print(f"    Family A     m_p err: {fa_err_ppm:>10.1f} ppm ({fa_err_ppm/10000:.3f} %)")
    print(f"    Reading A    m_p err: {r_a_err_ppm:>10.1f} ppm ({r_a_err_ppm/10000:.4f} %)")
    print(f"    Reading B    m_p err: {r_b_err_ppm:>10.1f} ppm ({r_b_err_ppm/10000:.4f} %)")
    print()
    print(f"    Reading A is {fa_err_ppm/r_a_err_ppm:>6.0f}x better than Family A")
    print(f"    Reading A is {r_b_err_ppm/r_a_err_ppm:>6.0f}x better than Reading B")

    # κ required for exact CODATA at fixed c_0 = 5/2 baseline
    kappa_required = (lam_closure - mp.mpf(5)/2) / H ** 2
    print()
    print(f"  κ such that 5/2 + κ·h² = closure-target at q_0:")
    print(f"    κ_required = {mp.nstr(kappa_required, 15)}")
    print(f"    −G          = {mp.nstr(-G, 15)}")
    print(f"    Difference  = {mp.nstr(kappa_required - (-G), 6)}")
    print(f"    Rel offset  = {mp.nstr((kappa_required - (-G)) / G * mp.mpf('100'), 6)} %")
    print()
    print("  So Reading A's κ = -G matches the required value to within ~0.07 %.")
    print("  Reading B's κ = 3/4 − G ≈ −0.166 is 5.5x off in magnitude.")

    # Witness emission
    w = WitnessBuilder(
        "lambda-reading-a-vs-b-comparison", engine="mpmath"
    )
    w.set_description(
        "Empirical h²-truncated comparison of Yekutieli Reading A "
        "(λ = 5/2 − G·h², 'replace') vs Reading B (λ = 5/2 + "
        "(3/4 − G)·h², 'add') vs Family A canonical (λ = 5/2 + "
        "(3/4)·h²) vs the closure-target (λ_p_codata = "
        "M_PE·ℏ_q²/(8G)).  Finding: Reading A matches CODATA to "
        "~0.07 % at q_0; Reading B leaves the 1.26 % gap; Family A "
        "leaves the 2.89 % gap.  Per docs/audits/2026-05-23-"
        "yekutieli-bijection-natural-reading-negative.md §Addendum 2: "
        "the audit's choice of Reading B over Reading A (per "
        "2026-05-23 user direction 'add not replace') is a structural "
        "preference (canonical Wedderburn theorem must contribute) "
        "at the cost of numerical fit (Reading A is ~16x better).  "
        "Research-grade comparison only — NOT a production replacement."
    )
    w.set_content_block("conj:lambda-scale-bring-bloch-identity")
    w.add_parameter("derivation_status",
                    "RESEARCH_COMPARISON_READING_A_VS_B")
    w.add_parameter("q_0", mp.nstr(Q, 20))
    w.add_parameter("h_0", mp.nstr(H, 20))
    w.add_parameter("h_squared", mp.nstr(H**2, 20))
    w.add_parameter("G_catalan", mp.nstr(G, 20))
    w.add_data("readings_comparison", rows)
    w.add_data("kappa_analysis", {
        "kappa_required_for_exact_match":  mp.nstr(kappa_required, 20),
        "minus_G":                          mp.nstr(-G, 20),
        "diff":                             mp.nstr(kappa_required - (-G), 12),
        "rel_offset_pct":                   mp.nstr(
            (kappa_required - (-G)) / G * mp.mpf('100'), 8
        ),
        "interpretation":
            "Reading A's κ = -G matches the closure target's required "
            "κ to ~0.07 % at h² truncation. The remaining 0.07 % is "
            "from h^4 and higher corrections to the closure-target "
            "that Reading A doesn't include.",
    })

    # Reading A is ~2400x better than Reading B at h² truncation
    # (Reading A is essentially the h²-truncation of the closure-target).
    w.add_assertion(
        "reading_a_dramatically_better_than_reading_b",
        computed=float(r_b_err_ppm / r_a_err_ppm),
        expected=2400.0,
        tolerance=1000.0,  # 1400x .. 3400x band
        unit="improvement factor",
        source="(|Reading B m_p err| / |Reading A m_p err|) at q_0",
    )
    w.add_assertion(
        "kappa_required_close_to_minus_G",
        computed=float(abs(kappa_required + G) / G * 100),
        expected=0.0,
        tolerance=0.1,  # 0.1 %
        unit="percent",
        source="Required κ in 5/2 + κ·h² for CODATA match vs −G",
    )

    w.add_caveat(
        "Reading A's numerical match to CODATA (~0.07 % at h² "
        "truncation) is STRIKING but should NOT be interpreted as "
        "evidence for production wiring.  Per the audit's structural "
        "argument:\n"
        "  - Family A's +3/4·h² is a PROVED theorem (Σ_λ⊢4 dim_q V_λ).\n"
        "  - Yekutieli's −G·h² claims to be an INDEPENDENT additive "
        "    contribution (non-abelian Stokes curvature integration).\n"
        "  - Reading B (sum) is therefore structurally mandatory if "
        "    both terms are real.\n"
        "Reading A's empirical-match advantage suggests EITHER:\n"
        "  (1) the audit's 'add not replace' user direction was wrong, OR\n"
        "  (2) there's a third categorical contribution `−3/4·h²` "
        "      that exactly cancels Family A at this layer, OR\n"
        "  (3) Reading A's near-match at h² is a coincidence that "
        "      breaks at higher orders.\n"
        "Without categorical justification for the per-cell curvature "
        "step (combinatorially unsupported per 2026-05-23 negative "
        "bijection audit), Reading A cannot be elevated to production."
    )

    out = w.save()
    print()
    print(f"Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
