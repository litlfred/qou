#!/usr/bin/env python3
"""
²H (deuterium) error source breakdown toward 1 ppb precision.

Current strategy-A prediction: B(D) = m_e · Vol(6_2) = 2.24884 MeV
AME2020:                       B(D) = 2.22458 MeV
Residual:                      +24.26 keV   (+1.09% on B, -12.9 ppm on M)

Goal: identify contributions to the 24.26 keV discrepancy so that a
refined model can close the gap toward 1 ppb of total mass M(²H) =
1876.124 MeV (1 ppb ≈ 1.876 eV).

Error-source accounting:

  (1) Knot-matching mismatch — Vol(6_2) = 4.40083 vs B/m_e = 4.35438.
      Residual 0.04645 volume units × m_e = 23.73 keV.  DOMINANT.

  (2) CODATA m_e precision — 0.510998 MeV ± 1e-9 relative.
      Contribution ≈ 2e-9 × 2.22 MeV ≈ 0.004 eV.  Negligible.

  (3) AME2020 B(D) uncertainty — ±0.00001 MeV = 10 eV.
      Contribution 10 eV.  Non-negligible at 1 ppb.

  (4) SnapPy Vol(6_2) precision — 15+ digits.
      Contribution ≈ 15e-15 × 4.4 × m_e ≈ 3e-14 MeV.  Negligible.

  (5) Missing physical contributions:
      - Electron atomic binding (Rydberg, 13.6 eV): affects M_atomic,
        usually subtracted from AME.  Check convention.
      - Hyperfine splitting (~100 eV scale): already in AME.
      - QED vacuum polarization on nucleon mass: μeV scale.

  (6) Model errors from strategy A:
      - Fixed-shape assumption z_c = shape of 6_2 triangulation.
      - Single-crossing vs JSJ-refined decomposition.

This script computes each contribution and the total, producing a
variance-accounting witness that pinpoints where the 1-ppb gap lives.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0, HBAR_Q, HBAR_Q_SQ

# ── CODATA 2022 (exact where possible) ──────────────────────────
M_E_MEV         = 0.51099895000
M_E_ERR_REL     = 3.0e-10              # CODATA 2022 uncertainty
M_P_MEV         = 938.27208816
M_N_MEV         = 939.56542052
U_MEV           = 931.49410372
DELTA_H_MEV     = M_P_MEV + M_E_MEV - U_MEV   # ¹H mass excess 7.2890
DELTA_N_MEV     = M_N_MEV - U_MEV              # n  mass excess 8.0714

# ── AME2020 (deuterium) ─────────────────────────────────────────
B_D_AME         = 2.22458                  # MeV
B_D_AME_ERR     = 1.0e-5                   # MeV (10 eV)
DELTA_D_AME     = 13.13572                 # MeV mass excess of D
M_D_AME         = 2 * U_MEV + DELTA_D_AME

# ── Strategy-A prediction ───────────────────────────────────────
# Get Vol(6_2) from SnapPy if available, else use pinned value.
try:
    import snappy
    VOL_62 = float(snappy.Manifold("6_2").volume())
    VOL_62_SOURCE = f"SnapPy Manifold('6_2').volume() = {VOL_62:.15f}"
except ImportError:
    VOL_62 = 4.400832516736
    VOL_62_SOURCE = "pinned fallback (SnapPy not available)"

B_D_PRED_STRAT_A  = M_E_MEV * VOL_62
RESIDUAL_MEV      = B_D_PRED_STRAT_A - B_D_AME
RESIDUAL_KEV      = 1e3 * RESIDUAL_MEV

# ── Target volume ───────────────────────────────────────────────
V_TARGET          = B_D_AME / M_E_MEV        # 4.35438...
V_GAP             = VOL_62 - V_TARGET         # ≈ 0.046

# ── Contribution 1: knot-matching mismatch ─────────────────────
C1_MEV = M_E_MEV * V_GAP

# ── Contribution 2: m_e precision ──────────────────────────────
C2_MEV = M_E_ERR_REL * B_D_AME

# ── Contribution 3: AME uncertainty ────────────────────────────
C3_MEV = B_D_AME_ERR

# ── Contribution 4: SnapPy Vol precision (conservative) ────────
C4_MEV = 1e-12 * M_E_MEV

# ── Contribution 5a: electron binding (Rydberg) ────────────────
# Hydrogen atom binding: 13.598 eV; D atom: 13.602 eV.
# AME quotes atomic mass excess, which INCLUDES electron binding.
# So this is already accounted for in the AME value.
RYDBERG_EV_D = 13.602
C5a_MEV = 1e-6 * RYDBERG_EV_D  # for reference; accounted for in AME

# ── Contribution 5b: hyperfine splitting ───────────────────────
# D hyperfine: ~327 MHz ≈ 1.35 μeV.  Accounted for in AME ground-state.
C5b_MEV = 1.35e-12

# ── Contribution 6: model error (crossing-graded first order) ──
# First-order correction under universal depth ξ(q_0) = D(z_q)/ℏ_q².
# At q_0: D(z_q) ≈ 0.9170 (from lambda-descartes-q0 witness),
# ℏ_q² = 0.00982, so ξ ≈ 93.4.
# Linear correction: B = m_GB + c·ξ·m_GB (where c = crossing count = 6).
# But we already fit Vol(6_2) to match B, so this correction is zero
# at zeroth-order *within* strategy A.  The 24 keV IS the model error.
C6_MEV = RESIDUAL_MEV  # by construction

# ── Report ──────────────────────────────────────────────────────

def main() -> int:
    print(f"\n  ²H deep-dive error breakdown — target: 1 ppb on M")
    print(f"  M(²H) observed = {M_D_AME:.6f} MeV;  1 ppb ≈ {M_D_AME * 1e-9 * 1e6:.3f} eV\n")

    print("  ── Strategy-A prediction ─────────────────────────────")
    print(f"    Vol(6_2) = {VOL_62:.12f}   [{VOL_62_SOURCE}]")
    print(f"    m_e      = {M_E_MEV:.11f} MeV  (CODATA 2022, σ_rel ≈ {M_E_ERR_REL:.1e})")
    print(f"    B_pred   = m_e · Vol(6_2) = {B_D_PRED_STRAT_A:.6f} MeV")
    print(f"    B_AME    = {B_D_AME:.6f} MeV  (σ ≈ {B_D_AME_ERR*1e6:.0f} eV)")
    print(f"    ΔB       = {RESIDUAL_MEV:+.6f} MeV  = {RESIDUAL_KEV:+.3f} keV")
    print()

    print("  ── Target volume analysis ────────────────────────────")
    print(f"    Vol(6_2)            = {VOL_62:.9f}")
    print(f"    V_target = B_AME/m_e = {V_TARGET:.9f}")
    print(f"    gap (6_2 − target)   = {V_GAP:+.9f}")
    print(f"    gap / Vol(6_2)       = {V_GAP/VOL_62*100:+.4f}%")
    print()

    contributions = [
        ("(1) Knot match: Vol(6_2)−V_target",   C1_MEV, "dominant — model error"),
        ("(2) CODATA m_e precision",              C2_MEV, "negligible"),
        ("(3) AME B(D) uncertainty",              C3_MEV, "matters at 1 ppb (10 eV)"),
        ("(4) SnapPy Vol(6_2) precision",         C4_MEV, "negligible"),
        ("(5a) e⁻ atomic binding (D Rydberg)",   C5a_MEV, "AME already subtracts"),
        ("(5b) D hyperfine splitting",           C5b_MEV, "AME ground-state value"),
        ("(6) Strategy-A model error (total)",    abs(C6_MEV),
                                                   "same as (1) by construction"),
    ]

    print(f"  ── Contribution breakdown (MeV) ──────────────────────")
    print(f"  {'source':<42} {'value':>14}   note")
    print("  " + "-" * 80)
    total_abs = 0.0
    for label, val, note in contributions:
        if label.startswith("(6)"):  # don't double-count
            continue
        total_abs += abs(val)
        print(f"  {label:<42} {val:>14.6e}   {note}")
    print("  " + "-" * 80)
    print(f"  {'TOTAL (minus (6) model)':<42} {total_abs:>14.6e}")
    print(f"  {'observed residual':<42} {RESIDUAL_MEV:>+14.6e}")
    print()

    print("  ── Target for 1 ppb on M(²H) ────────────────────────")
    target_eV = M_D_AME * 1e-9 * 1e6   # 1 ppb in eV
    target_MeV = target_eV * 1e-6
    print(f"    Required residual: < {target_eV:.3f} eV = {target_MeV:.3e} MeV")
    print(f"    Current residual:  {RESIDUAL_MEV*1e6:,.0f} eV")
    ratio = RESIDUAL_KEV * 1e3 / target_eV
    print(f"    Gap factor: current is {ratio:,.0f}× target precision")
    print()

    print("  ── Paths to 1 ppb ───────────────────────────────────")
    print("    (a) Refined knot: find manifold with Vol = V_target to 1e-6")
    print("        precision.  Census doesn't contain one; need Dehn-filling")
    print("        or hyperbolic mutant generation.")
    print("    (b) Crossing-graded 1st-order correction: B = m_e·V·(1+ξ·η_c)")
    print("        with η_c specific to the 6_2 topology; fit η_c from a")
    print("        second independent observable.")
    print("    (c) First-principles H₃(q) NF: bypass knot-volume ansatz,")
    print("        compute mass endomorphism directly from Hecke algebra")
    print("        and Markov trace at q_0.  Existing machinery in")
    print("        hecke_core.py + hecke_3a_weights.py.")

    witness = {
        "name": "h2-error-breakdown",
        "description": (
            "²H (deuterium) error source breakdown.  Identifies the "
            "dominant contribution (knot-matching mismatch, ~24 keV) "
            "and quantifies the gap between current ~13 ppm precision "
            "and the 1 ppb target (~1.88 eV residual on M(²H))."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "constants": {
            "q_0": Q0,
            "M_E_MEV": M_E_MEV,
            "M_E_ERR_REL": M_E_ERR_REL,
            "U_MEV": U_MEV,
            "DELTA_H_MEV": DELTA_H_MEV,
            "DELTA_N_MEV": DELTA_N_MEV,
            "B_D_AME": B_D_AME,
            "B_D_AME_ERR": B_D_AME_ERR,
            "DELTA_D_AME": DELTA_D_AME,
            "M_D_AME": M_D_AME,
            "VOL_62": VOL_62,
            "VOL_62_SOURCE": VOL_62_SOURCE,
        },
        "prediction": {
            "strategy_A_B_pred": B_D_PRED_STRAT_A,
            "residual_MeV": RESIDUAL_MEV,
            "residual_keV": RESIDUAL_KEV,
            "residual_ppm_of_M": 1e6 * RESIDUAL_MEV / M_D_AME,
            "target_volume_B_AME_over_m_e": V_TARGET,
            "volume_gap_vs_6_2": V_GAP,
            "gap_pct_of_vol_62": V_GAP / VOL_62 * 100,
        },
        "contributions_MeV": {
            "C1_knot_match":          C1_MEV,
            "C2_m_e_precision":       C2_MEV,
            "C3_AME_uncertainty":     C3_MEV,
            "C4_Vol_62_precision":    C4_MEV,
            "C5a_electron_binding":   C5a_MEV,
            "C5b_hyperfine":          C5b_MEV,
        },
        "note_on_model_error": (
            "The observed residual (field `prediction.residual_MeV`) "
            "equals contribution C1 by construction — the knot-match "
            "mismatch IS the leading-order model error.  An explicit "
            "C6 is not emitted to avoid redundancy."
        ),
        "target_1ppb_on_M_eV": target_eV,
        "current_gap_vs_1ppb_factor": RESIDUAL_KEV * 1e3 / target_eV,
        "paths_to_1ppb": [
            "(a) Refined knot Dehn-filling / mutant at Vol = V_target",
            "(b) Crossing-graded 1st-order correction with η_c fit",
            "(c) First-principles H_3(q) Markov trace from Hecke machinery",
        ],
    }
    out = Path(__file__).parent / "h2-error-breakdown.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"\n  Wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
