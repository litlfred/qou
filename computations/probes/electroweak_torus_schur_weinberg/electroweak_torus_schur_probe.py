#!/usr/bin/env python3
"""EXPLORATORY shape-probe (pre-registered 80-dps verification, bean qou-vexf):
Non-volume Frobenius, Higman, and Schur boson mass functionals on Vol = 0 torus links/knots
T(2,4) (sigma_0^4 in H_2 and (sigma_0 sigma_1 sigma_2)^2 in H_4), T(3,5) ((sigma_0 sigma_1)^5
in H_3), and T(2,6) (sigma_0^6 in H_2), testing the implied tree-level Weinberg ratio
sin^2(theta_W) = 1 - (M_W / M_Z)^2 with zero fitted parameters.

Pre-registration: PREREGISTRATION.md (committed in 5be409c2671 prior to evaluation).
Lean companion: QOU/StandardModel/TorusLinkElectroweakSchurRatio.lean.

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
from mpmath import mp, mpf  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import M_E_MEV_STR, Q_MP, q_at  # noqa: E402
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

R_LP_POS = {
    (0, 0): [((0, 0), LP_Q)],
    (0, 1): [((1, 0), LP_ONE)],
    (1, 0): [((0, 1), LP_ONE), ((1, 0), LP_H)],
    (1, 1): [((1, 1), LP_Q)],
}


def quantum_trace_word_sympy(
    n_strands: int, letters: list[int], q_sym: sp.Symbol
) -> sp.Expr:
    """Direct U_q(sl_2) Convention-D quantum trace [2]_q^-n Tr_{V^xn}(K^xn W) over Q(q)."""
    tot: LPoly = {}
    for st0 in itertools.product((0, 1), repeat=n_strands):
        cur: dict[tuple[int, ...], LPoly] = {st0: LP_ONE}
        for idx in reversed(letters):
            nxt: dict[tuple[int, ...], LPoly] = {}
            for st, coeff in cur.items():
                for (a, b), rc in R_LP_POS[(st[idx], st[idx + 1])]:
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
        diag = cur.get(st0)
        if diag:
            k_exp = n_strands - 2 * sum(st0)
            tot = lp_add(tot, lp_mul({k_exp: Fraction(1)}, diag))
    poly_expr = sum(
        sp.Rational(v.numerator, v.denominator) * (q_sym ** k) for k, v in tot.items()
    )
    return sp.factor(poly_expr / ((q_sym + 1 / q_sym) ** n_strands))


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


def main() -> int:
    with mp.workdps(80):
        q0 = q_at(80)
        qi0 = mpf(1) / q0
        hbar_sq = (mpf(1) - qi0) ** 2
        me_mev = mpf(M_E_MEV_STR)

        # Comparison-only empirical weak mixing angles:
        # CODATA-2022 on-shell sin^2(theta_W) = 1 - (m_W / m_Z)^2
        sin2_codata_onshell = codata("weak mixing angle").value
        # PDG MS-bar sin^2(theta_W)(M_Z) benchmark cited in prompt (comparison only)
        sin2_pdg_msbar = mpf("0.23122")  # noqa: P31 (PDG MS-bar comparison benchmark)

        wb = WitnessBuilder(
            "electroweak-torus-schur",
            engine="mpmath (80 dps) + sympy Q(q)",
            output_dir=HERE,
        )
        wb.set_description(
            "Pre-registered 80-dps evaluation of Convention-D Markov traces, Higman/Frobenius "
            "norms, and Schur-weighted boson mass ratios on Vol = 0 torus links/knots T(2,4) "
            "(H_2 and H_4), T(3,5) (H_3), and T(2,6) (H_2), testing tree-level sin^2(theta_W) = "
            "1 - (M_W / M_Z)^2 with zero fitted parameters (qou-vexf / L2 Gate 2)."
        )
        wb.add_parameter("workdps", 80)
        wb.add_parameter("q0_proton_50dps", fmt50(q0))
        wb.add_parameter("preregistration_commit", "5be409c2671")

        wb.add_assertion(
            "q0_at_80_matches_Q_MP",
            computed=abs(q0 - (+Q_MP)),
            expected=mpf(0),
            tolerance=mpf("1e-65"),
            source="qou_substrate.constants",
        )

        # ==================================================================
        # 1. Exact Symbolic Wedderburn & U_q(sl_2) Quantum-Trace Cross-Checks
        # ==================================================================
        q = sp.Symbol("q", positive=True)
        qi = 1 / q
        h = q - qi
        zD = q ** 3 / (q ** 2 + 1)

        # Quantum integers & balanced q-factorials [n]_q = (q^n - q^-n)/(q - q^-1)
        def q_int_sym(k: int) -> sp.Expr:
            return sp.factor(sum(q ** (k - 1 - 2 * j) for j in range(k)))

        def q_fact_sym(n: int) -> sp.Expr:
            prod = sp.Integer(1)
            for j in range(1, n + 1):
                prod *= q_int_sym(j)
            return sp.factor(prod)

        # H_2(q) Convention-D Wedderburn weights & Schur elements
        y2_triv = (q ** 4 + q ** 2 + 1) / ((q ** 2 + 1) ** 2)
        y2_sign = (q ** 2) / ((q ** 2 + 1) ** 2)
        c2_triv = sp.factor(q * q_fact_sym(2))  # q^2 + 1
        c2_sign = sp.factor(qi * q_fact_sym(2))  # 1 + q^-2

        # Verify H_2 Markov basis axioms: tr_M(1) = 1, tr_M(sigma_0) = z_D
        assert sp.simplify(y2_triv + y2_sign - 1) == 0
        assert sp.simplify(q * y2_triv - qi * y2_sign - zD) == 0

        # T(2,4) in H_2: sigma_0^4 = (h^3 + 2h) sigma_0 + (h^2 + 1)
        tr_t24_h2 = sp.factor(y2_triv * (q ** 4) + y2_sign * (qi ** 4))
        tr_t24_hecke = sp.factor((h ** 3 + 2 * h) * zD + (h ** 2 + 1))
        tr_t24_qtr = quantum_trace_word_sympy(2, [0, 0, 0, 0], q)
        assert sp.simplify(tr_t24_h2 - tr_t24_hecke) == 0
        assert sp.simplify(tr_t24_h2 - tr_t24_qtr) == 0

        # T(2,6) in H_2: sigma_0^6
        tr_t26_h2 = sp.factor(y2_triv * (q ** 6) + y2_sign * (qi ** 6))
        tr_t26_qtr = quantum_trace_word_sympy(2, [0] * 6, q)
        assert sp.simplify(tr_t26_h2 - tr_t26_qtr) == 0

        # Frobenius Gram norm squared on H_2: tr_M(beta^T beta) = tr_M(sigma_0^(2w))
        gram_t24_h2 = sp.factor(y2_triv * (q ** 8) + y2_sign * (qi ** 8))
        gram_t26_h2 = sp.factor(y2_triv * (q ** 12) + y2_sign * (qi ** 12))

        # H_3(q) Convention-D Wedderburn weights & Schur elements (WeakVertexT35)
        y3_triv = (q ** 4 + 1) / ((q ** 2 + 1) ** 2)
        y3_std = (q ** 2) / ((q ** 2 + 1) ** 2)
        c3_triv = sp.factor((q ** 3) * q_fact_sym(3))  # (q^2+1)(q^4+q^2+1)
        c3_std = q_int_sym(3)  # q^2 + 1 + q^-2
        c3_sign = sp.factor((qi ** 3) * q_fact_sym(3))

        # T(3,5) in H_3: (sigma_0 sigma_1)^5
        tr_t35_h3 = sp.factor(y3_triv * (q ** 10) - y3_std)
        tr_t35_qtr = quantum_trace_word_sympy(3, [0, 1] * 5, q)
        assert sp.simplify(tr_t35_h3 - tr_t35_qtr) == 0

        # Frobenius Gram norm squared on T(3,5): beta^T beta = (sigma_1 sigma_0)^5 (sigma_0 sigma_1)^5
        gram_t35_h3 = quantum_trace_word_sympy(3, ([1, 0] * 5) + ([0, 1] * 5), q)
        # Verify Wedderburn formula on (2,1) block for beta^T beta!
        s0_21 = sp.Matrix([[q, 1], [0, -qi]])
        s1_21 = sp.Matrix([[-qi, 0], [1, q]])
        # Note: in Young's orthogonal (symmetric) form or direct quantum trace, let's check trace on (2,1):
        # Wait: seminormal stdGen0/1 is NOT symmetric, so the anti-involution sigma_i -> sigma_i corresponds
        # to reversing the generator list: ((s1_21 * s0_21)^5 * (s0_21 * s1_21)^5).trace()!
        chi21_gram_t35 = sp.factor((((s1_21 * s0_21) ** 5) * ((s0_21 * s1_21) ** 5)).trace())
        assert sp.simplify(gram_t35_h3 - (y3_triv * (q ** 20) + y3_std * chi21_gram_t35)) == 0

        # H_4(q) Convention-D Wedderburn weights & Schur elements for T(4,2) = (sigma_0 sigma_1 sigma_2)^2
        y4_triv = (q ** 8 + q ** 6 + q ** 4 + q ** 2 + 1) / ((q ** 2 + 1) ** 4)
        y4_31 = (q ** 2) * (q ** 4 + q ** 2 + 1) / ((q ** 2 + 1) ** 4)
        y4_22 = (q ** 4) / ((q ** 2 + 1) ** 4)
        # Wenzl/Geck-Pfeiffer Schur elements on H_4(q):
        # hook product for (4): [4]_q!; for (3,1): hooks (4,2,1,1) -> [4][2], n(3,1)=1, contentSum=2 -> q^2 [4]_q [2]_q;
        # for (2,2): hooks (3,2,2,1) -> [3][2]^2, contentSum=0 -> [3]_q [2]_q^2.
        c4_triv = sp.factor((q ** 6) * q_fact_sym(4))
        c4_31 = sp.factor((q ** 2) * q_int_sym(4) * q_int_sym(2))
        c4_22 = sp.factor(q_int_sym(3) * (q_int_sym(2) ** 2))
        c4_sign = sp.factor((qi ** 6) * q_fact_sym(4))
        # Check Plancherel sum on H_4: sum_{lam |- 4} (f_lam)^2 / c_lam? Wait: sum_{lam} f_lam / c_lam(1) = 1/24 + 9/8 + ... no,
        # in H_n(q), 1 = sum_{lam |- n} f_lam / c_lam(q) when tr_reg(1) = 1! Let's check!
        c4_211 = sp.factor((qi ** 2) * q_int_sym(4) * q_int_sym(2))
        assert (
            sp.simplify(
                1 / c4_triv + 3 / c4_31 + 2 / c4_22 + 3 / c4_211 + 1 / c4_sign - 1
            )
            == 0
        )

        tr_t42_h4 = sp.factor(y4_triv * (q ** 6) + y4_31 * (-(q ** 2)) + y4_22 * 2)
        tr_t42_qtr = quantum_trace_word_sympy(4, [0, 1, 2, 0, 1, 2], q)
        assert sp.simplify(tr_t42_h4 - tr_t42_qtr) == 0
        assert sp.simplify(tr_t42_h4 - (zD ** 2) * tr_t24_h2) == 0

        gram_t42_h4 = quantum_trace_word_sympy(
            4, [2, 1, 0, 2, 1, 0, 0, 1, 2, 0, 1, 2], q
        )

        wb.add_assertion(
            "H2_T24_markov_trace_matches_Uqsl2_quantum_trace",
            computed=abs(eval_sym_at(tr_t24_h2 - tr_t24_qtr, q, q0)),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="TorusLinkElectroweakSchurRatio.ocneanuD_H2_T24_eq",
        )
        wb.add_assertion(
            "H4_T42_markov_stabilization_zD_sq_identity_exact",
            computed=abs(eval_sym_at(tr_t42_h4 - (zD ** 2) * tr_t24_h2, q, q0)),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="TorusLinkElectroweakSchurRatio.ocneanuD_H4_T42_eq_zD_sq_mul_T24",
        )
        wb.add_assertion(
            "H4_schur_elements_plancherel_partition_of_unity_exact",
            computed=mpf(0),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="1/c_(4) + 3/c_(3,1) + 2/c_(2,2) + 3/c_(2,1,1) + 1/c_(1^4) == 1 in Q(q)",
        )

        # ==================================================================
        # 2. Evaluate Pre-Registered Mass Functionals M1..M6 at q=1 and q_0
        # ==================================================================
        carriers = {
            "T24_H2": {
                "n": 2,
                "tr_M": tr_t24_h2,
                "c_triv": c2_triv,
                "qfact_over_qn": sp.factor(q_fact_sym(2) / (q ** 2)),
                "c_sign": c2_sign,
                "schur_irrep": sp.factor(
                    c2_triv * y2_triv * (q ** 4) + c2_sign * y2_sign * (qi ** 4)
                ),
                "gram_sq": gram_t24_h2,
            },
            "T42_H4": {
                "n": 4,
                "tr_M": tr_t42_h4,
                "c_triv": c4_triv,
                "qfact_over_qn": sp.factor(q_fact_sym(4) / (q ** 4)),
                "c_sign": c4_sign,
                "schur_irrep": sp.factor(
                    c4_triv * y4_triv * (q ** 6)
                    + c4_31 * y4_31 * (-(q ** 2))
                    + c4_22 * y4_22 * 2
                ),
                "gram_sq": gram_t42_h4,
            },
            "T35_H3": {
                "n": 3,
                "tr_M": tr_t35_h3,
                "c_triv": c3_triv,
                "qfact_over_qn": sp.factor(q_fact_sym(3) / (q ** 3)),
                "c_sign": c3_sign,
                "schur_irrep": sp.factor(
                    c3_triv * y3_triv * (q ** 10) + c3_std * y3_std * (-1)
                ),
                "gram_sq": gram_t35_h3,
            },
            "T26_H2": {
                "n": 2,
                "tr_M": tr_t26_h2,
                "c_triv": c2_triv,
                "qfact_over_qn": sp.factor(q_fact_sym(2) / (q ** 2)),
                "c_sign": c2_sign,
                "schur_irrep": sp.factor(
                    c2_triv * y2_triv * (q ** 6) + c2_sign * y2_sign * (qi ** 6)
                ),
                "gram_sq": gram_t26_h2,
            },
        }

        carrier_evals: dict[str, dict[str, mpf]] = {}
        carrier_sym_forms: dict[str, dict[str, str]] = {}
        carrier_q1_vals: dict[str, dict[str, sp.Expr]] = {}

        for cname, cd in carriers.items():
            n_val = int(cd["n"])
            tr_m_sym = cd["tr_M"]
            link_stab_sym = sp.factor(tr_m_sym / (zD ** (n_val - 1)))
            m3a_sym = sp.factor(tr_m_sym * cd["c_triv"])
            m3b_qf_sym = sp.factor(tr_m_sym * cd["qfact_over_qn"])
            m3b_sgn_sym = sp.factor(tr_m_sym * cd["c_sign"])
            m4_sym = cd["schur_irrep"]
            gram_sq_sym = cd["gram_sq"]

            tr_q0 = abs(eval_sym_at(tr_m_sym, q, q0))
            gram_q0 = mp.sqrt(abs(eval_sym_at(gram_sq_sym, q, q0)))
            c_triv_q0 = eval_sym_at(cd["c_triv"], q, q0)

            carrier_evals[cname] = {
                "M1_markov_raw": tr_q0,
                "M2_link_stabilized": abs(eval_sym_at(link_stab_sym, q, q0)),
                "M3a_schur_triv_poincare": abs(eval_sym_at(m3a_sym, q, q0)),
                "M3b_mass_channel_qfact_over_qn": abs(eval_sym_at(m3b_qf_sym, q, q0)),
                "M3c_schur_sign_element": abs(eval_sym_at(m3b_sgn_sym, q, q0)),
                "M4_schur_irrep_weighted": abs(eval_sym_at(m4_sym, q, q0)),
                "M5a_frobenius_gram_l2": gram_q0,
                "M5b_frobenius_gram_poincare": gram_q0 * c_triv_q0,
                "M6_log_action": abs(mp.log(tr_q0)),
            }
            carrier_q1_vals[cname] = {
                "M1_markov_raw": abs(tr_m_sym.subs(q, 1)),
                "M2_link_stabilized": abs(link_stab_sym.subs(q, 1)),
                "M3a_schur_triv_poincare": abs(m3a_sym.subs(q, 1)),
                "M3b_mass_channel_qfact_over_qn": abs(m3b_qf_sym.subs(q, 1)),
                "M3c_schur_sign_element": abs(m3b_sgn_sym.subs(q, 1)),
                "M4_schur_irrep_weighted": abs(m4_sym.subs(q, 1)),
                "M5a_frobenius_gram_l2": sp.sqrt(abs(gram_sq_sym.subs(q, 1))),
                "M5b_frobenius_gram_poincare": sp.sqrt(abs(gram_sq_sym.subs(q, 1)))
                * cd["c_triv"].subs(q, 1),
            }
            carrier_sym_forms[cname] = {
                "tr_M_D": str(tr_m_sym),
                "M3a_schur_triv_poincare": str(m3a_sym),
                "M3b_mass_channel_qfact_over_qn": str(m3b_qf_sym),
                "M4_schur_irrep_weighted": str(m4_sym),
                "gram_sq": str(gram_sq_sym),
                "GeV_scale_M3a_over_hbar2": fmt50(
                    carrier_evals[cname]["M3a_schur_triv_poincare"]
                    * me_mev
                    / hbar_sq
                    * mpf("1e-3")
                ),
            }

        # Verify M2 link_stabilized invariance between T24_H2 and T42_H4
        wb.add_assertion(
            "M2_link_stabilized_invariant_between_T24_H2_and_T42_H4",
            computed=abs(
                carrier_evals["T24_H2"]["M2_link_stabilized"]
                - carrier_evals["T42_H4"]["M2_link_stabilized"]
            ),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="Markov stabilization M2 invariance",
        )

        # ==================================================================
        # 3. Tree-Level Weinberg Mixing Ratios sin^2(theta_W) = 1 - (M_W / M_Z)^2
        # ==================================================================
        pairs = [
            ("T24_H2", "T35_H3", "Primary Gate 2: W=T(2,4) in H_2 vs Z=T(3,5) in H_3"),
            ("T42_H4", "T35_H3", "4-strand W=T(4,2) in H_4 vs Z=T(3,5) in H_3"),
            ("T24_H2", "T26_H2", "EW-triplet control: W=T(2,4) vs Z=T(2,6) in H_2"),
        ]

        weinberg_rows = []
        for w_key, z_key, desc in pairs:
            print(f"\n=== {desc} ===")
            for m_key in carrier_evals[w_key]:
                mw = carrier_evals[w_key][m_key]
                mz = carrier_evals[z_key][m_key]
                ratio = mw / mz
                cos2 = ratio ** 2
                sin2 = mpf(1) - cos2
                physical = mpf(0) < sin2 < mpf(1)

                q1_sin2_str = "log_0_over_log_singular_at_q1"
                if m_key in carrier_q1_vals[w_key]:
                    zq1 = carrier_q1_vals[z_key][m_key]
                    if zq1 != 0:
                        rq1 = sp.simplify(carrier_q1_vals[w_key][m_key] / zq1)
                        q1_sin2_str = str(sp.simplify(1 - rq1 ** 2))

                row = {
                    "W_carrier": w_key,
                    "Z_carrier": z_key,
                    "functional": m_key,
                    "sin2_thetaW_limit_q1": q1_sin2_str,
                    "M_W_over_M_Z_q0": fmt50(ratio),
                    "cos2_thetaW_q0": fmt50(cos2),
                    "sin2_thetaW_q0": fmt50(sin2),
                    "in_physical_window_0_1": physical,
                    "diff_vs_CODATA_onshell_0p22305": fmt50(sin2 - sin2_codata_onshell),
                    "diff_vs_PDG_MSbar_0p23122": fmt50(sin2 - sin2_pdg_msbar),
                }
                weinberg_rows.append(row)
                print(
                    f"  {m_key:31s} | q->1: {q1_sin2_str:10s} | M_W/M_Z={mp.nstr(ratio, 7):9s} "
                    f"| sin^2={mp.nstr(sin2, 8):11s} | phys={str(physical):5s}"
                )

        wb.add_data("carrier_closed_forms_Qq", carrier_sym_forms)
        wb.add_data(
            "carrier_evaluations_q0",
            {
                ck: {mk: fmt50(mv) for mk, mv in cv.items()}
                for ck, cv in carrier_evals.items()
            },
        )
        wb.add_data("weinberg_ratio_table", weinberg_rows)
        wb.add_data(
            "comparison_only_empirical",
            {
                "CODATA_2022_onshell_sin2_thetaW": fmt50(sin2_codata_onshell),
                "PDG_MSbar_sin2_thetaW_MZ": fmt50(sin2_pdg_msbar),
            },
        )
        wb.save({"q0Anchor": "proton"})
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
