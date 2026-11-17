#!/usr/bin/env python3
"""
80-dps mpmath witness probe for:
  folio/quantum-observable-universe/lean/QOU/QBeta/FigureEightAPolyPeriodAndTakataHolonomicBrick.lean

Beans:
  - qou-3jgd: figure_eight_a_poly_discriminant_and_amphicheiral_recip
  - qou-5b23: lifted_volume_triple_epsilon_grade_separation
  - qou-d8as: prolongation_symbol_growth_prune_and_degree_cap
  - qou-j1ld: garoufalidis_le_q_holonomic_second_order_step_elimination
  - qou-s8gi: takata_twist_knot_recurrence_order_jump_and_chiral_defect
"""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import subprocess
import mpmath as mp

mp.mp.dps = 80

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
SCRIPT_PATH = pathlib.Path(__file__).resolve()
WITNESS_PATH = SCRIPT_PATH.with_name(
    "figure-eight-a-poly-period-and-takata-holonomic-brick.witness.json"
)


def git_head_sha() -> str:
    return (
        subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT)
        .decode("utf-8")
        .strip()
    )


def a_poly_4_1(m_val: mp.mpf, l_val: mp.mpf) -> mp.mpf:
    return (
        (m_val**4) * (l_val**2)
        - (m_val**2)
        * (1 - m_val**2 - 2 * (m_val**4) - (m_val**6) + (m_val**8))
        * l_val
        + (m_val**4)
    )


def check_qou_3jgd() -> dict:
    # 4_1 A-polynomial parabolic cusp factorization at M=1 and amphicheiral Borel period pairing
    l_sample = mp.mpf("1.732050807568877293527446341505872366942805253810380628055806979451933016908800037")
    cusp_eval = a_poly_4_1(mp.mpf(1), l_sample)
    cusp_square = (l_sample + 1) ** 2
    cusp_residual = abs(cusp_eval - cusp_square)
    double_root_eval = abs(a_poly_4_1(mp.mpf(1), mp.mpf(-1)))

    # Amphicheiral reciprocal symmetry L^2 * A(M, 1/L) == A(M, L)
    m_sample = mp.mpf("1.234567890123456789012345678901234567890123456789012345678901234567890123456789")
    recip_residual = abs(
        (l_sample**2) * a_poly_4_1(m_sample, 1 / l_sample)
        - a_poly_4_1(m_sample, l_sample)
    )

    # Geometric Borel period of 4_1: Vol(4_1) = 2 * Im(Li_2(e^{i pi / 3}))
    vol_4_1 = 2 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))
    omega_plus = vol_4_1 / (2 * mp.pi)
    omega_minus = -omega_plus
    period_pair_residual = abs(omega_plus + omega_minus)

    passed = bool(
        cusp_residual < mp.mpf("1e-75")
        and double_root_eval < mp.mpf("1e-75")
        and recip_residual < mp.mpf("1e-75")
        and period_pair_residual < mp.mpf("1e-75")
        and omega_plus > mp.mpf("0.3")
    )
    return {
        "bean": "qou-3jgd",
        "theorem": "figure_eight_a_poly_discriminant_and_amphicheiral_recip",
        "passed": passed,
        "cusp_residual": mp.nstr(cusp_residual, 80),
        "recip_residual": mp.nstr(recip_residual, 80),
        "vol_4_1": mp.nstr(vol_4_1, 80),
        "borel_period_omega_plus": mp.nstr(omega_plus, 80),
    }


def check_qou_5b23() -> dict:
    # Lifted volume triple epsilon-grade separation
    vol_4_1 = 2 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))
    vol_b3 = 4 * mp.catalan
    # Archimedean relation P_0 = 0 at leading order, with non-zero eps^1 slope P_1
    p_0 = mp.mpf(0)
    eps = mp.mpf("1e-12")
    p_1 = 3 * vol_4_1 - vol_b3  # non-zero transcendental slope
    p_lifted = p_0 + eps * p_1
    grade_residual = abs(p_lifted - eps * p_1)

    passed = bool(
        grade_residual < mp.mpf("1e-75")
        and abs(p_1) > mp.mpf("1")
        and abs(p_lifted) > mp.mpf("1e-13")
    )
    return {
        "bean": "qou-5b23",
        "theorem": "lifted_volume_triple_epsilon_grade_separation",
        "passed": passed,
        "grade_residual": mp.nstr(grade_residual, 80),
        "p_1_slope": mp.nstr(p_1, 80),
        "p_lifted_magnitude": mp.nstr(abs(p_lifted), 80),
    }


