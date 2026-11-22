"""Exact level characters on H_3 for SIGNED braid words (sympy, q symbolic).

Same functional as exact_h3_level_chars.py (stage 7, commit 68ef4b266; lo=1, two-row shapes,
y(lam) = [l0-l1+1]_q/[2]_q^(l0+l1), Gelfand-Tsetlin basis), extended to inverse letters by the
Hecke relation sigma^2 = h sigma + 1, i.e. sigma^-1 = sigma - h.
A word is a list of (g, e): generator g in {0,1}, exponent e in {+1,-1}.
-- Ref: [leitner2026] bean qou-99qc
"""
import sympy as sp

q = sp.symbols("q", positive=True)
h = q - 1 / q


def qint(m):
    return sp.simplify((q**m - q**(-m)) / h)


def y(lam):
    lam = tuple(lam) + (0,) * (2 - len(lam))
    return qint(lam[0] - lam[1] + 1) / qint(2) ** (lam[0] + lam[1])


ROWS = {(3,): [(0, 0, 0)], (2, 1): [(0, 0, 1), (0, 1, 0)]}


def gen21(i):
    if i == 0:
        return sp.Matrix([[q, 0], [0, -1 / q]])
    a = -2
    d1 = h / (1 - q ** (-2 * a))
    d2 = h / (1 - q ** (2 * a))
    return sp.Matrix([[d1, 1], [d1 * d2 + 1, d2]])


def diag(word):
    M = sp.eye(2)
    t = sp.Integer(1)
    for g, e in word:
        G = gen21(g) if e > 0 else gen21(g) - h * sp.eye(2)
        M = M * G
        t = t * (q if e > 0 else 1 / q)
    return {(3,): [t], (2, 1): [sp.simplify(M[0, 0]), sp.simplify(M[1, 1])]}


def restricted(r, m):
    r1 = sum(r[:m])
    return (m - r1, r1) if r1 else (m,)


TWO_ROW = {1: [(1,)], 2: [(2,), (1, 1)], 3: [(3,), (2, 1)]}


def level_chars(word):
    d = diag(word)
    out = {}
    for m in (1, 2, 3):
        for mu in TWO_ROW[m]:
            acc = 0
            for lam, vals in d.items():
                s = sum(v for v, r in zip(vals, ROWS[lam]) if restricted(r, m) == mu)
                acc += y(lam) / y(mu) * s
            out[(m, mu)] = sp.factor(sp.simplify(acc))
    return out
