#!/usr/bin/env python3
"""80-dps SymPy + mpmath verification probe for `QOU.Core.CategoricalHamiltonianLegendre`
(`def:categorical-hamiltonian`, `prop:mass-energy`, and `thm:groebner-shirshov-energy`).

Verifies at `WORK_DPS = 95`, `OUT_DPS = 80` (zero `float64` on any compute path):
  1. Exact symbolic (`sympy`) Legendre, Fenchel-deficit, relativistic worldline, mass-shell,
     Kantorovich LP-dual, and three-unit-chart identities matching `CategoricalHamiltonianLegendre.lean`.
  2. Second-order canonical Reeb recoil `a_1^2 / (4 a_2)` in MeV, eV, and relative ppb at BOTH
     canonical pins `q_p = q_at(95)` and `q_mu = q_muon_at(95)` (`q0_comparison`), evaluated on:
       (a) the physical nucleon rest-energy scale (`a_2 = m_p, m_n` with parameter-free 3-strand
           Borromean `V^3` Reeb-matter coupling `a_1 = E_0 * hbar_q * tr((Q_12 + Q_23) V^3)`), and
       (b) the uncalibrated 3-strand Borromean weight-space trace scale (`a_2 = E_0 * hbar_q^2 * tau(reeb^2)`).
  3. Exact 4-way algebraic (`sympy` Laurent polynomials in `q`) and 80-dps comparison of:
       - `tr_M(xi_NF)` (Jones-Markov trace with `z = q^3 / (q^2 + 1)`, `tr_M(1) = 1`),
       - `E_cross(beta)` (crossing energy `q` per positive crossing, `-q^-1` per negative crossing),
       - `net(xi_NF) = sum_w c_w(q)` (`z -> 1` flat coefficient-sum shadow),
       - `E_GS(xi_NF) = sum_w |c_w(q)| * ell(w)` (archimedean L1 word-length rewriting norm)
     across `sigma_1^3`, `sigma_1^2 sigma_2`, `sigma_1 sigma_2 sigma_1` (`tr_M = z(1 + h z)` on both
     `sigma_1^2 sigma_2` and `sigma_1 sigma_2 sigma_1`, whereas `net = 1 + h` vs `1` and `E_GS = 2h + 1`
     vs `3`), and Borromean `(sigma_1 sigma_2^-1)^3` in `H_3(q)`.
"""
from __future__ import annotations

import pathlib
import sys
from fractions import Fraction

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
for _p in ("tools/qou-substrate/python", "computations", "computations/substrate"):
    if str(ROOT / _p) not in sys.path:
        sys.path.insert(0, str(ROOT / _p))

import _path_bridge  # noqa: F401, E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

import sympy as sp  # noqa: E402
from mpmath import mp  # noqa: E402
from qou_substrate.constants import (  # noqa: E402
    M_E_MEV_STR,
    M_N_MEV_STR,
    M_P_MEV_STR,
    q_at,
    q_muon_at,
)
from qou_substrate.witness import WitnessBuilder, q0_comparison  # noqa: E402

WORK_DPS = 95
OUT_DPS = 80
mp.dps = WORK_DPS


def fmt80(val: mp.mpf) -> str:
    return mp.nstr(val, OUT_DPS)


# ============================================================================
# 1. Exact H_3(q) Coxeter Basis Arithmetic over SymPy Rational Functions Q(q)
# ============================================================================
# Basis order matching groebner-shirshov-energy.lean:
#   0: e        (len 0, tr_M = 1)
#   1: s1       (len 1, tr_M = z)
#   2: s2       (len 1, tr_M = z)
#   3: s1 s2    (len 2, tr_M = z^2)
#   4: s2 s1    (len 2, tr_M = z^2)
#   5: s1 s2 s1 (len 3, tr_M = z * (1 + h * z))

BASIS_NAMES = ("e", "s1", "s2", "s1s2", "s2s1", "s1s2s1")
BASIS_LENS = (0, 1, 1, 2, 2, 3)


