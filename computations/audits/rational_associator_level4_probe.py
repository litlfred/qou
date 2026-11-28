#!/usr/bin/env python3
"""Solve the degree-3 and degree-4 associator equations exactly over Q.

Audit docs/audits/2026-11-27-grt-action-pentagon-derivation.md section 17q.

Setting (matches QOU/BraidsAndKnots/RationalAssociator): U4 N is the four-strand
Drinfeld-Kohno algebra truncated at word length N; the exponential of level N is
expHalfTrunc N = sum_{k<N} X^k / (2^k k!). Phi in Q<X,Y> is an associator in U4 N if
  * Phi(a,b) Phi(b,a) = 1            (checked in the free algebra on a, b, truncated),
  * hexagon  E(t13+t23) = Phi(t13,t12) E(t13) Phi(t23,t13) E(t23) Phi(t12,t23),
  * pentagon Phi(t12,t23+t24) Phi(t13+t23,t34) = Phi(t23,t34) Phi(t12+t13,t24+t34) Phi(t12,t23).

Equations in U4 N are decided by an explicit rewriting system (the same eleven rules
used in ExplicitLevelFive.lean), which pushes t12,t13,t23 right of t14,t24,t34 and t23
right of t12,t13. Unknowns: all 2^d words of degree d (d = 3, then 4). Everything is
exact Fraction arithmetic; no float, no measured value, no fitting.

Output:
  level 4: Phi = 1 + [X,Y]/24 + alpha*([X,[X,Y]] + [Y,[X,Y]]), alpha free (rank 7 of 8).
  level 5: degree-4 part unique: [X,Y]^2/1152 - [X,[X,L]]/1440 - [Y,[X,L]]/5760
           - [Y,[Y,L]]/1440, L = [X,Y]; alpha still free.
  control: with the level-3 exponential, 1 + [X,Y]/24 fails the degree-3 hexagon.
"""
from fractions import Fraction as F
from itertools import product
import math

RULES = {'PA': {'AP': 1, 'AB': 1, 'BA': -1}, 'PB': {'BP': 1, 'BA': 1, 'AB': -1}, 'PC': {'CP': 1},
         'QA': {'AQ': 1, 'AC': 1, 'CA': -1}, 'QC': {'CQ': 1, 'CA': 1, 'AC': -1}, 'QB': {'BQ': 1},
         'RA': {'AR': 1}, 'RB': {'BR': 1, 'BC': 1, 'CB': -1}, 'RC': {'CR': 1, 'CB': 1, 'BC': -1},
         'RP': {'PR': 1, 'PQ': 1, 'QP': -1}, 'RQ': {'QR': 1, 'QP': 1, 'PQ': -1}}
# P=t12 Q=t13 R=t23 A=t14 B=t24 C=t34


class Alg:
    def __init__(self, N):
        self.N = N

    def mul(self, p, q):
        r = {}
        for a, x in p.items():
            for b, y in q.items():
                if len(a) + len(b) < self.N:
                    r[a + b] = r.get(a + b, 0) + x * y
        return {k: v for k, v in r.items() if v}


def add(*ps):
    r = {}
    for p in ps:
        for k, v in p.items():
            r[k] = r.get(k, 0) + v
    return {k: v for k, v in r.items() if v}


def sc(c, p):
    return {k: c * v for k, v in p.items()}


def nf(p):
    out, todo = {}, dict(p)
    while todo:
        w, c = todo.popitem()
        for i in range(len(w) - 1):
            if w[i:i + 2] in RULES:
                for r, cc in RULES[w[i:i + 2]].items():
                    nw = w[:i] + r + w[i + 2:]
                    todo[nw] = todo.get(nw, 0) + c * cc
                    if todo[nw] == 0:
                        del todo[nw]
                break
        else:
            out[w] = out.get(w, 0) + c
            if out[w] == 0:
                del out[w]
    return out


ONE = {'': F(1)}


def ev(A, poly, a, b):
    r = {}
    for w, c in poly.items():
        t = ONE
        for l in w:
            t = A.mul(t, a if l == 'X' else b)
        r = add(r, sc(c, t))
    return r


