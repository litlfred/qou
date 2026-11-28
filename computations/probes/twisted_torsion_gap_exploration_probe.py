#!/usr/bin/env python3
"""Pre-registered 80-dps proton-pinned probe for twisted/adjoint Reidemeister torsion determinants.

Explores and cross-checks `QOU/BraidsAndKnots/AdjointTorsionSaddlePrefactors.lean` and
`docs/audits/2026-11-28-twisted-torsion-determinants-gap-exploration.md` across all four
candidate gap domains plus the stepwise `na-Stokes` / Nahm Hessian cross-fertilization:

  1. **Gap A (`4_1`, `5_2`, `(-2,3,7)` pretzel `m016` 1-Loop Saddle Prefactors & `A_0` / `A_omega`):**
     - `4_1`: `(2 tau_{DG,mu})^2 = -3` (`|tau_{DG,mu}| = sqrt(3)/2`, discharging `h_tau` of
       `OneLoopPrefactorInvariance.lean`), `tau_{DG,lam} = -3` (`|tau_{DG,lam}| = 3 = s(1) = A_omega(4_1)`),
       cusp shape `2*sqrt(3)`, and deformed A-polynomial factorization into `[2]_M^2 * Delta_41(M^2) * s(M^2)`.
     - `5_2`: exact 3-saddle `2 tau_{DG,mu}(xi_j) = 3*xi_j^2 - 3*xi_j + 5 = P'(xi_j)/xi_j`,
       3-saddle norm `prod (2 tau_j) = 23 = |disc(K_{5_2})|`, and Euler-Jacobi cancellation
       `sum 1/tau_j = 0`, `sum xi_j/tau_j = 2`.
     - `(-2,3,7)` pretzel (`m016`): exact sister-manifold identity `tau_{DG,lam}(-2,3,7) = 2 * tau_{DG,mu}(5_2)`,
       plastic-constant cusp shape `|1 - xi_0| = rho = 1.3247179572...`, and `3 + 3 = 6` saddle split
       `(1 - Z)^2(1 - Z^2)^2 - Z^2 = (Z^3 - Z^2 + 1)(Z^3 - Z^2 - 2Z + 1)` (`disc = -23` and `+49`).
  2. **Gap B (`alpha_EM` `FormBMinimalKernelClass` & `FormCPinned`):**
     - Pre-registered zero-parameter tests of `4_1` torsion prefactors against `mu_1 = 1/(8*pi)` and
       `deltaReq(q0) - deltaB3(q0)` (clean quantitative refutations: `9.2 ppb` to `7213 ppb` on Form B;
       `5.8x` to `128x` short on Form C).
  3. **Gap C (2026-11-28 Lepton Links `(e, mu, tau)` & Electroweak Torus Links):**
     - Two-variable Alexander / Conway evaluation at `(q0, q0)` and `(q0, q0^-1)` proving ordering
       inversion `|Delta_tau| << |Delta_e| < |Delta_mu|`, while diagonal symmetrized Alexander torsion
       on `{T(2,4), T(2,6), T(2,8)}` reproduces `[2]_{q0}, [3]_{q0}, [4]_{q0}`.
  4. **Cross-Fertilization (`Stepwise Monodromy / Farey Gluing <-> na-Stokes <-> 1-Loop Torsion`):**
     - Verifies that 1D state-integral / Nahm saddle Hessians reproduce `2|tau_{DG,mu}|` on `4_1` and `5_2`,
       and `2|xi_0|^3 |tau_{DG,mu}|` (with framing monomial `xi_0^3`) on `(-2,3,7)`.

Discipline & Owner Ruling (`2026-11-28`):
  - Strictly proton-pinned (`q0Anchor = "proton"`, `q_at(95)`), registered under `physical_proton`.
  - Zero muon-pin columns; `WORK_DPS = 95` (`80`-dps output); zero `float64` (`probe-float64-guard` clean);
    zero inline CODATA literals (`qou_substrate.codata.codata`); zero fitting.
"""

from __future__ import annotations

from pathlib import Path
import sys

_THIS = Path(__file__).resolve()
_ROOT = _THIS.parents[2]
for _p in (
    _ROOT / "tools" / "qou-substrate" / "python",
    _ROOT / "computations",
    _ROOT / "computations" / "substrate",
):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WORK_DPS = 95
OUT_DPS = 80
set_compute_dps(WORK_DPS)
mp.mp.dps = WORK_DPS


