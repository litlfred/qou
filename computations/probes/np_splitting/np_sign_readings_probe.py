"""PRE-REGISTERED: see np_sign_readings_preregistration.md (commit b49b8067a, before this run).
Which corpus reading of trace -> mass gives m_n > m_p?  Exact over Q(q) (sympy); decisions at the
rational points q = 111/100 and its bar image 100/111.  No float enters any decision.
Photon (owner ruling): gamma(phi) = 1 + phi0 s1 + phi1 s2 + phi01 s1 s2^{-1} (generators numbered
from 1 here).  Nucleon V^3 = (s1 s2^{-1})^3.  Electron s1 s2 s1.  u = e1, K = diag(q, 1/q)."""
import itertools, sympy as sp
q = sp.symbols('q', positive=True); h = q - 1/q
idx = lambda i, j: 2*i + j
R = sp.zeros(4, 4)
R[idx(0,0), idx(0,0)] = q; R[idx(1,1), idx(1,1)] = q
R[idx(1,0), idx(0,1)] = 1; R[idx(0,1), idx(1,0)] = 1; R[idx(1,0), idx(1,0)] = h
I2 = sp.eye(2)
S = {1: sp.kronecker_product(R, I2), 2: sp.kronecker_product(I2, R)}
S[-1] = sp.simplify(S[1].inv()); S[-2] = sp.simplify(S[2].inv())
assert sp.simplify(S[1]*S[2]*S[1] - S[2]*S[1]*S[2]) == sp.zeros(8, 8)
basis = list(itertools.product((0, 1), repeat=3))
def Pi(n_e1): return sp.diag(*[1 if b.count(0) == n_e1 else 0 for b in basis])
def K3(K): return sp.kronecker_product(sp.kronecker_product(K, K), K)
Kq, Kqi = sp.diag(q, 1/q), sp.diag(1/q, q)
d3 = (q + 1/q)**3
def eps(X, K, n_e1): return sp.simplify((K3(K)*X*Pi(n_e1)).trace() / d3)
def plain(X, n_e1): return sp.expand(sp.simplify((X*Pi(n_e1)).trace()))
Q1, Q2 = sp.Rational(111, 100), sp.Rational(100, 111)

def word(w):
    M = sp.eye(8)
    for g in w: M = M*S[g]
    return M
V3 = word([1, -2]*3); D3 = word([1, 2, 1])
ph = sp.symbols('a0 a1 a01 b0 b1 b01')
def photon(a0, a1, a01): return sp.eye(8) + a0*S[1] + a1*S[2] + a01*S[1]*S[-2]
els = {'V^3': V3, 'Delta3*V^3 (electron word inserted)': D3*V3,
       'gamma(phi)gamma(psi) symbolic': photon(*ph[:3])*photon(*ph[3:]),
       'gamma(0,0,qh)gamma(0,0,-h/q)': photon(0, 0, q*h)*photon(0, 0, -h/q)}
assert sp.simplify(els['gamma(0,0,qh)gamma(0,0,-h/q)'] - V3) == sp.zeros(8, 8)
words = [w for L in range(1, 6) for w in itertools.product((1, 2, -1, -2), repeat=L)]
print(f'signed words of length 1..5: {len(words)}')

c = {k: 0 for k in ('P1', 'P2', 'P2nz', 'P3neg', 'P4', 'P5', 'P6')}
for w in words:
    X = word(w)
    tp, tn = plain(X, 2), plain(X, 1)
    ok1 = sp.simplify(tp - tn) == 0; c["P1"] += bool(ok1)
    ep, en = eps(X, Kq, 2), eps(X, Kq, 1)
    ep1, en1 = ep.subs(q, Q1), en.subs(q, Q1)
    if ep1 != 0:
        c['P2nz'] += 1
        c["P2"] += bool(abs(en1) < abs(ep1))
        c["P4"] += bool(abs(en.subs(q, Q2)) > abs(ep.subs(q, Q2)))
        c["P3neg"] += bool(tp.subs(q, Q1) < 0)
    # Cartan involution: K^{-1} with u = e2 (proton = one e1, neutron = two e1)
    c["P5"] += bool(sp.simplify(eps(X, Kqi, 1) - ep) == 0 and sp.simplify(eps(X, Kqi, 2) - en) == 0)
    cem = sp.symbols('c')
    two_n = sp.simplify(en + cem*sp.Rational(-1, 3)*sp.simplify((K3(Kq)*X*Pi(1)).trace()/q**-1)/d3)
    c["P6"] += bool(sp.simplify(two_n - ep - (1/q - q - cem/3)*tp/d3) == 0)
N = len(words)
print(f"P1 plain traces equal on W_p, W_n: {c['P1']}/{N}")
print(f"P2 |eps_n|<|eps_p| at q=111/100 (words with eps_p != 0): {c['P2']}/{c['P2nz']}")
print(f"P3 words with tr_W<0 at q=111/100 (neutron heavier under signed linear reading): {c['P3neg']}/{c['P2nz']}  [reported, not predicted]")
print(f"P4 reversed at q=100/111: {c['P4']}/{c['P2nz']}")
print(f"P5 (K^-1, u=e2) gives same (eps_p, eps_n): {c['P5']}/{N}")
print(f"P6 two-term Q_pair difference = (1/q - q - c/3) tr_W: {c['P6']}/{N}")
for k, X in els.items():
    tp, tn = plain(X, 2), plain(X, 1)
    ep, en = eps(X, Kq, 2), eps(X, Kq, 1)
    print(f'{k}: plain equal={sp.simplify(tp-tn)==0}; eps_n/eps_p={sp.simplify(en/ep)};'
          f' tr_W(111/100)>0: {sp.simplify(tp.subs(q,Q1)) > 0 if not tp.free_symbols - {q} else "symbolic"}')
# P7 electron as spectator: its own quantum trace
te = sp.factor(sp.simplify((K3(Kq)*D3).trace()/d3))
print(f'P7 electron Delta3 quantum trace = {te}; at 111/100 > 0: {te.subs(q,Q1) > 0}')
print(f'V^3: eps_n - eps_p = {sp.factor(eps(V3,Kq,1)-eps(V3,Kq,2))}')
