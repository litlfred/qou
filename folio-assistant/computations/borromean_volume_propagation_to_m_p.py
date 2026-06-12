#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical propagation test.
"""Test whether the stale Vol(𝓑₃) explains the 250 ppb m_p residual.

Finding from `borromean_volume_100dps.py`:
  Vol(𝓑₃) = 8·G exactly (Lobachevsky / Catalan identity)
          = 7.327724753417752... at 100 dps
  Audit / production script Vol = 7.327722906465      (stale, ~10 dps)
  Δ = 1.85e-6 absolute = 0.252 ppm relative

The m_p_borromean_verification_50dps.py production script uses the
stale Vol(𝓑₃) value AND a hardcoded λ_p_scale = 2.4599527869 — and
together they close m_p to 250 ppb. The HYPOTHESIS this script tests:

  If the hardcoded λ_p_scale was originally calibrated against
  CODATA m_p using the CORRECT (8·G) Vol(𝓑₃), then plugging that
  same λ_p_scale BACK into the production formula WITH the stale
  Vol(𝓑₃) introduces exactly the 250 ppb mismatch.

If true → swapping in the correct Vol(𝓑₃) closes m_p entirely.

Ref: docs/audits/2026-05-18-lambda-scale-derivation-search.md §93–104
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402


def main() -> int:
    mp.mp.dps = 80

    w = WitnessBuilder(
        "borromean-volume-propagation-to-m-p",
        engine="mpmath",
    )
    w.set_description(
        "Tests whether replacing the stale Vol(𝓑₃) = 7.32772290 "
        "(SnapPy default-precision literature value, used in "
        "m_p_borromean_verification_50dps.py:68) with the exact "
        "8·G = 7.32772475 closes the 250 ppb m_p residual. "
        "Hypothesis: the hardcoded λ_p_scale = 2.4599527869 was "
        "calibrated against CODATA m_p using the CORRECT 8·G value, "
        "so the stale Vol in the production formula introduces a "
        "compensating ~0.25 ppm error."
    )
    w.add_parameter("compute_dps", "80")

    # ── Constants (CODATA + substrate) ──────────────────────
    # q_0 from q_parameter.Q_50_DIGIT_STR
    from q_parameter import Q_50_DIGIT_STR  # noqa: E402
    # CODATA values from the calibration registry, not free
    # literals (P31 audit discipline). m_e is CAL-1; m_p is the
    # validation-only reference (not a calibration anchor).
    from codata_constants import (  # noqa: E402
        M_E_MEV, M_P_MEV_VALIDATION,
    )
    Q = mp.mpf(Q_50_DIGIT_STR)
    HBAR_Q = (Q - 1) / Q
    HBAR_Q_SQ = HBAR_Q ** 2
    M_E_CODATA = M_E_MEV
    M_P_CODATA = M_P_MEV_VALIDATION

    # ── The two Vol(𝓑₃) candidates ─────────────────────────
    VOL_STALE = mp.mpf("7.327722906465")
    VOL_8G_EXACT = 8 * mp.catalan
    LAMBDA_HARDCODED = mp.mpf("2.4599527869")

    w.add_data("substrate", {
        "Q_50dps": mp.nstr(Q, 50),
        "ℏ_q": mp.nstr(HBAR_Q, 30),
        "ℏ_q²": mp.nstr(HBAR_Q_SQ, 30),
        "m_e_codata_MeV": mp.nstr(M_E_MEV, 20),
        "m_p_codata_MeV": mp.nstr(M_P_MEV_VALIDATION, 20),
        "source": "codata_constants.M_E_MEV (CAL-1) + M_P_MEV_VALIDATION (reference)",
    })

    w.add_data("vol_B3_candidates", {
        "stale_literature_used_by_borromean_verif_script": mp.nstr(VOL_STALE, 30),
        "8G_exact_via_catalan_at_100dps": mp.nstr(VOL_8G_EXACT, 30),
        "delta": mp.nstr(VOL_8G_EXACT - VOL_STALE, 20),
        "rel_diff_ppm": mp.nstr(
            (VOL_8G_EXACT - VOL_STALE) / VOL_8G_EXACT * mp.mpf("1e6"), 8,
        ),
    })

    # ── m_p prediction under both Vol(𝓑₃) values (same λ) ───
    def m_p_pred(vol_b3: mp.mpf, lam: mp.mpf) -> mp.mpf:
        return M_E_CODATA * vol_b3 / HBAR_Q_SQ * lam

    m_p_stale = m_p_pred(VOL_STALE, LAMBDA_HARDCODED)
    m_p_8G = m_p_pred(VOL_8G_EXACT, LAMBDA_HARDCODED)
    delta_stale = m_p_stale - M_P_CODATA
    delta_8G = m_p_8G - M_P_CODATA

    w.add_data("m_p_prediction_with_hardcoded_lambda", {
        "hardcoded_λ_p_scale": "2.4599527869",
        "via_stale_Vol(𝓑₃)": {
            "m_p_pred_MeV": mp.nstr(m_p_stale, 12),
            "delta_vs_CODATA_MeV": mp.nstr(delta_stale, 10),
            "delta_ppm": mp.nstr(delta_stale / M_P_CODATA * mp.mpf("1e6"), 6),
        },
        "via_exact_8G_Vol(𝓑₃)": {
            "m_p_pred_MeV": mp.nstr(m_p_8G, 12),
            "delta_vs_CODATA_MeV": mp.nstr(delta_8G, 10),
            "delta_ppm": mp.nstr(delta_8G / M_P_CODATA * mp.mpf("1e6"), 6),
        },
        "improvement": mp.nstr(
            mp.fabs(delta_stale) / max(mp.fabs(delta_8G), mp.mpf("1e-30")), 6,
        ),
    })

    # ── The implied λ_p_scale targets (solving the formula
    #    against CODATA m_p under each Vol(𝓑₃)) ─────────────
    lambda_implied_stale = M_P_CODATA / (M_E_CODATA * VOL_STALE / HBAR_Q_SQ)
    lambda_implied_8G = M_P_CODATA / (M_E_CODATA * VOL_8G_EXACT / HBAR_Q_SQ)

    w.add_data("lambda_p_implied_from_CODATA", {
        "definition": "λ implied = m_p_CODATA / (m_e · Vol/ℏ_q²)",
        "via_stale_Vol(𝓑₃)": mp.nstr(lambda_implied_stale, 20),
        "via_exact_8G_Vol(𝓑₃)": mp.nstr(lambda_implied_8G, 20),
        "hardcoded_lambda_in_script": "2.4599527869",
        "diff_implied_stale_vs_hardcoded": mp.nstr(
            lambda_implied_stale - LAMBDA_HARDCODED, 12,
        ),
        "diff_implied_8G_vs_hardcoded": mp.nstr(
            lambda_implied_8G - LAMBDA_HARDCODED, 12,
        ),
        "interpretation": (
            "If the hardcoded value matches the implied-via-8G λ to "
            "high precision, the hardcoded λ was originally fitted "
            "using the CORRECT Vol(𝓑₃) = 8·G, not the stale literature "
            "value. In that case the residual 250 ppb in production "
            "comes purely from the stale Vol(𝓑₃) in the formula."
        ),
    })

    # ── Headline assertion: does fixing Vol close m_p? ──────
    # With Vol(𝓑₃) = 8·G exact and the 11-digit hardcoded
    # λ_p_scale literal, the residual lands at ~1.03 ppb. The
    # remaining error is entirely literal truncation (11-digit
    # λ_p vs the 50-dps inverted target); see the
    # `lambda_p_implied_from_CODATA` block in the data above.
    delta_8G_ppm = mp.fabs(delta_8G / M_P_CODATA * mp.mpf("1e6"))
    w.add_assertion(
        "m_p residual via exact 8·G Vol(𝓑₃) drops below 2 ppb",
        computed=float(delta_8G_ppm * mp.mpf("1e3")),  # in ppb
        expected=0.0,
        tolerance=2.0,
        unit="ppb",
        source=(
            "Replace stale Vol with 8·G; hardcoded 11-digit λ "
            "unchanged. Residual = literal truncation of λ_p; "
            "drops to ~10^-50 ppb with full-precision λ."
        ),
    )

    # ── Print summary ─────────────────────────────────────────
    print(f"  λ_hardcoded         = {mp.nstr(LAMBDA_HARDCODED, 12)}")
    print(f"  λ_implied (stale)   = {mp.nstr(lambda_implied_stale, 12)}")
    print(f"  λ_implied (8·G)     = {mp.nstr(lambda_implied_8G, 12)}")
    print()
    print(f"  m_p_pred (stale)    = {mp.nstr(m_p_stale, 12)}  Δ={mp.nstr(delta_stale, 4)}  ({mp.nstr(delta_stale / M_P_CODATA * mp.mpf('1e6'), 4)} ppm)")
    print(f"  m_p_pred (8·G)      = {mp.nstr(m_p_8G, 12)}  Δ={mp.nstr(delta_8G, 4)}  ({mp.nstr(delta_8G / M_P_CODATA * mp.mpf('1e6'), 4)} ppm)")
    print(f"  m_p_codata          = {mp.nstr(M_P_CODATA, 12)}")

    w.add_data("lean_uniqueness_ref", lean_uniqueness_ref("proton"))
    out = w.set_audit_only(
        "docs/audits/2026-05-18-lambda-scale-derivation-search.md"
    ).save()
    print(f"\n→ wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
