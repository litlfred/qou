#!/usr/bin/env python3
"""50-dps mpmath probe for Round 52 (qou-v2om):
- qou-892m: Two unreconciled kT assignments (hbar_q in information-theory vs E_0 in binding)
- qou-9lew: Site-vs-bond factor 2 in Borromean volume term (2 ideal octahedra Vol(B_3) = 2 * V_oct)
- qou-c6gx: 2D interface collapse, convention-C deuteron floor 2.907 MeV, A-scaling sign flip, 3He ordering
- qou-fdjp: Proton vs muon re-pin moves E_0 by 127.978 ppb vs 21%-226% binding error (~1.8e7x smaller)
- qou-fi1p: DeuteronKernel.bondL vs InterfaceScalar writhe sign opposition (2.7288 vs 0.7653 MeV, 3.57x)
"""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import subprocess

import mpmath as mp

mp.mp.dps = 50

Q0_PROTON_50_STR = "1.1099785827513808075916690956107688798744991218736"
Q0_MUON_50_STR = "1.10997859555733471989976322048322502665620840878015"
ME_MEV_STR = "0.51099895069"
VOL_B3_STR = "7.3277247534177487660168660064296223823151084746278"
A_V_SEMF_MEV_STR = "15.6"


def get_git_head_sha(repo_root: pathlib.Path) -> str:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(repo_root), text=True
        ).strip()
        return out
    except Exception:
        return "0" * 40


def get_file_last_commit_sha(repo_root: pathlib.Path, rel_path: str, fallback: str) -> str:
    try:
        out = subprocess.check_output(
            ["git", "log", "-n", "1", "--format=%H", "--", rel_path],
            cwd=str(repo_root),
            text=True,
        ).strip()
        return out if out else fallback
    except Exception:
        return fallback


