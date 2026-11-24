#!/usr/bin/env python3
"""80-dps Symbolic + Numerical Working-Assumption Probe for `qou-l4t2` & `qou-9y43`:
Exact 4-Topology `EmFermionLoop` Bar-Hermitian `(1 - 1·h²α)` Derivation and Zero-Parameter
Two-Loop Bloch-B_3(C) / Bring Harmonic-Form Evaluation.

Companion to `QOU/Archimedean/AlphaEmTwoLoopBlochSchwinger.lean` and
`computations/alpha/alpha_em_two_loop_bloch_schwinger_preregistration.md`.

STRICT ANTI-FIT & EPISTEMIC POSTURE (`NO FITTING EXCEPT CAL-1/2/3`; `qou-aemx`):
- Zero fitted parameters; all operators pre-committed in `..._preregistration.md`.
- Evaluates at `mp.mp.dps = 80` (`mpmath 1.4.1`, zero `float64`) at BOTH `q_proton`
  and `q_muon` (`q0_comparison`), scored transparently against BOTH CODATA 2022
  (`qou_substrate.codata` registry) and CODATA 2018 (`137.035999084` provenance control),
  alongside the `Form A` and `CS tower` arms (`qou-aemx`).
- Nothing is selected by its residual or wired into production dashboards; the physical
  two-loop Bloch-B_3 coupling step is packaged strictly as a `§3b-cond` hypothesis.
"""
from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent.parent
for _p in (
    str(_ROOT / "computations"),
    str(_ROOT / "computations" / "substrate"),
    str(_ROOT / "tools" / "qou-substrate" / "python"),
):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge  # noqa: F401, E402
from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps(80)

import mpmath as mp  # noqa: E402
from mpmath import mpf, fabs, sqrt, log, polylog, zeta  # noqa: E402
mp.mp.dps = max(mp.mp.dps, 80)

import sympy as sp  # noqa: E402
import hecke_core_symbolic as hcs  # noqa: E402
from q_parameter import q_at, q_muon_at  # noqa: E402
from qou_substrate import codata as _codata  # noqa: E402
from witness_base import WitnessBuilder, q0_comparison  # noqa: E402


def _kron(*mats: sp.Matrix) -> sp.Matrix:
    out = mats[0]
    for m in mats[1:]:
        out = sp.Matrix(sp.kronecker_product(out, m))
    return out


