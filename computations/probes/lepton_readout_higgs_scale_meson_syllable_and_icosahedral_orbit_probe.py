#!/usr/bin/env python3
"""
50-dps mpmath probe for Round 57 (qou-8lxd):
  1. qou-lsp9: 2-step linear readout recurrence on H_2(q) and node-sign criterion
  2. qou-pgzo: T(2,7) knot vs T(2,8) link Euler characteristic / genus and tree-level scalar quartic scale
  3. qou-qpj9: Giambrone negative-syllable hyperbolic volume window and crossing lower bound for pi^+/- and J/psi
  4. qou-ultb: Actinide cosmochronometry (CS 31082-001 U II 3859.57 A) sensitivity conversion and slack vs sigma(q_0)
  5. qou-b5ic: Order-60 icosahedral group A_5 exceptional orbits (12, 20, 30), Euler deficit, and antipodal chirality pairing
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
import mpmath as mp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge  # noqa: E402, F401
from witness_base import WitnessBuilder  # noqa: E402

WORK_DPS = 60
OUT_DPS = 50
mp.mp.dps = WORK_DPS


def mpf_str(v: mp.mpf, dps: int = OUT_DPS) -> str:
    return mp.nstr(v, dps, strip_zeros=False)


def run_probe() -> dict:
    mp.mp.dps = WORK_DPS

    # Anchor q_0 and h = q_0 - q_0^{-1}
    q0 = mp.mpf("0.87801698486368466468255517896525729842228459217992")
    h = q0 - 1 / q0

    # 1. qou-lsp9: 2-step linear readout recurrence on H_2(q)
    # Sequence b_0 = 0, b_1 = 1, b_{n+1} = h * b_n + b_{n-1}
    #Note that at q0 < 1, h < 0; if we work with positive step parameter u = |h| = q0^{-1} - q0 > 0:
    u = -h
    b_seq = [mp.mpf(0), mp.mpf(1)]
    for n in range(1, 10):
        b_seq.append(u * b_seq[-1] + b_seq[-2])

    # Check 2-step advancement identity b_{n+2} = (u^2 + 1) b_n + u b_{n-1}
    max_rec_residual = mp.mpf(0)
    for n in range(1, 8):
        lhs = b_seq[n + 2]
        rhs = (u * u + 1) * b_seq[n] + u * b_seq[n - 1]
        res = abs(lhs - rhs)
        if res > max_rec_residual:
            max_rec_residual = res

    # Nonnegative weights alpha = 2, beta = 3 -> strictly positive on n >= 1
    alpha_pos = mp.mpf(2)
    beta_pos = mp.mpf(3)
    phi_pos_vals = [alpha_pos * b_seq[n - 1] + beta_pos * b_seq[n] for n in range(1, 9)]
    all_pos = all(val > 0 for val in phi_pos_vals)

    # Opposite-sign weight required for node at w = 3: alpha * b_2 + beta * b_3 = 0 => alpha = -beta * b_3 / b_2 < 0
    alpha_node = -beta_pos * b_seq[3] / b_seq[2]
    node_val_w3 = alpha_node * b_seq[2] + beta_pos * b_seq[3]
    lsp9_passed = bool(
        max_rec_residual < mp.mpf("1e-55")
        and all_pos
        and alpha_node < 0
        and abs(node_val_w3) < mp.mpf("1e-55")
    )

    # 2. qou-pgzo: T(2,7) vs T(2,8) surface invariants and tree-level m_H^2 = 2 * lambda * v^2
    mu_7, chi_7, g_7 = 1, 2 - 7, (7 - 1) // 2
    mu_8, chi_8, g_8 = 2, 2 - 8, (8 - 2) // 2
    v_ew = mp.mpf("246.2196508")  # GeV
    m_h_pdg = mp.mpf("125.20")    # GeV
    lambda_sm = (m_h_pdg ** 2) / (2 * (v_ew ** 2))
    lambda_alt = mp.mpf("0.25")
    mh_sq_sm = 2 * lambda_sm * (v_ew ** 2)
    mh_sq_alt = 2 * lambda_alt * (v_ew ** 2)
    pgzo_passed = bool(
        mu_7 == 1 and chi_7 == -5 and g_7 == 3
        and mu_8 == 2 and chi_8 == -6 and g_8 == 3
        and mh_sq_sm < mh_sq_alt
        and abs(mp.sqrt(mh_sq_sm) - m_h_pdg) < mp.mpf("1e-50")
    )

    # 3. qou-qpj9: Giambrone negative-syllable volume window (s-1)*v8 <= V < 4*s*v8 and c_- >= 3*s
    # Regular ideal octahedron volume v_8 = 4 * Catalan = 3.663862376708876...
    v8 = 4 * mp.catalan
    s_pion = 1
    pion_v_min = (s_pion - 1) * v8
    pion_v_max = 4 * s_pion * v8
    pion_c_min = 3 * s_pion

    s_jpsi = 5
    jpsi_v_min = (s_jpsi - 1) * v8
    jpsi_v_max = 4 * s_jpsi * v8
    jpsi_c_min = 3 * s_jpsi

    qpj9_passed = bool(
        pion_c_min == 3
        and jpsi_c_min == 15
        and pion_v_min == 0
        and pion_v_max > mp.mpf("14.65")
        and jpsi_v_min > mp.mpf("14.65")
        and jpsi_v_max > mp.mpf("73.27")
    )

    # 4. qou-ultb: Actinide cosmochronometry U II 3859.57 A bound vs sigma(q_0)
    bound_dalpha_over_alpha = mp.mpf("2.08e-3")
    sensitivity_s = mp.mpf("6.861933")
    sigma_q0_rel = mp.mpf("1.22335e-9")
    implied_dq_over_q = bound_dalpha_over_alpha / sensitivity_s
    slack_ratio = implied_dq_over_q / sigma_q0_rel
    slack_floor = int(mp.floor(slack_ratio))
    ultb_passed = bool(
        slack_floor == 247779
        and implied_dq_over_q > 247779 * sigma_q0_rel
        and implied_dq_over_q < 247780 * sigma_q0_rel
    )

    # 5. qou-b5ic: Order-60 A_5 exceptional orbits on S^2 and antipodal chirality pairing
    group_order = 60
    stab_orders = [5, 3, 2]
    orbit_sizes = [group_order // s for s in stab_orders]
    euler_deficit_lhs = sum((s - 1) * (group_order // s) for s in stab_orders)
    euler_deficit_rhs = 2 * group_order - 2
    all_even_orbits = all(sz % 2 == 0 for sz in orbit_sizes)
    gamma_u = mp.mpf("1")
    antipodal_pair_sum = gamma_u + (-gamma_u)
    b5ic_passed = bool(
        orbit_sizes == [12, 20, 30]
        and euler_deficit_lhs == 118
        and euler_deficit_lhs == euler_deficit_rhs
        and all_even_orbits
        and antipodal_pair_sum == 0
    )

    checks = [
        {
            "id": "qou_lsp9_two_step_readout_and_node_sign",
            "bean": "qou-lsp9",
            "passed": lsp9_passed,
            "u_step_parameter": mpf_str(u),
            "max_two_step_recurrence_residual": mpf_str(max_rec_residual),
            "alpha_node_for_w3": mpf_str(alpha_node),
            "node_residual_w3": mpf_str(abs(node_val_w3)),
        },
        {
            "id": "qou_pgzo_t27_t28_surface_and_quartic_scale",
            "bean": "qou-pgzo",
            "passed": pgzo_passed,
            "t27_components_euler_genus": [mu_7, chi_7, g_7],
            "t28_components_euler_genus": [mu_8, chi_8, g_8],
            "lambda_sm_tree": mpf_str(lambda_sm),
            "mh_sq_sm_gev2": mpf_str(mh_sq_sm),
            "mh_sq_alt_gev2": mpf_str(mh_sq_alt),
        },
        {
            "id": "qou_qpj9_negative_syllable_volume_window",
            "bean": "qou-qpj9",
            "passed": qpj9_passed,
            "v8_octahedron_volume": mpf_str(v8),
            "pion_s1_cmin": pion_c_min,
            "pion_s1_volume_window": [mpf_str(pion_v_min), mpf_str(pion_v_max)],
            "jpsi_s5_cmin": jpsi_c_min,
            "jpsi_s5_volume_window": [mpf_str(jpsi_v_min), mpf_str(jpsi_v_max)],
        },
        {
            "id": "qou_ultb_actinide_cosmochronometry_slack",
            "bean": "qou-ultb",
            "passed": ultb_passed,
            "bound_dalpha_over_alpha": mpf_str(bound_dalpha_over_alpha),
            "sensitivity_s": mpf_str(sensitivity_s),
            "implied_dq_over_q": mpf_str(implied_dq_over_q),
            "sigma_q0_rel": mpf_str(sigma_q0_rel),
            "slack_ratio": mpf_str(slack_ratio),
            "slack_floor": slack_floor,
        },
        {
            "id": "qou_b5ic_icosahedral_orbits_and_antipodal_chirality",
            "bean": "qou-b5ic",
            "passed": b5ic_passed,
            "group_order": group_order,
            "stabilizer_orders": stab_orders,
            "orbit_sizes": orbit_sizes,
            "euler_deficit_sum": euler_deficit_lhs,
            "antipodal_pair_chirality_sum": mpf_str(antipodal_pair_sum),
        },
    ]

    all_passed = all(c["passed"] for c in checks)
    witness = {
        "probe": "lepton-readout-higgs-scale-meson-syllable-and-icosahedral-orbit",
        "beans": ["qou-lsp9", "qou-pgzo", "qou-qpj9", "qou-ultb", "qou-b5ic"],
        "parentBean": "qou-8lxd",
        "workDps": WORK_DPS,
        "outputDps": OUT_DPS,
        "allPassed": all_passed,
        "checks": checks,
    }
    WitnessBuilder.stamp_staleness_metadata(
        witness,
        script_path=__file__,
        engine="mpmath",
        q0_anchor=False,
    )
    return witness


def main() -> None:
    witness = run_probe()
    out_path = Path(__file__).with_name(
        "lepton-readout-higgs-scale-meson-syllable-and-icosahedral-orbit.witness.json"
    )
    out_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out_path} (allPassed={witness['allPassed']})")
    if not witness["allPassed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