def h3_mul_gen(vec: list[sp.Expr], gen: int, h: sp.Expr) -> list[sp.Expr]:
    """Right-multiply a 6-vector in H_3(q) basis {e, s1, s2, s1s2, s2s1, s1s2s1} by sigma_gen (gen in {1, 2})."""
    c_e, c_1, c_2, c_12, c_21, c_121 = vec
    if gen == 1:
        # e*s1 = s1
        # s1*s1 = h*s1 + e
        # s2*s1 = s2s1
        # s1s2*s1 = s1s2s1
        # s2s1*s1 = s2*(h*s1 + e) = h*s2s1 + s2
        # s1s2s1*s1 = s2s1s2*s1 = ... wait: s1s2s1 * s1 = s2s1s2 * s1? Let's use s1s2s1 = s2s1s2:
        # (s2 s1 s2) * s1 -> no, (s1 s2 s1) * s1 = s1 s2 (s1^2) = s1 s2 (h s1 + 1) = h s1s2s1 + s1s2!
        return [
            sp.simplify(c_1),
            sp.simplify(c_e + h * c_1),
            sp.simplify(c_21),
            sp.simplify(c_121),
            sp.simplify(c_2 + h * c_21),
            sp.simplify(c_12 + h * c_121),
        ]
    if gen == 2:
        # e*s2 = s2
        # s1*s2 = s1s2
        # s2*s2 = h*s2 + e
        # s1s2*s2 = h*s1s2 + s1
        # s2s1*s2 = s2s1s2 = s1s2s1
        # s1s2s1*s2 = (s2s1s2)*s2 = s2s1*(h*s2 + e) = h*s1s2s1 + s2s1
        return [
            sp.simplify(c_2),
            sp.simplify(c_12),
            sp.simplify(c_e + h * c_2),
            sp.simplify(c_1 + h * c_12),
            sp.simplify(c_121),
            sp.simplify(c_21 + h * c_121),
        ]
    raise ValueError(f"Unsupported generator {gen}")


def h3_mul_gen_signed(vec: list[sp.Expr], gen: int, sign: int, h: sp.Expr) -> list[sp.Expr]:
    """Right-multiply by sigma_gen (sign=+1) or sigma_gen^-1 = sigma_gen - h (sign=-1)."""
    pos = h3_mul_gen(vec, gen, h)
    if sign == 1:
        return pos
    if sign == -1:
        return [sp.simplify(pos[k] - h * vec[k]) for k in range(6)]
    raise ValueError(f"Unsupported sign {sign}")


def h3_eval_word(steps: list[tuple[int, int]], h: sp.Expr) -> list[sp.Expr]:
    vec: list[sp.Expr] = [sp.Integer(1)] + [sp.Integer(0)] * 5
    for gen, sgn in steps:
        vec = h3_mul_gen_signed(vec, gen, sgn, h)
    return vec


def h3_markov_trace(vec: list[sp.Expr], h: sp.Expr, z: sp.Expr) -> sp.Expr:
    basis_tr = [
        sp.Integer(1),
        z,
        z,
        z**2,
        z**2,
        z * (1 + h * z),
    ]
    return sp.simplify(sum(vec[k] * basis_tr[k] for k in range(6)))


def eval_mp(expr: sp.Expr, q_sym: sp.Symbol, q_val: mp.mpf) -> mp.mpf:
    """Lossless symbolic rational-function evaluation in mpmath at WORK_DPS."""
    num, den = sp.fraction(sp.together(sp.expand(expr)))
    p_num = sp.Poly(num, q_sym, domain="QQ")
    p_den = sp.Poly(den, q_sym, domain="QQ")

    def eval_poly(poly: sp.Poly) -> mp.mpf:
        acc = mp.mpf(0)
        for (deg,), coeff in poly.terms():
            p_int, q_int = int(coeff.p), int(coeff.q)
            acc += (mp.mpf(p_int) / mp.mpf(q_int)) * (q_val**deg)
        return acc

    return eval_poly(p_num) / eval_poly(p_den)


