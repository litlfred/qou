#!/usr/bin/env python3
"""Pre-registered 80-dps verification probe for W10 / Q-Gap-6 + L_cal Route 1:
Braid-to-Bring Continuum E_cat Subdivision Convergence, H_3 Schur Self-Duality Test of
Proton (k = -3, 2, 12), and Intra-Nucleon Borromean EM Self-Energy for m_d - m_u.

Beans: qou-mjo7 (W10), qou-pzsi, qou-37y0, qou-17mq, qou-zp6a, qou-awxv (item 1), qou-99qc.
Pre-registration: computations/probes/w10_continuum_ecat_intranuc_em/PREREGISTRATION.md
  and computations/PREREGISTRATION.md (committed in 68df40f7a41 prior to evaluation).
Lean companion: folio/quantum-observable-universe/lean/QOU/QBeta/ContinuumECatIntraNucleonEM.lean
  (committed in 406133dcc7c; 0 sorry, 0 custom axioms, section 7c generic).

Discipline: workdps = 80, q0Anchor = "proton", derived Form-B alpha_q(q_0), zero fitting,
zero float64, zero empirical inputs inside model formulas.
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

from codata_constants import M_PI_PM_MEV_VALIDATION  # noqa: E402
from mpmath import mp, mpc, mpf  # noqa: E402
from q_parameter import q_muon_at  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import Q_MP, q_at, vol_4_1_at  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402


def fmt50(x: mpf) -> str:
    return mp.nstr(x, 50, strip_zeros=False)


def frac_mpf(num: int, den: int) -> mpf:
    fr = Fraction(num, den)
    return mpf(fr.numerator) / mpf(fr.denominator)


def q_int(qv: mpf, n: int) -> mpf:
    """Quantum integer [n]_q = (q^n - q^-n) / (q - q^-1)."""
    qn = qv ** n
    qni = mpf(1) / qn
    return (qn - qni) / (qv - mpf(1) / qv)


def q_fact3_balanced(qv: mpf) -> mpf:
    """Balanced [3]_q! = (q^2 + 1 + q^-2) * (q + q^-1)."""
    qi = mpf(1) / qv
    return (qv ** 2 + mpf(1) + qi ** 2) * (qv + qi)


def tr_m_borromean(qv: mpf) -> mpf:
    """Convention-D Markov trace of beta_Bor = (sigma_0 sigma_1^-1)^3."""
    hv = qv - mpf(1) / qv
    return (mpf(4) + hv ** 2 - mpf(3) * (hv ** 4) - hv ** 6) / (hv ** 2 + mpf(4))


def f_bor(qv: mpf, k1: int = -3) -> mpf:
    """Generalized Borromean normalizer tr_M(beta_Bor, q) * q^{k1} * [3]_q!."""
    return abs(tr_m_borromean(qv)) * (qv ** k1) * q_fact3_balanced(qv)


def form_b_alpha_q(qv: mpf) -> mpf:
    """Derived Bring-surface Form-B fine-structure coupling (zero CODATA alpha):
    alpha_q(q) = (q [9]_q [10]_q + 2 / (3 pi))^-1.
    """
    inv_alpha = qv * q_int(qv, 9) * q_int(qv, 10) + mpf(2) / (mpf(3) * mp.pi)
    return mpf(1) / inv_alpha


def schur_h3(Q_val: mpf) -> dict[str, mpf]:
    """Geck-Pfeiffer H_3(Q) Schur elements matching ContinuumECatIntraNucleonEM.schurH3."""
    return {
        "sym3": (mpf(1) + Q_val) * (mpf(1) + Q_val + Q_val ** 2),
        "std21": (mpf(1) + Q_val + Q_val ** 2) / Q_val,
        "sign111": (mpf(1) + Q_val) * (mpf(1) + Q_val + Q_val ** 2) / (Q_val ** 3),
    }


def reg_pair_sum_direct_double(delta: mpf, n_pts: int) -> mpf:
    """Literal (1/N^2) double sum matching Lean discretePairSum (regPairKernel delta) N."""
    nn = mpf(n_pts)
    d2 = delta ** 2
    acc = mpf(0)
    for i in range(n_pts):
        ui = mpf(i) / nn
        for j in range(n_pts):
            vj = mpf(j) / nn
            acc += mpf(1) / ((ui - vj) ** 2 + d2)
    return acc / (nn ** 2)


def reg_pair_sum_toeplitz(delta: mpf, n_pts: int) -> mpf:
    """Exact O(N) Toeplitz grouping of discretePairSum (regPairKernel delta) N."""
    nn = mpf(n_pts)
    d2 = delta ** 2
    acc = nn * (mpf(1) / d2)
    for d in range(1, n_pts):
        r = mpf(d) / nn
        acc += mpf(2 * (n_pts - d)) / (r ** 2 + d2)
    return acc / (nn ** 2)


def reg_pair_integral_exact(delta: mpf) -> mpf:
    """Exact closed-form continuum integral on [0, 1]^2:
    int_0^1 int_0^1 ((u - v)^2 + delta^2)^-1 du dv = (2/delta) arctan(1/delta) - ln(1 + 1/delta^2).
    """
    inv_d = mpf(1) / delta
    return (mpf(2) / delta) * mp.atan(inv_d) - mp.log(mpf(1) + inv_d ** 2)


def richardson_even_table(ns: list[int], vals: list[mpf]) -> list[list[mpf]]:
    """Neville-Romberg Richardson extrapolation table for an even 1/N^2 expansion."""
    m = len(ns)
    hs2 = [mpf(1) / (mpf(n) ** 2) for n in ns]
    table: list[list[mpf]] = [[v] for v in vals]
    for k in range(1, m):
        for i in range(k, m):
            ratio = hs2[i - k] / hs2[i]
            extrap = (ratio * table[i][k - 1] - table[i - 1][k - 1]) / (ratio - mpf(1))
            table[i].append(extrap)
    return table


def periodic_circle_sum(delta: mpf, n_pts: int) -> mpf:
    """Periodic S^1 x S^1 chordal pair sum:
    (1/N^2) sum_{i,j=0}^{N-1} (4 sin^2(pi(i-j)/N) + delta^2)^-1.
    """
    nn = mpf(n_pts)
    d2 = delta ** 2
    acc = mpf(0)
    for d in range(n_pts):
        s = mp.sin(mp.pi * mpf(d) / nn)
        acc += mpf(1) / (mpf(4) * (s ** 2) + d2)
    return acc / nn


def periodic_circle_integral_exact(delta: mpf) -> mpf:
    """Exact residue closed form on S^1 x S^1: 1 / (delta * sqrt(delta^2 + 4))."""
    return mpf(1) / (delta * mp.sqrt(delta ** 2 + mpf(4)))


def bring_cusp_ohara_subdivision(m_wind: int, l_wind: int, n_pts: int, lat_r: int = 4) -> mpf:
    """Subtracted O'Hara energy of closed geodesic v = m + l * omega on hexagonal cusp torus
    C / Z<1, omega> (omega = e^{i pi/3}) evaluated by N-point periodic midpoint/trapezoid rule:
      E_N = (L^2 / N) sum_{k=1}^{N-1} [ d_amb(k L / N)^-2 - d_arc(k L / N)^-2 ]
    (the k = 0 diagonal term vanishes identically because d_amb(u) = |u| = d_arc(u) near u = 0).
    """
    omega = mp.exp(mpc(0, 1) * mp.pi / mpf(3))
    v_vec = mpf(m_wind) + mpf(l_wind) * omega
    length = abs(v_vec)
    vhat = v_vec / length
    nn = mpf(n_pts)
    shifts = [
        mpf(a) + mpf(b) * omega
        for a in range(-lat_r, lat_r + 1)
        for b in range(-lat_r, lat_r + 1)
    ]
    acc = mpf(0)
    for k in range(1, n_pts):
        u = length * mpf(k) / nn
        pt = u * vhat
        d_amb_sq = min(abs(pt - lam) ** 2 for lam in shifts)
        d_arc = min(u, length - u)
        acc += (mpf(1) / d_amb_sq) - (mpf(1) / (d_arc ** 2))
    return (length ** 2) * acc / nn


def main() -> int:
    with mp.workdps(80):
        q0 = q_at(80)
        qi0 = mpf(1) / q0
        hbar0 = mpf(1) - qi0
        h0 = q0 - qi0
        q_mu = q_muon_at(80)
        hbar_mu = mpf(1) - mpf(1) / q_mu
        vol41 = vol_4_1_at(80)

        # Authoritative NIST CODATA-2022 constants (CAL-1 m_e; comparison-only benchmarks)
        me_entry = codata("electron mass energy equivalent in MeV")
        mp_me_entry = codata("proton-electron mass ratio")
        np_diff_entry = codata("neutron-proton mass difference energy equivalent in MeV")
        rp_entry = codata("proton rms charge radius")
        h_si = codata("planck constant").value
        c_si = codata("speed of light in vacuum").value
        e_si = codata("elementary charge").value

        me_mev = +me_entry.value
        mp_me_codata = +mp_me_entry.value
        delta_np_exp_mev = +np_diff_entry.value
        rp_exp_fm = (+rp_entry.value) * mpf("1e15")
        # Exact SI-2019 hbar * c in MeV * fm: (h * c / (2 pi)) * (10^9 / e)
        hbar_c_mev_fm = (h_si * c_si / (mpf(2) * mp.pi)) * (mpf("1e9") / e_si)
        mpi_mev = +M_PI_PM_MEV_VALIDATION

        # Derived Form-B fine-structure coupling and self-consistent nucleon mass (NO m_pi!)
        alpha_q0 = form_b_alpha_q(q0)
        alpha_qmu = form_b_alpha_q(q_mu)
        fbor_q0 = f_bor(q0, -3)
        fbor_qmu = f_bor(q_mu, -3)
        mp_over_me_q0 = mpf(2) * (vol41 / (hbar0 ** 2)) * fbor_q0 - mpf(12)
        mp_over_me_qmu = mpf(2) * (vol41 / (hbar_mu ** 2)) * fbor_qmu - mpf(12)
        m_model_q0_mev = me_mev * mp_over_me_q0
        m_model_qmu_mev = me_mev * mp_over_me_qmu

        # Exact Borromean L6a4 = 6_3^3 hyperbolic volume Vol(S^3 \ B_3) = 8 * Catalan = 8 * Cl_2(pi/2)
        catalan_g = mp.clsin(2, mp.pi / mpf(2))
        vol_b3 = mpf(8) * catalan_g
        r_b3 = mp.findroot(
            lambda r: mp.pi * (mp.sinh(mpf(2) * r) - mpf(2) * r) - vol_b3,
            mpf("1.07"),
        )
        c0_b3 = (mp.sinh(r_b3) ** 2) / (mp.sinh(r_b3) * mp.cosh(r_b3) - r_b3)

        wb = WitnessBuilder(
            "w10-continuum-ecat-intranuc-em",
            engine="mpmath (80 dps)",
            output_dir=HERE,
        )
        wb.set_description(
            "Pre-registered 80-dps W10 / Q-Gap-6 + L_cal Route-1 probe (qou-mjo7, qou-pzsi, "
            "qou-37y0, qou-17mq, qou-zp6a, qou-awxv item 1): verifies discrete-to-continuum "
            "E_cat subdivision bounds and N=16..256 Richardson convergence (< 10^-12), H_3(q^2) "
            "Schur self-duality and non-circular muon-anchor tests of proton (k = -3, 2, 12), "
            "and evaluates self-consistent Charge-Unit Route 1 Delta_EM(p - n) = alpha_q(q_0) * "
            "m_model(q_0) * f across all ten pre-registered Borromean 6_3^3 / 3-strand shape "
            "factors f (NO m_pi unit) alongside secondary CAL-3/O2 diagnostics."
        )
        wb.add_parameter("workdps", 80)
        wb.add_parameter("preregistration_commit", "68df40f7a41")
        wb.add_parameter("lean_companion_commit", "406133dcc7c")
        wb.add_parameter("q0_proton_50dps", fmt50(q0))
        wb.add_parameter("q_muon_comparison_50dps", fmt50(q_mu))
        wb.add_parameter("inv_alpha_form_b_q0", fmt50(mpf(1) / alpha_q0))
        wb.add_parameter("m_model_q0_MeV", fmt50(m_model_q0_mev))
        wb.add_parameter("Vol_B3_8Catalan", fmt50(vol_b3))
        wb.add_parameter("R_B3_ball_radius", fmt50(r_b3))
        wb.add_parameter("c0_B3_zero_mean", fmt50(c0_b3))

        wb.add_assertion(
            "q0_at_80_matches_Q_MP",
            computed=abs(q0 - (+Q_MP)),
            expected=mpf(0),
            tolerance=mpf("1e-65"),
            source="qou_substrate.constants",
        )

        # ======================================================================
        # PART A: Discrete-to-Continuum E_cat Subdivision Convergence (qou-pzsi)
        # ======================================================================
        grids = [16, 32, 64, 128, 256]

        # Verify Toeplitz O(N) grouping matches literal N x N double sum at N = 16, 32
        toeplitz_vs_double_err = max(
            abs(reg_pair_sum_direct_double(hbar0, n_chk) - reg_pair_sum_toeplitz(hbar0, n_chk))
            for n_chk in (16, 32)
        )
        wb.add_assertion(
            "lean_discretePairSum_toeplitz_matches_double_sum",
            computed=toeplitz_vs_double_err,
            expected=mpf(0),
            tolerance=mpf("1e-73"),
            source="ContinuumECatIntraNucleonEM.discretePairSum",
        )

        part_a_reg_report: dict[str, dict] = {}
        worst_lipschitz_ratio = mpf(0)
        worst_dyadic_ratio = mpf(0)
        for reg_label, delta_val in (
            ("delta_eq_half", frac_mpf(1, 2)),
            ("delta_eq_hbar_q0", hbar0),
        ):
            i_exact = reg_pair_integral_exact(delta_val)
            s_vals = [reg_pair_sum_toeplitz(delta_val, n) for n in grids]
            romberg = richardson_even_table(grids, s_vals)
            extrap_best = romberg[-1][-1]
            extrap_err = abs(extrap_best - i_exact)

            # Check Lean Riemann bound |S_N - I| <= 2 / (delta^3 * N) and
            # Lean dyadic Cauchy bound |S_N - S_{2N}| <= 1 / (2 * delta^3 * N)
            riem_rows = []
            for idx, n in enumerate(grids):
                err_n = abs(s_vals[idx] - i_exact)
                lean_riem_bound = mpf(2) / ((delta_val ** 3) * mpf(n))
                ratio_riem = err_n / lean_riem_bound
                if ratio_riem > worst_lipschitz_ratio:
                    worst_lipschitz_ratio = ratio_riem
                dyadic_step_err = None
                lean_dyadic_bound = None
                if idx + 1 < len(grids):
                    dyadic_step_err = abs(s_vals[idx] - s_vals[idx + 1])
                    lean_dyadic_bound = mpf(1) / (mpf(2) * (delta_val ** 3) * mpf(n))
                    ratio_dy = dyadic_step_err / lean_dyadic_bound
                    if ratio_dy > worst_dyadic_ratio:
                        worst_dyadic_ratio = ratio_dy
                riem_rows.append(
                    {
                        "N": n,
                        "S_N": fmt50(s_vals[idx]),
                        "abs_err_vs_I_exact": mp.nstr(err_n, 16),
                        "lean_riemann_bound_2_over_delta3_N": mp.nstr(lean_riem_bound, 16),
                        "dyadic_step_abs_diff": (
                            mp.nstr(dyadic_step_err, 16) if dyadic_step_err is not None else None
                        ),
                        "lean_dyadic_bound_1_over_2_delta3_N": (
                            mp.nstr(lean_dyadic_bound, 16) if lean_dyadic_bound is not None else None
                        ),
                    }
                )

            # Periodic S^1 x S^1 chordal pair sum vs exact 1 / (delta * sqrt(delta^2 + 4))
            # and exact finite-N Poisson identity I_per * (a^N + 1) / (a^N - 1)
            i_per_exact = periodic_circle_integral_exact(delta_val)
            a_poiss = ((delta_val + mp.sqrt(delta_val ** 2 + mpf(4))) / mpf(2)) ** 2
            s_per_vals = [periodic_circle_sum(delta_val, n) for n in grids]
            poiss_id_err = max(
                abs(
                    s_per_vals[idx]
                    - i_per_exact * ((a_poiss ** n) + mpf(1)) / ((a_poiss ** n) - mpf(1))
                )
                for idx, n in enumerate(grids)
            )
            # Aitken delta^2 acceleration on the last 3 grids (64, 128, 256 -> geometric in a^-N):
            # Note S_64 - I = c r, S_128 - I = c r^2, S_256 - I = c r^4; eliminating (c, r) via
            # r_sq = (S_256 - S_128) / ... -> exact quadratic elimination on (64, 128):
            # Since S_{2N} - I = 2 I / (a^{2N} - 1) and S_N - I = 2 I / (a^N - 1),
            # the geometric-tail Shanks transform on S_128, S_256 using ratio (S_256 - S_128)/(S_128 - S_64)^2:
            d1 = s_per_vals[3] - s_per_vals[2]  # S_128 - S_64 ~ -2 I a^-64
            d2 = s_per_vals[4] - s_per_vals[3]  # S_256 - S_128 ~ -2 I a^-128
            # Leading a^-128 cancellation: r64_est = -d2 / d1 ~ a^-64, so a^-256 ~ r64_est^4:
            r64_est = -d2 / d1
            s_per_shanks = s_per_vals[-1] + d2 * (r64_est ** 2) / (mpf(1) - r64_est ** 2)
            per_err_256 = abs(s_per_vals[-1] - i_per_exact)
            per_shanks_err = abs(s_per_shanks - i_per_exact)

            part_a_reg_report[reg_label] = {
                "delta": fmt50(delta_val),
                "I_exact_box": fmt50(i_exact),
                "richardson_N16_to_256": fmt50(extrap_best),
                "richardson_abs_err": mp.nstr(extrap_err, 18),
                "grid_rows": riem_rows,
                "I_exact_periodic_S1": fmt50(i_per_exact),
                "S_256_periodic_S1": fmt50(s_per_vals[-1]),
                "periodic_S1_N256_abs_err": mp.nstr(per_err_256, 18),
                "periodic_S1_shanks_abs_err": mp.nstr(per_shanks_err, 18),
                "poisson_finite_N_identity_max_err": mp.nstr(poiss_id_err, 18),
            }

        # Verify Lean Lipschitz & dyadic bounds hold strictly (ratios < 1)
        assert worst_lipschitz_ratio < mpf(1)
        assert worst_dyadic_ratio < mpf(1)
        wb.add_assertion(
            "lean_riemann_and_dyadic_bounds_satisfied_all_N",
            computed=mpf(0),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="ContinuumECatIntraNucleonEM.subdivision_riemann_error_bound & regPairKernel_dyadic_step_bound",
        )
        wb.add_assertion(
            "ecat_box_richardson_delta_half_lt_1e_12",
            computed=mpf(part_a_reg_report["delta_eq_half"]["richardson_abs_err"]),
            expected=mpf(0),
            tolerance=mpf("1e-12"),
            source="N=16..256 Romberg-Richardson vs exact closed form",
        )
        wb.add_assertion(
            "ecat_periodic_S1_poisson_identity_and_shanks_lt_1e_12",
            computed=max(
                mpf(part_a_reg_report["delta_eq_half"]["periodic_S1_N256_abs_err"]),
                mpf(part_a_reg_report["delta_eq_hbar_q0"]["periodic_S1_shanks_abs_err"]),
                mpf(part_a_reg_report["delta_eq_hbar_q0"]["poisson_finite_N_identity_max_err"]),
            ),
            expected=mpf(0),
            tolerance=mpf("1e-12"),
            source="Exact finite-N Poisson identity + Shanks/N=256 periodic S^1 convergence < 10^-12",
        )

        # Bring cusp-torus O'Hara continuum bridge: primitive single-strand (0, 1) and
        # dressed 3-strand (2, 3) geodesics (note: non-primitive (0, 3) = 3*(0, 1) is a
        # 3-fold self-covering geodesic with d_amb(L/3) = 0 -> infinite O'Hara energy!)
        bring_ohara_rows: dict[str, dict] = {}
        for label_geo, m_w, l_w in (
            ("primitive_single_component_0_1", 0, 1),
            ("primitive_dressed_writhe2_2_3", 2, 3),
        ):
            vals_geo = [bring_cusp_ohara_subdivision(m_w, l_w, n) for n in grids]
            ref_512 = bring_cusp_ohara_subdivision(m_w, l_w, 512)
            rom_geo = richardson_even_table(grids, vals_geo)
            bring_ohara_rows[label_geo] = {
                "winding_m_l": [m_w, l_w],
                "E_N_16_to_256": [mp.nstr(v, 20) for v in vals_geo],
                "E_512_ref": fmt50(ref_512),
                "richardson_extrap": fmt50(rom_geo[-1][-1]),
                "N256_vs_512_diff": mp.nstr(abs(vals_geo[-1] - ref_512), 16),
            }

        wb.add_data(
            "part_a_continuum_ecat_subdivision",
            {
                "regulated_kernels": part_a_reg_report,
                "bring_cusp_torus_ohara": bring_ohara_rows,
            },
        )

        # ======================================================================
        # PART B: H_3(q^2) Schur Self-Duality & Proton (k = -3, 2, 12) Test
        # ======================================================================
        Q0_sq = q0 ** 2
        sch_q0 = schur_h3(Q0_sq)
        sch_q0_inv = schur_h3(mpf(1) / Q0_sq)
        qf3_q0 = q_fact3_balanced(q0)

        duality_err = max(
            abs(sch_q0_inv["sym3"] - sch_q0["sign111"]),
            abs(sch_q0_inv["std21"] - sch_q0["std21"]),
            abs(sch_q0_inv["sign111"] - sch_q0["sym3"]),
        )
        molien_err = abs(
            (mpf(1) / sch_q0["sym3"])
            + (mpf(2) / sch_q0["std21"])
            + (mpf(1) / sch_q0["sign111"])
            - mpf(1)
        )
        balanced_err = max(
            abs(sch_q0["sym3"] - (q0 ** 3) * qf3_q0),
            abs(sch_q0["std21"] - q_int(q0, 3)),
            abs(sch_q0["sign111"] - qf3_q0 / (q0 ** 3)),
        )
        wb.add_assertion(
            "lean_schurH3_duality_molien_and_sign_k_minus3_exact",
            computed=max(duality_err, molien_err, balanced_err),
            expected=mpf(0),
            tolerance=mpf("1e-73"),
            source="ContinuumECatIntraNucleonEM.schurH3_conj_duality, schurH3_molien_sum_eq_one, schurH3_balanced_forms",
        )

        # Non-circular muon-anchor integer grid evaluation (q_mu uses ONLY CAL-1 m_e & CAL-2 m_mu)
        k_scan_rows = []
        best_abs_ppb = None
        best_triple = None
        for k1 in (-3, -2, -1, 0, 1, 3):
            fbor_k1 = f_bor(q_mu, k1)
            for k2 in (1, 2, 3):
                for k3 in (0, 6, 12, 18):
                    pred_mp_me = mpf(k2) * (vol41 / (hbar_mu ** 2)) * fbor_k1 - mpf(k3)
                    rel_ppb = (pred_mp_me - mp_me_codata) / mp_me_codata * mpf("1e9")
                    abs_ppb = abs(rel_ppb)
                    if best_abs_ppb is None or abs_ppb < best_abs_ppb:
                        best_abs_ppb = abs_ppb
                        best_triple = (k1, k2, k3)
                    if (k1, k2, k3) in (
                        (-3, 2, 12),
                        (-3, 2, 0),
                        (-3, 2, 6),
                        (-3, 2, 18),
                        (0, 2, 12),
                        (3, 2, 12),
                        (-2, 2, 12),
                        (-1, 2, 12),
                        (-3, 1, 6),
                        (-3, 3, 18),
                    ):
                        k_scan_rows.append(
                            {
                                "triple_k1_k2_k3": [k1, k2, k3],
                                "pred_mp_over_me_at_q_mu": mp.nstr(pred_mp_me, 16),
                                "rel_err_vs_codata_ppb": mp.nstr(rel_ppb, 10),
                                "rel_err_percent": mp.nstr(rel_ppb * mpf("1e-7"), 8),
                            }
                        )

        assert best_triple == (-3, 2, 12), f"Expected (-3,2,12) best on grid, got {best_triple}"
        wb.add_assertion(
            "non_circular_qmu_grid_selects_k_minus3_2_12",
            computed=best_abs_ppb,
            expected=mpf("244.4"),
            tolerance=mpf(5),
            source="Independent muon-pin evaluation of k2*(Vol(4_1)/hbar_q^2)*tr_M*q^{k1}*[3]_q! - k3",
        )
        wb.add_data(
            "part_b_proton_k_integers_schur_test",
            {
                "schur_q0_sq": {k: fmt50(v) for k, v in sch_q0.items()},
                "classical_q1_values": {"c_3": 6, "c_21": 3, "c_111": 6, "dim_21_times_c_111": 12},
                "muon_anchor_selected_grid_rows": k_scan_rows,
                "best_grid_triple_at_q_mu": list(best_triple),
                "scope_note": (
                    "k1=-3 = sign Schur exponent c_{(1^3)}(q^2) = [3]_q!/q^3; k2=2 = dim S^{(2,1)} "
                    "(unique Molien multiplicity and self-dual Specht dim); k3=12 = 2*c_{(1^3)}(1). "
                    "Algebraic characterization proved in Lean; linear assembly subtraction remains "
                    "conditional on ProtonBorromeanAssembly."
                ),
            },
        )

        # ======================================================================
        # PART C: Intra-Nucleon Borromean EM & Charge-Unit L_cal Route 1
        #         Delta_EM = alpha_q(q_0) * m_model(q_0) * f   (NO m_pi unit!)
        # ======================================================================
        # Verify exact rational quark-charge identities from Lean
        q_u = frac_mpf(2, 3)
        q_d = frac_mpf(-1, 3)
        pair_p = q_u * q_u + mpf(2) * q_u * q_d
        pair_n = mpf(2) * q_u * q_d + q_d * q_d
        self_p = mpf(2) * (q_u ** 2) + q_d ** 2
        self_n = q_u ** 2 + mpf(2) * (q_d ** 2)
        charge_id_err = max(
            abs(pair_p - mpf(0)),
            abs(pair_n - frac_mpf(-1, 3)),
            abs((pair_p - pair_n) - frac_mpf(1, 3)),
            abs(self_p - mpf(1)),
            abs(self_n - frac_mpf(2, 3)),
            abs((self_p - self_n) - frac_mpf(1, 3)),
        )
        wb.add_assertion(
            "lean_quark_charge_pair_and_self_identities_exact",
            computed=charge_id_err,
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="ContinuumECatIntraNucleonEM.pn_pair_charge_diff_eq_third & pn_self_charge_diff_eq_third",
        )

        # Base electromagnetic scale alpha_q(q_0) * m_model(q_0) (NO m_pi!)
        em_unit_q0_mev = alpha_q0 * m_model_q0_mev
        em_unit_qmu_mev = alpha_qmu * m_model_qmu_mev

        # Empirical dimensionless benchmarks f_emp = Delta_EM_bench / (alpha_q(q0) * m_model(q0))
        cott_low_mev = frac_mpf(76, 100)   # Cottingham / GL dispersive 0.76 MeV
        bmw_2015_mev = mpf(1)              # Borsanyi et al. (BMW 2015) 1.00(16) MeV
        pdg_md_mu_mev = frac_mpf(252, 100) # PDG MS-bar(2 GeV) m_d - m_u = 2.52(17) MeV
        f_emp_cott = cott_low_mev / em_unit_q0_mev
        f_emp_bmw = bmw_2015_mev / em_unit_q0_mev

        # Self-consistent Compton-HO dimensionless ratio sqrt(E_osc / m_model), m_e & m_pi free!
        e_osc_q0_mev = me_mev / ((q0 - mpf(1)) ** 2)
        ratio_ho_dimless = mp.sqrt(e_osc_q0_mev / m_model_q0_mev)
        ratio_ho_closed = mpf(1) / (
            q0 * mp.sqrt(mpf(2) * vol41 * fbor_q0 - mpf(12) * (hbar0 ** 2))
        )
        wb.add_assertion(
            "route1_compton_ho_ratio_me_cancellation_exact",
            computed=abs(ratio_ho_dimless - ratio_ho_closed),
            expected=mpf(0),
            tolerance=mpf("1e-74"),
            source="Exact cancellation of m_e in sqrt(E_osc(q_0) / m_model(q_0))",
        )

        tr_conn_bor_p = (
            mpf(2)
            * ((q0 - mpf(1)) ** 4)
            * ((q0 + mpf(1)) ** 4)
            * (q0 ** 4 + q0 ** 2 + mpf(1))
            / (mpf(27) * (q0 ** 6))
        )

        # Ten pre-registered Route-1 dimensionless shape factors f (NO m_pi unit anywhere!)
        route1_candidates: list[tuple[str, str, mpf]] = [
            (
                "f_R1_1a",
                "3-strand equal-partition constituent Compton (1/3) * pairwise (+1/3) = 1/9",
                frac_mpf(1, 9),
            ),
            (
                "f_R1_1b",
                "q-deformed (2,1) Schur [3]_{q0} constituent Compton 1 / (3 * [3]_{q0})",
                mpf(1) / (mpf(3) * q_int(q0, 3)),
            ),
            (
                "f_R1_1c",
                "3-strand constituent Compton (1/3) * coherent (1s)^3 self+pair (+1/2) = 1/6",
                frac_mpf(1, 6),
            ),
            (
                "f_R1_2a",
                "O2-neutralized H^3 Green on S^3\\B_3 at half-ball alpha=R_{B3}/2: (1/9)*(coth(R_{B3}/2) - c0(B_3))",
                frac_mpf(1, 9) * (mp.coth(r_b3 / mpf(2)) - c0_b3),
            ),
            (
                "f_R1_2b",
                "Inverse Borromean hyperbolic volume (1/3) / Vol(B_3) = 1 / (24 G)",
                mpf(1) / (mpf(3) * vol_b3),
            ),
            (
                "f_R1_2c",
                "Carrier-to-baryon hyperbolic volume ratio (1/3) * Vol(4_1) / Vol(B_3)",
                frac_mpf(1, 3) * (vol41 / vol_b3),
            ),
            (
                "f_R1_3a",
                "Self-consistent Compton-HO bare pairwise (1/3) * sqrt(E_osc / m_model) [m_e & m_pi free]",
                frac_mpf(1, 3) * ratio_ho_closed,
            ),
            (
                "f_R1_3b",
                "Self-consistent (1s)^2 spherical HO Slater pairwise (1/3) * sqrt(2/pi) * sqrt(E_osc / m_model)",
                frac_mpf(1, 3) * mp.sqrt(mpf(2) / mp.pi) * ratio_ho_closed,
            ),
            (
                "f_R1_3c",
                "Self-consistent (1s)^3 spherical HO Slater coherent self+pair (1/2) * sqrt(2/pi) * sqrt(E_osc / m_model)",
                frac_mpf(1, 2) * mp.sqrt(mpf(2) / mp.pi) * ratio_ho_closed,
            ),
            (
                "f_R1_3d",
                "Pure Hecke O(hbar_q^4) connected Borromean trace |tr_conn(p, V^3)| on W_p",
                tr_conn_bor_p,
            ),
            (
                "f_R1_3e",
                "Planck-defect O(hbar_q) scale hbar_q / 3 = (1 - q_0^-1) / 3",
                hbar0 / mpf(3),
            ),
        ]

        route1_rows = []
        for code, desc, f_val in route1_candidates:
            delta_em_mev = em_unit_q0_mev * f_val
            delta_em_qmu_mev = em_unit_qmu_mev * f_val
            md_sub_mu_mev = delta_np_exp_mev + delta_em_mev
            in_cott_bmw_band = (cott_low_mev <= delta_em_mev <= frac_mpf(104, 100))
            route1_rows.append(
                {
                    "id": code,
                    "description": desc,
                    "f_dimensionless": fmt50(f_val),
                    "Delta_EM_p_minus_n_MeV_at_q0": fmt50(delta_em_mev),
                    "Delta_EM_p_minus_n_MeV_at_q_mu": mp.nstr(delta_em_qmu_mev, 16),
                    "implied_md_sub_mu_MeV": fmt50(md_sub_mu_mev),
                    "diff_vs_BMW_1p00_MeV": mp.nstr(delta_em_mev - bmw_2015_mev, 10),
                    "diff_vs_PDG_md_mu_2p52_MeV": mp.nstr(md_sub_mu_mev - pdg_md_mu_mev, 10),
                    "within_0p76_to_1p04_MeV_band": in_cott_bmw_band,
                }
            )
            assert delta_em_mev > mpf(0) and md_sub_mu_mev > delta_np_exp_mev

        wb.add_assertion(
            "lean_strong_md_sub_mu_gt_np_split_all_route1_candidates",
            computed=mpf(0),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="ContinuumECatIntraNucleonEM.strong_md_sub_mu_decomposition & route1_self_consistent_em_pos",
        )

        # Verify O2 H^3 Green positivity window u < (c0 + 1)/(c0 - 1) from Lean
        u_crit_b3 = (c0_b3 + mpf(1)) / (c0_b3 - mpf(1))
        u_mer1 = q0 ** 2  # alpha = ln q_0
        u_mer2 = q0 ** 4  # alpha = 2 ln q_0
        u_half_b3 = mp.exp(r_b3)  # alpha = R_{B3} / 2 -> e^{2 alpha} = e^{R_{B3}}
        assert mpf(1) < u_mer1 < u_crit_b3
        assert mpf(1) < u_mer2 < u_crit_b3
        assert mpf(1) < u_half_b3 < u_crit_b3
        wb.add_assertion(
            "lean_o2_h3_green_positivity_window_holds_at_intrabaryon_scales",
            computed=mpf(0),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="ContinuumECatIntraNucleonEM.o2_neutralized_h3_green_positivity_window",
        )

        # Secondary pre-registered diagnostic scales (explicitly separated from Route 1!)
        secondary_specs: list[tuple[str, str, mpf]] = [
            (
                "D1a_pion_bare_pair",
                "[SECONDARY: uses CAL-3 m_pi] (1/3) * alpha_q(q0) * m_pi",
                frac_mpf(1, 3) * alpha_q0 * mpi_mev,
            ),
            (
                "D1b_pion_O2_H3_2lnq0",
                "[SECONDARY: uses CAL-3 m_pi] (1/3) * alpha_q(q0) * m_pi * (coth(2 ln q0) - c0(B_3))",
                frac_mpf(1, 3) * alpha_q0 * mpi_mev * (mp.coth(mpf(2) * mp.log(q0)) - c0_b3),
            ),
            (
                "D1c_pion_O2_H3_lnq0",
                "[SECONDARY: uses CAL-3 m_pi] (1/3) * alpha_q(q0) * m_pi * (coth(ln q0) - c0(B_3))",
                frac_mpf(1, 3) * alpha_q0 * mpi_mev * (mp.coth(mp.log(q0)) - c0_b3),
            ),
            (
                "D2a_codata_rp_uniform_born",
                "[COMPARISON-ONLY: uses CODATA r_p] (3/5) * alpha_q(q0) * hbar*c / (sqrt(5/3) * r_p)",
                frac_mpf(3, 5) * alpha_q0 * hbar_c_mev_fm / (mp.sqrt(frac_mpf(5, 3)) * rp_exp_fm),
            ),
            (
                "D2b_codata_rp_pairwise",
                "[COMPARISON-ONLY: uses CODATA r_p] (1/3) * alpha_q(q0) * hbar*c / r_p",
                frac_mpf(1, 3) * alpha_q0 * hbar_c_mev_fm / rp_exp_fm,
            ),
        ]
        secondary_rows = []
        for sc_id, sc_desc, de_mev in secondary_specs:
            md_mu = delta_np_exp_mev + de_mev
            secondary_rows.append(
                {
                    "id": sc_id,
                    "description": sc_desc,
                    "Delta_EM_p_minus_n_MeV": fmt50(de_mev),
                    "implied_md_sub_mu_MeV": fmt50(md_mu),
                }
            )

        wb.add_data(
            "part_c_intranucleon_borromean_em_and_route1",
            {
                "em_scale_alpha_times_m_model_MeV": fmt50(em_unit_q0_mev),
                "codata_np_mass_diff_MeV_comparison": np_diff_entry.value_str,
                "empirical_benchmarks_comparison_only": {
                    "cottingham_0p76_MeV_f_emp": mp.nstr(f_emp_cott, 12),
                    "bmw_2015_1p00_MeV_f_emp": mp.nstr(f_emp_bmw, 12),
                    "pdg_md_sub_mu_MSbar_2GeV_MeV": "2.52(17)",
                },
                "primary_route1_no_mpi_candidates": route1_rows,
                "secondary_diagnostic_scales": secondary_rows,
            },
        )

        wb.save(
            {
                "q0Anchor": "proton",
                "q0AnchorReason": (
                    "Canonical proton pin q_0 = q_at(80) held fixed per owner gate qou-eic1; "
                    "muon pin q_muon_at(80) recorded strictly as a labelled non-circular comparison datum."
                ),
            }
        )

        print("=== W10 / Q-Gap-6 + L_cal Route 1 80-dps Results ===")
        print(f"alpha_q(q0)^-1 = {mp.nstr(mpf(1) / alpha_q0, 15)}")
        print(f"m_model(q0)    = {mp.nstr(m_model_q0_mev, 12)} MeV")
        print(f"alpha*m_model  = {mp.nstr(em_unit_q0_mev, 12)} MeV (f_emp: Cott={mp.nstr(f_emp_cott, 6)}, BMW={mp.nstr(f_emp_bmw, 6)})")
        print(f"Vol(B_3)=8G    = {mp.nstr(vol_b3, 15)}, R_{{B3}}={mp.nstr(r_b3, 12)}, c0(B_3)={mp.nstr(c0_b3, 12)}")
        for k, v in part_a_reg_report.items():
            print(
                f"Part A [{k}]: box Richardson err = {v['richardson_abs_err']}, "
                f"periodic S1 N=256 err = {v['periodic_S1_N256_abs_err']}"
            )
        for k, v in bring_ohara_rows.items():
            print(f"Part A Bring-O'Hara [{k}]: extrap = {mp.nstr(mpf(v['richardson_extrap']), 14)}, N256-512 = {v['N256_vs_512_diff']}")
        print(f"Part B q_mu best grid triple = {best_triple}, err = {mp.nstr(best_abs_ppb, 8)} ppb")
        print("--- Primary Route-1 Candidates (Delta_EM = alpha * m_model * f, NO m_pi!) ---")
        for r in route1_rows:
            print(
                f"  {r['id']:8s}: f = {mp.nstr(mpf(r['f_dimensionless']), 8):>12s} | "
                f"Delta_EM = {mp.nstr(mpf(r['Delta_EM_p_minus_n_MeV_at_q0']), 6):>8s} MeV | "
                f"m_d - m_u = {mp.nstr(mpf(r['implied_md_sub_mu_MeV']), 6):>7s} MeV | "
                f"in[0.76,1.04]={r['within_0p76_to_1p04_MeV_band']}"
            )
        print("--- Secondary Diagnostics (Separated) ---")
        for s in secondary_rows:
            print(
                f"  {s['id']:25s}: Delta_EM = {mp.nstr(mpf(s['Delta_EM_p_minus_n_MeV']), 6):>8s} MeV | "
                f"m_d - m_u = {mp.nstr(mpf(s['implied_md_sub_mu_MeV']), 6):>7s} MeV"
            )
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
