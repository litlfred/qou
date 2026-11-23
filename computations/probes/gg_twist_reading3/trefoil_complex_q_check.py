#!/usr/bin/env python3
"""trefoil_complex_q_check.py — exact (sympy, formal q) traces of trefoil braids, for the complex-q question.

H_3 block (2,1) via reduced Burau rescaled to eigenvalues {q, -1/q} (checked: Hecke + braid relations hold).
Every 3-strand trefoil braid has (2,1) trace exactly -1 as a rational function of q, so at any complex q
the block trace is the negative real -1. On 2 strands chi_(2)(s^3) chi_(1,1)(s^3) = -1.
-- Ref: [leitner2026] bean qou-a1hh
"""
import sympy as sp

q = sp.symbols("q")
t = q ** -2
A = q * sp.Matrix([[-t, 1], [0, 1]])
B = q * sp.Matrix([[1, 0], [t, -t]])
assert sp.simplify(A ** 2 - (q - 1 / q) * A - sp.eye(2)) == sp.zeros(2)
assert sp.simplify(A * B * A - B * A * B) == sp.zeros(2)
Ai, Bi = A.inv(), B.inv()
words = {"s0^3 s1": A ** 3 * B, "s0^-3 s1^-1": Ai ** 3 * Bi, "(s0 s1)^2": (A * B) ** 2, "(s0^-1 s1^-1)^2": (Ai * Bi) ** 2}
for k, M in words.items():
    tr = sp.simplify(M.trace())
    print(f"tr_(2,1)({k}) = {tr}")
    assert tr == -1
print("2 strands: chi_(2)(s^3)*chi_(1,1)(s^3) =", sp.simplify(q ** 3 * (-1 / q) ** 3))
print("Re>=0 on both 2-strand characters iff cos(arg q^3) = 0 (both real parts then vanish).")
