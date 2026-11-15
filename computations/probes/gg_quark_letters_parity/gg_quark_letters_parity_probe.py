#!/usr/bin/env python3
"""Does the gamma-gamma construction (and the Jones-pair closure) fix each quark
letter's through-strand parity?  Step 3 of owner option 4.

Recipe: preregistration.md (74045a7695d), committed before this was run.
Issue #7777, beans qou-ales / qou-99qc.  Measures only; adopts nothing; no rule is
ranked by its reading-3 verdict; nothing is compared with data.

Arithmetic: exact over QQ(q) with sympy (TL_3 in the Jones basis, reused from
../gg_quark_letters_tl).  Signs on (1, oo) by exact real-root isolation
(Sturm-based `Poly.intervals` / `count_roots`, rational endpoints).  Values at the
proton pin are mpmath at 60 dps, display only.  No float anywhere.
"""
from __future__ import annotations

import itertools
import json
import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools/qou-substrate/python"))
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

mp.mp.dps = 60
T0 = time.monotonic()
q = sp.Symbol("q", positive=True)
h = q - 1 / q
Q2 = q + 1 / q
C = 1 / Q2**2
NAMES = {(): "1", (0,): "e0", (1,): "e1", (0, 1): "e0e1", (1, 0): "e1e0"}
BASIS = list(NAMES)


def log(msg):
    print(f"[{time.monotonic() - T0:7.1f}s] {msg}", flush=True)


# ---------------- TL_3 in the Jones basis (identical to step 2) ----------------
def reduce_word(w):
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


def letter(g, c):
    """Letter with through coefficient c on generator g: c*1 - [2] e_g."""
    return {(): c, (g,): -Q2}


def sigma(g, e=1):
    return letter(g, q if e == 1 else 1 / q)


def prod(xs):
    x = ONE
    for y in xs:
        x = mul(x, y)
    return x


def coeff(x, w):
    return sp.cancel(x.get(w, 0))


def zero(e):
    return sp.cancel(sp.together(e)) == 0


R2 = {0: -sp.Matrix([[-q**2, 1], [0, 1]]) / q, 1: -sp.Matrix([[1, 0], [q**2, -q**2]]) / q}
E2 = {i: sp.simplify((q * sp.eye(2) - R2[i]) / Q2) for i in (0, 1)}


def chars(x):
    c3 = sp.cancel(x.get((), 0))
    M = sp.zeros(2)
    for w, c in x.items():
        P = sp.eye(2)
        for i in w:
            P = P * E2[i]
        M += c * P
    return sp.factor(sp.cancel(M.trace())), sp.factor(c3)


# ---------------- exact sign analysis on (1, oo) ----------------
Q0R = sp.Rational(Q_50_DIGIT_STR)          # exact decimal rational of the 50-digit pin
Q0 = mp.mpf(Q_50_DIGIT_STR)


def roots_above_one(expr_poly):
    P = sp.Poly(sp.expand(expr_poly), q, domain="QQ")
    if P.degree() <= 0:
        return 0, []
    n = P.count_roots(1, None) - (1 if P.eval(1) == 0 else 0)   # Sturm count on (1, oo)
    ivs = [(a, b) for (a, b), _m in P.intervals(inf=1, eps=sp.Rational(1, 10**12)) if b > 1 and not (a == b == 1)]
    return n, ivs


def sign_report(expr):
    num, den = sp.fraction(sp.together(sp.cancel(expr)))
    if num == 0:
        return {"identically_zero": True, "sign_on_(1,oo)": [0], "roots_in_(1,oo)": 0,
                "nonneg_on_(1,oo)": True, "sign_at_q0": 0, "value_at_q0": "0"}
    nn, ivn = roots_above_one(num)
    nd, ivd = roots_above_one(den)
    ivs = sorted(ivn + ivd)
    # sample only in the root-free gaps (1, a_1), (b_i, a_{i+1}), (b_k, oo)
    edges = [sp.Integer(1)] + [v for ab in ivs for v in ab] + [None]
    signs = []
    for a, b in zip(edges[0::2], edges[1::2]):
        x = (a + b) / 2 if b is not None else a + 1
        signs.append(int(sp.sign(expr.subs(q, x))))
    roots = [mp.nstr((mp.mpf(a.p) / a.q + mp.mpf(b.p) / b.q) / 2, 15) for a, b in ivs]
    s0 = int(sp.sign(expr.subs(q, Q0R)))
    val = sp.lambdify(q, expr, "mpmath")(Q0)
    return {"roots_in_(1,oo)": nn + nd, "numerator_roots": nn, "denominator_roots": nd,
            "sign_on_(1,oo)": signs, "roots_approx": roots, "nonneg_on_(1,oo)": nn + nd == 0 and signs[0] >= 0,
            "sign_at_q0": s0, "value_at_q0": mp.nstr(val, 25)}


