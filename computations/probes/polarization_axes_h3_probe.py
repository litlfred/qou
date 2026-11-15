#!/usr/bin/env python3
"""Bloch angle between the eigen-axes of sigma_0 and sigma_1 in the (2,1) block of H_3.

Bean qou-qs2u, PR #7825. Solves the Hecke + braid relations for a symmetric sigma_1
against sigma_0 = diag(q, -1/q), and computes the Bloch z-coordinate of sigma_1's
q-eigenline relative to sigma_0's axis. Exact sympy; q is a positive real symbol.
The assertions are the gate.
"""
import sympy as sp

q = sp.symbols("q", positive=True)
a, b, d = sp.symbols("a b d")
S0 = sp.Matrix([[q, 0], [0, -1 / q]])
S1 = sp.Matrix([[a, b], [b, d]])
I2 = sp.eye(2)
eqs = list((S1 - q * I2) * (S1 + I2 / q)) + list(S0 * S1 * S0 - S1 * S0 * S1)
sols = [s for s in sp.solve(eqs, [a, b, d], dict=True) if s[b] != 0]
assert sols, "no non-diagonal symmetric sigma_1"
target = -(q**4 + 1) / (q**2 + 1) ** 2
for s in sols:
    M = S1.subs(s)
    for val, _, vecs in M.eigenvects():
        if sp.simplify(val - q) == 0:
            v = vecs[0]
            z = sp.simplify((v[0] ** 2 - v[1] ** 2) / (v[0] ** 2 + v[1] ** 2))
            print("sigma_1 =", sp.simplify(M).tolist())
            print("Bloch cos(angle between q-lines of sigma_0, sigma_1) =", z, "; at q=1:", z.subs(q, 1))
            assert sp.simplify(z - target) == 0
# Perpendicular (z=0) needs q^4+1=0; antipodal (z=-1) needs q=0: neither for real q > 0.
assert sp.solve(sp.Eq(target, 0), q) == [] and sp.solve(sp.Eq(target, -1), q) == []
print("PASS: axes neither perpendicular nor antipodal for any real q > 0")
