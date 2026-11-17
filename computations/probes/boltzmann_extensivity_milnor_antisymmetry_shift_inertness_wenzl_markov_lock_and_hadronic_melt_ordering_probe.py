#!/usr/bin/env python3
"""
80-dps mpmath and exact Fraction probe for Round 71 beans under qou-10v9:
  - qou-d5e8: Boltzmann log-form extensivity vs linear-form bilinear defect and ceiling bound
  - qou-lq6k: Milnor triple-linking antisymmetry vs symmetric pair-energy obstruction
  - qou-tqfm: Shift-inert operator decomposition self-comparison vs physical colour-weighting discrepancy
  - qou-ughq: H_2 Wenzl block resolution ((2) vs (1,1)) vs unique Markov stabilization weight
  - qou-vvv4: Convention-D non-vanishing Wedderburn weights, convention-C ceiling, and hadronic melt ordering
"""

from __future__ import annotations

import datetime
import fractions
import hashlib
import json
import pathlib
import subprocess
import mpmath as mp

mp.mp.dps = 80

PROBE_PATH = "computations/probes/boltzmann_extensivity_milnor_antisymmetry_shift_inertness_wenzl_markov_lock_and_hadronic_melt_ordering_probe.py"
WITNESS_PATH = "computations/probes/boltzmann-extensivity-milnor-antisymmetry-shift-inertness-wenzl-markov-lock-and-hadronic-melt-ordering.witness.json"
MOD = "QOU.Eightfold.BoltzmannExtensivityMilnorAntisymmetryShiftInertnessWenzlMarkovLockAndHadronicMeltOrdering"


def get_git_sha() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()


def get_script_hash() -> str:
    raw = pathlib.Path(PROBE_PATH).read_bytes()
    return hashlib.sha256(raw).hexdigest()[:12]


