#!/usr/bin/env python3
"""Helon battery on position colour K0 (issue #9096).

Pre-registration: PREREG.md in this directory (pushed before this file).

Bilson-Thompson 2005 helon fermions (library/arxiv-hep-ph-0503213v2) encoded as framed
B3 braids (beta, t), t the per-strand twist datum of strand-twist-datum.md, and tested
against: the twist charge Q = T/3, the crossing charge (half writhe), K0 position colour
(PR #9059), the convention-D residual symmetry K_D = diag(q^-3, q^-1, 0), the radical of
the convention-D trace form on H3(q), and the corpus rulings (electron s0 s1 s0 with Hopf
closure; up quark = unknot strand; photon 1 + p0 s0 + p1 s1 + p01 s0 s1^-1).

Exact sympy over Q(q) / Q(t). No float. q0 is not used. No gluon is identified.
Exit status 0 always; FAILs are results, recorded in the witness.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import os
import sys
from fractions import Fraction

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
q = sp.symbols("q", positive=True)
h = q - 1 / q
zD = q**3 / (q**2 + 1)

CHECKS = []


def check(cid, ok, detail, expected=None):
    CHECKS.append({"id": cid, "pass": bool(ok), "expected_pass": expected, "detail": detail})
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {cid}: {detail}")


# ---------------------------------------------------------------- braid words
# a word is a tuple of (i, e), i in {0,1}, e = +1 / -1, read top to bottom.
def inv(w):
    return tuple((i, -e) for (i, e) in reversed(w))


def Pmirror(w, n=3):  # left-right mirror: s_i -> s_{n-2-i}^{-1}
    return tuple((n - 2 - i, -e) for (i, e) in w)


def perm(w, n=3):
    """pi[top position] = bottom position of that strand."""
    pos = list(range(n))  # pos[strand] = current position; strand label = top position
    for (i, _e) in w:
        for s in range(n):
            if pos[s] == i:
                pos[s] = i + 1
            elif pos[s] == i + 1:
                pos[s] = i
    return tuple(pos)


def cycles(p):
    seen, cyc = set(), []
    for a in range(len(p)):
        if a in seen:
            continue
        c, x = [], a
        while x not in seen:
            seen.add(x)
            c.append(x)
            x = p[x]
        cyc.append(tuple(c))
    return cyc


def writhe(w):
    return sum(e for (_i, e) in w)


def wstr(w):
    return " ".join(f"s{i}" + ("" if e == 1 else "^-1") for (i, e) in w) or "1"


# reduced Burau of B3 (faithful on B3), exact over Q(t)
t_ = sp.symbols("t")
BUR = {
    0: sp.Matrix([[-t_, 1], [0, 1]]),
    1: sp.Matrix([[1, 0], [t_, -t_]]),
}


def burau(w):
    M = sp.eye(2)
    for (i, e) in w:
        M = M * (BUR[i] if e == 1 else BUR[i].inv())
    return M.applyfunc(sp.simplify)


def braid_eq(w1, w2):
    return (burau(w1) - burau(w2)).applyfunc(sp.simplify) == sp.zeros(2)


# ---------------------------------------------------------------- Hecke H3(q)
S3 = list(itertools.permutations(range(3)))


def length(p):
    return sum(1 for a in range(3) for b in range(a + 1, 3) if p[a] > p[b])


def rmul_s(p, i):  # p * s_i as functions on positions: (p s)(x) = p(s(x))
    s = list(range(3))
    s[i], s[i + 1] = s[i + 1], s[i]
    return tuple(p[s[x]] for x in range(3))


def h_rmul_gen(el, i, e):
    out = {}
    for p, c in el.items():
        ps = rmul_s(p, i)
        if length(ps) > length(p):
            terms = {ps: 1}
        else:
            terms = {p: h, ps: 1}
        if e == -1:  # s^-1 = s - h
            terms = dict(terms)
            terms[p] = terms.get(p, 0) - h
        for k, v in terms.items():
            out[k] = sp.simplify(out.get(k, 0) + c * v)
    return {k: v for k, v in out.items() if v != 0}


def rho(w):
    el = {tuple(range(3)): sp.Integer(1)}
    for (i, e) in w:
        el = h_rmul_gen(el, i, e)
    return el


def hmul(a, b):
    """a*b via expressing b's basis elements by reduced words."""
    out = {}
    for pb, cb in b.items():
        word = reduced_word(pb)
        el = dict(a)
        for i in word:
            el = h_rmul_gen(el, i, 1)
        for k, v in el.items():
            out[k] = sp.simplify(out.get(k, 0) + cb * v)
    return {k: v for k, v in out.items() if v != 0}


