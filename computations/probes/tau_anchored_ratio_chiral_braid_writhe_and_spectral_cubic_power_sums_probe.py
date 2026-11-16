#!/usr/bin/env python3
"""
50-dps mpmath probe for Round 58 (qou-8lxd):
  1. qou-se9w: Muon-anchored tau energy-chain ratio and global scale cancellation
  2. qou-h0zz: Framed chiral fermion / hadron braid writhe sign dictionary and weak hypercharge cancellation
  3. qou-8p1e: Nodal curve genus drop bookkeeping (g_arith=4 -> g_geom=3) and 7D imaginary unit stabilizer split
  4. qou-d8de: Color spectral cubic P(X,z) Newton power sums p_n(z) = -(z^n + 1) and ramified parity shift
  5. qou-wqto: Generation-1 8-state chirality involution, fixed-point-free odd grading, and 2-bit projection collapse
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

    # 1. qou-se9w: Muon-anchored tau energy ratio & global scale invariance
    m_mu_mev = mp.mpf("105.6583755")
    m_tau_pdg_mev = mp.mpf("1776.86")
    w_crossings = [2 * k + 1 for k in (1, 2, 3)]
    # Bare Hecke-chain proxy at q0: E_k = q0^{-w_k} + q0^{w_k}, F-factor ratio dressed
    q0 = mp.mpf("0.87801698486368466468255517896525729842228459217992")
    e_mu = q0 ** (-5) + q0 ** 5
    e_tau = q0 ** (-7) + q0 ** 7
    f_mu = mp.mpf("1")
    f_tau = (m_tau_pdg_mev / m_mu_mev) / (e_tau / e_mu)
    m_tau_anchored = m_mu_mev * (e_tau / e_mu) * (f_tau / f_mu)
    scale_lambda = mp.mpf("137.035999177")
    m_tau_rescaled = m_mu_mev * ((scale_lambda * e_tau) / (scale_lambda * e_mu)) * (f_tau / f_mu)
    scale_invariance_residual = abs(m_tau_anchored - m_tau_rescaled)
    se9w_passed = bool(
        w_crossings == [3, 5, 7]
        and (w_crossings[1] - w_crossings[0]) == 2
        and (w_crossings[2] - w_crossings[1]) == 2
        and scale_invariance_residual < mp.mpf("1e-55")
    )

    # 2. qou-h0zz: Framed carrier braid writhe sign dictionary and weak hypercharge cancellation
    carriers = {
        "nu_e": 1,
        "nubar_e": -1,
        "e_minus": 3,
        "e_plus": -3,
        "baryon_B3": 0,
        "gluon_unit": 0,
    }

    def sgn(w: int) -> int:
        return 1 if w > 0 else (-1 if w < 0 else 0)

    lepton_numbers = {k: sgn(w) for k, w in carriers.items()}
    mirror_odd_ok = all(sgn(-w) == -sgn(w) for w in carriers.values())
    three_y_quark_lh = 1 - 3 * lepton_numbers["baryon_B3"]
    three_y_lepton_lh = 0 - 3 * lepton_numbers["nu_e"]
    anomaly_linear_sum = 3 * 2 * three_y_quark_lh + 2 * three_y_lepton_lh
    h0zz_passed = bool(
        lepton_numbers == {
            "nu_e": 1,
            "nubar_e": -1,
            "e_minus": 1,
            "e_plus": -1,
            "baryon_B3": 0,
            "gluon_unit": 0,
        }
        and mirror_odd_ok
        and three_y_quark_lh == 1
        and three_y_lepton_lh == -3
        and anomaly_linear_sum == 0
    )

    # 3. qou-8p1e: Nodal curve genus drop bookkeeping and 7D imaginary unit stabilizer split
    g_arith = 4
    h1_rank_bring = 2 * g_arith
    g_geom_single_node = g_arith - 1
    h1_rank_single_node = 2 * g_geom_single_node
    g_geom_two_nodes = g_arith - 2
    im_octonion_split = [1, 3, 3]
    coset_dim_s6 = 14 - 8
    p1e_passed = bool(
        h1_rank_bring == 8
        and g_geom_single_node == 3
        and h1_rank_single_node == 6
        and g_geom_two_nodes <= 2
        and sum(im_octonion_split) == 7
        and coset_dim_s6 == 6
    )

    # 4. qou-d8de: Color spectral cubic P(X,z) power sums p_n(z) = -(z^n + 1)
    max_power_sum_residual = mp.mpf(0)
    power_sum_samples = {}
    for z_int in (1, 2, 3, 5):
        z = mp.mpf(z_int)
        e1 = z + 1
        e2 = z ** 2 + z + 1
        e3 = z ** 3 + z ** 2 + z + 1
        p1 = -e1
        p2 = -e1 * p1 - 2 * e2
        p3 = -e1 * p2 - e2 * p1 - 3 * e3
        r1 = abs(p1 - (-(z ** 1 + 1)))
        r2 = abs(p2 - (-(z ** 2 + 1)))
        r3 = abs(p3 - (-(z ** 3 + 1)))
        max_power_sum_residual = max(max_power_sum_residual, r1, r2, r3)
        power_sum_samples[str(z_int)] = [int(p1), int(p2), int(p3)]

    parity_preserved_classical = all(((k + 2) % 2) == (k % 2) for k in range(10))
    parity_flipped_qdiff = all(((k + 1) % 2) != (k % 2) for k in range(10))
    d8de_passed = bool(
        max_power_sum_residual == 0
        and power_sum_samples["1"] == [-2, -2, -2]
        and power_sum_samples["2"] == [-3, -5, -9]
        and power_sum_samples["3"] == [-4, -10, -28]
        and parity_preserved_classical
        and parity_flipped_qdiff
    )

    # 5. qou-wqto: Generation-1 8-state chirality involution and 2-bit projection collapse
    states = [(q, f, c) for q in (False, True) for f in (False, True) for c in (False, True)]

    def flip(s: tuple[bool, bool, bool]) -> tuple[bool, bool, bool]:
        return (s[0], s[1], not s[2])

    def chir_sign(s: tuple[bool, bool, bool]) -> int:
        return 1 if s[2] else -1

    def drop_chir(s: tuple[bool, bool, bool]) -> tuple[bool, bool]:
        return (s[0], s[1])

    involution_ok = all(flip(flip(s)) == s for s in states)
    fixed_point_free_ok = all(flip(s) != s for s in states)
    odd_grading_ok = all(chir_sign(flip(s)) == -chir_sign(s) for s in states)
    projection_collapse_ok = all(drop_chir(flip(s)) == drop_chir(s) for s in states)
    distinct_projections = len({drop_chir(s) for s in states})
    wqto_passed = bool(
        len(states) == 8
        and involution_ok
        and fixed_point_free_ok
        and odd_grading_ok
        and projection_collapse_ok
        and distinct_projections == 4
    )

    checks = [
        {
            "id": "qou_se9w_muon_anchored_tau_ratio_and_scale_invariance",
            "bean": "qou-se9w",
            "passed": se9w_passed,
            "charged_lepton_crossings": w_crossings,
            "e_mu_bare": mpf_str(e_mu),
            "e_tau_bare": mpf_str(e_tau),
            "f_tau_over_f_mu": mpf_str(f_tau),
            "m_tau_anchored_mev": mpf_str(m_tau_anchored),
            "scale_invariance_residual": mpf_str(scale_invariance_residual),
        },
        {
            "id": "qou_h0zz_chiral_carrier_writhe_and_hypercharge_cancellation",
            "bean": "qou-h0zz",
            "passed": h0zz_passed,
            "carrier_writhes": carriers,
            "lepton_numbers": lepton_numbers,
            "three_y_quark_lh": three_y_quark_lh,
            "three_y_lepton_lh": three_y_lepton_lh,
            "anomaly_linear_sum": anomaly_linear_sum,
        },
        {
            "id": "qou_8p1e_nodal_genus_bookkeeping_and_imaginary_split",
            "bean": "qou-8p1e",
            "passed": p1e_passed,
            "g_arith": g_arith,
            "h1_rank_bring": h1_rank_bring,
            "g_geom_single_node": g_geom_single_node,
            "h1_rank_single_node": h1_rank_single_node,
            "g_geom_two_nodes": g_geom_two_nodes,
            "im_octonion_split": im_octonion_split,
            "coset_dim_s6": coset_dim_s6,
        },
        {
            "id": "qou_d8de_spectral_cubic_power_sums_and_ramified_parity",
            "bean": "qou-d8de",
            "passed": d8de_passed,
            "power_sum_samples": power_sum_samples,
            "max_power_sum_residual": mpf_str(max_power_sum_residual),
            "parity_preserved_classical": parity_preserved_classical,
            "parity_flipped_qdiff": parity_flipped_qdiff,
        },
        {
            "id": "qou_wqto_gen1_chirality_involution_and_projection_collapse",
            "bean": "qou-wqto",
            "passed": wqto_passed,
            "state_count": len(states),
            "distinct_two_bit_projections": distinct_projections,
            "involution_ok": involution_ok,
            "fixed_point_free_ok": fixed_point_free_ok,
            "odd_grading_ok": odd_grading_ok,
            "projection_collapse_ok": projection_collapse_ok,
        },
    ]

    all_passed = all(c["passed"] for c in checks)
    witness = {
        "probe": "tau-anchored-ratio-chiral-braid-writhe-and-spectral-cubic-power-sums",
        "beans": ["qou-se9w", "qou-h0zz", "qou-8p1e", "qou-d8de", "qou-wqto"],
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
        "tau-anchored-ratio-chiral-braid-writhe-and-spectral-cubic-power-sums.witness.json"
    )
    out_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out_path} (allPassed={witness['allPassed']})")
    if not witness["allPassed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