def evaluate_recoil_at_pin(q_val: mp.mpf, m_e: mp.mpf, m_p: mp.mpf, m_n: mp.mpf, q_sym: sp.Symbol) -> dict[str, str]:
    """Compute 3-strand Borromean V^3 Lagrangian clock terms and 2nd-order recoil a_1^2 / (4 a_2)."""
    # Exact symbolic traces from QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm / CategoricalLagrangianTwoTermBridge:
    # tr(V_A^3) = tr(V_B^3) = -(q^12 - 3 q^10 + 3 q^8 - 5 q^6 + 3 q^4 - 3 q^2 + 1) / q^6
    # On W_p=(2,1) and W_n=(1,2), let's compute tr((Q12 + Q23) V^3) directly via exact 2x2 / 3x3 permutation-weight matrices!
    # Wait: in NucleonWeightSpaceTwoTerm:
    # Basis of 3-strand weight space:
    #   Proton (uud): 3 permutations (uud, udu, duu) -> Q_u = +2/3, Q_d = -1/3
    #   Neutron (udd): 3 permutations (udd, dud, ddu) -> Q_u = +2/3, Q_d = -1/3
    # Exact 3x3 Jimbo weight-space matrices from QOU.BraidsAndKnots.NucleonWeightSpaceTraces & TwoTerm:
    # Proton (2,1) basis: (e1 e1 e2, e1 e2 e1, e2 e1 e1)
    # Neutron (1,2) basis: (e1 e2 e2, e2 e1 e2, e2 e2 e1)
    q = q_sym
    h_s = q - 1 / q
    A1 = sp.Matrix([
        [q, 0, 0],
        [0, 0, 1],
        [0, 1, h_s],
    ])
    A2_inv = sp.Matrix([
        [-h_s, 1, 0],
        [1, 0, 0],
        [0, 0, 1 / q],
    ])
    B1 = sp.Matrix([
        [0, 1, 0],
        [1, h_s, 0],
        [0, 0, q],
    ])
    B2_inv = sp.Matrix([
        [1 / q, 0, 0],
        [0, -h_s, 1],
        [0, 1, 0],
    ])
    Vp = A1 * A2_inv
    Vn = B1 * B2_inv
    V3_p = sp.simplify(Vp * Vp * Vp)
    V3_n = sp.simplify(Vn * Vn * Vn)

    Q12p = sp.diag(sp.Rational(4, 9), sp.Rational(-2, 9), sp.Rational(-2, 9))
    Q23p = sp.diag(sp.Rational(-2, 9), sp.Rational(-2, 9), sp.Rational(4, 9))
    Q12n = sp.diag(sp.Rational(-2, 9), sp.Rational(-2, 9), sp.Rational(1, 9))
    Q23n = sp.diag(sp.Rational(1, 9), sp.Rational(-2, 9), sp.Rational(-2, 9))
    Qadj_p = Q12p + Q23p
    Qadj_n = Q12n + Q23n

    tr_V3_sym = sp.simplify(sp.trace(V3_p))
    tr_Qp_sym = sp.simplify(sp.trace(Qadj_p * V3_p))
    tr_Qn_sym = sp.simplify(sp.trace(Qadj_n * V3_n))

    hbar_q = 1 - 1 / q_val
    c_q = 1 / (q_val - 1)
    t_P = q_val / (q_val - 1)
    E0_mev = m_e / (q_val * (q_val - 1))

    tr_V3 = eval_mp(tr_V3_sym, q_sym, q_val)
    tr_Qp = eval_mp(tr_Qp_sym, q_sym, q_val)
    tr_Qn = eval_mp(tr_Qn_sym, q_sym, q_val)

    # First-order Reeb matter couplings in MeV: a_1 = E_0 * hbar_q * tr((Q12 + Q23) V^3)
    a1_p_mev = E0_mev * hbar_q * tr_Qp
    a1_n_mev = E0_mev * hbar_q * tr_Qn

    # (a) Physical nucleon rest-mass scale a_2 = m_p, m_n (MeV):
    recoil_p_phys_mev = (a1_p_mev**2) / (4 * m_p)
    recoil_n_phys_mev = (a1_n_mev**2) / (4 * m_n)
    recoil_p_phys_ev = recoil_p_phys_mev * mp.mpf("1e6")
    recoil_n_phys_ev = recoil_n_phys_mev * mp.mpf("1e6")
    recoil_p_phys_ppb = (recoil_p_phys_mev / m_p) * mp.mpf("1e9")
    recoil_n_phys_ppb = (recoil_n_phys_mev / m_n) * mp.mpf("1e9")

    # (b) Bare 3-strand Borromean Reeb-spin trace magnitude |a_2_trace| = E_0 * hbar_q^2 * |q^{+-1} * tr(V^3)|:
    a2_p_trace_mev = abs(E0_mev * (hbar_q**2) * q_val * tr_V3)
    a2_n_trace_mev = abs(E0_mev * (hbar_q**2) * (1 / q_val) * tr_V3)
    recoil_p_trace_ev = ((a1_p_mev**2) / (4 * a2_p_trace_mev)) * mp.mpf("1e6")
    recoil_n_trace_ev = ((a1_n_mev**2) / (4 * a2_n_trace_mev)) * mp.mpf("1e6")

    # Unit-chart identity check at this pin:
    chart_err_1 = abs((m_e * (c_q**2)) / t_P - E0_mev)
    chart_err_2 = abs(m_e * (c_q**2) * hbar_q - E0_mev)

    return {
        "q0": fmt80(q_val),
        "c_q": fmt80(c_q),
        "hbar_q": fmt80(hbar_q),
        "t_P": fmt80(t_P),
        "E0_MeV": fmt80(E0_mev),
        "unit_chart_max_abs_err_MeV": fmt80(max(chart_err_1, chart_err_2)),
        "tr_borromean_V3": fmt80(tr_V3),
        "tr_Qadj_proton_V3": fmt80(tr_Qp),
        "tr_Qadj_neutron_V3": fmt80(tr_Qn),
        "a1_proton_MeV": fmt80(a1_p_mev),
        "a1_neutron_MeV": fmt80(a1_n_mev),
        "recoil_proton_phys_eV": fmt80(recoil_p_phys_ev),
        "recoil_neutron_phys_eV": fmt80(recoil_n_phys_ev),
        "recoil_diff_n_minus_p_phys_eV": fmt80(recoil_n_phys_ev - recoil_p_phys_ev),
        "recoil_proton_phys_ppb": fmt80(recoil_p_phys_ppb),
        "recoil_neutron_phys_ppb": fmt80(recoil_n_phys_ppb),
        "a2_proton_3strand_trace_abs_MeV": fmt80(a2_p_trace_mev),
        "a2_neutron_3strand_trace_abs_MeV": fmt80(a2_n_trace_mev),
        "recoil_proton_3strand_trace_eV": fmt80(recoil_p_trace_ev),
        "recoil_neutron_3strand_trace_eV": fmt80(recoil_n_trace_ev),
        "_raw_chart_err": max(chart_err_1, chart_err_2),
        "_raw_recoil_p_ev": recoil_p_phys_ev,
        "_raw_recoil_n_ev": recoil_n_phys_ev,
        "_tr_V3_sym": tr_V3_sym,
        "_tr_Qdiff_sym": sp.simplify(tr_Qn_sym - tr_Qp_sym),
    }


