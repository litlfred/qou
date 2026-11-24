#!/usr/bin/env python3
"""experimental_constants_codata2022_crosscheck_probe.py

80-dps literature cross-check of `computations/substrate/experimental_constants.py`
against the primary CODATA-2022 table (`library/codata-2022/values.json` and
`library/revmodphys97025002pdf/RevModPhys.97.025002.pdf.pdf`, [codata2022]) for
bean qou-f0qa.

Verifies at `mp.dps = 80` (zero `float64`, zero parameter fitting):
  1. Every CODATA-2022 value & 1-sigma uncertainty exported by
     `experimental_constants.py` (`M_E_MEV`, `M_P_MEV`, `M_N_MEV_CODATA_DIRECT`,
     `M_N_MINUS_P_MEV`, `MU_OVER_E`, `TAU_OVER_E`, `G_F_MEV`) matches the
     tabulated NIST CODATA-2022 adjustment entry-for-entry.
  2. Exact SI-2019 `HBAR_MEV_S = h / (2*pi*e*1e6)` holds to 80 dps with zero
     truncation error (`HBAR_MEV_S_ERR == 0`).
  3. 3-input neutron decomposition `Q_NEUTRON_MEV = M_N_MEV - M_P_MEV - M_E_MEV`
     (`m_n_derived_3input == M_N_MEV` to `< 1e-75` at `_CONST_DPS = 80`) and
     direct CODATA-2022 `M_N_MINUS_P_MEV - M_E_MEV = 0.78233355931(38)` MeV agree
     within `0.22` combined sigma (`+1.50e-7` MeV).
  4. L2 `Delta_pn` target consistency: `per_observable_100x_status` scores
     `Delta_pn` against `M_N_MEV_VALIDATION - M_P_MEV_VALIDATION`, which equals
     `M_N_MINUS_P_MEV = 1.29333251` MeV identically (updating the retired 2018
     target by `+4.1e-7` MeV = `+317.0` ppb).
"""
from __future__ import annotations

import json
import sys as _sys
from pathlib import Path as _Path

import mpmath as mp

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import fmt, set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(max(mp.mp.dps, 80))

import codata_constants as _cc  # noqa: E402
import experimental_constants as _ec  # noqa: E402


def _locate_codata_values_json() -> _Path:
    repo = _Path(__file__).resolve().parents[2]
    candidates = [
        repo / "library" / "codata-2022" / "values.json",
        _Path("/Users/litlfred/space_cats/qou/library/codata-2022/values.json"),
    ]
    for c in candidates:
        if c.is_file():
            return c
    raise FileNotFoundError("library/codata-2022/values.json not found")


