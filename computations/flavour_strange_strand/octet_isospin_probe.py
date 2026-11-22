"""Octet isospin splittings with a strange strand: exact symbolic probe.

Setting: Jimbo braiding on (C^3)^{x3}, e1=u, e2=d, e3=s. For each octet pair
(N: uud/udd, Sigma: uus/dds, Xi: uss/dss) restrict sigma_1, sigma_2 to the
weight space and compare with the sl2 nucleon matrices. Then evaluate the
Cartan term (K_low - K_high) * tr(w) under two Cartan choices, and the
two-term charge operators Q_self, Q_pair. All exact in Q(q); no floats.
Lattice numbers appear ONLY in the final printed comparison, never upstream.
"""
import itertools, sympy as sp
q = sp.symbols('q', positive=True)

def R(N):
    M = sp.zeros(N*N, N*N)
    for i in range(N):
        for j in range(N):
            s = i*N + j
            if i == j: M[s, s] = q
            elif i < j: M[j*N+i, s] = 1
            else: M[j*N+i, s] = 1; M[s, s] = q - 1/q
    return M
N = 3
s1 = sp.kronecker_product(R(N), sp.eye(N)); s2 = sp.kronecker_product(sp.eye(N), R(N))
def ws(w):
    return [t[0]*9+t[1]*3+t[2] for t in itertools.product(range(3), repeat=3)
            if tuple(t.count(k) for k in range(3)) == w]
def restr(M, idx): return M.extract(idx, idx)

# sl2 reference: nucleon weight spaces in (C^2)^{x3}
s1b = sp.kronecker_product(R(2), sp.eye(2)); s2b = sp.kronecker_product(sp.eye(2), R(2))
def ws2(w): return [t[0]*4+t[1]*2+t[2] for t in itertools.product(range(2), repeat=3)
                    if tuple(t.count(k) for k in range(2)) == w]
ref = {'hi': (restr(s1b, ws2((2,1))), restr(s2b, ws2((2,1)))),
       'lo': (restr(s1b, ws2((1,2))), restr(s2b, ws2((1,2))))}

charge = [sp.Rational(2,3), sp.Rational(-1,3), sp.Rational(-1,3)]
# pair: (name, I3-up member weight, I3-down member weight); "down" = n, Sigma-, Xi-
pairs = [('N',     (2,1,0), (1,2,0)),
         ('Sigma', (2,0,1), (0,2,1)),
         ('Xi',    (1,0,2), (0,1,2))]
Krho = [q**2, 1, q**-2]          # q^{2 rho} for sl3
Kiso = [q, 1/q, 1]               # q^{H_1}: isospin Cartan only, s blind
def Kw(K, w): return sp.prod([K[k]**c for k, c in enumerate(w)])
def qself(w): return sum(c*charge[k]**2 for k, c in enumerate(w))
def qpair(w):
    cs = [charge[k] for k, c in enumerate(w) for _ in range(c)]
    return sum(cs[i]*cs[j] for i in range(3) for j in range(i+1, 3))

V3 = (s1 * s2.inv())**3
out = {}
for name, hi, lo in pairs:
    A1, A2 = restr(s1, ws(hi)), restr(s2, ws(hi))
    B1, B2 = restr(s1, ws(lo)), restr(s2, ws(lo))
    same = (sp.simplify(A1-ref['hi'][0]) == sp.zeros(3) and sp.simplify(A2-ref['hi'][1]) == sp.zeros(3)
            and sp.simplify(B1-ref['lo'][0]) == sp.zeros(3) and sp.simplify(B2-ref['lo'][1]) == sp.zeros(3))
    tr_hi = sp.simplify(restr(V3, ws(hi)).trace()); tr_lo = sp.simplify(restr(V3, ws(lo)).trace())
    out[name] = dict(
        same=same, tr_equal=sp.simplify(tr_hi-tr_lo) == 0, tr=tr_hi,
        dK_rho=sp.factor(Kw(Krho, lo) - Kw(Krho, hi)),
        dK_iso=sp.factor(Kw(Kiso, lo) - Kw(Kiso, hi)),
        dQself=qself(lo) - qself(hi), dQpair=qpair(lo) - qpair(hi))
    print(f"{name:6s} braid matrices = sl2 nucleon ones: {same}; tr V3 equal on both: {out[name]['tr_equal']}")
    print(f"       Cartan (low-high), q^2rho: {out[name]['dK_rho']};  isospin Cartan: {out[name]['dK_iso']}")
    print(f"       charge: dQ_self = {out[name]['dQself']}, dQ_pair = {out[name]['dQpair']}")

print("\nRatios to the nucleon (exact):")
for key in ('dK_rho', 'dK_iso'):
    for nm in ('Sigma', 'Xi'):
        print(f"  {key} {nm}/N = {sp.simplify(out[nm][key]/out['N'][key])}")
cg = sp.factor(out['Sigma']['dK_iso'] - out['N']['dK_iso'] - out['Xi']['dK_iso'])
print("  Coleman-Glashow defect of the isospin-Cartan term (Sigma - N - Xi):", cg)

# --- comparison boundary: physics enters only here ---
q0 = sp.Rational('1.1099785827513808')
print("\nAt q0 (display only):")
for key in ('dK_rho', 'dK_iso'):
    r = [sp.N(sp.simplify(out[nm][key]/out['N'][key]).subs(q, q0), 6) for nm in ('Sigma', 'Xi')]
    print(f"  {key}: Sigma:N:Xi = {r[0]} : 1 : {r[1]}")
print("  Lattice QCD parts (Horsley et al. 2016, MeV): 9.07 : 3.51 : 5.58 = 2.584 : 1 : 1.590")
print("  First-order SU(3) form (2a1+a2):(a1+2a2):(a1-a2); lattice gives a2/a1 =",
      sp.N(sp.Rational(-207,100)/3 / (sp.Rational(351,100) + sp.Rational(414,300)), 4))
