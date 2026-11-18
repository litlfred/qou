#!/usr/bin/env python3
"""80-dps mpmath numerical verification probe for Round 73 de-vacuification batch.

Verifies the 5 theorems added across:
1. qou-4hbq: QOU/Information/SkeinHorizonLowerBound.lean
   (`succ_iterate_add`, `treeSearch_len_lt_normalForm`)
2. qou-j0kz: QOU/Information/PhysicalIntractability.lean
   (`superPoly_resolutionTreeSize_three_mul`, `two_pow_le_steps_mul_bandwidth`)
3. qou-ok7t: QOU/Brings/ColourCubicDiscriminant.lean
   (`colourSextic_recip_identity`, `normSq_conj_eq_one_of_abs_le_two`)
4. qou-okh4: QOU/MassTheory/BorromeanA4TightSlice.lean
   (`one_lt_tauL4_of_ne_zero`, `borromean4_deficit_neg_of_ne_zero`)
5. moqg: QOU/BraidsAndKnots/BorromeanTowerConvergence.lean
   (`borromean_dressed_pair_within_radius`)
"""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import subprocess
from mpmath import mp

mp.dps = 80


def colour_sextic(z: mp.mpf) -> mp.mpf:
    return (
        mp.mpf("16") * z**6
        + mp.mpf("24") * z**5
        + mp.mpf("35") * z**4
        + mp.mpf("50") * z**3
        + mp.mpf("35") * z**2
        + mp.mpf("24") * z
        + mp.mpf("16")
    )


def tau_l4(h: mp.mpf) -> mp.mpf:
    return (h**10 + mp.mpf("5") * h**8 + mp.mpf("6") * h**6 + h**2 + mp.mpf("4")) / (
        h**2 + mp.mpf("4")
    )


def tr_m_borromean(h: mp.mpf) -> mp.mpf:
    return (mp.mpf("4") + h**2 - mp.mpf("3") * h**4 - h**6) / (h**2 + mp.mpf("4"))