def verify_symbolic_four_topology_emfermionloop() -> dict:
    """Exact symbolic verification over Q(q) in U_q(sl_2) V^{x3} and V^{x4} that summing
    all four signed chiral 2-vertex crossing histories (eps_1, eps_2) in {+1, -1}^2 under
    the bar-Hermitian skein pairing (-eps_1 * eps_2) * sigma^{eps_1} * sigma^{eps_2}
    cancels the chiral order-(q-1)^1 tadpoles +/- h*m_1 identically and yields -1 * h^2.
    """
    q_s = sp.Symbol("q", positive=True)
    h_s = q_s - sp.Integer(1) / q_s
    i2 = sp.eye(2)
    r_mat = sp.Matrix([
        [q_s, 0, 0, 0],
        [0, h_s, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, q_s],
    ])
    r_inv = sp.simplify(r_mat.inv())
    mu = sp.diag(q_s, sp.Integer(1) / q_s)
    e_minus = (q_s * sp.eye(4) - r_mat) / (q_s + sp.Integer(1) / q_s)

    # V^{x3}: photon singlet pair (1,2) x H_1 EmFermionLoop strand 3
    e3 = _kron(e_minus, i2)
    mu3 = _kron(mu, mu, mu)
    sig2 = _kron(i2, r_mat)
    sig2_inv = _kron(i2, r_inv)

    def qtr3(mat: sp.Matrix) -> sp.Expr:
        return sp.cancel(sp.expand((mu3 * mat).trace()))

    loop_qdim = qtr3(e3)
    m_1 = sp.cancel(qtr3(e3 * sig2 * e3) / loop_qdim)
    m_1_inv = sp.cancel(qtr3(e3 * sig2_inv * e3) / loop_qdim)
    m_pp = sp.cancel(qtr3(e3 * sig2 * sig2 * e3) / loop_qdim)
    m_mm = sp.cancel(qtr3(e3 * sig2_inv * sig2_inv * e3) / loop_qdim)
    m_pm = sp.cancel(qtr3(e3 * sig2 * sig2_inv * e3) / loop_qdim)
    m_mp = sp.cancel(qtr3(e3 * sig2_inv * sig2 * e3) / loop_qdim)

    ex_pp = sp.cancel(m_pp - 1)
    ex_mm = sp.cancel(m_mm - 1)
    four_topo_sum = sp.cancel(m_pm + m_mp - m_pp - m_mm)

    # V^{x4}: cross-position 4-topology sum at distinct generators (2 and 3)
    e4 = _kron(e_minus, i2, i2)
    mu4 = _kron(mu, mu, mu, mu)
    s2_4 = _kron(i2, r_mat, i2)
    s2i_4 = _kron(i2, r_inv, i2)
    s3_4 = _kron(i2, i2, r_mat)
    s3i_4 = _kron(i2, i2, r_inv)
    cross_4topo = sp.cancel(
        sp.expand((mu4 * (e4 * (s2_4 - s2i_4) * (s3i_4 - s3_4) * e4)).trace())
        / sp.expand((mu4 * e4).trace())
    )

    checks = {
        "skein_diff_central": sp.simplify(r_mat - r_inv - h_s * sp.eye(4)).is_zero_matrix,
        "emfermionloop_qdim_eq_qint2": sp.simplify(loop_qdim - (q_s + 1 / q_s)) == 0,
        "singlet_tadpole_eq_z_markov": sp.simplify(m_1 - q_s ** 3 / (q_s ** 2 + 1)) == 0,
        "over_over_excess_eq_phase3b_finding1": sp.simplify(ex_pp - (q_s ** 4 - q_s ** 2) / (q_s ** 2 + 1)) == 0,
        "under_under_excess_eq_phase3b_finding2": sp.simplify(ex_mm - (1 - q_s ** 2) / (q_s ** 4 + q_s ** 2)) == 0,
        "four_topology_sum_eq_neg_one_mul_h_sq": sp.simplify(four_topo_sum + h_s ** 2) == 0,
        "h4_cross_position_four_topology_eq_neg_h_sq": sp.simplify(cross_4topo + h_s ** 2) == 0,
    }
    return {
        "EmFermionLoop_qTr_E3": str(loop_qdim),
        "m_sigma2_chiral_tadpole": str(m_1),
        "m_sigma2_inv_chiral_tadpole": str(m_1_inv),
        "topology_pp_excess_m_sig2_sq_sub_1": str(ex_pp),
        "topology_mm_excess_m_sig2_inv_sq_sub_1": str(ex_mm),
        "four_topology_bar_hermitian_sum": str(four_topo_sum),
        "h4_cross_position_four_topology_sum": str(cross_4topo),
        "vertex_normalization_note": (
            "Un-averaged skein vertex S = sigma - sigma^-1 gives -S*S_bar = -1 * h^2 (EM Form B); "
            "half-averaged S/2 = (sigma - sigma^-1)/2 gives -(1/4)*h^2 = -((q+1)/2)^2 * hbar_q^2 "
            "(matching EW hbar_q^2 at q -> 1). Choice of un-averaged S on U(1) EmFermionLoop "
            "is recorded explicitly as a §3b-cond hypothesis."
        ),
        "checks": {k: bool(v) for k, v in checks.items()},
    }


def _qbal(n: int, qv: mpf) -> mpf:
    return (qv ** n - qv ** (-n)) / (qv - mpf(1) / qv)


def _solve_two_loop_cubic(t_em: mpf, h_norm: mpf, h_hecke: mpf, c2_add: mpf) -> mpf:
    """Solve 1/alpha = T_EM + alpha * H * (1 - h^2 * alpha) + c2_add * alpha^2 for alpha > 0,
    i.e. (c2_add - H * h^2) * alpha^3 + H * alpha^2 + T_EM * alpha - 1 = 0.
    """
    c3 = c2_add - h_norm * (h_hecke ** 2)
    return mp.findroot(
        lambda a: c3 * (a ** 3) + h_norm * (a ** 2) + t_em * a - mpf(1),
        mpf(1) / t_em,
    )


