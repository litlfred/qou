#!/usr/bin/env python3
"""
coulomb_measured_radius_comparison_probe.py — bean qou-usft, COMPARISON ARM (owner pick
"Both", 2026-11-27, thread "Derive the Coulomb shape factor from q-Bessel").

Question: in E_C = f · Z(Z−1) · α_EM ħc / r_rms, is the A = 3 Coulomb miss in the SHAPE f or
in the LENGTH r_rms?

Method: hold every model input fixed (f from the q-Hankel probe, α_EM derived from q₀) and
swap ONLY r_rms between
  * the model radius  r_rms = √(3/5)·λ̄_π·A^{1/3}   (coulomb_energy.py, CAL-3, conditional), and
  * the MEASURED rms charge radius of ³He / ⁴He     (Angeli–Marinova 2013).

THIS IS A COMPARISON, NOT A MODEL INPUT. The measured radius never enters coulomb_energy.py
or any production path. It isolates where the miss sits. The derived radius waits on the
energy-to-length map's open factor ε (thread "Derive the electron's categorical weight");
back-solving r_rms from the ³He−³H split would be a fit and is reported only as a number.

Caveat on the target: ΔB_AME(³H − ³He) = 0.7638 MeV contains strong charge-symmetry breaking
(Nolen–Schiffer; published A = 3 shortfall ≈ 0.06–0.08 MeV), so pure Coulomb should land
somewhat BELOW it. Agreement at the 0.3 % level is therefore not a claim of exactness.

Reference: [angeli-marinova2013] https://doi.org/10.1016/j.adt.2011.12.006
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parent))

import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from codata_constants import _ame_binding_mev  # noqa: E402
import coulomb_energy as ce  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
except ImportError:  # pragma: no cover
    WitnessBuilder = None

# Angeli & Marinova, ADNDT 99 (2013) 69, Table: rms charge radii (fm). Comparison only.
MEASURED_RMS_FM = {
    (2, 3): ("1.9661", "0.0030"),   # ³He
    (2, 4): ("1.6755", "0.0028"),   # ⁴He
}


def main() -> int:
    set_compute_dps(60)
    a_hc = ce.alpha_em_hbar_c_mev_fm()
    f_der = ce.shape_factor(3, "qhankel")
    f_ball = ce.shape_factor(3, "uniform_ball")
    split = mp.mpf(str(_ame_binding_mev(1, 3))) - mp.mpf(str(_ame_binding_mev(2, 3)))

    rows = {}
    for (Z, A), (r_s, dr_s) in MEASURED_RMS_FM.items():
        r_meas, dr = mp.mpf(r_s), mp.mpf(dr_s)
        r_model = mp.sqrt(mp.mpf(3) / 5) * ce.nuclear_radius_fm(A)
        q2 = Z * (Z - 1)
        rows[f"Z{Z}_A{A}"] = {
            "r_rms_measured_fm": r_s,
            "r_rms_measured_err_fm": dr_s,
            "r_rms_model_fm": mp.nstr(r_model, 20),
            "r_model_over_measured_minus_1": mp.nstr(r_model / r_meas - 1, 12),
            "E_C_derived_f_model_r_MeV": mp.nstr(f_der * q2 * a_hc / r_model, 20),
            "E_C_derived_f_measured_r_MeV": mp.nstr(f_der * q2 * a_hc / r_meas, 20),
            "E_C_ball_measured_r_MeV": mp.nstr(f_ball * q2 * a_hc / r_meas, 20),
            "E_C_derived_f_measured_r_err_MeV": mp.nstr(f_der * q2 * a_hc * dr / r_meas ** 2, 6),
        }

    he3 = rows["Z2_A3"]
    e_meas = mp.mpf(he3["E_C_derived_f_measured_r_MeV"])
    e_model = mp.mpf(he3["E_C_derived_f_model_r_MeV"])
    e_ball = mp.mpf(he3["E_C_ball_measured_r_MeV"])
    rel_meas = e_meas / split - 1
    rel_model = e_model / split - 1
    rel_ball = e_ball / split - 1
    r_implied = f_der * 2 * a_hc / split   # back-solved: a NUMBER, not an input

    print("³He−³H split (AME2020)      ", mp.nstr(split, 10), "MeV")
    print("derived f, model radius     ", mp.nstr(e_model, 10), f"({float(rel_model)*100:+.2f} %)")
    print("derived f, measured radius  ", mp.nstr(e_meas, 10), f"({float(rel_meas)*100:+.2f} %)")
    print("ball 3/5,  measured radius  ", mp.nstr(e_ball, 10), f"({float(rel_ball)*100:+.2f} %)")
    print("r_rms implied by the split  ", mp.nstr(r_implied, 10), "fm  (comparison only, not a fit input)")

    if WitnessBuilder is not None:
        wb = WitnessBuilder("coulomb-measured-radius-comparison-probe", engine="mpmath")
        wb.set_description(
            "COMPARISON ARM (bean qou-usft): E_C at A=3,4 with the derived q-Hankel shape "
            "factor and alpha_EM from q0, swapping only r_rms between the CAL-3 model radius "
            "and the measured charge radius (Angeli-Marinova 2013). Localises the A=3 Coulomb "
            "miss in the length, not the shape. Measured radii are never a model input."
        )
        for k, v in {
            "split_AME_3H_minus_3He_MeV": mp.nstr(split, 20),
            "f_derived": mp.nstr(f_der, 30),
            "f_uniform_ball": mp.nstr(f_ball, 30),
            "alpha_hbar_c_MeV_fm": mp.nstr(a_hc, 30),
            "rows": rows,
            "rel_to_split": {
                "derived_f_model_r": mp.nstr(rel_model, 12),
                "derived_f_measured_r": mp.nstr(rel_meas, 12),
                "ball_measured_r": mp.nstr(rel_ball, 12),
            },
            "r_rms_implied_by_split_fm_NOT_AN_INPUT": mp.nstr(r_implied, 20),
        }.items():
            wb.add_data(k, v)
        wb.add_assertion(
            name="shape_not_length_is_right_at_A3",
            computed=str(int(abs(rel_meas) < mp.mpf("0.02") and abs(rel_model) > mp.mpf("0.15"))),
            expected="1", tolerance=0,
            source="With the measured 3He radius the derived f lands within 2 % of the split "
                   f"({float(rel_meas)*100:+.2f} %), while the model radius misses by "
                   f"{float(rel_model)*100:+.2f} %: the miss is the length.")
        wb.add_assertion(
            name="derived_f_beats_ball_at_measured_radius",
            computed=str(int(abs(rel_meas) < abs(rel_ball))), expected="1", tolerance=0,
            source=f"At the measured radius: derived f {float(rel_meas)*100:+.2f} % vs uniform "
                   f"ball {float(rel_ball)*100:+.2f} %.")
        print(f"witness: {wb.save()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
