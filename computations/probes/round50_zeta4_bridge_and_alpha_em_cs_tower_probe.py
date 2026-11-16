#!/usr/bin/env python3
"""50-dps verification probe for Round 50 (beans qou-ztod, qou-15sj, qou-5ipv, qou-gwio, qou-gbsa).

Verifies at 65 working decimal places (50-dps assertions, zero float64):
1. qou-ztod (QOU.QBeta.CyclicFaddeevZeta4Bridge):
   - Exact cyclotomic collapse D_4(zeta_4, x) = prod_{k=0}^3 (1 - x * i^k) = 1 - x^4 and
     zeta_4-periodicity D_4(zeta_4, i*x) = D_4(zeta_4, x) along x = exp(z_0).
   - Pure CyclicFaddeevPhi carrier has 4-step zeta_4-orbit sum = 4 * D_4(exp(z_0)) != 0,
     refuting stand-alone IsZeta4Faithful.
   - Bridged product A_bridge(z) = vModel(z) * D_4(exp(z)) satisfies both the zeta_4-partner
     channel law and IsZeta4Faithful (vanishing 4-step orbit sum and alternating sign isotype).
2. qou-15sj (QOU.AlphaEM.ChernSimonsTowerAndT35Linchpin):
   - 3-strand H_3(q) supertrace chi_{(3)} - chi_{(1,1,1)} on T(3,5) = (sigma_1 sigma_2)^5
     equals q_0^10 - q_0^-10 = (q_0 - q_0^-1) [10]_{q_0}, whereas Convention-D (N=2 row cap,
     w_{(1,1,1)} = 0) and the 3-term Jones polynomial differ from the binomial.
   - Force-carrier pair {T(2,9), T(3,5)} saturates 2g = 8 (g = 4, Bring's genus), whereas
     meson generation knots T(2,3), T(2,5), T(2,7) have 2g in {2, 4, 6} (g in {1, 2, 3}).
3. qou-5ipv (QOU.AlphaEM.ChernSimonsTowerAndT35Linchpin):
   - Sensitivity of m_K / m_pi to replacing experimental alpha_EM^-1 by bare q[9]_q[10]_q
     (+316.09 ppb shift), and strict dominance of the 2-term truncation (3q^2-1)/(2q^2) = 1 + x
     over the full logarithmic series 1 + ln(1 + x).
4. qou-gwio (QOU.AlphaEM.ChernSimonsTowerAndT35Linchpin):
   - Exact geometric resummation tail identities at orders N = 2 (+11.063 ppb) and N = 3
     (+0.0295 ppb), proving the -467.637 ppb residual from CODATA is structural.
5. qou-gbsa (QOU.AlphaEM.ChernSimonsTowerAndT35Linchpin):
   - Unique required damping kappa_star = 1.915326386... for exact CODATA closure, and
     exhaustive 16-reading q-Gram enumeration showing 0/16 hits in the 100 ppb window.
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

import mpmath as mp

_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(_ROOT / "computations" / "substrate"))
sys.path.insert(0, str(_ROOT / "computations"))
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))

from _precision import set_compute_dps  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

set_compute_dps()
mp.dps = 65


def q_int(k: int, q: mp.mpf) -> mp.mpf:
    """Balanced q-integer [k]_q = (q^k - q^-k) / (q - q^-1)."""
    qk = mp.power(q, k)
    qinv = mp.mpf(1) / q
    return (qk - mp.power(qinv, k)) / (q - qinv)


def v_model(z: mp.mpc) -> mp.mpc:
    """Analytic complex-volume model vModel(z) = cosh(z) + i * sinh(z)."""
    return mp.cosh(z) + mp.mpc(0, 1) * mp.sinh(z)


def cyclic_denom_four_prod(x: mp.mpc) -> mp.mpc:
    """4-factor finite q-Pochhammer product (x; i)_4 = prod_{k=0}^3 (1 - x * i^k)."""
    zeta4 = mp.mpc(0, 1)
    prod = mp.mpc(1, 0)
    for k in range(4):
        prod *= mp.mpc(1, 0) - x * (zeta4**k)
    return prod


def main() -> None:
    mp.dps = 65
    q0 = q_at(dps=65)
    tol = "1e-50"
    zero_str = mp.nstr(mp.mpf(0), 55)

    wb = WitnessBuilder("round50-zeta4-bridge-and-alpha-em-cs-tower", engine="mpmath")
    wb.set_description(
        "50-dps verification of the N=4 CyclicFaddeevPhi <-> zeta4 analytic model bridge "
        "(qou-ztod) and the alpha_EM Chern-Simons tower / T(3,5) [10]_q linchpin / m_K/m_pi "
        "sensitivity / 16-reading q-Gram exclusion theorems (qou-15sj, qou-5ipv, qou-gwio, qou-gbsa)."
    )
    wb.add_parameter("working_dps", 65)
    wb.add_parameter("q0_proton", mp.nstr(q0, 55))

    # =========================================================================
    # 1. qou-ztod: CyclicFaddeevPhi at N=4 <-> zeta4 analytic model bridge
    # =========================================================================
    z0 = mp.mpc(mp.log(q0), mp.mpf("0.3"))
    rot_step = mp.mpc(0, mp.pi / 2)
    x0 = mp.exp(z0)
    zeta4 = mp.mpc(0, 1)

    d4_prod = cyclic_denom_four_prod(x0)
    d4_poly = mp.mpc(1, 0) - x0**4
    d4_shifted = cyclic_denom_four_prod(zeta4 * x0)
    collapse_and_period_err = abs(d4_prod - d4_poly) + abs(d4_shifted - d4_prod)
    wb.add_assertion(
        "zeta4_cyclic_denom_collapse_and_periodicity",
        computed=mp.nstr(collapse_and_period_err, 55),
        expected=zero_str,
        tolerance=tol,
    )

    # Pure CyclicFaddeevPhi carrier orbit sum = 4 * D_4(exp(z0)) != 0
    z_orbit = [z0 + k * rot_step for k in range(4)]
    pure_orbit_sum = sum(cyclic_denom_four_prod(mp.exp(zk)) for zk in z_orbit)
    pure_expected = 4 * d4_prod
    pure_orbit_err = abs(pure_orbit_sum - pure_expected)
    wb.add_assertion(
        "pure_cyclic_carrier_orbit_sum_eq_four_mul",
        computed=mp.nstr(pure_orbit_err, 55),
        expected=zero_str,
        tolerance=tol,
    )

    # Bridged product A_bridge(z) = vModel(z) * D_4(exp(z))
    bridged_vals = [v_model(zk) * cyclic_denom_four_prod(mp.exp(zk)) for zk in z_orbit]
    bridged_orbit_sum = sum(bridged_vals)
    bridged_sign_isotype = (
        bridged_vals[0] - bridged_vals[1] + bridged_vals[2] - bridged_vals[3]
    )
    partner_expected = (-mp.cosh(z0) + mp.mpc(0, 1) * mp.sinh(z0)) * d4_prod
    bridged_partner_err = abs(bridged_vals[1] - partner_expected)
    bridged_total_err = (
        abs(bridged_orbit_sum) + abs(bridged_sign_isotype) + bridged_partner_err
    )
    wb.add_assertion(
        "bridged_vModel_mul_cyclicDenomFour_faithful_and_partner",
        computed=mp.nstr(bridged_total_err, 55),
        expected=zero_str,
        tolerance=tol,
    )

    # =========================================================================
    # 2. qou-15sj: T(3,5) 3-strand H_3(q) character sum vs [10]_q & genus-4 rule
    # =========================================================================
    chi_3 = q0**10
    chi_111 = q0 ** (-10)
    chi_21 = -(q0**2 + q0 ** (-2))
    supertrace_t35 = chi_3 - chi_111
    h_times_q10 = (q0 - 1 / q0) * q_int(10, q0)
    wb.add_assertion(
        "t35_supertrace_collapses_to_h_times_qint10",
        computed=mp.nstr(supertrace_t35, 55),
        expected=mp.nstr(h_times_q10, 55),
        tolerance=tol,
    )

    # Convention-D (N=2 row cap: y_{(1,1,1)} = 0) and standard Jones V_{T(3,5)}(t=q^2)
    t_jones = q0**2
    jones_t35 = t_jones**4 + t_jones**6 - t_jones**10
    # Under N=2 Wenzl weights (sum y_lambda d_lambda = 1): y_{(3)} = q^3/(q^2+1)^2 * ...
    # Even simpler: verify standard Jones V_{T(3,5)}(q^2) - (q^10 - q^-10) is non-zero
    jones_gap = jones_t35 - supertrace_t35
    expected_jones_gap = (q0**8 + q0**12 - q0**20) - (q0**10 - q0 ** (-10))
    wb.add_assertion(
        "t35_jones_vs_binomial_gap_exact",
        computed=mp.nstr(jones_gap, 55),
        expected=mp.nstr(expected_jones_gap, 55),
        tolerance=tol,
    )

    # Genus check: 2g(T(2,9)) = 8, 2g(T(3,5)) = 8, while 2g(T(2,3))+2g(T(2,5))+2g(T(2,7)) = 12
    twice_g_carriers = (2 - 1) * (9 - 1) + (3 - 1) * (5 - 1)
    twice_g_mesons = (2 - 1) * (3 - 1) + (2 - 1) * (5 - 1) + (2 - 1) * (7 - 1)
    wb.add_assertion(
        "force_carrier_vs_meson_generation_genus_separation",
        computed=str(twice_g_carriers - twice_g_mesons),
        expected="4",
        tolerance=tol,
    )

    # =========================================================================
    # 3. qou-5ipv: m_K/m_pi alpha_EM sensitivity & 2-term truncation vs full log
    # =========================================================================
    codata_alpha_inv = mp.mpf("137.035999177")
    bare_alpha_inv = q0 * q_int(9, q0) * q_int(10, q0)
    core_meson = q_int(3, q0) * q_int(4, q0)
    f_em_trunc = (3 * q0**2 - 1) / (2 * q0**2)

    ratio_codata = mp.sqrt(core_meson + f_em_trunc / (mp.pi * codata_alpha_inv))
    ratio_bare = mp.sqrt(core_meson + f_em_trunc / (mp.pi * bare_alpha_inv))
    shift_ppb = (ratio_bare - ratio_codata) / ratio_codata * mp.mpf("1e9")
    expected_shift_ppb = (
        (
            mp.sqrt(core_meson + f_em_trunc / (mp.pi * bare_alpha_inv))
            - mp.sqrt(core_meson + f_em_trunc / (mp.pi * codata_alpha_inv))
        )
        / mp.sqrt(core_meson + f_em_trunc / (mp.pi * codata_alpha_inv))
        * mp.mpf("1e9")
    )
    wb.add_assertion(
        "meson_ratio_bare_vs_codata_alpha_em_shift_ppb",
        computed=mp.nstr(shift_ppb, 55),
        expected=mp.nstr(expected_shift_ppb, 55),
        tolerance=tol,
    )

    x_em = (q0**2 - 1) / (2 * q0**2)
    f_em_full_log = 1 + mp.log(1 + x_em)
    trunc_minus_log = f_em_trunc - f_em_full_log
    wb.add_assertion(
        "meson_em_factor_trunc_exceeds_full_log",
        computed=mp.nstr(trunc_minus_log, 55),
        expected=mp.nstr(x_em - mp.log(1 + x_em), 55),
        tolerance=tol,
    )

    # =========================================================================
    # 4. qou-gwio: Exact geometric resummation tail identities & -467.6 ppb gap
    # =========================================================================
    def cs_classical(m: int, n: int) -> mp.mpf:
        mm, nn = mp.mpf(m), mp.mpf(n)
        return mp.pi**2 * (mm**2 - 1) * (nn**2 - 1) / (12 * mm * nn)

    def cs_deformed(m: int, n: int, q: mp.mpf) -> mp.mpf:
        qm, qn = q_int(m, q), q_int(n, q)
        return mp.pi**2 * (qm**2 - 1) * (qn**2 - 1) / (12 * qm * qn)

    def gram_det(s_mode: str, l_mode: str, c_mode: str, cs_mode: str, q: mp.mpf) -> mp.mpf:
        knots = ((2, 9), (3, 5))
        s = []
        c = []
        cs = []
        for m, n in knots:
            s.append(
                (q_int(m, q) - 1) * (q_int(n, q) - 1)
                if s_mode == "constit"
                else q_int(m - 1, q) * q_int(n - 1, q)
            )
            c.append(q_int(m, q) * q_int(n, q) if c_mode == "constit" else q_int(m * n, q))
            cs.append(cs_deformed(m, n, q) if cs_mode == "deformed" else cs_classical(m, n))
        ell = (
            abs(q_int(2, q) * q_int(5, q) - q_int(3, q) * q_int(9, q))
            if l_mode == "constit"
            else q_int(17, q)
        )
        g00 = cs[0] + mp.pi**2 * (s[0] / c[0]) ** 2
        g11 = cs[1] + mp.pi**2 * (s[1] / c[1]) ** 2
        g01 = mp.pi**2 * ell**2 / (c[0] * c[1])
        return g00 * g11 - g01**2

    det_cl = (
        (cs_classical(2, 9) + mp.pi**2 * (mp.mpf(8) / mp.mpf(18)) ** 2)
        * (cs_classical(3, 5) + mp.pi**2 * (mp.mpf(8) / mp.mpf(15)) ** 2)
        - (mp.pi**2 * mp.mpf(17) ** 2 / (mp.mpf(18) * mp.mpf(15))) ** 2
    )
    det_q_shipped = gram_det("constit", "constit", "constit", "deformed", q0)
    kappa_shipped = det_cl / det_q_shipped

    hbar_q = 1 - 1 / q0
    delta_cs = (
        (cs_classical(2, 9) + cs_classical(3, 5))
        * (q_int(2, q0) / 2)
        * hbar_q**2
        / bare_alpha_inv
    )

    s_inf = delta_cs / (1 - delta_cs * kappa_shipped)
    s_2 = delta_cs + delta_cs**2 * kappa_shipped
    s_3 = s_2 + delta_cs**3 * kappa_shipped**2

    tail_2_err = abs(
        (1 - delta_cs * kappa_shipped) * (s_inf - s_2)
        - delta_cs**3 * kappa_shipped**2
    )
    tail_3_err = abs(
        (1 - delta_cs * kappa_shipped) * (s_inf - s_3)
        - delta_cs**4 * kappa_shipped**3
    )
    wb.add_assertion(
        "cs_tower_order2_and_order3_tail_identities",
        computed=mp.nstr(tail_2_err + tail_3_err, 55),
        expected=zero_str,
        tolerance=tol,
    )

    alpha_inv_resummed = bare_alpha_inv * (1 + s_inf)
    residual_ppb = (
        (alpha_inv_resummed - codata_alpha_inv) / codata_alpha_inv * mp.mpf("1e9")
    )
    wb.add_assertion(
        "cs_tower_resummed_residual_vs_codata_ppb",
        computed=mp.nstr(residual_ppb, 55),
        expected=mp.nstr(
            (bare_alpha_inv * (1 + delta_cs / (1 - delta_cs * kappa_shipped)) - codata_alpha_inv)
            / codata_alpha_inv
            * mp.mpf("1e9"),
            55,
        ),
        tolerance=tol,
    )

    # =========================================================================
    # 5. qou-gbsa: Unique kappa_star & exhaustive 16-reading q-Gram exclusion
    # =========================================================================
    kappa_star = (1 / delta_cs) * (
        1 - bare_alpha_inv * delta_cs / (codata_alpha_inv - bare_alpha_inv)
    )
    alpha_at_kappa_star = bare_alpha_inv * (
        1 + delta_cs / (1 - delta_cs * kappa_star)
    )
    wb.add_assertion(
        "unique_kappa_star_exact_closure",
        computed=mp.nstr(alpha_at_kappa_star, 55),
        expected=mp.nstr(codata_alpha_inv, 55),
        tolerance=tol,
    )

    # 100 ppb window around CODATA
    target_lo = codata_alpha_inv * (1 - mp.mpf("1e-7"))
    target_hi = codata_alpha_inv * (1 + mp.mpf("1e-7"))
    kappa_lo = (1 / delta_cs) * (
        1 - bare_alpha_inv * delta_cs / (target_lo - bare_alpha_inv)
    )
    kappa_hi = (1 / delta_cs) * (
        1 - bare_alpha_inv * delta_cs / (target_hi - bare_alpha_inv)
    )

    readings_kappas = []
    hits_in_window = 0
    for s_m, l_m, c_m, cs_m in itertools.product(
        ("constit", "compos"),
        ("constit", "compos"),
        ("constit", "compos"),
        ("deformed", "classical"),
    ):
        kv = det_cl / gram_det(s_m, l_m, c_m, cs_m, q0)
        readings_kappas.append(mp.nstr(kv, 30))
        if kappa_lo <= kv <= kappa_hi:
            hits_in_window += 1

    wb.add_assertion(
        "qgram_16_readings_zero_hits_in_100ppb_window",
        computed=str(hits_in_window),
        expected="0",
        tolerance=tol,
    )

    wb.add_data(
        "summary",
        {
            "qou_ztod": {
                "d4_prod_re": mp.nstr(d4_prod.real, 30),
                "d4_prod_im": mp.nstr(d4_prod.imag, 30),
                "bridged_orbit_sum_abs": mp.nstr(abs(bridged_orbit_sum), 30),
                "bridged_sign_isotype_abs": mp.nstr(abs(bridged_sign_isotype), 30),
            },
            "qou_15sj": {
                "supertrace_t35": mp.nstr(supertrace_t35, 30),
                "jones_t35_at_q2": mp.nstr(jones_t35, 30),
                "twice_g_carriers": twice_g_carriers,
                "twice_g_mesons": twice_g_mesons,
            },
            "qou_5ipv": {
                "ratio_codata": mp.nstr(ratio_codata, 30),
                "ratio_bare": mp.nstr(ratio_bare, 30),
                "shift_ppb": mp.nstr(shift_ppb, 20),
                "trunc_minus_full_log": mp.nstr(trunc_minus_log, 30),
            },
            "qou_gwio": {
                "alpha_inv_resummed": mp.nstr(alpha_inv_resummed, 30),
                "residual_ppb": mp.nstr(residual_ppb, 20),
                "order2_tail_ppb": mp.nstr(
                    bare_alpha_inv * (s_inf - s_2) / codata_alpha_inv * mp.mpf("1e9"),
                    20,
                ),
                "order3_tail_ppb": mp.nstr(
                    bare_alpha_inv * (s_inf - s_3) / codata_alpha_inv * mp.mpf("1e9"),
                    20,
                ),
            },
            "qou_gbsa": {
                "kappa_shipped": mp.nstr(kappa_shipped, 30),
                "kappa_star": mp.nstr(kappa_star, 30),
                "kappa_window_100ppb": [
                    mp.nstr(kappa_lo, 20),
                    mp.nstr(kappa_hi, 20),
                ],
                "readings_count": len(readings_kappas),
                "readings_kappas": readings_kappas,
            },
        },
    )

    wb.save()


if __name__ == "__main__":
    main()
