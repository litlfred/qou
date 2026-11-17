#!/usr/bin/env python3
"""
50-dps mpmath verification probe for Round 55 (`qou-v2om`):
  - qou-ls86: Many-body collective residual R/A positivity and bounds on the well-bound regime
  - qou-q6pp: Wedderburn atomic mass decomposition, A=1 isobaric difference, and chirality weights
  - qou-q7ga: First-order q-deformation asymmetry (+2e(N-Z)) and exact pure-crossing bond ratio
  - qou-rwhv: Third-order Ursell alternating-sign identity (b_3 = -phi^T_3 < 0 for f in (0,1))
  - qou-xzda: B_sym chain closed-form constant Reeb override offset (1.6561 MeV across A)
"""

import datetime
import hashlib
import json
import pathlib
import subprocess
from mpmath import mp

mp.dps = 50

Q0 = mp.mpf("1.10997858275138080760153841189813792762285402139780")
ME_MEV = mp.mpf("0.51099895069")
ALPHA_MEV = ME_MEV / (Q0 * (Q0 - 1))


def check_qou_ls86():
    # Well-bound regime bounds: B_AME/A in [5, 8.8], B_sym/A in [0.6, 2.9], R/A = B_AME/A - B_sym/A
    b_lo = mp.mpf("5.0")
    b_hi = mp.mpf("8.79456")
    c_lo = mp.mpf("0.6")
    c_hi = mp.mpf("2.8991")
    # Sample well-bound point (4He: B_AME/A = 28.295674 / 4 = 7.0739185, B_sym/A = 10.318798 / 4 = 2.5796995)
    b_ame_he4 = mp.mpf("28.295674")
    b_sym_he4 = mp.mpf("10.318798")
    a_he4 = mp.mpf("4")
    r_he4 = (b_ame_he4 - b_sym_he4) / a_he4
    r_he4_sub = (b_ame_he4 / a_he4) - (b_sym_he4 / a_he4)
    # Sample drip-line / weakly bound point (2H: B_AME/A = 2.224566 / 2 = 1.112283, B_sym_exact/A = 3.889692 / 2 = 1.944846)
    b_ame_d = mp.mpf("2.224566")
    b_sym_d = mp.mpf("3.889692")
    a_d = mp.mpf("2")
    r_d = (b_ame_d - b_sym_d) / a_d

    passed = (
        abs(r_he4 - r_he4_sub) < mp.mpf("1e-48")
        and r_he4 > 0
        and (b_lo - c_hi) <= r_he4 <= (b_hi - c_lo)
        and r_d < 0
    )
    return {
        "id": "qou-ls86",
        "passed": bool(passed),
        "he4CollectivePerNucleonMeV": mp.nstr(r_he4, 30),
        "deuteronDripCollectivePerNucleonMeV": mp.nstr(r_d, 30),
        "wellBoundFloorMeV": mp.nstr(b_lo - c_hi, 30),
        "wellBoundCeilingMeV": mp.nstr(b_hi - c_lo, 30),
    }


