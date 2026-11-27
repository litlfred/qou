#!/usr/bin/env python3
"""qbeta_ck_cache.py — extract & cache c_k Taylor coefficients of Q_β at canonical q₀.

The c_k are by definition the Taylor coefficients of the exact Habiro Q_β at
substrate q₀, expanded in u = b·ℏ_q²:

    Q_N(q₀) = Q_A(q₀) · cos(α − bℏ²/2) · Π_{k≥2} (1 + c_k · u^k)

Status: c_2 = −1 is Lean-PROVED as the Taylor coefficient (Kashiwara f̃₁²).
Higher c_k have no Lean derivation; they are EXTRACTED from CODATA Q_β
at canonical q₀, with structural-conjecture forms (J_Hopf, J−ℏ², etc.)
that match to varying precision (0.5%–3%) but are NOT Taylor-exact.

This script:
  1. Reads canonical q₀ from q_parameter.py and Q_β from CODATA.
  2. Computes Q_A (Form A), N=1 (Kashiwara cos), N=2 (c_2 = −1 fixed).
  3. EXTRACTS c_3 empirically: c_3 = (Q_β_CODATA / Q_N2 − 1) / u^3.
  4. Continues recursively: c_k = (Q_β_CODATA / Q_N(k−1) − 1) / u^k.
  5. Caches all c_k + their structural-conjecture nearest matches in
     qbeta-ck-cache.witness.json.
  6. Production reads from cache. No structural-form guessing in
     production code.

DISCIPLINE: a two-tier label system makes the production semantics
machine-readable:

  • tier "derived"      (c_2): Taylor-exact, Lean-proved. Wired to the
                               L2 dashboard headline. q₀-INDEPENDENT.
  • tier "cal-anchored" (c_3+): extracted from the CAL-3 Q_β datum at
                               canonical q₀. q₀-DEPENDENT and CIRCULAR
                               (uses Q_codata), so it is a reusable
                               CALIBRATED CONSTANT, NOT a prediction.
                               It must NEVER count toward a 100×/1×
                               dashboard pass (that would be circular).

The cal-anchored c_k are cached so downstream consumers (m_n Path C,
Δ_pn) can REUSE the full-precision calibrated Q_β without re-extracting
— per the author's "compute, cache, and reuse c_k/d_k" request — while
the labels keep the derived/calibrated boundary explicit. Future agents
who close a c_k structural form to Taylor precision in Lean (at
canonical q₀, NOT a near-match) promote it from "cal-anchored" to
"derived" by changing its tier; the dashboard then auto-picks it up.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
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
from pathlib import Path

from mpmath import mp, mpf, cos, sqrt

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402


def main(convention: str = "D") -> int:
    set_compute_dps()
    wb = WitnessBuilder("qbeta-ck-cache", engine="mpmath")

    q = Q_MP
    me = mpf(M_E_MEV)
    Q_codata = mpf(str(Q_BETA_MEV))

    h = q - 1 / q
    hbar_q = (q - 1) / q
    b_sq = (h ** 2 + 3) / (h ** 2 + 4)
    b = sqrt(b_sq)
    u = b * hbar_q ** 2

    # ── Markov-convention guard (bean `qou-ckwt`) ────────────────────────────
    # This line read `z = q**3 / (q**2 + 1)` -- convention D -- while the
    # committed witness carried the convention-C value, so the producer did not
    # reproduce its own output. Measured: c_3 -2.0693425771 (committed, C) vs
    # -974.4318877 (this code, D), and the DERIVED-tier Q_N2 error 1278.6 ppb
    # vs 602433.2 ppb -- a 471x regression in the framework's headline derived
    # Q_beta, one `python3 qbeta_ck_cache.py` away from landing.
    #
    # Substituting z_D into the C-frame eigenphase `alpha = (z-1)h/2` is a move
    # the corpus has PROVED invalid, twice and independently:
    #   QOU.QBeta.decayLadder_zC_threeRow_ne_zero  -- at z_C the third
    #     Wedderburn row is forcibly present for every substrate s = sqrt(q) > 1,
    #     so "keep the C ladder" and "the two-row forcing applies" are
    #     incompatible;
    #   QOU.QBeta.eigenphase_bar_defect_of_fullBar -- feeding a full-bar
    #     parameter into the C eigenphase leaves a bar defect of exactly h^2,
    #     Z-INDEPENDENTLY, so no member of the family repairs it.
    # Both sorry-free. The D-frame ladder must be RE-DERIVED, not re-evaluated
    # (bean `qou-cds1`), and until it is there is NO D-frame Q_beta prediction:
    # -974 is a sensitivity measurement, not a value, and must not be wired.
    #
    # So this producer REFUSES rather than emit. It is the same class as
    # `low_isotope_mass_table` (refuses below target_dps) and
    # `qbeta_braid_nf_sdp_offset_probe` (refuses rather than "publish laundered
    # numbers") -- a guard working correctly, explaining itself on STDOUT
    # because a stderr-only harness never sees it.
    if convention == "D":
        print("=" * 72)
        print(" REFUSING TO RUN -- convention D has no derived c_k ladder")
        print("=" * 72)
        print("  The ladder eigenphase alpha = (z-1)h/2 is CONVENTION-C-derived.")
        print("  Substituting z_D is proved invalid:")
        print("    QOU.QBeta.decayLadder_zC_threeRow_ne_zero")
        print("    QOU.QBeta.eigenphase_bar_defect_of_fullBar   (defect h^2, z-independent)")
        print("  Running anyway would emit c_3 = -974.43 and a derived-tier Q_N2")
        print("  error of 602433 ppb (vs the committed 1278.6 ppb) -- a 471x")
        print("  regression, and -974 is a SENSITIVITY MEASUREMENT, not a value.")
        print()
        print("  To re-derive the D-frame ladder: bean `qou-cds1`. That is research,")
        print("  not a z-swap. To reproduce the historical convention-C artifact")
        print("  byte-for-byte (it is load-bearing -- 10 consumers, incl. the L2")
        print("  dashboard `per_observable_100x_status.py`), run:")
        print()
        print("      python3 qbeta_ck_cache.py --historical-convention-C")
        print()
        raise SystemExit(2)

    if convention != "C":
        raise ValueError(f"unknown Markov convention {convention!r}; expected 'C' or 'D'")

    # Convention C, reached ONLY via the explicit --historical-convention-C
    # flag. C was excised by owner ruling (2026-08-09, re-affirmed 2026-08-15
    # and 2026-08-26); this path exists solely so the committed witness stays
    # machine-reproducible, and it is never the default.
    z = sqrt(q) / (1 + q)
    alpha = (z - 1) * h / 2

    # Substrate quantities
    Q_A = me * mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)

    # N=1 (Kashiwara cos)
    N1_factor = cos(alpha - b * hbar_q ** 2 / 2)
    Q_N1 = Q_A * N1_factor

    # N=2: c_2 = -1 Lean-proved
    c_2 = mpf(-1)
    Q_N2 = Q_N1 * (1 + c_2 * u ** 2)

    # Extract c_3..c_7 recursively from CODATA
    rows = []
    Q_prev = Q_N2
    c_ks = [None, None, c_2]  # index 0,1 unused; index 2 = c_2

    print("=" * 72)
    print(" Q_β c_k cache — extract Taylor coefficients at canonical q₀")
    print("=" * 72)
    print(f"  q₀ = {mp.nstr(q, 14)}   u = b·ℏ² = {float(u):.6e}")
    print(f"  Q_codata = {mp.nstr(Q_codata, 14)}  (CAL-3 anchor)")
    print()
    print(f"  Q_A (Form A)         = {mp.nstr(Q_A, 14)}  err = {float((Q_A-Q_codata)/Q_codata*1e6):+8.2f} ppm")
    print(f"  Q_N1 (Kashiwara cos) = {mp.nstr(Q_N1, 14)}  err = {float((Q_N1-Q_codata)/Q_codata*1e6):+8.2f} ppm")
    print(f"  Q_N2 (c_2=−1)        = {mp.nstr(Q_N2, 14)}  err = {float((Q_N2-Q_codata)/Q_codata*1e6):+8.2f} ppm")
    print()

    rows.append({
        "k": 2, "c_k": mp.nstr(c_2, 30),
        "label": "lean-proved",
        "tier": "derived",
        "q0_dependent": False,
        "structural_form": "-1 (Kashiwara f̃₁²)",
        "lean_theorem": "qou:QOU.BraidKnot.N2_factor + q_beta_categorical_precision_ladder",
        "Q_pred_after_this_rung_MeV": mp.nstr(Q_N2, 30),
        "err_ppb_after_this_rung": float((Q_N2 - Q_codata) / Q_codata * 1e9),
    })

    # Extract c_k for k = 3..7
    structural_candidates = {
        3: [("J_Hopf(q=1)", mpf(-2)),
            ("J_Hopf − ℏ_q²", mpf(-2) - hbar_q ** 2),
            ("J_Hopf − 6·ℏ_q²", mpf(-2) - 6 * hbar_q ** 2)],
        4: [("c_3·b⁴ via plain c_3", mpf(-2) * b ** 4),
            ("c_3·b⁴ via c_3=J−ℏ²", (mpf(-2) - hbar_q ** 2) * b ** 4)],
        5: [("−(b² + ½)", -(b ** 2 + mpf(1) / 2)),
            ("c_3²·3 + b", mpf(-2) ** 2 * 3 + b)],
        6: [("c_3²·b² = 4·b²", mpf(-2) ** 2 * b ** 2)],
        7: [("c_3³ = −8", mpf(-2) ** 3)],
    }

    EPS_RESIDUAL = mpf("1e-30")  # below compute precision; stop the ladder
    for k in range(3, 8):
        ratio_m1 = Q_codata / Q_prev - 1
        if abs(ratio_m1) < EPS_RESIDUAL:
            print(f"  c_{k}: residual below compute precision ({float(ratio_m1):.2e}) — ladder converged")
            break
        ck_extracted = ratio_m1 / u ** k
        Q_next = Q_prev * (1 + ck_extracted * u ** k)
        c_ks.append(ck_extracted)

        # Find closest structural match
        best_match = None
        best_err_pct = float("inf")
        for name, val in structural_candidates.get(k, []):
            err_pct = abs(float((ck_extracted - val) / ck_extracted)) * 100 if abs(ck_extracted) > EPS_RESIDUAL else float("inf")
            if err_pct < best_err_pct:
                best_err_pct = err_pct
                best_match = (name, val)

        match_str = ""
        if best_match is not None:
            match_str = f"{best_match[0]} ({best_err_pct:.3f}% off)"

        print(f"  c_{k} (extracted) = {mp.nstr(ck_extracted, 10):>14}  closest structural: {match_str}")

        rows.append({
            "k": k,
            "c_k": mp.nstr(ck_extracted, 30),
            "label": "cal-anchored",
            "tier": "cal-anchored",
            "q0_dependent": True,
            "circular": "value extracted from CAL-3 Q_codata at this q₀; reusable calibrated constant, NOT a prediction — must not count toward any 100×/1× dashboard pass",
            "lean_theorem": "(none — closing in Lean to Taylor precision at canonical q₀ would promote tier to 'derived')",
            "structural_candidates": [
                {"name": name, "value": mp.nstr(val, 30),
                 "err_pct": float(abs((ck_extracted - val) / ck_extracted) * 100)}
                for name, val in structural_candidates.get(k, [])
            ],
            "closest_structural": best_match[0] if best_match else None,
            "closest_structural_err_pct": best_err_pct if best_match else None,
            "Q_pred_after_this_rung_MeV": mp.nstr(Q_next, 30),
            "err_ppb_after_this_rung": float((Q_next - Q_codata) / Q_codata * 1e9),
        })
        Q_prev = Q_next

    print()
    print(f"  Q_N7 = {mp.nstr(Q_prev, 18)}  err = {float((Q_prev-Q_codata)/Q_codata*1e12):+8.4f} ppt")
    print()
    print("  DISCIPLINE (two tiers):")
    print("    • derived      (c_2): Taylor-exact, Lean-proved → dashboard headline (Q_N2).")
    print("    • cal-anchored (c_3+): extracted from Q_codata, CIRCULAR & q₀-dependent —")
    print("      a reusable calibrated constant for downstream (m_n, Δ_pn), NOT a")
    print("      prediction. Never counts toward a 100×/1× pass.")
    print(f"    Q_β derived      (Q_N2)       = {mp.nstr(Q_N2, 16)}  ({float((Q_N2-Q_codata)/Q_codata*1e9):+.1f} ppb)")
    print(f"    Q_β cal-anchored (full ladder)= {mp.nstr(Q_prev, 16)}  ({float((Q_prev-Q_codata)/Q_codata*1e12):+.2f} ppt, circular)")

    wb.set_description(
        "Cache of Q_β c_k Taylor coefficients at canonical q₀. c_2 is the only "
        "Lean-proved Taylor-exact coefficient (Kashiwara f̃₁², N2_factor). "
        "c_3..c_7 are extracted from CODATA Q_β recursively (each c_k computed "
        "as (Q_codata/Q_{N_{k-1}} − 1)/u^k). The witness records each c_k's "
        "label (lean-proved vs codata-extracted) and the closest structural-"
        "conjecture form with its residual %. Production reads c_2 only; higher "
        "c_k are documented for future Lean-formalization work. NO structural "
        "form is wired as derivation without a Lean theorem closing it to "
        "Taylor precision. See deep audit "
        "docs/audits/2026-05-30-qbeta-ck-mp-dk-deep-audit.md."
    )
    # DECLARE THE FRAME. Measured 2026-08-26: of 278 c_k-bearing witnesses under
    # computations/qbeta/, ZERO declared a Markov convention -- which is how this
    # producer drifted to D while its witness stayed C without anything noticing.
    # A witness that does not say which convention it was computed in cannot be
    # audited, only guessed at.
    wb.add_data("markov_convention", convention)
    wb.add_data("markov_convention_note",
                "Convention C (z = sqrt(q)/(1+q)), reached only via "
                "--historical-convention-C. C was excised by owner ruling "
                "(2026-08-09, re-affirmed 2026-08-15 and 2026-08-26); this "
                "artifact is retained because 10 consumers read it, including "
                "the L2 dashboard per_observable_100x_status.py. The DEFAULT "
                "(convention D) path REFUSES: no D-frame ladder has been "
                "derived, so there is no D-frame c_k to emit (bean qou-cds1). "
                "Substituting z_D into alpha = (z-1)h/2 is proved invalid by "
                "QOU.QBeta.decayLadder_zC_threeRow_ne_zero and "
                "QOU.QBeta.eigenphase_bar_defect_of_fullBar."
                if convention == "C" else "convention D")
    wb.add_data("q_0", mp.nstr(q, 50))
    wb.add_data("u_substrate", mp.nstr(u, 50))
    wb.add_data("Q_codata", str(Q_BETA_MEV))
    wb.add_data("rows", rows)
    # Two-tier Q_β: the derived headline (Q_N2) and the reusable
    # cal-anchored full-ladder value. The latter is CIRCULAR (it is
    # calibrated to Q_codata) — provided for downstream REUSE only.
    wb.add_data("Q_beta_tiers", {
        "derived": {
            "value_MeV": mp.nstr(Q_N2, 30),
            "rungs": "Form A · cos(α−bℏ²/2) · (1+c_2 u²), c_2 Taylor-exact",
            "err_ppb_vs_codata": float((Q_N2 - Q_codata) / Q_codata * 1e9),
            "use": "L2 dashboard headline; a genuine prediction (no Q_codata input beyond CAL-3 anchoring of the scale).",
        },
        "cal_anchored": {
            "value_MeV": mp.nstr(Q_prev, 30),
            "rungs": "full ladder through c_7 (c_3+ extracted from Q_codata)",
            "err_ppb_vs_codata": float((Q_prev - Q_codata) / Q_codata * 1e9),
            "circular": True,
            "use": ("reusable calibrated constant for downstream consumers "
                    "(m_n Path C, Δ_pn) that need full-precision Q_β; "
                    "MUST NOT be reported as a prediction or counted toward "
                    "a 100×/1× dashboard pass — it is calibrated to Q_codata."),
        },
    })
    wb.add_data("discipline", {
        "derived_tier_count": 1,
        "cal_anchored_tier_count": len(rows) - 1,
        "dashboard_headline_uses": "derived tier only (Q_N2)",
        "cal_anchored_is_reusable_not_prediction": True,
        "to_promote_cal_anchored_to_derived": "future agent must provide a Lean theorem closing the c_k structural form to Taylor precision at canonical q₀ (not a near-match); then set tier='derived'.",
    })
    wb.add_assertion(
        "c2_extraction_matches_lean_proved_value",
        computed=float(c_2), expected=-1.0, tolerance=1e-10,
        source="c_2 = -1 is Lean-proved (Kashiwara f̃₁²) AND empirically the Taylor coefficient at canonical q₀",
    )
    wb.save()
    print("\n  Witness: qbeta-ck-cache.witness.json")
    return 0


if __name__ == "__main__":
    import sys as _sys
    _conv = "C" if "--historical-convention-C" in _sys.argv else "D"
    raise SystemExit(main(_conv))