def fmt80(val: mp.mpf | mp.mpc) -> str:
    return mp.nstr(val, OUT_DPS, strip_zeros=False)


# ---------------------------------------------------------------------------
# 1. Exact Symbolic & Algebraic DG Torsion / Sister / Euler-Jacobi Checks
# ---------------------------------------------------------------------------
def verify_symbolic_and_saddle_theorems() -> dict[str, object]:
    m_s, z_s, xi_s = sp.symbols("M Z xi")

    # 4_1 deformed A-polynomial factorization
    l_sum = m_s**4 - m_s**2 - 2 - m_s ** (-2) + m_s ** (-4)
    delta_41 = -(m_s**2) + 3 - m_s ** (-2)
    stokes_s = m_s**2 + 1 + m_s ** (-2)
    apoly_41_ok = (
        sp.cancel((4 - l_sum**2) - (m_s - 1 / m_s) ** 2 * (m_s + 1 / m_s) ** 2 * delta_41 * stokes_s)
        == 0
    )

    # 5_2 & (-2,3,7) polynomial identities modulo P(xi) = xi^3 - 2*xi^2 + 3*xi - 1
    p_cub = sp.Poly(xi_s**3 - 2 * xi_s**2 + 3 * xi_s - 1, xi_s, domain=sp.QQ)

    def mod_p(expr: sp.Expr) -> sp.Expr:
        return sp.rem(sp.Poly(sp.expand(expr), xi_s, domain=sp.QQ), p_cub).as_expr()

    two_tau_mu_52 = 3 * xi_s**2 - 3 * xi_s + 5
    two_tau_lam_52 = -26 * xi_s**2 + 38 * xi_s - 50
    cusp_52 = -4 * xi_s**2 + 4 * xi_s - 10

    two_tau_mu_pret = 10 * xi_s**2 - 16 * xi_s + 20
    two_tau_lam_pret = 6 * xi_s**2 - 6 * xi_s + 10

    deriv_52_ok = mod_p(xi_s * two_tau_mu_52 - (3 * xi_s**2 - 4 * xi_s + 3)) == 0
    cusp_52_ok = mod_p(two_tau_mu_52 * cusp_52 - two_tau_lam_52) == 0
    sister_lam_ok = sp.expand(two_tau_lam_pret - 2 * two_tau_mu_52) == 0
    sister_cusp_ok = mod_p((1 - xi_s) * two_tau_mu_pret - two_tau_lam_pret) == 0

    # Pretzel 1D state-integral saddle splitting (`3 + 3 = 6` blocks)
    pret_split_ok = (
        sp.expand((1 - z_s) ** 2 * (1 - z_s**2) ** 2 - z_s**2 - (z_s**3 - z_s**2 + 1) * (z_s**3 - z_s**2 - 2 * z_s + 1))
        == 0
    )
    disc_hyp = int(sp.discriminant(z_s**3 - z_s**2 + 1, z_s))
    disc_ab = int(sp.discriminant(z_s**3 - z_s**2 - 2 * z_s + 1, z_s))

    # Numerical 95-dps evaluation at all 3 roots of P(xi) = 0
    xi_0 = mp.findroot(lambda t: t**3 - 2 * t**2 + 3 * t - 1, mp.mpc("0.78492", "1.30714"))
    xi_1 = mp.conj(xi_0)
    xi_2 = mp.findroot(lambda t: t**3 - 2 * t**2 + 3 * t - 1, mp.mpf("0.43016"))
    roots = [xi_0, xi_1, xi_2]

    tau52_saddles = [(3 * r**2 - 3 * r + 5) / 2 for r in roots]
    prod_tau52 = tau52_saddles[0] * tau52_saddles[1] * tau52_saddles[2]
    sum_inv_tau52 = sum((mp.mpf(1) / t for t in tau52_saddles), mp.mpc(0))
    sum_xi_inv_tau52 = sum((r / t for r, t in zip(roots, tau52_saddles)), mp.mpc(0))

    # Plastic constant rho: rho^3 - rho - 1 = 0
    rho_plastic = mp.findroot(lambda r: r**3 - r - 1, mp.mpf("1.32472"))
    pret_cusp_abs = abs(mp.mpf(1) - xi_0)
    tau_mu_pret_alg = abs(10 * xi_0**2 - 16 * xi_0 + 20) / 2
    tau_lam_pret_alg = abs(6 * xi_0**2 - 6 * xi_0 + 10) / 2
    tau_mu_52_alg = abs(tau52_saddles[0])
    tau_lam_52_alg = abs(-26 * xi_0**2 + 38 * xi_0 - 50) / 2

    # Optional live SnapPy + one_loop_torsion cross-check if SnapPy is installed
    snappy_checked = False
    snappy_max_err = mp.mpf(0)
    try:
        import snappy  # noqa: PLC0415
        from one_loop_torsion import one_loop  # noqa: PLC0415

        m41 = snappy.Manifold("4_1")
        m52 = snappy.Manifold("5_2")
        mm016 = snappy.Manifold("m016")
        mwh = snappy.Manifold("L5a1")
        errs = [
            abs(abs(one_loop(m41, [0])) - mp.sqrt(3) / 2),
            abs(abs(one_loop(m41, [1])) - mp.mpf(3)),
            abs(abs(one_loop(m52, [0])) - tau_mu_52_alg),
            abs(abs(one_loop(m52, [1])) - tau_lam_52_alg),
            abs(abs(one_loop(mm016, [0])) - tau_mu_pret_alg),
            abs(abs(one_loop(mm016, [1])) - tau_lam_pret_alg),
            abs(abs(one_loop(mwh)) - mp.sqrt(2)),
        ]
        snappy_max_err = max(errs)
        snappy_checked = True
    except Exception:
        snappy_checked = False
    finally:
        # `one_loop_torsion` resets compute_dps on import; restore WORK_DPS=95 (`80`-dps output).
        set_compute_dps(WORK_DPS)
        mp.mp.dps = WORK_DPS

    # 1D state-integral / Nahm Hessian checks (`Cross-Fertilization`)
    w6 = mp.exp(mp.mpc(0, 1) * mp.pi / 3)
    hess_1d_41 = abs((1 - 2 * w6) / (1 - w6))
    y0_oht = mp.mpf(1) / xi_1  # Im > 0 root of (y - 1)^3 = y
    hess_1d_52 = abs((2 * y0_oht + 1) / (y0_oht - 1))
    z_pret = mp.findroot(lambda z: z**3 - z**2 + 1, mp.mpc("0.8774", "0.7449"))
    hess_1d_pret = abs(-2 * z_pret / (1 - z_pret) - 4 * z_pret**2 / (1 - z_pret**2) - 2)
    # Framing monomial |z_pret|^-3 = |xi_0|^-1 converts |hess_1d_pret| -> 2 |tau_{DG,mu}(m016)|!
    hess_pret_framed = hess_1d_pret / (abs(z_pret) ** 3)

    ok = (
        apoly_41_ok
        and deriv_52_ok
        and cusp_52_ok
        and sister_lam_ok
        and sister_cusp_ok
        and pret_split_ok
        and disc_hyp == -23
        and disc_ab == 49
        and abs(prod_tau52 - mp.mpf(23) / mp.mpf(8)) < mp.mpf("1e-80")
        and abs(sum_inv_tau52) < mp.mpf("1e-80")
        and abs(sum_xi_inv_tau52 - mp.mpf(2)) < mp.mpf("1e-80")
        and abs(pret_cusp_abs - rho_plastic) < mp.mpf("1e-80")
        and abs(tau_lam_pret_alg - 2 * tau_mu_52_alg) < mp.mpf("1e-80")
        and abs(tau_mu_pret_alg - (2 / rho_plastic) * tau_mu_52_alg) < mp.mpf("1e-80")
        and abs(hess_1d_41 - mp.sqrt(3)) < mp.mpf("1e-80")
        and abs(hess_1d_52 - 2 * tau_mu_52_alg) < mp.mpf("1e-80")
        and abs(hess_pret_framed - 2 * tau_mu_pret_alg) < mp.mpf("1e-80")
        and (not snappy_checked or snappy_max_err < mp.mpf("1e-65"))
    )
    return {
        "passed": ok,
        "snappy_live_crosschecked": snappy_checked,
        "snappy_max_abs_err": fmt80(snappy_max_err),
        "tau_DG_mu_4_1": fmt80(mp.sqrt(3) / 2),
        "tau_DG_lam_4_1": "3",
        "cusp_shape_4_1": fmt80(2 * mp.sqrt(3)),
        "tau_DG_mu_5_2": fmt80(tau_mu_52_alg),
        "tau_DG_lam_5_2": fmt80(tau_lam_52_alg),
        "prod_three_saddles_tau_5_2": fmt80(prod_tau52.real),
        "euler_jacobi_sum_inv_tau_5_2_abs": fmt80(abs(sum_inv_tau52)),
        "euler_jacobi_sum_xi_div_tau_5_2": fmt80(sum_xi_inv_tau52.real),
        "tau_DG_mu_pretzel_m016": fmt80(tau_mu_pret_alg),
        "tau_DG_lam_pretzel_m016": fmt80(tau_lam_pret_alg),
        "pretzel_cusp_shape_plastic_rho": fmt80(rho_plastic),
        "pretzel_saddle_discriminants": {"hyperbolic_sister": disc_hyp, "abelian_dihedral_Z7": disc_ab},
        "hessian_1d_41_matches_2tau": abs(hess_1d_41 - mp.sqrt(3)) < mp.mpf("1e-80"),
        "hessian_1d_52_matches_2tau": abs(hess_1d_52 - 2 * tau_mu_52_alg) < mp.mpf("1e-80"),
        "hessian_1d_pretzel_framed_matches_2tau": abs(hess_pret_framed - 2 * tau_mu_pret_alg) < mp.mpf("1e-80"),
    }


