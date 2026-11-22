"""Pre-registered in PREREGISTRATION-eigenvalue-charges.md (3522c467284). Same arms as the
muon-scale probe, with charges from the gamma-gamma vertex eigenvalue phase t(q).
M1: E_n - E_p = 2 m_mu ([3]!/q^3)(tau_n - tau_p)(D^2); M2: same with D^2 - S (S = QPair*hol as potential);
E-pot: section-31 electron-calibrated map with -S. Exact sympy; mpmath 60 dps at the proton pin. No float64.
m_mu = m_e Vol(4_1)/hbar_q^2, Vol(4_1) = 2 Cl_2(pi/3).
"""
import json, itertools, sympy as sp, mpmath as mp
from qou_substrate import constants as C

q = sp.symbols('q', positive=True)
Rc = sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,q-1/q,0],[0,0,0,q]])
I2, I8 = sp.eye(2), sp.eye(8)
s0 = sp.kronecker_product(Rc, I2); s1 = sp.kronecker_product(I2, Rc)
basis = list(itertools.product([0,1], repeat=3))
T3 = sp.diag(*[sp.Rational(b.count(0) - b.count(1), 2) for b in basis])
K3 = sp.diag(*[q**(b.count(0) - b.count(1)) for b in basis])
cu, cd = sp.symbols('cu cd')
ch = {0: cu, 1: cd}
QPair = sp.diag(*[sum(ch[b[i]]*ch[b[j]] for i in range(3) for j in range(i+1,3)) for b in basis])
two = q + 1/q; three = q**2 + 1 + q**-2
hol_N = sp.simplify((s0*s1.inv())**3); X_e = sp.simplify(s0*s1*s0)
def D(hol, wr): return (hol - q**wr*I8)/q + (1 - 1/q)*T3
D_N, D_e = D(hol_N, 0), D(X_e, 3)
Wp = [i for i,b in enumerate(basis) if b.count(0) == 2]
Wn = [i for i,b in enumerate(basis) if b.count(0) == 1]
blk = lambda M, idx: M.extract(idx, idx)
DD = D_N*D_N; S = QPair*hol_N
def tau_np(X):  # tau_n - tau_p : convention-D sector shares (q^{+-1} tr / [2]^3)
    return sp.simplify((blk(K3*X, Wn).trace() - blk(K3*X, Wp).trace())/two**3)
F_norm = two*three/q**3                    # [3]_q!/q^3
hbar = 1 - 1/q
mp.mp.dps = 60
q0 = mp.mpf(C.Q_50_DIGIT_STR); me = mp.mpf(C.M_E_MEV_STR)
vol = 2*mp.clsin(2, mp.pi/3)
mmu0 = me*vol/(1 - 1/q0)**2
ev = lambda e: sp.lambdify(q, e, "mpmath")(q0)

tq = lambda qq: mp.acos(-(qq**4 - qq**2 + 1)/(2*qq**2))/(2*mp.pi)
t0 = tq(q0)
tsym = sp.acos(-(q**4 - q**2 + 1)/(2*q**2))/(2*sp.pi)
READ = {"R1_mirror": (tsym, -tsym), "R2_gap1": (1 - tsym, -tsym)}
res = {"preregistration": "3522c467284", "t_q0": mp.nstr(t0, 20), "readings": {}}
for rn, (u, d) in READ.items():
    sub = {cu: u, cd: d}; R = {}
    X = DD - S
    dM2 = tau_np(X).subs(sub)
    f = sp.lambdify(q, F_norm*dM2, "mpmath")
    R["M2_E_n_minus_E_p_MeV_at_q0"] = mp.nstr(2*mmu0*f(q0), 12)
    for arm, (Tn, Tp, Te) in {
        "Epot_P_plain": (blk(X, Wn).trace(), blk(X, Wp).trace(), (D_e*D_e).trace()),
        "Epot_K_quantum": (blk(K3*X, Wn).trace()/two**3, blk(K3*X, Wp).trace()/two**3,
                           (K3*D_e*D_e).trace()/two**3)}.items():
        r = ((Tn - Tp)/Te).subs(sub)
        g = sp.lambdify(q, r, "mpmath")
        lim1 = g(1 + mp.mpf('1e-30'))
        R[arm] = {"E_over_m_e_at_q0": mp.nstr(g(q0), 15),
                  "E_n_minus_E_p_keV_at_q0": mp.nstr(1000*me*g(q0), 12),
                  "value_at_q=1+1e-30": mp.nstr(lim1, 12)}
    uq, dq = (sp.lambdify(q, u, "mpmath")(q0), sp.lambdify(q, d, "mpmath")(q0))
    R["charges_q0"] = {"u": mp.nstr(uq, 15), "d": mp.nstr(dq, 15),
                       "proton": mp.nstr(2*uq + dq, 15), "neutron": mp.nstr(uq + 2*dq, 15)}
    res["readings"][rn] = R
res["comparison_printed_after"] = "CODATA m_n - m_p = 1.29333 MeV (context only; nothing selected)"
s = json.dumps(res, indent=2); print(s)
open(__file__.replace('.py', '.out.json'), 'w').write(s + "\n")