def reduced_word(p):
    word, cur = [], tuple(range(3))
    target = p
    # greedy: build from identity by right multiplication increasing length
    for _ in range(3):
        if cur == target:
            break
        for i in (0, 1):
            nxt = rmul_s(cur, i)
            if length(nxt) == length(cur) + 1 and length(_div(target, nxt)) == length(target) - length(nxt):
                cur = nxt
                word.append(i)
                break
    assert cur == target, (p, word)
    return word


def _div(a, b):  # b^-1 a
    binv = [0] * 3
    for x in range(3):
        binv[b[x]] = x
    return tuple(binv[a[x]] for x in range(3))


def tr_basis(p, z):
    L = length(p)
    return {0: sp.Integer(1), 1: z, 2: z**2, 3: z * (h * z + 1)}[L]


def trD(el, z=zD):
    return sp.simplify(sum(c * tr_basis(p, z) for p, c in el.items()))


def sign_char(w):
    v = sp.Integer(1)
    for (_i, e) in w:
        v *= (-1 / q) if e == 1 else (-1 / q - h)
    return sp.simplify(v)


# ---------------------------------------------------------------- helon data (BT 2005)
b = ((0, 1), (1, -1))        # BT Fig. 1 e+ (left panel), left-over convention
Pb = Pmirror(b)
HELON = {"+": 1, "0": 0, "-": -1}
COL = {2: "B", 1: "G", 0: "R"}  # BT table: odd-man-out position 2 -> B, 1 -> G, 0 -> R


def colour_of(trip):
    vals = list(trip)
    for k in range(3):
        others = [vals[j] for j in range(3) if j != k]
        if others[0] == others[1] and vals[k] != others[0]:
            return k
    return None


def bt_quarks():
    """ordered triplets from BT 2005 Sec. 2 table, keyed (name, colour letter)."""
    rows = {
        "u": ["++0", "+0+", "0++"], "dbar": ["00+", "0+0", "+00"],
        "ubar": ["--0", "-0-", "0--"], "d": ["00-", "0-0", "-00"],
    }
    out = {}
    for name, trips in rows.items():
        for col, tr in zip("BGR", trips):
            out[(name, col)] = tuple(HELON[c] for c in tr)
    return out


SM_Q = {"e-": Fraction(-1), "e+": Fraction(1), "nu": Fraction(0), "nubar": Fraction(0),
        "u": Fraction(2, 3), "ubar": Fraction(-2, 3), "d": Fraction(-1, 3), "dbar": Fraction(1, 3)}

# battery: (name, colour, twist-triplet, braid, twisted end, handedness panel)
BAT = []
for (name, col), trip in bt_quarks().items():
    pos = name in ("u", "dbar")
    if pos:
        BAT.append((name, col, trip, b, "top", "left"))
        BAT.append((name, col, trip, Pb, "top", "right"))
    else:
        BAT.append((name, col, trip, inv(b), "bottom", "left"))
        BAT.append((name, col, trip, inv(Pb), "bottom", "right"))
BAT += [("e+", None, (1, 1, 1), b, "top", "left"), ("e+", None, (1, 1, 1), Pb, "top", "right"),
        ("e-", None, (-1, -1, -1), inv(b), "bottom", "left"), ("e-", None, (-1, -1, -1), inv(Pb), "bottom", "right"),
        ("nubar", None, (0, 0, 0), Pb, "top", "right"), ("nu", None, (0, 0, 0), inv(Pb), "bottom", "right")]


