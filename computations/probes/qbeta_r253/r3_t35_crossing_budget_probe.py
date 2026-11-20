#!/usr/bin/env python3
"""R3 (bean qou-99qc): machine-check the T(3,5) weak-vertex claims of
predicted-spectra/beta-decay-skein-properties.md.

Pre-registered checks 1-8 in PREREGISTRATION.md (same directory). Exact arithmetic only
(sympy over Q(q), integer Burau over Z[t^{+-1}]). No q0, no MeV: no Q_beta is produced
here because the block's Q formula is not defined under convention D (check 8).
"""
from __future__ import annotations

import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import _path_bridge  # noqa: E402,F401

import sympy as sp  # noqa: E402

q, t = sp.symbols("q t", positive=True)
h = q - 1 / q
T35 = (1, 2) * 5

# reduced Burau, faithful on B3
B = {1: sp.Matrix([[-t, 1], [0, 1]]), 2: sp.Matrix([[1, 0], [t, -t]])}


def burau(w):
    M = sp.eye(2)
    for a in w:
        M = M * B[a]
    return M.applyfunc(sp.expand)


def perm(w):
    p = [0, 1, 2]
    for a in w:
        i = a - 1
        p[i], p[i + 1] = p[i + 1], p[i]
    return p


def check1():
    p = perm(T35)
    cyc = p != [0, 1, 2] and all(p[i] != i for i in range(3))
    return len(T35) == 10 and cyc, {"letters": len(T35), "permutation": p, "closure_is_knot": cyc}


def check2():
    target = burau(T35)
    lead = {}
    for i in (1, 2):
        lead[f"sigma{i}^3 * P"] = sum(1 for P in itertools.product((1, 2), repeat=7)
                                       if burau((i,) * 3 + P) == target)
    anywhere = 0
    for i in (1, 2):
        for a in range(8):
            for A in itertools.product((1, 2), repeat=a):
                for Bw in itertools.product((1, 2), repeat=7 - a):
                    if burau(A + (i,) * 3 + Bw) == target:
                        anywhere += 1
    lead["A * sigma_i^3 * B, all positions"] = anywhere
    return lead["sigma1^3 * P"] >= 1, lead


def hecke_reduce(word, strategy):
    """Rewrite in H3: s_i s_i -> h s_i + 1, (2,1,2) -> (1,2,1). Returns (normal form, #quadratic)."""
    terms = {tuple(word): sp.Integer(1)}
    nquad = 0
    while True:
        red = None
        for w, c in terms.items():
            pos = []
            for k in range(len(w) - 1):
                if w[k] == w[k + 1]:
                    pos.append((k, "quad"))
            for k in range(len(w) - 2):
                if w[k:k + 3] == (2, 1, 2):
                    pos.append((k, "braid"))
            if pos:
                pos.sort()
                red = (w, c, pos[0] if strategy == "left" else pos[-1])
                break
        if red is None:
            break
        w, c, (k, kind) = red
        del terms[w]
        if kind == "quad":
            nquad += 1
            out = [(w[:k] + w[k + 1:], c * h), (w[:k] + w[k + 2:], c)]
        else:
            out = [(w[:k] + (1, 2, 1) + w[k + 3:], c)]
        for nw, nc in out:
            terms[nw] = sp.simplify(terms.get(nw, 0) + nc)
            if terms[nw] == 0:
                del terms[nw]
    return {"".join(map(str, k)) or "1": sp.factor(v) for k, v in terms.items()}, nquad


# W- block model (udd, dud, ddu) = (3) + (2,1)
sm = {1: sp.Matrix([[0, 1, 0], [1, h, 0], [0, 0, q]]), 2: sp.Matrix([[q, 0, 0], [0, 0, 1], [0, 1, h]])}


def chars(x_poly_word_list):
    """characters of a linear combination [(coef, word)] on (3), (2,1), (1^3)."""
    c3 = c21 = c111 = sp.Integer(0)
    for c, w in x_poly_word_list:
        M = sp.eye(3)
        for a in w:
            M = M * sm[a]
        c3 += c * q ** len(w)
        c111 += c * (-1 / q) ** len(w)
        c21 += c * (M.trace() - q ** len(w))
    return sp.simplify(c3), sp.simplify(c21), sp.simplify(c111)


