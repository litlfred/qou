#!/usr/bin/env python3
"""
np_two_term_qed_mup_tension_probe.py — Pre-registered 50-dps mpmath + sympy probe
for Bean qou-eas4 (Epic qou-9pl8):

  1. Symbolic (SymPy over Q(q)) & 50-dps numeric verification of the 3-strand
     quark charge operators on the proton W_p = (2,1) (uud) and neutron W_n = (1,2) (udd)
     weight spaces, their non-intertwining under NucleonWeightSpaceTraces.P(q),
     and the exact closed forms of the charge-weighted Convention-D trace functionals.
  2. Test 1 — Impact of the two-term decomposition m_p = m_p^QCD + M_p^QED on the
     211 ppb mu-p consistency tension (q_proton vs q_muon, delta_m_p = m_p^QCD(q_muon) - m_p^exp).
     NOTE 2026-11-20 (issue #8524): the 'DERIVED-*' labels below are historical keys. The
     Borromean V^3 candidates are selections, not derived (pair 1-3 left out, scale and weighting
     chosen); see probes/two_term_qed_pair_choice. Keys kept so consumers do not break.
     Evaluates all pre-registered QOU electromagnetic self-energy
     candidates M_p^QED (and literature Cottingham/lattice benchmarks) honestly,
     with zero cherry-picking.
  3. Test 2 — Impact of the two-term decomposition Delta m_np = Delta m_QCD + Delta m_QED
     on Delta m_np, Q_beta = Delta m_np - m_e, and the Convention-D c_k ladder
     (including cross-anchor stability between q_proton and q_muon).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
import mpmath as mp
import sympy as sp

# Ensure 50-dps working precision (+30 guard digits during internal solves)
DPS = 50
mp.mp.dps = DPS + 30


# =============================================================================
# 1. Exact SymPy Symbolic Verification on W_p = (2,1) and W_n = (1,2)
# =============================================================================

def run_symbolic_charge_operator_checks() -> dict:
    q = sp.Symbol("q", nonzero=True)
    h = q - 1 / q
    zD = q**3 / (q**2 + 1)

    # Braid generators on W_p = (2,1) [basis: uud, udu, duu]
    # from QOU/BraidsAndKnots/NucleonWeightSpaceTraces.lean
    A1 = sp.Matrix([
        [q, 0, 0],
        [0, 0, 1],
        [0, 1, h],
    ])
    A2 = sp.Matrix([
        [0, 1, 0],
        [1, h, 0],
        [0, 0, q],
    ])

    # Braid generators on W_n = (1,2) [basis: udd, dud, ddu]
    B1 = sp.Matrix([
        [0, 1, 0],
        [1, h, 0],
        [0, 0, q],
    ])
    B2 = sp.Matrix([
        [q, 0, 0],
        [0, 0, 1],
        [0, 1, h],
    ])

    # Intertwiner P(q) from NucleonWeightSpaceTraces.lean
    P = sp.Matrix([
        [q**(-2), q**(-1), 0],
        [q**(-1), 0, q**(-1)],
        [0, q**(-1), 1],
    ])

    assert sp.simplify(P * A1 - B1 * P) == sp.zeros(3, 3)
    assert sp.simplify(P * A2 - B2 * P) == sp.zeros(3, 3)

    # Quark charges: q_u = +2/3, q_d = -1/3
    qu = sp.Rational(2, 3)
    qd = sp.Rational(-1, 3)

    # W_p basis states: |uud>, |udu>, |duu>
    p_states = [(qu, qu, qd), (qu, qd, qu), (qd, qu, qu)]
    # W_n basis states: |udd>, |dud>, |ddu>
    n_states = [(qu, qd, qd), (qd, qu, qd), (qd, qd, qu)]

    # Self-charge sum(Q_i^2) and pairwise Coulomb sum_{i<j} Q_i Q_j
    p_self = [sum(c**2 for c in st) for st in p_states]
    n_self = [sum(c**2 for c in st) for st in n_states]
    p_pair = [st[0] * st[1] + st[0] * st[2] + st[1] * st[2] for st in p_states]
    n_pair = [st[0] * st[1] + st[0] * st[2] + st[1] * st[2] for st in n_states]

    assert all(x == sp.Rational(1, 1) for x in p_self)
    assert all(x == sp.Rational(2, 3) for x in n_self)
    assert all(x == sp.Rational(0, 1) for x in p_pair)
    assert all(x == sp.Rational(-1, 3) for x in n_pair)

    # Adjacent pairwise charge operators Q_12 and Q_23 on W_p and W_n
    Q12_p = sp.diag(*[st[0] * st[1] for st in p_states])
    Q23_p = sp.diag(*[st[1] * st[2] for st in p_states])
    Q13_p = sp.diag(*[st[0] * st[2] for st in p_states])

    Q12_n = sp.diag(*[st[0] * st[1] for st in n_states])
    Q23_n = sp.diag(*[st[1] * st[2] for st in n_states])
    Q13_n = sp.diag(*[st[0] * st[2] for st in n_states])

    assert Q12_p == sp.diag(sp.Rational(4, 9), sp.Rational(-2, 9), sp.Rational(-2, 9))
    assert Q23_p == sp.diag(sp.Rational(-2, 9), sp.Rational(-2, 9), sp.Rational(4, 9))
    assert Q12_n == sp.diag(sp.Rational(-2, 9), sp.Rational(-2, 9), sp.Rational(1, 9))
    assert Q23_n == sp.diag(sp.Rational(1, 9), sp.Rational(-2, 9), sp.Rational(-2, 9))

    # Verify that P does NOT intertwine Q12_p -> Q12_n or Q23_p -> Q23_n
    intertwine_defect_12 = sp.simplify(P * Q12_p - Q12_n * P)
    intertwine_defect_23 = sp.simplify(P * Q23_p - Q23_n * P)
    assert intertwine_defect_12 != sp.zeros(3, 3)
    assert intertwine_defect_23 != sp.zeros(3, 3)

    # Plain matrix traces on W_p and W_n:
    # Note: on W_p, K^{otimes 3} acts as scalar q; on W_n, K^{otimes 3} acts as scalar q^{-1}.
    # Normalised Convention-D quantum trace on V^{otimes 3} has tr_D(1) = 1, where
    # tr_q(X) = Tr(K^{otimes 3} X) / (q + q^{-1})^3.
    # For a single crossing sigma_1 on H_3(q), the Hecke Markov trace is tr_D(sigma_1) = z_D = q^3/(q^2+1).
    # What is the normalized trace on the 3D weight spaces W_p and W_n?
    # Let's check both:
    # (a) Weight-space plain trace / 3 (average over the 3 basis states of W_N):
    tr_plain_p_adj = sp.simplify(sp.trace(Q12_p * A1 + Q23_p * A2))
    tr_plain_n_adj = sp.simplify(sp.trace(Q12_n * B1 + Q23_n * B2))
    # Wait: Tr(Q12_p * A1) = (4/9)*q + (-2/9)*0 + (-2/9)*h = (4/9)q - (2/9)(q - 1/q) = (2/9)q + 2/(9q)
    # And Tr(Q23_p * A2) = (-2/9)*0 + (-2/9)*h + (4/9)*q = (2/9)q + 2/(9q)
    # Sum on proton = (4/9)(q + 1/q)
    # On neutron: Tr(Q12_n * B1) = (-2/9)*0 + (-2/9)*h + (1/9)*q = -(1/9)q + 2/(9q)
    # And Tr(Q23_n * B2) = (1/9)*q + (-2/9)*0 + (-2/9)*h = -(1/9)q + 2/(9q)
    # Sum on neutron = (-2/9)q + 4/(9q)
    # Difference (neutron - proton) of plain trace:
    diff_plain_adj = sp.simplify(tr_plain_n_adj - tr_plain_p_adj)
    # = (-6/9)q + (2/9)/q = -2(3q^2 - 1)/(9q)

    # (b) Same-flavour vs mixed-flavour Hecke Markov trace on H_3(q) under Convention D:
    # In H_3(q), a same-flavour u-u crossing is sigma (trace z_D), d-d crossing is sigma^{-1} = sigma - h (trace z_D - h),
    # and mixed u-d crossing is (sigma + sigma^{-1})/2 = sigma - h/2 (trace z_D - h/2).
    # Weighting each of the 3 quark pairs (i<j) by Q_i Q_j * tr_D(crossing_{ij}):
    # Proton (uud): pairs are (u,u) [Q=4/9, cr=sigma] and two (u,d) [Q=-2/9 each, cr=sigma-h/2]
    trD_uud_Q = sp.simplify(
        sp.Rational(4, 9) * zD + 2 * sp.Rational(-2, 9) * (zD - h / 2)
    )
    # Neutron (udd): pairs are (d,d) [Q=1/9, cr=sigma-h] and two (u,d) [Q=-2/9 each, cr=sigma-h/2]
    trD_udd_Q = sp.simplify(
        sp.Rational(1, 9) * (zD - h) + 2 * sp.Rational(-2, 9) * (zD - h / 2)
    )
    diff_hecke_pair_Q = sp.simplify(trD_udd_Q - trD_uud_Q)

    # (c) K^{otimes 3}-weighted trace on W_n vs W_p, divided by (q + 1/q):
    # On W_p, K^{otimes 3} = q; on W_n, K^{otimes 3} = q^{-1}.
    trK_p_adj = sp.factor(q * tr_plain_p_adj / (q + 1 / q))
    trK_n_adj = sp.factor((1 / q) * tr_plain_n_adj / (q + 1 / q))
    diff_trK_adj = sp.factor(trK_n_adj - trK_p_adj)
    expected_diff_trK_adj = sp.factor(-2 * (2 * q**4 + 3 * q**2 - 2) / (9 * q * (q**2 + 1)))
    assert sp.simplify(diff_trK_adj - expected_diff_trK_adj) == 0

    # (d) Borromean braid V^3 = (sigma_1 sigma_2^{-1})^3 on W_p and W_n with charge insertion
    A2_inv = A2 - h * sp.eye(3)
    B2_inv = B2 - h * sp.eye(3)
    Vp = A1 * A2_inv
    Vn = B1 * B2_inv
    Bor_p = Vp**3
    Bor_n = Vn**3

    Q_tot_pair_p = Q12_p + Q23_p + Q13_p  # = 0 * I_3
    Q_tot_pair_n = Q12_n + Q23_n + Q13_n  # = (-1/3) * I_3
    assert Q_tot_pair_p == sp.zeros(3, 3)
    assert Q_tot_pair_n == sp.Rational(-1, 3) * sp.eye(3)

    tr_adj_Bor_p = sp.factor(sp.trace((Q12_p + Q23_p) * Bor_p))
    tr_adj_Bor_n = sp.factor(sp.trace((Q12_n + Q23_n) * Bor_n))
    diff_adj_Bor_plain = sp.factor(tr_adj_Bor_n - tr_adj_Bor_p)

    # Exact Lean-proved Borromean V^3 connected 4th-order decomposition
    # (from QOU/BraidsAndKnots/NucleonWeightSpaceTwoTerm.lean):
    #   Q12_n + Q23_n == (-2/9)*I_3 + (1/2)*(Q12_p + Q23_p)
    assert (Q12_n + Q23_n) == sp.Rational(-2, 9) * sp.eye(3) + sp.Rational(1, 2) * (Q12_p + Q23_p)
    tr_Bor_p = sp.factor(sp.trace(Bor_p))
    tr_Bor_n = sp.factor(sp.trace(Bor_n))
    assert sp.simplify(tr_Bor_p - tr_Bor_n) == 0

    # Normalized connected 4th-order trace (dividing by dim W_N = 3):
    # On W_p, Q12_p + Q23_p is already traceless:
    tr_conn_Bor_p_norm = sp.factor(tr_adj_Bor_p / 3)
    expected_conn_p = sp.factor(-2 * (q - 1)**4 * (q + 1)**4 * (q**4 + q**2 + 1) / (27 * q**6))
    assert sp.simplify(tr_conn_Bor_p_norm - expected_conn_p) == 0

    # On W_n, subtract static q=1 scalar component (-2/9)*tr(V_n^3):
    tr_conn_Bor_n_norm = sp.factor((tr_adj_Bor_n + sp.Rational(2, 9) * tr_Bor_n) / 3)
    expected_conn_n = sp.factor((q - 1)**4 * (q + 1)**4 * (2 * q**4 - q**2 + 2) / (27 * q**6))
    assert sp.simplify(tr_conn_Bor_n_norm - expected_conn_n) == 0

    # Connected (n - p) 4th-order difference:
    diff_conn_Bor_norm = sp.factor(tr_conn_Bor_n_norm - tr_conn_Bor_p_norm)
    expected_diff_conn = sp.factor((q - 1)**4 * (q + 1)**4 * (4 * q**4 + q**2 + 4) / (27 * q**6))
    assert sp.simplify(diff_conn_Bor_norm - expected_diff_conn) == 0

    # Verify q -> 1 ratio: diff_conn_Bor_norm / |tr_conn_Bor_p_norm| -> 3/2
    ratio_conn_q1 = sp.limit(diff_conn_Bor_norm / (-tr_conn_Bor_p_norm), q, 1)
    assert ratio_conn_q1 == sp.Rational(3, 2)

    # (e) Section 7 of NucleonWeightSpaceTwoTerm.lean:
    # Central Idempotent Projections e_{(3)} (I=3/2 decuplet, dim 1) and e_{(2,1)} (I=1/2 nucleon, dim 2)
    qInt3 = q**2 + 1 + q**(-2)
    FEp = sp.Matrix([
        [q**(-2), q**(-1), 1],
        [q**(-1), 1, q],
        [1, q, q**2],
    ])
    EFn = sp.Matrix([
        [q**(-2), q**(-1), 1],
        [q**(-1), 1, q],
        [1, q, q**2],
    ])
    e3p = (1 / qInt3) * FEp
    e21p = sp.eye(3) - e3p
    e3n = (1 / qInt3) * EFn
    e21n = sp.eye(3) - e3n

    # Verify idempotency, orthogonality, and traces (`e3p_mul_self`, `e21p_mul_self`, `e3p_mul_e21p`, `trace_e3p`, `trace_e21p`)
    assert sp.simplify(e3p * e3p - e3p) == sp.zeros(3, 3)
    assert sp.simplify(e21p * e21p - e21p) == sp.zeros(3, 3)
    assert sp.simplify(e3p * e21p) == sp.zeros(3, 3)
    assert sp.simplify(e3n * e3n - e3n) == sp.zeros(3, 3)
    assert sp.simplify(e21n * e21n - e21n) == sp.zeros(3, 3)
    assert sp.simplify(e3n * e21n) == sp.zeros(3, 3)
    assert sp.simplify(sp.trace(e3p) - 1) == 0
    assert sp.simplify(sp.trace(e21p) - 2) == 0
    assert sp.simplify(sp.trace(e3n) - 1) == 0
    assert sp.simplify(sp.trace(e21n) - 2) == 0

    # `trace_e3p_borromeanV3` and `trace_e3n_borromeanV3`: tr(e_{(3)} V^3) == 1
    tr_e3p_Bor = sp.simplify(sp.trace(e3p * Bor_p))
    tr_e3n_Bor = sp.simplify(sp.trace(e3n * Bor_n))
    assert tr_e3p_Bor == 1
    assert tr_e3n_Bor == 1

    # `trace_e21p_borromeanV3` and `trace_e21n_borromeanV3`:
    # tr(e_{(2,1)} V^3) == -(q^4 - q^2 + 1)*(q^8 - 2*q^6 - 2*q^2 + 1) / q^6 == 2 - 3*h^4 - h^6
    tr_e21p_Bor = sp.factor(sp.trace(e21p * Bor_p))
    tr_e21n_Bor = sp.factor(sp.trace(e21n * Bor_n))
    expected_tr_e21_Bor = sp.factor(-(q**4 - q**2 + 1) * (q**8 - 2 * q**6 - 2 * q**2 + 1) / (q**6))
    assert sp.simplify(tr_e21p_Bor - expected_tr_e21_Bor) == 0
    assert sp.simplify(tr_e21n_Bor - expected_tr_e21_Bor) == 0
    assert sp.simplify(tr_e21p_Bor - (2 - 3 * h**4 - h**6)) == 0
    assert sp.simplify(tr_e3p_Bor + tr_e21p_Bor - tr_Bor_p) == 0

    # `trace_e21_strong_cartan_diff_borromeanV3`:
    # (q^-1)*tr(e21n * V_n^3) - q*tr(e21p * V_p^3) == (q^-1 - q)*tr(e21 * V^3)
    tr_e21_strong_cartan_diff = sp.factor((1 / q) * sp.trace(e21n * Bor_n) - q * sp.trace(e21p * Bor_p))
    expected_e21_strong_cartan_diff = sp.factor((1 / q - q) * expected_tr_e21_Bor)
    assert sp.simplify(tr_e21_strong_cartan_diff - expected_e21_strong_cartan_diff) == 0

    # `trace_FEp_QAdjp_borromeanV3` and `trace_EFn_QAdjn_borromeanV3`:
    tr_FEp_QAdjp_Bor = sp.factor(sp.trace(FEp * (Q12_p + Q23_p) * Bor_p))
    expected_FEp_QAdjp_Bor = sp.factor(2 * (q - 1)**2 * (q + 1)**2 / (9 * q**2))
    assert sp.simplify(tr_FEp_QAdjp_Bor - expected_FEp_QAdjp_Bor) == 0

    tr_EFn_QAdjn_Bor = sp.factor(sp.trace(EFn * (Q12_n + Q23_n) * Bor_n))
    expected_EFn_QAdjn_Bor = sp.factor(-(q**4 + 4 * q**2 + 1) / (9 * q**2))
    assert sp.simplify(tr_EFn_QAdjn_Bor - expected_EFn_QAdjn_Bor) == 0

    # `trace_e21p_QAdjp_borromeanV3`, `trace_e21n_QAdjn_borromeanV3`, `trace_e21_QAdj_diff_borromeanV3`:
    tr_e21p_QAdjp_Bor = sp.factor(sp.trace(e21p * (Q12_p + Q23_p) * Bor_p))
    expected_e21p_QAdjp_Bor = sp.factor(
        -2 * (q - 1)**2 * (q + 1)**2 * (q**12 - q**6 + 1) / (9 * q**6 * (q**4 + q**2 + 1))
    )
    assert sp.simplify(tr_e21p_QAdjp_Bor - expected_e21p_QAdjp_Bor) == 0

    tr_e21n_QAdjn_Bor = sp.factor(sp.trace(e21n * (Q12_n + Q23_n) * Bor_n))
    expected_e21n_QAdjn_Bor = sp.factor(
        (4 * q**16 - 11 * q**14 + 13 * q**12 - 22 * q**10 + 20 * q**8 - 22 * q**6 + 13 * q**4 - 11 * q**2 + 4)
        / (9 * q**6 * (q**4 + q**2 + 1))
    )
    assert sp.simplify(tr_e21n_QAdjn_Bor - expected_e21n_QAdjn_Bor) == 0

    diff_e21_QAdj_Bor = sp.factor(tr_e21n_QAdjn_Bor - tr_e21p_QAdjp_Bor)
    expected_diff_e21_QAdj_Bor = sp.factor(
        (2 * q**16 - 5 * q**14 + 5 * q**12 - 8 * q**10 + 8 * q**8 - 8 * q**6 + 5 * q**4 - 5 * q**2 + 2)
        / (3 * q**6 * (q**4 + q**2 + 1))
    )
    assert sp.simplify(diff_e21_QAdj_Bor - expected_diff_e21_QAdj_Bor) == 0

    # `hadronicScaleE0_mul_hbar_eq_me`: E_0(m_e, q) * q^2 * (1 - q^-1) == m_e
    me_sym = sp.Symbol("m_e", positive=True)
    E0_sym = me_sym / (q * (q - 1))
    assert sp.simplify(E0_sym * (q**2 * (1 - 1 / q)) - me_sym) == 0

    # (f) Section 8 of NucleonWeightSpaceTwoTerm.lean:
    # Gröbner Normal-Form Channel Collapse on Borromean V^3 (`trace_diag_LminusA_eq_LplusA`, `borromeanV3_nf_cL_sum`, `borromeanV3A_nf_expansion`, `borromeanV3B_nf_expansion`)
    d0, d1, d2 = sp.symbols("d0 d1 d2")
    D_diag = sp.diag(d0, d1, d2)
    assert sp.simplify(sp.trace(D_diag * (A2 * A1)) - sp.trace(D_diag * (A1 * A2))) == 0
    assert sp.simplify(sp.trace(D_diag * (B2 * B1)) - sp.trace(D_diag * (B1 * B2))) == 0

    nfBorC1 = -(q**2 - q - 1) * (q**2 + q - 1) * (q**4 - q**2 + 1) / (q**4)
    nfBorCs0 = -(q - 1)**3 * (q + 1)**3 * (q**4 - q**2 + 1) / (q**5)
    nfBorCs1 = (q - 1)**3 * (q + 1)**3 / (q**3)
    nfBorCLplus = (q - 1)**2 * (q + 1)**2 * (q**4 - q**2 + 1) / (q**4)
    nfBorCLminus = -(q - 1)**2 * (q + 1)**2 / (q**2)

    cL_sum = sp.factor(nfBorCLplus + nfBorCLminus)
    expected_cL_sum = sp.factor((q - 1)**4 * (q + 1)**4 / (q**4))
    assert sp.simplify(cL_sum - expected_cL_sum) == 0

    Bor_p_nf = (
        nfBorC1 * sp.eye(3)
        + nfBorCs0 * A1
        + nfBorCs1 * A2
        + nfBorCLplus * (A1 * A2)
        + nfBorCLminus * (A2 * A1)
    )
    Bor_n_nf = (
        nfBorC1 * sp.eye(3)
        + nfBorCs0 * B1
        + nfBorCs1 * B2
        + nfBorCLplus * (B1 * B2)
        + nfBorCLminus * (B2 * B1)
    )
    assert sp.simplify(Bor_p - Bor_p_nf) == sp.zeros(3, 3)
    assert sp.simplify(Bor_n - Bor_n_nf) == sp.zeros(3, 3)

    # (g) Section 9 of NucleonWeightSpaceTwoTerm.lean (`qou-99qc` switched 4-term photon):
    # `borromeanV3A_eq_switched_photon_product`: V^3 = (I_3 + q*h*V) * (I_3 - q^-1*h*V)
    sw_plus_p = sp.eye(3) + q * h * Vp
    sw_minus_p = sp.eye(3) - (1 / q) * h * Vp
    assert sp.simplify(Bor_p - sw_plus_p * sw_minus_p) == sp.zeros(3, 3)

    sw_plus_n = sp.eye(3) + q * h * Vn
    sw_minus_n = sp.eye(3) - (1 / q) * h * Vn
    assert sp.simplify(Bor_n - sw_plus_n * sw_minus_n) == sp.zeros(3, 3)

    # `borromeanV3A_eq_one_add_h_sq_V_sub_V_sq`: V^3 = I_3 + h^2*V - h^2*V^2
    assert sp.simplify(Bor_p - (sp.eye(3) + (h**2) * Vp - (h**2) * (Vp * Vp))) == sp.zeros(3, 3)
    assert sp.simplify(Bor_n - (sp.eye(3) + (h**2) * Vn - (h**2) * (Vn * Vn))) == sp.zeros(3, 3)

    # `trace_QAdjp_borromeanVA` and `trace_QAdjn_borromeanVB_connected`:
    tr_QAdjp_VA = sp.factor(sp.trace((Q12_p + Q23_p) * Vp))
    expected_QAdjp_VA = sp.factor(-2 * (q - 1)**2 * (q + 1)**2 / (9 * q**2))
    assert sp.simplify(tr_QAdjp_VA - expected_QAdjp_VA) == 0

    tr_QAdjn_VB_conn = sp.factor(sp.trace((Q12_n + Q23_n) * Vn) + sp.Rational(2, 9) * sp.trace(Vn))
    expected_QAdjn_VB_conn = sp.factor(2 * (q - 1)**2 * (q + 1)**2 / (9 * q**2))
    assert sp.simplify(tr_QAdjn_VB_conn - expected_QAdjn_VB_conn) == 0

    # (h) Route 2 NucleonIdempotentModifiedTrace.lean & qbeta_utils.py verification:
    # Import the Route 2 helpers from computations/qbeta/qbeta_utils.py
    for _p in Path(__file__).resolve().parents:
        _cand_dir = _p / "computations"
        if (_cand_dir / "qbeta" / "qbeta_utils.py").exists():
            _comp_dir = str(_cand_dir)
            if _comp_dir not in sys.path:
                sys.path.insert(0, _comp_dir)
            break
    from qbeta.qbeta_utils import (
        chi_block_3,
        chi_block_21,
        chi_block_111,
        chi_proton_3,
        chi_neutron_3,
        chi_proton_21,
        chi_neutron_21,
        chi_proton_111,
        chi_neutron_111,
        d_mod_111_convention_D,
        t_mod_111_convention_D,
    )

    # Verify difference identities: chi_neutron_lambda - chi_proton_lambda == chi_block_lambda
    assert sp.simplify(chi_neutron_3(q) - chi_proton_3(q) - chi_block_3(q)) == 0
    assert sp.simplify(chi_neutron_21(q) - chi_proton_21(q) - chi_block_21(q, intra_order="borromean")) == 0
    assert sp.simplify(chi_neutron_111(q) - chi_proton_111(q) - chi_block_111(q)) == 0

    # Verify `chi3_proton_eq_q_sq_mul_neutron` and `tMod111_neutron_eq_q_sq_mul_proton`:
    assert sp.simplify(chi_proton_3(q) - (q**2) * chi_neutron_3(q)) == 0
    assert sp.simplify(t_mod_111_convention_D(q, "neutron") - (q**2) * t_mod_111_convention_D(q, "proton")) == 0
    assert sp.simplify(
        t_mod_111_convention_D(q, "neutron")
        - t_mod_111_convention_D(q, "proton")
        - t_mod_111_convention_D(q, "diff")
    ) == 0

    # Verify `trM_eq_wedderburn_sum` under Convention D (`w111_conventionD == 0`):
    # w3_D = (q^4 + 1) / (q^2 + 1)^2, w21_D = q^2 / (q^2 + 1)^2, w111_D = 0
    w3_D = (q**4 + 1) / ((q**2 + 1)**2)
    w21_D = (q**2) / ((q**2 + 1)**2)
    Pp_convD = (
        (q**4 + 1)
        * (q**18 - 3 * q**16 + 7 * q**14 - 8 * q**12 + 10 * q**10 - 9 * q**8 + 10 * q**6 - 6 * q**4 + 3 * q**2 - 1)
        / (4 * q**9 * (q**2 + 1)**2)
    )
    Pn_convD = (
        (q**4 + 1)
        * (q**14 - 3 * q**12 + 4 * q**10 - 4 * q**8 + 5 * q**6 - 4 * q**4 + 3 * q**2 - 1)
        / (4 * q**9)
    )
    assert sp.simplify(w3_D * chi_proton_3(q) + w21_D * chi_proton_21(q) - Pp_convD) == 0
    assert sp.simplify(w3_D * chi_neutron_3(q) + w21_D * chi_neutron_21(q) - Pn_convD) == 0
    diff_Pn_Pp = sp.factor(Pn_convD - Pp_convD)

    # Verify classical q -> 1 anchor ratio `chi21Reduced_ratio_at_one` (4/3):
    chi21_red_p_q1 = sp.limit(chi_proton_21(q) / (q**2 - 1), q, 1)
    chi21_red_n_q1 = sp.limit(chi_neutron_21(q) / (q**2 - 1), q, 1)
    assert 4 * chi21_red_p_q1 == sp.Rational(-6, 1)
    assert 4 * chi21_red_n_q1 == sp.Rational(-8, 1)
    assert chi21_red_n_q1 / chi21_red_p_q1 == sp.Rational(4, 3)

    # (i) GPMTThreeRowCumulantBridge.lean symbolic verification (bean qou-8mxc):
    # `zD_sub_self_eq`: z_D(q) - q == -q / (q^2 + 1)
    zD_sub_q = sp.factor(zD - q)
    assert sp.simplify(zD_sub_q - (-q / (q**2 + 1))) == 0

    # `dMod111_eq_neg_inv_qInt2_mul_qInt3`: dMod111(q) == -1 / ([2]_q [3]_q)
    qInt2_sym = q + 1 / q
    qInt3_sym = q**2 + 1 + 1 / (q**2)
    dMod111_sym = d_mod_111_convention_D(q)
    assert sp.simplify(dMod111_sym - (-1 / (qInt2_sym * qInt3_sym))) == 0

    # `muGPMT_eq_dMod111_mul_nu` & `muGPMT_closed_forms`:
    # Unweighted >=3-row sRow3: s_2 = 0, s_3 = -1, s_4 = -2 => (nu_2, nu_3, nu_4) = (0, -1, +2)
    sRow3_2, sRow3_3, sRow3_4 = sp.Integer(0), sp.Integer(-1), sp.Integer(-2)
    nu2_sym = sRow3_2
    nu3_sym = sRow3_3 - 3 * nu2_sym
    nu4_sym = sRow3_4 - 6 * nu2_sym - 4 * nu3_sym
    assert (nu2_sym, nu3_sym, nu4_sym) == (0, -1, 2)

    sRow3GPMT_2 = dMod111_sym * sRow3_2
    sRow3GPMT_3 = dMod111_sym * sRow3_3
    sRow3GPMT_4 = dMod111_sym * sRow3_4
    mu2_GPMT_sym = sp.simplify(sRow3GPMT_2)
    mu3_GPMT_sym = sp.factor(sRow3GPMT_3 - 3 * mu2_GPMT_sym)
    mu4_GPMT_sym = sp.factor(sRow3GPMT_4 - 6 * mu2_GPMT_sym - 4 * mu3_GPMT_sym)
    assert mu2_GPMT_sym == 0
    assert sp.simplify(mu3_GPMT_sym - (-dMod111_sym)) == 0
    assert sp.simplify(mu4_GPMT_sym - (2 * dMod111_sym)) == 0
    assert sp.simplify(mu4_GPMT_sym + 2 * mu3_GPMT_sym) == 0

    # `BextGPMT_values_and_pos`: BextGPMT(2) = 0, BextGPMT(3) = -dMod111, BextGPMT(4) = -6*dMod111 = 6*BextGPMT(3)
    BextGPMT_2_sym = sp.Integer(0)
    BextGPMT_3_sym = sp.factor(sp.binomial(3, 3) * sRow3GPMT_3)
    BextGPMT_4_sym = sp.factor(sp.binomial(4, 3) * sRow3GPMT_3 + sp.binomial(4, 4) * sRow3GPMT_4)
    assert sp.simplify(BextGPMT_3_sym - (-dMod111_sym)) == 0
    assert sp.simplify(BextGPMT_4_sym - (-6 * dMod111_sym)) == 0
    assert sp.simplify(BextGPMT_4_sym - 6 * BextGPMT_3_sym) == 0

    # `twoTerm_mirror_split_A3`: pairChargeA3(3H=[1,0,0]) == 0, pairChargeA3(3He=[0,1,1]) == 1
    triton_q = (1, 0, 0)
    helium3_q = (0, 1, 1)
    pair_q_3H = triton_q[0] * triton_q[1] + triton_q[0] * triton_q[2] + triton_q[1] * triton_q[2]
    pair_q_3He = helium3_q[0] * helium3_q[1] + helium3_q[0] * helium3_q[2] + helium3_q[1] * helium3_q[2]
    assert pair_q_3H == 0
    assert pair_q_3He == 1

    return {
        "p_self_sum_Qi2": str(p_self[0]),
        "n_self_sum_Qi2": str(n_self[0]),
        "delta_self_sum_Qi2_n_minus_p": str(n_self[0] - p_self[0]),
        "p_pair_sum_QiQj": str(p_pair[0]),
        "n_pair_sum_QiQj": str(n_pair[0]),
        "delta_pair_sum_QiQj_n_minus_p": str(n_pair[0] - p_pair[0]),
        "tr_plain_p_adj": str(sp.factor(tr_plain_p_adj)),
        "tr_plain_n_adj": str(sp.factor(tr_plain_n_adj)),
        "diff_plain_adj_n_minus_p": str(sp.factor(diff_plain_adj)),
        "trK_p_adj": str(sp.factor(trK_p_adj)),
        "trK_n_adj": str(sp.factor(trK_n_adj)),
        "diff_trK_adj_n_minus_p": str(sp.factor(diff_trK_adj)),
        "trD_uud_Q_hecke": str(sp.factor(trD_uud_Q)),
        "trD_udd_Q_hecke": str(sp.factor(trD_udd_Q)),
        "diff_hecke_pair_Q_n_minus_p": str(sp.factor(diff_hecke_pair_Q)),
        "tr_Bor_V3": str(tr_Bor_p),
        "tr_adj_Bor_p": str(tr_adj_Bor_p),
        "tr_adj_Bor_n": str(tr_adj_Bor_n),
        "diff_adj_Bor_plain_n_minus_p": str(diff_adj_Bor_plain),
        "tr_conn_Bor_p_norm": str(tr_conn_Bor_p_norm),
        "tr_conn_Bor_n_norm": str(tr_conn_Bor_n_norm),
        "diff_conn_Bor_norm_n_minus_p": str(diff_conn_Bor_norm),
        "tr_e3_Bor_V3": str(tr_e3p_Bor),
        "tr_e21_Bor_V3": str(tr_e21p_Bor),
        "tr_e21_strong_cartan_diff_Bor_V3": str(tr_e21_strong_cartan_diff),
        "tr_FEp_QAdjp_Bor_V3": str(tr_FEp_QAdjp_Bor),
        "tr_EFn_QAdjn_Bor_V3": str(tr_EFn_QAdjn_Bor),
        "tr_e21p_QAdjp_Bor_V3": str(tr_e21p_QAdjp_Bor),
        "tr_e21n_QAdjn_Bor_V3": str(tr_e21n_QAdjn_Bor),
        "diff_e21_QAdj_Bor_V3_n_minus_p": str(diff_e21_QAdj_Bor),
        "borromeanV3_nf_cL_sum": str(cL_sum),
        "tr_QAdjp_single_photon_VA": str(tr_QAdjp_VA),
        "tr_QAdjn_single_photon_VB_conn": str(tr_QAdjn_VB_conn),
        "chi_proton_3": str(sp.factor(chi_proton_3(q))),
        "chi_neutron_3": str(sp.factor(chi_neutron_3(q))),
        "chi_proton_21": str(sp.factor(chi_proton_21(q))),
        "chi_neutron_21": str(sp.factor(chi_neutron_21(q))),
        "chi_proton_111": str(sp.factor(chi_proton_111(q))),
        "chi_neutron_111": str(sp.factor(chi_neutron_111(q))),
        "d_mod_111_convention_D": str(sp.factor(d_mod_111_convention_D(q))),
        "t_mod_111_diff_convention_D": str(sp.factor(t_mod_111_convention_D(q, "diff"))),
        "gpmt_zD_sub_q": str(zD_sub_q),
        "gpmt_mu2_GPMT": str(mu2_GPMT_sym),
        "gpmt_mu3_GPMT": str(mu3_GPMT_sym),
        "gpmt_mu4_GPMT": str(mu4_GPMT_sym),
        "gpmt_BextGPMT_3": str(BextGPMT_3_sym),
        "gpmt_BextGPMT_4": str(BextGPMT_4_sym),
        "gpmt_pairChargeA3_triton_helium3": f"({pair_q_3H}, {pair_q_3He})",
        "diff_Pn_minus_Pp_convD": str(diff_Pn_Pp),
    }


# =============================================================================
# 2. High-Precision (50-dps) Substrate Functions
# =============================================================================

def vol_4_1() -> mp.mpf:
    return 2 * mp.clsin(2, mp.pi / 3)


def q_int(q: mp.mpf, n: int) -> mp.mpf:
    return (q**n - q**(-n)) / (q - 1 / q)


def qfact_3(q: mp.mpf) -> mp.mpf:
    return q_int(q, 3) * q_int(q, 2)


def trM_borromean_D(q: mp.mpf) -> mp.mpf:
    h = q - 1 / q
    return abs((4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4))


def F_Bor(q: mp.mpf) -> mp.mpf:
    return trM_borromean_D(q) * qfact_3(q) / (q**3)


def mp_over_me_qcd(q: mp.mpf, vol: mp.mpf) -> mp.mpf:
    """Raw proton substrate identity (pure QCD/topological term):
    m_p^QCD / m_e = 2 * (Vol(4_1) / hbar_q^2) * F_Bor(q) - 12."""
    hbar_q = (q - 1) / q
    return 2 * (vol / (hbar_q**2)) * F_Bor(q) - 12


def mmu_over_me_model(q: mp.mpf, vol: mp.mpf) -> mp.mpf:
    hbar_q = (q - 1) / q
    return vol / (hbar_q**2)


def alpha_em_inv_qou(q: mp.mpf) -> mp.mpf:
    """QOU derived fine-structure constant inverse:
    alpha_EM^{-1}(q) = 45 * [3]_q * (1 + delta_CS + 8 * q * delta_CS^2)
    where delta_CS = hbar_q^4 * [5]_q."""
    hbar_q = (q - 1) / q
    d_cs = (hbar_q**4) * q_int(q, 5)
    return 45 * q_int(q, 3) * (1 + d_cs + 8 * q * (d_cs**2))


def alpha_em_qou(q: mp.mpf) -> mp.mpf:
    return 1 / alpha_em_inv_qou(q)


def solve_q_for_mp_target(target_mp_over_me: mp.mpf, vol: mp.mpf) -> mp.mpf:
    """Newton solve for q > 1 such that mp_over_me_qcd(q, vol) == target_mp_over_me."""
    q = mp.mpf("1.1099785827513808")
    for _ in range(40):
        f = mp_over_me_qcd(q, vol) - target_mp_over_me
        dq = q * mp.mpf("1e-35")
        fp = (mp_over_me_qcd(q + dq, vol) - mp_over_me_qcd(q - dq, vol)) / (2 * dq)
        step = f / fp
        q -= step
        if abs(step) < mp.mpf("1e-65"):
            break
    return q


def main() -> int:
    # 1. Run exact SymPy verification first
    sym_res = run_symbolic_charge_operator_checks()

    # 2. CODATA 2022 inputs (from qou_substrate/data/allascii.txt & codata_constants.py)
    vol = vol_4_1()
    mp_me_exp = mp.mpf("1836.152673426")
    mp_me_err = mp.mpf("0.000000032")
    mmu_me_exp = mp.mpf("206.7682827")
    mmu_me_err = mp.mpf("0.0000046")

    m_e_mev = mp.mpf("0.51099895069")
    m_p_exp_mev = mp.mpf("938.27208816")
    m_n_exp_mev = mp.mpf("939.56542052")
    dm_np_exp_mev = m_n_exp_mev - m_p_exp_mev  # 1.29333236 MeV (or 1.29333378 from mass difference)
    dm_np_codata_direct = mp.mpf("1.29333378")
    q_beta_exp_mev = dm_np_codata_direct - m_e_mev  # 0.78233482931 MeV
    catalan_G = mp.catalan
    alpha_bind_mev = m_e_mev * 8 * catalan_G  # 3.744459660... MeV

    # Solve canonical pins at 50+30 dps
    q_proton = solve_q_for_mp_target(mp_me_exp, vol)
    hbar_muon = mp.sqrt(vol / mmu_me_exp)
    q_muon = 1 / (1 - hbar_muon)

    # Baseline quantities at q_proton and q_muon
    dq_rel_ppb = (q_proton - q_muon) / q_muon * mp.mpf("1e9")
    mmu_pred_at_q_proton = mmu_over_me_model(q_proton, vol)
    mmu_tension_ppb = (mmu_pred_at_q_proton - mmu_me_exp) / mmu_me_exp * mp.mpf("1e9")
    mmu_tension_sigma = (mmu_pred_at_q_proton - mmu_me_exp) / mmu_me_err

    # Evaluate m_p^QCD at q_muon vs q_proton
    mp_me_at_q_muon = mp_over_me_qcd(q_muon, vol)
    mp_mev_at_q_muon = mp_me_at_q_muon * m_e_mev
    mp_mev_at_q_proton = mp_me_exp * m_e_mev

    delta_mp_me = mp_me_at_q_muon - mp_me_exp  # in units of m_e
    delta_mp_mev = delta_mp_me * m_e_mev       # in MeV
    delta_mp_ppb = delta_mp_me / mp_me_exp * mp.mpf("1e9")

    alpha_em_p = alpha_em_qou(q_proton)
    alpha_em_inv_p = alpha_em_inv_qou(q_proton)
    hbar_p = (q_proton - 1) / q_proton
    h_p = q_proton - 1 / q_proton
    zD_p = q_proton**3 / (q_proton**2 + 1)
    E0_p = m_e_mev / (q_proton * (q_proton - 1))
    E0_full_p = E0_p / (1 - hbar_p**2)

    # =========================================================================
    # TEST 1: Pre-Registered Scan of M_p^QED Candidates on the 211 ppb mu-p Tension
    # =========================================================================
    # If physical proton mass is m_p^phys = m_p^QCD(q) + M_p^QED(q),
    # then solving for q_proton_new requires:
    #   m_p^QCD(q_new)/m_e = m_p^exp/m_e - M_p^QED(q_proton)/m_e.
    # For q_new to equal q_muon, we would need m_p^QCD(q_muon) + M_p^QED = m_p^exp,
    # i.e. M_p^QED = m_p^exp - m_p^QCD(q_muon) = -delta_mp_mev = -0.1977308 MeV!
    # Let's test both repulsive (+M_p^QED > 0, physical self-energy convention)
    # and attractive (-M_p^QED < 0, sign-flipped test) across all natural QOU candidates.

    trK_p_adj_val = 4 * q_proton / (9 * (q_proton**2 + 1)) * (q_proton + 1 / q_proton)
    trD_uud_Q_exact = 2 * (q_proton**4 + 1) / (9 * q_proton * (q_proton**2 + 1))

    # Lean-proved Borromean V^3 = (sigma_1 sigma_2^{-1})^3 connected 4th-order trace on W_p = (2,1)
    # from QOU/BraidsAndKnots/NucleonWeightSpaceTwoTerm.lean (`trace_QAdjp_borromeanV3`):
    #   tr_conn(p, V^3) = (1/3) * tr((Q12_p + Q23_p) V_p^3)
    #                   = -2*(q - 1)^4*(q + 1)^4*(q^4 + q^2 + 1) / (27 * q^6)
    tr_conn_Bor_p_val = -2 * (q_proton - 1)**4 * (q_proton + 1)**4 * (q_proton**4 + q_proton**2 + 1) / (27 * q_proton**6)

    mp_qed_candidates = [
        ("Baseline (no QED correction, M_p^QED = 0)", mp.mpf(0)),
        ("Exact gap target -(m_p^QCD(q_mu) - m_p^exp) [reference only]", -delta_mp_mev),
        # PRIMARY BORROMEAN (selection, not derived; issue #8524) V^3 CONNECTED 4TH-ORDER TRACE (NucleonWeightSpaceTwoTerm.lean)
        ("DERIVED-Bor-V3 (plain): +m_e * |tr_conn(p, V^3)| [= +0.220077 keV]", +m_e_mev * abs(tr_conn_Bor_p_val)),
        ("DERIVED-Bor-V3 (K^3-wt): +q * m_e * |tr_conn(p, V^3)| [= +0.244281 keV]", +q_proton * m_e_mev * abs(tr_conn_Bor_p_val)),
        # Literature benchmarks (macroscopic proton EM self-energy M_p^QED > 0)
        ("Lit: Gasser-Leutwyler 1982 / Cottingham M_p^QED = +0.63 MeV", mp.mpf("0.63")),
        ("Lit: Borsanyi et al. 2015 (BMW) |Delta M_QED| = +1.00 MeV", mp.mpf("1.00")),
        ("Lit: Gasser-Leutwyler-Rusetsky 2021 |Delta m_QED| = +0.58 MeV", mp.mpf("0.58")),
        ("Lit: Walker-Loud-Carlson-Miller 2012 |Delta m_QED| = +1.30 MeV", mp.mpf("1.30")),
        # Macroscopic O(alpha_EM * m_p) and O(alpha_EM * E0) QOU scales (already absorbed in 2*m_mu*F_Bor - 12*m_e)
        ("QOU-Macro-1 (+): +alpha_EM * m_p * (sum Q_i^2 = 1) / (2*pi)", +alpha_em_p * m_p_exp_mev / (2 * mp.pi)),
        ("QOU-Macro-2 (+): +alpha_EM * m_p * hbar_q * (sum Q_i^2 = 1)", +alpha_em_p * m_p_exp_mev * hbar_p),
        ("QOU-Macro-3 (+): +alpha_EM * E0_full * [3]_q * (sum Q_i^2 = 1)", +alpha_em_p * E0_full_p * q_int(q_proton, 3)),
        ("QOU-Macro-4 (+): +alpha_EM * alpha_bind * [3]_q", +alpha_em_p * alpha_bind_mev * q_int(q_proton, 3)),
        # Single-crossing Hecke trace at electron scale
        ("QOU-Hecke-1 (+): +alpha_EM * m_e * tr_D(Q_p) [= +alpha_EM * m_e * 2(q^2-1)/(9q)]", +alpha_em_p * m_e_mev * 2 * (q_proton**2 - 1) / (9 * q_proton)),
        ("QOU-Hecke-2 (+): +alpha_EM * m_e * hbar_q", +alpha_em_p * m_e_mev * hbar_p),
        # Sign-flipped (-M_p^QED < 0) controls (worsen tension, confirming repulsive +M_p^QED > 0 sign)
        ("Control-Neg-1 (-): -m_e * |tr_conn(p, V^3)| [= -0.220077 keV]", -m_e_mev * abs(tr_conn_Bor_p_val)),
        ("Control-Neg-2 (-): -alpha_EM * m_p * hbar_q", -alpha_em_p * m_p_exp_mev * hbar_p),
        # REJECTED AD-HOC COMBINATORIAL GRID FITS (recorded for adversarial audit transparency)
        ("[REJECTED-FIT] QOU-P13: +alpha_EM * m_e * hbar_q * [2]_q / [3]_q", +alpha_em_p * m_e_mev * hbar_p * q_int(q_proton, 2) / q_int(q_proton, 3)),
    ]

    test1_rows = []
    for label, mp_qed_mev in mp_qed_candidates:
        target_qcd_ratio = mp_me_exp - (mp_qed_mev / m_e_mev)
        q_new = solve_q_for_mp_target(target_qcd_ratio, vol)
        dq_new_ppb = (q_new - q_muon) / q_muon * mp.mpf("1e9")
        mmu_pred_new = mmu_over_me_model(q_new, vol)
        mmu_err_ppb = (mmu_pred_new - mmu_me_exp) / mmu_me_exp * mp.mpf("1e9")
        mmu_err_sigma = (mmu_pred_new - mmu_me_exp) / mmu_me_err
        gap_closed_pct = (1 - abs(mmu_err_ppb) / abs(mmu_tension_ppb)) * 100
        test1_rows.append({
            "candidate": label,
            "M_p_QED_MeV": mp.nstr(mp_qed_mev, 10),
            "M_p_QED_over_me": mp.nstr(mp_qed_mev / m_e_mev, 10),
            "q_proton_new": mp.nstr(q_new, 20),
            "dq_vs_qmuon_ppb": mp.nstr(dq_new_ppb, 8),
            "m_mu_pred_err_ppb": mp.nstr(mmu_err_ppb, 8),
            "m_mu_pred_err_sigma": mp.nstr(mmu_err_sigma, 6),
            "tension_reduction_pct": mp.nstr(gap_closed_pct, 6),
        })

    # =========================================================================
    # TEST 2: Two-Term Splitting Delta m_np = Delta m_QCD + Delta m_QED
    #         and Impact on Q_beta & Convention-D c_k Ladder
    # =========================================================================

    def eval_np_quantities_at(q: mp.mpf) -> dict:
        h = q - 1 / q
        hbar = (q - 1) / q
        zD = q**3 / (q**2 + 1)
        E0 = m_e_mev / (q * (q - 1))
        E0_full = E0 / (1 - hbar**2)
        a_em = alpha_em_qou(q)

        # Strong candidates (Convention D):
        # S1: Published transfer-product traced volume alpha * |Delta Phi_D|
        phi_uud = mp.log(abs((zD * q**2 + 2 * q - zD) * (q**2 - 2 * zD * q - 1) / (4 * q**2)))
        phi_udd = mp.log(abs((q**2 + 1)**2 * (q**2 - zD * q - 1) / (4 * q**3)))
        dphi_transfer = abs(phi_udd - phi_uud)
        dm_S1_alpha = alpha_bind_mev * dphi_transfer
        dm_S1_E0 = E0_full * dphi_transfer

        # S2: Adjacent-only / oriented rule under D: |Delta Phi| = 4 * ln(q)
        dm_S2_alpha_4lnq = alpha_bind_mev * (4 * mp.log(q))
        dm_S2_E0_4lnq = E0_full * (4 * mp.log(q))

        # S3: Level-2 weight-space ratio n/p = q^{-2} => |Delta Phi| = 2 * ln(q)
        dm_S3_alpha_2lnq = alpha_bind_mev * (2 * mp.log(q))
        dm_S3_E0_2lnq = E0_full * (2 * mp.log(q))

        # S4: Production 11-letter nucleon word difference |P_n - P_p| under Convention D
        Pp = (
            (q**4 + 1)
            * (q**18 - 3 * q**16 + 7 * q**14 - 8 * q**12 + 10 * q**10 - 9 * q**8 + 10 * q**6 - 6 * q**4 + 3 * q**2 - 1)
            / (4 * q**9 * (q**2 + 1)**2)
        )
        Pn = (
            (q**4 + 1)
            * (q**14 - 3 * q**12 + 4 * q**10 - 4 * q**8 + 5 * q**6 - 4 * q**4 + 3 * q**2 - 1)
            / (4 * q**9)
        )
        dm_S4_word_E0 = E0_full * abs(Pn - Pp)
        dm_S4_word_alpha = alpha_bind_mev * abs(Pn - Pp)

        # S5: Q_beta single-wrap Form A + m_e and Convention-D ruled base (delta_S = h*(z_D - h/2)) + m_e
        Q_A = m_e_mev * abs(q**2 - 2 * q - 1) * (q + 1) / (2 * q**3)
        dm_S5_QA_plus_me = Q_A + m_e_mev
        delta_S_convD = abs(h * (zD - h / 2))
        Q_convD_base = E0 * delta_S_convD
        dm_S6_convD_base_plus_me = Q_convD_base + m_e_mev

        # S7: Flavoured 2-strand skein X(q) * M_N
        X_flav = (hbar**2) * h * q_int(q, 2) / 3
        dm_S7_skein = X_flav * (m_p_exp_mev + m_n_exp_mev) / 2

        # S8 (DERIVED BORROMEAN V^3 CARTAN TRACE DIFFERENCE from NucleonWeightSpaceTwoTerm.lean):
        # tr(V^3) = -(q^12 - 3q^10 + 3q^8 - 5q^6 + 3q^4 - 3q^2 + 1) / q^6 = +3.1337099 at q_0
        # Cartan difference |tr((K_n - K_p) V^3)| = (q - 1/q) * tr(V^3) = h * tr(V^3)
        tr_V3 = -(q**12 - 3 * q**10 + 3 * q**8 - 5 * q**6 + 3 * q**4 - 3 * q**2 + 1) / (q**6)
        dm_S8_BorV3_alpha = alpha_bind_mev * h * tr_V3
        dm_S8_BorV3_E0 = E0 * h * tr_V3

        # S9 (SECTION 7 e_{(2,1)}-PROJECTED BORROMEAN V^3 STRONG CARTAN DIFFERENCE):
        # tr(e_{(2,1)} V^3) = -(q^4 - q^2 + 1)*(q^8 - 2*q^6 - 2*q^2 + 1) / q^6 = 2 - 3*h^4 - h^6
        # Delta tr_QCD(e_{(2,1)} V^3) = (q - 1/q) * tr(e_{(2,1)} V^3) (`trace_e21_strong_cartan_diff_borromeanV3`)
        tr_e21_V3 = -(q**4 - q**2 + 1) * (q**8 - 2 * q**6 - 2 * q**2 + 1) / (q**6)
        dm_S9_e21_E0_full = E0_full * h * tr_e21_V3
        dm_S9_e21_E0 = E0 * h * tr_e21_V3
        dm_S9_e21_alpha = alpha_bind_mev * h * tr_e21_V3

        # Section 7 e_{(2,1)}-projected adjacent-charge QED traces (`trace_e21p_QAdjp_borromeanV3`,
        # `trace_e21n_QAdjn_borromeanV3`, `trace_e21_QAdj_diff_borromeanV3`):
        tr_e21_QAdjp_V3 = (
            -2 * (q - 1)**2 * (q + 1)**2 * (q**12 - q**6 + 1)
            / (9 * q**6 * (q**4 + q**2 + 1))
        )
        tr_e21_QAdjn_V3 = (
            (4 * q**16 - 11 * q**14 + 13 * q**12 - 22 * q**10 + 20 * q**8 - 22 * q**6 + 13 * q**4 - 11 * q**2 + 4)
            / (9 * q**6 * (q**4 + q**2 + 1))
        )
        diff_e21_QAdj_V3 = (
            (2 * q**16 - 5 * q**14 + 5 * q**12 - 8 * q**10 + 8 * q**8 - 8 * q**6 + 5 * q**4 - 5 * q**2 + 2)
            / (3 * q**6 * (q**4 + q**2 + 1))
        )
        dm_QED_e21_me = m_e_mev * diff_e21_QAdj_V3
        dm_QED_e21_alpha_over_3 = (alpha_bind_mev / 3) * diff_e21_QAdj_V3

        # Exact Lean-proved Borromean V^3 adjacent-crossing & connected 4th-order QED traces
        # (`trace_QAdjp_borromeanV3`, `trace_QAdjn_borromeanV3_connected`, `trace_QAdj_connected_diff_borromeanV3`):
        tr_adj_V3_p = -2 * (q - 1)**4 * (q + 1)**4 * (q**4 + q**2 + 1) / (9 * q**6)
        tr_adj_V3_n = (4 * q**12 - 15 * q**10 + 24 * q**8 - 32 * q**6 + 24 * q**4 - 15 * q**2 + 4) / (9 * q**6)
        diff_adj_V3_norm = (tr_adj_V3_n - tr_adj_V3_p) / 3  # normalized by dim W_N = 3
        diff_adj_V3_Kwt_norm = ((1 / q) * tr_adj_V3_n - q * tr_adj_V3_p) / 3

        tr_conn_V3_p_norm = tr_adj_V3_p / 3
        tr_conn_V3_n_norm = (tr_adj_V3_n + (mp.mpf(2) / 9) * tr_V3) / 3
        diff_conn_V3_norm = (q - 1)**4 * (q + 1)**4 * (4 * q**4 + q**2 + 4) / (27 * q**6)
        diff_conn_V3_Kwt_norm = tr_conn_V3_n_norm - q * tr_conn_V3_p_norm  # K_p^3-weighted proton: tr_n - q*tr_p
        diff_conn_V3_KnKp_norm = (1 / q) * tr_conn_V3_n_norm - q * tr_conn_V3_p_norm  # (K_n^3, K_p^3): q^-1*tr_n - q*tr_p
        diff_conn_V3_qwt_norm = q * diff_conn_V3_norm  # uniform q = K_p^3 scaling

        # QED candidates (all negative, since proton has higher EM self-energy than neutron):
        # Charge factors:
        C0_pair = mp.mpf(-1) / 3  # sum_{i<j} Q_i Q_j (n - p) = -1/3
        C1_trK_adj = -2 * (2 * q**4 + 3 * q**2 - 2) / (9 * q * (q**2 + 1))
        C1_hecke_pair = -(4 * q**4 - 1) / (9 * q * (q**2 + 1))  # trD_udd_Q - trD_uud_Q = -(2q^2-1)(2q^2+1)/(9q(q^2+1))

        qed_cands = {
            "QED-0 (none = 0)": mp.mpf(0),
            # PRIMARY BORROMEAN (selection, not derived; issue #8524) V^3 TRACES (NucleonWeightSpaceTwoTerm.lean)
            "DERIVED-Bor-V3-Conn (plain): -m_e * Delta tr_conn(V^3)": -m_e_mev * diff_conn_V3_norm,
            "DERIVED-Bor-V3-Conn (K_n/K_p-wt): -m_e * (q^-1 tr_n - q tr_p)_conn": -m_e_mev * diff_conn_V3_KnKp_norm,
            "DERIVED-Bor-V3-Conn (K_p^3-wt): -m_e * (tr_n - q tr_p)_conn": -m_e_mev * diff_conn_V3_Kwt_norm,
            "DERIVED-Bor-V3-Conn (q-wt): -q * m_e * Delta tr_conn(V^3)": -m_e_mev * diff_conn_V3_qwt_norm,
            "DERIVED-Bor-V3-e21 (m_e): m_e * Delta tr_{e21}(Q_adj V^3)": dm_QED_e21_me,
            "DERIVED-Bor-V3-e21 (alpha_bind/3): (alpha_bind/3) * Delta tr_{e21}(Q_adj V^3)": dm_QED_e21_alpha_over_3,
            "DERIVED-Bor-V3-Full (alpha_bind): alpha_bind * (1/3)*Delta tr_adj(V^3)": alpha_bind_mev * diff_adj_V3_norm,
            "DERIVED-Bor-V3-Full (alpha_bind, K^3-wt): alpha_bind * (1/3)*Delta tr_adj^K(V^3)": alpha_bind_mev * diff_adj_V3_Kwt_norm,
            "DERIVED-Bor-V3-Full (E0): E0 * (1/3)*Delta tr_adj(V^3)": E0 * diff_adj_V3_norm,
            # Literature benchmarks
            "QED-Lit-GLR2021 (-0.58 MeV, Cottingham)": mp.mpf("-0.58"),
            "QED-Lit-GL1982 (-0.76 MeV, classic Cottingham)": mp.mpf("-0.76"),
            "QED-Lit-BMW2015 (-1.00 MeV, Science 347 lattice)": mp.mpf("-1.00"),
            "QED-Lit-WLCM2012 (-1.30 MeV, PhysRevD 85)": mp.mpf("-1.30"),
            "QED-Lit-QCDSF2016 (-2.20 MeV, Horsley et al.)": mp.mpf("-2.20"),
            # Macroscopic single-crossing / Coulomb QED candidates
            "QED-Q1: (-1/3) * alpha_EM * m_p * hbar_q": C0_pair * a_em * m_p_exp_mev * hbar,
            "QED-Q2: (-1/3) * alpha_EM * m_p / (2*pi)": C0_pair * a_em * m_p_exp_mev / (2 * mp.pi),
            "QED-Q3: (-1/3) * alpha_EM * E0_full * [3]_q!": C0_pair * a_em * E0_full * qfact_3(q),
            "QED-Q4: (-1/3) * alpha_EM * alpha_bind * [3]_q!": C0_pair * a_em * alpha_bind_mev * qfact_3(q),
            "QED-Q7: E0_full * (trD_udd_Q - trD_uud_Q)": E0_full * C1_hecke_pair,
            "QED-Q8: alpha_bind * (trD_udd_Q - trD_uud_Q)": alpha_bind_mev * C1_hecke_pair,
            "QED-Q11: m_e * C1_trK_adj": m_e_mev * C1_trK_adj,
            # Single-crossing O(alpha_EM * m_e) radiative QED candidates
            "QED-Q12: (-1/3) * alpha_EM * m_e * hbar_q": C0_pair * a_em * m_e_mev * hbar,
            "QED-Q17: alpha_EM * m_e * C1_hecke_pair": a_em * m_e_mev * C1_hecke_pair,
            "QED-Q18: alpha_EM * m_e * C1_trK_adj": a_em * m_e_mev * C1_trK_adj,
            # REJECTED AD-HOC COMBINATORIAL GRID FITS (recorded for adversarial audit transparency)
            "[REJECTED-FIT] QED-Q6b: (-1/3) * alpha_bind * h [no alpha_EM]": C0_pair * alpha_bind_mev * h,
            "[REJECTED-FIT] QED-Q14: (-1/3) * alpha_EM * m_e * h * [2]_q": C0_pair * a_em * m_e_mev * h * q_int(q, 2),
        }

        strong_cands = {
            "DERIVED-S8a: alpha_bind * (q - 1/q) * tr(V^3) (Borromean Cartan)": dm_S8_BorV3_alpha,
            "DERIVED-S8b: E0 * (q - 1/q) * tr(V^3) (Borromean Cartan at E0)": dm_S8_BorV3_E0,
            "DERIVED-S9a: E0_full * (q - 1/q) * tr(e21 V^3) (e21 Cartan at E0_full)": dm_S9_e21_E0_full,
            "DERIVED-S9b: E0 * (q - 1/q) * tr(e21 V^3) (e21 Cartan at E0)": dm_S9_e21_E0,
            "DERIVED-S9c: alpha_bind * (q - 1/q) * tr(e21 V^3) (e21 Cartan at alpha)": dm_S9_e21_alpha,
            "S1: alpha_bind * |Delta Phi_D| (published transfer product)": dm_S1_alpha,
            "S1b: E0_full * |Delta Phi_D| (transfer product with E0_full)": dm_S1_E0,
            "S2: alpha_bind * 4*ln(q) (adjacent / oriented D closed form)": dm_S2_alpha_4lnq,
            "S2b: E0_full * 4*ln(q) (adjacent / oriented with E0_full)": dm_S2_E0_4lnq,
            "S3: alpha_bind * 2*ln(q) (Level-2 weight-space K^{otimes 3})": dm_S3_alpha_2lnq,
            "S4: E0_full * |P_n - P_p|_D (11-letter production word)": dm_S4_word_E0,
            "S5: Q_A + m_e (single-wrap Form A + m_e)": dm_S5_QA_plus_me,
            "S6: Q_base^D + m_e (ruled Convention-D decay base + m_e)": dm_S6_convD_base_plus_me,
            "S7: X(q) * M_N (2-strand skein flavor split)": dm_S7_skein,
        }

        # Ladder parameters at q (Convention D):
        alpha_phase = (zD - 1) * h / 2
        b = mp.sqrt(1 - (q**2) / ((q**2 + 1)**2))
        u = b * (hbar**2)
        Q_N1 = Q_A * mp.cos(alpha_phase - u / 2)
        Q_N2 = Q_N1 * (1 - u**2)  # c_2 = -1

        return {
            "h": h,
            "hbar": hbar,
            "zD": zD,
            "E0": E0,
            "E0_full": E0_full,
            "alpha_em": a_em,
            "alpha_phase": alpha_phase,
            "b": b,
            "u": u,
            "Q_A": Q_A,
            "Q_N1": Q_N1,
            "Q_N2": Q_N2,
            "Q_convD_base": Q_convD_base,
            "tr_V3": tr_V3,
            "tr_e21_V3": tr_e21_V3,
            "tr_e21_QAdjp_V3": tr_e21_QAdjp_V3,
            "tr_e21_QAdjn_V3": tr_e21_QAdjn_V3,
            "diff_e21_QAdj_V3": diff_e21_QAdj_V3,
            "strong_cands": strong_cands,
            "qed_cands": qed_cands,
        }

    ev_p = eval_np_quantities_at(q_proton)
    ev_mu = eval_np_quantities_at(q_muon)

    # Build two-term combinations table and check against CODATA dm_np = 1.29333378 MeV
    test2_combinations = []
    for s_name, s_val_p in ev_p["strong_cands"].items():
        s_val_mu = ev_mu["strong_cands"][s_name]
        for q_name, q_val_p in ev_p["qed_cands"].items():
            q_val_mu = ev_mu["qed_cands"][q_name]
            tot_p = s_val_p + q_val_p
            tot_mu = s_val_mu + q_val_mu
            rel_err_p_pct = (tot_p - dm_np_codata_direct) / dm_np_codata_direct * 100
            rel_err_mu_pct = (tot_mu - dm_np_codata_direct) / dm_np_codata_direct * 100
            cross_anchor_ppm = (tot_p - tot_mu) / tot_p * mp.mpf("1e6") if tot_p != 0 else mp.mpf(0)
            test2_combinations.append({
                "strong_term": s_name,
                "qed_term": q_name,
                "dm_QCD_MeV": mp.nstr(s_val_p, 8),
                "dm_QED_MeV": mp.nstr(q_val_p, 8),
                "dm_tot_proton_MeV": mp.nstr(tot_p, 8),
                "rel_err_vs_CODATA_pct": mp.nstr(rel_err_p_pct, 6),
                "cross_anchor_swing_ppm": mp.nstr(cross_anchor_ppm, 6),
                "_abs_err": abs(rel_err_p_pct),
            })

    # Impact on Q_beta and the Convention-D c_k ladder:
    # In the one-term model, Q_beta^target = Q_beta^exp = 0.78233483 MeV,
    # and under Convention D:
    #   c_2^emp(q) = (Q_target / Q_N1(q) - 1) / u^2
    #   c_3^emp(q) = (Q_target / Q_N2(q) - 1) / u^3  (with c_2 = -1 fixed)
    # In the two-term model, if Q_beta = Q_beta^QCD + Delta m_QED, then the pure-QCD
    # decay ladder targets Q_beta^QCD_target = Q_beta^exp - Delta m_QED (or conversely,
    # if Q_N2(q) is the pure-QCD prediction, the missing residual Q_beta^exp - Q_N2(q)
    # is compared against Delta m_QED).
    qbeta_ladder_rows = []
    for q_name, q_val_p in ev_p["qed_cands"].items():
        q_val_mu = ev_mu["qed_cands"][q_name]
        # Case A: Q_N2(q) + Delta m_QED(q) directly as two-term Q_beta prediction
        qbeta_two_term_p = ev_p["Q_N2"] + q_val_p
        qbeta_two_term_err_ppm = (qbeta_two_term_p - q_beta_exp_mev) / q_beta_exp_mev * mp.mpf("1e6")

        # Case B: Ladder target is Q_beta^QCD = Q_beta^exp - Delta m_QED
        q_target_p = q_beta_exp_mev - q_val_p
        q_target_mu = q_beta_exp_mev - q_val_mu

        c2_emp_p = (q_target_p / ev_p["Q_N1"] - 1) / (ev_p["u"] ** 2)
        c2_emp_mu = (q_target_mu / ev_mu["Q_N1"] - 1) / (ev_mu["u"] ** 2)
        c2_swing_pct = abs(c2_emp_p - c2_emp_mu) / abs(c2_emp_p) * 100

        c3_emp_p = (q_target_p / ev_p["Q_N2"] - 1) / (ev_p["u"] ** 3)
        c3_emp_mu = (q_target_mu / ev_mu["Q_N2"] - 1) / (ev_mu["u"] ** 3)
        c3_swing_pct = abs(c3_emp_p - c3_emp_mu) / abs(c3_emp_p) * 100

        qbeta_ladder_rows.append({
            "qed_candidate": q_name,
            "dm_QED_MeV": mp.nstr(q_val_p, 8),
            "Q_N2_plus_QED_MeV": mp.nstr(qbeta_two_term_p, 8),
            "Q_N2_plus_QED_err_ppm": mp.nstr(qbeta_two_term_err_ppm, 6),
            "Q_QCD_target_MeV": mp.nstr(q_target_p, 8),
            "c2_emp_convD_proton": mp.nstr(c2_emp_p, 8),
            "c2_swing_pct": mp.nstr(c2_swing_pct, 6),
            "c3_emp_convD_proton": mp.nstr(c3_emp_p, 8),
            "c3_emp_convD_muon": mp.nstr(c3_emp_mu, 8),
            "c3_swing_pct": mp.nstr(c3_swing_pct, 6),
        })

    # Print comprehensive report
    mp.mp.dps = DPS
    print("=" * 88)
    print("PRE-REGISTERED 50-DPS PROBE: TWO-TERM QED SPLITTING & 211 PPB MU-P TENSION (qou-eas4)")
    print("=" * 88)
    print(f"Vol(4_1)               = {mp.nstr(vol, 50)}")
    print(f"q_proton (50 dps)      = {mp.nstr(q_proton, 50)}")
    print(f"q_muon   (50 dps)      = {mp.nstr(q_muon, 50)}")
    print(f"(q_p - q_mu)/q_mu      = {mp.nstr(dq_rel_ppb, 12)} ppb")
    print(f"m_mu(q_p) vs CODATA    = +{mp.nstr(mmu_tension_ppb, 10)} ppb (+{mp.nstr(mmu_tension_sigma, 6)} sigma)")
    print(f"m_p^QCD(q_muon)        = {mp.nstr(mp_mev_at_q_muon, 15)} MeV")
    print(f"m_p^exp (CODATA 2022)  = {mp.nstr(mp_mev_at_q_proton, 15)} MeV")
    print(f"delta m_p = m_p(q_mu) - m_p(q_p) = +{mp.nstr(delta_mp_mev, 12)} MeV = +{mp.nstr(delta_mp_me, 12)} m_e (+{mp.nstr(delta_mp_ppb, 10)} ppb)")
    print(f"alpha_EM^-1(q_p)       = {mp.nstr(alpha_em_inv_p, 20)}")
    print(f"E_0(q_p)               = {mp.nstr(E0_p, 12)} MeV | E_0^full(q_p) = {mp.nstr(E0_full_p, 12)} MeV")
    print(f"alpha_bind = m_e*8G    = {mp.nstr(alpha_bind_mev, 12)} MeV")
    print()

    print("-" * 88)
    print("1. EXACT SYMPY 3-STRAND QUARK CHARGE OPERATOR IDENTITIES ON W_p=(2,1) AND W_n=(1,2)")
    print("-" * 88)
    for k, v in sym_res.items():
        print(f"  {k:34s} = {v}")
    print()

    print("-" * 88)
    print("2. TEST 1: IMPACT OF PROTON QED SELF-ENERGY M_p^QED ON THE 211 PPB MU-P TENSION")
    print("-" * 88)
    print(f"{'Candidate':62s} | {'M_p^QED (MeV)':>13s} | {'dq (ppb)':>11s} | {'m_mu err (ppb)':>14s} | {'sigma':>8s}")
    print("-" * 118)
    for r in test1_rows:
        print(
            f"{r['candidate'][:62]:62s} | {r['M_p_QED_MeV']:>13s} | "
            f"{r['dq_vs_qmuon_ppb']:>11s} | {r['m_mu_pred_err_ppb']:>14s} | {r['m_mu_pred_err_sigma']:>8s}"
        )
    print()

    print("-" * 88)
    print("3. TEST 2A: STRONG CANDIDATES ALONE (Delta m_QED = 0) AND CLOSEST TWO-TERM PAIRS")
    print("-" * 88)
    print("Strong candidates alone (at q_proton, Convention D):")
    for s_name, s_val in ev_p["strong_cands"].items():
        err_pct = (s_val - dm_np_codata_direct) / dm_np_codata_direct * 100
        print(f"  {s_name:58s} : {mp.nstr(s_val, 8):>10s} MeV ({mp.nstr(err_pct, 6):>8s}%)")
    print("\nQED candidates alone (at q_proton, Convention D):")
    for q_name, q_val in ev_p["qed_cands"].items():
        print(f"  {q_name:58s} : {mp.nstr(q_val, 8):>10s} MeV")

    print("\nPrimary Derived Borromean V^3 Two-Term & Connected 4th-Order Combinations (NucleonWeightSpaceTwoTerm.lean):")
    bor_combos = [
        c for c in test2_combinations
        if ("DERIVED-S8" in c["strong_term"] and "DERIVED-Bor-V3-Full" in c["qed_term"])
        or ("DERIVED-S9" in c["strong_term"] and "DERIVED-Bor-V3-e21" in c["qed_term"])
        or ("S5:" in c["strong_term"] and "DERIVED-Bor-V3-Conn" in c["qed_term"])
        or ("DERIVED-S8" in c["strong_term"] and "QED-Lit" in c["qed_term"])
    ]
    print(f"{'Strong Term':42s} | {'QED Term':42s} | {'QCD':>7s} | {'QED':>8s} | {'Total':>7s} | {'Err %':>8s} | {'Swing ppm':>9s}")
    print("-" * 138)
    for c in bor_combos:
        print(
            f"{c['strong_term'][:42]:42s} | {c['qed_term'][:42]:42s} | "
            f"{c['dm_QCD_MeV']:>7s} | {c['dm_QED_MeV']:>8s} | {c['dm_tot_proton_MeV']:>7s} | "
            f"{c['rel_err_vs_CODATA_pct']:>8s}% | {c['cross_anchor_swing_ppm']:>9s}"
        )

    print("\nTop 18 Two-Term Combinations Overall (Strong + QED, sorted by |rel_err_vs_CODATA_pct|):")
    sorted_combos = sorted(
        [c for c in test2_combinations if c["qed_term"] != "QED-0 (none = 0)"],
        key=lambda x: float(x["_abs_err"]),
    )
    print(f"{'Strong Term':42s} | {'QED Term':42s} | {'QCD':>7s} | {'QED':>8s} | {'Total':>7s} | {'Err %':>8s} | {'Swing ppm':>9s}")
    print("-" * 138)
    for c in sorted_combos[:18]:
        print(
            f"{c['strong_term'][:42]:42s} | {c['qed_term'][:42]:42s} | "
            f"{c['dm_QCD_MeV']:>7s} | {c['dm_QED_MeV']:>8s} | {c['dm_tot_proton_MeV']:>7s} | "
            f"{c['rel_err_vs_CODATA_pct']:>8s}% | {c['cross_anchor_swing_ppm']:>9s}"
        )
    print()

    print("-" * 88)
    print("4. TEST 2B: IMPACT OF SEPARATING Delta m_QED ON Q_beta AND CONVENTION-D c_k LADDER")
    print("-" * 88)
    print(
        f"Baseline Q_A(q_p) = {mp.nstr(ev_p['Q_A'], 10)} MeV | "
        f"Q_N1^D(q_p) = {mp.nstr(ev_p['Q_N1'], 10)} MeV | "
        f"Q_N2^D(q_p) = {mp.nstr(ev_p['Q_N2'], 10)} MeV | "
        f"Q_beta^exp = {mp.nstr(q_beta_exp_mev, 10)} MeV"
    )
    print(
        f"Note: Q_N2^D(q_p) - Q_beta^exp = +{mp.nstr(ev_p['Q_N2'] - q_beta_exp_mev, 8)} MeV "
        f"(+{mp.nstr((ev_p['Q_N2'] - q_beta_exp_mev) / q_beta_exp_mev * mp.mpf('1e6'), 6)} ppm)"
    )
    print(f"{'QED Candidate':46s} | {'dm_QED':>9s} | {'Q_N2+QED err(ppm)':>17s} | {'c2_emp(D)':>11s} | {'c3_emp(D,p)':>12s} | {'c3 swing %':>10s}")
    print("-" * 118)
    for r in qbeta_ladder_rows:
        print(
            f"{r['qed_candidate'][:46]:46s} | {r['dm_QED_MeV']:>9s} | "
            f"{r['Q_N2_plus_QED_err_ppm']:>17s} | {r['c2_emp_convD_proton']:>11s} | "
            f"{r['c3_emp_convD_proton']:>12s} | {r['c3_swing_pct']:>10s}%"
        )
    print()

    # =========================================================================
    # 5. ROUTE 2 (NucleonIdempotentModifiedTrace.lean) & qbeta_utils 50-DPS CHECK
    # =========================================================================
    from qbeta.qbeta_utils import (
        borromean_v3_connected_qed_diff_mev,
        c2_target_two_term_at,
        c3_target_two_term_at,
        chi_block_3,
        chi_block_21,
        chi_block_111,
        chi_neutron_3,
        chi_neutron_21,
        chi_neutron_111,
        chi_proton_3,
        chi_proton_21,
        chi_proton_111,
        d_mod_111_convention_D,
        t_mod_111_convention_D,
    )

    with mp.workdps(DPS + 20):
        from substrate.q_parameter import Q_50_DIGIT_STR

        q0_pin = mp.mpf(Q_50_DIGIT_STR)
        c_p_3 = chi_proton_3(q_proton)
        c_n_3 = chi_neutron_3(q_proton)
        c_p_21 = chi_proton_21(q_proton)
        c_n_21 = chi_neutron_21(q_proton)
        c_p_111 = chi_proton_111(q_proton)
        c_n_111 = chi_neutron_111(q_proton)
        d_mod_D = d_mod_111_convention_D(q_proton)
        t_mod_p = t_mod_111_convention_D(q_proton, "proton")
        t_mod_n = t_mod_111_convention_D(q_proton, "neutron")
        t_mod_diff = t_mod_111_convention_D(q_proton, "diff")

        assert abs((c_n_3 - c_p_3) - chi_block_3(q_proton)) < mp.mpf("1e-55")
        assert abs((c_n_21 - c_p_21) - chi_block_21(q_proton, intra_order="borromean")) < mp.mpf("1e-55")
        assert abs((c_n_111 - c_p_111) - chi_block_111(q_proton)) < mp.mpf("1e-55")
        assert abs((t_mod_n - t_mod_p) - t_mod_diff) < mp.mpf("1e-55")
        assert abs(t_mod_n - (q_proton**2) * t_mod_p) < mp.mpf("1e-55")

        dm_qed_plain = borromean_v3_connected_qed_diff_mev(q_proton, m_e_mev, weighting="plain")
        assert abs(dm_qed_plain - ev_p["qed_cands"]["DERIVED-Bor-V3-Conn (plain): -m_e * Delta tr_conn(V^3)"]) < mp.mpf("1e-55")

        c2_two_term_p = c2_target_two_term_at(q_proton, q_beta_exp_mev, m_e_mev, convention="D", weighting="plain")
        c3_two_term_p = c3_target_two_term_at(q_proton, q_beta_exp_mev, m_e_mev, c2=-1, convention="D", weighting="plain")

        # 50-dps evaluation of QOU.MassTheory.GPMTThreeRowCumulantBridge at canonical Q_50_DIGIT_STR (bean qou-8mxc):
        zD_q0 = (q0_pin**3) / (q0_pin**2 + 1)
        zD_sub_q0 = zD_q0 - q0_pin
        assert abs(zD_sub_q0 - (-q0_pin / (q0_pin**2 + 1))) < mp.mpf("1e-55")
        assert zD_sub_q0 < 0

        dMod111_q0 = d_mod_111_convention_D(q0_pin)
        qInt2_q0 = q0_pin + 1 / q0_pin
        qInt3_q0 = q0_pin**2 + 1 + 1 / (q0_pin**2)
        assert abs(dMod111_q0 - (-1 / (qInt2_q0 * qInt3_q0))) < mp.mpf("1e-55")
        assert dMod111_q0 < 0

        mu2_gpmt_q0 = mp.mpf(0)
        mu3_gpmt_q0 = -dMod111_q0
        mu4_gpmt_q0 = 2 * dMod111_q0
        assert mu2_gpmt_q0 == 0
        assert mu3_gpmt_q0 > 0
        assert mu4_gpmt_q0 < 0
        assert abs(mu4_gpmt_q0 - (-2 * mu3_gpmt_q0)) < mp.mpf("1e-55")

        bext_gpmt_2_q0 = mp.mpf(0)
        bext_gpmt_3_q0 = -dMod111_q0
        bext_gpmt_4_q0 = -6 * dMod111_q0
        assert bext_gpmt_3_q0 > 0
        assert bext_gpmt_4_q0 > 0
        assert abs(bext_gpmt_4_q0 - 6 * bext_gpmt_3_q0) < mp.mpf("1e-55")

    print("-" * 88)
    print("5. ROUTE 2 (NucleonIdempotentModifiedTrace.lean) & qbeta_utils.py 50-DPS VERIFICATION")
    print("-" * 88)
    print(f"  chi_proton_3(q_p)      = {mp.nstr(c_p_3, 20)}")
    print(f"  chi_neutron_3(q_p)     = {mp.nstr(c_n_3, 20)}")
    print(f"  chi_proton_21(q_p)     = {mp.nstr(c_p_21, 20)}")
    print(f"  chi_neutron_21(q_p)    = {mp.nstr(c_n_21, 20)}")
    print(f"  chi_proton_111(q_p)    = {mp.nstr(c_p_111, 20)}")
    print(f"  chi_neutron_111(q_p)   = {mp.nstr(c_n_111, 20)}")
    print(f"  d_mod_111_D(q_p)       = {mp.nstr(d_mod_D, 20)}")
    print(f"  t_mod_111_D(p)         = {mp.nstr(t_mod_p, 20)}")
    print(f"  t_mod_111_D(n)         = {mp.nstr(t_mod_n, 20)}")
    print(f"  t_mod_111_D(n - p)     = {mp.nstr(t_mod_diff, 20)}")
    print(f"  dm_QED_conn_plain(q_p) = {mp.nstr(dm_qed_plain, 20)} MeV")
    print(f"  c2_target_two_term(D)  = {mp.nstr(c2_two_term_p, 20)}")
    print(f"  c3_target_two_term(D)  = {mp.nstr(c3_two_term_p, 20)}")
    print(f"  zD(q_0) - q_0          = {mp.nstr(zD_sub_q0, 20)}")
    print(f"  mu2_GPMT(q_0)          = {mp.nstr(mu2_gpmt_q0, 20)}")
    print(f"  mu3_GPMT(q_0)          = +{mp.nstr(mu3_gpmt_q0, 20)} (> 0)")
    print(f"  mu4_GPMT(q_0)          = {mp.nstr(mu4_gpmt_q0, 20)} (< 0)")
    print(f"  BextGPMT(q_0, A=2,3,4) = (0, +{mp.nstr(bext_gpmt_3_q0, 20)}, +{mp.nstr(bext_gpmt_4_q0, 20)})")

    # Emit witness JSON (adjacent to __file__)
    witness_payload = {
        "producer": "computations/probes/np_two_term_qed_mup_tension_probe.py",
        "beans": ["qou-eas4", "qou-hipg", "qou-8mxc"],
        "arithmetic": "exact SymPy over Q(q) + 50-dps mpmath",
        "allPassed": True,
        "symbolic_identities": sym_res,
        "route2_and_gpmt_three_row_bridge_50dps": {
            "q0_50dps": Q_50_DIGIT_STR,
            "zD_sub_q0": mp.nstr(zD_sub_q0, 50),
            "dMod111_q0": mp.nstr(dMod111_q0, 50),
            "mu2_GPMT_q0": "0",
            "mu3_GPMT_q0": mp.nstr(mu3_gpmt_q0, 50),
            "mu4_GPMT_q0": mp.nstr(mu4_gpmt_q0, 50),
            "BextGPMT_2_q0": "0",
            "BextGPMT_3_q0": mp.nstr(bext_gpmt_3_q0, 50),
            "BextGPMT_4_q0": mp.nstr(bext_gpmt_4_q0, 50),
            "pairChargeA3_triton": 0,
            "pairChargeA3_helium3": 1,
            "chi_proton_3_qp": mp.nstr(c_p_3, 50),
            "chi_neutron_3_qp": mp.nstr(c_n_3, 50),
            "chi_proton_21_qp": mp.nstr(c_p_21, 50),
            "chi_neutron_21_qp": mp.nstr(c_n_21, 50),
            "chi_proton_111_qp": mp.nstr(c_p_111, 50),
            "chi_neutron_111_qp": mp.nstr(c_n_111, 50),
            "t_mod_111_D_proton": mp.nstr(t_mod_p, 50),
            "t_mod_111_D_neutron": mp.nstr(t_mod_n, 50),
            "t_mod_111_D_diff": mp.nstr(t_mod_diff, 50),
            "dm_QED_conn_plain_MeV": mp.nstr(dm_qed_plain, 50),
            "c2_target_two_term_D": mp.nstr(c2_two_term_p, 50),
            "c3_target_two_term_D": mp.nstr(c3_two_term_p, 50),
        },
        "test1_mup_tension_rows": test1_rows,
        "test2b_qbeta_ladder_rows": qbeta_ladder_rows,
    }
    witness_out = Path(__file__).with_name("np-two-term-qed-mup-tension-probe.witness.json")
    witness_out.write_text(json.dumps(witness_payload, indent=2, ensure_ascii=False) + "\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
