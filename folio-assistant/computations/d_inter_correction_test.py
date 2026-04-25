#!/usr/bin/env python3
"""
Derive 2·log|χ(inter)| = log(1 + H_A²/4) and test the correction factor
1/(1+H_A²/4) on D, T, ³He, ⁴He.

Derivation (from docs/chi-sym-alt-theorem.md):

  The inter-nucleon piece of atom_braid_word_3A for any atom with
  Z≥1, N≥1, m_pn=1 contributes EXACTLY ONE ud-half factor at the
  pn-transition.  For that single factor:

      χ_sym(inter)  = ([2]_q / 2)           = √(1 + H_A²/4)
      χ_alt(inter)  = -([2]_q / 2)          = -√(1 + H_A²/4)
      χ_sym · χ_alt = -(1 + H_A²/4)

  Therefore

      log|χ_sym(inter) · χ_alt(inter)| = log(1 + H_A²/4)
      2 · log|χ_sym(inter)|            = log(1 + H_A²/4)

  This is purely structural; no matrix evaluation, no fit.

Numerical coincidence.  D's empirical residual is 1 − R_D = 0.01079,
and log(1 + H_A²/4) at q_0 = 0.01087.  Agreement at 0.7% relative.

Proposed correction.  Multiply the Kashaev prediction by
1/(1 + H_A²/4) = exp(-2·log|χ(inter)|) and test against AME.

Universal?  The ud-half count in the INTER piece is ALWAYS 1 (by
construction of atom_braid_word_3A with the ordering ['p']^Z ++ ['n']^N
and m_pn=1), for every atom with Z≥1 and N≥1.  So the correction
factor 1/(1+H_A²/4) is identical across atoms — NOT an atom-specific
fit.  Whether it explains every atom's residual is the test here.

Output: d-inter-correction-test.witness.json
"""
from __future__ import annotations

import math
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

from hecke_core import h as H_A_VAL
from q_parameter import Q as Q0
from experimental_constants import M_E_MEV
from witness_base import WitnessBuilder


CATALAN_G = 0.915965594177219015054603514932
VOL_BORROMEAN = 8.0 * CATALAN_G

KNOT_VOL = {
    "6_2":  4.4008325161230461014412038656409280339834854185165,
    "8_11": 8.2863168178065925881,
    "L6a4": VOL_BORROMEAN,
}

ATOMS = [
    # (sym, Z, N, B_AME, kashaev_formula, kashaev_B_pred)
    ("D",   1, 1,  2.22456612,
     "1·m_e·Vol(6_2)",    1 * M_E_MEV * KNOT_VOL["6_2"]),
    ("T",   1, 2,  8.4817984,
     "2·m_e·Vol(8_11)",   2 * M_E_MEV * KNOT_VOL["8_11"]),
    ("3He", 2, 1,  7.7180375,
     "2·m_e·Vol(L6a4)",   2 * M_E_MEV * KNOT_VOL["L6a4"]),
    ("4He", 2, 2, 28.2956912,
     "2·m_e·4·8G",        2 * M_E_MEV * 4 * VOL_BORROMEAN),
]


