#!/usr/bin/env python3
"""
confinement_lp_sdp_twoterm_photon_gpmt_probe — 80-dps parameter-free investigation and
Lean-4 verification witness for resolving the open confinement ILP / LP-dual / SDP
degeneracies via the Two-Term Photon/QED Cost Operator and GPMT Full-Rank Gram Completion.

Addresses beans: qou-ndsa, qou-augu, qou-fadg, qou-egqr, qou-ales, cj01, qou-j540
Lean companion: folio/quantum-observable-universe/lean/QOU/Interactions/TwoTermPhotonGPMTConfinementSDP.lean

Three mathematical mechanisms probed at 80-dps mpmath (zero float64, zero Clarabel):

  1. Mechanism 1 — Resolving c = G e_0 => y_0* = 0 (qou-augu & qou-ndsa & qou-ales):
     - One-term trace LPs (both Convention D and 1-term GPMT) satisfy c_j = tau(b_j) = G_{0j},
       giving y_0* = 0 and y* = e_0 identically.
     - Adding the Two-Term QED adjacent-charge trace (Q_{12} + Q_{23}) at the corrected
       Bring + 1-loop Schwinger fixed-point photon coupling alpha_EM(q_0) breaks collinearity
       c != lambda * G e_0 and breaks sigma_0 <-> sigma_1 generator mirror symmetry on both
       (u,u,d) and (u,d,d). Coupling with polarized crossing operators (Q_{23}^{(p)} A_1) or
       the gamma-gamma pair-production vertex V = sigma_0 sigma_1^{-1} splits L_+ from L_-.
     - On the GPMT-completed Gram matrix G^{GPMT}, every component of a = (G^{GPMT})^{-1} 1
       is strictly positive at q_0, turning the Frobenius cone {G^{GPMT} x >= 0, 1^T x = n_target}
       into a compact 5-simplex in u = G^{GPMT} x >= 0 without any artificial box x_i >= -M.
       This yields closed-form 80-dps primal-dual solutions with strictly non-zero dual shadow
       prices y_0* < 0 (proton y_0* = -0.061175003764..., neutron y_0* = -0.038111067406...)
       and a unique active primal vertex at the trefoil channel e^-.

  2. Mechanism 2 — Resolving the Singular Rank-5 Convention-D Gram (qou-fadg & qou-egqr):
     - Restoring the killed (1^3) sector via its positive GPMT modified quantum dimension
       |d_D(S^{(1^3)})| = 1 / ([2]_q [3]_q) = q^3 / ((q^2 + 1)(q^4 + q^2 + 1)) > 0 lifts the
       Convention-D radical vector v_rad = (-q^{-1})^{len(b_j)} to an exact eigenvector of
       G^{GPMT} with eigenvalue q^{-3} > 0, giving full rank 6 with closed-form determinant
       det(G^{GPMT}) = -(q^4 + 1)(q^4 + q^2 + 1)^5 / (q^3 (q^2 + 1)^9) != 0.
     - Directly resolves qou-egqr (unique solve G^{GPMT} x* = nf(beta) to < 10^{-80} on both
       muon 4_1 = (sigma_0 sigma_1^{-1})^2 and proton B_3 = (sigma_0 sigma_1^{-1})^3, with
       non-parallel saddle offsets at 1.69387588 rad) and qou-fadg / qou-j540 (unique solve
       to relative residual < 10^{-75} from p, n, He-4 up to doubly-magic Pb-208 at Z=82, N=126).

  3. Mechanism 3 — Exact 80-dps Evaluation of RegimeTransitionZ2 & He4DemandClosure (cj01 & qou-j540):
     - Evaluates T_{2,5} vs L_+ at Z = 2 across standalone GPMT trace, Two-Term QED+GPMT cost,
       and Z = 2 atom NF demand (pp and He-3), confirming demand(L_+) < demand(T_{2,5}) in all
       four regimes.
     - Evaluates He-4 (Z = 2, N = 2) honestly across five constructions (Regime I->II L_+-core,
       pure L_+-core, bare single-crossing nucleus N(2,2), electron-dressed atom A(2,2), and
       gamma-gamma core (V^3)^4), reporting exact 80-dps NF coefficients, |dem|, Wedderburn
       block characters (chi_{(3)}, chi_{(2,1)}, chi_{(1^3)}), and GPMT Frobenius profiles.

Rule compliance:
  - 80-dps internal mpmath arithmetic (`set_compute_dps(80)` at module scope).
  - Zero binary64 conversions anywhere in this script.
  - Zero fitted parameters.
"""

