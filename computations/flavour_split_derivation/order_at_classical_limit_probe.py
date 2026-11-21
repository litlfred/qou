"""Order of vanishing at q = 1 of every derived proton/neutron (or u/d) differentiator on record,
against the Step-2 ansatz of prf:flavor-split-substrate. Exact over Q(q^{1/2}); no float, no q0, no CODATA.

Question: can (mu_d - mu_u)/mu_avg = h^2 hbar_q / sqrt(q) (order (q-1)^3) come from an object the corpus derives?
Every object tested here is either U_q(sl2)-equivariant (so the p/n difference is a pure pivot power of q,
NucleonIsospinExclusions.restrictedTrace_ratio) or a weight-space split already on record."""
import sympy as sp, itertools, sys
t = sp.symbols('t', positive=True)          # t = q^{1/2}
q = t**2
e = sp.symbols('e')
h = q - 1/q; hb = (q - 1)/q; br2 = q + 1/q

def order(expr):
    """order of vanishing at q = 1 and leading coefficient in (q-1)."""
    s = sp.series(sp.simplify(expr).subs(t, sp.sqrt(1 + e)), e, 0, 6).removeO()
    p = sp.Poly(sp.expand(s), e)
    for k in range(0, 6):
        c = p.coeff_monomial(e**k)
        if c != 0:
            return k, sp.nsimplify(c)
    return None, 0

def bar(expr):
    return sp.simplify(expr.subs(t, 1/t))

rows = []
# 0. the ansatz
f = h**2*hb/t
rows.append(("Step-2 ansatz h^2 hbar/sqrt(q)", f))
# 1. per-strand pivot weight: K = diag(q, q^-1), u = e1 (forced orientation), mu ∝ K-eigenvalue
mu_u, mu_d = q, 1/q
rows.append(("per-strand pivot, mu ∝ K", (mu_d - mu_u)/((mu_u + mu_d)/2)))
rows.append(("per-strand pivot, mu ∝ K^-1", (mu_u - mu_d)/((mu_u + mu_d)/2)))
# 2. nucleon restricted trace T_p = q^2 T_n (every word, Lean), additive strands 2mu_u+mu_d = c q X, mu_u+2mu_d = c q^-1 X
U, D, c = sp.symbols('U D c')
for lab, (mp, mn) in [("restricted trace, m ∝ T", (q, 1/q)), ("restricted trace, m ∝ 1/T", (1/q, q))]:
    sol = sp.solve([2*U + D - mp, U + 2*D - mn], [U, D])
    rows.append((lab + ", additive strands", (sol[D] - sol[U])/((sol[U] + sol[D])/2)))
# 3. eps_flavour(V^3) from audit 2026-11-20 (T^3 split of the z_D trace on V^3)
P = q**12 - 3*q**10 + 3*q**8 - 5*q**6 + 3*q**4 - 3*q**2 + 1
rows.append(("eps_flavour(V^3) [2026-11-20 audit]", (q**2 - 1)*P/(q**4*(q**2 + 1)**3)))

print(f"{'object':48s} order  lead-coeff   bar-image / self")
for lab, x in rows:
    k, c0 = order(x)
    r = sp.factor(sp.simplify(bar(x)/x)) if x != 0 else None
    print(f"{lab:48s} {k!s:5s}  {c0!s:10s}  {r}")

# 4. I3-weighted Murphy sum on (C^3)^{x3}: nucleon splitting D_N, normalised by the nucleon mean
def jimbo(pos):
    M = sp.zeros(9, 9)
    for i in range(3):
        for j in range(3):
            s = i*3 + j
            if i == j: M[s, s] = q
            elif pos[i] < pos[j]: M[j*3+i, s] = 1
            else: M[j*3+i, s] = 1; M[s, s] = q - 1/q
    return M
R = jimbo((0, 1, 2)); s1 = sp.kronecker_product(R, sp.eye(3)); s2 = sp.kronecker_product(sp.eye(3), R)
L = [sp.eye(27), s1*s1, s2*s1*s1*s2]
BASIS = list(itertools.product(range(3), repeat=3)); idx = lambda tt: tt[0]*9 + tt[1]*3 + tt[2]
wsp = lambda w: [tt for tt in BASIS if tuple(tt.count(k) for k in range(3)) == w]
I3 = [sp.Rational(1, 2), sp.Rational(-1, 2), 0]
M = sum((sp.diag(*[I3[tt[k]] for tt in BASIS])*L[k] for k in range(3)), sp.zeros(27))
trw = lambda X, w: sp.simplify(sum(X[idx(tt), idx(tt)] for tt in wsp(w)))
for lab, X in [("I3-Murphy tr M", M), ("I3-Murphy tr V3 M", (s1*s2.inv())**3*M)]:
    Tp, Tn = trw(X, (2, 1, 0)), trw(X, (1, 2, 0))
    k, c0 = order(Tn - Tp)
    print(f"{lab:48s} D_N=Tn-Tp order {k}, lead {c0};  T_p(1) = {sp.simplify(Tp.subs(t,1))}, T_n(1) = {sp.simplify(Tn.subs(t,1))}")