def main() -> int:
    res = {}
    ok1, d1 = check1(); res["1_ten_crossings_knot"] = (ok1, d1)
    ok2, d2 = check2(); res["2_sigma1cubed_divides"] = (ok2, d2)
    res["3_R2_moves_in_positive_word"] = (True, {"free_reductions_possible": 0,
        "note": "a positive word has no sigma sigma^-1 pair; the block's 'R2 (T^2=hT+1)' is the Hecke "
                "quadratic relation, not Reidemeister II"})
    nfL, nL = hecke_reduce(T35, "left"); nfR, nR = hecke_reduce(T35, "right")
    same_nf = all(sp.simplify(nfL.get(k, 0) - nfR.get(k, 0)) == 0 for k in set(nfL) | set(nfR))
    res["4_quadratic_count_order_dependence"] = (same_nf, {"left_first": nL, "right_first": nR,
        "order_independent": nL == nR, "normal_forms_agree": same_nf})
    y3 = (q**4 + 1) / (q**2 + 1) ** 2; y21 = q**2 / (q**2 + 1) ** 2
    c3, c21, c111 = chars([(1, T35)])
    W = sp.factor(sp.simplify(y3 * c3 + y21 * c21))
    num, den = sp.fraction(sp.together(W))
    laurent = sp.Poly(den, q).is_monomial
    res["5_W_in_Z[q^{+-1/2}]"] = (laurent, {"W_zD": str(W), "denominator": str(sp.factor(den)),
        "is_laurent_polynomial": laurent, "chi3": str(c3), "chi21": str(sp.factor(c21)), "chi111": str(c111)})
    res["6_normal_form"] = (max(len(k) for k in nfL) <= 3, {k: str(v) for k, v in nfL.items()})
    Bp = [(1, (1, 2)), (-h / 2, (1,))]
    Bn = [(1, (1, 2)), (-h, (1,)), (-h / 2, (2,)), (h**2 / 2, ())]
    BnW = [(c, w + T35) for c, w in Bn]
    a3, a21, a111 = chars(BnW); b3, b21, b111 = chars(Bp)
    ratios = [sp.factor(sp.simplify(a3 / b3)), sp.factor(sp.simplify(a111 / b111))]
    scalar = sp.simplify(ratios[0] - ratios[1]) == 0
    res["7_Bn_T35_eq_c_Bp"] = (scalar, {"ratio_trivial_block": str(ratios[0]), "ratio_sign_block": str(ratios[1]),
        "single_scalar_exists": scalar})
    BpL = [(c, w + (1, 1, 1)) for c, w in Bp]
    e3, e21, e111 = chars(BpL)
    r2 = [sp.factor(sp.simplify(a3 / e3)), sp.factor(sp.simplify(a111 / e111))]
    res["7b_post_registration_Bn_T35_eq_c_Bp_sigma1cubed"] = (sp.simplify(r2[0] - r2[1]) == 0,
        {"ratio_trivial": str(r2[0]), "ratio_sign": str(r2[1])})
    res["8_Q_formula_under_D"] = (False, {"reason": "Q = Delta(R2 steps) x (q-q^-1) x (pair Skein scale): the scale "
        "is the excised convention-C weight 1/(q^1/2+q^-1/2) and the 'R2 step count' is order-dependent "
        "(check 4) and undefined for a positive word (check 3). No convention-D Q_beta is defined by the block."})
    for k, (ok, d) in res.items():
        print(("TRUE  " if ok else "FALSE ") + k, d)
    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("qbeta-r3-t35-crossing-budget", engine="sympy")
        wb.set_description("R3 of bean qou-99qc: exact checks of the T(3,5) claims of "
                           "beta-decay-skein-properties.md (pre-registered).")
        for k, (ok, d) in res.items():
            wb.add_data(k, {"holds": bool(ok), "detail": {kk: (vv if isinstance(vv, (int, bool, str, list)) else str(vv)) for kk, vv in d.items()}})
        wb.add_caveat("Exact arithmetic only; no q0 and no MeV value enters.")
        print("witness:", wb.save())
    except Exception as exc:  # pragma: no cover
        print("witness not written:", exc)
    return 0


if __name__ == "__main__":
    sys.exit(main())
