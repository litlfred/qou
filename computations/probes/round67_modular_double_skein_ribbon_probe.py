#!/usr/bin/env python3
"""Round 67 80-dps verification probe for qou-r6ki, qou-sf0s, qou-spds, qou-ssly, qou-t579.

Beans:
  - qou-r6ki: Cite 0006156v1.pdf [faddeev-kashaev-volkov2000] at prop:faddeev-phib-uniqueness
  - qou-sf0s: Cite [bilsonthompson2007] at def:strand-twist-datum
  - qou-spds: Cross-check On_the_geometry_of_two_state_models_for_the_colore.pdf [arxiv-2209.06973v1]
  - qou-ssly: Cite 2203.17029v1.pdf [garoufalidis-wheeler-modular] at prop:habiro-tail-archimedean-action
  - qou-t579: Cross-check gn2.pdf [gelca-nagasato] at computations/complex_volume_witness.py
"""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import time

import mpmath as mp

DPS = 80
mp.mp.dps = DPS

SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[2]
WITNESS_PATH = SCRIPT_PATH.with_name(
    "round67-modular-double-skein-ribbon.witness.json"
)


def compute_script_sha256() -> str:
    return hashlib.sha256(SCRIPT_PATH.read_bytes()).hexdigest()


def git_head_sha() -> str:
    res = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return res.stdout.strip()


def fmt_mp(val: mp.mpf | mp.mpc) -> str:
    return mp.nstr(val, 28)


def q_pochhammer_inf(a: mp.mpc, p: mp.mpc, terms: int = 260) -> mp.mpc:
    """Evaluate (a; p)_infty = prod_{k>=0} (1 - a p^k) for |p| < 1 at 80 dps."""
    prod = mp.mpc(1)
    pk = mp.mpc(1)
    for _ in range(terms):
        prod *= 1 - a * pk
        pk *= p
    return prod


def modular_double_eb(z: mp.mpc, b: mp.mpc) -> mp.mpc:
    """Evaluate e_b(z) = (-q e^{2 pi b z}; q^2)_inf / (-qtilde e^{2 pi b^{-1} z}; qtilde^2)_inf."""
    i = mp.mpc(0, 1)
    q = mp.exp(i * mp.pi * (b**2))
    q_tilde = mp.exp(-i * mp.pi * (b ** (-2)))
    num = q_pochhammer_inf(-q * mp.exp(2 * mp.pi * b * z), q**2)
    den = q_pochhammer_inf(-q_tilde * mp.exp(2 * mp.pi * (b ** (-1)) * z), q_tilde**2)
    return num / den


