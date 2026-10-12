#!/usr/bin/env python3
"""Quark letters and gamma-gamma words in the Temperley-Lieb (Jones) basis of TL_3.

Recipe: preregistration.md (59fcf0d0594), committed before this was run.
Issue #7777, bean qou-ales. Measures only; adopts nothing; no data compared.
Exact over QQ(q) (sympy); no floats in any verdict.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
q = sp.Symbol("q", positive=True)
h = q - 1 / q
Q2 = q + 1 / q                       # [2]_q
C = 1 / Q2**2                        # e0 e1 e0 = C e0

BASIS = [(), (0,), (1,), (0, 1), (1, 0)]


def reduce_word(w):
    """Reduce a word in e0, e1 to (coef, basis word)."""
    w, c = list(w), sp.Integer(1)
    changed = True
    while changed:
        changed = False
        for i in range(len(w) - 1):
            if w[i] == w[i + 1]:
                del w[i + 1]
                changed = True
                break
        else:
            for i in range(len(w) - 2):
                if w[i] == w[i + 2] != w[i + 1]:
                    del w[i + 1:i + 3]
                    c *= C
                    changed = True
                    break
    return c, tuple(w)


def mul(x, y):
    out = {}
    for a, ca in x.items():
        for b, cb in y.items():
            c, w = reduce_word(a + b)
            out[w] = sp.cancel(out.get(w, 0) + c * ca * cb)
    return {w: c for w, c in out.items() if c != 0}


def add(x, y, s=1):
    out = dict(x)
    for w, c in y.items():
        out[w] = sp.cancel(out.get(w, 0) + s * c)
    return {w: c for w, c in out.items() if c != 0}


ONE = {(): sp.Integer(1)}


def E(i):
    return {(i,): sp.Integer(1)}


def sigma(i, e=1):
    """sigma_i = q - [2] e_i ; sigma_i^-1 = q^-1 - [2] e_i."""
    return {(): q if e == 1 else 1 / q, (i,): -Q2}


def letter(g, c):
    """Template letter sigma_g + c*h (c = shift)."""
    return add(sigma(g), {(): c * h})


def prod(elts):
    x = ONE
    for y in elts:
        x = mul(x, y)
    return x


# --- representations of TL_3 on the y > 0 blocks (from #7718's rho) -----------
R2 = {0: -sp.Matrix([[-q**2, 1], [0, 1]]) / q, 1: -sp.Matrix([[1, 0], [q**2, -q**2]]) / q}
E2 = {i: sp.simplify((q * sp.eye(2) - R2[i]) / Q2) for i in (0, 1)}


def chars(x):
    c3 = sp.cancel(x.get((), 0))                    # (3): sigma -> q, so e -> 0
    M = sp.zeros(2)
    for w, c in x.items():
        P = sp.eye(2)
        for i in w:
            P = P * E2[i]
        M += c * P
    return sp.factor(sp.cancel(M.trace())), sp.factor(c3)


def show(x):
    names = {(): "1", (0,): "e0", (1,): "e1", (0, 1): "e0e1", (1, 0): "e1e0"}
    return {names[w]: str(sp.factor(x.get(w, 0))) for w in BASIS}


NAMES = {(): "1", (0,): "e0", (1,): "e1", (0, 1): "e0e1", (1, 0): "e1e0"}


def at_q1(x):
    return {NAMES[w]: str(sp.cancel(x.get(w, 0)).subs(q, 1)) for w in BASIS}


# --- template data, identical to computations/probes/quark_template ----------
QUARKS = {"p": "uud", "n": "udd"}
PAIRS = [(0, 1), (0, 2), (1, 2)]
PLACEMENT = [0, 0, 1]
SIGNS = {"S+": {"u": 1, "d": -1}, "S-": {"u": -1, "d": 1}, "S0": {"u": 1, "d": 1}, "S1": {"u": -1, "d": -1}}


def shift(rule, ea, eb):
    if rule == "AVG":
        return sp.Rational(ea + eb - 2, 4)
    e = ea if rule == "LO" else eb
    return sp.Rational(e - 1, 2)


def templates():
    for s in ("S0", "S1"):
        yield s, s, "AVG"
    for s in ("S+", "S-"):
        for r in ("AVG", "LO", "HI"):
            yield f"{s}{r}", s, r


def main():
    checks = {}
    # T1 Hecke + braid in TL_3
    ok = True
    for i in (0, 1):
        s = sigma(i)
        ok &= add(mul(s, s), add({(): sp.Integer(1)}, {w: h * c for w, c in s.items()}), -1) == {}
        ok &= add(mul(s, sigma(i, -1)), ONE, -1) == {}
    ok &= add(prod([sigma(0), sigma(1), sigma(0)]), prod([sigma(1), sigma(0), sigma(1)]), -1) == {}
    for i in (0, 1):
        ok &= sp.simplify(E2[i] * E2[i] - E2[i]) == sp.zeros(2)
    ok &= sp.simplify(E2[0] * E2[1] * E2[0] - C * E2[0]) == sp.zeros(2)
    checks["T1_hecke_braid_in_TL3"] = bool(ok)
    # T2 bar fixes e_i: q^-1 - sigma_i^-1 = [2] e_i
    ok = all(add(add({(): 1 / q}, sigma(i, -1), -1), {(i,): Q2}, -1) == {} for i in (0, 1))
    checks["T2_bar_fixes_e"] = bool(ok)

    out = {"letters": {}, "gg_words": {}, "nucleons": {}}
    # letters
    for name, sgn, rule in templates():
        for a, b in [("u", "u"), ("u", "d"), ("d", "d")]:
            c = shift(rule, SIGNS[sgn][a], SIGNS[sgn][b])
            x = letter(0, c)
            out["letters"][f"{name} {a}{b}"] = {"through": str(sp.factor(x.get((), 0))),
                                                "e_coeff": str(sp.factor(x.get((0,), 0)))}
    e_coeffs = {v["e_coeff"] for v in out["letters"].values()}
    out["letter_e_coefficient_set"] = sorted(e_coeffs)
    # gg words
    V = prod([sigma(0), sigma(1, -1)])
    U = prod([sigma(0), sigma(1)])
    for nm, base in (("V", V), ("U", U)):
        x = ONE
        for k in range(1, 7):
            x = mul(x, base)
            out["gg_words"][f"{nm}^{k}"] = {"coeffs": show(x), "at_q1": at_q1(x)}
    # nucleons
    ref = json.loads((ROOT / "computations/probes/quark_template/results.json").read_text())["primary_k0"]
    ok3 = True
    core = prod([V, V, V])
    for name, sgn, rule in templates():
        for nuc, qs in QUARKS.items():
            lets = [letter(g, shift(rule, SIGNS[sgn][qs[a]], SIGNS[sgn][qs[b]]))
                    for (a, b), g in zip(PAIRS, PLACEMENT)]
            x = prod([core] + lets)
            c21, c3 = chars(x)
            r = ref[f"{nuc} {name}"]
            ok3 &= sp.simplify(c21 - sp.sympify(r["chi21"], locals={"q": q})) == 0
            ok3 &= sp.simplify(c3 - sp.sympify(r["chi3"], locals={"q": q})) == 0
            out["nucleons"][f"{nuc} {name}"] = {"coeffs": show(x), "at_q1": at_q1(x),
                                                "chi21": str(c21), "chi3": str(c3)}
    checks["T3_reproduces_7718"] = bool(ok3)
    # where S+ and S- nucleons differ, per basis element (AVG rule)
    diff = {}
    for nuc in QUARKS:
        a, b = out["nucleons"][f"{nuc} S+AVG"]["coeffs"], out["nucleons"][f"{nuc} S-AVG"]["coeffs"]
        diff[nuc] = {k: str(sp.factor(sp.sympify(a[k], locals={"q": q}) - sp.sympify(b[k], locals={"q": q})))
                     for k in a}
    out["Splus_minus_Sminus_AVG"] = diff
    out["checks"] = checks
    out["recipe"] = "computations/probes/gg_quark_letters_tl/preregistration.md (59fcf0d0594)"
    out["issue"] = 7777
    (HERE / "gg-quark-letters-tl.witness.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps({"checks": checks, "letter_e_coefficient_set": out["letter_e_coefficient_set"],
                      "V": out["gg_words"]["V^1"], "V3": out["gg_words"]["V^3"],
                      "Splus_minus_Sminus_AVG": diff}, indent=1, ensure_ascii=False))
    sys.exit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
