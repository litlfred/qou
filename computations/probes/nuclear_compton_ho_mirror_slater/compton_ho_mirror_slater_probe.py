#!/usr/bin/env python3
"""EXPLORATORY shape-probe (pre-registered 80-dps verification, bean qou-otet):
Exact spherical harmonic-oscillator Slater Coulomb integrals (1s_1/2, 1p_3/2, 1p_1/2, 1d_5/2)
using QOU's derived Compton nuclear oscillator E_osc = m_e / (q_0 - 1)^2 (hbar omega_0(A) =
E_osc * A^(-1/3)) + backward Thomae-Jackson proper-time UV damping across T = 1/2 mirror
nuclei A = 3, 7, 11, 13, 15, 17, recording exact before/after residuals vs PR #9204's
uniform (3/A)^(1/3) scaling and AME2020.

Pre-registration: PREREGISTRATION.md (committed in 5be409c2671 prior to evaluation).
Lean companion: QOU/AtomicMass/ComptonHarmonicOscillatorSlaterRatios.lean.

Zero fitting, zero empirical nuclear radius, zero CODATA alpha, zero float64; proton pin q_0 = q_at(80).
"""
from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
for _p in ("computations", "computations/substrate", "tools/qou-substrate/python"):
    if str(ROOT / _p) not in sys.path:
        sys.path.insert(0, str(ROOT / _p))

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

import sympy as sp  # noqa: E402
from codata_constants import M_PI_PM_MEV_VALIDATION, ame_binding_mev  # noqa: E402
from mpmath import mp, mpf  # noqa: E402
from qou_substrate.constants import (  # noqa: E402
    M_E_MEV_STR,
    Q_MP,
    q_at,
    q_int_at,
    vol_4_1_at,
)
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from sympy.physics.wigner import wigner_3j, wigner_6j  # noqa: E402


def fmt50(x: mpf) -> str:
    return mp.nstr(x, 50, strip_zeros=False)


def frac_to_mpf(fr: Fraction) -> mpf:
    return mpf(fr.numerator) / mpf(fr.denominator)


def rat_to_mpf(r: sp.Rational) -> mpf:
    rr = sp.Rational(r)
    return mpf(int(rr.p)) / mpf(int(rr.q))


def alpha_form_b_at(qv: mpf, dps: int = 80) -> mpf:
    q9 = q_int_at(9, q=qv, dps=dps)
    q10 = q_int_at(10, q=qv, dps=dps)
    return mpf(1) / (qv * q9 * q10 + mpf(2) / (mpf(3) * mp.pi))


def derived_mp_mev(qv: mpf, me: mpf, dps: int = 80) -> mpf:
    qi = mpf(1) / qv
    hv = qv - qi
    hbar_sq = (mpf(1) - qi) ** 2
    vol = vol_4_1_at(dps)
    tr_m = abs((mpf(4) + hv ** 2 - mpf(3) * (hv ** 4) - hv ** 6) / (hv ** 2 + mpf(4)))
    qf3 = (qv ** 2 + mpf(1) + qi ** 2) * (qv + qi)
    return me * (mpf(2) * vol / hbar_sq * (tr_m * qf3 / (qv ** 3)) - mpf(12))