# ---------------------------------------------------------------------------
# 2. Pre-Registered Proton-Pinned Tests on Gap B (`alpha_EM`) & Gap C (`Leptons` / `EW`)
# ---------------------------------------------------------------------------
def evaluate_proton_gap_tests(q0: mp.mpf) -> dict[str, object]:
    alpha_entry = codata("inverse fine-structure constant")
    alpha_inv_exp = mp.mpf(alpha_entry.value_str)
    alpha_inv_sig = mp.mpf(alpha_entry.uncertainty_str)

    h0 = q0 - mp.mpf(1) / q0
    hbar_q0 = mp.mpf(1) - mp.mpf(1) / q0

    def qbal(n: int, q: mp.mpf) -> mp.mpf:
        return (q**n - q ** (-n)) / (q - mp.mpf(1) / q)

    q2 = qbal(2, q0)
    t0_em = q0 * qbal(9, q0) * qbal(10, q0) + mp.mpf(2) / (mp.mpf(3) * mp.pi)
    mu1_std = mp.mpf(1) / (mp.mpf(8) * mp.pi)

    def deformed_porti_ratio(u_val: mp.mpf) -> mp.mpf:
        m_v = mp.exp(u_val / mp.mpf(2))
        x_v = m_v**2
        t_u = mp.sqrt(((m_v + mp.mpf(1) / m_v) ** 2) * (-x_v + mp.mpf(3) - mp.mpf(1) / x_v) * (x_v + mp.mpf(1) + mp.mpf(1) / x_v))
        return t_u / (mp.mpf(2) * mp.sqrt(mp.mpf(3)))

    delta_41_q0 = -q0 + mp.mpf(3) - mp.mpf(1) / q0
    ratio_u_lnq = deformed_porti_ratio(mp.log(q0))
    ratio_u_hbar = deformed_porti_ratio(hbar_q0)

    def solve_form_b_with_mu1(mu_cand: mp.mpf) -> dict[str, str]:
        h_c = q2 * mu_cand
        inv_a = mp.findroot(
            lambda a: a**3 - t0_em * (a**2) - h_c * a + (h0**2) * h_c,
            mp.mpf("137.036"),
        )
        ppb = ((inv_a - alpha_inv_exp) / alpha_inv_exp) * mp.mpf("1e9")
        sig = (inv_a - alpha_inv_exp) / alpha_inv_sig
        return {"mu1": fmt80(mu_cand), "alpha_inv": fmt80(inv_a), "err_ppb": fmt80(ppb), "pull_sigma": fmt80(sig)}

    form_b_tests = {
        "baseline_Bring_1_over_8pi": solve_form_b_with_mu1(mu1_std),
        "cand_1_over_sqrt_8pi_TAd41": solve_form_b_with_mu1(mp.mpf(1) / mp.sqrt(mp.mpf(8) * mp.pi * mp.mpf(2) * mp.sqrt(mp.mpf(3)))),
        "cand_1_over_8pi_tauDG41": solve_form_b_with_mu1(mp.mpf(1) / (mp.mpf(8) * mp.pi * (mp.sqrt(mp.mpf(3)) / mp.mpf(2)))),
        "cand_deformed_torsion_u_eq_ln_q0": solve_form_b_with_mu1(mu1_std * ratio_u_lnq),
        "cand_deformed_torsion_u_eq_hbar_q0": solve_form_b_with_mu1(mu1_std * ratio_u_hbar),
        "cand_alexander_Delta41_q0": solve_form_b_with_mu1(mu1_std * delta_41_q0),
        "cand_inv_alexander_Delta41_q0": solve_form_b_with_mu1(mu1_std / delta_41_q0),
    }

    # Every 4_1 torsion modification of mu1 = 1/(8*pi) worsens |pull_sigma| past 50 sigma
    all_torsion_mu1_refuted = all(
        abs(mp.mpf(v["pull_sigma"])) > mp.mpf("50")
        for k, v in form_b_tests.items()
        if k != "baseline_Bring_1_over_8pi"
    )

    # Form C defect comparison
    a_exp = mp.mpf(1) / alpha_inv_exp
    hab_std = q2 * mu1_std
    delta_b3 = mp.zeta(3) - mp.polylog(3, q0 ** (-2))
    delta_req_exp = (
        ((mp.mpf(8) * mp.pi) ** 2 / q2)
        * (alpha_inv_exp - (t0_em + hab_std * a_exp * (mp.mpf(1) - (h0**2) * a_exp)))
        / (a_exp**2)
    )
    torsion_defects = {
        "one_sub_Delta41_q0": mp.mpf(1) - delta_41_q0,
        "one_sub_deformed_T_ratio_ln_q0": mp.mpf(1) - ratio_u_lnq,
        "log_stokes_s_q0_div_3": mp.log((q0 + mp.mpf(1) + mp.mpf(1) / q0) / mp.mpf(3)),
        "two_h0_sq_div_sqrt3": mp.mpf(2) * (h0**2) / mp.sqrt(mp.mpf(3)),
    }
    all_form_c_torsion_short = all(abs(v - delta_req_exp) / delta_req_exp > mp.mpf("0.8") for v in torsion_defects.values())

    # Gap C: Lepton two-variable Alexander at (q0, q0) and (q0, q0^-1)
    de_par, dmu_par, dtau_par = mp.mpf(1), mp.mpf(1) + q0**2, (q0 - mp.mpf(1)) ** 2
    de_bar, dmu_bar, dtau_bar = mp.mpf(1), mp.mpf(2), -(q0 + mp.mpf(1) / q0 - mp.mpf(2))
    lepton_inverts_tau = (mp.mpf(0) < dtau_par < de_par < dmu_par) and (dtau_bar < mp.mpf(0) and abs(dtau_bar) < de_bar < dmu_bar)

    # Torus-link symmetrized Alexander = [k]_{q0} for k = 1..4
    torus_alex = [
        mp.mpf(1),
        q0 + mp.mpf(1) / q0,
        q0**2 + mp.mpf(1) + q0 ** (-2),
        q0**3 + q0 + mp.mpf(1) / q0 + q0 ** (-3),
    ]
    torus_qint_ok = all(abs(torus_alex[k - 1] - qbal(k, q0)) < mp.mpf("1e-85") for k in (1, 2, 3, 4))

    return {
        "passed": all_torsion_mu1_refuted and all_form_c_torsion_short and lepton_inverts_tau and torus_qint_ok,
        "all_torsion_mu1_modifications_refuted_gt_50sigma": all_torsion_mu1_refuted,
        "all_form_c_torsion_shifts_miss_by_gt_80pct": all_form_c_torsion_short,
        "lepton_alexander_inverts_tau_below_e_and_mu": lepton_inverts_tau,
        "torus_link_sym_alexander_eq_qInt_1_to_4": torus_qint_ok,
        "alpha_em_form_b_torsion_tests": form_b_tests,
        "alpha_em_form_c_defect_comparison": {
            "delta_B3_q0": fmt80(delta_b3),
            "delta_req_codata22": fmt80(delta_req_exp),
            "torsion_candidates": {k: fmt80(v) for k, v in torsion_defects.items()},
        },
        "lepton_two_variable_alexander_proton_q0": {
            "parallel_q0_q0": {"De": fmt80(de_par), "Dmu": fmt80(dmu_par), "Dtau": fmt80(dtau_par)},
            "bar_q0_q0inv": {"De": fmt80(de_bar), "Dmu": fmt80(dmu_bar), "Dtau": fmt80(dtau_bar)},
            "whitehead_tau_nonabelian_tau_DG": fmt80(mp.sqrt(mp.mpf(2))),
        },
    }