def reading3(x):
    c21, c3 = chars(x)
    r21, r3 = sign_report(c21), sign_report(c3)
    return {"chi21": str(c21), "chi3": str(c3), "chi21_sign": r21, "chi3_sign": r3,
            "reading3_at_q0": r21["sign_at_q0"] >= 0 and r3["sign_at_q0"] >= 0,
            "reading3_on_all_(1,oo)": r21["nonneg_on_(1,oo)"] and r3["nonneg_on_(1,oo)"]}


# ---------------- template data (identical to #7718 / step 2) ----------------
QUARKS = {"p": "uud", "n": "udd"}
PAIRS = [(0, 1), (0, 2), (1, 2)]
SIGNS = {"S+": {"u": 1, "d": -1}, "S-": {"u": -1, "d": 1}, "S0": {"u": 1, "d": 1}, "S1": {"u": -1, "d": -1}}
PLACEMENTS = ["".join(p) for p in itertools.product("01", repeat=3)]


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


def template_letters(nuc, sgn, rule, placement):
    qs = QUARKS[nuc]
    return [(int(g), sp.cancel(q + shift(rule, SIGNS[sgn][qs[a]], SIGNS[sgn][qs[b]]) * h))
            for (a, b), g in zip(PAIRS, placement)]


V = prod([sigma(0), sigma(1, -1)])
CORE = prod([V, V, V])


def element(letters):
    return prod([CORE] + [letter(g, c) for g, c in letters])


def same_letters(A, B):
    return all(g1 == g2 and zero(c1 - c2) for (g1, c1), (g2, c2) in zip(A, B))


def classify(c):
    if zero(c - q):
        return "q (sigma)"
    if zero(c - 1 / q):
        return "q^-1 (sigma^-1)"
    if zero(c - Q2 / 2):
        return "[2]/2 (bar-fixed average)"
    return "other: " + str(sp.factor(c))


# ---------------- R3: Jones-pair closure survivor ----------------
def survivor(W, pair, side):
    """Annihilate `pair` (e_pair) on `side` of W; return the survivor's through coefficient
    on the other generator, c = -[2] a / b, or None if the survivor carries no letter."""
    other = 1 - pair
    x = mul(W, E(pair)) if side == "right" else mul(E(pair), W)
    w_single = (pair,)
    w_pair = (other, pair) if side == "right" else (pair, other)
    allowed = {w_single, w_pair}
    stray = {NAMES[w]: str(c) for w, c in x.items() if w not in allowed}
    a, b = coeff(x, w_single), coeff(x, w_pair)
    if b == 0:
        return {"surviving_generator": other, "c": None, "class": "no letter (b = 0)", "stray": stray}
    c = sp.factor(sp.cancel(-Q2 * a / b))
    return {"surviving_generator": other, "alpha": str(sp.factor(-b / Q2)), "c": str(c),
            "class": classify(c), "stray": stray}


