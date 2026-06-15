#!/usr/bin/env python3
"""
ISOSPIN COLLAPSE OF MASS-TOWER RATIOS

Tests whether the T vs 3He gap in the mass-tower ratios from
tr-m-plus-tower-and-log.witness.json is the well-known Coulomb
correction (isospin symmetry).

Mirror nuclei T (1p,2n) and 3He (2p,1n) should have identical
strong-force binding under isospin symmetry; their AME values differ
by ~0.76 MeV due to Coulomb repulsion of the extra pp pair in 3He.
Removing this Coulomb energy from B(3He) should make the T and 3He
ratios coincide.

See content block: rem:commutative-crossing-energy.

Usage:
    python3 folio-assistant/computations/isospin_mass_tower_collapse.py
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import math
import sys
from pathlib import Path
from mpmath import mp

sys.path.insert(0, str(Path(__file__).parent))

from witness_base import WitnessBuilder
# CAL-1: m_e sourced from codata_constants registry (P31-triage Phase A);
# coerced to float for json-serialisable arithmetic in this script.
from codata_constants import M_E_MEV as _M_E_MEV_MP

# ── Constants ──────────────────────────────────────────────────
# Knot volumes from canonical knot_volumes module (mpmath 50dps).
# See PR #781 knot-vol propagation.
from knot_volumes import CATALAN_G, VOL_BORROMEAN  # noqa: E402
M_E_MEV = float(_M_E_MEV_MP)
ALPHA_MEV = M_E_MEV * VOL_BORROMEAN  # 3.74445965488548 MeV

# Coulomb energy of 3He ground state (well-known empirical value)
E_COULOMB_3HE_MEV = 0.76


def main() -> None:
    # ── Inputs from tr-m-plus-tower-and-log.witness.json ──────────
    # m_cat_total values (already include |tr_M| + tower):
    m_cat = {"D": 1.813186209713881, "T": 7.874495793321092,
             "3He": 7.872184876047902}
    # AME binding energies (MeV):
    B_AME = {"D": 2.22456612, "T": 8.4817984, "3He": 7.7180375}

    # ── Raw ratios = alpha * m_cat / B_AME ────────────────────────
    raw = {atom: ALPHA_MEV * m_cat[atom] / B_AME[atom]
            for atom in ("D", "T", "3He")}

    # ── Coulomb-corrected 3He ratio ──────────────────────────────
    B_3He_strong = B_AME["3He"] + E_COULOMB_3HE_MEV
    corrected_3He = ALPHA_MEV * m_cat["3He"] / B_3He_strong

    isospin = {
        "D":              raw["D"],
        "T":              raw["T"],
        "3He_corrected":  corrected_3He,
        "T_minus_3He_corr_pct":
            abs(raw["T"] - corrected_3He) / raw["T"] * 100,
    }

    # ── Branch-phase predictions ──────────────────────────────────
    sin72 = 2 * abs(mp.sin(2 * mp.pi / 5))
    sin144 = 2 * abs(mp.sin(4 * mp.pi / 5))
    phi = (1 + mp.sqrt(5)) / 2

    D_pred_value = sin72 + sin144           # 2|sin72| + 2|sin144|
    T_3He_pred_value = 3 * sin144           # 3 * 2|sin144|
    A3_value = (raw["T"] + corrected_3He) / 2

    branch_phase = {
        "sin72_2x": float(sin72),
        "sin144_2x": float(sin144),
        "sin72_over_sin144": float(sin72 / sin144),
        "phi": float(phi),
        "D_pred": {
            "formula": "2|sin72| + 2|sin144|",
            "value":   float(D_pred_value),
            "obs":     raw["D"],
            "err_pct": float((D_pred_value - raw["D"]) / raw["D"] * 100),
        },
        "T_3He_pred": {
            "formula": "3 * 2|sin144|",
            "value":   float(T_3He_pred_value),
            "obs":     A3_value,
            "err_pct": float((T_3He_pred_value - A3_value) / A3_value * 100),
        },
    }

    # ── Witness ────────────────────────────────────────────────────
    w = WitnessBuilder("isospin-mass-tower-collapse", engine="python")
    w.set_description(
        "Tests whether the T vs 3He gap in the mass-tower ratios is "
        "the Coulomb correction (isospin symmetry). Mirror nuclei T "
        "(1p,2n) and 3He (2p,1n) should have identical strong-force "
        "binding; their AME values differ by ~0.76 MeV due to Coulomb "
        "repulsion of the extra pp pair in 3He. Removing this from "
        "B(3He) should make T and 3He ratios coincide."
    )
    w.set_content_block("rem:commutative-crossing-energy")
    w.add_parameter("alpha_MeV", ALPHA_MEV)
    w.add_parameter("E_coulomb_3He_MeV", E_COULOMB_3HE_MEV)
    w.add_parameter("note",
                     "Coulomb energy of 3He ground state ≈ 0.76 MeV "
                     "(well-known).")
    w.add_data("raw_ratios", raw)
    w.add_data("isospin_corrected", isospin)
    w.add_data("branch_phase_predictions", branch_phase)
    w.add_data("structural_reading",
                "Two distinct branch-phase magnitudes 2|sin(2*pi*k/5)|: "
                "outer (k=1,4) = phi*inner (k=2,3). D (A=2) sums one of "
                "each; A=3 nuclei (T and Coulomb-corrected 3He) match 3 "
                "copies of the inner phase, suggesting the per-nucleon "
                "scaling pulls in the inner phase only. Both fits at "
                "<1.5% level, with the A=3 fit improving once Coulomb "
                "is removed.")
    w.add_caveat(
        "Per-nucleon scaling A=2 -> A=3 not derived from first "
        "principles. Match at <1.5% level is suggestive, not a "
        "derivation."
    )

    # Assertion: T and Coulomb-corrected 3He coincide under isospin
    w.add_assertion(
        name="T_eq_3He_corrected_under_isospin",
        computed=corrected_3He,
        expected=raw["T"],
        tolerance=0.01,   # 1% — observed match is 0.014%
        unit="dimensionless ratio",
        source="approach_1_multi_brane (tr-m-plus-tower-and-log) "
               "+ standard Coulomb energy of 3He (Wigner-energy "
               "convention, satula1997)",
    )

    out = w.save()
    print(f"Witness: {out}")
    print(f"\nIsospin collapse:")
    print(f"  T raw ratio:           {raw['T']:.4f}")
    print(f"  3He raw ratio:         {raw['3He']:.4f}")
    print(f"  3He Coulomb-corrected: {corrected_3He:.4f}")
    print(f"  T vs 3He_corr diff:    "
           f"{isospin['T_minus_3He_corr_pct']:.4f}%")
    print(f"\nBranch-phase fits:")
    print(f"  D   (A=2):           obs={raw['D']:.4f}  "
           f"pred={float(D_pred_value):.4f}  "
           f"err={branch_phase['D_pred']['err_pct']:+.2f}%")
    print(f"  T=3He_corr (A=3):    obs={A3_value:.4f}  "
           f"pred={float(T_3He_pred_value):.4f}  "
           f"err={branch_phase['T_3He_pred']['err_pct']:+.2f}%")


if __name__ == "__main__":
    main()
