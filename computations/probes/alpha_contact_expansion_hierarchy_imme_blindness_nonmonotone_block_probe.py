#!/usr/bin/env python3
"""
50-dps mpmath numerical witness probe for:
  - qou-3lsb: GAP-4 cluster/halo deviations below max-contact (3*n_alpha - 6 rigid
              contact ceiling vs C(n_alpha,2) complete pairs; 20Ne prolate 8 vs 9)
  - qou-ebs6: b_alpha-alpha ~ 2.41 MeV is not closable on present evidence
              (n_alpha <= 4 equilateral domain has 3 nuclei, 8Be excused, 2 fit
              points 2.425 and 2.406 MeV for 1 parameter -> 1 residual DOF, 0 out-of-sample)
  - qou-3wxk: A7 chiral-EFT power counting vs native QOU expansion parameter
              u = b*hbar_q^2 ~ 0.00852 vs Q/Lambda_chi ~ 0.33 (> 38x hierarchy gap)
  - qou-se8k: A5 IMME rank <= 2 second and third differences in T_3 annihilate
              the isoscalar extensive term a identically
  - qou-wdij: Borromean atom word [0,1,0,1,0,1,0,0,1,0,0] is non-monotone (refused
              by monotone transfer), while disjoint-block quadratic epsilon-series
              factorisation holds to O(eps^3)
"""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import subprocess
import mpmath as mp

mp.mp.dps = 50


def fmt50(x: mp.mpf) -> str:
    return mp.nstr(x, 50, strip_zeros=False)