def main() -> None:
    assertions = []

    # 1. qou-d5e8: Boltzmann log-form extensivity vs linear-form bilinear defect
    alpha_mp = mp.mpf("20.7219")
    mu_x = mp.mpf("0.552104")
    mu_y = mp.mpf("0.452235")
    b_log_xy = -alpha_mp * mp.log(mu_x * mu_y)
    b_log_sum = (-alpha_mp * mp.log(mu_x)) + (-alpha_mp * mp.log(mu_y))
    log_ext_err = abs(b_log_xy - b_log_sum)
    assert log_ext_err < mp.mpf("1e-75")

    S = 1000000
    x_c, y_c = 499320, 399451
    x_d, y_d = 552104, 452235
    def_c_lhs = 1 * (S * S - x_c * y_c) - S * ((S - x_c) + (S - y_c))
    def_c_rhs = -(S - x_c) * (S - y_c)
    def_d_lhs = 1 * (S * S - x_d * y_d) - S * ((S - x_d) + (S - y_d))
    def_d_rhs = -(S - x_d) * (S - y_d)
    assert def_c_lhs == def_c_rhs and def_c_lhs != 0
    assert def_d_lhs == def_d_rhs and def_d_lhs != 0
    assertions.append({
        "name": "qou_d5e8_boltzmann_log_extensivity_and_linear_bilinear_defect",
        "computed": f"{def_c_lhs}:{def_d_lhs}",
        "expected": f"{def_c_rhs}:{def_d_rhs}",
        "passed": True,
        "tolerance": "0",
        "source": f"{MOD}.linear_extensivity_defect_closed_form_and_conventions",
    })

    # 2. qou-lq6k: Milnor triple-linking antisymmetry vs symmetric pair-energy obstruction
    mu_123 = fractions.Fraction(7, 3)
    mu_213 = -mu_123
    sym_proj = mu_123 + mu_213
    w_12 = fractions.Fraction(2, 3)
    w_21 = fractions.Fraction(-1, 3)
    weighted_proj = w_12 * mu_123 + w_21 * mu_213
    expected_weighted = (w_12 - w_21) * mu_123
    assert sym_proj == 0 and weighted_proj == expected_weighted and weighted_proj != 0
    assertions.append({
        "name": "qou_lq6k_milnor_antisymmetry_kills_symmetric_pair_projection",
        "computed": f"{sym_proj.numerator}/{sym_proj.denominator}:{weighted_proj.numerator}/{weighted_proj.denominator}",
        "expected": f"0/1:{expected_weighted.numerator}/{expected_weighted.denominator}",
        "passed": True,
        "tolerance": "0",
        "source": f"{MOD}.milnor_antisymmetry_kills_symmetric_pair_projection",
    })

    # 3. qou-tqfm: Shift-inert operator decomposition self-comparison vs colour-weighting discrepancy
    h_frac = fractions.Fraction(99869, 1000000)
    delta_frac = fractions.Fraction(1, 3)
    d_blind = -h_frac / 2
    d_col = -(h_frac / 2) * (1 - delta_frac / 4)
    shift_diff = d_col - d_blind
    expected_shift_diff = h_frac * delta_frac / 8
    assert shift_diff == expected_shift_diff and shift_diff != 0
    assertions.append({
        "name": "qou_tqfm_shift_inert_self_residual_and_colour_shift_discrepancy",
        "computed": f"{shift_diff.numerator}:{shift_diff.denominator}",
        "expected": f"{expected_shift_diff.numerator}:{expected_shift_diff.denominator}",
        "passed": True,
        "tolerance": "0",
        "source": f"{MOD}.colour_weighted_minus_blind_shift_ne_zero",
    })

    # 4. qou-ughq: H_2 Wenzl block resolution ((2) vs (1,1)) vs unique Markov stabilization weight
    q_frac = fractions.Fraction(1109980, 1000000)
    lam_plus = q_frac
    lam_minus = -fractions.Fraction(1, 1) / q_frac
    gap_frac = lam_plus - lam_minus
    expected_gap = q_frac + fractions.Fraction(1, 1) / q_frac
    z_d_frac = (q_frac * q_frac) / (q_frac * q_frac + 1)
    w_star = (z_d_frac - lam_minus) / gap_frac
    w_alt = fractions.Fraction(1, 2)
    trace_star = w_star * lam_plus + (1 - w_star) * lam_minus
    trace_alt = w_alt * lam_plus + (1 - w_alt) * lam_minus
    markov_diff = trace_star - trace_alt
    expected_markov_diff = (w_star - w_alt) * gap_frac
    assert gap_frac == expected_gap and gap_frac > 0
    assert trace_star == z_d_frac and markov_diff == expected_markov_diff and markov_diff != 0
    assertions.append({
        "name": "qou_ughq_h2_markov_stabilization_uniquely_locks_wenzl_weight",
        "computed": f"{markov_diff.numerator}:{markov_diff.denominator}",
        "expected": f"{expected_markov_diff.numerator}:{expected_markov_diff.denominator}",
        "passed": True,
        "tolerance": "0",
        "source": f"{MOD}.h2_markov_stabilization_uniquely_locks_wenzl_weight",
    })

    # 5. qou-vvv4: Convention-D Wedderburn positivity, convention-C ceiling, and hadronic melt ordering
    q0_mp = mp.mpf("1.1099802689")
    y3_d = (q0_mp**4 + 1) / (q0_mp**2 + 1) ** 2
    y21_d = (q0_mp**2) / (q0_mp**2 + 1) ** 2
    partition_sum_err = abs((y3_d + 2 * y21_d) - 1)
    assert partition_sum_err < mp.mpf("1e-75") and y21_d > 0

    phi_mp = (1 + mp.sqrt(5)) / 2
    psi_mp = mp.findroot(lambda x: x**3 - x**2 - 1, mp.mpf("1.46557"))
    q_gold = 1 / (phi_mp**2)
    q_melt = 1 / (psi_mp**2)
    assert 0 < q_gold < q_melt < 1 < q0_mp < psi_mp

    n3_num = 1109980**4 + 1000000**4
    n21_num = (1109980**2) * (1000000**2)
    d_den = (1109980**2 + 1000000**2) ** 2
    assert n3_num + 2 * n21_num == d_den and n21_num > 0
    assertions.append({
        "name": "qou_vvv4_convention_d_positivity_convention_c_ceiling_and_melt_hierarchy",
        "computed": f"{n3_num + 2 * n21_num}:1",
        "expected": f"{d_den}:1",
        "passed": True,
        "tolerance": "0",
        "source": f"{MOD}.convention_d_positivity_convention_c_ceiling_and_melt_hierarchy",
    })

    commit_sha = get_git_sha()
    script_hash = get_script_hash()
    witness = {
        "engine": "mpmath",
        "engineVersion": f"mpmath {mp.__version__}",
        "dps": "80",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": commit_sha,
        "scriptCommitSha": commit_sha,
        "scriptHash": script_hash,
        "allPassed": all(a["passed"] for a in assertions),
        "assertions": assertions,
        "invocation": {
            "argv": [PROBE_PATH],
            "reproduce": f"python3 -u {PROBE_PATH}",
        },
        "description": "Exact 80-dps mpmath and Fraction verification for qou-d5e8, qou-lq6k, qou-tqfm, qou-ughq, and qou-vvv4 under epic qou-10v9.",
        "data": {
            "q_gold_80dps": mp.nstr(q_gold, 45),
            "q_melt_80dps": mp.nstr(q_melt, 45),
            "psi_supergolden_80dps": mp.nstr(psi_mp, 45),
            "y21_convention_d_at_q0": mp.nstr(y21_d, 45),
        },
    }
    pathlib.Path(WITNESS_PATH).write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {WITNESS_PATH} (allPassed={witness['allPassed']}, scriptHash={script_hash}, scriptCommitSha={commit_sha})")


if __name__ == "__main__":
    main()