def at_other_end(trip, w, end):
    """move twist triplet (indexed by positions at `end`) to the other end."""
    p = perm(w)
    out = [None] * 3
    if end == "top":
        for k in range(3):
            out[p[k]] = trip[k]
    else:
        for k in range(3):
            out[k] = trip[p[k]]
    return tuple(out)


def main():
    rows = []
    # ---------------- H0
    reads = [b, inv(b), Pb, inv(Pb)]
    pis = [sorted(len(c) for c in cycles(perm(w))) for w in reads]
    trs = [trD(rho(w)) for w in reads]
    ok_conj = braid_eq(Pb, ((1, -1),) + b + ((1, 1),))
    ok = all(pp == [3] for pp in pis) and all(writhe(w) == 0 for w in reads) \
        and all(sp.simplify(x - trs[0]) == 0 for x in trs) and ok_conj
    check("H0a four readings one orbit (cycle type, writhe, tr_D, P(b) = s1^-1 b s1)", ok,
          f"words {[wstr(w) for w in reads]}, tr_D = {sp.factor(trs[0])}", True)
    prod = rho(b + inv(b))
    check("H0b b * C(b) = 1 in H3", prod == {tuple(range(3)): 1}, str(prod), True)

    # ---------------- H1, H2, H3
    h1 = h2 = 0
    h3_fail = 0
    for (name, col, trip, w, end, hand) in BAT:
        Qt = Fraction(sum(trip), 3)
        Qc = Fraction(writhe(w), 2)
        c_end = colour_of(trip)
        other = at_other_end(trip, w, end)
        c_other = colour_of(other)
        r = {"particle": name, "colour_BT": col, "handedness": hand, "word": wstr(w),
             "permutation": list(perm(w)), "writhe": writhe(w), "twist_at_twisted_end": list(trip),
             "twisted_end": end, "twist_at_other_end": list(other), "Q_twist": str(Qt),
             "Q_SM": str(SM_Q[name]), "Q_crossing_half_writhe": str(Qc),
             "H1_pass": Qt == SM_Q[name], "H2_pass": Qt == Qc}
        h1 += Qt == SM_Q[name]
        h2 += Qt == Qc
        if col is not None:
            r["colour_position_twisted_end"] = c_end
            r["colour_position_other_end"] = c_other
            r["colour_letter_twisted_end"] = COL[c_end]
            r["colour_letter_other_end"] = COL[c_other]
            r["H3_end_independent"] = c_end == c_other
            assert COL[c_end] == col, (name, col, c_end)
            h3_fail += c_end != c_other
        rows.append(r)
    n = len(BAT)
    check("H1 Q_twist = T/3 equals BT / SM charge", h1 == n, f"{h1}/{n}", True)
    h2_detail = {r["particle"]: r["H2_pass"] for r in rows}
    check("H2 Q_twist = Q_crossing (half writhe) for every fermion", h2 == n,
          f"{h2}/{n} pass; per particle {h2_detail}", False)
    nq = sum(1 for r in rows if r["colour_BT"])
    check("H3 K0 colour is end-independent", h3_fail == 0,
          f"{nq - h3_fail}/{nq} end-independent; pi(b) = {perm(b)} is a 3-cycle", False)

    # ---------------- H4  colour under C
    qk = bt_quarks()
    okC = 0
    for (pn, an) in (("u", "ubar"), ("dbar", "d")):
        for col in "BGR":
            # left panel: particle b twists top; C -> inv(b) twists bottom at same index
            okC += colour_of(qk[(pn, col)]) == colour_of(qk[(an, col)])
    check("H4 colour index at twisted end preserved by C (u_c -> ubar_c, dbar_c -> d_c)", okC == 6,
          f"{okC}/6 (by construction: C is a top-bottom reflection)", True)

    # ---------------- H5  proton charge equality under K0
    dB, uR, uG = qk[("d", "B")], qk[("u", "R")], qk[("u", "G")]
    h5 = []
    for dw, uw1, uw2 in itertools.product([inv(b), inv(Pb)], [b, Pb], [b, Pb]):
        d_top = at_other_end(dB, dw, "bottom")
        uR_bot, uG_bot = at_other_end(uR, uw1, "top"), at_other_end(uG, uw2, "top")
        top = [d_top[k] + uR[k] + uG[k] for k in range(3)]
        bot = [dB[k] + uR_bot[k] + uG_bot[k] for k in range(3)]
        naive = [dB[k] + uR[k] + uG[k] for k in range(3)]
        h5.append({"d": wstr(dw), "u_R": wstr(uw1), "u_G": wstr(uw2), "top_sums": top,
                   "bottom_sums": bot, "BT_mixed_end_sums": naive,
                   "top_equal": len(set(top)) == 1, "bottom_equal": len(set(bot)) == 1})
    same = [x for x in h5 if (x["u_R"] == x["u_G"]) and
            ((x["d"] == wstr(inv(b)) and x["u_R"] == wstr(b)) or (x["d"] == wstr(inv(Pb)) and x["u_R"] == wstr(Pb)))]
    check("H5(i) proton d_B+u_R+u_G, one panel: equal super-strand sums at both ends",
          all(x["top_equal"] and x["bottom_equal"] for x in same),
          "; ".join(f"[{x['d']}|{x['u_R']}|{x['u_G']}] top {x['top_sums']} bot {x['bottom_sums']}" for x in same), True)
    nboth = sum(1 for x in h5 if x["top_equal"] and x["bottom_equal"])
    check("H5(ii) all 8 handedness assignments: equal sums at both ends", nboth == 8,
          f"{nboth}/8; BT's own table sum (ends mixed) {h5[0]['BT_mixed_end_sums']}", None)
    # POST-HOC (not pre-registered): a twist slides along its strand, so read every
    # quark's table triplet at the TOP end, whatever end Fig. 1 draws it at.
    h5p = []
    for dw, uw1, uw2 in itertools.product([inv(b), inv(Pb)], [b, Pb], [b, Pb]):
        top = [dB[k] + uR[k] + uG[k] for k in range(3)]
        bots = [at_other_end(x, w, "top") for x, w in ((dB, dw), (uR, uw1), (uG, uw2))]
        bot = [sum(v[k] for v in bots) for k in range(3)]
        h5p.append({"d": wstr(dw), "u_R": wstr(uw1), "u_G": wstr(uw2), "top_sums": top,
                    "bottom_sums": bot, "top_equal": len(set(top)) == 1, "bottom_equal": len(set(bot)) == 1})
    ntop = sum(x["top_equal"] for x in h5p)
    nbot = sum(x["bottom_equal"] for x in h5p)
    check("H5-post (POST-HOC) all tables read at top: equal sums at top / at bottom", ntop == 8 and nbot == 8,
          f"top {ntop}/8, bottom {nbot}/8; bottom equal only when d shares u's permutation: "
          + "; ".join(f"[{x['d']}|{x['u_R']}|{x['u_G']}] bot {x['bottom_sums']}" for x in h5p), None)

    # ---------------- H6  D residual
    KD = sp.diag(q**-3, q**-1, 0)
    E1 = sp.Matrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]])
    F1 = E1.T
    K1, K2 = sp.diag(q, 1 / q, 1), sp.diag(1, q, 1 / q)
    N3 = sp.diag(0, 0, 1)
    gens = [E1, F1, K1, K2, K1.inv(), K2.inv(), N3]
    e = [sp.Matrix([1 if j == k else 0 for j in range(3)]) for k in range(3)]

    def orbit_span(v):
        span = [v]
        for _ in range(4):
            new = [g * x for g in gens for x in span]
            M = sp.Matrix.hstack(*(span + new))
            cols = M.columnspace()
            if len(cols) == len(span):
                break
            span = cols
        return sp.Matrix.hstack(*span).rank(), [list(c) for c in span]

    spans = {k: orbit_span(e[k]) for k in range(3)}
    rel12 = (E1 * e[1] == e[0]) and (F1 * e[0] == e[1])
    rel3 = spans[2][0] == 1 and all(c[0] == 0 and c[1] == 0 for c in spans[2][1])
    check("H6a all three colours related by residual U_q(gl2) x U(1)", not rel3,
          f"colour e3 orbit span = {spans[2][1]} (N3 = 1, D weight 0)", False)
    check("H6b colours 1,2 related by U_q(gl2) (E1 e2 = e1, F1 e1 = e2)", rel12, "", True)
    dvis = []
    for r in rows:
        if r["colour_BT"] is None:
            continue
        de, do = KD[r["colour_position_twisted_end"], r["colour_position_twisted_end"]], \
            KD[r["colour_position_other_end"], r["colour_position_other_end"]]
        r["D_weight_twisted_end"], r["D_weight_other_end"] = str(de), str(do)
        dvis.append((de != 0) == (do != 0))
    check("H6c D-visibility of a quark colour is end-independent", all(dvis),
          f"{sum(dvis)}/{len(dvis)} end-independent", False)
    Pc = sp.Matrix(3, 3, lambda i, j: 1 if perm(b)[j] == i else 0)
    check("H6d braid 3-cycle on colour labels commutes with K_D", (Pc * KD - KD * Pc) == sp.zeros(3),
          f"P K_D P^-1 = {list((Pc * KD * Pc.T).diagonal())}", False)

    # ---------------- H7  D radical
    G = sp.Matrix(6, 6, lambda i, j: trD(hmul({S3[i]: 1}, {S3[j]: 1})))
    G = G.applyfunc(sp.simplify)
    ns = G.nullspace()
    check("H7a radical of (x,y) -> tr_D(xy) on H3 has dimension 1", len(ns) == 1,
          f"dim {len(ns)}; det G = {sp.factor(G.det())}", True)
    r = ns[0]
    rel = {S3[i]: sp.simplify(r[i]) for i in range(6) if sp.simplify(r[i]) != 0}
    is_sign = all(
        all(sp.simplify(v - (-1 / q) * rel.get(p, 0)) == 0 for p, v in
            {**{p: 0 for p in S3}, **h_rmul_gen(rel, i, 1)}.items()) for i in (0, 1))
    check("H7a' radical vector spans the sign block (r s_i = -q^-1 r)", is_sign, str(rel), True)
    vb = sp.Matrix([rho(b).get(p, 0) for p in S3])
    inrad = (G * vb).applyfunc(sp.simplify) == sp.zeros(6, 1)
    check("H7b rho(b) lies in the D radical", inrad, "b invertible; radical a proper ideal", False)
    chi = sign_char(b)
    check("H7c sign character chi_(1^3)(b) = 1 (nonzero radical-block component)", sp.simplify(chi - 1) == 0,
          str(chi), True)
    tb = trD(rho(b))
    check("H7d tr_D(b) recorded", True, f"tr_D(s0 s1^-1) = {sp.factor(tb)} = z_D^2 - h z_D: "
          f"{sp.simplify(tb - (zD**2 - h * zD)) == 0}", True)

    # ---------------- H8  corpus electron
    el = ((0, 1), (1, 1), (0, 1))
    helon_e = [inv(b), inv(Pb)]
    eqs = [braid_eq(w, el) for w in helon_e]
    check("H8a helon electron word equals ruled electron s0 s1 s0 in B3", any(eqs),
          f"helon e- {[wstr(w) for w in helon_e]}: perm {[perm(w) for w in helon_e]} cycles "
          f"{[len(cycles(perm(w))) for w in helon_e]} writhe 0; ruled: perm {perm(el)} components "
          f"{len(cycles(perm(el)))} writhe {writhe(el)}", False)
    tr_el = trD(rho(el))
    check("H8b BT fermion criterion (non-identity permutation) on ruled electron s0 s1 s0",
          perm(el) != (0, 1, 2), f"perm {perm(el)}; tr_D = {sp.factor(tr_el)}", True)
    check("H8b' BT fermion criterion on trefoil backup s0^3 in B2", True,
          "permutation of s0^3 in B2 = transposition (odd exponent) -> non-identity", True)

    # ---------------- H9  up quark
    last_once = sum(1 for (i, _e) in b if i == 1) == 1
    check("H9a helon u closure: 1 component, Markov-destabilises s0 s1^-1 ~ s0 in B2 -> unknot T(2,1)",
          len(cycles(perm(b))) == 1 and last_once, "agrees with 'up quark is an unknot'", True)
    check("H9b level: helon u is a whole 3-strand triplet; ruled u is one strand of beta_Bor", False,
          "conflict of level, not of knot type", False)

    # ---------------- H10 composition reading
    b3 = b * 3
    V3 = ((0, 1), (1, -1)) * 3
    comps = cycles(perm(b3))

    def lk(w, A, B):  # pairwise linking number of components A, B of a pure braid closure
        pos = list(range(3))
        s = 0
        for (i, e) in w:
            a = [st for st in range(3) if pos[st] == i][0]
            c = [st for st in range(3) if pos[st] == i + 1][0]
            if {a, c} == {A, B}:
                s += e
            pos[a], pos[c] = i + 1, i
        return Fraction(s, 2)

    lks = {f"{A}{B}": str(lk(b3, A, B)) for A, B in ((0, 1), (0, 2), (1, 2))}
    check("H10 (coincidence, labelled in advance) b^3 = V^3 = beta_Bor; 3 components, pairwise lk 0",
          braid_eq(b3, V3) and len(comps) == 3 and all(v == "0" for v in lks.values()),
          f"components {comps}, lk {lks}; BT stacks in layers, NOT by composition", True)

    # ---------------- H11 photon terms
    terms = {"1": (), "s0": ((0, 1),), "s1": ((1, 1),), "s0 s1^-1": ((0, 1), (1, -1))}
    bos = {k: perm(w) == (0, 1, 2) for k, w in terms.items()}
    check("H11 only the '1' term of the ruled photon is a BT boson (identity permutation)",
          bos == {"1": True, "s0": False, "s1": False, "s0 s1^-1": False},
          f"{bos}; photon fourth term s0 s1^-1 == helon fermion braid b: {braid_eq(terms['s0 s1^-1'], b)}", True)

    npass = sum(c["pass"] for c in CHECKS)
    mism = [c["id"] for c in CHECKS if c["expected_pass"] is not None and c["pass"] != c["expected_pass"]]
    print(f"SUMMARY {npass}/{len(CHECKS)} pass; outcomes differing from pre-registered expectation: {mism}")
    src = open(__file__, "rb").read()
    wit = {
        "description": "Helon battery on K0 position colour (issue #9096). Exact sympy; no float; q0 unused.",
        "prereg": "computations/probes/qcd_helon_battery/PREREG.md",
        "source": "bilson-thompson2005 (library/arxiv-hep-ph-0503213v2) Sec. 2 table, Sec. 3, Fig. 1",
        "q0Anchor": "independent",
        "q0AnchorReason": "exact sympy over Q(q) and Q(t); q0 never read",
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "z_D": str(zD), "K_D": "diag(q^-3, q^-1, 0)",
        "helon_braid_b": wstr(b),
        "checks": CHECKS,
        "battery": rows,
        "proton_H5": h5, "proton_H5_posthoc_read_at_top": h5p,
        "D_radical_vector": {str(k): str(v) for k, v in rel.items()},
        "tr_D_b": str(sp.factor(tb)), "tr_D_electron_s0s1s0": str(sp.factor(tr_el)),
        "summary": {"pass": npass, "total": len(CHECKS), "differs_from_prereg_expectation": mism},
    }
    with open(os.path.join(HERE, "helon-battery.witness.json"), "w") as f:
        json.dump(wit, f, indent=1, ensure_ascii=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
