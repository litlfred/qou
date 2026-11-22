"""H6: is the wall end a derived choice? Exact sympy.
Checks: strand reversal (P) composed with flavour swap (S on both factors) fixes the Jimbo R,
and maps the pivot K=diag(q,1/q) to its inverse. Type-B Markov value of the d=0 wall."""
import sympy as sp
q, x, y = sp.symbols('q x y', positive=True)
h = q - 1/q
R = sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,q]])
P = sp.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
S = sp.Matrix([[0,1],[1,0]]); SS = sp.kronecker_product(S, S)
K = sp.diag(q, 1/q)
print("P R P == (S x S) R (S x S):", sp.simplify(P*R*P - SS*R*SS) == sp.zeros(4))
print("S K S == K^-1:", sp.simplify(S*K*S - K.inv()) == sp.zeros(2))
Kw = sp.Matrix([[x+y, 1], [-x*y, 0]])  # wall at strand 1, d = 0
yB = sp.simplify((K*Kw).trace() / K.trace())
print("type-B Markov value tr(K Kw)/tr(K) =", yB, " free in x+y:", sp.diff(yB, x) != 0)
