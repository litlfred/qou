#!/usr/bin/env python3
"""Quark template, tracked order by order in the tower (recipe: preregistration.md, committed 6b9dd5d172
before this ran).

Every letter of a nucleon word is sigma_g + c*h with c rational and h = q - 1/q, because
sigma^-1 = sigma - h. The template is split into a sign map eps: {u,d} -> {+1,-1} and a pair rule
(AVG, LO, HI). Each variant's characters chi_(3), chi_(2,1), chi_(1^3) are computed EXACTLY over Q(q)
with sympy; signs are decided on the whole interval (1, oo) by real-root isolation, and the Taylor
series in t = q - 1 is reported with the sign of every partial sum at q0.

No ranking, no Q_beta / CODATA / mass input. Exact arithmetic for verdicts; mpmath 60 dps for values.
"""
import itertools
import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
for p in ("tools/pyhecke/python", "tools/qou-substrate/python", "computations", "computations/substrate"):
    sys.path.insert(0, str(ROOT / p))
from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 60
q, t = sp.symbols("q t", positive=True)
h = q - 1 / q
ORDER = 6

# 2-dim irreducible of H_3(q): rho(s_i) = -q^-1 * S_i(q^2), S = reduced Burau (checked in ../bring_route2)
R = {0: -sp.Matrix([[-q**2, 1], [0, 1]]) / q, 1: -sp.Matrix([[1, 0], [q**2, -q**2]]) / q}
I2 = sp.eye(2)

CORE = [(0, 0), (1, -1)] * 3                      # (sigma_0 sigma_1^-1)^3 ; letter = (gen, c)
GLUON = [(0, 0), (0, 0)]
QUARKS = {"p": "uud", "n": "udd"}
PAIRS = [(0, 1), (0, 2), (1, 2)]
PLACEMENT = [0, 0, 1]                              # builder: each pair on its lower-index generator

SIGNS = {"S+": {"u": 1, "d": -1}, "S-": {"u": -1, "d": 1}, "S0": {"u": 1, "d": 1}, "S1": {"u": -1, "d": -1}}
RULES = ("AVG", "LO", "HI")


def shift(rule, ea, eb):
    if rule == "AVG":
        return sp.Rational(ea + eb - 2, 4)
    e = ea if rule == "LO" else eb
    return sp.Rational(e - 1, 2)


def templates():
    for s in ("S0", "S1"):
        yield f"{s}", s, "AVG"
    for s in ("S+", "S-"):
        for r in RULES:
            yield f"{s}{r}", s, r


def quark_letters(nuc, sign, rule, placement=PLACEMENT):
    qs, eps = QUARKS[nuc], SIGNS[sign]
    return [(g, shift(rule, eps[qs[a]], eps[qs[b]])) for (a, b), g in zip(PAIRS, placement)]


def chars(letters):
    M, c3, c111 = I2, sp.Integer(1), sp.Integer(1)
    for g, c in letters:
        M = M * (R[g] + c * h * I2)
        c3 *= q + c * h
        c111 *= -1 / q + c * h
    return sp.factor(sp.simplify(M.trace())), sp.factor(c3), sp.factor(c111)


def sign_on_interval(expr):
    """Exact sign pattern of a rational function on (1, oo): roots of numerator and denominator
    isolated as real algebraic numbers, sign sampled at a rational point in every sub-interval."""
    num, den = sp.fraction(sp.together(expr))
    crit = set()
    for poly in (num, den):
        P = sp.Poly(sp.expand(poly), q)
        if P.degree() > 0:
            for r in sp.real_roots(P):
                if r > 1:
                    crit.add(r)
    crit = sorted(crit)
    pts = [sp.Integer(1)] + crit + [None]
    out = []
    for a, b in zip(pts[:-1], pts[1:]):
        lo = sp.Rational(a.evalf(30)) if a != 1 else sp.Integer(1)
        x = (lo + sp.Rational(b.evalf(30))) / 2 if b is not None else lo + 1
        val = expr.subs(q, x)
        out.append({"from": str(sp.N(a, 20)), "to": "oo" if b is None else str(sp.N(b, 20)),
                    "sign": int(sp.sign(val))})
    return out


def series(expr):
    s = sp.series(expr.subs(q, 1 + t), t, 0, ORDER + 1).removeO()
    return [sp.nsimplify(sp.expand(s).coeff(t, k)) for k in range(ORDER + 1)]


def at_q0(expr, q0):
    return sp.lambdify(q, expr, "mpmath")(q0)


def leading(coeffs):
    for k, c in enumerate(coeffs):
        if c != 0:
            return k, int(sp.sign(c))
    return None, 0