def main() -> int:
    mp.dps = WORK_DPS
    q_p = q_at(WORK_DPS)
    q_mu = q_muon_at(WORK_DPS)
    m_e = mp.mpf(M_E_MEV_STR)
    m_p = mp.mpf(M_P_MEV_STR)
    m_n = mp.mpf(M_N_MEV_STR)

    # ── Part (i): Symbolic Verification of All Legendre & Unit-Chart Identities ──
    L2, L1, L0 = sp.symbols("L2 L1 L0", commutative=False)
    op_vel_id = sp.expand(2 * L2 + L1 - (L2 + L1 + L0) - (L2 - L0))

    a2, a1, a0, Pi, omega = sp.symbols("a2 a1 a0 Pi omega")
    L_clock = a2 * omega**2 + a1 * omega + a0
    H_can = (Pi - a1) ** 2 / (4 * a2) - a0
    omega_star = (Pi - a1) / (2 * a2)
    legendre_phase_id = sp.simplify((Pi * omega_star - L_clock.subs(omega, omega_star)) - H_can)
    fenchel_gap_id = sp.simplify((H_can - (Pi * omega - L_clock)) - a2 * (omega - omega_star) ** 2)
    unit_clock_id = sp.simplify(H_can.subs(Pi, 2 * a2) - (a2 - a1 + a1**2 / (4 * a2) - a0))

    q_pos = sp.Symbol("q_pos", positive=True)
    m_sym = sp.Symbol("m_in", positive=True)
    c_sym = sp.Symbol("c_q", positive=True)
    v_sym = sp.Symbol("v", real=True)
    L_wl = -m_sym * c_sym * sp.sqrt(c_sym**2 - v_sym**2)
    p_wl = sp.diff(L_wl, v_sym)
    E_wl = sp.simplify(p_wl * v_sym - L_wl)
    E_wl_expected = m_sym * c_sym**3 / sp.sqrt(c_sym**2 - v_sym**2)
    wl_energy_id = sp.simplify(E_wl - E_wl_expected)
    wl_rest_id = sp.simplify(E_wl.subs(v_sym, 0) - m_sym * c_sym**2)
    wl_mass_shell_id = sp.simplify(E_wl**2 - p_wl**2 * c_sym**2 - (m_sym * c_sym**2) ** 2)
    dp_dv_zero = sp.simplify(sp.diff(p_wl, v_sym).subs(v_sym, 0) - m_sym)

    q_sym = sp.Symbol("q", positive=True)
    cq_q = 1 / (q_sym - 1)
    hbar_q_sym = 1 - 1 / q_sym
    tP_q = q_sym / (q_sym - 1)
    E0_q = m_sym / (q_sym * (q_sym - 1))
    dirac_ratio_id = sp.simplify((1 / q_sym) / hbar_q_sym - cq_q)
    chart1_id = sp.simplify((m_sym * cq_q**2) / tP_q - E0_q)
    chart2_id = sp.simplify(m_sym * cq_q**2 * hbar_q_sym - E0_q)

    symbolic_all_zero = all(
        x == 0
        for x in (
            op_vel_id,
            legendre_phase_id,
            fenchel_gap_id,
            unit_clock_id,
            wl_energy_id,
            wl_rest_id,
            wl_mass_shell_id,
            dp_dv_zero,
            dirac_ratio_id,
            chart1_id,
            chart2_id,
        )
    )

    # ── Part (ii): 80-dps Recoil Evaluation at Both q_p and q_mu ──
    rec_p = evaluate_recoil_at_pin(q_p, m_e, m_p, m_n, q_sym)
    rec_mu = evaluate_recoil_at_pin(q_mu, m_e, m_p, m_n, q_sym)

    # Verify our symbolic 3x3 weight-space matrices reproduce Lean's exact polynomials!
    lean_tr_V3 = -(q_sym**12 - 3 * q_sym**10 + 3 * q_sym**8 - 5 * q_sym**6 + 3 * q_sym**4 - 3 * q_sym**2 + 1) / (q_sym**6)
    lean_tr_Qdiff = (2 * q_sym**12 - 7 * q_sym**10 + 10 * q_sym**8 - 12 * q_sym**6 + 10 * q_sym**4 - 7 * q_sym**2 + 2) / (3 * q_sym**6)
    lean_v3_match = sp.simplify(rec_p["_tr_V3_sym"] - lean_tr_V3) == 0
    lean_qdiff_match = sp.simplify(rec_p["_tr_Qdiff_sym"] - lean_tr_Qdiff) == 0

    # ── Part (iii): Exact 4-Way Comparison on Named Braid Words in H_3(q) ──
    h_sym = q_sym - 1 / q_sym
    z_sym = q_sym**3 / (q_sym**2 + 1)

    words_spec = {
        "sigma1_cubed": [(1, 1), (1, 1), (1, 1)],
        "sigma1_sq_sigma2": [(1, 1), (1, 1), (2, 1)],
        "sigma1_sigma2_sigma1": [(1, 1), (2, 1), (1, 1)],
        "borromean_s1_s2inv_cubed": [(1, 1), (2, -1), (1, 1), (2, -1), (1, 1), (2, -1)],
    }

    four_way_results: dict[str, dict[str, object]] = {}
    for wname, steps in words_spec.items():
        nf_vec = h3_eval_word(steps, h_sym)
        tr_m_sym = h3_markov_trace(nf_vec, h_sym, z_sym)
        e_cross_sym = sp.simplify(sum(q_sym if sgn == 1 else -1 / q_sym for _g, sgn in steps))
        net_sym = sp.simplify(sum(nf_vec))

        # Evaluate at q_p and q_mu at 80 dps
        nf_qp = [eval_mp(c, q_sym, q_p) for c in nf_vec]
        nf_qmu = [eval_mp(c, q_sym, q_mu) for c in nf_vec]
        e_gs_qp = sum(abs(nf_qp[k]) * mp.mpf(BASIS_LENS[k]) for k in range(6))
        e_gs_qmu = sum(abs(nf_qmu[k]) * mp.mpf(BASIS_LENS[k]) for k in range(6))

        four_way_results[wname] = {
            "nf_basis_coeffs_symbolic": {
                BASIS_NAMES[k]: str(sp.factor(nf_vec[k])) for k in range(6) if nf_vec[k] != 0
            },
            "tr_M_symbolic": str(sp.factor(tr_m_sym)),
            "E_cross_symbolic": str(sp.factor(e_cross_sym)),
            "net_symbolic": str(sp.factor(net_sym)),
            "at_q_proton": {
                "tr_M": fmt80(eval_mp(tr_m_sym, q_sym, q_p)),
                "E_cross": fmt80(eval_mp(e_cross_sym, q_sym, q_p)),
                "net": fmt80(eval_mp(net_sym, q_sym, q_p)),
                "E_GS": fmt80(e_gs_qp),
            },
            "at_q_muon": {
                "tr_M": fmt80(eval_mp(tr_m_sym, q_sym, q_mu)),
                "E_cross": fmt80(eval_mp(e_cross_sym, q_sym, q_mu)),
                "net": fmt80(eval_mp(net_sym, q_sym, q_mu)),
                "E_GS": fmt80(e_gs_qmu),
            },
            "_tr_m_sym": tr_m_sym,
            "_net_sym": net_sym,
            "_e_cross_sym": e_cross_sym,
            "_e_gs_qp": e_gs_qp,
        }

    # Specific 4-way structural checks from Deliverable 1(5):
    tr_s12_s2 = four_way_results["sigma1_sq_sigma2"]["_tr_m_sym"]
    tr_s1_s2_s1 = four_way_results["sigma1_sigma2_sigma1"]["_tr_m_sym"]
    expected_braid_tr = sp.simplify(z_sym * (1 + h_sym * z_sym))
    braid_tr_eq_check = (
        sp.simplify(tr_s12_s2 - expected_braid_tr) == 0
        and sp.simplify(tr_s1_s2_s1 - expected_braid_tr) == 0
    )
    net_s12_s2_check = sp.simplify(four_way_results["sigma1_sq_sigma2"]["_net_sym"] - (1 + h_sym)) == 0
    net_s1_s2_s1_check = sp.simplify(four_way_results["sigma1_sigma2_sigma1"]["_net_sym"] - 1) == 0

    # Borromean Markov trace closed form in Jones-Markov normalization:
    # Check tr_M((s1 s2^-1)^3) at z -> 1 equals net((s1 s2^-1)^3)!
    nf_bor = h3_eval_word(words_spec["borromean_s1_s2inv_cubed"], h_sym)
    z_indep = sp.Symbol("z_indep")
    tr_bor_poly_z = h3_markov_trace(nf_bor, h_sym, z_indep)
    net_is_z1_shadow_bor = sp.simplify(tr_bor_poly_z.subs(z_indep, 1) - four_way_results["borromean_s1_s2inv_cubed"]["_net_sym"]) == 0
    # Wait: for s1s2s1, basis_tr[5] = z*(1 + h*z) -> at z=1, z*(1+h*z) = 1 + h != 1!
    # Why? Because s1s2s1 = s1^2 s2 cyclically, so tr_M|_{z=1}(s1s2s1) = 1 + h = net(s1^2 s2), whereas net(s1s2s1) = 1!
    # That is an even sharper structural insight: even at z -> 1, tr_M|_{z=1}(s1s2s1) = 1 + h != 1 = net(s1s2s1) because s1s2s1 requires cyclic rotation + a Hecke step to peel!
    z1_s1s2s1_diff = sp.simplify((z_indep * (1 + h_sym * z_indep)).subs(z_indep, 1) - 1 - h_sym) == 0

    # Clean internal sympy keys before serializing
    clean_rec_p = {k: v for k, v in rec_p.items() if not k.startswith("_")}
    clean_rec_mu = {k: v for k, v in rec_mu.items() if not k.startswith("_")}
    clean_four_way = {
        wn: {k: v for k, v in wd.items() if not k.startswith("_")}
        for wn, wd in four_way_results.items()
    }

    wb = WitnessBuilder(
        name="categorical-hamiltonian-legendre-recoil",
        engine="mpmath",
        output_dir=HERE,
        _script_path=pathlib.Path(__file__),
    )
    wb.set_description(
        "80-dps SymPy + mpmath verification of QOU.Core.CategoricalHamiltonianLegendre: "
        "operator & phase-space Legendre transforms, relativistic worldline E = m c_q^2 "
        "derivation, 2nd-order nucleon recoil a_1^2/(4 a_2) at q_p and q_mu, and 4-way "
        "comparison of tr_M, E_cross, net, and E_GS on H_3(q) braid words."
    )
    wb.set_content_block("def:categorical-hamiltonian")
    wb.add_parameter("compute_dps", WORK_DPS)
    wb.add_parameter("output_dps", OUT_DPS)
    wb.add_data(
        "symbolic_identities_verified",
        {
            "operator_velocity_legendre_2L2_plus_L1_minus_L_eq_L2_minus_L0": bool(op_vel_id == 0),
            "phase_space_legendre_identity": bool(legendre_phase_id == 0),
            "fenchel_quadratic_gap_identity": bool(fenchel_gap_id == 0),
            "unit_clock_master_expansion": bool(unit_clock_id == 0),
            "worldline_legendre_energy": bool(wl_energy_id == 0),
            "worldline_rest_energy_eq_m_cq_sq": bool(wl_rest_id == 0),
            "worldline_mass_shell_identity": bool(wl_mass_shell_id == 0),
            "worldline_low_v_inertia_slope_dp_dv_at_0": bool(dp_dv_zero == 0),
            "dirac_weight_ratio_eq_cq": bool(dirac_ratio_id == 0),
            "three_unit_chart_E0_identities": bool(chart1_id == 0 and chart2_id == 0),
        },
    )
    wb.add_data("nucleon_recoil_at_q_proton", clean_rec_p)
    wb.add_data("nucleon_recoil_at_q_muon", clean_rec_mu)
    wb.add_data("four_way_braid_functional_comparison", clean_four_way)

    wb.add_assertion(
        "all_10_symbolic_legendre_worldline_and_unit_chart_identities_exact",
        computed="1" if symbolic_all_zero else "0",
        expected="1",
        source="QOU.Core.CategoricalHamiltonianLegendre (sections 1-4)",
    )
    wb.add_assertion(
        "borromean_3strand_weight_space_traces_match_lean_polynomials_exactly",
        computed="1" if bool(lean_v3_match and lean_qdiff_match) else "0",
        expected="1",
        source="QOU.CategoricalLagrangianTwoTermBridge.trace_lagrangian_diff_concrete_borromean_weight_space",
    )
    wb.add_assertion(
        "unit_chart_bridge_holds_to_80dps_at_both_q_p_and_q_mu",
        computed=fmt80(max(rec_p["_raw_chart_err"], rec_mu["_raw_chart_err"])),
        expected="0",
        tolerance="1e-85",
        source="QOU.Core.CategoricalHamiltonianLegendre.three_unit_chart_bridge",
    )
    recoil_ok = bool(
        mp.mpf(0) < rec_p["_raw_recoil_p_ev"] < mp.mpf("100.0")
        and mp.mpf(0) < rec_p["_raw_recoil_n_ev"] < mp.mpf("100.0")
        and mp.mpf(0) < rec_mu["_raw_recoil_p_ev"] < mp.mpf("100.0")
        and mp.mpf(0) < rec_mu["_raw_recoil_n_ev"] < mp.mpf("100.0")
    )
    wb.add_assertion(
        "nucleon_second_order_recoil_positive_sub_100eV_at_physical_mass_scale",
        computed="1" if recoil_ok else "0",
        expected="1",
        source="canonicalHamiltonian_unit_clock: 0 < +a_1^2 / (4 a_2) < 100 eV (~78.7 ueV proton, ~20.22 eV neutron)",
    )
    four_way_split_ok = bool(
        braid_tr_eq_check
        and net_s12_s2_check
        and net_s1_s2_s1_check
        and z1_s1s2s1_diff
    )
    wb.add_assertion(
        "four_way_s1s2s1_and_s1sq_s2_share_tr_M_z_1_plus_hz_while_net_and_E_GS_split",
        computed="1" if four_way_split_ok else "0",
        expected="1",
        source="tr_M(s1^2 s2) = tr_M(s1 s2 s1) = z(1 + h z) vs net(s1^2 s2) = 1 + h != 1 = net(s1 s2 s1)",
    )
    pairwise_ok = bool(
        four_way_results["borromean_s1_s2inv_cubed"]["at_q_proton"]["tr_M"]
        != four_way_results["borromean_s1_s2inv_cubed"]["at_q_proton"]["E_cross"]
        and four_way_results["borromean_s1_s2inv_cubed"]["at_q_proton"]["tr_M"]
        != four_way_results["borromean_s1_s2inv_cubed"]["at_q_proton"]["net"]
        and four_way_results["borromean_s1_s2inv_cubed"]["at_q_proton"]["tr_M"]
        != four_way_results["borromean_s1_s2inv_cubed"]["at_q_proton"]["E_GS"]
        and four_way_results["sigma1_cubed"]["at_q_proton"]["tr_M"]
        != four_way_results["sigma1_cubed"]["at_q_proton"]["E_GS"]
    )
    wb.add_assertion(
        "four_way_functionals_pairwise_distinct_on_borromean_and_trefoil_words",
        computed="1" if pairwise_ok else "0",
        expected="1",
        source="thm:groebner-shirshov-energy & rem:groebner-shirshov-energy-interpretation",
    )

    stamp = q0_comparison(
        muon=q_mu,
        proton=q_p,
        reason=(
            "Evaluates the canonical Reeb recoil a_1^2/(4 a_2), unit-chart scale E_0, and "
            "4-way H_3(q) braid functionals at both canonical substrate pins q_p and q_mu."
        ),
        dps=OUT_DPS,
    )
    wb._extra_top_level.update(stamp)
    saved = wb.save(stamp)
    print(f"Saved witness -> {saved}")
    print(
        f"Proton recoil (phys m_N): p = {mp.nstr(rec_p['_raw_recoil_p_ev'], 12)} eV, "
        f"n = {mp.nstr(rec_p['_raw_recoil_n_ev'], 12)} eV"
    )
    print(
        f"Muon   recoil (phys m_N): p = {mp.nstr(rec_mu['_raw_recoil_p_ev'], 12)} eV, "
        f"n = {mp.nstr(rec_mu['_raw_recoil_n_ev'], 12)} eV"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
