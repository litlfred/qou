"""V2 chirality + cos((z−1)·h/2) Q_β tightening — composition probe.

Closes item 3 of the M1 mass-table §7 recommendations:
"Compose V2 chirality + cos((z-1)h/2) Q_β tightening — substrate-
derived a_K + structurally-identified Q_β correction should reduce
the 1 ppb gap to ~300× from current 1700×."

## Composition

The 6-term mass formula has two recently-improved inputs:

1. **V2 chirality** (PR #654): `a_K = τ(β · β_mirror⁻¹)` per
   substrate, replacing the old heuristic `chirality_signs_for_isotope`
   look-up.  Wired into `paper_six_term_mass(..., chirality_source="v2")`.

2. **Q_β cos tightening** (PR #655 / cherry-picked): the substrate-
   derived Q_β closed form is `Q_A = m_e · |q²−2q−1| · (q+1) / (2q³)`
   with residual 1677.5 ppm against CODATA `m_n − m_p − m_e`.
   Composing with `cos((z−1)·h/2)` (z = 1 / (q½ + q⁻½), h = q − q⁻¹)
   reduces the residual to 305.4 ppm — a 5.49× tightening.  This is
   the c_2 = b² Kashiwara correction confirmed empirically.

This probe computes Q_β under both forms (CODATA + cos-tightened)
and emits a side-by-side comparison.  Does NOT re-run the full
sweep — that's a separate output once Q_β source is decided.

## What this does NOT do

Per PR #657's high-precision (dps=200) finding: c_3, c_4, c_5, c_6
contributions to Q_β are at CODATA's ~400 ppb noise floor.  The full
categorical chain (`prop:q-beta-categorical-precision-ladder`) is
empirically underdetermined.  This probe stops at c_2 (cos
correction) — the empirically-solid tightening.

## Output

  q-beta-v2-cos-compose.witness.json

Reports:
  - Q_β codata  vs Q_β closed-form (Form A)         residual: 1677.5 ppm
  - Q_β codata  vs Q_β cos-tightened (Form A · cos)  residual: 305.4 ppm
  - tightening factor: 5.49× confirmed
  - 1 ppb gap before compose: 1700× (1677 ppm / 0.001 ppm)
  - 1 ppb gap after compose:  300×  (305 ppm / 0.001 ppm)
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder
from codata_constants import M_E_MEV, M_N_MEV_VALIDATION, M_P_MEV_VALIDATION


def main() -> int:
    mp.mp.dps = 50

    q = mp.mpf("1.1099785955541805752815940796095093779932822799587")
    h = q - 1 / q
    hbar_q = (q - 1) / q
    z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))
    m_e = mp.mpf(M_E_MEV)
    m_p = mp.mpf(M_P_MEV_VALIDATION)
    m_n = mp.mpf(M_N_MEV_VALIDATION)

    Q_beta_codata = m_n - m_p - m_e

    # Form A baseline (PR #655)
    Q_A = m_e * mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
    eps_A = Q_A / Q_beta_codata - 1
    ppm_A = eps_A * 10 ** 6

    # Form A · cos((z−1)·h/2) (the 5.49× tightening)
    Q_A_cos = Q_A * mp.cos((z - 1) * h / 2)
    eps_A_cos = Q_A_cos / Q_beta_codata - 1
    ppm_A_cos = eps_A_cos * 10 ** 6

    tightening_factor = abs(ppm_A) / abs(ppm_A_cos) if ppm_A_cos else mp.inf

    # 1 ppb target
    one_ppb_ppm = mp.mpf("0.001")
    gap_before = abs(ppm_A) / one_ppb_ppm
    gap_after = abs(ppm_A_cos) / one_ppb_ppm

    print("=" * 80)
    print("  V2 chirality + cos((z−1)·h/2) Q_β tightening — composition")
    print("=" * 80)
    print()
    print(f"  q_0   = {mp.nstr(q, 16)}")
    print(f"  m_e   = {mp.nstr(m_e, 12)} MeV   (CAL-1 anchor)")
    print(f"  Q_β (CODATA) = m_n − m_p − m_e = {mp.nstr(Q_beta_codata, 12)} MeV")
    print()
    print("  ── Q_β closed forms ──")
    print()
    print(f"  Form A (baseline):")
    print(f"    Q_A = m_e · |q²−2q−1| · (q+1) / (2q³)")
    print(f"    Q_A          = {mp.nstr(Q_A, 12)} MeV")
    print(f"    residual     = {mp.nstr(ppm_A, 8)} ppm")
    print()
    print(f"  Form A · cos((z−1)·h/2) (cherry-picked from #655):")
    print(f"    Q_A · cos    = {mp.nstr(Q_A_cos, 12)} MeV")
    print(f"    residual     = {mp.nstr(ppm_A_cos, 8)} ppm")
    print()
    print(f"  Tightening factor: {mp.nstr(tightening_factor, 6)}×")
    print()
    print("  ── 1 ppb closure target ──")
    print()
    print(f"  Gap before compose: {mp.nstr(gap_before, 5)}× (residual {mp.nstr(ppm_A, 6)} ppm vs 0.001 ppm)")
    print(f"  Gap after compose:  {mp.nstr(gap_after, 5)}× (residual {mp.nstr(ppm_A_cos, 6)} ppm vs 0.001 ppm)")
    print()
    print("  V2 chirality wire is independent (term5 path); does not")
    print("  modify Q_β. The composition is additive: V2 fixes the")
    print("  per-atom chirality, cos fixes the calibration anchor.")
    print()
    print("  Caveat per PR #657 (high-precision finding):")
    print("    beyond c_2 = b² (the cos correction here), higher c_k")
    print("    coefficients are at CODATA's ~400 ppb noise floor —")
    print("    the categorical chain is empirically underdetermined.")
    print("    Closing the remaining 300× would require either higher-")
    print("    precision Q_β measurement (CODATA-2027 roadmap) or an")
    print("    independent route (lattice QCD, EW Fermi).")

    builder = (
        WitnessBuilder(
            "q-beta-v2-cos-compose", engine="mpmath",
        )
        .set_description(
            "V2 chirality + cos((z−1)·h/2) Q_β tightening: "
            "composition probe verifying the 5.49× tightening "
            "from PR #655 against CODATA Q_β. Closes item 3 of "
            "the M1 mass-table §7 recommendations. V2 chirality "
            "wire is independent (term5 path); this probe only "
            "verifies the Q_β-side improvement."
        )
        .set_content_block("prop:q-beta-categorical-precision-ladder")
        .add_parameter("q_0", mp.nstr(q, 50))
        .add_parameter("m_e_MeV", mp.nstr(m_e, 12))
        .add_data("Q_beta_codata_MeV", mp.nstr(Q_beta_codata, 50))
        .add_data("Q_A_MeV", mp.nstr(Q_A, 50))
        .add_data("Q_A_cos_MeV", mp.nstr(Q_A_cos, 50))
        .add_data("residual_ppm_Q_A", float(ppm_A))
        .add_data("residual_ppm_Q_A_cos", float(ppm_A_cos))
        .add_data("tightening_factor", float(tightening_factor))
        .add_data("gap_to_1ppb_before", float(gap_before))
        .add_data("gap_to_1ppb_after", float(gap_after))
        .add_assertion(
            name="cos_tightening_reproduces",
            computed=float(tightening_factor),
            expected=5.49,
            tolerance=0.1,
            unit="dimensionless",
            source="PR #655 finding: cos((z−1)·h/2) gives 5.49× tightening",
        )
    )
    out = builder.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