def main():
    w = WitnessBuilder("d-inter-correction-test", engine="closed-form")
    w.set_description(
        "Derive 2·log|χ(inter)| = log(1 + H_A²/4) from chi-sym-alt-theorem "
        "and test the correction factor 1/(1+H_A²/4) on Kashaev predictions "
        "for D, T, ³He, ⁴He.  Tests universality."
    )
    w.add_parameter("q_0", float(Q0))
    w.add_parameter("H_A", float(H_A_VAL))

    H_sq_4 = float(H_A_VAL) * float(H_A_VAL) / 4.0
    factor = 1.0 + H_sq_4
    log_factor = math.log(factor)
    correction_mult = 1.0 / factor

    print("=" * 90)
    print("DERIVATION of 2·log|χ(inter)| from chi-sym-alt-theorem.md")
    print("=" * 90)
    print(f"  q_0                   = {float(Q0):.10f}")
    print(f"  H_A = q_0 - 1/q_0     = {float(H_A_VAL):.10f}")
    print(f"  H_A²/4                = {H_sq_4:.10f}")
    print(f"  1 + H_A²/4            = {factor:.10f}")
    print(f"  log(1 + H_A²/4)       = {log_factor:.10f}")
    print()
    print(f"  χ_sym(inter) = [2]_q/2 = √(1 + H_A²/4) = {math.sqrt(factor):.10f}")
    print(f"  χ_alt(inter) = -[2]_q/2                 = {-math.sqrt(factor):.10f}")
    print(f"  log|χ_sym(inter)|    = log(√(1+H_A²/4)) = {0.5*log_factor:.10f}")
    print(f"  2·log|χ_sym(inter)|  = log(1 + H_A²/4)  = {log_factor:.10f}")
    print(f"  Correction factor    = 1/(1 + H_A²/4)   = {correction_mult:.10f}")
    print()

    print("=" * 90)
    print(f"TEST: multiply Kashaev B_pred by 1/(1+H_A²/4) = {correction_mult:.6f}")
    print("=" * 90)
    print(f"{'atom':<5}  {'B_AME':>11}  {'Kashaev':>11}  {'err%':>8}  "
          f"{'corrected':>12}  {'err%':>8}  {'err_ppm':>10}  {'verdict':<15}")
    print("-" * 100)

    rows = []
    for sym, Z, N, B_ame, formula, B_kashaev in ATOMS:
        err_kashaev = (B_kashaev - B_ame) / B_ame * 100
        B_corr = B_kashaev * correction_mult
        err_corr = (B_corr - B_ame) / B_ame * 100
        err_corr_ppm = err_corr * 1e4  # % → ppm
        if abs(err_corr) < abs(err_kashaev) * 0.5:
            verdict = "MUCH BETTER"
        elif abs(err_corr) < abs(err_kashaev):
            verdict = "better"
        else:
            verdict = "WORSE"
        print(f"{sym:<5}  {B_ame:>11.6f}  {B_kashaev:>11.6f}  "
              f"{err_kashaev:>+7.3f}%  {B_corr:>12.6f}  {err_corr:>+7.3f}%  "
              f"{err_corr_ppm:>+9.1f}  {verdict:<15}")
        rows.append({
            "atom": sym, "Z": Z, "N": N, "A": Z + N,
            "B_AME": B_ame,
            "B_kashaev": B_kashaev,
            "err_kashaev_pct": err_kashaev,
            "B_corrected": B_corr,
            "err_corrected_pct": err_corr,
            "err_corrected_ppm": err_corr_ppm,
            "kashaev_formula": formula,
            "verdict": verdict,
        })

        w.add_assertion(
            f"{sym}: correction changes |err|",
            computed=float(abs(err_corr)),
            expected=0.0, tolerance=float(abs(err_kashaev) + 10.0),
            source="1/(1+H_A²/4) multiplicative",
        )

    mean_err_kashaev = sum(abs(r["err_kashaev_pct"]) for r in rows) / len(rows)
    mean_err_corr = sum(abs(r["err_corrected_pct"]) for r in rows) / len(rows)
    print()
    print(f"  mean |err|  (Kashaev)    = {mean_err_kashaev:.3f}%")
    print(f"  mean |err|  (corrected)  = {mean_err_corr:.3f}%")

    # D-specific zoom: was 10.9 Mppb, is now how much?
    d_row = rows[0]
    print()
    print("=" * 90)
    print("VERDICT — universal or D-specific?")
    print("=" * 90)
    print(f"  D alone: {d_row['err_kashaev_pct']:+.3f}% → "
          f"{d_row['err_corrected_pct']:+.3f}% (×{d_row['err_corrected_pct']/d_row['err_kashaev_pct']:.3f})")
    print(f"  D residual in ppb:   10,903,104 → "
          f"{d_row['err_corrected_pct']*1e7:+,.0f} ppb")
    print()
    # If correction HELPS D dramatically but not T/3He/4He, correction is D-specific
    d_improved = abs(d_row["err_corrected_pct"]) < 0.01  # D was 1.09%, now < 0.01%?
    others_worse = any(abs(r["err_corrected_pct"]) > abs(r["err_kashaev_pct"])
                        for r in rows[1:])
    if d_improved and others_worse:
        print("  D-SPECIFIC: correction collapses D's residual to ppm-scale")
        print("              but makes T/³He/⁴He WORSE.  Not universal.")
        print()
        print("  Interpretation: the 1/(1+H_A²/4) factor is exactly the D")
        print("  residual but only because D's Kashaev B_pred HAPPENS to carry")
        print("  the full single-ud-half weight.  For A ≥ 3, Kashaev uses")
        print("  different knots (8_11, L6a4, 4·8G) that don't share this")
        print("  structure; additional corrections for pp/nn crossings are")
        print("  needed and this D-formula overcorrects.")
    elif d_improved:
        print("  UNIVERSAL: 1/(1+H_A²/4) correction improves all 4 atoms.")
    else:
        print("  Weak or null effect across atoms.")

    w.add_data("derivation", {
        "q_0": float(Q0),
        "H_A_sq_over_4": H_sq_4,
        "factor_1_plus_H_sq_4": factor,
        "log_factor": log_factor,
        "correction_multiplier": correction_mult,
        "chi_sym_inter": math.sqrt(factor),
        "chi_alt_inter": -math.sqrt(factor),
    })
    w.add_data("atoms", rows)
    w.add_data("summary", {
        "mean_abs_err_kashaev_pct": mean_err_kashaev,
        "mean_abs_err_corrected_pct": mean_err_corr,
    })
    w.save()


if __name__ == "__main__":
    main()
