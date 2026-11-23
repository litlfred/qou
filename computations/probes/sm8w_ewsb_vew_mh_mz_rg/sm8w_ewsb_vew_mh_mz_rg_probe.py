#!/usr/bin/env python3
"""80-dps pre-registered evaluation of Standard Model Package 3 (`qou-ewsb`, `Q-Gap-9`):
Electroweak VEV `v_EW`, Higgs mass & quartic `(m_H, lambda_H)`, Sweedler `(q_0^2 - 1)^k`
weak suppression vs `ElectroweakBringSchwingerBridge` / `ElectroweakVevGaps`, and
zero-parameter 1-loop & 2-loop UV-to-`M_Z` / `Lambda_QCD` RG threshold running.

Pre-registered in `PREREGISTRATION.md` (commit `bdfaf539356`) BEFORE running any
numerical evaluation. Companion to:
  - `folio/quantum-observable-universe/lean/QOU/StandardModel/ElectroweakSweedlerScaleAndRGThresholds.lean`
  - `folio/quantum-observable-universe/lean/QOU/BraidKnot/HiggsCategoricalMassFormula.lean`

Precision & anti-fit discipline:
  - `mpmath` at `workdps = 80` (`OUT_DPS = 50` serialized),
  - `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`),
  - CAL-1 `m_e`, proton validation pin `m_p`, CAL-3 `m_{pi+-}`, Form-B `alpha_q^{-1}(q_0)`,
    exact Catalan series `mp.catalan = Cl_2(pi/2)`,
  - PDG-2024 empirical values (`G_F`, `v_EW`, `M_W`, `M_Z`, `m_H`, `sin^2 theta_W(M_Z)`,
    `alpha_s(M_Z)`) used strictly as external comparison targets, NEVER to fit any QOU
    coefficient,
  - zero `float64` imports, literals, or casts (`probe-float64-guard.py --diff` clean).
"""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[3]
if str(_ROOT / "tools" / "qou-substrate" / "python") not in sys.path:
    sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))
if str(_ROOT / "computations") not in sys.path:
    sys.path.insert(0, str(_ROOT / "computations"))

import mpmath as mp  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WORK_DPS = 80
OUT_DPS = 50
set_compute_dps(WORK_DPS)

# CAL-3 meson scale (MeV)
M_PI_CHARGED_MEV = mp.mpf("139.57039")

# PDG-2024 / CODATA-2022 external comparison targets ONLY (zero fitting)
PDG_GF_GEV_INV2 = mp.mpf("1.1663787e-5")
PDG_GF_SIG_GEV_INV2 = mp.mpf("0.0000006e-5")
PDG_MW_GEV = mp.mpf("80.3692")
PDG_MW_SIG_GEV = mp.mpf("0.0133")
PDG_MZ_GEV = mp.mpf("91.1876")
PDG_MZ_SIG_GEV = mp.mpf("0.0021")
PDG_MH_GEV = mp.mpf("125.20")
PDG_MH_SIG_GEV = mp.mpf("0.11")
PDG_SIN2_THETAW_MSBAR = mp.mpf("0.23122")
PDG_SIN2_THETAW_SIG = mp.mpf("0.00004")
PDG_ALPHA_EM_INV_MZ_MSBAR = mp.mpf("127.951")
PDG_ALPHA_EM_INV_MZ_SIG = mp.mpf("0.009")
PDG_ALPHA_S_MZ = mp.mpf("0.1180")
PDG_ALPHA_S_MZ_SIG = mp.mpf("0.0009")

# Remediated 52-digit rational literal formerly in HiggsCategoricalMassFormula.lean:96
RETIRED_CATALAN_DECIMAL_STR = "0.9159655941772190150546035149323841107741493742816721"


def _binom(n: int, k: int) -> int:
    """Exact integer binomial coefficient without importing Python `math`."""
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    num = 1
    for i in range(k):
        num = num * (n - i) // (i + 1)
    return num


def qbal(n: int, q: mp.mpf) -> mp.mpf:
    """Balanced quantum integer `[n]_q = (q^n - q^{-n}) / (q - q^{-1})`."""
    one = mp.mpf(1)
    return (q ** n - q ** (-n)) / (q - one / q)


def trace_poly_p(m: int, h: mp.mpf) -> mp.mpf:
    """Binomial Plancherel trace polynomial `P_m(h) = sum_{j=0}^m C(m+j, 2j)/2 * h^{2j}`."""
    two = mp.mpf(2)
    acc = mp.mpf(0)
    for j in range(m + 1):
        acc += (mp.mpf(_binom(m + j, 2 * j)) / two) * (h ** (2 * j))
    return acc


def solve_form_b_alpha_inv(q_val: mp.mpf) -> mp.mpf:
    """Solve QOU Form-B Bring-Schwinger cubic for `alpha_EM^{-1}(q)` at 85 dps."""
    with mp.workdps(85):
        q = mp.mpf(q_val)
        one = mp.mpf(1)
        h = q - one / q
        h2 = h * h
        two_q = q + one / q
        q9 = (q ** 9 - q ** (-9)) / h
        q10 = (q ** 10 - q ** (-10)) / h
        t_term = q * q9 * q10 + mp.mpf(2) / (mp.mpf(3) * mp.pi)
        h_term = two_q / (mp.mpf(8) * mp.pi)
        a = (-t_term + mp.sqrt(t_term * t_term + mp.mpf(4) * h_term)) / (
            mp.mpf(2) * h_term
        )
        for _ in range(40):
            fa = -h_term * h2 * (a ** 3) + h_term * (a ** 2) + t_term * a - one
            dfa = (
                -mp.mpf(3) * h_term * h2 * (a ** 2)
                + mp.mpf(2) * h_term * a
                + t_term
            )
            da = fa / dfa
            a -= da
            if abs(da) < mp.mpf(10) ** (-80):
                break
        return one / a


def solve_ew_vev_cubic(q_val: mp.mpf) -> tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    """Solve `ElectroweakBringSchwingerBridge.ewFixedPointCubic` at 85 dps.

    Returns `(N_v_pred, alpha_v_root, T_EW, H_hab)`.
    """
    with mp.workdps(85):
        q = mp.mpf(q_val)
        one = mp.mpf(1)
        hbar_q = one - one / q
        q2 = qbal(2, q)
        bare = q * qbal(4, q) * qbal(6, q) * qbal(8, q)
        tree = bare * (q2 / mp.mpf(2))
        t_ew = tree + one / mp.pi
        h_hab = q2 / (mp.mpf(8) * mp.pi)
        a = one / t_ew
        for _ in range(40):
            fa = (
                (hbar_q ** 2) * h_hab * (a ** 3)
                - h_hab * (a ** 2)
                + t_ew * a
                - one
            )
            dfa = (
                mp.mpf(3) * (hbar_q ** 2) * h_hab * (a ** 2)
                - mp.mpf(2) * h_hab * a
                + t_ew
            )
            da = fa / dfa
            a -= da
            if abs(da) < mp.mpf(10) ** (-80):
                break
        return one / a, a, t_ew, h_hab