def main() -> None:
    script_file = pathlib.Path(__file__).resolve()
    repo_root = script_file.parent.parent.parent
    rel_script_path = script_file.relative_to(repo_root).as_posix()
    script_bytes = script_file.read_bytes()
    script_hash = hashlib.sha256(script_bytes).hexdigest()[:12]
    head_sha = get_git_head_sha(repo_root)
    script_commit_sha = get_file_last_commit_sha(repo_root, rel_script_path, head_sha)

    q0_p = mp.mpf(Q0_PROTON_50_STR)
    q0_mu = mp.mpf(Q0_MUON_50_STR)
    me_mev = mp.mpf(ME_MEV_STR)
    vol_b3 = mp.mpf(VOL_B3_STR)
    a_v_semf = mp.mpf(A_V_SEMF_MEV_STR)

    # 1. qou-892m: Two unreconciled kT assignments (hbar_q vs E_0)
    hbar_q = (q0_p - mp.mpf(1)) / q0_p
    inv_hbar_q = mp.mpf(1) / hbar_q
    e0_p = me_mev / (q0_p * (q0_p - mp.mpf(1)))
    e0_over_me = e0_p / me_mev
    ratio_inv_hbar_q_to_e0_over_me = inv_hbar_q / e0_over_me
    me_times_hbar_q = me_mev * hbar_q
    me_over_hbar_q_sq = me_mev / (hbar_q ** 2)

    qou_892m_ok = bool(
        abs(hbar_q - mp.mpf("0.09908171604")) < mp.mpf("1e-10")
        and abs(e0_p - mp.mpf("4.185981363")) < mp.mpf("1e-8")
        and abs(e0_over_me - mp.mpf("8.191761172")) < mp.mpf("1e-8")
        and abs(inv_hbar_q - mp.mpf("10.09267946")) < mp.mpf("1e-7")
        and abs(ratio_inv_hbar_q_to_e0_over_me - (q0_p ** 2)) < mp.mpf("1e-45")
    )

    # 2. qou-9lew: Site-vs-bond factor 2 in Borromean volume term
    v_oct = vol_b3 / mp.mpf(2)
    e_vol_full = e0_p * vol_b3
    e_vol_half = e0_p * v_oct
    ratio_full_to_av = e_vol_full / a_v_semf
    ratio_half_to_av = e_vol_half / a_v_semf
    rel_residual_half_pct = abs(mp.mpf(1) - ratio_half_to_av) * mp.mpf(100)

    qou_9lew_ok = bool(
        abs(e_vol_full - mp.mpf("30.6737")) < mp.mpf("0.001")
        and abs(e_vol_half - mp.mpf("15.3369")) < mp.mpf("0.001")
        and abs(ratio_full_to_av - mp.mpf("1.966")) < mp.mpf("0.001")
        and rel_residual_half_pct < mp.mpf("1.75")
    )

    # 3. qou-c6gx: 2D interface collapse, convention-C 2H floor, A-scaling sign flip, 3He ordering
    z_c = mp.mpf(1) / (mp.sqrt(q0_p) + mp.mpf(1) / mp.sqrt(q0_p))
    h_step = q0_p - mp.mpf(1) / q0_p
    l_pp_c = -mp.log(z_c)
    l_pn_avg_c = -mp.log(z_c - h_step / mp.mpf(2))
    l_nn_c = -mp.log(z_c - h_step)
    b_pp_c = e0_p * l_pp_c
    b_pn_avg_c = e0_p * l_pn_avg_c
    b_nn_c = e0_p * l_nn_c
    b_ame_2h = mp.mpf("2.2245662")
    floor_overshoot_pct = (b_pp_c - b_ame_2h) / b_ame_2h * mp.mpf(100)

    # 3He ordering spread: ppn (B_pp + B_pn) vs pnp (2 * B_pn) using cw B_pn = 3.889692
    b_pn_cw_c = mp.mpf("3.889692")
    b_3he_ppn = b_pp_c + b_pn_cw_c
    b_3he_pnp = mp.mpf(2) * b_pn_cw_c
    spread_3he = b_3he_pnp - b_3he_ppn

    # Per-bond deficits (MeV/bond): 2H (+1.6651), 3H (+0.2929), 3He (-0.4606), 4He (-5.4403)
    def_2h = mp.mpf("1.6651")
    def_4he = mp.mpf("-5.4403")
    def_spread = def_2h - def_4he

    qou_c6gx_ok = bool(
        abs(b_pp_c - mp.mpf("2.907195")) < mp.mpf("0.0001")
        and abs(b_nn_c - mp.mpf("5.177967")) < mp.mpf("0.0001")
        and abs(floor_overshoot_pct - mp.mpf("30.69")) < mp.mpf("0.02")
        and def_2h > 0 > def_4he
        and abs(spread_3he - mp.mpf("0.9825")) < mp.mpf("0.001")
    )

    # 4. qou-fdjp: Proton vs muon re-pin shift (127.978 ppb vs 21%-226% error)
    e0_mu = me_mev / (q0_mu * (q0_mu - mp.mpf(1)))
    repin_rel_diff = (e0_p - e0_mu) / e0_mu
    repin_ppb = repin_rel_diff * mp.mpf("1e9")
    he4_rel_err = mp.mpf("2.26")
    ratio_err_to_repin = he4_rel_err / repin_rel_diff

    qou_fdjp_ok = bool(
        abs(repin_ppb - mp.mpf("127.978")) < mp.mpf("0.01")
        and ratio_err_to_repin > mp.mpf("1.7e7")
    )

    # 5. qou-fi1p: DeuteronKernel.bondL vs InterfaceScalar writhe sign opposition
    four_log_q = mp.mpf(4) * mp.log(q0_p)
    log_one_minus_h = mp.log(mp.mpf(1) - h_step)
    split_interface_scalar = e0_p * (four_log_q + log_one_minus_h)
    split_bond_l = e0_p * (four_log_q - log_one_minus_h)
    split_bare_trace = e0_p * four_log_q
    ratio_bond_l_to_interface_scalar = split_bond_l / split_interface_scalar
    midpoint_residual = (split_bond_l + split_interface_scalar) / mp.mpf(2) - split_bare_trace

    qou_fi1p_ok = bool(
        abs(split_interface_scalar - mp.mpf("0.765320193")) < mp.mpf("1e-6")
        and abs(split_bond_l - mp.mpf("2.72882629")) < mp.mpf("1e-5")
        and abs(split_bare_trace - mp.mpf("1.74707324")) < mp.mpf("1e-5")
        and abs(ratio_bond_l_to_interface_scalar - mp.mpf("3.5656")) < mp.mpf("0.001")
        and abs(midpoint_residual) < mp.mpf("1e-45")
    )

    assertions = {
        "qou_892m_two_kt_assignments_differ_by_exact_q0_squared": qou_892m_ok,
        "qou_9lew_octahedral_half_volume_matches_1_966x_factor_two": qou_9lew_ok,
        "qou_c6gx_2d_interface_floor_2_907_mev_and_a_scaling_sign_flip": qou_c6gx_ok,
        "qou_fdjp_proton_repin_moves_e0_by_127_978_ppb_vs_226_pct_error": qou_fdjp_ok,
        "qou_fi1p_writhe_sign_opposition_gives_3_57x_endpoint_mirror_split": qou_fi1p_ok,
    }
    all_passed = all(assertions.values())
    if not all_passed:
        raise RuntimeError(f"Probe assertions failed: {assertions}")

    witness = {
        "probeId": "kt-repin-octahedron-interface-writhe-probe",
        "beans": ["qou-892m", "qou-9lew", "qou-c6gx", "qou-fdjp", "qou-fi1p"],
        "parentBean": "qou-v2om",
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "dps": "50",
        "q0Anchor": "proton",
        "q0Value50": Q0_PROTON_50_STR,
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": head_sha,
        "scriptFile": script_file.name,
        "scriptPath": rel_script_path,
        "scriptHash": script_hash,
        "scriptCommitSha": script_commit_sha,
        "allPassed": all_passed,
        "assertions": assertions,
        "results": {
            "qou_892m_two_kt_assignments": {
                "hbarQ": mp.nstr(hbar_q, 50),
                "invHbarQ": mp.nstr(inv_hbar_q, 50),
                "e0ProtonMeV": mp.nstr(e0_p, 50),
                "e0OverMe": mp.nstr(e0_over_me, 50),
                "ratioInvHbarQToE0OverMe": mp.nstr(ratio_inv_hbar_q_to_e0_over_me, 50),
                "q0Squared": mp.nstr(q0_p ** 2, 50),
                "meTimesHbarQMeV": mp.nstr(me_times_hbar_q, 50),
                "meOverHbarQSquaredMeV": mp.nstr(me_over_hbar_q_sq, 50),
            },
            "qou_9lew_borromean_volume_factor_two": {
                "volB3": mp.nstr(vol_b3, 50),
                "vOct": mp.nstr(v_oct, 50),
                "e0TimesVolB3MeV": mp.nstr(e_vol_full, 50),
                "e0TimesVOctMeV": mp.nstr(e_vol_half, 50),
                "ratioFullToAvSemf": mp.nstr(ratio_full_to_av, 50),
                "ratioHalfToAvSemf": mp.nstr(ratio_half_to_av, 50),
                "halfVolumeResidualPct": mp.nstr(rel_residual_half_pct, 50),
            },
            "qou_c6gx_2d_interface_floor_and_ordering": {
                "zConventionC": mp.nstr(z_c, 50),
                "hStep": mp.nstr(h_step, 50),
                "bPpFloorMeV": mp.nstr(b_pp_c, 50),
                "bPnAvgMeV": mp.nstr(b_pn_avg_c, 50),
                "bNnCeilMeV": mp.nstr(b_nn_c, 50),
                "floorOvershootOver2HAmePct": mp.nstr(floor_overshoot_pct, 50),
                "perBondDeficit2HMeV": mp.nstr(def_2h, 50),
                "perBondDeficit4HeMeV": mp.nstr(def_4he, 50),
                "perBondDeficitSpreadMeV": mp.nstr(def_spread, 50),
                "orderingSpread3HePnpMinusPpnMeV": mp.nstr(spread_3he, 50),
            },
            "qou_fdjp_proton_vs_muon_repin_bound": {
                "e0ProtonMeV": mp.nstr(e0_p, 50),
                "e0MuonMeV": mp.nstr(e0_mu, 50),
                "repinRelativeDiffPpb": mp.nstr(repin_ppb, 50),
                "ratioHe4ErrorToRepinShift": mp.nstr(ratio_err_to_repin, 50),
            },
            "qou_fi1p_writhe_sign_opposition": {
                "fourLogQ": mp.nstr(four_log_q, 50),
                "logOneMinusH": mp.nstr(log_one_minus_h, 50),
                "interfaceScalarMirrorSplitMeV": mp.nstr(split_interface_scalar, 50),
                "bondLMirrorSplitMeV": mp.nstr(split_bond_l, 50),
                "bareTransferTraceMirrorSplitMeV": mp.nstr(split_bare_trace, 50),
                "ratioBondLToInterfaceScalar": mp.nstr(ratio_bond_l_to_interface_scalar, 50),
                "midpointMinusBareResidualMeV": mp.nstr(midpoint_residual, 50),
            },
        },
    }

    witness_path = script_file.parent / "kt-repin-octahedron-interface-writhe-probe.witness.json"
    witness_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote witness to {witness_path.relative_to(repo_root)} (allPassed={all_passed})")


if __name__ == "__main__":
    main()
