"""Weighted Jucys-Murphy sums on the octet weight spaces of (C^3)^{x3}. Exact over Q(q).

Jimbo braiding (flavour order given by `pos`), Murphy elements L1 = 1, L2 = s1^2, L3 = s2 s1^2 s2.
Weighted sum M_w = sum_k w(flavour on strand k) * L_k  (diagonal weight times L_k).
Splitting of an isospin pair: D = tr_lo(M_w) - tr_hi(M_w) over the weight spaces.
Weights: hypercharge Y = (1/3, 1/3, -2/3); isospin I3 = (1/2, -1/2, 0); charge Q = I3 + Y/2.
Also: the same with the isospin Cartan weight q^{H1} and with V3 = (s1 s2^-1)^3 inserted.
q0 appears only in the final display lines; lattice numbers only at the comparison print."""
import itertools, sympy as sp
q = sp.symbols('q', positive=True)

def jimbo(pos):
    M = sp.zeros(9, 9)
    for i in range(3):
        for j in range(3):
            s = i*3 + j
            if i == j: M[s, s] = q
            elif pos[i] < pos[j]: M[j*3+i, s] = 1
            else: M[j*3+i, s] = 1; M[s, s] = q - 1/q
    return M

Y  = [sp.Rational(1, 3), sp.Rational(1, 3), sp.Rational(-2, 3)]
I3 = [sp.Rational(1, 2), sp.Rational(-1, 2), 0]
Qc = [I3[k] + Y[k]/2 for k in range(3)]
PAIRS = [('N', (2, 1, 0), (1, 2, 0)), ('Sigma', (2, 0, 1), (0, 2, 1)), ('Xi', (1, 0, 2), (0, 1, 2))]
BASIS = list(itertools.product(range(3), repeat=3))
def idx(t): return t[0]*9 + t[1]*3 + t[2]
def wsp(w): return [t for t in BASIS if tuple(t.count(k) for k in range(3)) == w]

def setup(pos):
    R = jimbo(pos)
    s1 = sp.kronecker_product(R, sp.eye(3)); s2 = sp.kronecker_product(sp.eye(3), R)
    return s1, s2, [sp.eye(27), s1*s1, s2*s1*s1*s2]

def murphy_sum(L, w):
    D = [sp.diag(*[w[t[k]] for t in BASIS]) for k in range(3)]
    return sum((D[k]*L[k] for k in range(3)), sp.zeros(27))

def trw(X, w): return sp.simplify(sum(X[idx(t), idx(t)] for t in wsp(w)))

def splittings(X, cartan=False):
    out = {}
    for name, hi, lo in PAIRS:
        Kh, Kl = (q**(hi[0]-hi[1]), q**(lo[0]-lo[1])) if cartan else (1, 1)
        out[name] = sp.factor(sp.simplify(Kl*trw(X, lo) - Kh*trw(X, hi)))
    return out

def report(label, D):
    cg = sp.factor(sp.simplify(D['Sigma'] - D['N'] - D['Xi']))
    print(f"== {label}\n   D = {D}\n   Coleman-Glashow defect Sigma-N-Xi = {cg}")
    if D['N'] == 0:
        return None
    rx = sp.simplify(D['Xi']/D['N']); x = sp.factor(sp.simplify((1 - rx)/(1 + 2*rx)))
    e = sp.Symbol('e')
    print(f"   a2/a1 (from Xi/N = (1-x)/(1+2x)) = {x};  series: {sp.series(x.subs(q, 1+e), e, 0, 3)}")
    return x

if __name__ == '__main__':
    s1, s2, L = setup((0, 1, 2))
    print("L2, L3 commute:", sp.simplify(L[1]*L[2] - L[2]*L[1]) == sp.zeros(27))
    V3 = (s1*s2.inv())**3
    res = {}
    for wl, w in [('Y', Y), ('I3', I3), ('Q', Qc)]:
        M = murphy_sum(L, w)
        res[(wl, 'bare')] = report(f"{wl}-Murphy, tr M", splittings(M))
        res[(wl, 'V3')]   = report(f"{wl}-Murphy, tr V3 M", splittings(V3*M))
        report(f"{wl}-Murphy x isospin Cartan q^H1, tr M", splittings(M, cartan=True))
    print("\nFlavour-order dependence (I3-Murphy, tr M):")
    for lab, pos in [("u<d<s", (0, 1, 2)), ("s<u<d", (1, 2, 0)), ("u<s<d", (0, 2, 1)), ("d<u<s", (1, 0, 2))]:
        _, _, Lp = setup(pos)
        res[('order', lab)] = report(lab, splittings(murphy_sum(Lp, I3)))
    # --- comparison boundary: physics enters only here ---
    q0 = sp.Rational('1.1099785827513808')
    print("\nAt q0 (display only):")
    for k, x in res.items():
        if x is not None:
            print(f"   {k}: a2/a1 = {sp.N(x.subs(q, q0), 6)}")
    print("   Lattice QCD parts (Horsley et al., MeV) 9.07 : 3.51 : 5.58 imply a2/a1 = -0.1411")