def sm_beta_constants() -> tuple[list[mp.mpf], list[list[mp.mpf]], list[mp.mpf]]:
    """Exact rational 1-loop `b_i`, 2-loop Machacek-Vaughn `b_{ij}`, and top-Yukawa `c_i`."""
    b1 = [
        mp.mpf(41) / mp.mpf(10),
        -mp.mpf(19) / mp.mpf(6),
        -mp.mpf(7),
    ]
    b2 = [
        [mp.mpf(199) / mp.mpf(50), mp.mpf(27) / mp.mpf(10), mp.mpf(44) / mp.mpf(5)],
        [mp.mpf(9) / mp.mpf(10), mp.mpf(35) / mp.mpf(6), mp.mpf(12)],
        [mp.mpf(11) / mp.mpf(10), mp.mpf(9) / mp.mpf(2), -mp.mpf(26)],
    ]
    c_top = [
        mp.mpf(17) / mp.mpf(10),
        mp.mpf(3) / mp.mpf(2),
        mp.mpf(2),
    ]
    return b1, b2, c_top


def integrate_sm_2loop_taylor(
    inv_a0: list[mp.mpf],
    log_ratio: mp.mpf,
    include_top_yukawa: bool = False,
    n_steps: int = 100,
    order: int = 38,
) -> tuple[bool, list[mp.mpf]]:
    """Integrate 2-loop SM RG ODE `d(alpha_i^{-1})/du = b_i/(2*pi) + sum_j b_{ij}/(8*pi^2 * alpha_j^{-1}) - c_i*alpha_t/(8*pi^2)`
    from `u = 0` (`mu = mu_UV`) to `u = log_ratio` (`mu = M_Z`) via power-series stepping.

    Returns `(regular, y_final)` where `regular` is `False` if any `alpha_i^{-1}(u) <= 0.05`
    along `[0, log_ratio]` (2-loop infrared Landau pole reached above `M_Z`).
    """
    b1, b2, c_top = sm_beta_constants()
    two_pi = mp.mpf(2) * mp.pi
    eight_pi2 = mp.mpf(8) * (mp.pi ** 2)
    alpha_t = (mp.mpf(1) / (mp.mpf(4) * mp.pi)) if include_top_yukawa else mp.mpf(0)

    const_drift = [
        b1[i] / two_pi - c_top[i] * alpha_t / eight_pi2 for i in range(3)
    ]
    coup_mat = [[b2[i][j] / eight_pi2 for j in range(3)] for i in range(3)]

    du = log_ratio / mp.mpf(n_steps)
    y = [mp.mpf(v) for v in inv_a0]
    one = mp.mpf(1)
    pole_floor = mp.mpf("0.05")

    for _ in range(n_steps):
        if y[0] <= pole_floor or y[1] <= pole_floor or y[2] <= pole_floor:
            return False, y
        y_c = [[mp.mpf(0)] * (order + 1) for _ in range(3)]
        z_c = [[mp.mpf(0)] * order for _ in range(3)]
        for i in range(3):
            y_c[i][0] = y[i]
            z_c[i][0] = one / y[i]
        for m in range(order):
            if m > 0:
                for j in range(3):
                    s = mp.mpf(0)
                    for r in range(1, m + 1):
                        s += y_c[j][r] * z_c[j][m - r]
                    z_c[j][m] = -s / y_c[j][0]
            inv_mp1 = one / mp.mpf(m + 1)
            for i in range(3):
                c_sum = (
                    coup_mat[i][0] * z_c[0][m]
                    + coup_mat[i][1] * z_c[1][m]
                    + coup_mat[i][2] * z_c[2][m]
                )
                if m == 0:
                    y_c[i][1] = const_drift[i] + c_sum
                else:
                    y_c[i][m + 1] = inv_mp1 * c_sum
        for i in range(3):
            acc = y_c[i][order]
            for m in range(order - 1, -1, -1):
                acc = acc * du + y_c[i][m]
            y[i] = acc
        if y[0] <= pole_floor or y[1] <= pole_floor or y[2] <= pole_floor:
            return False, y
    return True, y


def solve_unified_2loop_at_log_ratio(
    log_ratio: mp.mpf,
    target_inv_alpha_em_mz: mp.mpf,
    include_top_yukawa: bool = False,
) -> tuple[bool, mp.mpf, list[mp.mpf]]:
    """Find unified `inv_alpha_UV` (`alpha_1 = alpha_2 = alpha_3` at `u = 0`) such that
    `(5/3)*alpha_1^{-1}(L) + alpha_2^{-1}(L) = target_inv_alpha_em_mz` at 2-loop via secant steps.

    Returns `(regular, inv_alpha_UV, y_final)`. If the 2-loop QCD Landau pole is reached
    before `M_Z` (`L > ~34.45`), returns `(False, x_1loop, y_pole)`.
    """
    with mp.workdps(84):
        five_thirds = mp.mpf(5) / mp.mpf(3)
        eight_thirds = mp.mpf(8) / mp.mpf(3)
        eleven_thirds = mp.mpf(11) / mp.mpf(3)
        t_step = log_ratio / (mp.mpf(2) * mp.pi)
        x0 = (target_inv_alpha_em_mz - eleven_thirds * t_step) / eight_thirds
        ok0, y0 = integrate_sm_2loop_taylor(
            [x0, x0, x0], log_ratio, include_top_yukawa=include_top_yukawa
        )
        if not ok0:
            return False, x0, y0
        f0 = five_thirds * y0[0] + y0[1] - target_inv_alpha_em_mz
        x1 = x0 - f0 / eight_thirds
        for _ in range(14):
            ok1, y1 = integrate_sm_2loop_taylor(
                [x1, x1, x1], log_ratio, include_top_yukawa=include_top_yukawa
            )
            if not ok1:
                return False, x1, y1
            f1 = five_thirds * y1[0] + y1[1] - target_inv_alpha_em_mz
            if abs(f1) < mp.mpf(10) ** (-72):
                ok_f, yf = integrate_sm_2loop_taylor(
                    [x1, x1, x1],
                    log_ratio,
                    include_top_yukawa=include_top_yukawa,
                    n_steps=150,
                    order=48,
                )
                return ok_f, x1, yf
            denom = f1 - f0
            if denom == mp.mpf(0):
                break
            x_next = x1 - f1 * (x1 - x0) / denom
            x0, f0 = x1, f1
            x1 = x_next
        ok_f, yf = integrate_sm_2loop_taylor(
            [x1, x1, x1],
            log_ratio,
            include_top_yukawa=include_top_yukawa,
            n_steps=150,
            order=48,
        )
        return ok_f, x1, yf


def solve_alpha_s_2loop_from_lambda5(mu_gev: mp.mpf, lambda5_gev: mp.mpf) -> mp.mpf:
    """Solve exact PDG 2-loop implicit QCD RG relation for `alpha_s(mu)` at `n_f = 5`:
    `ln(mu^2 / Lambda^2) = 1/(beta_0 * a_s) + (beta_1 / beta_0^2) * ln(beta_0 * a_s / (1 + (beta_1/beta_0)*a_s))`
    where `a_s = alpha_s / (4*pi)`, `beta_0 = 23/3`, `beta_1 = 116/3`.
    """
    with mp.workdps(85):
        one = mp.mpf(1)
        four_pi = mp.mpf(4) * mp.pi
        b0 = mp.mpf(23) / mp.mpf(3)
        b1 = mp.mpf(116) / mp.mpf(3)
        l2 = mp.mpf(2) * mp.log(mu_gev / lambda5_gev)
        a_s = one / (b0 * l2) * (one - (b1 / (b0 ** 2)) * mp.log(l2) / l2)
        for _ in range(45):
            rhs = one / (b0 * a_s) + (b1 / (b0 ** 2)) * mp.log(
                (b0 * a_s) / (one + (b1 / b0) * a_s)
            )
            res = rhs - l2
            # Exact derivative d(rhs)/d(a_s) = -1 / (b0 * a_s^2 + b1 * a_s^3)
            drhs = -one / (b0 * (a_s ** 2) + b1 * (a_s ** 3))
            da = res / drhs
            a_s -= da
            if abs(da) < mp.mpf(10) ** (-80):
                break
        return four_pi * a_s


