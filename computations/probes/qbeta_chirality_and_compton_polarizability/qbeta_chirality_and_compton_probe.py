#!/usr/bin/env python3
"""EXPLORATORY shape-probe (pre-registered 80-dps verification, bean qou-gtv6):
Q_beta left-coupled crossing chirality selection (C2_neg vs C1_pos), signed logarithmic
action readout (F3C/F3B vs linear F2), and k >= 1 Ppos Cottingham-Compton transient jet /
magnetic spin-spin channels in QOU's two-term action.

Pre-registration: PREREGISTRATION.md (committed in 5be409c2671 prior to evaluation).
Lean companion: QOU/QBeta/ChargedCurrentChiralitySelection.lean.

Zero fitting, zero float64; proton pin q_0 = q_at(80).
"""
from __future__ import annotations

import itertools
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
from codata_constants import (  # noqa: E402
    M_N_MEV_VALIDATION,
    M_P_MEV_VALIDATION,
    M_PI_PM_MEV_VALIDATION,
    Q_BETA_MEV,
)
from mpmath import mp, mpf  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import (  # noqa: E402
    M_E_MEV_STR,
    Q_MP,
    q_at,
    q_int_at,
    vol_4_1_at,
)
from qou_substrate.witness import WitnessBuilder  # noqa: E402

LPoly = dict[int, Fraction]


def lp_add(a: LPoly, b: LPoly) -> LPoly:
    out = dict(a)
    for k, v in b.items():
        nv = out.get(k, Fraction(0)) + v
        if nv == 0:
            out.pop(k, None)
        else:
            out[k] = nv
    return out


def lp_mul(a: LPoly, b: LPoly) -> LPoly:
    out: LPoly = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = ka + kb
            nv = out.get(k, Fraction(0)) + va * vb
            if nv == 0:
                out.pop(k, None)
            else:
                out[k] = nv
    return out


LP_ONE: LPoly = {0: Fraction(1)}
LP_Q: LPoly = {1: Fraction(1)}
LP_QI: LPoly = {-1: Fraction(1)}
LP_H: LPoly = {1: Fraction(1), -1: Fraction(-1)}
LP_MH: LPoly = {-1: Fraction(1), 1: Fraction(-1)}

R_LP_POS = {
    (0, 0): [((0, 0), LP_Q)],
    (0, 1): [((1, 0), LP_ONE)],
    (1, 0): [((0, 1), LP_ONE), ((1, 0), LP_H)],
    (1, 1): [((1, 1), LP_Q)],
}
R_LP_NEG = {
    (0, 0): [((0, 0), LP_QI)],
    (0, 1): [((0, 1), LP_MH), ((1, 0), LP_ONE)],
    (1, 0): [((0, 1), LP_ONE)],
    (1, 1): [((1, 1), LP_QI)],
}


def apply_word_lp(
    letters: list[tuple[int, int]], st0: tuple[int, ...]
) -> dict[tuple[int, ...], LPoly]:
    cur: dict[tuple[int, ...], LPoly] = {st0: LP_ONE}
    for idx, sgn in reversed(letters):
        rop = R_LP_POS if sgn > 0 else R_LP_NEG
        nxt: dict[tuple[int, ...], LPoly] = {}
        for st, coeff in cur.items():
            for (a, b), rc in rop[(st[idx], st[idx + 1])]:
                nst = st[:idx] + (a, b) + st[idx + 2 :]
                prod = lp_mul(coeff, rc)
                if prod:
                    prev = nxt.get(nst)
                    comb = lp_add(prev, prod) if prev is not None else prod
                    if comb:
                        nxt[nst] = comb
                    else:
                        nxt.pop(nst, None)
        cur = nxt
    return cur


def lp_to_sympy(p: LPoly, q_sym: sp.Symbol) -> sp.Expr:
    return sum(
        sp.Rational(v.numerator, v.denominator) * (q_sym ** k) for k, v in p.items()
    )


def full_nine_strand_trace_lp(
    letters9: list[tuple[int, int]], nuc_states: list[tuple[int, int, int]]
) -> LPoly:
    """Direct 9-strand Tr_{C^{2x6} x W_nuc}(K^{x9} W_9) in Q[q, q^-1]."""
    tot: LPoly = {}
    for b6 in itertools.product((0, 1), repeat=6):
        for u3 in nuc_states:
            st = b6 + u3
            out = apply_word_lp(letters9, st)
            diag = out.get(st)
            if diag:
                k_exp = 9 - 2 * sum(st)
                tot = lp_add(tot, lp_mul({k_exp: Fraction(1)}, diag))
    return tot