def ho_radial_slater_ratio_exact(
    l1: int, l2: int, l3: int, l4: int, k: int
) -> sp.Rational:
    """Exact analytical ratio R^k(1 l1, 1 l2; 1 l3, 1 l4) / E_C^(1s) over Q for nodeless (n_r=0)
    spherical harmonic-oscillator orbitals u_{1l}(x) = sqrt(2 / Gamma(l + 3/2)) x^l e^(-x^2/2),
    in units of E_C^(1s) = alpha sqrt(2/pi) / b.

    Uses polar coordinates (x_1, x_2) = (r sin t, r cos t) on 0 < x_1 < x_2 and (r cos t, r sin t)
    on 0 < x_2 < x_1, reducing via u = sin t in [0, 1/sqrt(2)] whenever l1+l3+k and l2+l4+k are even.
    """
    assert (l1 + l3 + k) % 2 == 0 and (l2 + l4 + k) % 2 == 0
    assert k <= l1 + l3 and k <= l2 + l4

    # Normalization product N_{l1} N_{l2} N_{l3} N_{l4}, where N_l^2 = 2 / Gamma(l + 3/2)
    # Note Gamma(m + 1/2) = ((2m)! / (4^m m!)) sqrt(pi), so N_{l1}..N_{l4} * Gamma(...) * sqrt(pi/2)
    # has all powers of pi and sqrt(2) cancel identically!
    def gamma_half(two_m_plus_1: int) -> sp.Expr:
        # two_m_plus_1 = 2*m + 1 -> Gamma(m + 1/2)
        return sp.gamma(sp.Rational(two_m_plus_1, 2))

    norm_prod = sp.sqrt(
        (sp.Integer(2) / gamma_half(2 * l1 + 3))
        * (sp.Integer(2) / gamma_half(2 * l2 + 3))
        * (sp.Integer(2) / gamma_half(2 * l3 + 3))
        * (sp.Integer(2) / gamma_half(2 * l4 + 3))
    )
    # Radial integral int_0^infty r^(l1+l2+l3+l4+4) e^(-r^2) dr = (1/2) Gamma((l1+l2+l3+l4+5)/2)
    rad_int = sp.Rational(1, 2) * gamma_half(l1 + l2 + l3 + l4 + 5)

    def angular_half(even_pow: int, odd_pow: int) -> sp.Expr:
        # int_0^(pi/4) sin^(even_pow)(t) cos^(odd_pow)(t) dt
        # u = sin t: int_0^(1/sqrt(2)) u^(2p) (1 - u^2)^m du
        assert even_pow % 2 == 0 and odd_pow % 2 == 1 and odd_pow >= 1
        p = even_pow // 2
        m = (odd_pow - 1) // 2
        u = sp.Symbol("u", positive=True)
        return sp.integrate((u ** (2 * p)) * ((1 - u ** 2) ** m), (u, 0, 1 / sp.sqrt(2)))

    ang1 = angular_half(l1 + l3 + k + 2, l2 + l4 - k + 1)
    ang2 = angular_half(l2 + l4 + k + 2, l1 + l3 - k + 1)
    val = sp.simplify(sp.sqrt(sp.pi / 2) * norm_prod * rad_int * (ang1 + ang2))
    assert val.is_rational, f"Expected exact rational Slater ratio, got {val}"
    return sp.Rational(val)


def closed_subshell_interaction_coeffs(
    l_val: int, j_val_twice: int, l_core: int, j_core_twice: int
) -> tuple[int, dict[int, sp.Rational]]:
    """Exact jj-coupled antisymmetrized interaction of one valence proton (l_val, j_val)
    with a closed core subshell (l_core, j_core)^(2 j_core + 1):
      V = (2 j_core + 1) F^0 - sum_{k: l_val + l_core + k even} c_k G^k,
    where c_k = (2 j_core + 1) * (3j(j_val, k, j_core; 1/2, 0, -1/2))^2.
    """
    jv = sp.Rational(j_val_twice, 2)
    jc = sp.Rational(j_core_twice, 2)
    deg_c = j_core_twice + 1
    exch: dict[int, sp.Rational] = {}
    for k in range(abs(l_val - l_core), l_val + l_core + 1):
        if (l_val + l_core + k) % 2 == 0:
            w3 = wigner_3j(jv, k, jc, sp.Rational(1, 2), 0, sp.Rational(-1, 2))
            coeff = sp.simplify(sp.Integer(deg_c) * (w3 ** 2))
            if coeff != 0:
                exch[k] = sp.Rational(coeff)
    return deg_c, exch