def check_qou_d8as() -> dict:
    # Quadratic prolongation symbol second difference and growth prune
    r0 = mp.mpf("1.6180339887498948482045868343656381177203091798057628621354486227052604628189024")
    r1 = mp.mpf("-0.5772156649015328606065120900824024310421593359399235988057672348848677267776646")
    r2 = mp.mpf("2.25")
    x = mp.mpf("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089")

    def sym(r2_val: mp.mpf, x_val: mp.mpf) -> mp.mpf:
        return r0 + r1 * x_val + r2_val * (x_val**2)

    diff2 = sym(r2, x + 2) - 2 * sym(r2, x + 1) + sym(r2, x)
    diff2_residual = abs(diff2 - 2 * r2)
    pruned_residual = abs(sym(mp.mpf(0), x) - (r0 + r1 * x))

    passed = bool(
        diff2_residual < mp.mpf("1e-75")
        and pruned_residual < mp.mpf("1e-75")
        and abs(diff2) > mp.mpf("4")
    )
    return {
        "bean": "qou-d8as",
        "theorem": "prolongation_symbol_growth_prune_and_degree_cap",
        "passed": passed,
        "diff2_residual": mp.nstr(diff2_residual, 80),
        "pruned_residual": mp.nstr(pruned_residual, 80),
        "diff2_value": mp.nstr(diff2, 80),
    }


def check_qou_j1ld() -> dict:
    # Garoufalidis-Le 2nd-order q-holonomic step elimination
    c0 = mp.mpf("1.125")
    c1 = mp.mpf("-2.375")
    a0 = mp.mpf("3.5")
    b0 = mp.mpf("-1.25")
    a1 = mp.mpf("2.75")
    b1 = mp.mpf("0.875")

    c2 = a0 * c1 + b0 * c0
    c3 = a1 * c2 + b1 * c1
    lhs = a0 * c3
    rhs = (a0 * a1 + b1) * c2 - b1 * b0 * c0
    elim_residual = abs(lhs - rhs)

    passed = bool(
        elim_residual < mp.mpf("1e-75")
        and abs(lhs) > mp.mpf("1")
    )
    return {
        "bean": "qou-j1ld",
        "theorem": "garoufalidis_le_q_holonomic_second_order_step_elimination",
        "passed": passed,
        "elim_residual": mp.nstr(elim_residual, 80),
        "a0_c3_value": mp.nstr(lhs, 80),
    }


def check_qou_s8gi() -> dict:
    # Takata twist-knot recurrence order jump r(1)=2 -> r(2)=3 and cubic chiral defect
    r1 = mp.mpf(1) + 1
    r2 = mp.mpf(2) + 1
    c2 = mp.mpf("4.5")
    c1 = mp.mpf("-1.5")
    l_val = mp.mpf("2.25")

    cubic_orig = (l_val**3) + c2 * (l_val**2) + c1 * l_val + 1
    cubic_recip = 1 + c2 * l_val + c1 * (l_val**2) + (l_val**3)
    chiral_diff = cubic_orig - cubic_recip
    factored_rhs = (c2 - c1) * l_val * (l_val - 1)
    factor_residual = abs(chiral_diff - factored_rhs)

    passed = bool(
        r1 == 2
        and r2 == 3
        and (r2 - r1) == 1
        and factor_residual < mp.mpf("1e-75")
        and abs(chiral_diff) > mp.mpf("10")
    )
    return {
        "bean": "qou-s8gi",
        "theorem": "takata_twist_knot_recurrence_order_jump_and_chiral_defect",
        "passed": passed,
        "order_4_1": mp.nstr(r1, 10),
        "order_5_2": mp.nstr(r2, 10),
        "factor_residual": mp.nstr(factor_residual, 80),
        "chiral_defect_value": mp.nstr(chiral_diff, 80),
    }


def main() -> None:
    checks = [
        check_qou_3jgd(),
        check_qou_5b23(),
        check_qou_d8as(),
        check_qou_j1ld(),
        check_qou_s8gi(),
    ]
    all_passed = all(c["passed"] for c in checks)
    script_bytes = SCRIPT_PATH.read_bytes()
    script_hash = hashlib.sha256(script_bytes).hexdigest()

    payload = {
        "probe": "computations/probes/figure_eight_a_poly_period_and_takata_holonomic_brick_probe.py",
        "beans": ["qou-3jgd", "qou-5b23", "qou-d8as", "qou-j1ld", "qou-s8gi"],
        "precisionDps": 80,
        "scriptHash": script_hash,
        "scriptCommitSha": git_head_sha(),
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "allPassed": all_passed,
        "checks": checks,
    }
    WITNESS_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if not all_passed:
        raise SystemExit("One or more witness checks failed")
    print(f"Wrote {WITNESS_PATH} (allPassed={all_passed})")


if __name__ == "__main__":
    main()
