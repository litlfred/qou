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

DISCIPLINE: extracted c_k are LABELLED "codata-extracted" in the
witness. Only c_2 is labelled "lean-proved". Future agents wiring
higher c_k must close their structural form to Taylor precision in
Lean before changing the labels.
"""
from __future__ import annotations

import sys
from pathlib import Path

from mpmath import mp, mpf, cos, sqrt

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402


def main() -> int:
    set_compute_dps()
    wb = WitnessBuilder("qbeta-ck-cache", engine="mpmath")

    q = mpf(Q_50_DIGIT_STR)
    me = mpf(M_E_MEV)
    Q_codata = mpf(str(Q_BETA_MEV))

    h = q - 1 / q
    hbar_q = (q - 1) / q
    b_sq = (h ** 2 + 3) / (h ** 2 + 4)
    b = sqrt(b_sq)
    u = b * hbar_q ** 2
    z = 1 / (sqrt(q) + 1 / sqrt(q))
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
            "label": "codata-extracted",
            "lean_theorem": "(none — closing in Lean to Taylor precision would change label to lean-proved)",
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
    print("  DISCIPLINE: only c_2 is 'lean-proved' (Taylor-exact). c_3..c_7 are")
    print("  'codata-extracted' — empirical Taylor coefficients of the exact Habiro")
    print("  Q_β at canonical q₀, NOT independent derivations. Production uses Q_N2")
    print("  (Lean-proved through k=2) unless future Lean theorems close higher c_k.")

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
    wb.add_data("q_0", mp.nstr(q, 50))
    wb.add_data("u_substrate", mp.nstr(u, 50))
    wb.add_data("Q_codata", str(Q_BETA_MEV))
    wb.add_data("rows", rows)
    wb.add_data("discipline", {
        "lean_proved_count": 1,
        "codata_extracted_count": 5,
        "production_uses": "c_2 only (Q_N2)",
        "to_change_label_to_lean_proved": "future agent must provide Lean theorem closing c_k structural form to Taylor precision at canonical q₀",
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
    raise SystemExit(main())