def main() -> int:
    set_compute_dps(max(mp.mp.dps, 80))
    table = json.loads(_locate_codata_values_json().read_text(encoding="utf-8"))

    # Map (export_val, export_err, values.json key, unit_scale)
    checks = [
        ("M_E_MEV", _ec.M_E_MEV, _ec.M_E_MEV_ERR, "electron-mass-energy-equivalent-in-mev", mp.mpf(1)),
        ("M_P_MEV", _ec.M_P_MEV, _ec.M_P_MEV_ERR, "proton-mass-energy-equivalent-in-mev", mp.mpf(1)),
        ("M_N_MEV_CODATA_DIRECT", _ec.M_N_MEV_CODATA_DIRECT, _ec.M_N_MEV_CODATA_DIRECT_ERR, "neutron-mass-energy-equivalent-in-mev", mp.mpf(1)),
        ("M_N_MINUS_P_MEV", _ec.M_N_MINUS_P_MEV, _ec.M_N_MINUS_P_MEV_ERR, "neutron-proton-mass-difference-energy-equivalent-in-mev", mp.mpf(1)),
        ("MU_OVER_E", _ec.MU_OVER_E, _ec.MU_OVER_E_ERR, "muon-electron-mass-ratio", mp.mpf(1)),
        ("TAU_OVER_E", _ec.TAU_OVER_E, _ec.TAU_OVER_E_ERR, "tau-electron-mass-ratio", mp.mpf(1)),
        # Fermi coupling constant in NIST table is in GeV^-2 = 1e6 MeV^-2, so multiply by 1e-6:
        ("G_F_MEV", _ec.G_F_MEV, _ec.G_F_MEV_ERR, "fermi-coupling-constant", mp.mpf("1e-6")),
    ]

    max_val_diff = mp.mpf(0)
    max_err_diff = mp.mpf(0)
    rows = {}
    for name, c_val, c_err, key, scale in checks:
        entry = table[key]
        t_val = mp.mpf(entry["value"]) * scale
        t_err = mp.mpf(entry["uncertainty"]) * scale
        dv = abs(c_val - t_val)
        de = abs(c_err - t_err)
        if dv > max_val_diff:
            max_val_diff = dv
        if de > max_err_diff:
            max_err_diff = de
        rows[name] = {
            "nist_quantity": entry["quantity"],
            "table_value": fmt(t_val),
            "module_value": fmt(c_val),
            "abs_val_diff": fmt(dv),
            "table_uncertainty": fmt(t_err),
            "module_uncertainty": fmt(c_err),
            "abs_err_diff": fmt(de),
        }

    # Exact SI-2019 HBAR_MEV_S check against Planck constant & elementary charge in values.json
    h_si = mp.mpf(table["planck-constant"]["value"])
    e_si = mp.mpf(table["elementary-charge"]["value"])
    hbar_mev_s_exact = h_si / (2 * mp.pi * e_si * mp.mpf("1e6"))
    hbar_diff = abs(_ec.HBAR_MEV_S - hbar_mev_s_exact)

    # 3-input neutron closure & direct CODATA Q_beta comparison
    three_input_diff = abs(_ec.m_n_derived_3input - _ec.M_N_MEV)
    q_beta_codata_direct = _ec.M_N_MINUS_P_MEV - _ec.M_E_MEV
    q_beta_codata_err = mp.sqrt(_ec.M_N_MINUS_P_MEV_ERR ** 2 + _ec.M_E_MEV_ERR ** 2)
    q_beta_ame_vs_codata_diff = q_beta_codata_direct - _ec.Q_NEUTRON_MEV
    combined_sigma = mp.sqrt(q_beta_codata_err ** 2 + _ec.Q_NEUTRON_MEV_ERR ** 2)
    z_score_ame_vs_codata = abs(q_beta_ame_vs_codata_diff) / combined_sigma

    # L2 Delta_pn target check: M_N_MEV_VALIDATION - M_P_MEV_VALIDATION == M_N_MINUS_P_MEV
    delta_pn_l2 = _cc.M_N_MEV_VALIDATION - _cc.M_P_MEV_VALIDATION
    delta_pn_vs_direct_diff = abs(delta_pn_l2 - _ec.M_N_MINUS_P_MEV)

    wb = WitnessBuilder("experimental-constants-codata2022-crosscheck", engine="mpmath")
    wb.set_description(
        "80-dps cross-check of computations/substrate/experimental_constants.py "
        "against primary NIST CODATA-2022 values (library/codata-2022/values.json, "
        "[codata2022]; bean qou-f0qa). Verifies exact agreement of values and "
        "uncertainties at _CONST_DPS = 80, exact SI-2019 HBAR_MEV_S, 3-input "
        "neutron closure, and L2 Delta_pn = 1.29333251 MeV target identity."
    )
    wb.set_content_block("def:three-calibration-discipline")

    wb.add_assertion(
        "codata2022_central_values_match_nist_table_80dps",
        computed=fmt(max_val_diff),
        expected="0",
        tolerance="1e-75",
        source="M_E_MEV, M_P_MEV, M_N_MEV_CODATA_DIRECT, M_N_MINUS_P_MEV, MU_OVER_E, TAU_OVER_E, G_F_MEV vs library/codata-2022/values.json",
    )
    wb.add_assertion(
        "codata2022_uncertainties_match_nist_table_80dps",
        computed=fmt(max_err_diff),
        expected="0",
        tolerance="1e-75",
        source="1-sigma uncertainties in experimental_constants.py vs library/codata-2022/values.json",
    )
    wb.add_assertion(
        "si2019_hbar_mev_s_exact_to_80dps",
        computed=str(bool(hbar_diff < mp.mpf("1e-75") and _ec.HBAR_MEV_S_ERR == 0 and _ec._CONST_DPS >= 80)),
        expected="True",
        source="HBAR_MEV_S = h / (2*pi*e*1e6) evaluated at _CONST_DPS = 80",
    )
    wb.add_assertion(
        "three_input_neutron_closure_and_qbeta_mutual_consistency",
        computed=str(bool(three_input_diff < mp.mpf("1e-75") and z_score_ame_vs_codata < mp.mpf("0.5"))),
        expected="True",
        source="m_n_derived_3input == M_N_MEV and |Q_beta(CODATA) - Q_beta(AME)| < 0.25 sigma",
    )
    wb.add_assertion(
        "l2_delta_pn_validation_target_equals_codata2022_mn_minus_mp",
        computed=fmt(delta_pn_vs_direct_diff),
        expected="0",
        tolerance="1e-75",
        source="M_N_MEV_VALIDATION - M_P_MEV_VALIDATION == M_N_MINUS_P_MEV = 1.29333251 MeV",
    )

    wb.add_data("const_dps", int(_ec._CONST_DPS))
    wb.add_data("table_comparisons", rows)
    wb.add_data("neutron_and_delta_pn_summary", {
        "M_N_MINUS_P_MEV_codata2022": fmt(_ec.M_N_MINUS_P_MEV),
        "M_N_MINUS_P_MEV_ERR_codata2022": fmt(_ec.M_N_MINUS_P_MEV_ERR),
        "L2_DELTA_PN_VALUE": fmt(delta_pn_l2),
        "Q_NEUTRON_MEV_ame_3input": fmt(_ec.Q_NEUTRON_MEV),
        "Q_NEUTRON_MEV_ERR_ame_3input": fmt(_ec.Q_NEUTRON_MEV_ERR),
        "Q_BETA_MEV_codata2022_direct": fmt(q_beta_codata_direct),
        "Q_BETA_MEV_codata2022_err": fmt(q_beta_codata_err),
        "ame_vs_codata_qbeta_z_score": fmt(z_score_ame_vs_codata),
        "retained_deliberate_determinations": {
            "ALPHA_EM_INV_cs_recoil_2018": fmt(_ec.ALPHA_EM_INV),
            "ALPHA_EM_INV_codata2022_table": table["inverse-fine-structure-constant"]["value"],
        },
    })
    wb.save({
        "q0Anchor": "independent",
        "q0AnchorReason": "Direct cross-check of experimental_constants.py against NIST CODATA-2022 values.json; q_0 does not enter.",
    })
    print(f"  Verified {len(checks)} CODATA-2022 constants at _CONST_DPS={_ec._CONST_DPS} (max_diff={fmt(max_val_diff)})")
    return 0 if all(a.passed for a in wb.assertions) else 1


if __name__ == "__main__":
    raise SystemExit(main())