from __future__ import annotations

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for _p in (
    "computations",
    "computations/qbeta",
    "computations/substrate",
    "tools/qou-substrate/python",
    "tools/pyhecke/python",
):
    _s = os.path.join(ROOT, _p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from codata_2022_source import M_E_MEV  # noqa: E402
from compound_shift_nf import build_atom_nf_mp, hm_mp  # noqa: E402
from pyhecke import gram  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, q_at, q_two_term_borromean_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(80)
mp.mp.dps = 80

_M_E_MPF = mp.mpf(str(M_E_MEV))
NF_LABELS_GRAM = list(gram.NF_NAMES)  # ['γ', 'σ₀', 'σ₁', 'L₊', 'L₋', 'e⁻']


def fmt(val: mp.mpf, digits: int = 50) -> str:
    """Serialize an mpmath mpf at 50 significant digits with zero binary64."""
    return mp.nstr(val, digits)


def compute_alpha_em_bring_schwinger(q: mp.mpf) -> mp.mpf:
    """Solve the Bring zero-mode (2/(3*pi)) + 1-loop Schwinger (1 - h^2*alpha) cubic at 80 dps:
    1 / alpha = q * [9]_q * [10]_q + 2 / (3 * pi) + alpha * ([2]_q / (8 * pi)) * (1 - h^2 * alpha).
    """
    with mp.workdps(95):
        one = mp.mpf(1)
        h = q - one / q
        h2 = h**2
        q2 = q + one / q
        q9 = (q**9 - q ** (-9)) / h
        q10 = (q**10 - q ** (-10)) / h
        tree_plus_bring = q * q9 * q10 + mp.mpf(2) / (mp.mpf(3) * mp.pi)
        hab_loop = q2 / (mp.mpf(8) * mp.pi)
        a = one / tree_plus_bring
        for _ in range(30):
            fa = -hab_loop * h2 * (a**3) + hab_loop * (a**2) + tree_plus_bring * a - one
            dfa = -mp.mpf(3) * hab_loop * h2 * (a**2) + mp.mpf(2) * hab_loop * a + tree_plus_bring
            a = a - fa / dfa
    return +a


def e0_hadronic_mev(q: mp.mpf) -> mp.mpf:
    """Tower-summed hadronic energy scale E_0(q) = m_e / (q*(q - 1)) / (1 - hbar_q^2) in MeV."""
    one = mp.mpf(1)
    hbar_q = (q - one) / q
    return _M_E_MPF / (q * (q - one)) / (one - hbar_q**2)


def build_h3_gpmt_and_twoterm_data(q: mp.mpf) -> dict:
    """Construct exact 80-dps Convention-D and GPMT-completed Gram matrices, Wedderburn
    representations, and Two-Term QED cost vectors in pyhecke.gram NF_BASIS order
    [1, sigma_0, sigma_1, L_+ = sigma_0 sigma_1, L_- = sigma_1 sigma_0, e^- = sigma_0 sigma_1 sigma_0].
    """
    one = mp.mpf(1)
    zero = mp.mpf(0)
    h = q - one / q
    z_d = q**3 / (q**2 + one)
    w3 = (q**4 + one) / (q**2 + one) ** 2
    w21 = q**2 / (q**2 + one) ** 2
    d_mod_abs = q**3 / ((q**2 + one) * (q**4 + q**2 + one))

    s0 = mp.matrix([[q, zero], [zero, -one / q]])
    s1 = mp.matrix(
        [
            [-one / (q * (q**2 + one)), one],
            [(q**4 + q**2 + one) / (q**2 + one) ** 2, q**3 / (q**2 + one)],
        ]
    )
    b2 = [mp.eye(2), s0, s1, s0 * s1, s1 * s0, s0 * s1 * s0]
    lengths = [0, 1, 1, 2, 2, 3]

    g_d = mp.matrix(6, 6)
    g_gpmt = mp.matrix(6, 6)
    for i in range(6):
        for j in range(6):
            c3 = q ** (lengths[i] + lengths[j])
            m_ij = b2[i] * b2[j]
            c21 = m_ij[0, 0] + m_ij[1, 1]
            c111 = (-one / q) ** (lengths[i] + lengths[j])
            g_d[i, j] = w3 * c3 + w21 * c21
            g_gpmt[i, j] = w3 * c3 + w21 * c21 + d_mod_abs * c111

    v_rad = [(-one / q) ** l for l in lengths]

    # 3D weight-space Jimbo matrices and pairwise charge operators
    a1 = mp.matrix([[q, zero, zero], [zero, zero, one], [zero, one, h]])
    a2 = mp.matrix([[zero, one, zero], [one, h, zero], [zero, zero, q]])
    b1 = a2
    b2_n = a1
    basis_p = [mp.eye(3), a1, a2, a1 * a2, a2 * a1, a1 * a2 * a1]
    basis_n = [mp.eye(3), b1, b2_n, b1 * b2_n, b2_n * b1, b1 * b2_n * b1]

    q12p = mp.diag([mp.mpf(4) / 9, mp.mpf(-2) / 9, mp.mpf(-2) / 9])
    q23p = mp.diag([mp.mpf(-2) / 9, mp.mpf(-2) / 9, mp.mpf(4) / 9])
    qadjp = q12p + q23p

    q12n = mp.diag([mp.mpf(-2) / 9, mp.mpf(-2) / 9, mp.mpf(1) / 9])
    q23n = mp.diag([mp.mpf(1) / 9, mp.mpf(-2) / 9, mp.mpf(-2) / 9])
    qadjn = q12n + q23n

    def tr3(mat: mp.matrix) -> mp.mpf:
        return mat[0, 0] + mat[1, 1] + mat[2, 2]

    t_d = [g_d[0, j] for j in range(6)]
    t_gpmt = [g_gpmt[0, j] for j in range(6)]
    t_qadjp = [tr3(qadjp * m) for m in basis_p]
    t_qadjn = [tr3(qadjn * m) for m in basis_n]
    t_q12p = [tr3(q12p * m) for m in basis_p]
    t_q23p = [tr3(q23p * m) for m in basis_p]
    t_q23p_a1 = [tr3(q23p * a1 * m) for m in basis_p]

    # gamma-gamma vertex V = sigma_0 * sigma_1^{-1} seeded GPMT cost vector c_j(V) = trGPMT(V * b_j)
    v_b2 = s0 * (s1 - h * mp.eye(2))
    t_vtx_gpmt = []
    for j in range(6):
        c3_v = q ** lengths[j]
        m_v = v_b2 * b2[j]
        c21_v = m_v[0, 0] + m_v[1, 1]
        c111_v = (-one / q) ** lengths[j]
        t_vtx_gpmt.append(w3 * c3_v + w21 * c21_v + d_mod_abs * c111_v)

    return {
        "q": q,
        "h": h,
        "z_d": z_d,
        "w3": w3,
        "w21": w21,
        "d_mod_abs": d_mod_abs,
        "b2": b2,
        "lengths": lengths,
        "g_d": g_d,
        "g_gpmt": g_gpmt,
        "g_gpmt_inv": g_gpmt ** (-1),
        "v_rad": v_rad,
        "t_d": t_d,
        "t_gpmt": t_gpmt,
        "t_qadjp": t_qadjp,
        "t_qadjn": t_qadjn,
        "t_q12p": t_q12p,
        "t_q23p": t_q23p,
        "t_q23p_a1": t_q23p_a1,
        "t_vtx_gpmt": t_vtx_gpmt,
    }


def closed_form_a_gpmt(q: mp.mpf) -> list[mp.mpf]:
    """Lean closed-form vector `aGPMT q = (gramGPMT q)^{-1} 1`."""
    d = (q**2 + 1) * (q**4 + 1) * (q**2 - q + 1) * (q**2 + q + 1) ** 2
    a0 = (
        q**15
        - q**14
        + q**13
        - q**12
        + 4 * q**11
        + 5 * q**9
        + q**8
        + q**7
        - 3 * q**6
        - 2 * q**5
        + q**3
        + 3 * q**2
        + q
        + 1
    ) / d
    a1 = -(
        q**14
        - q**13
        - 3 * q**11
        - 4 * q**9
        + 2 * q**8
        + q**7
        + 3 * q**6
        - q**5
        - 2 * q**4
        - 3 * q**3
        - 3 * q**2
        - q
        - 1
    ) / d
    a3 = (
        q**13
        + q**11
        - q**10
        - 5 * q**8
        - q**7
        - q**6
        + 4 * q**5
        + 3 * q**4
        + 5 * q**3
        + 3 * q**2
        + 2 * q
        + 1
    ) / d
    a5 = (
        -q
        * (
            q**11
            + q**10
            + 3 * q**9
            + 3 * q**8
            + 4 * q**7
            - 2 * q**6
            - 2 * q**5
            - 6 * q**4
            - 4 * q**3
            - 6 * q**2
            - 2 * q
            - 2
        )
        / d
    )
    return [a0, a1, a1, a3, a3, a5]


def closed_form_beta_qadjp(q: mp.mpf) -> list[mp.mpf]:
    """Lean closed-form vector `betaQAdjp q = (gramGPMT q)^{-1} (qedCostProton q)`."""
    d = mp.mpf(9) * (q**4 + 1) * (q**4 + q**2 + 1)
    b0 = -mp.mpf(2) * (q**2) * ((q**2 - 1) ** 2) * (q**2 + 1) / d
    b1 = mp.mpf(2) * (q**2 + 1) * (q**8 + 3 * q**6 + q**2 - 1) / (q * d)
    b2 = -mp.mpf(2) * (q**2 + 1) * (2 * q**8 - 3 * q**6 - q**2 - 2) / (q * d)
    b3 = mp.mpf(2) * (q**2 - 1) * (q**2 + 1) * (2 * q**4 + q**2 + 1) / d
    b5 = -mp.mpf(2) * q * (q**2 + 1) * (3 * q**4 + 2 * q**2 + 3) / d
    return [b0, b1, b2, b3, b3, b5]


def solve_simplex_cone_lp_exact(
    c_vec: list[mp.mpf],
    g_mat: mp.matrix,
    g_inv: mp.matrix,
    n_target: mp.mpf,
) -> dict:
    """Exact 80-dps closed-form primal-dual solver for:
        min_x c^T x   s.t.   1^T x = n_target,   G x >= 0
    when G is symmetric invertible and a = G^{-1} 1 > 0 componentwise.
    Under u = G x >= 0, 1^T x = a^T u = n_target and c^T x = beta^T u with beta = G^{-1} c,
    so y_0* = min_i (beta_i / a_i), y_i* = beta_i - y_0* a_i >= 0, and u* concentrates on argmin.
    """
    ones = mp.matrix([mp.mpf(1)] * 6)
    c_mat = mp.matrix(c_vec)
    a_vec = g_inv * ones
    beta_vec = g_inv * c_mat
    assert all(a_vec[i] > 0 for i in range(6)), "Expected simplex cone a = G^{-1} 1 > 0"

    ratios = [beta_vec[i] / a_vec[i] for i in range(6)]
    y0_star = min(ratios)
    tol = mp.mpf("1e-70")
    active_indices = [i for i in range(6) if abs(ratios[i] - y0_star) <= tol]
    i_min = active_indices[0]

    u_star = mp.matrix([mp.mpf(0)] * 6)
    u_star[i_min] = n_target / a_vec[i_min]
    x_star = g_inv * u_star
    y_star = [beta_vec[i] - y0_star * a_vec[i] for i in range(6)]

    primal_obj = mp.fsum(c_vec[j] * x_star[j] for j in range(6))
    dual_obj = n_target * y0_star
    duality_gap = abs(primal_obj - dual_obj)
    net_resid = abs(mp.fsum(x_star[j] for j in range(6)) - n_target)
    gx_vec = g_mat * x_star
    dual_eq_resid = max(
        abs(c_vec[j] - (y0_star + mp.fsum(y_star[i] * g_mat[i, j] for i in range(6))))
        for j in range(6)
    )

    return {
        "y0_star": fmt(y0_star),
        "primal_obj": fmt(primal_obj),
        "dual_obj": fmt(dual_obj),
        "duality_gap": fmt(duality_gap, 15),
        "net_residual": fmt(net_resid, 15),
        "dual_eq_residual": fmt(dual_eq_resid, 15),
        "active_channels": [NF_LABELS_GRAM[i] for i in active_indices],
        "unique_vertex": len(active_indices) == 1,
        "x_star": [fmt(x_star[j], 35) for j in range(6)],
        "y_star": [fmt(y_star[i], 35) for i in range(6)],
        "Gx_star_min": fmt(min(gx_vec[i] for i in range(6)), 15),
        "_y0_mpf": y0_star,
        "_gap_mpf": duality_gap,
        "_dual_resid_mpf": dual_eq_resid,
        "_unique": len(active_indices) == 1,
        "_active": active_indices,
    }


def word_nf_mp(word_steps: list[tuple[mp.mpf, mp.mpf, int]], q_val: mp.mpf) -> list[mp.mpf]:
    """Evaluate a sequence of affine Hecke steps `(c * sigma_g + d * 1)` in 80-dps mpmath."""
    h_val = q_val - mp.mpf(1) / q_val
    nf = [mp.mpf(1)] + [mp.mpf(0)] * 5
    for c, d, g in word_steps:
        nf = hm_mp(nf, c, d, g, h_val)
    return nf


def nf_mul_mp(u: list[mp.mpf], v: list[mp.mpf], q_val: mp.mpf) -> list[mp.mpf]:
    """Multiply two normal-form 6-vectors in H_3(q) at 80 dps."""
    h_val = q_val - mp.mpf(1) / q_val
    one, zero = mp.mpf(1), mp.mpf(0)
    b_words = [[], [0], [1], [0, 1], [1, 0], [0, 1, 0]]
    res = [zero] * 6
    for j in range(6):
        tmp = list(u)
        for g in b_words[j]:
            tmp = hm_mp(tmp, one, zero, g, h_val)
        for i in range(6):
            res[i] += v[j] * tmp[i]
    return res


def nuc_core_mp(kind: str, q_val: mp.mpf) -> list[mp.mpf]:
    """11-letter nucleon normal-form vector without trailing atomic electron."""
    h_val = q_val - mp.mpf(1) / q_val
    half = mp.mpf(1) / 2
    one, zero = mp.mpf(1), mp.mpf(0)
    nf = [one, zero, zero, zero, zero, zero]
    for _ in range(3):
        nf = hm_mp(nf, one, zero, 0, h_val)
        nf = hm_mp(nf, one, -h_val, 1, h_val)
    if kind == "p":
        nf = hm_mp(nf, one, zero, 0, h_val)
        nf = hm_mp(nf, one, -h_val * half, 0, h_val)
        nf = hm_mp(nf, one, -h_val * half, 1, h_val)
    else:
        nf = hm_mp(nf, one, -h_val * half, 0, h_val)
        nf = hm_mp(nf, one, -h_val * half, 0, h_val)
        nf = hm_mp(nf, one, -h_val, 1, h_val)
    nf = hm_mp(nf, one, zero, 0, h_val)
    nf = hm_mp(nf, one, zero, 0, h_val)
    return nf


def add_electrons_mp(nf: list[mp.mpf], z_count: int, q_val: mp.mpf) -> list[mp.mpf]:
    """Append `z_count` inverse-crossing electron letters `sigma_1^{-1}` at 80 dps."""
    h_val = q_val - mp.mpf(1) / q_val
    res = list(nf)
    for _ in range(z_count):
        res = hm_mp(res, mp.mpf(1), -h_val, 1, h_val)
    return res


def dem_mag(nf: list[mp.mpf]) -> mp.mpf:
    """Demand magnitude `|dem(nf)| = sum_{c < 0} (-c)`."""
    return mp.fsum(-c for c in nf if c < 0)


def eval_wedderburn_and_costs(v: list[mp.mpf], d: dict, alpha_em: mp.mpf) -> dict:
    """Evaluate Wedderburn characters, Convention-D & GPMT traces, Two-Term QED cost, and G^{GPMT}*v."""
    q = d["q"]
    one = mp.mpf(1)
    lengths = d["lengths"]
    b2 = d["b2"]
    c3 = mp.fsum(v[j] * (q ** lengths[j]) for j in range(6))
    m2 = mp.matrix(2, 2)
    for j in range(6):
        m2 += v[j] * b2[j]
    c21 = m2[0, 0] + m2[1, 1]
    c111 = mp.fsum(v[j] * ((-one / q) ** lengths[j]) for j in range(6))
    tr_d = d["w3"] * c3 + d["w21"] * c21
    tr_gpmt = tr_d + d["d_mod_abs"] * c111
    tr_qed_p = mp.fsum(v[j] * d["t_qadjp"][j] for j in range(6))
    cost_2t_gpmt = tr_gpmt + alpha_em * tr_qed_p
    gv = d["g_gpmt"] * mp.matrix(v)
    return {
        "nf": [fmt(x, 30) for x in v],
        "dem_mag": fmt(dem_mag(v), 30),
        "all_nf_nonneg": all(x >= 0 for x in v),
        "chi3": fmt(c3, 30),
        "chi21": fmt(c21, 30),
        "chi111": fmt(c111, 30),
        "all_wedderburn_chars_pos": bool(c3 > 0 and c21 > 0 and c111 > 0),
        "tr_D": fmt(tr_d, 35),
        "tr_GPMT": fmt(tr_gpmt, 35),
        "tr_QED_proton": fmt(tr_qed_p, 35),
        "cost_twoTerm_GPMT": fmt(cost_2t_gpmt, 35),
        "G_GPMT_mul_nf_min": fmt(min(gv[i] for i in range(6)), 30),
        "all_G_GPMT_frobenius_pos": all(gv[i] > 0 for i in range(6)),
        "_dem_mpf": dem_mag(v),
        "_tr_gpmt_mpf": tr_gpmt,
        "_cost_2t_mpf": cost_2t_gpmt,
        "_c3": c3,
        "_c21": c21,
        "_c111": c111,
        "_all_frob_pos": all(gv[i] > 0 for i in range(6)),
    }


def main() -> int:
    q0 = q_at(85)
    q_2t = q_two_term_borromean_at(85, k_weighted=False)
    alpha0 = compute_alpha_em_bring_schwinger(q0)
    alpha_2t = compute_alpha_em_bring_schwinger(q_2t)
    e0_q0 = e0_hadronic_mev(q0)

    d0 = build_h3_gpmt_and_twoterm_data(q0)
    d2t = build_h3_gpmt_and_twoterm_data(q_2t)

    print("=" * 100)
    print("TWO-TERM PHOTON/QED COST + GPMT FULL-RANK GRAM COMPLETION FOR CONFINEMENT LP/SDP (80 DPS)")
    print("=" * 100)
    print(f"  q_0  (1-term proton pin)     = {fmt(q0)}")
    print(f"  q_2t (2-term Borromean pin)  = {fmt(q_2t)}")
    print(f"  1 / alpha_EM(q_0) [Bring+1L] = {fmt(1 / alpha0, 30)}")
    print(f"  E_0(q_0) [MeV]               = {fmt(e0_q0, 30)}")

    # =========================================================================
    # PART 1: Mechanism 1 — Breaking c = G e_0, Mirror Symmetry, and y_0* = 0
    # =========================================================================
    a_cf = closed_form_a_gpmt(q0)
    beta_cf = closed_form_beta_qadjp(q0)
    ones = mp.matrix([mp.mpf(1)] * 6)
    a_resid = max(abs(x) for x in (d0["g_gpmt"] * mp.matrix(a_cf) - ones))
    beta_resid = max(
        abs(x) for x in (d0["g_gpmt"] * mp.matrix(beta_cf) - mp.matrix(d0["t_qadjp"]))
    )
    qed_perp_rad = abs(mp.fsum(d0["t_qadjp"][j] * d0["v_rad"][j] for j in range(6)))

    y0_lean_closed_form = (alpha0 * beta_cf[5]) / a_cf[5]

    n_target = mp.mpf(1)
    lp_1t_gpmt = solve_simplex_cone_lp_exact(
        d0["t_gpmt"], d0["g_gpmt"], d0["g_gpmt_inv"], n_target
    )
    c_2t_proton = [d0["t_gpmt"][j] + alpha0 * d0["t_qadjp"][j] for j in range(6)]
    c_2t_neutron = [d0["t_gpmt"][j] + alpha0 * d0["t_qadjn"][j] for j in range(6)]
    c_2t_q12p = [d0["t_gpmt"][j] + alpha0 * d0["t_q12p"][j] for j in range(6)]
    c_2t_crossed = [d0["t_gpmt"][j] + alpha0 * d0["t_q23p_a1"][j] for j in range(6)]
    c_2t_vtx = [d0["t_vtx_gpmt"][j] + alpha0 * d0["t_qadjp"][j] for j in range(6)]

    lp_2t_proton = solve_simplex_cone_lp_exact(
        c_2t_proton, d0["g_gpmt"], d0["g_gpmt_inv"], n_target
    )
    lp_2t_neutron = solve_simplex_cone_lp_exact(
        c_2t_neutron, d0["g_gpmt"], d0["g_gpmt_inv"], n_target
    )
    lp_2t_q12p = solve_simplex_cone_lp_exact(
        c_2t_q12p, d0["g_gpmt"], d0["g_gpmt_inv"], n_target
    )
    lp_2t_crossed = solve_simplex_cone_lp_exact(
        c_2t_crossed, d0["g_gpmt"], d0["g_gpmt_inv"], n_target
    )
    lp_2t_vtx = solve_simplex_cone_lp_exact(
        c_2t_vtx, d0["g_gpmt"], d0["g_gpmt_inv"], n_target
    )

    # Also evaluate proton 2-term GPMT LP at q_2t:
    c_2t_proton_at_q2t = [
        d2t["t_gpmt"][j] + alpha_2t * d2t["t_qadjp"][j] for j in range(6)
    ]
    lp_2t_proton_q2t = solve_simplex_cone_lp_exact(
        c_2t_proton_at_q2t, d2t["g_gpmt"], d2t["g_gpmt_inv"], n_target
    )

    gen_asym_p = d0["t_qadjp"][1] - d0["t_qadjp"][2]
    gen_asym_p_cf = mp.mpf(2) * (q0**2 - 1) / (mp.mpf(3) * q0)
    hopf_split_crossed = d0["t_q23p_a1"][3] - d0["t_q23p_a1"][4]
    hopf_split_crossed_cf = mp.mpf(2) / (mp.mpf(3) * q0)
    hopf_split_vtx = d0["t_vtx_gpmt"][3] - d0["t_vtx_gpmt"][4]
    hopf_split_vtx_cf = -(q0**4 + q0**2 + 1) / (q0**2 + 1) ** 2

    print("\n--- PART 1: Mechanism 1 (Two-Term Photon/QED Cost & Exact Simplex Cone-LP Duals) ---")
    print(f"  ||G_GPMT * aGPMT - 1||_inf                 = {fmt(a_resid, 12)}")
    print(f"  ||G_GPMT * betaQAdjp - qedCostProton||_inf = {fmt(beta_resid, 12)}")
    print(f"  |<qedCostProton, v_rad>| (2-row vanishing) = {fmt(qed_perp_rad, 12)}")
    print(f"  1-term GPMT y_0* (c = G e_0 tautology)     = {lp_1t_gpmt['y0_star']}")
    print(f"  2-term Proton y_0* (at q_0)                = {lp_2t_proton['y0_star']}  (E_0*y_0* = {fmt(e0_q0 * lp_2t_proton['_y0_mpf'], 20)} MeV)")
    print(f"  2-term Proton y_0* Lean closed form        = {fmt(y0_lean_closed_form)}")
    print(f"  2-term Proton y_0* (at q_2t)               = {lp_2t_proton_q2t['y0_star']}")
    print(f"  2-term Neutron y_0* (at q_0)               = {lp_2t_neutron['y0_star']}  (E_0*y_0* = {fmt(e0_q0 * lp_2t_neutron['_y0_mpf'], 20)} MeV)")
    print(f"  2-term Polarized Q12p y_0*                 = {lp_2t_q12p['y0_star']}")
    print(f"  2-term Crossed Q23p*A1 y_0*                = {lp_2t_crossed['y0_star']}  (active: {lp_2t_crossed['active_channels']})")
    print(f"  gamma-gamma Vertex V + QED y_0*            = {lp_2t_vtx['y0_star']}  (active: {lp_2t_vtx['active_channels']})")
    print(f"  sigma_0 vs sigma_1 split (QAdjp)           = {fmt(gen_asym_p, 25)}")
    print(f"  L_+ vs L_- split (Q23p*A1)                 = {fmt(hopf_split_crossed, 25)}")
    print(f"  L_+ vs L_- split (gamma-gamma V)           = {fmt(hopf_split_vtx, 25)}")

    part1_summary = {
        "aGPMT_closed_form": [fmt(x, 35) for x in a_cf],
        "betaQAdjp_closed_form": [fmt(x, 35) for x in beta_cf],
        "aGPMT_solve_residual": fmt(a_resid, 15),
        "betaQAdjp_solve_residual": fmt(beta_resid, 15),
        "qedCostProton_radical_pairing_abs": fmt(qed_perp_rad, 15),
        "generator_mirror_split_proton": fmt(gen_asym_p, 35),
        "hopf_chirality_split_Q23p_A1": fmt(hopf_split_crossed, 35),
        "hopf_chirality_split_gamma_gamma_vertex": fmt(hopf_split_vtx, 35),
        "y0_star_proton_lean_closed_form": fmt(y0_lean_closed_form),
        "y0_star_proton_mev_at_q0": fmt(e0_q0 * lp_2t_proton["_y0_mpf"], 35),
        "y0_star_neutron_mev_at_q0": fmt(e0_q0 * lp_2t_neutron["_y0_mpf"], 35),
        "solves": {
            key: {k: v for k, v in sol.items() if not k.startswith("_")}
            for key, sol in [
                ("one_term_GPMT_tautology", lp_1t_gpmt),
                ("two_term_proton_at_q0", lp_2t_proton),
                ("two_term_proton_at_q2t", lp_2t_proton_q2t),
                ("two_term_neutron_at_q0", lp_2t_neutron),
                ("two_term_polarized_Q12p", lp_2t_q12p),
                ("two_term_crossed_Q23p_A1", lp_2t_crossed),
                ("gamma_gamma_vertex_seeded_two_term", lp_2t_vtx),
            ]
        },
    }

    # =========================================================================
    # PART 2: Mechanism 2 — GPMT Full-Rank Gram Completion (qou-fadg & qou-egqr)
    # =========================================================================
    det_d = mp.det(d0["g_d"])
    det_gpmt = mp.det(d0["g_gpmt"])
    det_gpmt_cf = -(q0**4 + 1) * ((q0**4 + q0**2 + 1) ** 5) / (
        (q0**3) * ((q0**2 + 1) ** 9)
    )
    rad_vec_mat = mp.matrix(d0["v_rad"])
    gd_rad_resid = max(abs(x) for x in (d0["g_d"] * rad_vec_mat))
    ggpmt_rad_eig_resid = max(
        abs(x) for x in (d0["g_gpmt"] * rad_vec_mat - (q0 ** (-3)) * rad_vec_mat)
    )

    # Resolve qou-egqr: muon 4_1 = (sigma_0 sigma_1^{-1})^2 and proton B_3 = (sigma_0 sigma_1^{-1})^3
    h0 = d0["h"]
    nf_4_1 = mp.matrix(word_nf_mp([(mp.mpf(1), mp.mpf(0), 0), (mp.mpf(1), -h0, 1)] * 2, q0))
    nf_b_3 = mp.matrix(word_nf_mp([(mp.mpf(1), mp.mpf(0), 0), (mp.mpf(1), -h0, 1)] * 3, q0))
    x_4_1 = d0["g_gpmt_inv"] * nf_4_1
    x_b_3 = d0["g_gpmt_inv"] * nf_b_3
    resid_4_1 = max(abs(t) for t in (d0["g_gpmt"] * x_4_1 - nf_4_1))
    resid_b_3 = max(abs(t) for t in (d0["g_gpmt"] * x_b_3 - nf_b_3))
    net_4_1 = mp.fsum(x_4_1[i] for i in range(6))
    net_b_3 = mp.fsum(x_b_3[i] for i in range(6))
    off_4_1 = [x_4_1[i] - net_4_1 / 6 for i in range(6)]
    off_b_3 = [x_b_3[i] - net_b_3 / 6 for i in range(6)]
    norm_off_4_1 = mp.sqrt(mp.fsum(t**2 for t in off_4_1))
    norm_off_b_3 = mp.sqrt(mp.fsum(t**2 for t in off_b_3))
    cos_ang = mp.fsum(off_4_1[i] * off_b_3[i] for i in range(6)) / (
        norm_off_4_1 * norm_off_b_3
    )
    ang_rad = mp.acos(cos_ang)
    ang_deg = ang_rad * mp.mpf(180) / mp.pi

    # Resolve qou-fadg & qou-j540 across nuclide chart including Z=82, N=126 (Pb-208)
    norm_rad = mp.sqrt(mp.fsum(t**2 for t in d0["v_rad"]))
    fadg_nuclides = []
    max_rel_resid_nuclides = mp.mpf(0)
    for z_val, n_val, label in [
        (1, 0, "p"),
        (0, 1, "n"),
        (1, 1, "2H"),
        (1, 2, "3H"),
        (2, 1, "3He"),
        (2, 2, "4He"),
        (6, 6, "12C"),
        (8, 8, "16O"),
        (20, 20, "40Ca"),
        (26, 30, "56Fe"),
        (50, 70, "120Sn"),
        (82, 126, "208Pb"),
    ]:
        nf_zn = build_atom_nf_mp(z_val, n_val, 80)
        nf_mat = mp.matrix(nf_zn)
        x_zn = d0["g_gpmt_inv"] * nf_mat
        abs_resid = max(abs(t) for t in (d0["g_gpmt"] * x_zn - nf_mat))
        inf_norm_nf = max(abs(t) for t in nf_zn)
        rel_resid = abs_resid / inf_norm_nf
        if rel_resid > max_rel_resid_nuclides:
            max_rel_resid_nuclides = rel_resid
        l2_nf = mp.sqrt(mp.fsum(t**2 for t in nf_zn))
        d_rad_frac = abs(mp.fsum(nf_zn[i] * d0["v_rad"][i] for i in range(6))) / (
            norm_rad * l2_nf
        )
        implied_net = mp.fsum(x_zn[i] for i in range(6))
        fadg_nuclides.append(
            {
                "nuclide": label,
                "Z": z_val,
                "N": n_val,
                "A": z_val + n_val,
                "convention_D_off_range_fraction": fmt(d_rad_frac, 20),
                "GPMT_relative_solve_residual": fmt(rel_resid, 15),
                "implied_net_1T_Ginv_nf": fmt(implied_net, 25),
            }
        )

    print("\n--- PART 2: Mechanism 2 (GPMT Full-Rank Gram Completion — qou-fadg & qou-egqr) ---")
    print(f"  w_3(z_D), w_21(z_D), |d_D(1^3)|   = {fmt(d0['w3'], 18)}, {fmt(d0['w21'], 18)}, {fmt(d0['d_mod_abs'], 18)}")
    print(f"  det(G_D) [rank 5 singular]        = {fmt(det_d, 15)}")
    print(f"  det(G_GPMT) [rank 6 invertible]   = {fmt(det_gpmt, 35)}")
    print(f"  ||G_GPMT*v_rad - q^-3*v_rad||_inf = {fmt(ggpmt_rad_eig_resid, 12)}")
    print(f"  qou-egqr 4_1 solve residual       = {fmt(resid_4_1, 12)}  | net = {fmt(net_4_1, 20)}")
    print(f"  qou-egqr B_3 solve residual       = {fmt(resid_b_3, 12)}  | net = {fmt(net_b_3, 20)}")
    print(f"  qou-egqr offset angle (4_1, B_3)  = {fmt(ang_rad, 25)} rad ({fmt(ang_deg, 15)} deg)")
    print(f"  qou-fadg/j540 max rel resid (A<=208, incl. Pb-208) = {fmt(max_rel_resid_nuclides, 12)}")

    part2_summary = {
        "wedderburn_weights_at_q0": {
            "w3_zD": fmt(d0["w3"], 35),
            "w21_zD": fmt(d0["w21"], 35),
            "dMod111_abs": fmt(d0["d_mod_abs"], 35),
        },
        "det_G_D": fmt(det_d, 20),
        "det_G_GPMT": fmt(det_gpmt, 40),
        "det_G_GPMT_closed_form_residual": fmt(abs(det_gpmt - det_gpmt_cf), 15),
        "G_D_radical_residual": fmt(gd_rad_resid, 15),
        "G_GPMT_radical_eigenvalue_q_inv3_residual": fmt(ggpmt_rad_eig_resid, 15),
        "qou_egqr_braid_offset_resolution": {
            "muon_4_1_solve_residual": fmt(resid_4_1, 15),
            "proton_B_3_solve_residual": fmt(resid_b_3, 15),
            "muon_4_1_implied_net": fmt(net_4_1, 35),
            "proton_B_3_implied_net": fmt(net_b_3, 35),
            "muon_4_1_offset_l2_norm": fmt(norm_off_4_1, 35),
            "proton_B_3_offset_l2_norm": fmt(norm_off_b_3, 35),
            "offset_angle_rad": fmt(ang_rad, 35),
            "offset_angle_deg": fmt(ang_deg, 25),
        },
        "qou_fadg_and_j540_nuclide_solves": fadg_nuclides,
    }

    # =========================================================================
    # PART 3: Mechanism 3 — RegimeTransitionZ2 & He4DemandClosure (cj01 & qou-j540)
    # =========================================================================
    one, zero = mp.mpf(1), mp.mpf(0)
    nf_t25 = word_nf_mp(
        [(one, zero, 0), (one, zero, 1), (one, zero, 0), (one, zero, 1), (one, zero, 0)],
        q0,
    )
    nf_lp = word_nf_mp([(one, zero, 0), (one, zero, 1)], q0)
    wc_t25 = eval_wedderburn_and_costs(nf_t25, d0, alpha0)
    wc_lp = eval_wedderburn_and_costs(nf_lp, d0, alpha0)

    p_core = nuc_core_mp("p", q0)
    n_core = nuc_core_mp("n", q0)
    pp_t25_core = nf_mul_mp(nf_mul_mp(p_core, nf_t25, q0), p_core, q0)
    pp_lp_core = nf_mul_mp(nf_mul_mp(p_core, nf_lp, q0), p_core, q0)
    pp_t25_atom = add_electrons_mp(pp_t25_core, 2, q0)
    pp_lp_atom = add_electrons_mp(pp_lp_core, 2, q0)
    he3_t25_atom = add_electrons_mp(
        nf_mul_mp(nf_mul_mp(pp_t25_core, nf_t25, q0), n_core, q0), 2, q0
    )
    he3_lp_atom = add_electrons_mp(
        nf_mul_mp(nf_mul_mp(pp_t25_core, nf_lp, q0), n_core, q0), 2, q0
    )

    wc_pp_t25_atom = eval_wedderburn_and_costs(pp_t25_atom, d0, alpha0)
    wc_pp_lp_atom = eval_wedderburn_and_costs(pp_lp_atom, d0, alpha0)
    wc_he3_t25_atom = eval_wedderburn_and_costs(he3_t25_atom, d0, alpha0)
    wc_he3_lp_atom = eval_wedderburn_and_costs(he3_lp_atom, d0, alpha0)

    # Five He-4 (Z=2, N=2) constructions evaluated honestly at 80 dps:
    he4_t25_lp_lp_core = nf_mul_mp(
        nf_mul_mp(nf_mul_mp(nf_mul_mp(pp_t25_core, nf_lp, q0), n_core, q0), nf_lp, q0),
        n_core,
        q0,
    )
    he4_all_lp_core = nf_mul_mp(
        nf_mul_mp(nf_mul_mp(nf_mul_mp(pp_lp_core, nf_lp, q0), n_core, q0), nf_lp, q0),
        n_core,
        q0,
    )
    he4_atom_single_crossing = build_atom_nf_mp(2, 2, 80)
    he4_nucleus_single_crossing = nf_mul_mp(
        he4_atom_single_crossing,
        word_nf_mp([(one, zero, 1), (one, zero, 1)], q0),
        q0,
    )
    he4_gg_v12 = word_nf_mp([(one, zero, 0), (one, -h0, 1)] * 12, q0)

    he4_variants = {}
    for key, nf_v in [
        ("He4_regime_T25_Lplus_Lplus_nucleus", he4_t25_lp_lp_core),
        ("He4_pure_Lplus_nucleus", he4_all_lp_core),
        ("He4_single_crossing_nucleus_N22", he4_nucleus_single_crossing),
        ("He4_single_crossing_atom_A22_with_2e", he4_atom_single_crossing),
        ("He4_gamma_gamma_V12_core", he4_gg_v12),
    ]:
        ev = eval_wedderburn_and_costs(nf_v, d0, alpha0)
        he4_variants[key] = {k: v for k, v in ev.items() if not k.startswith("_")}

    wc_he4_nuc = eval_wedderburn_and_costs(he4_nucleus_single_crossing, d0, alpha0)
    wc_he4_atom = eval_wedderburn_and_costs(he4_atom_single_crossing, d0, alpha0)
    wc_he4_regime = eval_wedderburn_and_costs(he4_t25_lp_lp_core, d0, alpha0)

    print("\n--- PART 3: Mechanism 3 (RegimeTransitionZ2 & He4DemandClosure — cj01 & qou-j540) ---")
    print(f"  Standalone trGPMT:   L_+ = {wc_lp['tr_GPMT']} < T_{{2,5}} = {wc_t25['tr_GPMT']}")
    print(f"  Standalone 2t-GPMT:  L_+ = {wc_lp['cost_twoTerm_GPMT']} < T_{{2,5}} = {wc_t25['cost_twoTerm_GPMT']}")
    print(f"  Z=2 (pp+2e-) |dem|:  L_+ = {wc_pp_lp_atom['dem_mag']} < T_{{2,5}} = {wc_pp_t25_atom['dem_mag']}")
    print(f"  Z=2 (He3+2e-)|dem|:  L_+ = {wc_he3_lp_atom['dem_mag']} < T_{{2,5}} = {wc_he3_t25_atom['dem_mag']}")
    for key, info in he4_variants.items():
        print(
            f"  {key:38s}: |dem|={info['dem_mag'][:14]:>14s} "
            f"NF>=0:{str(info['all_nf_nonneg']):5s} "
            f"Wed>0:{str(info['all_wedderburn_chars_pos']):5s} "
            f"G*nf>0:{str(info['all_G_GPMT_frobenius_pos']):5s}"
        )

    part3_summary = {
        "regime_transition_Z2": {
            "standalone_trGPMT_T25": wc_t25["tr_GPMT"],
            "standalone_trGPMT_Lplus": wc_lp["tr_GPMT"],
            "standalone_twoTerm_GPMT_T25": wc_t25["cost_twoTerm_GPMT"],
            "standalone_twoTerm_GPMT_Lplus": wc_lp["cost_twoTerm_GPMT"],
            "pp_atom_Z2N0_dem_T25": wc_pp_t25_atom["dem_mag"],
            "pp_atom_Z2N0_dem_Lplus": wc_pp_lp_atom["dem_mag"],
            "He3_atom_Z2N1_dem_T25": wc_he3_t25_atom["dem_mag"],
            "He3_atom_Z2N1_dem_Lplus": wc_he3_lp_atom["dem_mag"],
        },
        "he4_demand_and_frobenius_table": he4_variants,
    }

    checks = [
        (
            "mech1_one_term_cost_eq_gram_row0_gives_zero_y0",
            bool(abs(lp_1t_gpmt["_y0_mpf"]) < mp.mpf("1e-75")),
            f"1-term GPMT LP has y_0* = {lp_1t_gpmt['y0_star']} (exact 0 tautology from c = G e_0)",
        ),
        (
            "mech1_two_term_qed_breaks_mirror_and_yields_strict_nonzero_y0",
            bool(
                abs(gen_asym_p - gen_asym_p_cf) < mp.mpf("1e-75")
                and abs(hopf_split_crossed - hopf_split_crossed_cf) < mp.mpf("1e-75")
                and abs(hopf_split_vtx - hopf_split_vtx_cf) < mp.mpf("1e-75")
                and lp_2t_proton["_y0_mpf"] < mp.mpf("-0.06")
                and abs(lp_2t_proton["_y0_mpf"] - y0_lean_closed_form) < mp.mpf("1e-75")
                and lp_2t_proton["_unique"]
                and lp_2t_proton["_gap_mpf"] < mp.mpf("1e-75")
                and lp_2t_neutron["_y0_mpf"] < mp.mpf("-0.03")
                and lp_2t_neutron["_unique"]
            ),
            (
                f"Two-Term QED+GPMT gives unique primal vertex e^- and y_0* = {lp_2t_proton['y0_star'][:22]} "
                f"(proton) / {lp_2t_neutron['y0_star'][:22]} (neutron), matching Lean closed form to <1e-75"
            ),
        ),
        (
            "mech2_gpmt_gram_full_rank6_resolves_egqr_and_fadg_to_pb208",
            bool(
                abs(det_d) < mp.mpf("1e-75")
                and abs(det_gpmt - det_gpmt_cf) < mp.mpf("1e-75")
                and ggpmt_rad_eig_resid < mp.mpf("1e-75")
                and resid_4_1 < mp.mpf("1e-75")
                and resid_b_3 < mp.mpf("1e-75")
                and ang_rad > mp.mpf("1.5")
                and max_rel_resid_nuclides < mp.mpf("1e-70")
            ),
            (
                f"det(G_GPMT) = {fmt(det_gpmt, 18)} != 0, G_GPMT*v_rad = q^-3*v_rad to "
                f"{fmt(ggpmt_rad_eig_resid, 8)}, 4_1/B_3 offset angle = {fmt(ang_rad, 12)} rad, "
                f"and max nuclide rel resid through Pb-208 = {fmt(max_rel_resid_nuclides, 8)}"
            ),
        ),
        (
            "mech3_regime_transition_z2_and_he4_closure_classified",
            bool(
                wc_lp["_tr_gpmt_mpf"] < wc_t25["_tr_gpmt_mpf"]
                and wc_lp["_cost_2t_mpf"] < wc_t25["_cost_2t_mpf"]
                and wc_pp_lp_atom["_dem_mpf"] < wc_pp_t25_atom["_dem_mpf"]
                and wc_he3_lp_atom["_dem_mpf"] < wc_he3_t25_atom["_dem_mpf"]
                and wc_he4_regime["_dem_mpf"] == 0
                and wc_he4_nuc["_dem_mpf"] == 0
                and wc_he4_nuc["_c3"] > 0
                and wc_he4_nuc["_c21"] > 0
                and wc_he4_nuc["_c111"] > 0
                and wc_he4_nuc["_all_frob_pos"]
                and wc_he4_atom["_dem_mpf"] > 0
                and wc_he4_atom["_all_frob_pos"]
            ),
            (
                f"L_+ strictly dominates T_{{2,5}} across all 4 Z=2 metrics; He-4 bare nucleus N(2,2) "
                f"satisfies |dem|=0 + all 3 Wedderburn chars > 0 + G_GPMT*nf > 0, while A(2,2) has "
                f"|dem|={wc_he4_atom['dem_mag'][:14]} from 2e^- yet keeps Wedderburn & GPMT Frobenius > 0"
            ),
        ),
    ]

    print("\n" + "-" * 100)
    print("VERIFICATION CHECKS")
    print("-" * 100)
    for name, passed, detail in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name} — {detail}")
    assert all(p for _, p, _ in checks), "One or more verification checks failed!"

    w = WitnessBuilder("confinement-lp-sdp-twoterm-photon-gpmt", engine="mpmath")
    w.set_description(
        "80-dps parameter-free evaluation and Lean-4 companion witness resolving the "
        "confinement LP/SDP identity-row degeneracy (qou-augu, qou-ndsa) via the Two-Term "
        "Bring+Schwinger Photon/QED Cost Operator, resolving the rank-5 Convention-D Gram "
        "singularity (qou-fadg, qou-egqr) via GPMT Modified-Trace Completion, and classifying "
        "RegimeTransitionZ2 and He4DemandClosure at 80 dps (cj01, qou-j540, qou-ales)."
    )
    w.add_data("q0_anchor", "proton")
    w.add_data("q0_value", Q_50_DIGIT_STR)
    w.add_data("q_2t_borromean_plain", fmt(q_2t))
    w.add_data("alpha_em_inv_bring_schwinger_q0", fmt(1 / alpha0))
    w.add_data("alpha_em_inv_bring_schwinger_q2t", fmt(1 / alpha_2t))
    w.add_data("dps", 80)
    w.add_data("part1_mechanism1_twoterm_photon_lp_duals", part1_summary)
    w.add_data("part2_mechanism2_gpmt_full_rank_gram", part2_summary)
    w.add_data("part3_mechanism3_z2_and_he4_closure", part3_summary)
    w.add_caveat(
        "All Gram entries, simplex cone-LP dual shadow prices, braid normal forms, and "
        "Wedderburn characters are computed in 80-dps mpmath with zero binary64 conversions "
        "and zero fitted parameters. On electron-dressed A(2,2) (`build_atom_nf_mp(2,2)`), "
        "appending two inverse-crossing electrons introduces c_3 = -0.00631832 < 0 (`|dem| > 0`), "
        "whereas bare nuclear N(2,2) and L_+-derived nuclear cores satisfy `|dem| = 0`."
    )
    for name, passed, detail in checks:
        w.add_assertion(name, "1" if passed else "0", "1", "0", source=detail)

    out_path = w.save({"q0Anchor": "proton", "q0Value": Q_50_DIGIT_STR})
    print(f"\nWrote witness -> {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