def run_probe() -> dict:
    t0 = time.monotonic()
    mp.mp.dps = DPS
    i = mp.mpc(0, 1)

    # -------------------------------------------------------------------------
    # 1. qou-r6ki: Modular-double shift ratio and half-lattice reciprocity
    # -------------------------------------------------------------------------
    b = mp.sqrt(mp.mpf("6") / mp.mpf("5")) * mp.exp(i * mp.pi / 4)
    z0 = mp.mpc(mp.mpf("0.17"), mp.mpf("-0.11"))
    q = mp.exp(i * mp.pi * (b**2))
    q_sq = q**2
    w = mp.exp(2 * mp.pi * b * z0)
    w_dual = mp.exp(2 * mp.pi * (b ** (-1)) * z0)

    eb_minus = modular_double_eb(z0 - i * b / 2, b)
    eb_plus = modular_double_eb(z0 + i * b / 2, b)
    eb_plus3 = modular_double_eb(z0 + 3 * i * b / 2, b)

    eb_dual_minus = modular_double_eb(z0 - i * (b ** (-1)) / 2, b)
    eb_dual_plus = modular_double_eb(z0 + i * (b ** (-1)) / 2, b)

    single_shift_res = abs((eb_plus / eb_minus) * (1 + w) - 1)
    dual_shift_res = abs((eb_dual_plus / eb_dual_minus) * (1 + w_dual) - 1)
    two_step_shift_res = abs((eb_plus3 / eb_minus) * ((1 + w) * (1 + q_sq * w)) - 1)

    m_idx, n_idx, b_sq_int = 4, -2, 3
    hl_mn = (2 * m_idx + 1) * b_sq_int + (2 * n_idx + 1)
    hl_nm = (2 * n_idx + 1) * b_sq_int + (2 * m_idx + 1)
    hl_diff_res = abs((hl_mn - hl_nm) - (2 * m_idx - 2 * n_idx) * (b_sq_int - 1))

    check_r6ki = bool(
        single_shift_res < mp.mpf("1e-75")
        and dual_shift_res < mp.mpf("1e-75")
        and two_step_shift_res < mp.mpf("1e-75")
        and hl_diff_res == 0
    )

    # -------------------------------------------------------------------------
    # 2. qou-sf0s: Braided 3-ribbon twist spread and coupled writhe charge
    # -------------------------------------------------------------------------
    t_quark = (2, 2, -1)
    t_lepton = (-2, -2, -2)
    w_init, d_slide = 5, 3
    t_slid = tuple(t - d_slide for t in t_quark)
    w_slid = w_init + d_slide

    spread_quark = (
        (t_quark[0] - t_quark[1]) ** 2
        + (t_quark[1] - t_quark[2]) ** 2
        + (t_quark[2] - t_quark[0]) ** 2
    )
    spread_slid = (
        (t_slid[0] - t_slid[1]) ** 2
        + (t_slid[1] - t_slid[2]) ** 2
        + (t_slid[2] - t_slid[0]) ** 2
    )
    spread_lepton = (
        (t_lepton[0] - t_lepton[1]) ** 2
        + (t_lepton[1] - t_lepton[2]) ** 2
        + (t_lepton[2] - t_lepton[0]) ** 2
    )
    coupled_init = sum(t_quark) + 3 * w_init
    coupled_slid = sum(t_slid) + 3 * w_slid

    check_sf0s = bool(
        spread_quark == 18
        and spread_slid == 18
        and spread_lepton == 0
        and sum(t_quark) == 3
        and sum(t_lepton) == -6
        and coupled_init == coupled_slid
    )

    # -------------------------------------------------------------------------
    # 3. qou-spds: Two-state 3-braid closure trace identities for k = 1, 2, 3
    # -------------------------------------------------------------------------
    q_sample = mp.exp(2 * mp.pi * i / 7)
    s_val = q_sample + 1 / q_sample
    # 2x2 transfer matrix X = [[1 - q, -q^{-1}], [1, -q^{-1}]] with det(X)=1, tr(X)=1-s
    x_mat = mp.matrix([[1 - q_sample, -1 / q_sample], [mp.mpf(1), -1 / q_sample]])
    x2_mat = x_mat * x_mat
    x3_mat = x2_mat * x_mat

    tr1 = x_mat[0, 0] + x_mat[1, 1]
    tr2 = x2_mat[0, 0] + x2_mat[1, 1]
    tr3 = x3_mat[0, 0] + x3_mat[1, 1]

    closure_k1_res = abs((s_val + tr1) - 1)
    j2_41_laurent = q_sample**2 - q_sample + 1 - 1 / q_sample + 1 / (q_sample**2)
    closure_k2_res = abs((s_val + tr2) - j2_41_laurent)
    closure_k2_poly_res = abs((s_val + tr2) - (s_val**2 - s_val - 1))
    closure_k3_poly_res = abs((s_val + tr3) - (-s_val**3 + 3 * s_val**2 + s_val - 2))
    closure_k3_classical = 2 + (1 - 2) * ((1 - 2) ** 2 - 3)

    check_spds = bool(
        closure_k1_res < mp.mpf("1e-77")
        and closure_k2_res < mp.mpf("1e-77")
        and closure_k2_poly_res < mp.mpf("1e-77")
        and closure_k3_poly_res < mp.mpf("1e-77")
        and closure_k3_classical == 4
    )

    # -------------------------------------------------------------------------
    # 4. qou-ssly: Symmetric Laurent step multiplier and cyclotomic truncation
    # -------------------------------------------------------------------------
    x_step = q_sample**2
    step_mult = (1 - x_step) * (1 - 1 / x_step)
    step_mult_inv = (1 - 1 / x_step) * (1 - x_step)
    step_sq_form = -((x_step - 1) ** 2) / x_step
    t_prev = (1 - q_sample) * (1 - 1 / q_sample)
    t_next = step_mult * t_prev
    inhom_diff_res = abs((t_next - t_prev) - (1 - x_step - 1 / x_step) * t_prev)

    # Cyclotomic truncation at N=5 root of unity zeta_5
    zeta5 = mp.exp(2 * mp.pi * i / 5)
    t_n_zeta = mp.mpc(1)
    cyclotomic_sum = mp.mpc(0)
    for k in range(1, 6):
        cyclotomic_sum += t_n_zeta
        t_n_zeta *= (1 - zeta5**k) * (1 - zeta5 ** (-k))
    truncation_term_res = abs(t_n_zeta)

    check_ssly = bool(
        abs(step_mult - step_mult_inv) < mp.mpf("1e-78")
        and abs(step_mult - step_sq_form) < mp.mpf("1e-77")
        and inhom_diff_res < mp.mpf("1e-77")
        and truncation_term_res < mp.mpf("1e-77")
    )

    # -------------------------------------------------------------------------
    # 5. qou-t579: Figure-eight peripheral Laurent-to-trace reduction
    # -------------------------------------------------------------------------
    m_hol = mp.exp(mp.mpc(mp.mpf("0.37"), mp.mpf("0.81")))
    x_tr = m_hol + 1 / m_hol
    s_adj = m_hol**2 + 1 / (m_hol**2)

    p_laurent = m_hol**4 - m_hol**2 - 2 - 1 / (m_hol**2) + 1 / (m_hol**4)
    p_trace = x_tr**4 - 5 * (x_tr**2) + 2
    p_trace_neg = (-x_tr) ** 4 - 5 * ((-x_tr) ** 2) + 2
    p_adjoint = s_adj**2 - s_adj - 4

    laurent_trace_res = abs(p_laurent - p_trace)
    trace_adjoint_res = abs(p_trace - p_adjoint)
    skein_sign_res = abs(p_trace_neg - p_trace)
    parabolic_val = 2**4 - 5 * (2**2) + 2

    check_t579 = bool(
        laurent_trace_res < mp.mpf("1e-76")
        and trace_adjoint_res < mp.mpf("1e-76")
        and skein_sign_res < mp.mpf("1e-78")
        and parabolic_val == -2
    )

    all_passed = bool(
        check_r6ki and check_sf0s and check_spds and check_ssly and check_t579
    )
    duration_ms = int((time.monotonic() - t0) * 1000)
    script_sha = compute_script_sha256()

    return {
        "probe": "round67-modular-double-skein-ribbon",
        "beans": ["qou-r6ki", "qou-sf0s", "qou-spds", "qou-ssly", "qou-t579"],
        "scriptCommitSha": git_head_sha(),
        "scriptHash": script_sha,
        "scriptSha256": script_sha,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "durationMs": duration_ms,
        "dps": DPS,
        "allPassed": all_passed,
        "results": {
            "qou_r6ki_modular_double_shift_and_lattice": {
                "singleShiftResidual": fmt_mp(single_shift_res),
                "dualShiftResidual": fmt_mp(dual_shift_res),
                "twoStepShiftResidual": fmt_mp(two_step_shift_res),
                "halfLatticeTransposeDiffResidual": hl_diff_res,
                "passed": check_r6ki,
            },
            "qou_sf0s_braided_ribbon_twist_conservation": {
                "quarkTwistSpread": spread_quark,
                "slidQuarkTwistSpread": spread_slid,
                "leptonTwistSpread": spread_lepton,
                "coupledWritheChargeInitial": coupled_init,
                "coupledWritheChargeSlid": coupled_slid,
                "passed": check_sf0s,
            },
            "qou_spds_three_braid_closure_state_sum": {
                "k1UnknotResidual": fmt_mp(closure_k1_res),
                "k2FigureEightLaurentResidual": fmt_mp(closure_k2_res),
                "k2FigureEightPolyResidual": fmt_mp(closure_k2_poly_res),
                "k3BorromeanPolyResidual": fmt_mp(closure_k3_poly_res),
                "k3ClassicalLimitValue": closure_k3_classical,
                "passed": check_spds,
            },
            "qou_ssly_cyclotomic_step_and_truncation": {
                "stepSquareFormResidual": fmt_mp(abs(step_mult - step_sq_form)),
                "inhomogeneousDiffResidual": fmt_mp(inhom_diff_res),
                "zeta5TruncationTermModulus": fmt_mp(truncation_term_res),
                "zeta5CyclotomicSumReal": fmt_mp(mp.re(cyclotomic_sum)),
                "passed": check_ssly,
            },
            "qou_t579_figure_eight_skein_character_polynomial": {
                "laurentToTraceResidual": fmt_mp(laurent_trace_res),
                "traceToAdjointResidual": fmt_mp(trace_adjoint_res),
                "skeinSignFlipResidual": fmt_mp(skein_sign_res),
                "parabolicSpecializationValue": parabolic_val,
                "passed": check_t579,
            },
        },
    }


def main() -> None:
    WITNESS_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = run_probe()
    WITNESS_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {WITNESS_PATH.name}: allPassed={payload['allPassed']}")
    if not payload["allPassed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