def main() -> None:
    script_path = pathlib.Path(__file__).resolve()
    repo_root = script_path.parents[2]
    script_bytes = script_path.read_bytes()
    script_hash = hashlib.sha256(script_bytes).hexdigest()[:12]

    try:
        commit_sha = (
            subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=str(repo_root)
            )
            .decode("utf-8")
            .strip()
        )
    except Exception:
        commit_sha = "0" * 40

    checks = []

    # 1. qou-3lsb: alpha-cluster contact ceiling 3*n_alpha - 6 vs C(n_alpha,2) and 20Ne prolate deficit
    for n_a in [3, 4, 5, 6]:
        n_mp = mp.mpf(n_a)
        rigid_max = mp.mpf(3) * n_mp - mp.mpf(6)
        comp_s2 = n_mp * (n_mp - mp.mpf(1))
        excess_s2 = comp_s2 - mp.mpf(2) * rigid_max
        fac_s2 = (n_mp - mp.mpf(3)) * (n_mp - mp.mpf(4))
        prolate = mp.mpf(3) * n_mp - mp.mpf(7)
        passed_3lsb = (
            (excess_s2 == fac_s2)
            and ((n_a in (3, 4) and excess_s2 == mp.mpf(0)) or (n_a >= 5 and excess_s2 > mp.mpf(0)))
            and (rigid_max - prolate == mp.mpf(1))
        )
        checks.append(
            {
                "id": f"qou_3lsb_alpha_contact_ceiling_n_alpha_{n_a}",
                "bean": "qou-3lsb",
                "nAlpha": str(n_a),
                "rigidMaxContacts": fmt50(rigid_max),
                "completePairsScaled2": fmt50(comp_s2),
                "excessScaled2": fmt50(excess_s2),
                "prolateSubMaxContacts": fmt50(prolate),
                "passed": bool(passed_3lsb),
            }
        )

    # 2. qou-ebs6: b_alpha_alpha DOF accounting and 12C / 16O spread
    b_c12_mev = mp.mpf("2.425")
    b_o16_mev = mp.mpf("2.406")
    spread_mev = b_c12_mev - b_o16_mev
    total_valid = mp.mpf(3)
    excused_be8 = mp.mpf(1)
    fitted_params = mp.mpf(1)
    residual_dof = total_valid - excused_be8 - fitted_params
    passed_ebs6 = (
        (residual_dof == mp.mpf(1))
        and mp.almosteq(spread_mev, mp.mpf("0.019"), rel_eps=mp.mpf("1e-45"))
    )
    checks.append(
        {
            "id": "qou_ebs6_b_alpha_alpha_dof_and_spread",
            "bean": "qou-ebs6",
            "bAlphaAlphaC12MeV": fmt50(b_c12_mev),
            "bAlphaAlphaO16MeV": fmt50(b_o16_mev),
            "spreadMeV": fmt50(spread_mev),
            "residualDOF": fmt50(residual_dof),
            "passed": bool(passed_ebs6),
        }
    )

    # 3. qou-3wxk: native u = 0.00852 vs chiral Q/Lambda_chi = 0.33 hierarchy ratio
    u_qou = mp.mpf("0.00852")
    q_over_lambda = mp.mpf("0.33")
    ratio_chiral_to_u = q_over_lambda / u_qou
    spread_hierarchy = q_over_lambda - u_qou
    passed_3wxk = (ratio_chiral_to_u > mp.mpf(38)) and mp.almosteq(
        spread_hierarchy, mp.mpf("0.32148"), rel_eps=mp.mpf("1e-45")
    )
    checks.append(
        {
            "id": "qou_3wxk_expansion_hierarchy_incommensurability",
            "bean": "qou-3wxk",
            "uQOU": fmt50(u_qou),
            "chiralQOverLambda": fmt50(q_over_lambda),
            "hierarchyRatio": fmt50(ratio_chiral_to_u),
            "hierarchySpread": fmt50(spread_hierarchy),
            "passed": bool(passed_3wxk),
        }
    )

    # 4. qou-se8k: IMME second and third differences annihilate isoscalar a
    def imme_poly(a: mp.mpf, b: mp.mpf, c: mp.mpf, d: mp.mpf, t3: mp.mpf) -> mp.mpf:
        return a + b * t3 + c * (t3 ** 2) + d * (t3 ** 3)

    b_val = mp.mpf("-1.372")
    c_val = mp.mpf("0.215")
    d_val = mp.mpf("0.0000001")
    a_val_1 = mp.mpf("100.0")
    a_val_2 = mp.mpf("9500.0")
    diff2_a1 = imme_poly(a_val_1, b_val, c_val, d_val, mp.mpf(1)) - mp.mpf(2) * imme_poly(a_val_1, b_val, c_val, d_val, mp.mpf(0)) + imme_poly(a_val_1, b_val, c_val, d_val, mp.mpf(-1))
    diff2_a2 = imme_poly(a_val_2, b_val, c_val, d_val, mp.mpf(1)) - mp.mpf(2) * imme_poly(a_val_2, b_val, c_val, d_val, mp.mpf(0)) + imme_poly(a_val_2, b_val, c_val, d_val, mp.mpf(-1))
    diff3_a1 = (
        imme_poly(a_val_1, b_val, c_val, d_val, mp.mpf(2))
        - mp.mpf(3) * imme_poly(a_val_1, b_val, c_val, d_val, mp.mpf(1))
        + mp.mpf(3) * imme_poly(a_val_1, b_val, c_val, d_val, mp.mpf(0))
        - imme_poly(a_val_1, b_val, c_val, d_val, mp.mpf(-1))
    )
    diff3_a2 = (
        imme_poly(a_val_2, b_val, c_val, d_val, mp.mpf(2))
        - mp.mpf(3) * imme_poly(a_val_2, b_val, c_val, d_val, mp.mpf(1))
        + mp.mpf(3) * imme_poly(a_val_2, b_val, c_val, d_val, mp.mpf(0))
        - imme_poly(a_val_2, b_val, c_val, d_val, mp.mpf(-1))
    )
    passed_se8k = (
        mp.almosteq(diff2_a1, mp.mpf(2) * c_val, rel_eps=mp.mpf("1e-45"))
        and mp.almosteq(diff2_a1, diff2_a2, rel_eps=mp.mpf("1e-45"))
        and mp.almosteq(diff3_a1, mp.mpf(6) * d_val, rel_eps=mp.mpf("1e-40"))
        and mp.almosteq(diff3_a1, diff3_a2, rel_eps=mp.mpf("1e-40"))
    )
    checks.append(
        {
            "id": "qou_se8k_imme_differences_isoscalar_blindness",
            "bean": "qou-se8k",
            "secondDiffA1": fmt50(diff2_a1),
            "secondDiffA2": fmt50(diff2_a2),
            "thirdDiffA1": fmt50(diff3_a1),
            "thirdDiffA2": fmt50(diff3_a2),
            "passed": bool(passed_se8k),
        }
    )

    # 5. qou-wdij: Borromean generator sequence non-monotonicity and disjoint-block epsilon product
    borromean_gens = [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0]
    grouped_gens = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
    borromean_descents = sum(max(0, borromean_gens[i] - borromean_gens[i + 1]) for i in range(len(borromean_gens) - 1))
    grouped_descents = sum(max(0, grouped_gens[i] - grouped_gens[i + 1]) for i in range(len(grouped_gens) - 1))
    # Proton (a1, b1, c1) = (1/2, 3/4, 23/8) and Neutron (a2, b2, c2) = (1/2, -1/2, 3/2)
    a1, b1, c1 = mp.mpf("0.5"), mp.mpf("0.75"), mp.mpf("2.875")
    a2, b2, c2 = mp.mpf("0.5"), mp.mpf("-0.5"), mp.mpf("1.5")
    eps = mp.mpf("0.01")
    full_prod = (a1 + b1 * eps + c1 * (eps ** 2)) * (a2 + b2 * eps + c2 * (eps ** 2))
    trunc_quad = (a1 * a2) + (a1 * b2 + b1 * a2) * eps + (a1 * c2 + b1 * b2 + c1 * a2) * (eps ** 2)
    rem_exact = (b1 * c2 + c1 * b2) * (eps ** 3) + (c1 * c2) * (eps ** 4)
    passed_wdij = (
        (borromean_descents == 4)
        and (grouped_descents == 0)
        and mp.almosteq(full_prod - trunc_quad, rem_exact, rel_eps=mp.mpf("1e-45"))
    )
    checks.append(
        {
            "id": "qou_wdij_borromean_nonmonotone_and_disjoint_block_series",
            "bean": "qou-wdij",
            "borromeanDescentSum": str(borromean_descents),
            "groupedDescentSum": str(grouped_descents),
            "fullBlockProductAtEps001": fmt50(full_prod),
            "truncatedQuadraticAtEps001": fmt50(trunc_quad),
            "cubicPlusQuarticRemainder": fmt50(rem_exact),
            "passed": bool(passed_wdij),
        }
    )

    all_passed = all(c["passed"] for c in checks)
    witness = {
        "probe": "alpha_contact_expansion_hierarchy_imme_blindness_nonmonotone_block_probe",
        "beans": ["qou-3lsb", "qou-3wxk", "qou-ebs6", "qou-se8k", "qou-wdij"],
        "dps": "50",
        "scriptCommitSha": commit_sha,
        "scriptHash": script_hash,
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "allPassed": bool(all_passed),
        "checks": checks,
    }

    out_path = script_path.with_name(
        "alpha-contact-expansion-hierarchy-imme-blindness-nonmonotone-block-probe.witness.json"
    )
    out_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"allPassed={all_passed} scriptHash={script_hash} commit={commit_sha}")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
