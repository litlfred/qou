"""H10: D for the Hecke-normalised wall with parameter Q (eigenvalues {Q, -1/Q}), V^3, exact."""
import sympy as sp
q = sp.symbols('q', positive=True)
s = sp.symbols('s')
# From H8 (h8_open_trace_probe.out.txt): D(s) for V^3, mirror-free type-B wall at strand 1
D = (q**12 - 3*q**10 - q**8*s + 3*q**8 + 2*q**6*s - 5*q**6 - 3*q**4*s + 3*q**4 + q**2*s - 3*q**2 + 1) / \
    (q**12*s + q**12 - 3*q**10*s - 3*q**10 + 3*q**8*s + 3*q**8 - 3*q**6*s - 5*q**6 + 3*q**4 - 3*q**2 + 1)
from qou_substrate.constants import Q_50_DIGIT_STR
q0 = sp.Rational(Q_50_DIGIT_STR)
for name, Q in (("L Lusztig Q=q^(1/2)", sp.sqrt(q)), ("E equal Q=q", q)):
    sv = Q - 1/Q
    Dv = sp.simplify(D.subs(s, sv))
    print(f"{name}: s = {sp.simplify(sv)}; D(1) = {sp.limit(Dv, q, 1)}; D(q0) = {sp.N(Dv.subs(q, q0), 20)}")
# M: type-B Markov value with the pivot: y = tr(K Kw)/tr(K) = q^2 s/(q^2+1) (H6). Does any Markov condition fix Q?
print("M: y(Q) = q^2 (Q - 1/Q)/(q^2+1); a Markov condition fixes y, i.e. one value of Q per chosen y.")