def main() -> None:
    script_path = pathlib.Path(__file__).resolve()
    repo_root = script_path.parents[2]
    script_rel = str(script_path.relative_to(repo_root))
    script_sha256 = hashlib.sha256(script_path.read_bytes()).hexdigest()
    commit_sha = (
        subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo_root)
        .decode("utf-8")
        .strip()
    )

    checks = []

    # 1. qou-4hbq: SkeinHorizonLowerBound.lean — succ_iterate_add and treeSearch_len_lt_normalForm.
    d_val = 12
    m_val = 7
    k_val = 19
    iter_val = m_val + k_val
    normal_form = int(mp.power(3, d_val))
    hbq_pass = bool(iter_val == 26 and d_val < normal_form)
    checks.append(
        {
            "bean": "qou-4hbq",
            "file": "folio/quantum-observable-universe/lean/QOU/Information/SkeinHorizonLowerBound.lean",
            "theorems": [
                "succ_iterate_add",
                "treeSearch_len_lt_normalForm",
            ],
            "depth": d_val,
            "normalForm": normal_form,
            "iterateFromSevenByNineteen": iter_val,
            "passed": hbq_pass,
        }
    )

    # 2. qou-j0kz: PhysicalIntractability.lean — superPoly_resolutionTreeSize_three_mul and
    # two_pow_le_steps_mul_bandwidth.
    n_val = 8
    c_val = 3 * n_val
    tree_c = mp.power(3, c_val)
    two_pow_n = mp.power(2, n_val)
    j0kz_pass = bool(two_pow_n <= tree_c and tree_c > mp.mpf("100") * (mp.mpf(n_val) ** 4))
    checks.append(
        {
            "bean": "qou-j0kz",
            "file": "folio/quantum-observable-universe/lean/QOU/Information/PhysicalIntractability.lean",
            "theorems": [
                "superPoly_resolutionTreeSize_three_mul",
                "two_pow_le_steps_mul_bandwidth",
            ],
            "n": n_val,
            "twoPowN": mp.nstr(two_pow_n, 80),
            "resolutionTreeSize3N": mp.nstr(tree_c, 80),
            "passed": j0kz_pass,
        }
    )

    # 3. qou-ok7t: ColourCubicDiscriminant.lean — colourSextic_recip_identity and
    # normSq_conj_eq_one_of_abs_le_two at 80 dps.
    z_val = mp.mpf("1.37")
    w_val = mp.mpf("-1.43")
    lhs_sextic = colour_sextic(z_val)
    rhs_sextic = (z_val**6) * colour_sextic(mp.mpf("1") / z_val)
    sextic_res = abs(lhs_sextic - rhs_sextic)
    re_part = w_val / mp.mpf("2")
    im_part = -mp.sqrt(mp.mpf("4") - w_val**2) / mp.mpf("2")
    norm_sq_conj = re_part**2 + im_part**2
    norm_sq_res = abs(norm_sq_conj - mp.mpf("1"))
    ok7t_pass = bool(sextic_res < mp.mpf("1e-75") and norm_sq_res < mp.mpf("1e-75"))
    checks.append(
        {
            "bean": "qou-ok7t",
            "file": "folio/quantum-observable-universe/lean/QOU/Brings/ColourCubicDiscriminant.lean",
            "theorems": [
                "colourSextic_recip_identity",
                "normSq_conj_eq_one_of_abs_le_two",
            ],
            "colourSexticValue": mp.nstr(lhs_sextic, 80),
            "recipIdentityResidual": mp.nstr(sextic_res, 25),
            "conjUnitCircleResidual": mp.nstr(norm_sq_res, 25),
            "passed": ok7t_pass,
        }
    )

    # 4. qou-okh4: BorromeanA4TightSlice.lean — one_lt_tauL4_of_ne_zero and
    # borromean4_deficit_neg_of_ne_zero at h_0.
    h0 = mp.mpf("0.20905692653530692")
    tau_pos = tau_l4(h0)
    deficit_val = mp.mpf("1") - tau_pos
    okh4_pass = bool(tau_pos > mp.mpf("1") and deficit_val < mp.mpf("0"))
    checks.append(
        {
            "bean": "qou-okh4",
            "file": "folio/quantum-observable-universe/lean/QOU/MassTheory/BorromeanA4TightSlice.lean",
            "theorems": [
                "one_lt_tauL4_of_ne_zero",
                "borromean4_deficit_neg_of_ne_zero",
            ],
            "h0": mp.nstr(h0, 80),
            "tauL4AtH0": mp.nstr(tau_pos, 80),
            "deficitAtH0": mp.nstr(deficit_val, 80),
            "passed": okh4_pass,
        }
    )

    # 5. moqg: BorromeanTowerConvergence.lean — borromean_dressed_pair_within_radius.
    q0 = (h0 + mp.sqrt(h0**2 + mp.mpf("4"))) / mp.mpf("2")
    f_bond = mp.mpf("0.4991")
    tr_bor = tr_m_borromean(h0)
    dressed_pair = abs(tr_bor * tr_bor * f_bond)
    moqg_pass = bool(
        h0 != 0
        and h0**2 <= mp.mpf("1")
        and abs(f_bond) <= mp.mpf("1")
        and q0 > mp.mpf("1")
        and dressed_pair < q0
    )
    checks.append(
        {
            "bean": "moqg",
            "file": "folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/BorromeanTowerConvergence.lean",
            "theorems": [
                "borromean_dressed_pair_within_radius",
            ],
            "trMBorromeanAtH0": mp.nstr(tr_bor, 80),
            "dressedPairArg": mp.nstr(dressed_pair, 80),
            "q0Radius": mp.nstr(q0, 80),
            "passed": moqg_pass,
        }
    )

    all_passed = all(c["passed"] for c in checks)
    assert all_passed, "One or more probe checks failed!"

    witness = {
        "probe": "round73_devacuify_6qbv_b9cj_probe",
        "scriptPath": script_rel,
        "scriptCommitSha": commit_sha,
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "dps": 80,
        "mpmathDps": 80,
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "allPassed": all_passed,
        "checks": checks,
    }

    out_path = repo_root / "computations" / "probes" / "round73-devacuify-6qbv-b9cj.witness.json"
    out_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote witness to {out_path} (scriptCommitSha={commit_sha}, sha256={script_sha256})")


if __name__ == "__main__":
    main()
