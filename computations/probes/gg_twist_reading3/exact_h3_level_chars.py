"""Exact level characters on H_3 (sympy, q symbolic): the same functional as h2_gg_atom_probe.level_chars
(lo=1, two-row shapes, y(lam) = [l0-l1+1]_q/[2]_q^(l0+l1)), in a Gelfand-Tsetlin (seminormal) basis.
Diagonal entries in a GT basis do not depend on how each basis vector is scaled, so they agree with the
mpmath engine's; this is checked numerically in the stage-7 probe before being used.
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


# (2,1): T1 = [[1,2],[3]] rows (0,0,1), contents 0,1,-1 ; T2 = [[1,3],[2]] rows (0,1,0), contents 0,-1,1
ROWS = {(3,): [(0, 0, 0)], (2, 1): [(0, 0, 1), (0, 1, 0)]}


def gen21(i):
    if i == 0:    # entries 1,2: same row in T1, same column in T2
        return sp.Matrix([[q, 0], [0, -1 / q]])
    a = -2       # axial distance c(3)-c(2) in T1 = -1-1
    d1 = h / (1 - q ** (-2 * a))
    d2 = h / (1 - q ** (2 * a))
    return sp.Matrix([[d1, 1], [d1 * d2 + 1, d2]])


def diag(gens):
    M = sp.eye(2)
    for g in gens:
        M = M * gen21(g)
    return {(3,): [q ** len(gens)], (2, 1): [sp.simplify(M[0, 0]), sp.simplify(M[1, 1])]}


def restricted(r, m):
    r1 = sum(r[:m])
    return (m - r1, r1) if r1 else (m,)


TWO_ROW = {1: [(1,)], 2: [(2,), (1, 1)], 3: [(3,), (2, 1)]}


def level_chars(gens):
    d = diag(gens)
    out = {}
    for m in (1, 2, 3):
        for mu in TWO_ROW[m]:
            acc = 0
            for lam, vals in d.items():
                s = sum(v for v, r in zip(vals, ROWS[lam]) if restricted(r, m) == mu)
                acc += y(lam) / y(mu) * s
            out[(m, mu)] = sp.factor(sp.simplify(acc))
    return out
