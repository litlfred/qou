"""H10b: Lusztig 16.7(b) normalisation check. Same D(s) as H10 (V^3, from H8).

Lusztig, Hecke algebras with unequal parameters (arXiv math/0208154v2) §16.2, 16.7(b):
the folded algebra H(W, L), L = restriction of the ambient length, has quadratic relation
(b_w0I - v^{l(w0I)})(b_w0I + v^{-l(w0I)}) = 0 with v the AMBIENT indeterminate.
Reading A (H10): folded bulk generator has {q, -1/q}  => v = q^(1/2), wall Q = q^(1/2).
Reading B (conj:type-b-folding-cpt folds the physical H_n(q), so v = q):
  folded bulk has {q^2, -q^-2}, wall has {q, -1/q}. D(s) then has bulk parameter q^2.
"""
import sympy as sp
q = sp.symbols('q', positive=True)
s = sp.symbols('s')
D = (q**12 - 3*q**10 - q**8*s + 3*q**8 + 2*q**6*s - 5*q**6 - 3*q**4*s + 3*q**4 + q**2*s - 3*q**2 + 1) / \
    (q**12*s + q**12 - 3*q**10*s - 3*q**10 + 3*q**8*s + 3*q**8 - 3*q**6*s - 5*q**6 + 3*q**4 - 3*q**2 + 1)
from qou_substrate.constants import Q_50_DIGIT_STR
q0 = sp.Rational(Q_50_DIGIT_STR)
DA = D.subs(s, sp.sqrt(q) - 1/sp.sqrt(q))
DB = D.subs(q, q**2).subs(s, q - 1/q)   # bulk q^2, wall q
print("A (bulk q, wall q^(1/2)):   D(q0) =", sp.N(DA.subs(q, q0), 20), " D(1) =", sp.limit(DA, q, 1))
print("B (bulk q^2, wall q):       D(q0) =", sp.N(DB.subs(q, q0), 20), " D(1) =", sp.limit(DB, q, 1))
print("check: A at q = q0^2 equals B at q0:", sp.N(DA.subs(q, q0**2) - DB.subs(q, q0), 30))
