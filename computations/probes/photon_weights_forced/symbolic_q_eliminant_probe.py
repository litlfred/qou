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
  * (branch checks, at the end) every other branch carries no genuine solution for generic q:
    the linear-in-a factors a = q, -q, 1/q and the octic-in-q root, the a-values where both
    b-leading coefficients vanish, and the five degenerate branches read off the common factor
    (b = -a, b = q, b = -1/q, q^2 a + q^2 b + q - b = 0, q^2 b + q - a - b = 0). On a = 0 the
    only genuine solutions are b = 0 with c^2 - h^2 c - h^2 = 0, i.e. the ruled pair
    c in {q h, -q^-1 h}, h = q - q^-1.
    "Genuine" means t * s * det G != 0 (the photon gamma is invertible). "Generic q" means over
    the field Q(q): a branch with no genuine solution there can have one only at finitely many q.
What it does NOT establish: that the a-degree-10 factor (degree (115, 10)) carries no genuine
solution for generic q. That factor is checked only numerically, at 80 digits, at the five
rational q of exact_elimination_probe.py; a symbolic check needs work over Q(q)[a]/(f10).
Nor which finitely many exceptional q exist, nor anything at a specific
numerical q0 beyond the five rational q of exact_elimination_probe.py.
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

# ---- branch checks over Q(q) -------------------------------------------------------------
X = sp.Symbol('x')
nd = sp.numer(sp.together(t*s*dG))
bctx = flint.fmpz_mpoly_ctx.get(('q', 'x', 'c'), 'lex')
QQq = sp.QQ.frac_field(q)

def branch(name, S, x):
    """Substitute S, eliminate c, and test each candidate x-value for a common c-root
    of the three equations at which t*s*det G does not vanish, working over Q(q)."""
    sub = lambda e: sp.numer(sp.together(e.subs(S))).subs(x, X)
    def F(e):
        Pp = sp.Poly(sp.expand(sub(e)), q, X, c)
        den = sp.ilcm(*[sp.Rational(v).q for v in Pp.coeffs()])
        return bctx.from_dict({m: int(v*den) for m, v in Pp.terms()})
    E = [F(e) for e in eqs]
    g2 = E[0].resultant(E[1], 'c').gcd(E[0].resultant(E[2], 'c'))
    d = E[0].degrees()[2]
    lc = bctx.from_dict({(m[0], m[1], 0): v for m, v in E[0].to_dict().items() if m[2] == d})
    cand = {str(f) for src in (g2, lc) if not src.is_zero()
            for f, _ in src.factor()[1] if f.degrees()[1] > 0}
    genuine = []
    for fs in sorted(cand):
        f = sp.sympify(fs.replace('^', '**'), locals={'q': q, 'x': X})
        if sp.degree(f, X) != 1:
            genuine.append(('nonlinear candidate, not checked', fs)); continue
        xv = sp.solve(f, X)[0]
        Ps = [sp.Poly(sp.numer(sp.together(e.subs(S).subs(x, xv))), c, domain=QQq) for e in eqs]
        Ns = sp.Poly(sp.numer(sp.together(nd.subs(S).subs(x, xv))), c, domain=QQq)
        Gc = Ps[0]
        for e in Ps[1:]:
            Gc = sp.gcd(Gc, e)
        if Gc.is_zero:
            genuine.append((xv, 'all three equations vanish identically in c')); continue
        while Gc.degree() > 0 and sp.gcd(Gc, Ns).degree() > 0:
            Gc = sp.quo(Gc, sp.gcd(Gc, Ns))
        if Gc.degree() > 0:
            genuine.append((xv, sp.factor(Gc.as_expr())))
    print(f"  branch {name}: " + ("no genuine solution over Q(q)" if not genuine
                                  else f"genuine: {x} = ... {genuine}"))
    return genuine

print("branch checks (generic q, i.e. over Q(q)):")
lin = [sp.sympify(str(f).replace('^', '**'), locals={'q': q, 'a': a})
       for f, m in facs if f.degrees()[1] == 1]
lc_a = None
for r in (r1 // g, r2 // g):
    db = r.degrees()[2]
    l = ctx.from_dict({(m[0], m[1], 0, 0): v for m, v in r.to_dict().items() if m[2] == db})
    lc_a = l if lc_a is None else lc_a.gcd(l)
lin += [sp.sympify(str(f).replace('^', '**'), locals={'q': q, 'a': a})
        for f, _ in lc_a.factor()[1] if f.degrees()[1] == 1]
a_roots = sorted({sp.simplify(sp.solve(f, a)[0]) for f in lin}, key=str)
assert all(sp.degree(f, a) == 1 for f in lin)
bad = []
for av in a_roots:
    gen = branch(f"a = {av}", {a: av}, b)
    if av == 0:
        ok = (len(gen) == 1 and gen[0][0] == 0 and
              sp.expand(sp.Poly(gen[0][1], c).monic().as_expr() - (c**2 - (q - 1/q)**2*c - (q - 1/q)**2)) == 0)
        print("    a = 0 gives exactly the ruled pair c^2 - h^2 c - h^2 = 0 at b = 0:", ok)
        bad += [] if ok else ['a=0']
    elif gen:
        bad.append(f"a={av}")
for name, S, x in [("b = -a", {b: -a}, a), ("b = q", {b: q}, a), ("b = -1/q", {b: -1/q}, a),
                   ("q^2 a + q^2 b + q - b = 0", {a: (b - q - q**2*b)/q**2}, b),
                   ("q^2 b + q - a - b = 0", {a: q**2*b + q - b}, b)]:
    if branch(name, S, x):
        bad.append(name)
print("ALL BRANCH CHECKS PASS:", not bad, bad)