def exp_half(M):
    return {'X' * k: F(1, 2 ** k * math.factorial(k)) for k in range(M)}


def defects(A, Phi, E):
    g = lambda ch: {ch: F(1)}
    t12, t13, t23, t24, t34 = g('P'), g('Q'), g('R'), g('B'), g('C')
    m = A.mul
    hexd = add(ev(A, E, add(t13, t23), {}), sc(-1, m(m(m(m(ev(A, Phi, t13, t12), ev(A, E, t13, {})),
              ev(A, Phi, t23, t13)), ev(A, E, t23, {})), ev(A, Phi, t12, t23))))
    pent = add(m(m(ev(A, Phi, t23, t34), ev(A, Phi, add(t12, t13), add(t24, t34))), ev(A, Phi, t12, t23)),
               sc(-1, m(ev(A, Phi, t12, add(t23, t24)), ev(A, Phi, add(t13, t23), t34))))
    a, b = g('a'), g('b')
    inv = add(m(ev(A, Phi, a, b), ev(A, Phi, b, a)), sc(-1, ONE))
    return [nf(hexd), nf(pent), inv]


def solve(A, base_phi, E, d):
    words = [''.join(w) for w in product('XY', repeat=d)]
    b = defects(A, base_phi, E)
    cols = []
    for w in words:
        dd = defects(A, add(base_phi, {w: F(1)}), E)
        cols.append([add(x, sc(-1, y)) for x, y in zip(dd, b)])
    keys = sorted({(i, k) for i in range(3) for k in b[i]} |
                  {(i, k) for col in cols for i in range(3) for k in col[i]})
    rows = [[col[i].get(k, F(0)) for col in cols] + [-b[i].get(k, F(0))] for i, k in keys]
    n, piv, r = len(words), [], 0
    for c in range(n):
        pr = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if pr is None:
            continue
        rows[r], rows[pr] = rows[pr], rows[r]
        pv = rows[r][c]
        rows[r] = [x / pv for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]
                rows[i] = [x - f * y for x, y in zip(rows[i], rows[r])]
        piv.append(c)
        r += 1
    consistent = all(row[-1] == 0 for row in rows[r:])
    free = [words[c] for c in range(n) if c not in piv]
    part = {words[c]: rows[i][-1] for i, c in enumerate(piv) if rows[i][-1] != 0}
    null = {}
    for fw in free:
        fi = words.index(fw)
        null[fw] = {words[c]: -rows[i][fi] for i, c in enumerate(piv) if rows[i][fi] != 0}
    return consistent, r, part, null


def main():
    L = {'XY': F(1), 'YX': F(-1)}
    phi = add(ONE, sc(F(1, 24), L))
    ok = True
    # control: level-3 exponential fails at degree 3
    A4 = Alg(4)
    ctrl = defects(A4, phi, exp_half(3))[0]
    print('control (E3, degree-3 hexagon defect nonzero):', bool(ctrl))
    ok &= bool(ctrl)
    cons, rank, part, null = solve(A4, phi, exp_half(4), 3)
    print('level 4: consistent', cons, 'rank', rank, 'particular', part, 'kernel', null)
    ok &= cons and rank == 7 and part == {}
    A5 = Alg(5)
    cons5, rank5, part5, null5 = solve(A5, phi, exp_half(5), 4)
    print('level 5: consistent', cons5, 'rank', rank5, 'kernel', null5)
    m = A5.mul
    br = lambda p, q: add(m(p, q), sc(-1, m(q, p)))
    X, Y = {'X': F(1)}, {'Y': F(1)}
    expected = add(sc(F(1, 1152), m(L, L)), sc(F(-1, 1440), br(X, br(X, L))),
                   sc(F(-1, 5760), br(Y, br(X, L))), sc(F(-1, 1440), br(Y, br(Y, L))))
    print('level 5 degree-4 part equals the stated Lie form:', part5 == expected)
    ok &= cons5 and rank5 == 16 and part5 == expected and null5 == {}
    print('ALL CHECKS PASS' if ok else 'CHECK FAILED')
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
