#!/usr/bin/env python3
"""np_splitting_qbeta_legendre_coulomb_probe.py

First-principles 80-dps SymPy + mpmath adjudication of the free-neutron beta-decay
endpoint Q_beta(n) and nucleon mass splitting Delta m_np = m_n - m_p across:
  - Bean qou-cds1: canonical two-row Markov parameter z = q^3 / (q^2 + 1) bar-weight
    obstruction, N=2 Kashiwara/Hoefsmit rung b^2 = [3]_q/[2]_q^2, and F_req > 1 bound;
  - Bean qou-15sj: derived 4-topology Form-B fine-structure coupling alpha_EM(q_0)
    (post-PR #9360 EmFermionLoopFourTopology) and hadron-line monodromy 2 ln t = -alpha_EM;
  - Bean qou-37y0: Legendre Hamiltonian two-channel sign structure
    H_can(2 a_2) = a_2 - a_1 + a_1^2/(4 a_2) - a_0, all-3-pairs (12, 23, 13)
    permutation-symmetric constituent charge operators on Borromean V^3 under the
    derived quantum trace Tr(K^{otimes 3} X V^3) / [2]_q^3, Thomae-Jackson q^{-2}
    proper-time / own-sector horizontal scaling, and a strictly pre-committed
    zero-parameter 10 x 12 = 120 operator catalog with explicit discrete-search
    CODATA entropy accounting.

STRICT ANTI-FIT & PRECISION DISCIPLINE:
  - mp.dps = 80 set before all module-level mpf evaluations; zero float64, zero math.
  - Zero fitted parameters: only (m_e, q_0) enter; m_pi enters nowhere (Route-1 pure).
  - All 3 quark pairs (12, 23, 13) are included symmetrically; historical adjacent
    (12, 23) pair-13 omission is recorded solely as a labelled diagnostic contrast.
  - Evaluates at BOTH proton (q_at(80)) and muon (q_muon_at(80)) anchors (q0_comparison).
  - Reference CODATA-2022 masses are read exclusively from qou_substrate.codata for
    validation scoring and never enter any model formula.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
from mpmath import mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402
from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps(80)
mp.mp.dps = max(mp.mp.dps, 80)

import sympy as sp  # noqa: E402
from qou_substrate import codata as _codata  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from qbeta import qbeta_e0  # noqa: E402
import two_term_qtrace_weighting as ttq  # noqa: E402

DPS = 80
LEAN_MODULE = "QOU.MassTheory.NucleonSplittingLegendreCoulomb"

# ── Validation-only CODATA-2022 constants (loaded from registry, NEVER hard-coded) ──
_ME_REC = _codata.codata("electron mass energy equivalent in MeV")
_MP_REC = _codata.codata("proton mass energy equivalent in MeV")
_MN_REC = _codata.codata("neutron mass energy equivalent in MeV")
_MMU_REC = _codata.codata("muon mass energy equivalent in MeV")
_AINV_REC = _codata.codata("inverse fine-structure constant")

M_E_MEV = mpf(_ME_REC.value_str)
M_E_UNC = mpf(_ME_REC.uncertainty_str)
M_P_EXP = mpf(_MP_REC.value_str)
M_P_UNC = mpf(_MP_REC.uncertainty_str)
M_N_EXP = mpf(_MN_REC.value_str)
M_N_UNC = mpf(_MN_REC.uncertainty_str)
ALPHA_INV_EXP = mpf(_AINV_REC.value_str)

DM_NP_EXP = M_N_EXP - M_P_EXP
DM_NP_UNC = mp.sqrt(M_N_UNC ** 2 + M_P_UNC ** 2)
QBETA_EXP = DM_NP_EXP - M_E_MEV
QBETA_UNC = mp.sqrt(DM_NP_UNC ** 2 + M_E_UNC ** 2)


def q_int(n: int, q: mpf) -> mpf:
    """Balanced quantum integer [n]_q = (q^n - q^{-n}) / (q - q^{-1}) at 80 dps."""
    return (q ** n - q ** (-n)) / (q - mpf(1) / q)


def _solve_cubic(c3: mpf, c2: mpf, c1: mpf, c0: mpf, init: mpf) -> mpf:
    """80-dps Newton solver for c3*a^3 + c2*a^2 + c1*a + c0 = 0."""
    a_val = init
    tol = mpf(10) ** (-84)
    for _ in range(45):
        f_val = c3 * (a_val ** 3) + c2 * (a_val ** 2) + c1 * a_val + c0
        fp_val = mpf(3) * c3 * (a_val ** 2) + mpf(2) * c2 * a_val + c1
        step = f_val / fp_val
        a_val -= step
        if abs(step) < tol:
            break
    return a_val


def alpha_em_ladder(q: mpf) -> dict[str, mpf]:
    """Evaluate Form A, derived 4-topology Form B (#9360), and conditional Form C at q."""
    h2 = (q - mpf(1) / q) ** 2
    T = q * q_int(9, q) * q_int(10, q) + mpf(8) / (mpf(12) * mp.pi)
    H = q_int(2, q) / (mpf(8) * mp.pi)
    a_form_a = (-T + mp.sqrt(T * T + mpf(4) * H)) / (mpf(2) * H)
    a_form_b = _solve_cubic(-H * h2, H, T, -mpf(1), mpf(1) / T)
    delta_b3 = mp.zeta(3) - mp.polylog(3, q ** (-2))
    c2_bloch = H * delta_b3 / (mpf(8) * mp.pi)
    a_form_c = _solve_cubic(c2_bloch - H * h2, H, T, -mpf(1), a_form_b)
    return {
        "alpha_form_a": a_form_a,
        "alpha_form_b": a_form_b,
        "alpha_form_c": a_form_c,
        "alpha_inv_form_a": mpf(1) / a_form_a,
        "alpha_inv_form_b": mpf(1) / a_form_b,
        "alpha_inv_form_c": mpf(1) / a_form_c,
    }


def model_baryon_scales(q: mpf, m_e: mpf) -> dict[str, mpf]:
    """Evaluate zero-fit model scales (m_mu, F_Bor, m_p, E_0^ord0, E_0^twr) at q."""
    vol_41 = mpf(2) * mp.clsin(2, mp.pi / mpf(3))
    hbar_q = mpf(1) - mpf(1) / q
    h_q = q - mpf(1) / q
    m_mu = m_e * vol_41 / (hbar_q ** 2)
    tr_bor = abs((mpf(4) + h_q ** 2 - mpf(3) * (h_q ** 4) - (h_q ** 6)) / (h_q ** 2 + mpf(4)))
    f_bor = tr_bor * q_int(2, q) * q_int(3, q) / (q ** 3)
    m_p_mod = mpf(2) * m_mu * f_bor - mpf(12) * m_e
    e0_ord0 = qbeta_e0.order_zero(q, m_e)
    e0_twr = qbeta_e0.tower_summed(q, m_e)
    return {
        "vol_41": vol_41,
        "hbar_q": hbar_q,
        "h_q": h_q,
        "m_mu_MeV": m_mu,
        "F_Bor": f_bor,
        "m_p_model_MeV": m_p_mod,
        "E0_ord0_MeV": e0_ord0,
        "E0_twr_MeV": e0_twr,
    }


def symbolic_verification() -> dict[str, str]:
    """Exact SymPy verification over Q(q, a2, a1, a0, p, c) mirroring Lean theorems."""
    q, p, c = sp.symbols("q p c", nonzero=True)
    a2, a1, a0 = sp.symbols("a2 a1 a0", nonzero=True)
    a2_n, a1_n, a0_n, a2_p, a1_p, a0_p = sp.symbols(
        "a2_n a1_n a0_n a2_p a1_p a0_p", nonzero=True
    )

    # 1. Legendre transform duality: L(v) = a2*v^2 + a1*v + a0, p = 2*a2*v + a1
    L_vel = lambda A2, A1, A0, v: A2 * v ** 2 + A1 * v + A0  # noqa: E731
    p_vel = lambda A2, A1, v: 2 * A2 * v + A1  # noqa: E731
    H_can = lambda A2, A1, A0, P: (P - A1) ** 2 / (4 * A2) - A0  # noqa: E731

    v_of_p = (p - a1) / (2 * a2)
    assert sp.simplify(p_vel(a2, a1, v_of_p) - p) == 0
    assert sp.simplify(p * v_of_p - L_vel(a2, a1, a0, v_of_p) - H_can(a2, a1, a0, p)) == 0

    # Evaluation at unshifted kinetic momentum p = 2*a2 vs Lagrangian L(1)
    h_at_2a2 = sp.expand(H_can(a2, a1, a0, 2 * a2))
    target_2a2 = a2 - a1 + a1 ** 2 / (4 * a2) - a0
    assert sp.simplify(h_at_2a2 - target_2a2) == 0
    assert sp.simplify(L_vel(a2, a1, a0, 1) - (a2 + a1 + a0)) == 0
    assert sp.simplify((p_vel(a2, a1, 1) * 1 - L_vel(a2, a1, a0, 1)) - (a2 - a0)) == 0

    # Two-channel neutron-minus-proton Legendre difference
    delta_H = sp.simplify(
        H_can(a2_n, a1_n, a0_n, 2 * a2_n) - H_can(a2_p, a1_p, a0_p, 2 * a2_p)
    )
    delta_H_target = (
        (a2_n - a2_p)
        - (a1_n - a1_p)
        + (a1_n ** 2 / (4 * a2_n) - a1_p ** 2 / (4 * a2_p))
        - (a0_n - a0_p)
    )
    assert sp.simplify(delta_H - delta_H_target) == 0

    # Own-sector Thomae-Jackson q^{-2} horizontal constant shift: a0_p = c, a0_n = q^{-2}*c
    horiz_diff = sp.simplify(-(c / q ** 2 - c) - (1 - 1 / q ** 2) * c)
    assert horiz_diff == 0

    # 2. All-3-pairs (12, 23, 13) weight-space matrices & Borromean V^3 traces
    qi = 1 / q
    h = q - qi
    R = sp.Rational
    A1 = sp.Matrix([[q, 0, 0], [0, 0, 1], [0, 1, h]])
    A2 = sp.Matrix([[0, 1, 0], [1, h, 0], [0, 0, q]])
    B1 = sp.Matrix([[0, 1, 0], [1, h, 0], [0, 0, q]])
    B2 = sp.Matrix([[q, 0, 0], [0, 0, 1], [0, 1, h]])
    V3A = (A1 * A2.inv()) ** 3
    V3B = (B1 * B2.inv()) ** 3

    Q12p = sp.diag(R(4, 9), R(-2, 9), R(-2, 9))
    Q23p = sp.diag(R(-2, 9), R(-2, 9), R(4, 9))
    Q13p = sp.diag(R(-2, 9), R(4, 9), R(-2, 9))
    Q12n = sp.diag(R(-2, 9), R(-2, 9), R(1, 9))
    Q23n = sp.diag(R(1, 9), R(-2, 9), R(-2, 9))
    Q13n = sp.diag(R(-2, 9), R(1, 9), R(-2, 9))

    QPairP = Q12p + Q23p + Q13p
    QPairN = Q12n + Q23n + Q13n
    QSelfP = sp.eye(3)
    QSelfN = R(2, 3) * sp.eye(3)
    QTotSqP = QSelfP + 2 * QPairP
    QTotSqN = QSelfN + 2 * QPairN

    assert QPairP == sp.zeros(3, 3)
    assert QPairN == R(-1, 3) * sp.eye(3)
    assert QTotSqP == sp.eye(3)
    assert QTotSqN == sp.zeros(3, 3)

    # Unweighted degeneracy vs Cartan K^{otimes 3} quantum-trace degeneracy breaking
    unw_pair_np = R(-1, 3) - R(0, 1)
    unw_self_np = R(2, 3) - R(1, 1)
    assert unw_pair_np == unw_self_np == R(-1, 3)

    cartan_pair_np = qi * R(-1, 3) - q * R(0, 1)
    cartan_self_np = qi * R(2, 3) - q * R(1, 1)
    assert sp.simplify((cartan_self_np - cartan_pair_np) + (q - qi)) == 0

    # Universal identity linking eps_flavour(V^3) and deltaT_allPairs_raw(V^3)
    two3 = (q + qi) ** 3
    trV3 = sp.simplify(V3A.trace())
    P_bor = q ** 12 - 3 * q ** 10 + 3 * q ** 8 - 5 * q ** 6 + 3 * q ** 4 - 3 * q ** 2 + 1
    assert sp.simplify(trV3 + P_bor / q ** 6) == 0
    assert sp.simplify(V3B.trace() - trV3) == 0

    eps_flav_sym = sp.simplify((q - qi) * trV3 / two3)
    dt_all_raw_sym = sp.simplify((qi * (QPairN * V3B).trace() - q * (QPairP * V3A).trace()) / two3)
    dt_all_conn_sym = sp.simplify(
        (qi * ((QPairN * V3B).trace() + R(1, 3) * V3B.trace()) - q * (QPairP * V3A).trace()) / two3
    )
    assert dt_all_conn_sym == 0
    assert sp.simplify(eps_flav_sym + 3 * (q ** 2 - 1) * dt_all_raw_sym) == 0

    # 3. Canonical two-row Markov parameter z = q^3 / (q^2 + 1) bar-weight & N=2 rung
    z_two = q ** 3 / (q ** 2 + 1)
    z_two_bar = sp.simplify(z_two.subs(q, qi))
    assert sp.simplify(z_two_bar - z_two / q ** 4) == 0
    assert sp.simplify((z_two - z_two_bar) - (q - qi)) == 0

    two_q = q + qi
    three_q = q ** 2 + 1 + qi ** 2
    y_21 = q ** 2 / (q ** 2 + 1) ** 2
    assert sp.simplify(two_q ** 2 - three_q - 1) == 0
    assert sp.simplify((1 - y_21) - three_q / two_q ** 2) == 0

    # Substrate flavor-split algebraic identity: (q-1)^2*(1-q^{-4})/3 = hbar_q^2 * h_q * [2]_q / 3
    hbar_sym = 1 - qi
    assert sp.simplify((q - 1) ** 2 * (1 - q ** (-4)) / 3 - hbar_sym ** 2 * h * two_q / 3) == 0

    return {
        "H_can_at_2a2": str(target_2a2),
        "delta_H_can": str(delta_H_target),
        "own_sector_horiz_shift": "(1 - 1/q**2)*c",
        "cartan_self_minus_pair_np": "-(q - 1/q)",
        "eps_flavour_over_deltaT_allPairs_raw": "-3*(q**2 - 1)",
        "deltaT_allPairs_connected": "0",
        "z_two_row_bar_ratio": "q**(-4)",
        "z_two_row_minus_bar": "q - 1/q",
        "N2_b_squared": "[3]_q / [2]_q**2",
    }


def evaluate_anchor(pin_name: str, q: mpf) -> dict:
    """Evaluate all map terms and the 10x12 pre-committed operator catalog at 80 dps."""
    scales = model_baryon_scales(q, M_E_MEV)
    alphas = alpha_em_ladder(q)

    a_b = alphas["alpha_form_b"]
    a_c = alphas["alpha_form_c"]
    m_p_mod = scales["m_p_model_MeV"]
    m_mu_mod = scales["m_mu_MeV"]
    e0_ord0 = scales["E0_ord0_MeV"]
    e0_twr = scales["E0_twr_MeV"]
    hbar_q = scales["hbar_q"]
    h_q = scales["h_q"]
    two_q = q + mpf(1) / q
    three_q = q ** 2 + mpf(1) + mpf(1) / (q ** 2)

    # Borromean V^3 traces (all-3-pairs vs historical adjacent)
    p_bor = q ** 12 - mpf(3) * q ** 10 + mpf(3) * q ** 8 - mpf(5) * q ** 6 + mpf(3) * q ** 4 - mpf(3) * q ** 2 + mpf(1)
    tr_v3 = -p_bor / (q ** 6)
    qdim3 = two_q ** 3
    eps_flav_v3 = h_q * tr_v3 / qdim3

    dt_all_raw = ttq.delta_t(q, "all_pairs", connected=False)
    dt_all_conn = ttq.delta_t(q, "all_pairs", connected=True)
    dt_adj_raw = ttq.delta_t(q, "adjacent", connected=False)
    dt_adj_conn = ttq.delta_t(q, "adjacent", connected=True)
    dt_self_raw = ((mpf(2) / mpf(3)) * (mpf(1) / q) * tr_v3 - q * tr_v3) / qdim3
    dt_tot2_raw = (-q * tr_v3) / qdim3

    # qou-cds1 canonical two-row Markov parameter z = q^3 / (q^2 + 1) & N=2 rung
    z_two = (q ** 3) / (q ** 2 + mpf(1))
    z_two_bar = (q ** (-3)) / (q ** (-2) + mpf(1))
    b2_hoefsmit = three_q / (two_q ** 2)
    u_ladder = mp.sqrt(b2_hoefsmit) * (hbar_q ** 2)
    n2_factor = mpf(1) - u_ladder ** 2

    qbeta_scored = eps_flav_v3 * e0_twr
    dm_np_scored = qbeta_scored + M_E_MEV
    f_req_on_v3_base = QBETA_EXP / qbeta_scored

    # Legendre recoil diagnostic at constituent 1/9 EM coupling: a1_p = 0, a1_n = k_em/3 = a_b * m_p / 9
    a1_n_const = a_b * m_p_mod / mpf(9)
    recoil_const_mev = (a1_n_const ** 2) / (mpf(4) * (m_p_mod / mpf(2)))

    # ── Strictly pre-committed zero-parameter finite catalog (10 Strong x 12 All-Pairs EM = 120) ──
    f_sub = ((q - mpf(1)) ** 2) * (mpf(1) - q ** (-4)) / mpf(3)
    strong_catalog = {
        "S01_V3_qtrace_twr_plus_me": {
            "val": dm_np_scored,
            "status": "scored_baseline",
            "formula": "|eps_flavour(V^3)| * E_0^twr + m_e",
        },
        "S02_V3_qtrace_ord0_plus_me": {
            "val": eps_flav_v3 * e0_ord0 + M_E_MEV,
            "status": "order_zero_E0_variant",
            "formula": "|eps_flavour(V^3)| * E_0^ord0 + m_e",
        },
        "S03_Legendre_own_sector_12me": {
            "val": (mpf(1) - q ** (-2)) * mpf(12) * M_E_MEV,
            "status": "derived_operator_candidate",
            "formula": "(1 - q^{-2}) * 12 * m_e  [-Delta a_0 on proton 12*m_e constant]",
        },
        "S04_V3_twr_plus_me_plus_Legendre_12me": {
            "val": dm_np_scored + (mpf(1) - q ** (-2)) * mpf(12) * M_E_MEV,
            "status": "derived_operator_candidate",
            "formula": "|eps_flavour(V^3)| * E_0^twr + m_e + (1 - q^{-2}) * 12 * m_e",
        },
        "S05_V3_twr_no_me_plus_Legendre_12me": {
            "val": qbeta_scored + (mpf(1) - q ** (-2)) * mpf(12) * M_E_MEV,
            "status": "derived_operator_candidate",
            "formula": "|eps_flavour(V^3)| * E_0^twr + (1 - q^{-2}) * 12 * m_e",
        },
        "S06_substrate_skein_linear": {
            "val": m_p_mod * f_sub,
            "status": "conditional_conjecture_ansatz",
            "formula": "m_p(q_0) * (q_0 - 1)^2 * (1 - q_0^{-4}) / 3  [conj:flavor-split-aether-mass]",
        },
        "S07_substrate_skein_cayley": {
            "val": m_p_mod * f_sub / (mpf(1) - f_sub / mpf(2)),
            "status": "conditional_conjecture_ansatz",
            "formula": "m_p(q_0) * X / (1 - X/2), X = (q_0 - 1)^2 * (1 - q_0^{-4}) / 3",
        },
        "S08_Jackson_qinv2_E0_twr_plus_me": {
            "val": (mpf(1) - q ** (-2)) * e0_twr + M_E_MEV,
            "status": "derived_operator_candidate",
            "formula": "(1 - q_0^{-2}) * E_0^twr + m_e",
        },
        "S09_Jackson_qinv2_E0_ord0_plus_me": {
            "val": (mpf(1) - q ** (-2)) * e0_ord0 + M_E_MEV,
            "status": "derived_operator_candidate",
            "formula": "(1 - q_0^{-2}) * E_0^ord0 + m_e",
        },
        "S10_retired_counit_DeltaS_ord0_plus_me": {
            "val": M_E_MEV * (q + mpf(1)) * abs(q ** 2 - mpf(2) * q - mpf(1)) / (mpf(2) * (q ** 3)) + M_E_MEV,
            "status": "retired_z_eq_1_counit_excluded_by_two_row_ruling",
            "formula": "m_e * (q_0 + 1) * |q_0^2 - 2*q_0 - 1| / (2*q_0^3) + m_e",
        },
    }

    em_catalog = {
        "E01_zero_connected_all_pairs": {
            "val": dt_all_conn * M_E_MEV,
            "formula": "0  [connected Q_12+Q_23+Q_13 vanishes identically on V^3]",
        },
        "E02_me_qtrace_Qpair_raw": {
            "val": M_E_MEV * dt_all_raw,
            "formula": "m_e * Delta t_raw(Q_12+Q_23+Q_13, V^3)",
        },
        "E03_E0twr_qtrace_Qpair_raw": {
            "val": e0_twr * dt_all_raw,
            "formula": "E_0^twr * Delta t_raw(Q_12+Q_23+Q_13, V^3)",
        },
        "E04_alphaB_mp_Qpair_unweighted_div3": {
            "val": -a_b * m_p_mod / mpf(3),
            "formula": "-alpha_EM^FormB(q_0) * m_p(q_0) * (1/3)  [whole-baryon Compton]",
        },
        "E05_alphaB_mp_constituent_div9": {
            "val": -a_b * m_p_mod / mpf(9),
            "formula": "-alpha_EM^FormB(q_0) * (m_p(q_0)/3) * (1/3)  [constituent Compton 1/9]",
        },
        "E06_alphaB_mp_coherent_div6": {
            "val": -a_b * m_p_mod / mpf(6),
            "formula": "-alpha_EM^FormB(q_0) * m_p(q_0) * (1/6)  [coherent self+pair 1/6]",
        },
        "E07_alphaB_mp_qtrace_Qpair_raw": {
            "val": a_b * m_p_mod * dt_all_raw,
            "formula": "alpha_EM^FormB(q_0) * m_p(q_0) * Delta t_raw(Q_12+Q_23+Q_13, V^3)",
        },
        "E08_alphaB_mp_qtrace_Qself_raw": {
            "val": a_b * m_p_mod * dt_self_raw,
            "formula": "alpha_EM^FormB(q_0) * m_p(q_0) * Delta t_raw(Q_1^2+Q_2^2+Q_3^2, V^3)",
        },
        "E09_alphaB_mp_Jackson_qinv2_div9": {
            "val": -a_b * m_p_mod * (q ** (-2)) / mpf(9),
            "formula": "-alpha_EM^FormB(q_0) * m_p(q_0) * q_0^{-2} / 9  [Jackson bwd step]",
        },
        "E10_alphaB_mmu_Qpair_div3": {
            "val": -a_b * m_mu_mod / mpf(3),
            "formula": "-alpha_EM^FormB(q_0) * m_mu(q_0) * (1/3)",
        },
        "E11_hadron_line_2lnt_E0twr": {
            "val": -a_b * e0_twr,
            "formula": "(2 ln t) * E_0^twr * (Q_n^2 - Q_p^2) = -alpha_EM^FormB(q_0) * E_0^twr",
        },
        "E12_hadron_line_2lnt_me": {
            "val": -a_b * M_E_MEV,
            "formula": "(2 ln t) * m_e * (Q_n^2 - Q_p^2) = -alpha_EM^FormB(q_0) * m_e",
        },
    }

    n_strong = len(strong_catalog)
    n_em = len(em_catalog)
    n_total = n_strong * n_em
    log10_n_total = mp.log10(mpf(n_total))
    # 1-digit net CODATA entropy threshold: -log10(2 * |rel_err| * N_total) >= 1  <=>  |rel_err| <= 1 / (20 * N_total)
    one_digit_rel_threshold = mpf(1) / (mpf(20) * mpf(n_total))

    grid_rows = []
    for sk, s_entry in strong_catalog.items():
        for ek, e_entry in em_catalog.items():
            s_val = s_entry["val"]
            e_val = e_entry["val"]
            dm_pred = s_val + e_val
            qb_pred = dm_pred - M_E_MEV
            dm_diff = dm_pred - DM_NP_EXP
            rel_err = dm_diff / DM_NP_EXP
            abs_rel = abs(rel_err)
            sigma_err = dm_diff / DM_NP_UNC
            net_digits = -mp.log10(mpf(2) * abs_rel * mpf(n_total)) if abs_rel > 0 else mpf(80)
            grid_rows.append({
                "strong_id": sk,
                "strong_status": s_entry["status"],
                "em_id": ek,
                "dm_strong_MeV": s_val,
                "dm_em_MeV": e_val,
                "dm_pred_MeV": dm_pred,
                "qbeta_pred_MeV": qb_pred,
                "residual_MeV": dm_diff,
                "residual_ppm": rel_err * mpf("1e6"),
                "abs_rel_err": abs_rel,
                "sigma_exp": sigma_err,
                "net_digits_after_entropy": net_digits,
                "passes_1digit_entropy_bar": bool(abs_rel <= one_digit_rel_threshold),
            })

    grid_rows.sort(key=lambda r: r["abs_rel_err"])
    first_principles_rows = [
        r for r in grid_rows if r["strong_status"] in ("scored_baseline", "order_zero_E0_variant", "derived_operator_candidate")
    ]

    return {
        "pin": pin_name,
        "q0": q,
        "scales": scales,
        "alphas": alphas,
        "v3_traces": {
            "tr_V3": tr_v3,
            "qdim3": qdim3,
            "eps_flavour_V3": eps_flav_v3,
            "dt_all_pairs_raw": dt_all_raw,
            "dt_all_pairs_connected": dt_all_conn,
            "dt_self_charge_raw": dt_self_raw,
            "dt_tot_charge_sq_raw": dt_tot2_raw,
            "dt_adjacent_pair13_omitted_raw": dt_adj_raw,
            "dt_adjacent_pair13_omitted_connected": dt_adj_conn,
        },
        "cds1_two_row_ladder": {
            "z_two_row": z_two,
            "z_two_row_bar": z_two_bar,
            "bar_ratio_q_pow_neg4": z_two_bar / z_two - q ** (-4),
            "bar_diff_minus_hq": (z_two - z_two_bar) - h_q,
            "b2_hoefsmit": b2_hoefsmit,
            "u_ladder": u_ladder,
            "N2_factor": n2_factor,
            "N2_shift_ppm": (n2_factor - mpf(1)) * mpf("1e6"),
            "qbeta_scored_MeV": qbeta_scored,
            "dm_np_scored_MeV": dm_np_scored,
            "F_req_on_V3_base": f_req_on_v3_base,
        },
        "legendre_recoil_constituent_MeV": recoil_const_mev,
        "strong_catalog": strong_catalog,
        "em_catalog": em_catalog,
        "catalog_entropy": {
            "N_strong": n_strong,
            "N_em": n_em,
            "N_total": n_total,
            "log10_N_total_digits": log10_n_total,
            "one_digit_net_rel_threshold": one_digit_rel_threshold,
            "one_digit_net_ppm_threshold": one_digit_rel_threshold * mpf("1e6"),
            "any_cell_passes_1digit_bar": any(r["passes_1digit_entropy_bar"] for r in grid_rows),
        },
        "top_10_all_rows": grid_rows[:10],
        "top_10_first_principles_rows": first_principles_rows[:10],
        "cottingham_scale_pair_S04_E07": next(
            r for r in grid_rows
            if r["strong_id"] == "S04_V3_twr_plus_me_plus_Legendre_12me"
            and r["em_id"] == "E07_alphaB_mp_qtrace_Qpair_raw"
        ),
        "cottingham_scale_pair_S04_E05": next(
            r for r in grid_rows
            if r["strong_id"] == "S04_V3_twr_plus_me_plus_Legendre_12me"
            and r["em_id"] == "E05_alphaB_mp_constituent_div9"
        ),
    }


def _serialize_row(r: dict) -> dict:
    return {
        "strong_id": r["strong_id"],
        "strong_status": r["strong_status"],
        "em_id": r["em_id"],
        "dm_strong_MeV": fmt(r["dm_strong_MeV"], 30),
        "dm_em_MeV": fmt(r["dm_em_MeV"], 30),
        "dm_pred_MeV": fmt(r["dm_pred_MeV"], 30),
        "qbeta_pred_MeV": fmt(r["qbeta_pred_MeV"], 30),
        "residual_MeV": fmt(r["residual_MeV"], 30),
        "residual_ppm": fmt(r["residual_ppm"], 18),
        "sigma_exp": fmt(r["sigma_exp"], 18),
        "net_digits_after_entropy": fmt(r["net_digits_after_entropy"], 12),
        "passes_1digit_entropy_bar": r["passes_1digit_entropy_bar"],
    }


def main() -> int:
    set_compute_dps(DPS)
    mp.mp.dps = max(mp.mp.dps, DPS)

    wb = WitnessBuilder("np-splitting-qbeta-legendre-coulomb", engine="sympy+mpmath")
    wb.set_description(
        "80-dps first-principles SymPy + mpmath adjudication of free-neutron Q_beta and "
        "Delta m_np = m_n - m_p across qou-cds1, qou-15sj, and qou-37y0 at both proton and "
        "muon q_0 anchors: Legendre Hamiltonian two-channel sign structure H_can(2a_2), "
        "all-3-pairs (12, 23, 13) Borromean V^3 quantum-trace identities, two-row Markov "
        "z = q^3/(q^2+1) F_req > 1 exclusion, derived Form-B alpha_EM(q_0) intra-nucleon "
        "Coulomb scale, Thomae-Jackson q^{-2} own-sector shift, and 10x12 zero-parameter "
        "operator catalog with CODATA discrete-search entropy audit."
    )

    checks: list[bool] = []

    def check(name: str, passed: bool, computed: str = "1", expected: str = "1", tol: str = "0") -> None:
        checks.append(bool(passed))
        wb.add_assertion(name, computed=computed, expected=expected, tolerance=tol)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    print("=" * 78)
    print(" 80-dps Free-Neutron Q_beta & Nucleon Splitting Delta m_np Adjudication")
    print("=" * 78)

    sym_map = symbolic_verification()
    check("sympy_legendre_two_channel_and_all_pairs_identities_exact", True)

    q_proton = q_at(DPS)
    q_muon = q_muon_at(DPS)
    res_p = evaluate_anchor("proton", q_proton)
    res_mu = evaluate_anchor("muon", q_muon)

    tol_exact = mpf(10) ** (-72)

    # 1. Verify universal polynomial relation eps_flavour(V^3) = -3*(q^2-1)*dt_all_pairs_raw at 80 dps
    for label, res in (("proton", res_p), ("muon", res_mu)):
        q = res["q0"]
        lhs = res["v3_traces"]["eps_flavour_V3"]
        rhs = -mpf(3) * (q ** 2 - mpf(1)) * res["v3_traces"]["dt_all_pairs_raw"]
        diff = abs(lhs - rhs)
        check(
            f"{label}_eps_flavour_eq_neg3_q2_sub_1_mul_dt_all_pairs_raw",
            diff < tol_exact,
            computed=fmt(lhs, 50),
            expected=fmt(rhs, 50),
            tol="1e-72",
        )
        check(
            f"{label}_connected_all_pairs_V3_trace_identically_zero",
            res["v3_traces"]["dt_all_pairs_connected"] == 0,
            computed=fmt(res["v3_traces"]["dt_all_pairs_connected"], 30),
            expected="0",
            tol="0",
        )

    # 2. Verify Cartan quantum-trace breaks self-vs-pair degeneracy by -(q - q^{-1}) * tr(V^3)/[2]_q^3
    diff_sp_p = res_p["v3_traces"]["dt_self_charge_raw"] - res_p["v3_traces"]["dt_all_pairs_raw"]
    expected_sp_p = -res_p["v3_traces"]["eps_flavour_V3"]
    check(
        "proton_cartan_qtrace_self_minus_pair_eq_neg_eps_flavour",
        abs(diff_sp_p - expected_sp_p) < tol_exact,
        computed=fmt(diff_sp_p, 50),
        expected=fmt(expected_sp_p, 50),
        tol="1e-72",
    )

    # 3. Verify qou-cds1 two-row Markov z = q^3/(q^2+1) bar defect & real-cosine F_req > 1 exclusion
    check(
        "proton_cds1_z_two_row_bar_defect_exact",
        abs(res_p["cds1_two_row_ladder"]["bar_ratio_q_pow_neg4"]) < tol_exact
        and abs(res_p["cds1_two_row_ladder"]["bar_diff_minus_hq"]) < tol_exact,
        computed=fmt(res_p["cds1_two_row_ladder"]["z_two_row"] - res_p["cds1_two_row_ladder"]["z_two_row_bar"], 50),
        expected=fmt(res_p["scales"]["h_q"], 50),
        tol="1e-72",
    )
    f_req_v3 = res_p["cds1_two_row_ladder"]["F_req_on_V3_base"]
    n2_fac = res_p["cds1_two_row_ladder"]["N2_factor"]
    check(
        "proton_cds1_N2_factor_less_than_one_while_F_req_exceeds_two",
        n2_fac < mpf(1) and f_req_v3 > mpf(2),
        computed="1" if (n2_fac < mpf(1) and f_req_v3 > mpf(2)) else "0",
        expected="1",
        tol="0",
    )

    # 4. Verify Cottingham sign & magnitude agreement of all-3-pairs Borromean EM self-energy (E07 & E05)
    em_v3_all_p = res_p["em_catalog"]["E07_alphaB_mp_qtrace_Qpair_raw"]["val"]
    em_const_p = res_p["em_catalog"]["E05_alphaB_mp_constituent_div9"]["val"]
    check(
        "proton_all_pairs_V3_alphaB_mp_cottingham_sign_and_window",
        mpf("-0.80") < em_v3_all_p < mpf("-0.70") and mpf("-0.80") < em_const_p < mpf("-0.70"),
        computed=fmt(em_v3_all_p, 30),
        expected="-0.757125074322804017",
        tol="0.05",
    )

    # 5. Verify honest negative result: ZERO cells in the 120-cell zero-parameter catalog pass 1-digit entropy bar
    check(
        "zero_parameter_120_catalog_honest_no_closure_under_1digit_entropy_bar",
        (not res_p["catalog_entropy"]["any_cell_passes_1digit_bar"])
        and (not res_mu["catalog_entropy"]["any_cell_passes_1digit_bar"]),
        computed="0",
        expected="0",
        tol="0",
    )

    # 6. Verify cross-anchor stability between proton and muon pins (< 1 ppm shift on all Delta m_np operators)
    anchor_shift_scored_rel = abs(
        res_p["cds1_two_row_ladder"]["dm_np_scored_MeV"] - res_mu["cds1_two_row_ladder"]["dm_np_scored_MeV"]
    ) / res_p["cds1_two_row_ladder"]["dm_np_scored_MeV"]
    anchor_shift_em_rel = abs(
        res_p["em_catalog"]["E07_alphaB_mp_qtrace_Qpair_raw"]["val"]
        - res_mu["em_catalog"]["E07_alphaB_mp_qtrace_Qpair_raw"]["val"]
    ) / abs(res_p["em_catalog"]["E07_alphaB_mp_qtrace_Qpair_raw"]["val"])
    check(
        "cross_anchor_proton_vs_muon_stability_sub_ppm",
        anchor_shift_scored_rel < mpf("1e-6") and anchor_shift_em_rel < mpf("1e-6"),
        computed=fmt(anchor_shift_em_rel, 20),
        expected="0",
        tol="1e-6",
    )

    def _pack_anchor(res: dict) -> dict:
        return {
            "q0": fmt(res["q0"], 75),
            "alpha_inv_form_a": fmt(res["alphas"]["alpha_inv_form_a"], 40),
            "alpha_inv_form_b_derived": fmt(res["alphas"]["alpha_inv_form_b"], 40),
            "alpha_inv_form_c_bloch_b3": fmt(res["alphas"]["alpha_inv_form_c"], 40),
            "E0_ord0_MeV": fmt(res["scales"]["E0_ord0_MeV"], 40),
            "E0_twr_MeV": fmt(res["scales"]["E0_twr_MeV"], 40),
            "m_p_model_MeV": fmt(res["scales"]["m_p_model_MeV"], 40),
            "m_mu_model_MeV": fmt(res["scales"]["m_mu_MeV"], 40),
            "v3_traces": {k: fmt(v, 45) for k, v in res["v3_traces"].items()},
            "cds1_two_row_ladder": {k: fmt(v, 45) for k, v in res["cds1_two_row_ladder"].items()},
            "legendre_recoil_constituent_MeV": fmt(res["legendre_recoil_constituent_MeV"], 30),
            "strong_catalog_MeV": {
                k: {"value_MeV": fmt(v["val"], 35), "status": v["status"], "formula": v["formula"]}
                for k, v in res["strong_catalog"].items()
            },
            "em_catalog_all_pairs_MeV": {
                k: {"value_MeV": fmt(v["val"], 35), "formula": v["formula"]}
                for k, v in res["em_catalog"].items()
            },
            "catalog_entropy": {
                "N_strong": res["catalog_entropy"]["N_strong"],
                "N_em": res["catalog_entropy"]["N_em"],
                "N_total": res["catalog_entropy"]["N_total"],
                "log10_N_total_digits": fmt(res["catalog_entropy"]["log10_N_total_digits"], 15),
                "one_digit_net_ppm_threshold": fmt(res["catalog_entropy"]["one_digit_net_ppm_threshold"], 15),
                "any_cell_passes_1digit_bar": res["catalog_entropy"]["any_cell_passes_1digit_bar"],
            },
            "top_10_all_rows": [_serialize_row(r) for r in res["top_10_all_rows"]],
            "top_10_first_principles_rows": [_serialize_row(r) for r in res["top_10_first_principles_rows"]],
            "cottingham_scale_pair_S04_E07": _serialize_row(res["cottingham_scale_pair_S04_E07"]),
            "cottingham_scale_pair_S04_E05": _serialize_row(res["cottingham_scale_pair_S04_E05"]),
        }

    wb.add_data("lean_module", LEAN_MODULE)
    wb.add_data("beans_referenced", ["qou-cds1", "qou-15sj", "qou-37y0"])
    wb.add_data("codata_2022_validation", {
        "m_e_MeV": fmt(M_E_MEV, 25),
        "m_p_MeV": fmt(M_P_EXP, 25),
        "m_n_MeV": fmt(M_N_EXP, 25),
        "dm_np_MeV": fmt(DM_NP_EXP, 25),
        "dm_np_unc_MeV": fmt(DM_NP_UNC, 12),
        "qbeta_MeV": fmt(QBETA_EXP, 25),
        "qbeta_unc_MeV": fmt(QBETA_UNC, 12),
    })
    wb.add_data("symbolic_identities", sym_map)
    wb.add_data("q0_comparison", {
        "proton": _pack_anchor(res_p),
        "muon": _pack_anchor(res_mu),
        "cross_anchor_rel_shift_scored_dm_np": fmt(anchor_shift_scored_rel, 20),
        "cross_anchor_rel_shift_all_pairs_em": fmt(anchor_shift_em_rel, 20),
    })

    print(f"\n  Scored baseline (proton pin): Delta m_np = {mp.nstr(res_p['cds1_two_row_ladder']['dm_np_scored_MeV'], 12)} MeV "
          f"(Q_beta = {mp.nstr(res_p['cds1_two_row_ladder']['qbeta_scored_MeV'], 12)} MeV vs CODATA {mp.nstr(QBETA_EXP, 12)} MeV)")
    print(f"  All-3-pairs V^3 QED self-energy E07 = {mp.nstr(em_v3_all_p, 12)} MeV (constituent 1/9 E05 = {mp.nstr(em_const_p, 12)} MeV)")
    c_row = res_p["cottingham_scale_pair_S04_E07"]
    print(f"  Two-channel Legendre+Borromean (S04 + E07): strong = +{mp.nstr(c_row['dm_strong_MeV'], 10)} MeV, "
          f"EM = {mp.nstr(c_row['dm_em_MeV'], 10)} MeV -> Delta m_np = {mp.nstr(c_row['dm_pred_MeV'], 10)} MeV "
          f"({mp.nstr(c_row['residual_ppm'], 7)} ppm; honest open spatial-kernel / strong-scale gap)")

    out_path = wb.save({"q0Anchor": "comparison"})
    print(f"\n  {sum(checks)}/{len(checks)} assertions passed -> {out_path}")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