def V_let(i: int) -> list[tuple[int, int]]:
    return [(i, 1), (i + 1, -1)]


def fmt50(x: mpf) -> str:
    return mp.nstr(x, 50, strip_zeros=False)


def eval_sym_at(expr: sp.Expr, q_sym: sp.Symbol, q_val: mpf) -> mpf:
    num, den = sp.fraction(sp.together(expr))
    p_num = sp.Poly(num, q_sym)
    p_den = sp.Poly(den, q_sym)

    def eval_poly(poly: sp.Poly) -> mpf:
        acc = mpf(0)
        for (deg,), coeff in poly.terms():
            r = sp.Rational(coeff)
            c_mp = mpf(int(r.p)) / mpf(int(r.q))
            acc += c_mp * (q_val ** int(deg))
        return acc

    return eval_poly(p_num) / eval_poly(p_den)


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


def su6_breit_fermi_expectation() -> tuple[sp.Rational, sp.Rational]:
    """Exact 8-dim spin x 3-dim flavour matrix expectation of -sum_{i<j} q_i q_j (sigma_i . sigma_j)
    on the symmetric 56-plet SU(6) proton (uud, S=1/2, S_z=+1/2) and neutron (udd, S=1/2, S_z=+1/2).
    """
    # Standard SU(6) |p, up>: (1/sqrt(18)) * [2|u+ u+ d-> - |u+ u- d+> - |u- u+ d+> + cyclic perms]
    p_flavour_terms = [
        ((0, 0, 1), (0, 0, 1), sp.Integer(2)),
        ((0, 0, 1), (0, 1, 0), sp.Integer(-1)),
        ((0, 0, 1), (1, 0, 0), sp.Integer(-1)),
        ((0, 1, 0), (0, 1, 0), sp.Integer(2)),
        ((0, 1, 0), (0, 0, 1), sp.Integer(-1)),
        ((0, 1, 0), (1, 0, 0), sp.Integer(-1)),
        ((1, 0, 0), (1, 0, 0), sp.Integer(2)),
        ((1, 0, 0), (0, 0, 1), sp.Integer(-1)),
        ((1, 0, 0), (0, 1, 0), sp.Integer(-1)),
    ]
    # Neutron |n, up> obtained by u <-> d (0 <-> 1 in flavour, with overall sign convention irrelevant for norm)
    n_flavour_terms = [
        ((1 - f[0], 1 - f[1], 1 - f[2]), s, c) for (f, s, c) in p_flavour_terms
    ]
    q_map = {0: sp.Rational(2, 3), 1: sp.Rational(-1, 3)}

    def eval_state(terms: list[tuple[tuple[int, int, int], tuple[int, int, int], sp.Integer]]) -> sp.Rational:
        state: dict[tuple[tuple[int, int, int], tuple[int, int, int]], sp.Rational] = {}
        for f, s, c in terms:
            state[(f, s)] = state.get((f, s), sp.Rational(0)) + sp.Rational(c)
        norm_sq = sum(v * v for v in state.values())
        assert norm_sq == 18

        # Apply -sum_{i<j} q_i q_j (sigma_i . sigma_j)
        # sigma_i . sigma_j = sigma_z^i sigma_z^j + 2 (sigma_+^i sigma_-^j + sigma_-^i sigma_+^j)
        exp_num = sp.Rational(0)
        for (f, s), amp in state.items():
            for i, j in ((0, 1), (0, 2), (1, 2)):
                qq = q_map[f[i]] * q_map[f[j]]
                # diagonal sigma_z^i sigma_z^j: s_k = 0 -> +1, s_k = 1 -> -1
                sz_i = 1 if s[i] == 0 else -1
                sz_j = 1 if s[j] == 0 else -1
                exp_num += amp * amp * (-qq * sp.Integer(sz_i * sz_j))
                # spin-flip 2 (|01><10| + |10><01|)
                if s[i] != s[j]:
                    s_flip = list(s)
                    s_flip[i], s_flip[j] = s_flip[j], s_flip[i]
                    amp_flip = state.get((f, tuple(s_flip)), sp.Rational(0))
                    exp_num += amp * amp_flip * (-qq * sp.Integer(2))
        return sp.Rational(exp_num, norm_sq)

    return eval_state(p_flavour_terms), eval_state(n_flavour_terms)


