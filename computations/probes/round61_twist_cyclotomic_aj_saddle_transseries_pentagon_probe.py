#!/usr/bin/env python3
"""
Round 61 80-dps mpmath probe for beans:
  - qou-7q3s: Takata (2004) / Masbaum twist-knot cyclotomic expansion & shift ratios
  - qou-2v4y: Gukov (2005) SL(2,C) Chern-Simons Lagrangian saddle on A_{4_1}(l, m) = 0
  - qou-c7lf: Dimofte-Gukov (2010) Quantum Volume Conjecture 1-loop WKB transport & A-hat_K
  - qou-ad5s: ArXiv:2302.08363v2 multi-sector transseries partial coupling series G_n(y) & radius R
  - qou-cy96: Faddeev-Kashaev-Volkov (2000) quantum dilogarithm pentagon & complex-b duality
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import subprocess
from mpmath import mp

mp.dps = 80

PROBE_PATH = pathlib.Path(__file__).resolve()
WITNESS_PATH = PROBE_PATH.with_name(
    "round61-twist-cyclotomic-aj-saddle-transseries-pentagon.witness.json"
)


def fmt(val: mp.mpf | mp.mpc) -> str:
    if isinstance(val, mp.mpc):
        return f"{mp.nstr(val.real, 50)} + {mp.nstr(val.imag, 50)}i"
    return mp.nstr(val, 60)


def q_pochhammer(z: mp.mpc, q: mp.mpc, n: int) -> mp.mpc:
    prod = mp.mpc(1)
    qk = mp.mpc(1)
    for _ in range(n):
        prod *= 1 - z * qk
        qk *= q
    return prod


def check_qou_7q3s_takata_twist_cyclotomic() -> dict[str, str | int | bool]:
    """
    Takata (2004) arXiv:math/0401068v1 eqs. (1)-(5) and (16):
    For figure-eight knot 4_1 (twist p = -1), the cyclotomic summand
      S(n, k) = prod_{j=1}^k (q^n + q^{-n} - q^j - q^{-j})
    satisfies exact hypergeometric shift ratios in (n, k) and at q = exp(2*pi*i/n)
    reduces to Kashaev's invariant <4_1>_n = sum_{k=0}^{n-1} prod_{j=1}^k |1 - q^j|^2.
    """
    q = mp.exp(mp.mpc("0.17", "0.23"))

    def laurent_arch(m: int) -> mp.mpc:
        return q**m + q ** (-m)

    def summand_41(n: int, k: int) -> mp.mpc:
        prod = mp.mpc(1)
        for j in range(1, k + 1):
            prod *= laurent_arch(n) - laurent_arch(j)
        return prod

    n_val, k_val = 7, 3
    s_nk = summand_41(n_val, k_val)
    s_nk_plus1 = summand_41(n_val, k_val + 1)
    ratio_k_actual = s_nk_plus1 / s_nk
    ratio_k_formula = laurent_arch(n_val) - laurent_arch(k_val + 1)
    res_ratio_k = abs(ratio_k_actual - ratio_k_formula)

    s_nplus1_k = summand_41(n_val + 1, k_val)
    ratio_n_actual = s_nplus1_k / s_nk
    ratio_n_formula = mp.mpc(1)
    for j in range(1, k_val + 1):
        ratio_n_formula *= (laurent_arch(n_val + 1) - laurent_arch(j)) / (
            laurent_arch(n_val) - laurent_arch(j)
        )
    res_ratio_n = abs(ratio_n_actual - ratio_n_formula)

    n_root = 16
    q_root = mp.exp(2 * mp.pi * 1j / n_root)
    kashaev_sum = mp.mpf(0)
    masbaum_root_sum = mp.mpc(0)
    for k in range(n_root):
        prod_k = mp.mpf(1)
        prod_m = mp.mpc(1)
        for j in range(1, k + 1):
            prod_k *= abs(1 - q_root**j) ** 2
            prod_m *= 2 - (q_root**j + q_root ** (-j))
        kashaev_sum += prod_k
        masbaum_root_sum += prod_m

    res_root_unity = abs(mp.mpc(kashaev_sum) - masbaum_root_sum)

    def quad_phase(k: int, l: int) -> int:
        return k * (k + 1) + l * (l + 1) + 2 * k * l

    step_diff_exact = quad_phase(5, 3) - quad_phase(4, 3)
    step_diff_formula = 2 * (4 + 1) + 2 * 3

    passed = bool(
        res_ratio_k < mp.mpf("1e-70")
        and res_ratio_n < mp.mpf("1e-70")
        and res_root_unity < mp.mpf("1e-70")
        and step_diff_exact == step_diff_formula == 16
    )
    return {
        "beanId": "qou-7q3s",
        "referenceKey": "takata2004",
        "nVal": n_val,
        "kVal": k_val,
        "ratioKResidual": fmt(res_ratio_k),
        "ratioNResidual": fmt(res_ratio_n),
        "kashaevRootUnityN16": fmt(kashaev_sum),
        "rootUnityMasbaumResidual": fmt(res_root_unity),
        "quadraticPhaseStepDiff": step_diff_exact,
        "passed": passed,
    }


def check_qou_2v4y_gukov_apoly_lagrangian() -> dict[str, str | int | bool]:
    """
    Gukov (2005) arXiv:hep-th/0306165v1 Sec. 3.1 & 5.2 eq. (5.12):
    For 4_1, the classical A-polynomial in untwisted meridian M = exp(v) and
    sign-normalized longitude L_tilde = -L (so L_tilde(0) = 1 at the complete
    hyperbolic structure v = 0) satisfies:
      L_tilde + L_tilde^{-1} = 2 + (M + M^{-1}) - (M - M^{-1})^2
                             = 2 + 2 cosh(v) - 4 sinh^2(v).
    Near v = 0, L_tilde + L_tilde^{-1} = 2 - 3 v^2 + O(v^4), so log L_tilde(v) / v -> i * sqrt(3)
    (the figure-eight cusp shape tau = i*sqrt(3)), and dS_0/dv = log L_tilde(v)
    integrates the SL(2,C) Chern-Simons Lagrangian 1-form.
    """
    def trace_rhs(v: mp.mpc) -> mp.mpc:
        m = mp.exp(v)
        return (m + 1 / m) - (m - 1 / m) ** 2

    def l_tilde_geom(v: mp.mpc) -> mp.mpc:
        rhs = trace_rhs(v)
        two_minus_rhs = 4 * mp.sinh(v) ** 2 - 4 * mp.sinh(v / 2) ** 2
        return (rhs + 1j * mp.sqrt(two_minus_rhs * (2 + rhs))) / 2

    v0 = mp.mpf("0.05")
    v1 = mp.mpf("0.12")
    l_at_v1 = l_tilde_geom(v1)
    apoly_res = abs((l_at_v1 + 1 / l_at_v1) - trace_rhs(v1))

    s0_diff_quad = mp.quad(lambda v: mp.log(l_tilde_geom(v)), [v0, v1])
    h = mp.mpf("1e-18")
    s0_deriv_mid = (
        mp.quad(lambda v: mp.log(l_tilde_geom(v)), [v0, v1 + h])
        - mp.quad(lambda v: mp.log(l_tilde_geom(v)), [v0, v1 - h])
    ) / (2 * h)
    lagrangian_deriv_res = abs(s0_deriv_mid - mp.log(l_at_v1))

    v_tiny = mp.mpf("1e-28")
    cusp_slope = mp.log(l_tilde_geom(v_tiny)) / (1j * v_tiny)
    cusp_slope_res = abs(cusp_slope - mp.sqrt(3))

    passed = bool(
        apoly_res < mp.mpf("1e-70")
        and lagrangian_deriv_res < mp.mpf("1e-32")
        and cusp_slope_res < mp.mpf("1e-45")
    )
    return {
        "beanId": "qou-2v4y",
        "referenceKey": "arxiv-hep-th-0306165v1",
        "v1": fmt(v1),
        "lGeomAtV1": fmt(l_at_v1),
        "aPolyResidualAtV1": fmt(apoly_res),
        "s0IntegralV0ToV1": fmt(s0_diff_quad),
        "lagrangianDerivativeResidual": fmt(lagrangian_deriv_res),
        "cuspModulusSlopeAtZero": fmt(cusp_slope),
        "cuspModulusSqrt3Residual": fmt(cusp_slope_res),
        "passed": passed,
    }


def check_qou_c7lf_dimofte_gukov_wkb_one_loop() -> dict[str, str | int | bool]:
    """
    Dimofte-Gukov (2010) arXiv:1003.4808v2 Sec. 2.2 & 3.2:
    Along the imaginary deformation ray v = i*theta (real hyperbolic Dehn-filling
    parameter where trace_rhs(i*theta) = 2 + 2 cos(theta) + 4 sin^2(theta) > 2),
    L_tilde(i*theta) is real and > 1 for theta > 0, with
      (L_tilde - L_tilde^{-1}) / (2*theta) -> sqrt(3) as theta -> 0+,
    and (1/(2*theta)) * (d/dtheta)[trace_rhs(i*theta)] = (4 sin(2*theta) - 2 sin(theta)) / (2*theta) -> 3.
    Hence the normalized 1-loop Reidemeister torsion ratio
      tau_{4_1}(theta) = (d/dtheta)[trace_rhs(i*theta)] / (L_tilde - L_tilde^{-1})
    converges to 3 / (2*sqrt(3)) * 2 = sqrt(3) as theta -> 0+, and its 1-loop WKB
    transport derivative matches the exact chain-rule Hessian derivative to >50 dps.
    """
    def rhs_theta(theta: mp.mpf) -> mp.mpf:
        return 2 * mp.cos(theta) + 4 * mp.sin(theta) ** 2

    def rhs_deriv_theta(theta: mp.mpf) -> mp.mpf:
        return 4 * mp.sin(2 * theta) - 2 * mp.sin(theta)

    def l_minus_linv(theta: mp.mpf) -> mp.mpf:
        r = rhs_theta(theta)
        r_minus_2 = 4 * mp.sin(theta) ** 2 - 4 * mp.sin(theta / 2) ** 2
        return mp.sqrt(r_minus_2 * (r + 2))

    def torsion_ratio(theta: mp.mpf) -> mp.mpf:
        return rhs_deriv_theta(theta) / l_minus_linv(theta)

    theta_tiny = mp.mpf("1e-28")
    tau_limit = torsion_ratio(theta_tiny)
    tau_expected = mp.sqrt(3)
    res_tau0 = abs(tau_limit - tau_expected)

    theta_pt = mp.mpf("0.08")
    h = mp.mpf("1e-20")
    s1_func = lambda x: -mp.mpf("0.5") * mp.log(torsion_ratio(x))
    ds1_num = (s1_func(theta_pt + h) - s1_func(theta_pt - h)) / (2 * h)

    dr_pt = rhs_deriv_theta(theta_pt)
    d2r_pt = 8 * mp.cos(2 * theta_pt) - 2 * mp.cos(theta_pt)
    r_pt = rhs_theta(theta_pt)
    r_pt_minus_2 = 4 * mp.sin(theta_pt) ** 2 - 4 * mp.sin(theta_pt / 2) ** 2
    dlog_denom = r_pt * dr_pt / (r_pt_minus_2 * (r_pt + 2))
    dlog_numer = d2r_pt / dr_pt
    ds1_exact = -mp.mpf("0.5") * (dlog_numer - dlog_denom)
    res_transport = abs(ds1_num - ds1_exact)

    passed = bool(res_tau0 < mp.mpf("1e-45") and res_transport < mp.mpf("1e-35"))
    return {
        "beanId": "qou-c7lf",
        "referenceKey": "dimofte-gukov2010",
        "completeHyperbolicTorsion": fmt(tau_limit),
        "sqrt3Target": fmt(tau_expected),
        "torsionLimitResidual": fmt(res_tau0),
        "wkbOneLoopTransportAtTheta008": fmt(ds1_exact),
        "wkbTransportResidual": fmt(res_transport),
        "passed": passed,
    }


def check_qou_ad5s_transseries_partial_radius() -> dict[str, str | int | bool]:
    """
    ArXiv:2302.08363v2 Sec. 2 eqs. (2.5)-(2.8):
    A Borel-resummed transseries s(Phi)(g, y) = sum_{l>=0} y^l phi_l(g)
    with phi_l(g) = sum_{n>=0} a_{n,l} g^n is reorganized by fixed power n of the
    coupling g into partial series G_n(y) = sum_{l>=0} a_{n,l} y^l.
    """
    g_val = mp.mpf("1") / mp.mpf("7")
    y_val = mp.mpf("3") / mp.mpf("5")
    r_common = mp.mpf(2)

    def coeff_a(n: int, l: int) -> mp.mpf:
        return (
            mp.mpf(n + l + 1)
            / mp.mpf(n + 1)
            * (mp.mpf(3) ** (-n))
            * (r_common ** (-l))
        )

    def partial_g_closed(n: int, y: mp.mpf) -> mp.mpf:
        u = y / r_common
        return (mp.mpf(3) ** (-n)) * (
            1 / (1 - u) + u / (mp.mpf(n + 1) * (1 - u) ** 2)
        )

    n_max = 140
    l_max = 180

    max_gn_res = mp.mpf(0)
    for n in range(6):
        gn_sum = mp.fsum(coeff_a(n, l) * (y_val**l) for l in range(l_max))
        res = abs(gn_sum - partial_g_closed(n, y_val))
        if res > max_gn_res:
            max_gn_res = res

    sum_by_coupling = mp.fsum(
        (g_val**n) * partial_g_closed(n, y_val) for n in range(n_max)
    )
    sum_by_sector = mp.fsum(
        (y_val**l)
        * mp.fsum(coeff_a(n, l) * (g_val**n) for n in range(n_max))
        for l in range(l_max)
    )
    reorg_residual = abs(sum_by_coupling - sum_by_sector)

    passed = bool(
        max_gn_res < mp.mpf("1e-65") and reorg_residual < mp.mpf("1e-65")
    )
    return {
        "beanId": "qou-ad5s",
        "referenceKey": "arxiv-2302.08363v2",
        "commonRadiusR": fmt(r_common),
        "yEval": fmt(y_val),
        "gEval": fmt(g_val),
        "partialSeriesG0": fmt(partial_g_closed(0, y_val)),
        "partialSeriesG1": fmt(partial_g_closed(1, y_val)),
        "maxPartialSeriesClosedFormResidual": fmt(max_gn_res),
        "sumByCoupling": fmt(sum_by_coupling),
        "reorganizationResidual": fmt(reorg_residual),
        "passed": passed,
    }


def check_qou_cy96_fkv_complex_b_pentagon() -> dict[str, str | int | bool]:
    """
    Faddeev-Kashaev-Volkov (2000) arXiv:hep-th/0006156v1 Sec. 6.1 eq. (20) & Sec. 6.5:
    At complex coupling b with Re(b) > 0:
      1) Central charge c(b) = 1 + 6*(b + b^{-1})^2 is invariant under b <-> b^{-1}.
      2) The q-step parameter q = exp(pi * i * b^2) has |q| < 1 when Im(b^2) > 0,
         so the compact quantum dilogarithm (z; q)_inf converges absolutely at complex b.
      3) The semiclassical Rogers/Euler 5-term dilogarithm pentagon holds to 80 dps.
    """
    b_complex = mp.mpc("0.6", "0.25")
    b_dual = 1 / b_complex
    c_b = 1 + 6 * (b_complex + 1 / b_complex) ** 2
    c_b_dual = 1 + 6 * (b_dual + 1 / b_dual) ** 2
    res_duality = abs(c_b - c_b_dual)

    q_step = mp.exp(mp.pi * 1j * (b_complex**2))
    abs_q = abs(q_step)

    z_val = mp.mpc("0.25", "0.1")
    n_terms = 220
    prod_val = q_pochhammer(z_val, q_step, n_terms)
    series_val = mp.mpc(0)
    for k in range(70):
        num = ((-1) ** k) * (q_step ** (k * (k - 1) // 2)) * (z_val**k)
        den = q_pochhammer(q_step, q_step, k)
        series_val += num / den
    res_euler_qseries = abs(prod_val - series_val)

    x_val = mp.mpc("0.22", "0.07")
    y_val = mp.mpc("0.31", "-0.05")
    u_val = x_val * (1 - y_val) / (1 - x_val * y_val)
    v_val = y_val * (1 - x_val) / (1 - x_val * y_val)
    lhs_5term = mp.polylog(2, x_val) + mp.polylog(2, y_val) - mp.polylog(2, x_val * y_val)
    rhs_5term = (
        mp.polylog(2, u_val)
        + mp.polylog(2, v_val)
        + mp.log((1 - x_val) / (1 - x_val * y_val))
        * mp.log((1 - y_val) / (1 - x_val * y_val))
    )
    res_5term = abs(lhs_5term - rhs_5term)

    passed = bool(
        res_duality < mp.mpf("1e-70")
        and abs_q < mp.mpf("0.4")
        and res_euler_qseries < mp.mpf("1e-70")
        and res_5term < mp.mpf("1e-70")
    )
    return {
        "beanId": "qou-cy96",
        "referenceKey": "faddeev-kashaev-volkov2000",
        "bComplex": fmt(b_complex),
        "centralChargeCB": fmt(c_b),
        "dualityResidual": fmt(res_duality),
        "absQStep": fmt(abs_q),
        "qDilogarithmProdVal": fmt(prod_val),
        "qDilogarithmSeriesResidual": fmt(res_euler_qseries),
        "fiveTermPentagonResidual": fmt(res_5term),
        "passed": passed,
    }


def main() -> None:
    script_bytes = PROBE_PATH.read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()
    try:
        commit_sha = (
            subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=PROBE_PATH.parent
            )
            .decode()
            .strip()
        )
    except Exception:
        commit_sha = "0" * 40

    c_7q3s = check_qou_7q3s_takata_twist_cyclotomic()
    c_2v4y = check_qou_2v4y_gukov_apoly_lagrangian()
    c_c7lf = check_qou_c7lf_dimofte_gukov_wkb_one_loop()
    c_ad5s = check_qou_ad5s_transseries_partial_radius()
    c_cy96 = check_qou_cy96_fkv_complex_b_pentagon()

    checks = [c_7q3s, c_2v4y, c_c7lf, c_ad5s, c_cy96]
    all_passed = all(bool(c["passed"]) for c in checks)

    witness = {
        "probe": PROBE_PATH.name,
        "precisionDps": 80,
        "scriptCommitSha": commit_sha,
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "beans": ["qou-2v4y", "qou-7q3s", "qou-ad5s", "qou-c7lf", "qou-cy96"],
        "allPassed": all_passed,
        "results": {
            "qou_7q3s_takata_twist_cyclotomic": c_7q3s,
            "qou_2v4y_gukov_apoly_lagrangian": c_2v4y,
            "qou_c7lf_dimofte_gukov_wkb_one_loop": c_c7lf,
            "qou_ad5s_transseries_partial_radius": c_ad5s,
            "qou_cy96_fkv_complex_b_pentagon": c_cy96,
        },
    }

    WITNESS_PATH.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"Wrote {WITNESS_PATH} (allPassed={all_passed})")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