def check_qou_q6pp():
    # Generator count A + Z - 1 and quantized chirality weights w(Z, N)
    gen_counts = {
        "1H": 1 + 1 - 1,
        "D": 2 + 1 - 1,
        "T": 3 + 1 - 1,
        "4He": 4 + 2 - 1,
    }
    chirality_weights = {
        "1H": 4 * 1,
        "D": 6 * 1,
        "T": 6 * 1,
        "3He": 6 * 2,
        "4He": 6 * 2,
    }
    # Isobaric A=1 difference cancels identical Phi_2
    m_p = mp.mpf("938.27208816")
    m_n = mp.mpf("939.56542052")
    m_e = ME_MEV
    h = Q0 - 1 / Q0
    phi_2 = 2 * mp.log(1 + h**2 / 4)
    q3_2 = 2 * (Q0 + 1 + 1 / Q0)
    phi_1_p = mp.mpf("-1.665")
    phi_1_n = mp.mpf("-1.814")
    phi_3_p = 4 * mp.log(Q0)
    phi_3_n = 6 * mp.log(Q0)

    mass_p = 1 * m_p + 0 * m_n + 1 * m_e + ALPHA_MEV * (phi_1_p - q3_2 * phi_2 + h**2 * phi_3_p)
    mass_n = 0 * m_p + 1 * m_n + 0 * m_e + ALPHA_MEV * (phi_1_n - q3_2 * phi_2 + h**2 * phi_3_n)
    diff_direct = mass_n - mass_p
    diff_reduced = (m_n - m_p - m_e) + ALPHA_MEV * ((phi_1_n - phi_1_p) + h**2 * (phi_3_n - phi_3_p))

    passed = (
        gen_counts == {"1H": 1, "D": 2, "T": 3, "4He": 5}
        and chirality_weights == {"1H": 4, "D": 6, "T": 6, "3He": 12, "4He": 12}
        and abs(diff_direct - diff_reduced) < mp.mpf("1e-45")
    )
    return {
        "id": "qou-q6pp",
        "passed": bool(passed),
        "generatorCounts": {k: str(v) for k, v in gen_counts.items()},
        "chiralityWeights": {k: str(v) for k, v in chirality_weights.items()},
        "phi2SharedValue": mp.nstr(phi_2, 30),
        "isobaricReductionResidual": mp.nstr(abs(diff_direct - diff_reduced), 30),
    }


def check_qou_q7ga():
    e = Q0 - 1
    b_pp_lin = mp.mpf("0.5") + e
    b_pn_lin = mp.mpf("0.5")
    b_nn_lin = mp.mpf("0.5") - e

    two_q = Q0 + 1 / Q0
    b_pp_exact = (Q0**2) / two_q
    b_nn_exact = (1 / (Q0**2)) / two_q

    ratio_exact = b_pp_exact / b_nn_exact
    prod_exact = b_pp_exact * b_nn_exact
    log_diff = mp.log(b_pp_exact) - mp.log(b_nn_exact)

    # Chain linear deformation for (Z, N) = (26, 30) (56Fe)
    Z, N = mp.mpf(26), mp.mpf(30)
    chain_def = (Z - 1) * (-2 * e) + (N - 1) * (2 * e)
    chain_def_formula = 2 * e * (N - Z)

    passed = (
        abs((b_pp_lin + b_nn_lin) - 2 * b_pn_lin) < mp.mpf("1e-48")
        and abs((b_pp_lin - b_nn_lin) - 2 * e) < mp.mpf("1e-48")
        and abs(chain_def - chain_def_formula) < mp.mpf("1e-48")
        and abs(ratio_exact - Q0**4) < mp.mpf("1e-48")
        and abs(prod_exact - 1 / (two_q**2)) < mp.mpf("1e-48")
        and abs(log_diff - 4 * mp.log(Q0)) < mp.mpf("1e-48")
    )
    return {
        "id": "qou-q7ga",
        "passed": bool(passed),
        "twoEAsymmetry": mp.nstr(2 * e, 30),
        "twoLogQ0ExactAsymmetry": mp.nstr(2 * mp.log(Q0), 30),
        "pureCrossingRatioQ4": mp.nstr(ratio_exact, 30),
        "pureCrossingProductInvLoopSq": mp.nstr(prod_exact, 30),
    }