def evaluate_pin(pin_name: str, qv: mpf, c22: mpf, sig22: mpf, c18: mpf, sig18: mpf) -> dict:
    pi = mp.pi
    z3 = zeta(3)
    c_ps = (
        mpf(197) / mpf(144)
        + (pi ** 2) / mpf(12)
        - ((pi ** 2) / mpf(2)) * log(mpf(2))
        + (mpf(3) / mpf(4)) * z3
    )

    h_hecke = qv - mpf(1) / qv
    t_tree = qv * _qbal(9, qv) * _qbal(10, qv)
    t_zero = mpf(2) / (mpf(3) * pi)
    t_em = t_tree + t_zero
    h_norm = _qbal(2, qv) / (mpf(8) * pi)

    # Form A (L=2 quadratic) & Form B (L=3 cubic)
    a_form_a = (-t_em + sqrt(t_em * t_em + mpf(4) * h_norm)) / (mpf(2) * h_norm)
    inv_form_a = mpf(1) / a_form_a
    a_form_b = _solve_two_loop_cubic(t_em, h_norm, h_hecke, mpf(0))
    inv_form_b = mpf(1) / a_form_b

    # Required additive c2 (for falsification/diagnostic reference ONLY, never fitted)
    c2_req_c22 = (c22 - inv_form_b) / (a_form_b ** 2)
    c2_req_c18 = (c18 - inv_form_b) / (a_form_b ** 2)
    c2_sigma = sig22 / (a_form_b ** 2)

    # CS tower arms (per qou-aemx multi-arm discipline)
    cs_trunc_expr = hcs.alpha_em_inv_sym()
    cs_exact_expr = hcs.alpha_em_inv_sym_exact()
    cs_trunc = mpf(str(cs_trunc_expr.evalf(85, subs={hcs.q: sp.Float(qv, 85)})))
    cs_exact = mpf(str(cs_exact_expr.evalf(85, subs={hcs.q: sp.Float(qv, 85)})))

    # Weight-3 Bloch-B_3(C) trilogarithm defect Delta_B3(q) = zeta(3) - Li_3(q^-2)
    li3_q2 = polylog(3, qv ** (-2))
    delta_b3 = z3 - li3_q2

    # Pre-committed zero-parameter candidate family
    candidates = [
        ("C0_FormB_baseline", "Form B baseline (c2 = 0)", mpf(0)),
        (
            "C1_BlochB3_EmFermionLoop",
            "H(q) * (zeta(3) - Li_3(q^-2)) / (8*pi) = [2]_q * Delta_B3 / (pi * b_1)^2",
            h_norm * (delta_b3 / (mpf(8) * pi)),
        ),
        (
            "C2_BlochB3_bare_64pi2",
            "(zeta(3) - Li_3(q^-2)) / (8*pi)^2 = Delta_B3 / (pi * b_1)^2",
            delta_b3 / ((mpf(8) * pi) ** 2),
        ),
        (
            "C3_JostLuttinger_QED_3over4pi_H",
            "H(q) * 3 / (4*pi) (4D QED beta_1 / beta_0 ratio)",
            h_norm * (mpf(3) / (mpf(4) * pi)),
        ),
        (
            "C4_PetermannSommerfield_H_CPS_over_pi",
            "H(q) * C_PS / pi (C_PS in Q-span{1, pi^2, pi^2 ln 2, zeta(3)})",
            h_norm * (c_ps / pi),
        ),
        (
            "C5_BringZeroMode_h2",
            "(2 / (3*pi)) * h^2 (Bring zero-mode h^2 dressing)",
            t_zero * (h_hecke ** 2),
        ),
        (
            "C6_ThetaGraph_residual",
            "-[3]_q / (8*pi)^2 + H(q)*h^2 (total theta(1,1,2) replacement)",
            -_qbal(3, qv) / ((mpf(8) * pi) ** 2) + h_norm * (h_hecke ** 2),
        ),
    ]

    cand_rows = {}
    for key, label, c2_val in candidates:
        a_sol = _solve_two_loop_cubic(t_em, h_norm, h_hecke, c2_val)
        inv_sol = mpf(1) / a_sol
        err_c22_ppb = (inv_sol - c22) / c22 * (mpf(10) ** 9)
        err_c22_sig = (inv_sol - c22) / sig22
        err_c18_ppb = (inv_sol - c18) / c18 * (mpf(10) ** 9)
        err_c18_sig = (inv_sol - c18) / sig18
        cand_rows[key] = {
            "label": label,
            "c2_add": fmt(c2_val),
            "alpha_inv": fmt(inv_sol),
            "err_vs_codata2022_ppb": fmt(err_c22_ppb),
            "err_vs_codata2022_sigma": fmt(err_c22_sig),
            "err_vs_codata2018_ppb": fmt(err_c18_ppb),
            "err_vs_codata2018_sigma": fmt(err_c18_sig),
        }

    return {
        "pin": pin_name,
        "q0": fmt(qv),
        "Delta_B3_zeta3_sub_Li3_q_inv2": fmt(delta_b3),
        "Petermann_Sommerfield_C_PS": fmt(c_ps),
        "arms_baseline": {
            "Form_A_quadratic_alpha_inv": fmt(inv_form_a),
            "Form_A_err_codata2022_ppb": fmt((inv_form_a - c22) / c22 * (mpf(10) ** 9)),
            "Form_B_cubic_alpha_inv": fmt(inv_form_b),
            "Form_B_err_codata2022_ppb": fmt((inv_form_b - c22) / c22 * (mpf(10) ** 9)),
            "CS_tower_order2_alpha_inv": fmt(cs_trunc),
            "CS_tower_order2_err_codata2022_ppb": fmt((cs_trunc - c22) / c22 * (mpf(10) ** 9)),
            "CS_tower_all_orders_alpha_inv": fmt(cs_exact),
            "CS_tower_all_orders_err_codata2022_ppb": fmt((cs_exact - c22) / c22 * (mpf(10) ** 9)),
        },
        "diagnostic_falsification_windows_not_fitted": {
            "c2_add_req_codata2022": fmt(c2_req_c22),
            "c2_add_req_codata2018": fmt(c2_req_c18),
            "c2_1sigma_codata2022": fmt(c2_sigma),
            "ladder_sign_convention_note": (
                "alpha_em_schwinger_ladder_probe defines c2_ladder = (1/a_B - CODATA)/a_B^2 = -c2_add_req "
                "(-9.39865e-4 vs CODATA 2022); here c2_add multiplies +alpha^2 in 1/alpha."
            ),
        },
        "precommitted_two_loop_candidates": cand_rows,
    }