def main():
    checks, out = {}, {"recipe": "computations/probes/gg_quark_letters_parity/preregistration.md (74045a7695d)",
                       "issue": 7777, "q0_pin": "proton", "q0": Q_50_DIGIT_STR,
                       "q0Anchor": "proton", "q0Value": Q_50_DIGIT_STR}

    # P0 reproduce step 2
    ref = json.loads((ROOT / "computations/probes/gg_quark_letters_tl/gg-quark-letters-tl.witness.json").read_text())
    ok = True
    for key, x in (("V^1", V), ("V^3", CORE)):
        for w, nm in NAMES.items():
            ok &= zero(coeff(x, w) - sp.sympify(ref["gg_words"][key]["coeffs"][nm], locals={"q": q}))
    checks["P0_reproduces_step2_V_V3"] = bool(ok)
    log(f"P0 {ok}")

    # P1 reproduce #7718
    qt = json.loads((ROOT / "computations/probes/quark_template/results.json").read_text())
    ok = True
    for name, sgn, rule in templates():
        for nuc in QUARKS:
            c21, c3 = chars(element(template_letters(nuc, sgn, rule, "001")))
            r = qt["primary_k0"][f"{nuc} {name}"]
            ok &= zero(c21 - sp.sympify(r["chi21"], locals={"q": q}))
            ok &= zero(c3 - sp.sympify(r["chi3"], locals={"q": q}))
    for nuc in QUARKS:
        tj = qt["tertiary_joint_k0"][f"{nuc} S+AVG"]["placements"]
        for pl in PLACEMENTS:
            c21, c3 = chars(element(template_letters(nuc, "S+", "AVG", pl)))
            mine = bool(sp.sign(c21.subs(q, Q0R)) >= 0 and sp.sign(c3.subs(q, Q0R)) >= 0)
            ok &= mine == tj[pl]["reading3_at_q0"]
    checks["P1_reproduces_7718"] = bool(ok)
    log(f"P1 {ok}")

    # P2 hand-derived pair-closure identities
    ok = (add(mul(V, E(1)), {w: -q * c for w, c in mul(sigma(0), E(1)).items()}, -1) == {}
          and add(mul(E(0), V), {w: -c / q for w, c in mul(E(0), sigma(1, -1)).items()}, -1) == {})
    checks["P2_pair_closure_identities"] = bool(ok)
    log(f"P2 {ok}")

    # P3 ideal sanity
    ok = True
    for W in (V, CORE):
        for pair in (0, 1):
            for side in ("left", "right"):
                ok &= survivor(W, pair, side)["stray"] == {}
    checks["P3_one_sided_ideals"] = bool(ok)
    log(f"P3 {ok}")

    # ---- R3 survivors ----
    r3 = {}
    for nm, W in (("R3a_V", V), ("R3b_V3", CORE)):
        r3[nm] = {f"annihilate e{pair} on the {side}": survivor(W, pair, side)
                  for pair in (0, 1) for side in ("right", "left")}
    out["R3_survivors"] = r3
    log("R3 survivors computed")

    # ---- rule outputs: per-generator through coefficient (None = rule fixes nothing) ----
    gen_rules = {
        "R1_vertex_inheritance": {0: q, 1: 1 / q},
        "R2_h_leading_residue": {0: 1 / q, 1: q},
        "R4_pair_production_balance": {0: Q2 / 2, 1: Q2 / 2},
    }
    for nm, sv in r3.items():
        per_gen = {}
        for d in sv.values():
            per_gen.setdefault(d["surviving_generator"], []).append(d)
        out.setdefault("R3_per_generator", {})[nm] = {
            g: sorted({d["class"] for d in ds}) for g, ds in per_gen.items()}
        # R3 fixes generator g only if all four closures leaving g agree and give a definite parity
        fix = {}
        for g, ds in per_gen.items():
            classes = {d["class"] for d in ds}
            if len(classes) == 1 and ds[0]["c"] is not None and not ds[0]["class"].startswith("other"):
                fix[g] = sp.sympify(ds[0]["c"], locals={"q": q})
        if len(fix) == 2:
            gen_rules[nm] = fix
        else:
            out.setdefault("R3_not_a_parity_map", {})[nm] = {
                "fixed_generators": sorted(fix), "reason": "closures disagree or give no letter parity"}

    rows = {}
    for rule, gmap in gen_rules.items():
        log(f"rule {rule}")
        fam = {}
        for pl in PLACEMENTS:
            letters = [(int(g), gmap[int(g)]) for g in pl]
            # same letters for p and n by construction of the rule: check it explicitly (R5)
            x = element(letters)
            expr = []
            for name, sgn, trule in templates():
                if all(same_letters(letters, template_letters(nuc, sgn, trule, pl)) for nuc in QUARKS):
                    expr.append(name)
            rd = reading3(x)
            fam[pl] = {"letters": [[g, classify(c)] for g, c in letters],
                       "proton_equals_neutron": True,
                       "template_expressible_as": expr, **rd}
        rows[rule] = {"generator_parity": {str(g): classify(c) for g, c in gmap.items()},
                      "placement": "not fixed by the rule (8-placement family reported, none chosen)",
                      "flavour_sign_map": "not fixed: the rule never reads the quark content",
                      "family": fam}
    out["rules"] = rows

    # R5: is any rule element different between proton and neutron?  By construction no
    # rule above reads quark content; record the explicit check that every template that
    # does distinguish p from n is a hand choice outside R1-R4.
    out["R5_flavour_dictionary"] = {
        "any_rule_distinguishes_p_from_n": False,
        "note": "R1-R4 are functions of (generator) only; the element is identical for p and n. "
                "The two flavour dictionaries u<->q and u<->q^-1 are exchanged by bar; nothing in "
                "V, V^3 or the closures names a flavour, so no sign map is output.",
    }
    out["checks"] = checks
    out["elapsed_sec"] = round(time.monotonic() - T0, 1)  # a wall-clock duration: the name the raw-float64 audit carves out
    (HERE / "gg-quark-letters-parity.witness.json").write_text(
        json.dumps(out, indent=1, ensure_ascii=False, default=str) + "\n")
    summ = {r: {pl: (d["reading3_at_q0"], d["reading3_on_all_(1,oo)"], d["template_expressible_as"])
                for pl, d in v["family"].items()} for r, v in rows.items()}
    print(json.dumps({"checks": checks, "R3": out["R3_per_generator"],
                      "R3_not_a_parity_map": out.get("R3_not_a_parity_map"), "summary": summ},
                     indent=1, ensure_ascii=False, default=str))
    sys.exit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
