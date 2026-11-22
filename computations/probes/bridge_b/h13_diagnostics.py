"""H13 post-hoc diagnostics (written AFTER the pre-registered criteria failed; not part of the test)."""
import sys; sys.path.insert(0, "computations/probes/bridge_b")
import sympy as sp
from h13_graded_six_strand_probe import build, T, words, prod
q = sp.Rational(3, 2)
I, G, iota, sig, b, tau = build(q)
z = lambda A: A.to_Matrix().is_zero_matrix
print("b1 b2 b1 = b2 b1 b2 as operators:", z(b[1]*b[2]*b[1] - b[2]*b[1]*b[2]))
print("tau b1 tau b1 = b1 tau b1 tau as operators:", z(tau*b[1]*tau*b[1] - b[1]*tau*b[1]*tau))
print("sig: tau s1 tau s1 = s1 tau s1 tau as operators:", z(tau*sig[1]*tau*sig[1] - sig[1]*tau*sig[1]*tau))
quad = (b[1] - I*q**2)*(b[1] + I*(1/q**2))
for name, F in [("1", I), ("b1", b[1]), ("b2", b[2]), ("tau", tau), ("b2 b2", b[2]*b[2]), ("tau tau", tau*tau)]:
    print(f"T(F*quad(b1)) for F = {name}:", T(iota, F*quad))
