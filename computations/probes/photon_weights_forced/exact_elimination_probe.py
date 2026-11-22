"""Exact elimination of the six-weight two-photon factorisations of V^3 at q = 11/10.

Photon gamma(a,b,c) = 1 + a s0 + b s1 + c V, V = s0 s1^-1, in H_3(q) seen through its three
irreps. Given the first photon, the second is forced: psi = gamma^-1 V^3, and it must lie in
the photon affine subspace (two linear functionals vanish on it, a third reads the
coefficient of 1). Clearing the denominators t, s, det G gives three polynomials in a, b, c over
Q. Eliminating c, then b, gives a univariate polynomial in a, factored over Q.

All arithmetic is exact (sympy Rational). Roots are printed with mpmath only for display.
Every candidate is checked against t, s, det G != 0, so solutions created by clearing
denominators are discarded. Bean qou-99qc.
"""
import sys, sympy as sp, mpmath as mp
q = sp.Rational(sys.argv[1]) if len(sys.argv) > 1 else sp.Rational(11, 10)
a, b, c = sp.symbols('a b c')
M = sp.Matrix
I2 = sp.eye(2)
S0 = M([[q, 0], [0, -1/q]])
S1 = M([[-1/(q**3 + q), (q**2*(q**2 + 1) + 1)/(q**2 + 1)**2], [1, q**3/(q**2 + 1)]])
W = S0*S1.inv()
vec = lambda t, s, G: M([t, s, G[0, 0], G[0, 1], G[1, 0], G[1, 1]])
Bm = M.hstack(vec(1, 1, I2), vec(q, -1/q, S0), vec(q, -1/q, S1), vec(1, 1, W))
L1, L2 = [n.T for n in Bm.T.nullspace()]
sol = list(sp.linsolve((Bm.T, M([1, 0, 0, 0]))))[0]
L0 = M(sol).T.subs({x: 0 for x in M(sol).free_symbols})
t = 1 + q*(a + b) + c; s = 1 - (a + b)/q + c; G = I2 + a*S0 + b*S1 + c*W
dG = sp.expand(G.det())
adj = M([[G[1, 1], -G[0, 1]], [-G[1, 0], G[0, 0]]])
P = vec(s*dG, t*dG, t*s*adj*W**3).applyfunc(sp.expand)
den = sp.expand(t*s*dG)
e1, e2, e0 = [sp.expand(x) for x in ((L1*P)[0], (L2*P)[0], (L0*P)[0] - den)]
eqs = (e1, e2, e0)
nondeg = lambda S: all(sp.simplify(z.subs(S)) != 0 for z in (t, s, dG))

r1, r2 = sp.resultant(e1, e2, c), sp.resultant(e1, e0, c)
g = sp.gcd(r1, r2)
print("common factor of the two c-resultants:", sp.factor(g))
R = sp.Poly(sp.resultant(sp.Poly(sp.cancel(r1/g), b), sp.Poly(sp.cancel(r2/g), b)), a)
print("univariate eliminant in a: degree", R.degree())
mp.mp.dps = 30
for f, m in sp.factor_list(R.as_expr())[1]:
    P1 = sp.Poly(f, a)
    rts = mp.polyroots([mp.mpf(sp.Rational(x).p)/sp.Rational(x).q for x in P1.all_coeffs()], maxsteps=200, extraprec=200)
    print(f"  factor degree {P1.degree()} (multiplicity {m}): roots", [mp.nstr(r, 8) for r in rts])
    if P1.degree() == 6:
        print("  sextic:", P1.as_expr())

print("branch a = 0 (genuine solutions):",
      [S for S in sp.solve([x.subs(a, 0) for x in eqs], [b, c], dict=True) if nondeg({a: 0, **S})])
branches = []
for f, _ in sp.factor_list(g)[1]:
    v = a if sp.Poly(f, a, b).degree(a) > 0 else b
    branches.append({v: sp.solve(f, v)[0]})
for sub in branches:
    v = [x for x in (a, b) if x not in sub][0]
    S = sp.solve([sp.expand(x.subs(sub)) for x in eqs], [v, c], dict=True)
    full = lambda z: {**z, **{k: sp.sympify(e).subs(z) for k, e in sub.items()}}
    print("common-factor branch", sub, "genuine:", [full(z) for z in S if nondeg(full(z))])

print("every rational root of the eliminant, checked for genuine solutions:")
for f, m in sp.factor_list(R.as_expr())[1]:
    P1 = sp.Poly(f, a)
    if P1.degree() == 1:
        av = sp.solve(f, a)[0]
        S = sp.solve([sp.expand(x.subs(a, av)) for x in eqs], [b, c], dict=True)
        print(f"  a = {av}: genuine", [z for z in S if nondeg({a: av, **z})], f"(of {len(S)} candidates)")