def main() -> None:
    q0 = q_at(WORK_DPS)
    alg_res = verify_symbolic_and_saddle_theorems()
    gap_res = evaluate_proton_gap_tests(q0)

    wb = (
        WitnessBuilder(
            "twisted-torsion-gap-exploration-probe",
            engine="mpmath",
            output_dir=_THIS.parent,
        )
        .set_description(
            "Pre-registered 80-dps strictly proton-pinned exploration of twisted/adjoint "
            "Reidemeister torsion determinants across 4_1, 5_2, (-2,3,7) pretzel (m016), "
            "alpha_EM Form B/C, A_0/A_omega, 2026-11-28 lepton links (e, mu, tau), and "
            "stepwise na-Stokes / 1D state-integral Hessians, paired with sorry-free Lean 4 "
            "formalization QOU/BraidsAndKnots/AdjointTorsionSaddlePrefactors.lean."
        )
        .set_audit_only("docs/audits/2026-11-28-twisted-torsion-determinants-gap-exploration.md")
    )

    wb.add_parameter("q0", fmt80(q0))
    wb.add_parameter("compute_dps", WORK_DPS)
    wb.add_parameter("output_dps", OUT_DPS)

    wb.add_assertion(
        "fourOne_52_pretzel_dg_torsion_sister_and_euler_jacobi",
        computed="1" if alg_res["passed"] else "0",
        expected="1",
        tolerance="0.1",
        source="AdjointTorsionSaddlePrefactors (Sections 1-3)",
    )
    wb.add_assertion(
        "fiveTwo_three_saddle_norm_23_div_8",
        computed=alg_res["prod_three_saddles_tau_5_2"],
        expected=fmt80(mp.mpf(23) / mp.mpf(8)),
        tolerance="1e-80",
        source="AdjointTorsionSaddlePrefactors.fiveTwo_three_saddle_norm_and_euler_jacobi",
    )
    wb.add_assertion(
        "fiveTwo_euler_jacobi_squared_saddle_weights_cancel",
        computed=alg_res["euler_jacobi_sum_inv_tau_5_2_abs"],
        expected="0",
        tolerance="1e-80",
        source="AdjointTorsionSaddlePrefactors.fiveTwo_three_saddle_norm_and_euler_jacobi",
    )
    wb.add_assertion(
        "pretzel_sister_lam_eq_two_mul_52_mu",
        computed=alg_res["tau_DG_lam_pretzel_m016"],
        expected=fmt80(mp.mpf(2) * mp.mpf(alg_res["tau_DG_mu_5_2"])),
        tolerance="1e-80",
        source="AdjointTorsionSaddlePrefactors.pretzel_sister_torsion_bridge",
    )
    wb.add_assertion(
        "alpha_em_formB_torsion_replacements_cleanly_refuted",
        computed="1" if gap_res["all_torsion_mu1_modifications_refuted_gt_50sigma"] else "0",
        expected="1",
        tolerance="0.1",
        source="Pre-registered 80-dps proton-pin test vs CODATA 2022 alpha_EM^-1",
    )
    wb.add_assertion(
        "alpha_em_formC_torsion_shifts_miss_weight3_defect",
        computed="1" if gap_res["all_form_c_torsion_shifts_miss_by_gt_80pct"] else "0",
        expected="1",
        tolerance="0.1",
        source="Pre-registered 80-dps proton-pin test vs Form C deltaReq(q0)",
    )
    wb.add_assertion(
        "lepton_alexander_inverts_tau_and_torus_links_give_qInt",
        computed="1" if (gap_res["lepton_alexander_inverts_tau_below_e_and_mu"] and gap_res["torus_link_sym_alexander_eq_qInt_1_to_4"]) else "0",
        expected="1",
        tolerance="0.1",
        source="AdjointTorsionSaddlePrefactors (Section 4)",
    )

    wb.add_data("exact_dg_torsion_and_hessian_bridges", alg_res)
    wb.add_data("proton_pinned_gap_tests_80dps", gap_res)

    out_path = wb.save(
        {
            "q0Anchor": "proton",
            "q0AnchorReason": (
                "Owner ruling 2026-11-28: strictly proton-pinned q0 (q_at(95)); "
                "muon pin on hold until rederivation."
            ),
        }
    )

    built = wb.build()
    print(f"Wrote {out_path.relative_to(_ROOT)} (allPassed={built['allPassed']}, assertions={len(built['assertions'])})")
    if not built["allPassed"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
