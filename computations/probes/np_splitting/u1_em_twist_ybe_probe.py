#!/usr/bin/env python3
"""Can a U(1)_em charge phase be put on the Jimbo braiding without breaking Yang-Baxter?

Ansatz: R' = R * diag(a, b, b, c) on two sites (basis uu, ud, du, dd), the most general
weight-diagonal phase symmetric in the two strands. A U(1) charge line coupling t^{9 Q Q'} with
Q_u = 2/3, Q_d = -1/3 gives (a, b, c) = (t^4, t^-2, t^1).
Solves R'_12 R'_23 R'_12 = R'_23 R'_12 R'_23 symbolically in q, a, b, c (sympy, exact).
"""
import sympy as sp

q, a, b, c, t = sp.symbols("q a b c t", nonzero=True)
h = q - 1 / q
R = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]]) * sp.diag(a, b, b, c)
I2 = sp.eye(2)
R12, R23 = sp.kronecker_product(R, I2), sp.kronecker_product(I2, R)
E = (R12 * R23 * R12 - R23 * R12 * R23).applyfunc(sp.simplify)
eqs = sorted({sp.factor(e) for e in E if e != 0}, key=str)
print("independent YBE obstructions:", eqs)
print("solutions (a, b, c):", sp.solve(eqs, [a, b, c], dict=True))
sub = {a: t**4, b: t**-2, c: t}
print("U(1)_em charge phase, obstructions:", [sp.factor(e.subs(sub)) for e in eqs])
w = sp.exp(2 * sp.pi * sp.I / 3)
print("at t = exp(2 pi i/3): (a, b, c) =", [sp.simplify(x.subs(t, w)) for x in (t**4, t**-2, t)], "(a scalar)")
# Hecke term removed (h -> 0 in the matrix): the charge phase is then allowed for every t
R0 = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, q]]) * sp.diag(t**4, t**-2, t**-2, t)
A, B = sp.kronecker_product(R0, I2), sp.kronecker_product(I2, R0)
print("h-term removed, charge phase satisfies YBE for all t:", (A * B * A - B * A * B).applyfunc(sp.simplify) == sp.zeros(8, 8))
