#!/usr/bin/env python3
"""Tree-level QED: is gamma gamma -> e+ e- nonzero for PARALLEL linear polarizations?

Bean qou-qs2u, PR #7825 (owner D1 follow-up, item 3). The corpus's BW selection rule
(`mass-theory/breit-wheeler-vertex.md`) says the vertex vanishes for parallel
polarizations. This script checks that against tree-level QED, the comparison point.

Method: exact symbolic spin-summed |M|^2 = Tr[(p1/ + m) G (p2/ - m) Gbar] with explicit
Dirac matrices, real linear polarization vectors, and on-shell momenta with RATIONAL
components (m = 1, CM frame, photons along z, E = 5/4, |p| = 3/4). Exact rationals
throughout: no floats.

  M ~ ubar(p1) [ e2/ (p1/ - k1/ + m) e1/ / (t - m^2) + e1/ (p1/ - k2/ + m) e2/ / (u - m^2) ] v(p2)

The script's assertions are the gate.
"""
import sympy as sp
from itertools import product

I = sp.I
Z2 = sp.zeros(2)
E2 = sp.eye(2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -I], [I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])


def block(a, b, c, d):
    return sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))


g0 = block(E2, Z2, Z2, -E2)
gs = [block(Z2, s, -s, Z2) for s in (sx, sy, sz)]
G = [g0] + gs
metric = [1, -1, -1, -1]


def slash(p):  # p contravariant (p0, p1, p2, p3); p/ = g^mu p_mu
    return sum((metric[m] * p[m] * G[m] for m in range(4)), sp.zeros(4))


def dot(a, b):
    return sum(metric[m] * a[m] * b[m] for m in range(4))


m = sp.Integer(1)
E = sp.Rational(5, 4)
P = sp.Rational(3, 4)
k1 = [E, 0, 0, E]
k2 = [E, 0, 0, -E]


def msq(p1, e1, e2):
    p2 = [2 * E - p1[0]] + [-x for x in p1[1:]]
    assert dot(p1, p1) == m**2 and dot(p2, p2) == m**2
    t = dot([p1[i] - k1[i] for i in range(4)], [p1[i] - k1[i] for i in range(4)])
    u = dot([p1[i] - k2[i] for i in range(4)], [p1[i] - k2[i] for i in range(4)])
    one = sp.eye(4)
    Gm = (slash(e2) * (slash([p1[i] - k1[i] for i in range(4)]) + m * one) * slash(e1) / (t - m**2)
          + slash(e1) * (slash([p1[i] - k2[i] for i in range(4)]) + m * one) * slash(e2) / (u - m**2))
    Gbar = g0 * Gm.H * g0
    return sp.nsimplify(sp.simplify(((slash(p1) + m * one) * Gm * (slash(p2) - m * one) * Gbar).trace()))


ex = [0, 1, 0, 0]
ey = [0, 0, 1, 0]
# Electron directions with rational unit vectors (Pythagorean triples), |p| = 3/4.
dirs = {
    "along x-z (3/5,0,4/5)": (sp.Rational(3, 5), 0, sp.Rational(4, 5)),
    "along y-z (0,3/5,4/5)": (0, sp.Rational(3, 5), sp.Rational(4, 5)),
    "transverse (3/5,4/5,0)": (sp.Rational(3, 5), sp.Rational(4, 5), 0),
    "along z (0,0,1)": (0, 0, 1),
}
rows = []
for name, n in dirs.items():
    p1 = [E] + [P * x for x in n]
    par_xx = msq(p1, ex, ex)
    par_yy = msq(p1, ey, ey)
    perp_xy = msq(p1, ex, ey)
    rows.append((name, par_xx, par_yy, perp_xy))
    print(f"{name:26s}  |M|^2 par(x,x) = {par_xx}   par(y,y) = {par_yy}   perp(x,y) = {perp_xy}")

assert all(r[1] >= 0 and r[2] >= 0 and r[3] >= 0 for r in rows)
assert any(r[1] > 0 for r in rows), "parallel pair production vanishes at every point tested"
print("VERDICT: tree-level QED gives NONZERO pair production for parallel linear polarizations.")