def same_subshell_pair_coeffs(l_val: int, j_twice: int, J_tot: int) -> dict[int, sp.Rational]:
    """Exact antisymmetrized <(nlj)^2 J | 1/r_12 | (nlj)^2 J> = sum_{k even} f_k F^k(nl, nl)
    for even J_tot.
    """
    assert J_tot % 2 == 0
    j = sp.Rational(j_twice, 2)
    res: dict[int, sp.Rational] = {}
    for k in range(0, 2 * l_val + 1, 2):
        w3 = wigner_3j(j, k, j, sp.Rational(1, 2), 0, sp.Rational(-1, 2))
        w6 = wigner_6j(j, j, J_tot, j, j, k)
        fk = sp.simplify(
            ((-1) ** (j_twice + J_tot)) * ((j_twice + 1) ** 2) * (w3 ** 2) * w6
        )
        if fk != 0:
            res[k] = sp.Rational(fk)
    return res


def main() -> int:
    with mp.workdps(80):
        q0 = q_at(80)
        qi0 = mpf(1) / q0
        me_mev = mpf(M_E_MEV_STR)
        mpi_mev = +M_PI_PM_MEV_VALIDATION
        mp_q0 = derived_mp_mev(q0, me_mev, dps=80)
        alpha_q0 = alpha_form_b_at(q0, dps=80)

        # QOU derived Compton nuclear harmonic-oscillator energy scale:
        # E_osc = m_e / (q_0 - 1)^2 = 42.24777... MeV, hbar*omega_0(A) = E_osc * A^(-1/3)
        e_osc_mev = me_mev / ((q0 - mpf(1)) ** 2)

        # Backward Thomae-Jackson proper-time UV damping from PR #9204
        tau0 = mp.log(q0)
        mu_sq = q0 * (q0 ** 2 - mpf(1))
        mu = mp.sqrt(mu_sq)
        raw_grid_sum = mpf(0)
        for j_idx in range(600):
            tau_j = tau0 * (q0 ** (2 * j_idx))
            exponent = -mu_sq * tau_j
            if exponent < mpf("-230"):
                break
            raw_grid_sum += (mpf(1) / mp.sqrt(mp.pi * tau_j)) * mp.exp(exponent) * tau_j

        d_back = mu * (mpf(1) - (qi0 ** 2)) * raw_grid_sum
        d_erfc = mp.erfc(mu * mp.sqrt(tau0))
        base_coul_pr9204_mev = alpha_q0 * mpi_mev

        recoil_sq = (mpi_mev / (mpf(2) * mp_q0)) ** 2
        recoil_su6_minus = mpf(1) - (mpf(3) / mpf(2)) * recoil_sq

        wb = WitnessBuilder(
            "compton-ho-mirror-slater",
            engine="mpmath (80 dps) + sympy exact Slater/Racah",
            output_dir=HERE,
        )
        wb.set_description(
            "Pre-registered 80-dps evaluation of exact 1s_1/2, 1p_3/2, 1p_1/2, 1d_5/2 spherical "
            "harmonic-oscillator Slater Coulomb integrals at QOU's derived Compton oscillator "
            "E_osc = m_e / (q_0 - 1)^2 = 42.24777 MeV + backward Thomae-Jackson UV damping across "
            "mirror nuclei A = 3, 7, 11, 13, 15, 17 vs PR #9204 uniform (3/A)^(1/3) and AME2020 "
            "(qou-otet / L2 Gate 3)."
        )
        wb.add_parameter("workdps", 80)
        wb.add_parameter("q0_proton_50dps", fmt50(q0))
        wb.add_parameter("E_osc_Compton_MeV", fmt50(e_osc_mev))
        wb.add_parameter("D_jackson_backward", fmt50(d_back))
        wb.add_parameter("D_continuum_erfc", fmt50(d_erfc))
        wb.add_parameter("preregistration_commit", "5be409c2671")

        wb.add_assertion(
            "q0_at_80_matches_Q_MP",
            computed=abs(q0 - (+Q_MP)),
            expected=mpf(0),
            tolerance=mpf("1e-65"),
            source="qou_substrate.constants",
        )

        # ==================================================================
        # 1. Exact Analytical Spherical HO Slater Ratios over Q
        # ==================================================================
        F0_1s1s = ho_radial_slater_ratio_exact(0, 0, 0, 0, 0)  # 1
        F0_1s1p = ho_radial_slater_ratio_exact(0, 1, 0, 1, 0)  # 5/6
        F0_1p1p = ho_radial_slater_ratio_exact(1, 1, 1, 1, 0)  # 3/4? Let's verify!
        F2_1p1p = ho_radial_slater_ratio_exact(1, 1, 1, 1, 2)
        G1_1s1p = ho_radial_slater_ratio_exact(0, 1, 1, 0, 1)
        F0_1s1d = ho_radial_slater_ratio_exact(0, 2, 0, 2, 0)
        G2_1s1d = ho_radial_slater_ratio_exact(0, 2, 2, 0, 2)
        F0_1p1d = ho_radial_slater_ratio_exact(1, 2, 1, 2, 0)
        G1_1p1d = ho_radial_slater_ratio_exact(1, 2, 2, 1, 1)
        G3_1p1d = ho_radial_slater_ratio_exact(1, 2, 2, 1, 3)

        # Numerical 80-dps Gaussian quadrature cross-check on F0_1p1p and F0_1p1d
        # Using Talmi-Moshinsky / Fourier: 1/|x_1 - x_2| = (2/pi) int_0^infty dk j_0(k x_1) j_0(k x_2)
        # For spherically averaged densities rho_l(x): int_0^infty 4 pi x^2 rho_l(x) j_0(k x) dx:
        # 1s: exp(-k^2/4); 1p: (1 - k^2/6) exp(-k^2/4); 1d: (1 - k^2/3 + k^4/60) exp(-k^2/4)!
        # Then F^0(1 l, 1 l') / E_C^(1s) = sqrt(2/pi) int_0^infty dk f_l(k) f_{l'}(k)!!
        k_var = sp.Symbol("k", positive=True)
        f_fourier = {
            0: sp.exp(-(k_var ** 2) / 4),
            1: (1 - (k_var ** 2) / 6) * sp.exp(-(k_var ** 2) / 4),
            2: (1 - (k_var ** 2) / 3 + (k_var ** 4) / 60) * sp.exp(-(k_var ** 2) / 4),
        }
        for (la, lb), f0_pol in (
            ((0, 0), F0_1s1s),
            ((0, 1), F0_1s1p),
            ((1, 1), F0_1p1p),
            ((0, 2), F0_1s1d),
            ((1, 2), F0_1p1d),
        ):
            f0_ft = sp.simplify(
                sp.sqrt(2 / sp.pi) * sp.integrate(f_fourier[la] * f_fourier[lb], (k_var, 0, sp.oo))
            )
            assert f0_ft == f0_pol, f"Mismatch ({la},{lb}): polar={f0_pol} vs fourier={f0_ft}"

        wb.add_assertion(
            "slater_F0_polar_matches_fourier_bessel_identically",
            computed=mpf(0),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="ComptonHarmonicOscillatorSlaterRatios exact rational F^0 ladder",
        )

        # Verify jj-coupling Racah coefficients
        p32_J0 = same_subshell_pair_coeffs(1, 3, 0)  # {0: 1, 2: 1/5}
        p32_J2 = same_subshell_pair_coeffs(1, 3, 2)  # {0: 1, 2: -3/25}
        p12_J0 = same_subshell_pair_coeffs(1, 1, 0)  # {0: 1}
        assert p32_J0 == {0: sp.Rational(1, 1), 2: sp.Rational(1, 5)}
        assert p32_J2 == {0: sp.Rational(1, 1), 2: sp.Rational(-3, 25)}
        assert p12_J0 == {0: sp.Rational(1, 1)}

        _, ex_p32_s12 = closed_subshell_interaction_coeffs(1, 3, 0, 1)  # {1: 1/3}
        _, ex_p12_s12 = closed_subshell_interaction_coeffs(1, 1, 0, 1)  # {1: 1/3}
        _, ex_p12_p32 = closed_subshell_interaction_coeffs(1, 1, 1, 3)  # {2: 2/5}
        _, ex_d52_s12 = closed_subshell_interaction_coeffs(2, 5, 0, 1)  # {2: 1/5}
        _, ex_d52_p32 = closed_subshell_interaction_coeffs(2, 5, 1, 3)
        _, ex_d52_p12 = closed_subshell_interaction_coeffs(2, 5, 1, 1)
        assert ex_p32_s12 == {1: sp.Rational(1, 3)}
        assert ex_p12_s12 == {1: sp.Rational(1, 3)}
        assert ex_p12_p32 == {2: sp.Rational(2, 5)}
        assert ex_d52_s12 == {2: sp.Rational(1, 5)}

        # Closed 1p^6 = 1p_{3/2}^4 + 1p_{1/2}^2 exchange with 1d_{5/2}:
        ex_d52_p6_G1 = ex_d52_p32.get(1, sp.Rational(0)) + ex_d52_p12.get(1, sp.Rational(0))
        ex_d52_p6_G3 = ex_d52_p32.get(3, sp.Rational(0)) + ex_d52_p12.get(3, sp.Rational(0))

        # Exact dimensionless Coulomb step C_direct(A) and C_antisym(A) in units of E_C^(1s)(A):
        # A=3:  1s^1 -> 1s^2 (J=0)
        # A=7:  1s^2 1p3/2^1 -> 1s^2 1p3/2^2 (v=0): +V(1p3/2, 1s^2) + <(1p3/2)^2 J=0>
        # A=11: 1s^2 1p3/2^3 -> 1s^2 1p3/2^4 (closed): +V(1p3/2, 1s^2) + (1/2) E_closed((1p3/2)^4)
        #       where E_closed((1p3/2)^4) = 1*(F0 + 1/5 F2) + 5*(F0 - 3/25 F2) = 6 F0 - 2/5 F2,
        #       so half is 3 F0 - 1/5 F2!
        # A=13: 1s^2 1p3/2^4 -> + 1p1/2^1: +V(1p1/2, 1s^2) + V(1p1/2, 1p3/2^4)
        # A=15: + 1p1/2^1 -> 1p1/2^2 (J=0): +V(1p1/2, 1s^2) + V(1p1/2, 1p3/2^4) + F0(1p,1p)
        # A=17: 1s^2 1p^6 -> + 1d5/2^1: +V(1d5/2, 1s^2) + V(1d5/2, 1p^6)
        v_1p_1s2_antisym = 2 * F0_1s1p - sp.Rational(1, 3) * G1_1s1p
        v_p12_p32_antisym = 4 * F0_1p1p - sp.Rational(2, 5) * F2_1p1p
        v_d52_1s2_antisym = 2 * F0_1s1d - sp.Rational(1, 5) * G2_1s1d
        v_d52_1p6_antisym = 6 * F0_1p1d - ex_d52_p6_G1 * G1_1p1d - ex_d52_p6_G3 * G3_1p1d

        step_coeffs_rat: dict[int, tuple[sp.Rational, sp.Rational]] = {
            3: (F0_1s1s, F0_1s1s),
            7: (2 * F0_1s1p + F0_1p1p, v_1p_1s2_antisym + (F0_1p1p + sp.Rational(1, 5) * F2_1p1p)),
            11: (
                2 * F0_1s1p + 3 * F0_1p1p,
                v_1p_1s2_antisym + (3 * F0_1p1p - sp.Rational(1, 5) * F2_1p1p),
            ),
            13: (2 * F0_1s1p + 4 * F0_1p1p, v_1p_1s2_antisym + v_p12_p32_antisym),
            15: (
                2 * F0_1s1p + 5 * F0_1p1p,
                v_1p_1s2_antisym + v_p12_p32_antisym + F0_1p1p,
            ),
            17: (2 * F0_1s1d + 6 * F0_1p1d, v_d52_1s2_antisym + v_d52_1p6_antisym),
        }

        slater_catalog = {
            "F0_1s_1s": str(F0_1s1s),
            "F0_1s_1p": str(F0_1s1p),
            "G1_1s_1p": str(G1_1s1p),
            "F0_1p_1p": str(F0_1p1p),
            "F2_1p_1p": str(F2_1p1p),
            "F0_1s_1d": str(F0_1s1d),
            "G2_1s_1d": str(G2_1s1d),
            "F0_1p_1d": str(F0_1p1d),
            "G1_1p_1d": str(G1_1p1d),
            "G3_1p_1d": str(G3_1p1d),
            "exch_1d52_with_1p6_G1_coeff": str(ex_d52_p6_G1),
            "exch_1d52_with_1p6_G3_coeff": str(ex_d52_p6_G3),
        }

        wb.add_assertion(
            "major_shell_Z8_to_Z9_slater_drop_below_linear_extrapolation",
            computed=mpf(
                0
                if (step_coeffs_rat[17][0] - step_coeffs_rat[15][0])
                < (step_coeffs_rat[15][0] - step_coeffs_rat[13][0])
                else 1
            ),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="ComptonHarmonicOscillatorSlaterRatios.step_jump_15_to_17_lt_13_to_15",
        )

        # ==================================================================
        # 2. Evaluate Mirror-Nuclei Splits A = 3, 7, 11, 13, 15, 17 at 80 dps
        # ==================================================================
        mirror_pairs = [
            (3, 1, 2, "3H-3He"),
            (7, 3, 4, "7Li-7Be"),
            (11, 5, 6, "11B-11C"),
            (13, 6, 7, "13C-13N"),
            (15, 7, 8, "15N-15O"),
            (17, 8, 9, "17O-17F"),
        ]

        rows = []
        abs_pct_pr9204_open1p = []
        abs_pct_s1_open1p = []
        abs_pct_s2_open1p = []

        print("Slater ratios (in units of E_C^(1s)):")
        for k_sl, v_sl in slater_catalog.items():
            print(f"  {k_sl:28s} = {v_sl}")
        print()

        for A_val, z_low, z_high, label in mirror_pairs:
            ame_db = ame_binding_mev(z_low, A_val) - ame_binding_mev(z_high, A_val)
            n_pairs = (A_val - 1) // 2

            # Baseline PR #9204 uniform volume scaling
            vol_scale = (mpf(3) / mpf(A_val)) ** (mpf(1) / mpf(3))
            pr9204_coul = mpf(n_pairs) * vol_scale * base_coul_pr9204_mev * d_back
            pr9204_su6 = pr9204_coul * recoil_su6_minus

            # Derived Compton HO scale at mass number A:
            # hbar*omega_0(A) = E_osc * A^(-1/3), b(A)^(-1) = sqrt(m_p(q_0) * hbar*omega_0(A))
            hbar_omega_a = e_osc_mev * (mpf(A_val) ** (-mpf(1) / mpf(3)))
            inv_b_a = mp.sqrt(mp_q0 * hbar_omega_a)
            ec_1s_a = alpha_q0 * mp.sqrt(mpf(2) / mp.pi) * inv_b_a

            c_dir_rat, c_anti_rat = step_coeffs_rat[A_val]
            c_dir = rat_to_mpf(c_dir_rat)
            c_anti = rat_to_mpf(c_anti_rat)

            s1_dir_coul = c_dir * ec_1s_a * d_back
            s1_dir_su6 = s1_dir_coul * recoil_su6_minus
            s2_anti_coul = c_anti * ec_1s_a * d_back
            s2_anti_su6 = s2_anti_coul * recoil_su6_minus
            s3_dir_undamped = c_dir * ec_1s_a
            s3_anti_undamped = c_anti * ec_1s_a

            pct_pr9204 = (pr9204_su6 - ame_db) / ame_db * mpf(100)
            pct_s1 = (s1_dir_su6 - ame_db) / ame_db * mpf(100)
            pct_s2 = (s2_anti_su6 - ame_db) / ame_db * mpf(100)
            pct_s2_coul = (s2_anti_coul - ame_db) / ame_db * mpf(100)
            pct_s3_anti = (s3_anti_undamped - ame_db) / ame_db * mpf(100)

            if A_val in (11, 13, 15):
                abs_pct_pr9204_open1p.append(abs(pct_pr9204))
                abs_pct_s1_open1p.append(abs(pct_s1))
                abs_pct_s2_open1p.append(abs(pct_s2))

            rows.append(
                {
                    "A": A_val,
                    "mirror_pair": label,
                    "hbar_omega0_MeV": fmt50(hbar_omega_a),
                    "E_C_1s_unit_MeV": fmt50(ec_1s_a),
                    "C_direct_F0_exact": str(c_dir_rat),
                    "C_antisym_jj_exact": str(c_anti_rat),
                    "AME2020_DeltaB_MeV_comparison": fmt50(ame_db),
                    "baseline_PR9204_vol_A13_su6_MeV": fmt50(pr9204_su6),
                    "baseline_PR9204_rel_pct": fmt50(pct_pr9204),
                    "S1_ho_direct_F0_jackson_coulomb_MeV": fmt50(s1_dir_coul),
                    "S1_ho_direct_F0_jackson_su6_MeV": fmt50(s1_dir_su6),
                    "S1_rel_pct_su6": fmt50(pct_s1),
                    "S2_ho_antisym_jj_jackson_coulomb_MeV": fmt50(s2_anti_coul),
                    "S2_ho_antisym_jj_jackson_su6_MeV": fmt50(s2_anti_su6),
                    "S2_rel_pct_coulomb": fmt50(pct_s2_coul),
                    "S2_rel_pct_su6": fmt50(pct_s2),
                    "S3_ho_direct_F0_undamped_MeV": fmt50(s3_dir_undamped),
                    "S3_ho_antisym_jj_undamped_MeV": fmt50(s3_anti_undamped),
                    "S3_antisym_undamped_rel_pct": fmt50(pct_s3_anti),
                }
            )
            print(
                f"A={A_val:2d} ({label:7s}) AME={mp.nstr(ame_db, 6):7s} | "
                f"PR9204={mp.nstr(pr9204_su6, 6):7s} ({mp.nstr(pct_pr9204, 4):>7s}%) | "
                f"S1_F0={mp.nstr(s1_dir_su6, 6):7s} ({mp.nstr(pct_s1, 4):>7s}%) | "
                f"S2_jj={mp.nstr(s2_anti_su6, 6):7s} ({mp.nstr(pct_s2, 4):>7s}%) | "
                f"undamp_jj={mp.nstr(s3_anti_undamped, 6):7s} ({mp.nstr(pct_s3_anti, 4):>7s}%)"
            )

        wb.add_data("slater_integral_ratios_over_E_C_1s", slater_catalog)
        wb.add_data("mirror_nuclei_comparison_table", rows)
        wb.add_data(
            "open_1p_shell_A11_13_15_mean_abs_pct_summary",
            {
                "PR9204_uniform_vol_A13_su6_mean_abs_pct": fmt50(
                    sum(abs_pct_pr9204_open1p) / mpf(3)
                ),
                "S1_ho_direct_F0_jackson_su6_mean_abs_pct": fmt50(
                    sum(abs_pct_s1_open1p) / mpf(3)
                ),
                "S2_ho_antisym_jj_jackson_su6_mean_abs_pct": fmt50(
                    sum(abs_pct_s2_open1p) / mpf(3)
                ),
            },
        )
        wb.save({"q0Anchor": "proton"})
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