def main() -> int:
    with mp.workdps(WORK_DPS):
        one = mp.mpf(1)
        two = mp.mpf(2)
        q0 = q_at(WORK_DPS)
        h0 = q0 - one / q0
        hbar_q0 = one - one / q0
        u0 = q0 ** 2 - one  # single-passage Sweedler factor q_0 * (q_0 - q_0^{-1})

        me_mev = codata("electron mass energy equivalent in MeV").value
        mp_mev = codata("proton mass energy equivalent in MeV").value
        me_gev = me_mev / mp.mpf(1000)
        mp_gev = mp_mev / mp.mpf(1000)
        mpi_gev = M_PI_CHARGED_MEV / mp.mpf(1000)

        alpha_q_inv_0 = solve_form_b_alpha_inv(q0)
        alpha_q_0 = one / alpha_q_inv_0

        # Derived PDG comparison quantities
        v_ew_pdg = one / mp.sqrt(mp.sqrt(two) * PDG_GF_GEV_INV2)
        v_ew_pdg_sig = v_ew_pdg * PDG_GF_SIG_GEV_INV2 / (two * PDG_GF_GEV_INV2)
        nv_pdg = v_ew_pdg / mp_gev
        gf_mp2_pdg = PDG_GF_GEV_INV2 * (mp_gev ** 2)
        lam_h_pdg = (PDG_MH_GEV ** 2) / (two * (v_ew_pdg ** 2))

        # ------------------------------------------------------------------
        # 0. Catalan constant exact Clausen series vs certified 24-term sum
        # ------------------------------------------------------------------
        g_cat = mp.catalan
        g_cat_rat24 = mp.mpf(102476291858462752) / mp.mpf(111983464450883025)
        g_cat_24_err = abs(g_cat - g_cat_rat24)
        g_cat_retired_diff = abs(g_cat - mp.mpf(RETIRED_CATALAN_DECIMAL_STR))

        # ------------------------------------------------------------------
        # Part A: Sweedler `(q_0^2 - 1)^k` vs Bring-Schwinger `v_EW`, `M_W`, `M_Z`, `m_H`
        # ------------------------------------------------------------------
        # Sweedler powers:
        sweedler_amp1 = u0
        sweedler_rate1 = u0 ** 2
        sweedler_amp2 = u0 ** 2
        sweedler_rate2 = u0 ** 4
        sweedler_amp4 = u0 ** 4
        sweedler_rate4 = u0 ** 8

        two_quarter = two ** (one / mp.mpf(4))
        inv_two_quarter = one / two_quarter

        # S1 (`#9204` direct Frobenius-norm identification `G_F m_p^2 = (q_0^2 - 1)^8`):
        gf_mp2_s1 = sweedler_rate4
        gf_s1_gev_inv2 = gf_mp2_s1 / (mp_gev ** 2)
        gf_s1_rel_err_pct = (gf_mp2_s1 - gf_mp2_pdg) / gf_mp2_pdg * mp.mpf(100)
        nv_s1_bare = one / sweedler_amp4  # (q_0^2 - 1)^{-4} = 344.871...
        nv_s1_fermi = inv_two_quarter * nv_s1_bare  # 2^{-1/4} * (q_0^2 - 1)^{-4} = 290.000...
        v_s1_bare_gev = nv_s1_bare * mp_gev
        v_s1_fermi_gev = nv_s1_fermi * mp_gev
        v_s1_bare_err_pct = (v_s1_bare_gev - v_ew_pdg) / v_ew_pdg * mp.mpf(100)
        v_s1_fermi_err_pct = (v_s1_fermi_gev - v_ew_pdg) / v_ew_pdg * mp.mpf(100)

        # S2 (`G_F m_model^2 = (q_0^2 - 1)^4 <=> v_EW / m_model = 2^{-1/4} (q_0^2 - 1)^{-2}`):
        e0_full_gev = me_gev / (q0 * (q0 - one) * (one - hbar_q0 ** 2))
        e0_mu_gev = me_gev / ((q0 - one) ** 2)
        s2_scales = {}
        for key, m_mod in [
            ("S2a_proton_mp", mp_gev),
            ("S2b_CAL3_pion", mpi_gev),
            ("S2c_tower_E0_full", e0_full_gev),
            ("S2d_muon_unit_E0_mu", e0_mu_gev),
        ]:
            v_bare = m_mod / sweedler_amp2
            v_fermi = inv_two_quarter * v_bare
            s2_scales[key] = {
                "m_model_GeV": fmt(m_mod, dps=OUT_DPS),
                "v_EW_bare_q2m1_inv2_GeV": fmt(v_bare, dps=OUT_DPS),
                "v_EW_fermi_2m14_q2m1_inv2_GeV": fmt(v_fermi, dps=OUT_DPS),
                "rel_err_fermi_pct": fmt(
                    (v_fermi - v_ew_pdg) / v_ew_pdg * mp.mpf(100), dps=OUT_DPS
                ),
            }

        # S3: Reconciliation with `ElectroweakBringSchwingerBridge` & `EwVevGaps`
        nv_bs, alpha_v_bs, t_ew_bs, h_hab_bs = solve_ew_vev_cubic(q0)
        v_bs_gev = nv_bs * mp_gev
        gf_bs_gev_inv2 = one / (mp.sqrt(two) * (v_bs_gev ** 2))
        v_bs_err_ppb = (v_bs_gev - v_ew_pdg) / v_ew_pdg * (mp.mpf(10) ** 9)
        v_bs_err_sigma = (v_bs_gev - v_ew_pdg) / v_ew_pdg_sig

        # Non-self-consistent loop test: `N(kappa) = T_EW - kappa * H * (1 - hbar_q^2 * kappa)`
        def ew_loop_eval(kappa: mp.mpf) -> mp.mpf:
            return t_ew_bs - kappa * h_hab_bs * (one - (hbar_q0 ** 2) * kappa)

        kappa_s1_bare = sweedler_amp4  # (q_0^2 - 1)^4 = 0.00289962... < 1/30
        kappa_s1_fermi = two_quarter * sweedler_amp4  # 2^{1/4} * (q_0^2 - 1)^4 = 0.00344825... < 1/30
        alpha2_pdg = mp.sqrt(two) * PDG_GF_GEV_INV2 * (PDG_MW_GEV ** 2) / mp.pi

        nv_loop_s1_bare = ew_loop_eval(kappa_s1_bare)
        nv_loop_s1_fermi = ew_loop_eval(kappa_s1_fermi)
        nv_loop_alpha2 = ew_loop_eval(alpha2_pdg)

        # Exact algebraic identity check for `ewVev_sweedler_loop_shift_eq`:
        shift_lhs = nv_loop_s1_bare - nv_bs
        shift_rhs = (
            -h_hab_bs
            * (kappa_s1_bare - alpha_v_bs)
            * (one - (hbar_q0 ** 2) * (kappa_s1_bare + alpha_v_bs))
        )
        loop_shift_identity_err = abs(shift_lhs - shift_rhs)

        ppb_loop_s1_bare = (nv_loop_s1_bare - nv_pdg) / nv_pdg * (mp.mpf(10) ** 9)
        ppb_loop_s1_fermi = (nv_loop_s1_fermi - nv_pdg) / nv_pdg * (mp.mpf(10) ** 9)
        ppb_loop_alpha2 = (nv_loop_alpha2 - nv_pdg) / nv_pdg * (mp.mpf(10) ** 9)

        # Torus-link Plancherel polynomials `P_2, P_3, P_4` & boson/Higgs masses:
        q2_bal = qbal(2, q0)
        p2_h0 = trace_poly_p(2, h0)
        p3_h0 = trace_poly_p(3, h0)
        p4_h0 = trace_poly_p(4, h0)
        r_zw_dressed = (p3_h0 / p2_h0) * ((q2_bal / two) ** 2)
        cos_thetaw_torus = one / r_zw_dressed
        sin2_thetaw_torus = one - (cos_thetaw_torus ** 2)
        r_zw_pdg = PDG_MZ_GEV / PDG_MW_GEV
        r_zw_err_ppm = (r_zw_dressed - r_zw_pdg) / r_zw_pdg * (mp.mpf(10) ** 6)

        # Perturbative zero-input QOU Form-B `alpha_EM(M_Z)` running from `m_e` to `M_Z`
        # Using CAL-1 `m_e`, CAL-2 proxy `m_mu = m_e * Vol(4_1)/hbar_q^2`, and proton/pion hadronic threshold `m_p`:
        vol_4_1 = two * mp.clsin(2, mp.pi / mp.mpf(3))
        mmu_cal2_gev = me_gev * vol_4_1 / (hbar_q0 ** 2)
        # 5 active quark flavours `(u, d, s, c, b)` above hadronic threshold `m_p` + 3 charged leptons:
        # `(2/(3*pi)) * [ln(M_Z/m_e) + ln(M_Z/m_mu) + ln(M_Z/m_p) + 3*(4/9 + 1/9 + 1/9 + 4/9 + 1/9)*ln(M_Z/m_p)]`
        # where `sum_{5 quarks} N_c Q_q^2 = 3 * (11/9) = 11/3`:
        delta_inv_alpha_pert = (two / (mp.mpf(3) * mp.pi)) * (
            mp.log(PDG_MZ_GEV / me_gev)
            + mp.log(PDG_MZ_GEV / mmu_cal2_gev)
            + mp.log(PDG_MZ_GEV / mp_gev)
            + (mp.mpf(11) / mp.mpf(3)) * mp.log(PDG_MZ_GEV / mp_gev)
        )
        alpha_q_inv_mz_pert = alpha_q_inv_0 - delta_inv_alpha_pert

        # Absolute `M_W, M_Z` from `(v_BS, v_S1_fermi)` + torus `sin^2 theta_W`:
        e_mz_qou = mp.sqrt(mp.mpf(4) * mp.pi / alpha_q_inv_mz_pert)
        e_mz_pdg = mp.sqrt(mp.mpf(4) * mp.pi / PDG_ALPHA_EM_INV_MZ_MSBAR)
        mw_from_bs_torus_qou = (e_mz_qou / (two * mp.sqrt(sin2_thetaw_torus))) * v_bs_gev
        mz_from_bs_torus_qou = mw_from_bs_torus_qou * r_zw_dressed
        mw_from_bs_torus_pdg_aem = (e_mz_pdg / (two * mp.sqrt(sin2_thetaw_torus))) * v_bs_gev
        mz_from_bs_torus_pdg_aem = mw_from_bs_torus_pdg_aem * r_zw_dressed
        mw_from_s1_torus_qou = (e_mz_qou / (two * mp.sqrt(sin2_thetaw_torus))) * v_s1_fermi_gev
        mz_from_s1_torus_qou = mw_from_s1_torus_qou * r_zw_dressed

        # Higgs mass & quartic `lambda_H = m_H^2 / (2 v^2)` across pre-registered H0..H3:
        six_fifths = mp.mpf(6) / mp.mpf(5)
        borromean_corr = one - two * g_cat * (h0 ** 4)
        bring_zero_corr = one - (two / (mp.mpf(3) * mp.pi)) * (hbar_q0 ** 2)

        higgs_table = {}
        for h_key, mw_anchor, v_anchor, factor in [
            ("H0_undressed_2G_PDG_MW", PDG_MW_GEV, v_bs_gev, borromean_corr),
            ("H1_dressed_tree_PDG_MW", PDG_MW_GEV, v_bs_gev, q2_bal / two),
            ("H2_dressed_2G_PDG_MW", PDG_MW_GEV, v_bs_gev, (q2_bal / two) * borromean_corr),
            ("H3_dressed_BringZero_PDG_MW", PDG_MW_GEV, v_bs_gev, (q2_bal / two) * bring_zero_corr),
            ("H1_dressed_tree_from_PDG_MZ", PDG_MZ_GEV / r_zw_dressed, v_bs_gev, q2_bal / two),
            ("H3_dressed_BringZero_from_BS_torus_MW", mw_from_bs_torus_pdg_aem, v_bs_gev, (q2_bal / two) * bring_zero_corr),
            ("H3_dressed_BringZero_from_S1_torus_MW", mw_from_s1_torus_qou, v_s1_fermi_gev, (q2_bal / two) * bring_zero_corr),
        ]:
            mh_val = mw_anchor * (p4_h0 / p2_h0) * six_fifths * factor
            lam_h_val = (mh_val ** 2) / (two * (v_anchor ** 2))
            higgs_table[h_key] = {
                "m_H_GeV": fmt(mh_val, dps=OUT_DPS),
                "lambda_H_quartic": fmt(lam_h_val, dps=OUT_DPS),
                "m_H_err_pct": fmt((mh_val - PDG_MH_GEV) / PDG_MH_GEV * mp.mpf(100), dps=OUT_DPS),
                "m_H_err_sigma": fmt((mh_val - PDG_MH_GEV) / PDG_MH_SIG_GEV, dps=OUT_DPS),
                "lambda_H_err_pct": fmt((lam_h_val - lam_h_pdg) / lam_h_pdg * mp.mpf(100), dps=OUT_DPS),
            }

        # ------------------------------------------------------------------
        # Part B: 1-Loop & 2-Loop SM RG Threshold Running (`sin^2 theta_W`, `alpha_s`)
        # ------------------------------------------------------------------
        b1_vec, _, _ = sm_beta_constants()
        # Verify 2-loop Taylor ODE convergence (`n_steps=150` vs `n_steps=300`) at `L = 32`:
        test_l = mp.mpf(32)
        _, ode_150 = integrate_sm_2loop_taylor([mp.mpf(42)] * 3, test_l, n_steps=150, order=48)
        _, ode_300 = integrate_sm_2loop_taylor([mp.mpf(42)] * 3, test_l, n_steps=300, order=48)
        max_ode_conv_err = max(abs(ode_150[i] - ode_300[i]) for i in range(3))

        # Pre-registered candidate UV-to-M_Z log-ratios `L = ln(mu_UV / M_Z)`:
        neg_ln_u0 = -mp.log(u0)  # -ln(q_0^2 - 1) = 1.460785...
        candidate_thresholds = [
            ("T1_sweedler_k4", mp.mpf(4) * neg_ln_u0),
            ("T2_sweedler_k8", mp.mpf(8) * neg_ln_u0),
            ("T3_sweedler_k16", mp.mpf(16) * neg_ln_u0),
            ("T3_sweedler_k17", mp.mpf(17) * neg_ln_u0),
            ("T3_sweedler_k18", mp.mpf(18) * neg_ln_u0),
            ("T3_sweedler_k20_lcm45", mp.mpf(20) * neg_ln_u0),
            ("T3_sweedler_k21", mp.mpf(21) * neg_ln_u0),
            ("T3_sweedler_k22_su2_22", mp.mpf(22) * neg_ln_u0),
            ("T3_sweedler_k24_4chi", mp.mpf(24) * neg_ln_u0),
            ("T4a_kashaev_pi_over_hbarq", mp.pi / hbar_q0),
            ("T4b_quarter_alpha_q_inv", alpha_q_inv_0 / mp.mpf(4)),
            ("T4c_bring_area_12pi", mp.mpf(12) * mp.pi),
        ]

        rg_threshold_results = {}
        five_thirds = mp.mpf(5) / mp.mpf(3)
        three_eighths = mp.mpf(3) / mp.mpf(8)

        for th_name, l_val in candidate_thresholds:
            t_1loop = l_val / (two * mp.pi)
            entry = {
                "ln_muUV_over_MZ": fmt(l_val, dps=OUT_DPS),
                "muUV_over_MZ_log10": fmt(l_val / mp.log(mp.mpf(10)), dps=OUT_DPS),
            }
            for aem_tag, inv_aem_mz in [
                ("QOU_pert_alphaEM", alpha_q_inv_mz_pert),
                ("PDG_MSbar_alphaEM", PDG_ALPHA_EM_INV_MZ_MSBAR),
            ]:
                # 1-loop exact Georgi-Quinn-Weinberg & unified alpha_3:
                inv_auv_1l = (inv_aem_mz - (mp.mpf(11) / mp.mpf(3)) * t_1loop) * three_eighths
                sin2_1l = three_eighths - (mp.mpf(109) / mp.mpf(24)) * t_1loop / inv_aem_mz
                inv_a3_1l = three_eighths * inv_aem_mz - (mp.mpf(67) / mp.mpf(8)) * t_1loop
                alpha_s_1l = (one / inv_a3_1l) if inv_a3_1l > mp.mpf(0) else mp.mpf(-1)

                # Verify Lean `smTriangleInv` = 0 on unified 1-loop trajectory:
                inv_a1_1l = inv_auv_1l + b1_vec[0] * t_1loop
                inv_a2_1l = inv_auv_1l + b1_vec[1] * t_1loop
                tri_1l = mp.mpf(115) * inv_a1_1l - mp.mpf(333) * inv_a2_1l + mp.mpf(218) * inv_a3_1l

                # 2-loop pure gauge-matter (`b_{ij}`):
                ok_g, _, y_2l_gauge = solve_unified_2loop_at_log_ratio(
                    l_val, inv_aem_mz, include_top_yukawa=False
                )
                if ok_g:
                    sin2_2l_gauge = y_2l_gauge[1] / (five_thirds * y_2l_gauge[0] + y_2l_gauge[1])
                    alpha_s_2l_gauge = one / y_2l_gauge[2]
                    status_g = "regular"
                    sin2_2l_g_str = fmt(sin2_2l_gauge, dps=OUT_DPS)
                    sin2_2l_g_err_str = fmt(
                        (sin2_2l_gauge - PDG_SIN2_THETAW_MSBAR)
                        / PDG_SIN2_THETAW_MSBAR
                        * mp.mpf(100),
                        dps=OUT_DPS,
                    )
                    as_2l_g_str = fmt(alpha_s_2l_gauge, dps=OUT_DPS)
                    as_2l_g_err_str = fmt(
                        (alpha_s_2l_gauge - PDG_ALPHA_S_MZ) / PDG_ALPHA_S_MZ * mp.mpf(100),
                        dps=OUT_DPS,
                    )
                else:
                    status_g = "qcd_2loop_landau_pole_above_MZ"
                    sin2_2l_g_str = "landau_pole"
                    sin2_2l_g_err_str = "landau_pole"
                    as_2l_g_str = "landau_pole"
                    as_2l_g_err_str = "landau_pole"

                # 2-loop with `y_t = 1` top Yukawa:
                ok_t, _, y_2l_top = solve_unified_2loop_at_log_ratio(
                    l_val, inv_aem_mz, include_top_yukawa=True
                )
                if ok_t:
                    sin2_2l_top = y_2l_top[1] / (five_thirds * y_2l_top[0] + y_2l_top[1])
                    alpha_s_2l_top = one / y_2l_top[2]
                    sin2_2l_t_str = fmt(sin2_2l_top, dps=OUT_DPS)
                    as_2l_t_str = fmt(alpha_s_2l_top, dps=OUT_DPS)
                else:
                    sin2_2l_t_str = "landau_pole"
                    as_2l_t_str = "landau_pole"

                entry[aem_tag] = {
                    "two_loop_status": status_g,
                    "sin2_thetaW_1loop": fmt(sin2_1l, dps=OUT_DPS),
                    "sin2_thetaW_1loop_err_pct": fmt(
                        (sin2_1l - PDG_SIN2_THETAW_MSBAR) / PDG_SIN2_THETAW_MSBAR * mp.mpf(100),
                        dps=OUT_DPS,
                    ),
                    "alpha_s_1loop_unified": fmt(alpha_s_1l, dps=OUT_DPS),
                    "alpha_s_1loop_err_pct": fmt(
                        (alpha_s_1l - PDG_ALPHA_S_MZ) / PDG_ALPHA_S_MZ * mp.mpf(100),
                        dps=OUT_DPS,
                    ),
                    "triangle_invariant_1loop_residual": fmt(abs(tri_1l), dps=20),
                    "sin2_thetaW_2loop_gauge": sin2_2l_g_str,
                    "sin2_thetaW_2loop_gauge_err_pct": sin2_2l_g_err_str,
                    "alpha_s_2loop_gauge_unified": as_2l_g_str,
                    "alpha_s_2loop_gauge_err_pct": as_2l_g_err_str,
                    "sin2_thetaW_2loop_with_top": sin2_2l_t_str,
                    "alpha_s_2loop_with_top_unified": as_2l_t_str,
                }
            rg_threshold_results[th_name] = entry

        # Inverse diagnostic: exact `L*` required for `sin^2 theta_W(M_Z) = 0.23122` at 1-loop & 2-loop,
        # and minimal-SM coupling triangle mismatch at PDG `(alpha_EM, sin^2 theta_W, alpha_s)`:
        l_star_1loop_pdg = (
            (three_eighths - PDG_SIN2_THETAW_MSBAR)
            * PDG_ALPHA_EM_INV_MZ_MSBAR
            * (mp.mpf(48) * mp.pi / mp.mpf(109))
        )
        k_eff_1loop_pdg = l_star_1loop_pdg / neg_ln_u0
        t_star_1loop = l_star_1loop_pdg / (two * mp.pi)
        inv_a3_at_lstar_1l = (
            three_eighths * PDG_ALPHA_EM_INV_MZ_MSBAR - (mp.mpf(67) / mp.mpf(8)) * t_star_1loop
        )
        alpha_s_at_lstar_1l = one / inv_a3_at_lstar_1l

        # Exact 2-loop `L*` via secant search around `l_star_1loop_pdg`:
        la = l_star_1loop_pdg
        lb = l_star_1loop_pdg + mp.mpf("0.1")
        _, _, ya = solve_unified_2loop_at_log_ratio(la, PDG_ALPHA_EM_INV_MZ_MSBAR)
        fa = ya[1] / (five_thirds * ya[0] + ya[1]) - PDG_SIN2_THETAW_MSBAR
        for _ in range(12):
            _, _, yb = solve_unified_2loop_at_log_ratio(lb, PDG_ALPHA_EM_INV_MZ_MSBAR)
            fb = yb[1] / (five_thirds * yb[0] + yb[1]) - PDG_SIN2_THETAW_MSBAR
            if abs(fb) < mp.mpf(10) ** (-70):
                break
            lnext = lb - fb * (lb - la) / (fb - fa)
            la, fa = lb, fb
            lb = lnext
        l_star_2loop_pdg = lb
        k_eff_2loop_pdg = l_star_2loop_pdg / neg_ln_u0
        _, _, y_at_lstar_2l = solve_unified_2loop_at_log_ratio(
            l_star_2loop_pdg, PDG_ALPHA_EM_INV_MZ_MSBAR
        )
        alpha_s_at_lstar_2l = one / y_at_lstar_2l[2]

        # Empirical minimal-SM triangle invariant at PDG `M_Z` couplings:
        inv_a2_pdg_mz = PDG_SIN2_THETAW_MSBAR * PDG_ALPHA_EM_INV_MZ_MSBAR
        inv_a1_pdg_mz = (mp.mpf(3) / mp.mpf(5)) * (PDG_ALPHA_EM_INV_MZ_MSBAR - inv_a2_pdg_mz)
        inv_a3_pdg_mz = one / PDG_ALPHA_S_MZ
        sm_triangle_pdg_mz = (
            mp.mpf(115) * inv_a1_pdg_mz
            - mp.mpf(333) * inv_a2_pdg_mz
            + mp.mpf(218) * inv_a3_pdg_mz
        )

        # ------------------------------------------------------------------
        # Part B.3: Zero-parameter infrared QCD `Lambda_QCD -> alpha_s(M_Z)` bridge
        # ------------------------------------------------------------------
        b0_nf5 = mp.mpf(23) / mp.mpf(3)
        qcd_ir_candidates = {}
        for qcd_key, lam_gev in [
            ("Q1_sweedler_mp_q02m1", mp_gev * u0),
            ("Q2_hecke_mp_h0", mp_gev * h0),
            ("Q3_CAL3_mpi_charged", mpi_gev),
            ("Q4_habiro_mp_hbarq", mp_gev * hbar_q0),
        ]:
            as_1loop = (two * mp.pi) / (b0_nf5 * mp.log(PDG_MZ_GEV / lam_gev))
            as_2loop = solve_alpha_s_2loop_from_lambda5(PDG_MZ_GEV, lam_gev)
            # Also evaluate using QOU Bring-Schwinger torus `M_Z` (`mz_from_bs_torus_qou`) so zero PDG `M_Z` enters:
            as_2loop_qou_mz = solve_alpha_s_2loop_from_lambda5(mz_from_bs_torus_qou, lam_gev)
            qcd_ir_candidates[qcd_key] = {
                "Lambda_MeV": fmt(lam_gev * mp.mpf(1000), dps=OUT_DPS),
                "alpha_s_MZ_1loop": fmt(as_1loop, dps=OUT_DPS),
                "alpha_s_MZ_1loop_err_pct": fmt(
                    (as_1loop - PDG_ALPHA_S_MZ) / PDG_ALPHA_S_MZ * mp.mpf(100), dps=OUT_DPS
                ),
                "alpha_s_MZ_2loop_PDG_MZ": fmt(as_2loop, dps=OUT_DPS),
                "alpha_s_MZ_2loop_err_pct": fmt(
                    (as_2loop - PDG_ALPHA_S_MZ) / PDG_ALPHA_S_MZ * mp.mpf(100), dps=OUT_DPS
                ),
                "alpha_s_MZ_2loop_err_sigma": fmt(
                    (as_2loop - PDG_ALPHA_S_MZ) / PDG_ALPHA_S_MZ_SIG, dps=OUT_DPS
                ),
                "alpha_s_MZ_2loop_QOU_MZ": fmt(as_2loop_qou_mz, dps=OUT_DPS),
                "alpha_s_MZ_2loop_QOU_MZ_err_sigma": fmt(
                    (as_2loop_qou_mz - PDG_ALPHA_S_MZ) / PDG_ALPHA_S_MZ_SIG, dps=OUT_DPS
                ),
            }

        # Print concise 80-dps summary (using `fmt` / `mp.nstr`, zero `float(...)` calls):
        print("=== SM8W EWSB + SWEEDLER + M_Z RG PROBE (80 dps, proton pin) ===")
        print(f"  q0 (proton pin)                      = {fmt(q0, dps=30)}")
        print(f"  q0^2 - 1 (Sweedler 1-passage)        = {fmt(u0, dps=25)}")
        print(f"  Catalan |G - S_24| (<= 1/24)         = {fmt(g_cat_24_err, dps=18)}")
        print(f"  Catalan retired-literal drift        = {fmt(g_cat_retired_diff, dps=12)}")
        print()
        print("  -- Part A: Sweedler vs Bring-Schwinger v_EW & Higgs Quartic --")
        print(f"  S1 G_F*m_p^2 = (q0^2-1)^8            = {fmt(gf_mp2_s1, dps=16)} ({fmt(gf_s1_rel_err_pct, dps=6)}% vs PDG)")
        print(f"  S1 v_EW = 2^(-1/4)*(q0^2-1)^(-4)*m_p = {fmt(v_s1_fermi_gev, dps=14)} GeV ({fmt(v_s1_fermi_err_pct, dps=6)}%)")
        print(f"  S2a v_EW = 2^(-1/4)*(q0^2-1)^(-2)*m_p= {s2_scales['S2a_proton_mp']['v_EW_fermi_2m14_q2m1_inv2_GeV'][:16]} GeV ({s2_scales['S2a_proton_mp']['rel_err_fermi_pct'][:8]}%)")
        print(f"  BS self-consistent v_EW              = {fmt(v_bs_gev, dps=16)} GeV ({fmt(v_bs_err_ppb, dps=6)} ppb, {fmt(v_bs_err_sigma, dps=5)} sigma)")
        print(f"  EwVevGaps loop w/ kappa=(q0^2-1)^4   = {fmt(nv_loop_s1_bare * mp_gev, dps=16)} GeV ({fmt(ppb_loop_s1_bare, dps=6)} ppb)")
        print(f"  EwVevGaps loop w/ kappa=2^(1/4)u0^4  = {fmt(nv_loop_s1_fermi * mp_gev, dps=16)} GeV ({fmt(ppb_loop_s1_fermi, dps=6)} ppb)")
        print(f"  EwVevGaps loop w/ kappa=alpha_2      = {fmt(nv_loop_alpha2 * mp_gev, dps=16)} GeV ({fmt(ppb_loop_alpha2, dps=6)} ppb)")
        print(f"  Torus M_Z/M_W dressed                = {fmt(r_zw_dressed, dps=14)} ({fmt(r_zw_err_ppm, dps=6)} ppm), sin^2 theta_W^torus = {fmt(sin2_thetaw_torus, dps=12)}")
        for hk, hv in higgs_table.items():
            print(f"    {hk:<40} m_H = {hv['m_H_GeV'][:12]} GeV ({hv['m_H_err_pct'][:8]}%, {hv['m_H_err_sigma'][:7]} sig), lam_H = {hv['lambda_H_quartic'][:12]}")
        print()
        print("  -- Part B: UV-to-M_Z RG Thresholds (PDG_MSbar_alphaEM / QOU_pert_alphaEM) --")
        for th_name, entry in rg_threshold_results.items():
            p_res = entry["PDG_MSbar_alphaEM"]
            q_res = entry["QOU_pert_alphaEM"]
            print(
                f"    {th_name:<28} L={entry['ln_muUV_over_MZ'][:9]} | "
                f"PDG-aEM 2L sin^2={p_res['sin2_thetaW_2loop_gauge'][:10]} ({p_res['sin2_thetaW_2loop_gauge_err_pct'][:7]}%), a_s={p_res['alpha_s_2loop_gauge_unified'][:9]} | "
                f"QOU-aEM 2L sin^2={q_res['sin2_thetaW_2loop_gauge'][:10]}"
            )
        print(f"  1-loop target L*(sin^2=0.23122)      = {fmt(l_star_1loop_pdg, dps=12)} (k_eff = {fmt(k_eff_1loop_pdg, dps=10)}, unified a_s = {fmt(alpha_s_at_lstar_1l, dps=10)})")
        print(f"  2-loop target L*(sin^2=0.23122)      = {fmt(l_star_2loop_pdg, dps=12)} (k_eff = {fmt(k_eff_2loop_pdg, dps=10)}, unified a_s = {fmt(alpha_s_at_lstar_2l, dps=10)})")
        print(f"  Minimal-SM triangle inv at PDG M_Z   = {fmt(sm_triangle_pdg_mz, dps=12)} (!= 0)")
        print()
        print("  -- Part B.3: Zero-Parameter IR QCD Lambda -> alpha_s(M_Z) --")
        for qk, qv in qcd_ir_candidates.items():
            print(
                f"    {qk:<28} Lambda={qv['Lambda_MeV'][:10]} MeV | "
                f"1L a_s={qv['alpha_s_MZ_1loop'][:10]} | "
                f"2L a_s={qv['alpha_s_MZ_2loop_PDG_MZ'][:10]} ({qv['alpha_s_MZ_2loop_err_pct'][:7]}%, {qv['alpha_s_MZ_2loop_err_sigma'][:6]} sig) | "
                f"QOU-MZ 2L a_s={qv['alpha_s_MZ_2loop_QOU_MZ'][:10]}"
            )

        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath")
        wb.set_description(
            "80-dps (50-dps serialized) pre-registered evaluation of Standard Model Package 3 "
            "(qou-ewsb / Q-Gap-9): Sweedler (q0^2 - 1)^k weak suppression vs Bring-Schwinger "
            "v_EW (-29.37 ppb self-consistent, +81.13 ppb / +248.39 ppb non-self-consistent "
            "Sweedler loop escaping EwVevGaps.su2_coupling_not_selfConsistent), exact Catalan "
            "remediation in HiggsCategoricalMassFormula.lean, M_W / M_Z / m_H / lambda_H "
            "predictions (H3 m_H = 125.230 GeV, +0.27 sigma; H2 m_H = 125.052 GeV, -1.34 sigma), "
            "and zero-parameter 1-loop & 2-loop SM RG running across Sweedler, Kashaev, and Bring "
            "thresholds plus IR QCD Lambda_QCD = m_p*(q0^2 - 1) -> alpha_s(M_Z) = 0.11849 (+0.54 sigma)."
        )
        wb.set_content_block("prose:sm-params-higgs")

        wb.add_parameter("q0", fmt(q0, dps=OUT_DPS))
        wb.add_parameter("q0_pin", "proton (qou_substrate.constants.q_at)")
        wb.add_parameter("work_dps", WORK_DPS)
        wb.add_parameter("output_dps", OUT_DPS)
        wb.add_parameter("alpha_EM_inv_FormB_q0", fmt(alpha_q_inv_0, dps=OUT_DPS))
        wb.add_parameter("alpha_EM_inv_MZ_QOU_pert", fmt(alpha_q_inv_mz_pert, dps=OUT_DPS))
        wb.add_parameter("catalan_G_Cl2_pi_div_2", fmt(g_cat, dps=OUT_DPS))
        wb.add_parameter("catalan_retired_literal_abs_diff", fmt(g_cat_retired_diff, dps=20))

        wb.add_data(
            "part_a_sweedler_and_vev_reconciliation",
            {
                "u0_sweedler_single_passage": fmt(u0, dps=OUT_DPS),
                "sweedler_rate2_u0_pow4": fmt(sweedler_rate2, dps=OUT_DPS),
                "sweedler_rate4_u0_pow8": fmt(sweedler_rate4, dps=OUT_DPS),
                "PDG_GF_mp2": fmt(gf_mp2_pdg, dps=OUT_DPS),
                "S1_GF_mp2_rel_err_pct": fmt(gf_s1_rel_err_pct, dps=OUT_DPS),
                "S1_GF_pred_GeV_inv2": fmt(gf_s1_gev_inv2, dps=OUT_DPS),
                "S1_Nv_bare_u0_inv4": fmt(nv_s1_bare, dps=OUT_DPS),
                "S1_Nv_fermi_2m14_u0_inv4": fmt(nv_s1_fermi, dps=OUT_DPS),
                "S1_v_EW_bare_GeV": fmt(v_s1_bare_gev, dps=OUT_DPS),
                "S1_v_EW_fermi_GeV": fmt(v_s1_fermi_gev, dps=OUT_DPS),
                "S1_v_EW_bare_err_pct": fmt(v_s1_bare_err_pct, dps=OUT_DPS),
                "S1_v_EW_fermi_err_pct": fmt(v_s1_fermi_err_pct, dps=OUT_DPS),
                "S2_amplitude_squared_rate_scales": s2_scales,
                "BS_self_consistent_Nv": fmt(nv_bs, dps=OUT_DPS),
                "BS_self_consistent_v_EW_GeV": fmt(v_bs_gev, dps=OUT_DPS),
                "BS_self_consistent_GF_GeV_inv2": fmt(gf_bs_gev_inv2, dps=OUT_DPS),
                "BS_v_EW_err_ppb": fmt(v_bs_err_ppb, dps=OUT_DPS),
                "BS_v_EW_err_sigma": fmt(v_bs_err_sigma, dps=OUT_DPS),
                "PDG_v_EW_GeV": fmt(v_ew_pdg, dps=OUT_DPS),
                "EwVevGaps_loop_kappa_s1_bare_ppb": fmt(ppb_loop_s1_bare, dps=OUT_DPS),
                "EwVevGaps_loop_kappa_s1_fermi_ppb": fmt(ppb_loop_s1_fermi, dps=OUT_DPS),
                "EwVevGaps_loop_kappa_alpha2_ppb": fmt(ppb_loop_alpha2, dps=OUT_DPS),
            },
        )
        wb.add_data(
            "part_a_boson_and_higgs_quartic",
            {
                "P2_h0": fmt(p2_h0, dps=OUT_DPS),
                "P3_h0": fmt(p3_h0, dps=OUT_DPS),
                "P4_h0": fmt(p4_h0, dps=OUT_DPS),
                "r_ZW_dressed": fmt(r_zw_dressed, dps=OUT_DPS),
                "r_ZW_err_ppm": fmt(r_zw_err_ppm, dps=OUT_DPS),
                "sin2_thetaW_torus_on_shell": fmt(sin2_thetaw_torus, dps=OUT_DPS),
                "MW_from_BS_torus_QOU_aEM_GeV": fmt(mw_from_bs_torus_qou, dps=OUT_DPS),
                "MZ_from_BS_torus_QOU_aEM_GeV": fmt(mz_from_bs_torus_qou, dps=OUT_DPS),
                "MW_from_BS_torus_PDG_aEM_GeV": fmt(mw_from_bs_torus_pdg_aem, dps=OUT_DPS),
                "MZ_from_BS_torus_PDG_aEM_GeV": fmt(mz_from_bs_torus_pdg_aem, dps=OUT_DPS),
                "MW_from_S1_torus_QOU_aEM_GeV": fmt(mw_from_s1_torus_qou, dps=OUT_DPS),
                "MZ_from_S1_torus_QOU_aEM_GeV": fmt(mz_from_s1_torus_qou, dps=OUT_DPS),
                "PDG_lambda_H_tree": fmt(lam_h_pdg, dps=OUT_DPS),
                "higgs_variants": higgs_table,
            },
        )
        wb.add_data(
            "part_b_uv_to_mz_rg_thresholds",
            {
                "ode_taylor_150_vs_300_max_diff": fmt(max_ode_conv_err, dps=20),
                "l_star_1loop_for_PDG_sin2_thetaW": fmt(l_star_1loop_pdg, dps=OUT_DPS),
                "k_eff_1loop_sweedler_exponent": fmt(k_eff_1loop_pdg, dps=OUT_DPS),
                "unified_1loop_alpha_s_at_l_star": fmt(alpha_s_at_lstar_1l, dps=OUT_DPS),
                "l_star_2loop_for_PDG_sin2_thetaW": fmt(l_star_2loop_pdg, dps=OUT_DPS),
                "k_eff_2loop_sweedler_exponent": fmt(k_eff_2loop_pdg, dps=OUT_DPS),
                "unified_2loop_alpha_s_at_l_star": fmt(alpha_s_at_lstar_2l, dps=OUT_DPS),
                "minimal_sm_triangle_invariant_at_PDG_MZ": fmt(sm_triangle_pdg_mz, dps=OUT_DPS),
                "thresholds": rg_threshold_results,
            },
        )
        wb.add_data("part_b_ir_qcd_lambda_bridge", qcd_ir_candidates)

        wb.add_assertion(
            "catalan_24term_rational_bracket_holds",
            "1" if g_cat_24_err <= (one / mp.mpf(24)) else "0",
            "1",
            "0",
            source="HiggsCategoricalMassFormula.catalanG_certified_rational_bracket",
        )
        wb.add_assertion(
            "ewVev_sweedler_loop_shift_identity_exact",
            fmt(loop_shift_identity_err, dps=15),
            "0",
            "1e-75",
            source="ElectroweakSweedlerScaleAndRGThresholds.ewVev_sweedler_loop_shift_eq",
        )
        wb.add_assertion(
            "sweedler_fourHop_escapes_su2_wall_and_exceeds_ewTree",
            "1"
            if (
                kappa_s1_bare < (one / mp.mpf(256))
                and nv_bs < nv_s1_bare
                and alpha_q_0 > mp.mpf(0)
            )
            else "0",
            "1",
            "0",
            source="ElectroweakSweedlerScaleAndRGThresholds.ewDressedTreeComplexity_lt_sweedlerFourHopInv_of_rational_bracket",
        )
        wb.add_assertion(
            "two_loop_taylor_ode_step_doubling_convergence",
            fmt(max_ode_conv_err, dps=15),
            "0",
            "1e-55",
            source="80-dps order-48 Taylor RG integrator n_steps=150 vs n_steps=300",
        )
        wb.add_assertion(
            "sm_1loop_triangle_invariant_vanishes_on_unified_trajectories",
            rg_threshold_results["T3_sweedler_k21"]["PDG_MSbar_alphaEM"][
                "triangle_invariant_1loop_residual"
            ],
            "0",
            "1e-70",
            source="ElectroweakSweedlerScaleAndRGThresholds.sm_oneLoop_unification_iff_triangle_zero",
        )

        wb.add_caveat(
            "Honest hits & misses: (1) Sweedler 4-hop rate G_F*m_p^2 = (q0^2 - 1)^8 misses PDG G_F "
            "by -18.12% (+10.51% on v_EW = 272.10 GeV) at tree level, while the amplitude-squared "
            "reading G_F*m_p^2 = (q0^2 - 1)^4 gives v_EW = 14.65 GeV (-94.05% miss at m_model = m_p); "
            "however, inserting parameter-free kappa_S = 2^(1/4)*(q0^2 - 1)^4 into the 1-loop Habiro "
            "slot of EwVevGaps escapes su2_coupling_not_selfConsistent (< 1/30) and lands at +81.13 ppb "
            "(+0.32 sigma) vs PDG v_EW (still conditional on T_EW's 3 open slots). (2) Low Sweedler "
            "threshold mu_UV/M_Z = (q0^2 - 1)^(-4) (L = 5.843) only runs sin^2 theta_W from 0.375 to "
            "0.3420 (2-loop, +47.9% above 0.23122), whereas matching sin^2 theta_W(M_Z) = 0.23122 "
            "requires L* = 25.45 (1-loop, k_eff = 17.42) / ~25.33 (2-loop, straddled by k = 17 and "
            "k = 18), where single-step minimal-SM unification undershoots alpha_s(M_Z) (~0.071-0.074 "
            "vs 0.1180) because smTriangleInv = -1217.03 != 0; thresholds L >= 35 (k = 24, 12*pi) hit "
            "the 2-loop QCD Landau pole above M_Z. (3) Conversely, the zero-parameter IR QCD "
            "dimensional-transmutation scale Lambda = m_p*(q0^2 - 1) = 217.73 MeV gives 2-loop "
            "alpha_s(M_Z) = 0.11849 (+0.41%, +0.54 sigma vs PDG 0.1180 +/- 0.0009; 0.11825 / +0.27 sigma "
            "using QOU's own torus M_Z)."
        )

        out = wb.save({"q0Anchor": "proton", "q0Value": fmt(q0, dps=OUT_DPS)})
        print(f"\nwitness -> {out}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