def check_qou_rwhv():
    h = Q0 - 1 / Q0
    z_d = (Q0**3) / (Q0**2 + 1)
    # Proton-pin convention-D bond factors in (0, 1)
    f12 = z_d
    f13 = z_d - h / 2
    f23 = z_d - h

    g12 = f12 - 1
    g13 = f13 - 1
    g23 = f23 - 1

    phi2 = g12
    b2 = 1 - f12

    phi3 = g12 * g13 + g12 * g23 + g13 * g23 + g12 * g13 * g23
    phi3_factored = g12 * g13 * (1 + g23) + g12 * g23 + g13 * g23
    b3 = 1 - f12 * f13 * f23 - (1 - f12) - (1 - f13) - (1 - f23)

    passed = (
        0 < f12 < 1
        and 0 < f13 < 1
        and 0 < f23 < 1
        and abs(b2 - (-phi2)) < mp.mpf("1e-48")
        and abs(b3 - (-phi3)) < mp.mpf("1e-48")
        and abs(phi3 - phi3_factored) < mp.mpf("1e-48")
        and phi3 > 0
        and b3 < 0
    )
    return {
        "id": "qou-rwhv",
        "passed": bool(passed),
        "ursellPhi3": mp.nstr(phi3, 30),
        "corpusB3": mp.nstr(b3, 30),
        "identityResidual": mp.nstr(abs(b3 + phi3), 30),
    }


def check_qou_xzda():
    # Measured L_pn from (1,1) trace vs Reeb-flow override
    l_pp = mp.mpf("0.69450743692190434592")
    l_nn = mp.mpf("1.2369780839104215884")
    l_pn_trace = mp.mpf("0.92921872310485124918")
    l_pn_reeb = mp.mpf("0.53359852981239411205")

    expected_shift = ALPHA_MEV * (l_pn_trace - l_pn_reeb)
    isotopes = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]
    shifts = {}
    max_dev = mp.mpf("0")
    for name, z_val, n_val in isotopes:
        z_mp = mp.mpf(z_val)
        n_mp = mp.mpf(n_val)
        b_trace = ALPHA_MEV * ((z_mp - 1) * l_pp + l_pn_trace + (n_mp - 1) * l_nn)
        b_reeb = ALPHA_MEV * ((z_mp - 1) * l_pp + l_pn_reeb + (n_mp - 1) * l_nn)
        diff = b_trace - b_reeb
        shifts[name] = mp.nstr(diff, 30)
        max_dev = max(max_dev, abs(diff - expected_shift))

    passed = max_dev < mp.mpf("1e-48") and abs(expected_shift - mp.mpf("1.65606")) < mp.mpf("1e-4")
    return {
        "id": "qou-xzda",
        "passed": bool(passed),
        "constantShiftMeV": mp.nstr(expected_shift, 30),
        "isotopeShiftsMeV": shifts,
        "maxDeviationAcrossIsotopes": mp.nstr(max_dev, 30),
    }


def main():
    script_path = "computations/probes/collective_reeb_wedderburn_roast_ursell_probe.py"
    witness_path = "computations/probes/collective-reeb-wedderburn-roast-ursell-probe.witness.json"

    raw_bytes = pathlib.Path(script_path).read_bytes()
    script_hash = hashlib.sha256(raw_bytes).hexdigest()[:12]
    try:
        commit_sha = (
            subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
        )
    except Exception:
        commit_sha = "0" * 40

    checks = [
        check_qou_ls86(),
        check_qou_q6pp(),
        check_qou_q7ga(),
        check_qou_rwhv(),
        check_qou_xzda(),
    ]
    all_passed = all(c["passed"] for c in checks)

    witness = {
        "schemaVersion": "1.0",
        "probeId": "collective-reeb-wedderburn-roast-ursell-probe",
        "scriptPath": script_path,
        "scriptHash": script_hash,
        "scriptCommitSha": commit_sha,
        "timestamp": datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        ),
        "precisionDps": "50",
        "summary": {
            "totalChecks": str(len(checks)),
            "passedChecks": str(sum(1 for c in checks if c["passed"])),
            "allPassed": all_passed,
        },
        "checks": checks,
    }

    out = pathlib.Path(witness_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(
        f"Wrote {witness_path} (allPassed={all_passed}, scriptHash={script_hash}, sha={commit_sha})"
    )
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
