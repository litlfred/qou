"""Symbolic-q eliminant of the six-weight two-photon factorisations of V^3 = (s0 s1^-1)^3.

Same set-up as exact_elimination_probe.py, but with q left symbolic. The three polynomial
equations in (q, a, b, c) are built with sympy, then the eliminations (resultant in c, gcd,
resultant in b) and the factorisation over Z[q, a] are done with python-flint (FLINT
fmpz_mpoly), which takes seconds where sympy did not finish in hours.

What this establishes, exactly:
  * the univariate eliminant in a, over Z[q], and its irreducible factors over Z[q, a];
  * the factor of a-degree 6 (the six non-ruled solutions) is irreducible over Z[q, a], hence by
    Gauss's lemma irreducible over Q(q)[a]. So for generic q, no non-ruled solution has
    phi0 in Q(q), and the six form one Galois orbit over Q(q).
What it does NOT establish: that the linear-in-a factors other than a = 0 (a = +-q, a = 1/q, and
one more) and the degenerate branches carry no genuine solution for symbolic q. That is checked
exactly only at the five rational q of exact_elimination_probe.py.
Needs: pip install python-flint (tested 0.7.1). Bean qou-99qc.
"""
import sympy as sp, flint
q, a, b, c = sp.symbols('q a b c')
M = sp.Matrix; I2 = sp.eye(2)
S0 = M([[q, 0], [0, -1/q]])
S1 = M([[-1/(q**3 + q), (q**2*(q**2 + 1) + 1)/(q**2 + 1)**2], [1, q**3/(q**2 + 1)]])
W = (S0*S1.inv()).applyfunc(sp.factor)
vec = lambda t, s, G: M([t, s, G[0, 0], G[0, 1], G[1, 0], G[1, 1]])
Bm = M.hstack(vec(1, 1, I2), vec(q, -1/q, S0), vec(q, -1/q, S1), vec(1, 1, W))
L1, L2 = [n.applyfunc(sp.factor).T for n in Bm.T.nullspace()]
sol = list(sp.linsolve((Bm.T, M([1, 0, 0, 0]))))[0]
L0 = M(sol).T.subs({x: 0 for x in M(sol).free_symbols if x != q}).applyfunc(sp.factor)
t = 1 + q*(a + b) + c; s = 1 - (a + b)/q + c; G = I2 + a*S0 + b*S1 + c*W
dG = sp.factor(G.det())
adj = M([[G[1, 1], -G[0, 1]], [-G[1, 0], G[0, 0]]])
P = vec(s*dG, t*dG, t*s*adj*(W**3).applyfunc(sp.factor))
clean = lambda e: sp.numer(sp.factor(sp.together(e)))
eqs = [clean((L1*P)[0]), clean((L2*P)[0]), clean((L0*P)[0] - t*s*dG)]

ctx = flint.fmpz_mpoly_ctx.get(('q', 'a', 'b', 'c'), 'lex')
def conv(e):
    Pp = sp.Poly(sp.expand(e), q, a, b, c)
    den = sp.ilcm(*[sp.Rational(x).q for x in Pp.coeffs()])
    return ctx.from_dict({m: int(x*den) for m, x in Pp.terms()})
E1, E2, E0 = [conv(e) for e in eqs]
r1, r2 = E1.resultant(E2, 'c'), E1.resultant(E0, 'c')
g = r1.gcd(r2)
print("common factor of the two c-resultants:", g.factor())
R = (r1 // g).resultant(r2 // g, 'b')
const, facs = R.factor()
print("eliminant in a, irreducible factors over Z[q, a] (degrees are (q, a, b, c)):")
for f, m in facs:
    d = f.degrees()
    txt = str(f) if d[1] <= 1 else f"<a-degree {d[1]}, q-degree {d[0]}, {len(f)} terms>"
    print(f"  degrees {d}, multiplicity {m}: {txt}")
sextic = [f for f, m in facs if f.degrees()[1] == 6]
print("a-degree-6 factor present and irreducible over Z[q, a]:", len(sextic) == 1)