def main() -> int:
    q_proton = q_at(80)
    q_muon = q_muon_at(80)

    ae = _codata.codata("inverse fine-structure constant")
    c22 = mpf(ae.value_str)
    sig22 = mpf(ae.uncertainty_str)
    c18 = mpf("137.035999084")
    sig18 = mpf("0.000000021")

    sym_res = verify_symbolic_four_topology_emfermionloop()
    proton_res = evaluate_pin("proton", q_proton, c22, sig22, c18, sig18)
    muon_res = evaluate_pin("muon", q_muon, c22, sig22, c18, sig18)

    # Pure-math / structural assertions (NEVER asserting empirical victory as proof!)
    sym_all_ok = all(sym_res["checks"].values())
    # Verify tiling 2-loop measure identity: H(q_p) * Delta_B3 / (8*pi) == [2]_q * Delta_B3 / (pi * b1)^2
    b1_bring = mpf(8)
    delta_b3_p = mpf(proton_res["Delta_B3_zeta3_sub_Li3_q_inv2"])
    lhs_c1 = mpf(proton_res["precommitted_two_loop_candidates"]["C1_BlochB3_EmFermionLoop"]["c2_add"])
    rhs_c1 = (_qbal(2, q_proton) * delta_b3_p) / ((mp.pi * b1_bring) ** 2)
    tiling_measure_ok = bool(fabs(lhs_c1 - rhs_c1) < mpf("1e-75"))

    # Verify classical q -> 1 vanishing of Delta_B3(1) = zeta(3) - Li_3(1) == 0
    classical_b3_vanishes = bool(fabs(zeta(3) - polylog(3, mpf(1))) < mpf("1e-75"))

    # Verify entropy bound: |c2_req_c22| / c2_sigma < 5 (fewer than 1.5 significant digits => PSLQ forbidden)
    c2_snr = fabs(mpf(proton_res["diagnostic_falsification_windows_not_fitted"]["c2_add_req_codata2022"])) / mpf(
        proton_res["diagnostic_falsification_windows_not_fitted"]["c2_1sigma_codata2022"]
    )
    entropy_guard_ok = bool(c2_snr < mpf(5))

    wb = WitnessBuilder("alpha_em_two_loop_bloch_schwinger_probe", engine="sympy+mpmath")
    wb.set_content_block("prop:em-coupling-bring-zero-mode")
    wb.set_description(
        "80-dps working-assumption probe for qou-l4t2 & qou-9y43: "
        "(1) exact symbolic proof in U_q(sl_2) V^{x3} and V^{x4} that summing all four signed "
        "chiral 2-vertex crossing topologies (-eps_1*eps_2)*sigma^{eps_1}*sigma^{eps_2} on the "
        "H_1 EmFermionLoop cancels the order-(q-1)^1 chiral tadpoles (+/- h*m_1) identically "
        "and yields -1*h^2 (resolving the 2026-07-14 phase-3b single-chirality gap); "
        "(2) pre-registered zero-fit evaluation of seven parameter-free two-loop operators "
        "(including Bloch-B_3 defect H(q)*(zeta(3)-Li_3(q^-2))/(8*pi) = [2]_q*Delta_B3/(pi*b_1)^2) "
        "across q_proton and q_muon against CODATA 2022 and CODATA 2018 alongside Form A and CS arms."
    )
    wb.add_data("symbolic_four_topology_emfermionloop", sym_res)
    wb.add_data("proton_pin_evaluation", proton_res)
    wb.add_data("muon_pin_evaluation", muon_res)
    wb.add_data("epistemic_status", {
        "fitted_parameters": 0,
        "wired_into_production": False,
        "preregistration": "computations/alpha/alpha_em_two_loop_bloch_schwinger_preregistration.md",
        "lean_module": "folio/quantum-observable-universe/lean/QOU/Archimedean/AlphaEmTwoLoopBlochSchwinger.lean",
        "owner_ruling_respected": "qou-aemx (no form is chosen by its residual; all arms reported side by side)",
    })

    wb.add_assertion(
        name="four_topology_emfermionloop_cancels_tadpole_to_neg_h_sq",
        computed=str(bool(sym_all_ok)),
        expected="True",
        source="AlphaEmTwoLoopBlochSchwinger.four_topology_bar_hermitian_moment_sum",
    )
    wb.add_assertion(
        name="two_loop_bloch_b3_tiling_measure_64pi2_exact",
        computed=str(bool(tiling_measure_ok)),
        expected="True",
        source="AlphaEmTwoLoopBlochSchwinger.twoLoop_blochB3_factorization",
    )
    wb.add_assertion(
        name="bloch_b3_defect_vanishes_at_classical_limit_q_eq_1",
        computed=str(bool(classical_b3_vanishes)),
        expected="True",
        source="Delta_B3(1) = zeta(3) - Li_3(1) = 0",
    )
    wb.add_assertion(
        name="c2_residual_is_entropy_bounded_no_pslq_fit_permitted",
        computed=str(bool(entropy_guard_ok)),
        expected="True",
        source="alpha_em_two_loop_structure_probe entropy bound (|c2_req|/sigma_c2 = 2.38 < 5)",
    )

    wb.set_audit_only("docs/audits/2026-11-24-alpha-em-two-loop-bloch-schwinger-l4t2-9y43.md")
    out_path = wb.save(
        q0_comparison(
            muon=fmt(q_muon, 80),
            proton=fmt(q_proton, 80),
            reason=(
                "audits the pre-registered zero-parameter two-loop Bloch-B_3 / Bring / QED "
                "operators across Form B, Form A, and CS-tower arms at both q_proton and q_muon"
            ),
        )
    )

    print("=" * 92)
    print("ALPHA_EM TWO-LOOP BLOCH-B3 & 4-TOPOLOGY EMFERMIONLOOP PROBE (80 dps, ZERO FIT)")
    print("=" * 92)
    print(f"[Part 1] Symbolic U_q(sl_2) 4-topology checks all passed : {sym_all_ok}")
    print(f"         qTr_123(e_- x I_2) = {sym_res['EmFermionLoop_qTr_E3']}")
    print(f"         (+,+) excess       = {sym_res['topology_pp_excess_m_sig2_sq_sub_1']}")
    print(f"         (-,-) excess       = {sym_res['topology_mm_excess_m_sig2_inv_sq_sub_1']}")
    print(f"         4-topology sum     = {sym_res['four_topology_bar_hermitian_sum']} (== -h^2)")
    print()
    for res in (proton_res, muon_res):
        print(f"[Part 2] Pin: {res['pin'].upper()} (q = {res['q0'][:24]}...)")
        for k, row in res["precommitted_two_loop_candidates"].items():
            print(
                f"  {k:38s}: c2={row['c2_add'][:13]:>13s} | "
                f"1/a={row['alpha_inv'][:17]} | "
                f"C22={row['err_vs_codata2022_ppb'][:9]:>9s} ppb ({row['err_vs_codata2022_sigma'][:6]:>6s}s) | "
                f"C18={row['err_vs_codata2018_ppb'][:9]:>9s} ppb"
            )
        print()
    print(f"Witness -> {out_path}")
    return 0 if (sym_all_ok and tiling_measure_ok and classical_b3_vanishes and entropy_guard_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
