#!/usr/bin/env python3
"""EXPLORATORY (canonical infrastructure, unproved −G·h² numerical claim).

Borromean baryon mass prediction under Yekutieli-extended λ_scale.

Companion to `m_p_borromean_verification_50dps.py` (production:
PROVED canonical Family A `λ_A = 5/2 + (3/4) h²`).  Here we wire
the **categorically-conditional** Yekutieli-extended form

    λ_Yekutieli(q) := λ_A(q) + (−G · h²)
                   =  5/2 + (3/4 − G) · h²
                   ≈  2.49266 at q_0

per `docs/agent-briefs/2026-05-22-lambda-scale-qdilog-tower-direct.md`
§Strategy I and `docs/audits/2026-05-22-yekutieli-percell-conjecture-
formalized.md`.

The Yekutieli `−G·h²` term is structurally distinct from the
canonical Wedderburn `+3/4·h²` (different categorical mechanism:
non-abelian Stokes curvature integration over 𝓑_3's 8-fold ideal
octahedral tessellation, vs Wedderburn-block dim_q V_λ sum) and is
the framework's substrate-pure additive correction.  No fit; both
contributions derive from independent substrate-natural principles.

## Gating

The Yekutieli term is **load-bearing-conjectural**: the explicit
cell-↔-half-sym-projection bijection at H_4 is open.  This script
is therefore opt-in / probe-grade, NOT a production replacement
for `m_p_borromean_verification_50dps.py`.  Per AGENTS.md §3b-cond
(conditional-class exception), the Lean wiring of the Yekutieli
extension would carry the bijection as a class instance.

## Composed prediction (with PR #942's substrate flavor split)

    m_avg^pred  =  m_e · Vol(𝓑_3)/ℏ_q² · λ_Yekutieli ≈ 951 MeV
    m_p^pred    =  m_avg · (1 − Δm/M_N / 2)            ≈ 950.3 MeV
    m_n^pred    =  m_avg · (1 + Δm/M_N / 2)            ≈ 951.7 MeV

vs CODATA m_p = 938.27, m_n = 939.57 → ~1.3% gap (vs Family A's
~2.9%; halved by the Yekutieli term).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from _li_2_q_util import (  # noqa: E402
    lambda_scale_family_a,
    lambda_scale_yekutieli_extended,
    flavor_split_subleading,
)
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV as _M_E_MEV,
    M_P_MEV_VALIDATION as _M_P_MEV_VALIDATION,
    M_N_MEV_VALIDATION as _M_N_MEV_VALIDATION,
)

set_compute_dps()

# Substrate q_0 at 50 dps
Q_PIN = HERE / "q-pinning-50-digit.witness.json"
Q = mp.mpf(json.load(Q_PIN.open())["derived_50_digit"]["q"])
Q_INV = mp.mpf(1) / Q
HBAR_Q = (Q - mp.mpf(1)) / Q

# Borromean rings volume (exact Vol(𝓑_3) = 8 · G).
VOL_B3 = 8 * mp.catalan

M_E = _M_E_MEV
M_P_CODATA = _M_P_MEV_VALIDATION
M_N_CODATA = _M_N_MEV_VALIDATION
M_AVG_CODATA = (M_P_CODATA + M_N_CODATA) / 2


def main() -> int:
    w = WitnessBuilder(
        "lambda-yekutieli-extended-borromean", engine="mpmath"
    )
    w.set_description(
        "Borromean baryon mass prediction under the Yekutieli-extended "
        "λ_scale = 5/2 + (3/4 − G)·h².  EMPIRICAL MATCH AWAITING "
        "CATEGORICAL BACKING (reclassified 2026-05-23 per audit "
        "`docs/audits/2026-05-23-yekutieli-bijection-natural-reading-"
        "negative.md`): the load-bearing cell-↔-half-sym-projection "
        "bijection at H_4 is NOT supported by natural-reading partition "
        "combinatorics (κ-half-sym sum is +0.5·h², not the claimed "
        "−G·h² ≈ −0.916·h² — different sign AND magnitude).  Composed "
        "with PR #942's substrate flavor split, the script predicts "
        "m_p ≈ 950 MeV, m_n ≈ 952 MeV — ~1.3 % vs CODATA, gap halved "
        "from the canonical-only (Family A) ~2.9 %, but the categorical "
        "justification gap means this 950 MeV match is currently a "
        "numerical curiosity (or possibly a coincidence) pending "
        "either (a) precise definition of Π_HS differing from "
        "conjugation-averaging, (b) direct Yekutieli 2015 non-abelian "
        "Stokes evaluation, or (c) sign-convention reconciliation.  "
        "Probe / comparison column ONLY — NOT a production replacement; "
        "the production prediction in `m_p_borromean_verification_50dps.py` "
        "uses the PROVED canonical λ_A only."
    )
    w.set_content_block("conj:lambda-scale-bring-bloch-identity")
    w.add_parameter("derivation_status",
                    "EMPIRICAL_MATCH_AWAITING_CATEGORICAL_BACKING")
    w.add_parameter("reclassification_audit",
                    "docs/audits/2026-05-23-yekutieli-bijection-"
                    "natural-reading-negative.md")
    w.add_parameter("cal_class", "CAL-1 m_e only")
    w.add_parameter("lambda_scale_form",
                    "λ_canonical + λ_Yekutieli = 5/2 + (3/4 − G)·h²")
    w.add_parameter("gating_conjecture",
                    "cell-↔-half-sym-projection bijection at H_4 "
                    "(docs/audits/2026-05-22-yekutieli-percell-conjecture-"
                    "formalized.md §Conjecture)")
    w.add_parameter("q_0", mp.nstr(Q, 20))
    w.add_parameter("hbar_q", mp.nstr(HBAR_Q, 20))
    w.add_parameter("Vol_B3_8G", mp.nstr(VOL_B3, 20))
    w.add_parameter("m_e_codata_MeV", mp.nstr(M_E, 20))

    # ── λ values: canonical (production) vs Yekutieli (conditional) ──
    lam_canonical = lambda_scale_family_a(Q, Q_INV)
    lam_yekutieli = lambda_scale_yekutieli_extended(Q, Q_INV)
    yekutieli_curvature = lam_yekutieli - lam_canonical  # = -G · h²
    w.add_data("lambda_scale_comparison", {
        "lambda_canonical_family_a": mp.nstr(lam_canonical, 25),
        "lambda_yekutieli_extended": mp.nstr(lam_yekutieli, 25),
        "yekutieli_curvature_term":  mp.nstr(yekutieli_curvature, 25),
        "G_catalan": mp.nstr(mp.catalan, 25),
        "h_squared": mp.nstr((Q - Q_INV) ** 2, 25),
        "ratio_yekutieli_to_canonical": mp.nstr(lam_yekutieli / lam_canonical, 15),
    })

    # ── m_avg under each λ ────────────────────────────────────────
    factor = VOL_B3 / HBAR_Q ** 2
    m_avg_canonical = factor * lam_canonical * M_E
    m_avg_yekutieli = factor * lam_yekutieli * M_E
    rel_canonical = (m_avg_canonical - M_AVG_CODATA) / M_AVG_CODATA
    rel_yekutieli = (m_avg_yekutieli - M_AVG_CODATA) / M_AVG_CODATA
    w.add_data("m_avg_predictions", {
        "m_avg_canonical_MeV":  mp.nstr(m_avg_canonical, 18),
        "m_avg_yekutieli_MeV":  mp.nstr(m_avg_yekutieli, 18),
        "m_avg_codata_MeV":     mp.nstr(M_AVG_CODATA, 12),
        "rel_diff_canonical_pct": mp.nstr(rel_canonical * 100, 8),
        "rel_diff_yekutieli_pct": mp.nstr(rel_yekutieli * 100, 8),
        "gap_reduction_factor": mp.nstr(abs(rel_canonical) / abs(rel_yekutieli), 6),
    })

    # ── m_p / m_n with substrate flavor split (Yekutieli column) ──
    dm_over_Mn = flavor_split_subleading(Q, Q_INV)
    m_p_yek = m_avg_yekutieli * (mp.mpf(1) - dm_over_Mn / 2)
    m_n_yek = m_avg_yekutieli * (mp.mpf(1) + dm_over_Mn / 2)
    rel_p = (m_p_yek - M_P_CODATA) / M_P_CODATA
    rel_n = (m_n_yek - M_N_CODATA) / M_N_CODATA
    delta_pn = m_n_yek - m_p_yek
    delta_codata = M_N_CODATA - M_P_CODATA
    w.add_data("composed_predictions_yekutieli_plus_flavor_split", {
        "formula": "m_{p,n} = (Vol·λ_Yekutieli/ℏ_q²)·m_e · (1 ∓ Δm/M_N / 2)",
        "delta_m_over_M_N":  mp.nstr(dm_over_Mn, 20),
        "m_p_pred_MeV":      mp.nstr(m_p_yek, 18),
        "m_n_pred_MeV":      mp.nstr(m_n_yek, 18),
        "m_p_codata_MeV":    mp.nstr(M_P_CODATA, 12),
        "m_n_codata_MeV":    mp.nstr(M_N_CODATA, 12),
        "rel_diff_m_p_pct":  mp.nstr(rel_p * 100, 8),
        "rel_diff_m_n_pct":  mp.nstr(rel_n * 100, 8),
        "delta_m_pn_pred_MeV":   mp.nstr(delta_pn, 12),
        "delta_m_pn_codata_MeV": mp.nstr(delta_codata, 12),
        "delta_rel_diff_pct": mp.nstr(((delta_pn - delta_codata) / delta_codata) * 100, 6),
    })

    # Headline assertion — the Yekutieli extension halves the m_avg
    # residual from ~2.9% (canonical) to ~1.4% (with the Yekutieli
    # additive).  Gate: gap_reduction_factor > 1.5x.
    gap_ratio = float(abs(rel_canonical) / abs(rel_yekutieli))
    w.add_assertion(
        "yekutieli_extension_halves_m_avg_gap",
        computed=gap_ratio,
        expected=2.07,  # canonical 2.89% / yekutieli 1.40% ≈ 2.07
        tolerance=0.5,  # accept 1.5x .. 2.5x band
        unit="ratio (canonical_gap / yekutieli_gap)",
        source=(
            "Strategy I: canonical Wedderburn `+3/4·h²` + Yekutieli "
            "per-cell `−G·h²` ≈ 2.49266 (vs canonical 2.55304); "
            "Vol·λ_Yek/ℏ_q²·m_e ≈ 951 MeV; "
            "1.4% vs CODATA m_avg vs canonical 2.9%."
        ),
    )

    w.add_caveat(
        "RECLASSIFIED 2026-05-23: the load-bearing "
        "cell-↔-half-sym-projection bijection at H_4 (audit "
        "`docs/audits/2026-05-22-yekutieli-percell-conjecture-"
        "formalized.md` §Conjecture) is NOT supported by natural-"
        "reading partition combinatorics, per "
        "`docs/audits/2026-05-23-yekutieli-bijection-natural-reading-"
        "negative.md`.  Empirical κ_λ findings (Richardson-extrapolated "
        "50 dps): κ_(4) = κ_(1^4) = 0, κ_(3,1) = κ_(2,1,1) = κ_(2,2) = 1.  "
        "Sum is 3 (consistent with Family A's 3/4·h² theorem) but is "
        "SYMMETRIC under conjugation involution, so the natural-reading "
        "half-sym projection (conjugation averaging) gives +0.5·h², "
        "NOT the audit's −G·h² ≈ −0.916·h² (different sign and "
        "magnitude).  The 950 MeV prediction therefore stands as a "
        "numerical match WITHOUT the substrate-pure categorical "
        "backing the brief claimed.  Closing the gap requires either: "
        "(1) a different operator definition for Π_HS; (2) Yekutieli "
        "2015's non-abelian Stokes machinery applied beyond partition "
        "combinatorics; or (3) sign-convention reconciliation.  Until "
        "one of these closes, treat the Yekutieli-extended prediction "
        "as empirical-only (NOT a substrate-pure framework prediction).  "
        "Production `m_p_borromean_verification_50dps.py` continues to "
        "use ONLY the PROVED canonical λ_A."
    )

    out = w.save()
    print(f"Witness emitted: {out.name}")
    print()
    print(f"λ_canonical (Family A)   = {float(lam_canonical):.10f}")
    print(f"λ_Yekutieli extended     = {float(lam_yekutieli):.10f}")
    print(f"Yekutieli curvature −Gh² = {float(yekutieli_curvature):.10f}")
    print()
    print(f"m_avg^canonical  = {float(m_avg_canonical):.6f} MeV  ({float(rel_canonical*100):+.4f} %)")
    print(f"m_avg^Yekutieli  = {float(m_avg_yekutieli):.6f} MeV  ({float(rel_yekutieli*100):+.4f} %)")
    print(f"  gap reduction: {gap_ratio:.3f}x")
    print()
    print(f"With flavor split:")
    print(f"  m_p^Yek = {float(m_p_yek):.6f} MeV  vs CODATA {float(M_P_CODATA):.6f}  ({float(rel_p*100):+.4f} %)")
    print(f"  m_n^Yek = {float(m_n_yek):.6f} MeV  vs CODATA {float(M_N_CODATA):.6f}  ({float(rel_n*100):+.4f} %)")
    print(f"  Δm_pn   = {float(delta_pn):.6f} MeV  vs CODATA {float(delta_codata):.6f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
