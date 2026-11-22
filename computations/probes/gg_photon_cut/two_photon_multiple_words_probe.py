#!/usr/bin/env python3
"""two_photon_multiple_words_probe.py — D1: which braid words are scalar multiples of a two-photon product?

Pre-registered in bean qou-99qc (PRE-REGISTRATION 2026-11-21 12:25Z) before this file was written.
Ruled photon gamma(phi) = 1 + phi0 s0 + phi1 s1 + phi01 s0 s1^-1 (#8583). In the regular representation of
H_3(q) over Q(q) (s^2 = h s + 1, s^-1 = s - h, h = q - 1/q; exact sympy, q symbolic), for every free-reduced
word w in s0^+-, s1^+- with 1..MAXC crossings, solve gamma(phi) gamma(psi) = c w, c != 0.
Question: is the phi01-psi01 sector (the V-only gamma-gamma grammar) forced by this element criterion?
Nothing is compared with measurement.
-- Ref: [leitner2026] bean qou-99qc; QEDHigherOrderCovariance.photon_product_eq_borWord
"""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

import sympy as sp

MAXC = int(sys.argv[1]) if len(sys.argv) > 1 else 6
q = sp.symbols("q", positive=True)
h = q - 1 / q
p0, p1, p01, s0_, s1_, s01, c = sp.symbols("phi0 phi1 phi01 psi0 psi1 psi01 c")
PERMS = list(itertools.permutations(range(3)))
ID = (0, 1, 2)


def length(w):
    return sum(1 for i in range(3) for j in range(i + 1, 3) if w[i] > w[j])


def compose(s, w):  # (s o w)(k) = s(w(k))
    return tuple(s[w[k]] for k in range(3))


GEN = {0: (1, 0, 2), 1: (0, 2, 1)}


def left_gen(i, Y):
    s, out = GEN[i], {}
    for w, a in Y.items():
        sw = compose(s, w)
        if length(sw) > length(w):
            out[sw] = out.get(sw, 0) + a
        else:
            out[w] = out.get(w, 0) + h * a
            out[sw] = out.get(sw, 0) + a
    return out


def left_letter(g, e, Y):
    Z = left_gen(g, Y)
    if e < 0:  # s^-1 = s - h
        for w, a in Y.items():
            Z[w] = Z.get(w, 0) - h * a
    return Z


def word_elem(word):
    Y = {ID: sp.Integer(1)}
    for g, e in reversed(word):
        Y = left_letter(g, e, Y)
    return Y


def add(*terms):
    out = {}
    for coef, Y in terms:
        for w, a in Y.items():
            out[w] = out.get(w, 0) + coef * a
    return out


def mul(X, Y):
    out = {}
    for w, a in X.items():
        # reduced word for w: T_w = product of generators; build by bubble sort
        Z = Y
        for g in reversed(reduced_word(w)):
            Z = left_gen(g, Z)
        for u, b in Z.items():
            out[u] = out.get(u, 0) + a * b
    return out


def reduced_word(w):
    # w = s_{a1} o ... o s_{ak}; find by repeatedly stripping a left descent
    res, cur = [], w
    while cur != ID:
        for i in (0, 1):
            sc = compose(GEN[i], cur)
            if length(sc) < length(cur):
                res.append(i)
                cur = sc
                break
    return res


V = [(0, 1), (1, -1)]


def photon(a0, a1, a01):
    return add((1, {ID: sp.Integer(1)}), (a0, word_elem([(0, 1)])), (a1, word_elem([(1, 1)])),
               (a01, word_elem(V)))


GG = mul(photon(p0, p1, p01), photon(s0_, s1_, s01))
UNK = [p0, p1, p01, s0_, s1_, s01, c]


def reduce_word(w):
    out = []
    for x in w:
        if out and out[-1][0] == x[0] and out[-1][1] == -x[1]:
            out.pop()
        else:
            out.append(x)
    return tuple(out)


def words(maxc):
    letters = [(0, 1), (0, -1), (1, 1), (1, -1)]
    seen = set()
    for n in range(1, maxc + 1):
        for t in itertools.product(letters, repeat=n):
            r = reduce_word(t)
            if len(r) == n:
                seen.add(r)
    return sorted(seen, key=lambda w: (len(w), w))


def components(w):
    p = [0, 1, 2]
    for g, _ in w:
        p[g], p[g + 1] = p[g + 1], p[g]
    seen, k = set(), 0
    for i in range(3):
        if i not in seen:
            k += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = p[j]
    return k


def show(w):
    return "".join(f"s{g}" + ("" if e > 0 else "^-1") for g, e in w)


def solve_word(w):
    W = word_elem(list(w))
    eqs = [sp.together(sp.expand(GG.get(u, 0) - c * W.get(u, 0))) for u in PERMS]
    eqs = [sp.numer(e) for e in eqs if e != 0]
    G = sp.groebner(eqs + [c * sp.Symbol("t") - 1], *UNK, sp.Symbol("t"), order="lex", domain=sp.QQ.frac_field(q))
    if list(G.exprs) == [1]:
        return None
    sols = sp.solve(list(G.exprs), UNK + [sp.Symbol("t")], dict=True)
    return [{str(k): str(sp.simplify(v)) for k, v in s.items() if str(k) != "t"} for s in sols] or ["positive-dimensional: " + str(G.exprs)]


def main():
    # control: the ruled identity in the full H_3
    lhs = mul(photon(0, 0, q * h), photon(0, 0, -h / q))
    rhs = word_elem(V * 3)
    ctrl = all(sp.simplify(lhs.get(u, 0) - rhs.get(u, 0)) == 0 for u in PERMS)
    print("control gamma(0,0,qh)gamma(0,0,-h/q) = V^3 in full H_3:", ctrl, flush=True)
    hits = []
    ws = words(MAXC)
    for i, w in enumerate(ws):
        r = solve_word(w)
        if r:
            row = {"word": show(w), "crossings": len(w), "writhe": sum(e for _, e in w),
                   "components": components(w), "solutions": r}
            hits.append(row)
            print(json.dumps(row), flush=True)
        if i % 50 == 0:
            print(f"  {i}/{len(ws)}", flush=True)
    out = {"max_crossings": MAXC, "words_tested": len(ws), "control_full_H3": ctrl, "hits": hits}
    Path(__file__).with_name("two-photon-multiple-words.json").write_text(json.dumps(out, indent=1))
    print("tested", len(ws), "hits", len(hits))


if __name__ == "__main__":
    main()