def analyse(letters, q0):
    c21, c3, c111 = chars(letters)
    co21, co3 = series(c21), series(c3)
    t0 = q0 - 1
    partial = []
    acc = mp.mpf(0)
    for k, c in enumerate(co21):
        acc += mp.mpf(sp.Rational(c).p) / mp.mpf(sp.Rational(c).q) * t0 ** k
        partial.append(int(mp.sign(acc)))
    lk, ls = leading(co21)
    v21, v3 = at_q0(c21, q0), at_q0(c3, q0)
    iv = sign_on_interval(c21)
    contains = next(i for i in iv if mp.mpf(i["from"]) < q0 and (i["to"] == "oo" or q0 < mp.mpf(i["to"])))
    return {
        "chi21": str(c21), "chi3": str(c3), "chi111": str(c111),
        "chi21_series_t": [str(c) for c in co21], "chi3_series_t": [str(c) for c in co3],
        "chi21_leading_order": lk, "chi21_leading_sign": ls,
        "chi21_partial_sum_signs_at_q0": partial,
        "chi21_at_q0": v21, "chi3_at_q0": v3, "chi111_at_q0": at_q0(c111, q0),
        "chi21_sign_on_(1,oo)": iv, "chi21_sign_on_interval_containing_q0": contains["sign"],
        "reading3_at_q0": bool(v21 >= 0 and v3 >= 0),
        "reading3_on_all_(1,oo)": all(i["sign"] >= 0 for i in iv) and all(
            s["sign"] >= 0 for s in sign_on_interval(c3)),
    }


def ser(o):
    if isinstance(o, dict):
        return {k: ser(v) for k, v in o.items()}
    if isinstance(o, list):
        return [ser(v) for v in o]
    if isinstance(o, mp.mpf):
        return mp.nstr(o, 25)
    return o


def main():
    q0 = Q_MP
    checks, out = {}, {"recipe": "preregistration.md (6b9dd5d172)", "q0": Q_50_DIGIT_STR}

    # C1: S+AVG with gluon reproduces the builder's chi_(2,1) at q0
    from pyhecke import atom as A
    h0 = q0 - 1 / q0
    chi21_basis = [mp.mpf(2), h0, h0, mp.mpf(-1), mp.mpf(-1), mp.mpf(0)]
    ok1 = True
    for nuc in ("p", "n"):
        nf = A.build_nucleon_nf_mp(list(QUARKS[nuc]), 60)
        b = sum(c * x for c, x in zip(nf, chi21_basis))
        mine = at_q0(chars(CORE + quark_letters(nuc, "S+", "AVG") + GLUON)[0], q0)
        ok1 &= abs(b - mine) < mp.mpf(10) ** -40
    checks["C1_SplusAVG_gluon_equals_builder"] = bool(ok1)

    # C2: at t = 0 all templates give the same element (matrix-level, not just characters)
    ok2 = True
    for nuc in ("p", "n"):
        for dress in ([], GLUON):
            mats = set()
            for _, s, r in templates():
                M = I2
                for g, c in CORE + quark_letters(nuc, s, r) + dress:
                    M = M * (R[g] + c * h * I2)
                mats.add(tuple(sp.simplify(M.subs(q, 1))))
            ok2 &= len(mats) == 1
    checks["C2_all_templates_equal_at_order_zero"] = bool(ok2)

    # C3: one-dimensional characters equal the product formulas
    ok3 = True
    for nuc in ("p", "n"):
        L = CORE + quark_letters(nuc, "S+", "AVG")
        _, c3, c111 = chars(L)
        p3 = sp.prod([q + c * h for _, c in L])
        p111 = sp.prod([-1 / q + c * h for _, c in L])
        ok3 &= sp.simplify(c3 - p3) == 0 and sp.simplify(c111 - p111) == 0
    checks["C3_one_dim_characters_are_products"] = bool(ok3)

    # primary and secondary tables
    for label, dress in (("primary_k0", []), ("secondary_gluon", GLUON)):
        tab = {}
        for name, s, r in templates():
            for nuc in ("p", "n"):
                tab[f"{nuc} {name}"] = analyse(CORE + quark_letters(nuc, s, r) + dress, q0)
                print(label, nuc, name, mp.nstr(tab[f"{nuc} {name}"]["chi21_at_q0"], 12),
                      "lead", tab[f"{nuc} {name}"]["chi21_leading_order"],
                      tab[f"{nuc} {name}"]["chi21_leading_sign"],
                      "partials", tab[f"{nuc} {name}"]["chi21_partial_sum_signs_at_q0"],
                      "R3(q0)", tab[f"{nuc} {name}"]["reading3_at_q0"],
                      "R3(1,oo)", tab[f"{nuc} {name}"]["reading3_on_all_(1,oo)"], flush=True)
        out[label] = tab

    # tertiary: joint template x placement at k = 0 (values at q0 + leading order only)
    joint, ok4 = {}, True
    for name, s, r in templates():
        for nuc in ("p", "n"):
            row = {}
            for pl in itertools.product((0, 1), repeat=3):
                c21, c3, _ = chars(CORE + quark_letters(nuc, s, r, list(pl)))
                v21 = at_q0(c21, q0)
                row["".join(map(str, pl))] = {"chi21_at_q0": v21,
                                              "chi21_leading": leading(series(c21)),
                                              "reading3_at_q0": bool(v21 >= 0 and at_q0(c3, q0) >= 0)}
            n_ok = sum(v["reading3_at_q0"] for v in row.values())
            joint[f"{nuc} {name}"] = {"feasible_of_8": n_ok, "placements": row}
            if name == "S+AVG":
                ok4 &= n_ok == 4
            print("joint", nuc, name, n_ok, "/8", flush=True)
    checks["C4_joint_SplusAVG_reproduces_corpus_4_of_8"] = bool(ok4)
    out["tertiary_joint_k0"] = joint
    out["checks"] = checks
    print(json.dumps(checks))
    (HERE / "results.json").write_text(json.dumps(ser(out), indent=1) + "\n")
    sys.exit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