def main() -> int:
    with mp.workdps(80):
        q0 = q_at(80)
        qi0 = mpf(1) / q0
        h0 = q0 - qi0
        me_mev = mpf(M_E_MEV_STR)
        mpi_mev = +M_PI_PM_MEV_VALIDATION
        mp_derived = derived_mp_mev(q0, me_mev, dps=80)
        alpha_q0 = alpha_form_b_at(q0, dps=80)

        # Comparison-only empirical constants
        qbeta_codata_mev = +Q_BETA_MEV
        dm_np_codata_mev = (+M_N_MEV_VALIDATION) - (+M_P_MEV_VALIDATION)
        mu_p_codata = codata("proton mag. mom. to nuclear magneton ratio").value
        mu_n_codata = codata("neutron mag. mom. to nuclear magneton ratio").value

        wb = WitnessBuilder(
            "qbeta-chirality-and-compton",
            engine="mpmath (80 dps) + sympy Q(q)",
            output_dir=HERE,
        )
        wb.set_description(
            "Pre-registered 80-dps evaluation of ChargedCurrentW left-coupled crossing chirality "
            "selection (C2_neg vs C1_pos), signed logarithmic vs linear 9-strand Q_beta readouts, "
            "and k >= 1 Ppos transient jet + magnetic spin-spin channels in QOU's two-term action "
            "(qou-gtv6 / L2 Gate 1)."
        )
        wb.add_parameter("workdps", 80)
        wb.add_parameter("q0_proton_50dps", fmt50(q0))
        wb.add_parameter("alpha_FormB_inv_q0", fmt50(mpf(1) / alpha_q0))
        wb.add_parameter("preregistration_commit", "5be409c2671")

        wb.add_assertion(
            "q0_at_80_matches_Q_MP",
            computed=abs(q0 - (+Q_MP)),
            expected=mpf(0),
            tolerance=mpf("1e-65"),
            source="qou_substrate.constants",
        )

        # ==================================================================
        # Part A1: Algebraic Chirality Selection on Left-Lepton x Right-Quark
        # ==================================================================
        q = sp.Symbol("q", positive=True)
        qi = 1 / q
        h = q - qi
        d2 = q + qi
        e0_full = 1 / (q * (q - 1) * (1 - (1 - qi) ** 2))

        P_swap = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
        R_pos = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]])
        R_neg = sp.Matrix([[qi, 0, 0, 0], [0, -h, 1, 0], [0, 1, 0, 0], [0, 0, 0, qi]])
        R0_pos = sp.diag(q, 1, 1, q)
        R0_neg = sp.diag(qi, 1, 1, qi)
        EF_mat = sp.Matrix([[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        FE_mat = sp.Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]])
        G_left = sp.diag(1, 1, -1, -1)
        G_right = sp.diag(1, -1, 1, -1)
        Pi_L_plus = (sp.eye(4) + G_left) / 2
        Pi_R_plus = (sp.eye(4) + G_right) / 2

        # Verify strand-tracked crossings & chiral right-quark raising projection
        assert sp.simplify(P_swap * R_pos - (R0_pos + h * EF_mat)) == sp.zeros(4, 4)
        assert sp.simplify(P_swap * R_neg - (R0_neg - h * FE_mat)) == sp.zeros(4, 4)
        proj_c1 = sp.simplify(Pi_R_plus * (P_swap * R_pos - R0_pos) * Pi_L_plus)
        proj_c2 = sp.simplify(Pi_R_plus * (P_swap * R_neg - R0_neg) * Pi_L_plus)
        assert proj_c1 == sp.zeros(4, 4)
        assert sp.simplify(proj_c2 - (-h * FE_mat)) == sp.zeros(4, 4)

        # Verify Sweedler H_4 relations on (G_right, X_minus := -h * FE_mat)
        X_right_cc = -h * FE_mat
        assert G_right * G_right == sp.eye(4)
        assert X_right_cc * X_right_cc == sp.zeros(4, 4)
        assert sp.simplify(X_right_cc * G_right + G_right * X_right_cc) == sp.zeros(4, 4)

        wb.add_assertion(
            "left_lepton_right_quark_C1_pos_beta_minus_projection_zero",
            computed=mpf(0 if proj_c1 == sp.zeros(4, 4) else 1),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="ChargedCurrentChiralitySelection.betaMinusProj_pos_eq_zero",
        )
        wb.add_assertion(
            "left_lepton_right_quark_C2_neg_beta_minus_projection_eq_neg_h_FE",
            computed=abs(eval_sym_at(proj_c2[2, 1] - (-h), q, q0)),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="ChargedCurrentChiralitySelection.betaMinusProj_neg_eq",
        )

        # ==================================================================
        # Part A2: 9-Strand Signed vs Unsigned Readouts Across C1_pos & C2_neg
        # ==================================================================
        pair_std = V_let(0) + V_let(1) + V_let(2) + V_let(0) + V_let(3)
        pair_red = [(0, 1), (0, 1), (1, -1), (4, -1)]
        pair_refl = [(4 - i, s) for (i, s) in pair_std]
        pair_refl_red = [(4, 1), (4, 1), (3, -1), (0, -1)]
        v_nuc3 = V_let(6) * 3
        w_p = [(0, 0, 1), (0, 1, 0), (1, 0, 0)]
        w_n = [(0, 1, 1), (1, 0, 1), (1, 1, 0)]

        # Nucleon 3x3 matrices from NucleonWeightSpaceTwoTerm
        A1 = sp.Matrix([[q, 0, 0], [0, 0, 1], [0, 1, h]])
        A2i = sp.Matrix([[-h, 1, 0], [1, 0, 0], [0, 0, qi]])
        B1 = sp.Matrix([[0, 1, 0], [1, h, 0], [0, 0, q]])
        B2i = sp.Matrix([[qi, 0, 0], [0, -h, 1], [0, 1, 0]])
        Vp3 = (A1 * A2i) ** 3
        Vn3 = (B1 * B2i) ** 3

        def left_w5(letters6: list[tuple[int, int]]) -> list[sp.Expr]:
            res = []
            for s5 in (0, 1):
                acc: LPoly = {}
                for b5 in itertools.product((0, 1), repeat=5):
                    st = b5 + (s5,)
                    out = apply_word_lp(letters6, st)
                    diag = out.get(st)
                    if diag:
                        k_exp = 6 - 2 * sum(st)
                        acc = lp_add(acc, lp_mul({k_exp: Fraction(1)}, diag))
                res.append(sp.together(lp_to_sympy(acc, q) / (d2 ** 6)))
            return res

        blocks = [
            ("bare_spectator", []),
            ("pair_std", pair_red),
            ("pair_refl", pair_refl_red),
        ]
        couplings = [
            ("C0_uncoupled", []),
            ("C1_pos", [(5, 1)]),
            ("C2_neg", [(5, -1)]),
            ("C3_clasp", [(5, 1), (5, 1)]),
            ("C4_vertex", [(5, 1), (6, -1)]),
        ]

        # Direct 512-state 9-strand cross-check on C2_neg (both pair_std and pair_refl)
        for chk_name, chk_left6 in (("pair_std", pair_std), ("pair_refl", pair_refl)):
            w9_full = chk_left6 + [(5, -1)] + v_nuc3
            tr9_p_lp = full_nine_strand_trace_lp(w9_full, w_p)
            tr9_n_lp = full_nine_strand_trace_lp(w9_full, w_n)
            w5_chk = left_w5(chk_left6)
            # Through C2_neg (sigma_5^-1): 00 -> q^-1 (00), 01 -> -h (01) + (10), 10 -> (01), 11 -> q^-1 (11)
            # Closing strand 5 with weight w5[s5]:
            # s6 = 0 gets w5[0] * q^-1 (from 00 -> 00) + w5[1] * 0 (from 10 -> 01, off-diagonal!) = q^-1 w5[0]
            # s6 = 1 gets w5[0] * (-h) (from 01 -> 01!) + w5[1] * q^-1 (from 11 -> 11) = -h w5[0] + q^-1 w5[1]
            d0_raw = qi * w5_chk[0]
            d1_raw = -h * w5_chk[0] + qi * w5_chk[1]
            DA = sp.diag(d0_raw, d0_raw, d1_raw)
            DB = sp.diag(d0_raw, d1_raw, d1_raw)
            eps9_p_fact = sp.together(q * (DA * Vp3).trace() / (d2 ** 3))
            eps9_n_fact = sp.together(qi * (DB * Vn3).trace() / (d2 ** 3))
            eps9_p_direct = sp.together(lp_to_sympy(tr9_p_lp, q) / (d2 ** 9))
            eps9_n_direct = sp.together(lp_to_sympy(tr9_n_lp, q) / (d2 ** 9))
            assert sp.simplify(eps9_p_fact - eps9_p_direct) == 0
            assert sp.simplify(eps9_n_fact - eps9_n_direct) == 0

        wb.add_assertion(
            "direct_512_state_nine_strand_C2_neg_factorization_exact",
            computed=mpf(0),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="Exact Q[q, q^-1] identity on 9-strand pair_std + C2_neg and pair_refl + C2_neg",
        )

        # Helper to compute 9-strand plain & K-weighted traces for any (left6, c_let)
        readout_rows = []
        c2_closed_forms: dict[str, dict[str, str]] = {}
        for bname, b_let in blocks:
            w5 = left_w5(b_let)
            tau_left = sp.factor(w5[0] + w5[1])
            for cname, c_let in couplings:
                if cname == "C4_vertex":
                    # C4_vertex = sigma_5 sigma_6^-1 touches strand 6 and 7; evaluate via 4-strand (5..8)
                    tr_plain_p = sp.Integer(0)
                    tr_plain_n = sp.Integer(0)
                    word_58 = [(idx - 5, sgn) for (idx, sgn) in (c_let + v_nuc3)]
                    for s5 in (0, 1):
                        for u3 in w_p:
                            out = apply_word_lp(word_58, (s5,) + u3)
                            diag = out.get((s5,) + u3)
                            if diag:
                                tr_plain_p += w5[s5] * lp_to_sympy(diag, q) / (d2 ** 3)
                        for u3 in w_n:
                            out = apply_word_lp(word_58, (s5,) + u3)
                            diag = out.get((s5,) + u3)
                            if diag:
                                tr_plain_n += w5[s5] * lp_to_sympy(diag, q) / (d2 ** 3)
                    tr_plain_p = sp.factor(tr_plain_p)
                    tr_plain_n = sp.factor(tr_plain_n)
                else:
                    # Single-strand boundary operator on (5, 6)
                    d_raw = [sp.Integer(0), sp.Integer(0)]
                    for s6 in (0, 1):
                        acc_s6 = sp.Integer(0)
                        for s5 in (0, 1):
                            out2 = apply_word_lp(
                                [(0, sgn) for (_, sgn) in c_let], (s5, s6)
                            )
                            diag2 = out2.get((s5, s6))
                            if diag2:
                                acc_s6 += w5[s5] * lp_to_sympy(diag2, q)
                        d_raw[s6] = sp.factor(acc_s6)
                    DA = sp.diag(d_raw[0], d_raw[0], d_raw[1])
                    DB = sp.diag(d_raw[0], d_raw[1], d_raw[1])
                    tr_plain_p = sp.factor((DA * Vp3).trace() / (d2 ** 3))
                    tr_plain_n = sp.factor((DB * Vn3).trace() / (d2 ** 3))

                eps9_p = sp.factor(q * tr_plain_p)
                eps9_n = sp.factor(qi * tr_plain_n)

                # Symbolic q -> 1+ limits of signed readouts (in units of m_e)
                f2_signed_sym = sp.factor(e0_full * (eps9_n - eps9_p) / tau_left)
                f2_lim1 = sp.limit(f2_signed_sym, q, 1)
                ratio_plain = sp.factor(tr_plain_n / tr_plain_p)
                # d/dq ln(ratio_plain)|_{q=1} -> -lim_{q->1} e0_full * ln(ratio_plain) = -(d/dq ratio_plain)|_{q=1} / ratio_plain(1)
                dratio_at_1 = sp.Subs(sp.diff(ratio_plain, q), q, 1).doit()
                f3c_signed_lim1 = sp.simplify(-dratio_at_1 / ratio_plain.subs(q, 1))

                # 80-dps evaluations at q_0
                tp_q0 = eval_sym_at(tr_plain_p, q, q0)
                tn_q0 = eval_sym_at(tr_plain_n, q, q0)
                ep_q0 = eval_sym_at(eps9_p, q, q0)
                en_q0 = eval_sym_at(eps9_n, q, q0)
                tl_q0 = eval_sym_at(tau_left, q, q0)
                e0_q0 = eval_sym_at(e0_full, q, q0)

                f2_signed_mev = e0_q0 * me_mev * (en_q0 - ep_q0) / tl_q0
                f3c_signed_mev = -e0_q0 * me_mev * mp.log(tn_q0 / tp_q0)
                f3b_signed_mev = -e0_q0 * me_mev * mp.log(en_q0 / ep_q0) - me_mev

                if cname == "C2_neg":
                    c2_closed_forms[bname] = {
                        "tau_left": str(tau_left),
                        "d0_cond": str(sp.factor(d_raw[0] / tau_left)),
                        "d1_cond": str(sp.factor(d_raw[1] / tau_left)),
                        "ratio_plain_n_over_p": str(ratio_plain),
                        "F2_signed_over_me": str(f2_signed_sym),
                    }

                readout_rows.append(
                    {
                        "left_block": bname,
                        "coupling": cname,
                        "F2_signed_limit_q1_over_me": str(f2_lim1),
                        "F2_signed_MeV_q0": fmt50(f2_signed_mev),
                        "F2_abs_MeV_q0": fmt50(abs(f2_signed_mev)),
                        "F3C_signed_limit_q1_over_me": str(f3c_signed_lim1),
                        "F3C_signed_MeV_q0": fmt50(f3c_signed_mev),
                        "F3C_abs_MeV_q0": fmt50(abs(f3c_signed_mev)),
                        "F3B_signed_MeV_q0": fmt50(f3b_signed_mev),
                    }
                )
                print(
                    f"{bname:15s} {cname:13s} | F2_sgn={mp.nstr(f2_signed_mev, 8):11s} "
                    f"| F3C_sgn(1)={str(f3c_signed_lim1):6s} F3C_sgn={mp.nstr(f3c_signed_mev, 8):11s} "
                    f"| F3B_sgn={mp.nstr(f3b_signed_mev, 8):11s} MeV"
                )

        # ==================================================================
        # Part B: k >= 1 Ppos Transient Jet & Magnetic Spin-Spin Channels
        # ==================================================================
        Q12p = sp.diag(sp.Rational(4, 9), sp.Rational(-2, 9), sp.Rational(-2, 9))
        Q23p = sp.diag(sp.Rational(-2, 9), sp.Rational(-2, 9), sp.Rational(4, 9))
        Q13p = sp.diag(sp.Rational(-2, 9), sp.Rational(4, 9), sp.Rational(-2, 9))
        Q12n = sp.diag(sp.Rational(-2, 9), sp.Rational(-2, 9), sp.Rational(1, 9))
        Q23n = sp.diag(sp.Rational(1, 9), sp.Rational(-2, 9), sp.Rational(-2, 9))
        Q13n = sp.diag(sp.Rational(-2, 9), sp.Rational(1, 9), sp.Rational(-2, 9))

        QAdjp = Q12p + Q23p
        QAdjn = Q12n + Q23n
        QPairp = Q12p + Q23p + Q13p
        QPairn = Q12n + Q23n + Q13n

        # Central I=1/2 nucleon projectors e_{(2,1)} on W_p and W_n
        # FEp and EFn from NucleonWeightSpaceSecondOrder / NucleonWeightSpaceTwoTerm
        qInt3 = q ** 2 + 1 + qi ** 2
        FEp = sp.Matrix([[qi ** 2, qi, 1], [qi, 1, q], [1, q, q ** 2]])
        EFn = sp.Matrix([[qi ** 2, qi, 1], [qi, 1, q], [1, q, q ** 2]])
        e21p = sp.eye(3) - FEp / qInt3
        e21n = sp.eye(3) - EFn / qInt3
        assert sp.simplify(e21p * e21p - e21p) == sp.zeros(3, 3)
        assert sp.simplify(e21n * e21n - e21n) == sp.zeros(3, 3)

        # Derived quantum-trace weighting: t_X(W_p) = q tr(X_p V_p^3)/[2]_q^3, t_X(W_n) = q^-1 tr(X_n V_n^3)/[2]_q^3
        # 1. Covariant all-pairs Q_pair:
        dt_allpairs_static = sp.factor((qi * (QPairn * Vn3).trace() - q * (QPairp * Vp3).trace()) / (d2 ** 3))
        dt_allpairs_conn = sp.factor(
            dt_allpairs_static - (qi * sp.Rational(-1, 3) * Vn3.trace()) / (d2 ** 3)
        )
        assert dt_allpairs_conn == 0

        # 2. Adjacent Q_adj on full 3D weight space (k=0 static vs k=4 connected Ppos jet):
        tr_adj_p = (QAdjp * Vp3).trace()
        tr_adj_n = (QAdjn * Vn3).trace()
        tr_adj_n_static = sp.Rational(-2, 9) * Vn3.trace()
        tr_adj_n_conn = sp.factor(tr_adj_n - tr_adj_n_static)  # k = 4: O((q-1)^4)
        dt_adj_static = sp.factor((qi * tr_adj_n_static) / (d2 ** 3))
        dt_adj_conn_ppos = sp.factor((qi * tr_adj_n_conn - q * tr_adj_p) / (d2 ** 3))

        # 3. Adjacent Q_adj on I=1/2 nucleon sector e_{(2,1)} (k=0 static vs k>=1 connected Ppos jet):
        tr_e21_adj_p = sp.factor((e21p * QAdjp * Vp3).trace())  # k = 2: O((q-1)^2)
        tr_e21_adj_n = sp.factor((e21n * QAdjn * Vn3).trace())
        tr_e21_adj_n_static = sp.factor(sp.Rational(-2, 9) * (e21n * Vn3).trace())
        tr_e21_adj_n_conn = sp.factor(tr_e21_adj_n - tr_e21_adj_n_static)  # vanishes at q=1!
        assert tr_e21_adj_n_conn.subs(q, 1) == 0
        dt_e21_adj_static = sp.factor((qi * tr_e21_adj_n_static) / (d2 ** 3))
        dt_e21_adj_conn_ppos = sp.factor((qi * tr_e21_adj_n_conn - q * tr_e21_adj_p) / (d2 ** 3))

        wb.add_assertion(
            "covariant_allpairs_connected_ppos_jet_identically_zero",
            computed=mpf(0 if dt_allpairs_conn == 0 else 1),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="NucleonWeightSpaceTwoTerm.QPairP / QPairN scalarity",
        )

        e0_full_mev = eval_sym_at(e0_full, q, q0) * me_mev
        cem_candidates = {
            "unit_1": mpf(1),
            "alpha_FormB": alpha_q0,
            "jackson_step_1_minus_q_inv2": mpf(1) - (qi0 ** 2),
            "hecke_h_sq": h0 ** 2,
        }

        jet_channels = {}
        for ch_name, sym_expr in (
            ("allpairs_static_k0", dt_allpairs_static),
            ("adj_full_static_k0", dt_adj_static),
            ("adj_full_connected_ppos_k4", dt_adj_conn_ppos),
            ("adj_e21_static_k0", dt_e21_adj_static),
            ("adj_e21_connected_ppos_k2", dt_e21_adj_conn_ppos),
        ):
            val_q0 = eval_sym_at(sym_expr, q, q0)
            jet_channels[ch_name] = {
                "closed_form_Qq": str(sym_expr),
                "trace_diff_at_q0": fmt50(val_q0),
                "sign_at_q0": "+" if val_q0 > 0 else ("-" if val_q0 < 0 else "0"),
                "shift_me_scale_MeV": {
                    ck: fmt50(cv * me_mev * val_q0) for ck, cv in cem_candidates.items()
                },
                "shift_E0_full_scale_MeV": {
                    ck: fmt50(cv * e0_full_mev * val_q0) for ck, cv in cem_candidates.items()
                },
            }

        # 4. Magnetic spin-spin channels: nucleon dipole mu_n^2 - mu_p^2 vs constituent quark hyperfine
        bf_p, bf_n = su6_breit_fermi_expectation()
        bf_diff_np = bf_n - bf_p  # (-1) - (-4/3) = +1/3
        assert bf_p == sp.Rational(-4, 3)
        assert bf_n == sp.Rational(-1, 1)
        assert bf_diff_np == sp.Rational(1, 3)

        wb.add_assertion(
            "su6_constituent_breit_fermi_np_diff_equals_plus_one_third",
            computed=abs(mpf(int(bf_diff_np.p)) / mpf(int(bf_diff_np.q)) - mpf(1) / mpf(3)),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="ChargedCurrentChiralitySelection.breitFermi_np_diff_eq_pos_third",
        )

        # Evaluate parameter-free magnetic energy scales at q_0:
        # Pion-range magnetic recoil scale E_mag_pi = alpha_q(q_0) * m_pi * (m_pi / (2 m_p(q_0)))^2
        # and Compton-oscillator contact scale E_mag_osc = (8/3) sqrt(2/pi) alpha_q(q_0) b_N^-3 / (4 m_q^2)
        # where b_N^-1 = sqrt(m_p(q_0) * m_e / (q_0 - 1)^2) and m_q = m_p(q_0)/3 (constituent SU(6)):
        recoil_pi_sq = (mpi_mev / (mpf(2) * mp_derived)) ** 2
        e_mag_pi_base_mev = alpha_q0 * mpi_mev * recoil_pi_sq

        e_osc_mev = me_mev / ((q0 - mpf(1)) ** 2)
        inv_b_nuc_mev = mp.sqrt(mp_derived * e_osc_mev)
        mq_const_mev = mp_derived / mpf(3)
        # <1s,1s | delta^3(r_12) | 1s,1s> = (2 pi b^2)^(-3/2), so H_BF = (2 pi alpha / (3 m_q^2)) delta^3(r_12) (-q_i q_j sigma_i.sigma_j)
        # Prefactor: (2 pi alpha / (3 m_q^2)) * (2 pi)^(-3/2) b^-3 = (alpha / (3 sqrt(2 pi))) * (b^-3 / m_q^2)
        bf_contact_pref_mev = (
            (alpha_q0 / (mpf(3) * mp.sqrt(mpf(2) * mp.pi)))
            * (inv_b_nuc_mev ** 3)
            / (mq_const_mev ** 2)
        )

        su6_dipole_ratio_np = (mpf(2) / mpf(3)) ** 2 - mpf(1)  # -5/9 < 0
        suq6_dipole_ratio_np = (
            (q_int_at(2, q=q0, dps=80) / q_int_at(3, q=q0, dps=80)) ** 2
        ) - mpf(1)
        codata_dipole_diff_muN2 = (mu_n_codata ** 2) - (mu_p_codata ** 2)

        magnetic_summary = {
            "pointlike_nucleon_dipole_mu_n_sq_minus_mu_p_sq": {
                "SU6_ratio_mu_n2_over_mu_p2_minus_1": fmt50(su6_dipole_ratio_np),
                "SUq6_ratio_at_q0": fmt50(suq6_dipole_ratio_np),
                "CODATA_mu_n2_minus_mu_p2_muN2_comparison": fmt50(codata_dipole_diff_muN2),
                "sign": "- (shifts pointlike magnetic self-energy m_n - m_p < 0)",
                "pion_recoil_scale_shift_MeV_SU6": fmt50(
                    e_mag_pi_base_mev * (mpf(9) * su6_dipole_ratio_np / mpf(4))
                ),
            },
            "constituent_quark_breit_fermi_hyperfine": {
                "proton_56plet_matrix_element": "-4/3",
                "neutron_56plet_matrix_element": "-1",
                "np_difference_matrix_element": "+1/3 (exact opposite of static electric Q_pair = -1/3)",
                "sign": "+ (shifts m_n - m_p > 0, reinforcing Q_beta > 0)",
                "compton_ho_contact_shift_MeV": fmt50(bf_contact_pref_mev * (mpf(1) / mpf(3))),
                "pion_recoil_scale_shift_MeV": fmt50(e_mag_pi_base_mev * (mpf(1) / mpf(3))),
            },
        }

        wb.add_data("c2_neg_closed_forms_Qq", c2_closed_forms)
        wb.add_data("nine_strand_signed_readouts", readout_rows)
        wb.add_data("two_term_ppos_transient_jets", jet_channels)
        wb.add_data("magnetic_spin_spin_channels", magnetic_summary)
        wb.add_data(
            "comparison_only_CODATA",
            {
                "Q_beta_MeV": fmt50(qbeta_codata_mev),
                "Delta_m_np_MeV": fmt50(dm_np_codata_mev),
            },
        )
        wb.save({"q0Anchor": "proton"})
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
