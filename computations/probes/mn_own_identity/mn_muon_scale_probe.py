"""Pre-registered in PREREGISTRATION-muon-scale.md (68658c687a0).
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
ch = {0: sp.Rational(2,3), 1: sp.Rational(-1,3)}
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
res = {"preregistration": "68658c687a0", "q0_proton_pin": mp.nstr(q0, 20),
       "Vol_4_1": mp.nstr(vol, 20), "m_mu_from_CAL2_MeV": mp.nstr(mmu0, 15), "arms": {}}
# checks
whole = lambda X: (X.trace() if False else None)
res["checks"] = {
  "K3 on W_p is q, on W_n is 1/q": blk(K3, Wp) == q*sp.eye(3) and blk(K3, Wn) == sp.eye(3)/q,
  "Vol(4_1) matches constants": abs(vol - mp.mpf(str(C.VOL_4_1_MP))) < mp.mpf('1e-40'),
}
for name, X in {"M1_D2": DD, "M2_D2_minus_S": DD - S}.items():
    d = tau_np(X)
    expr = sp.factor(sp.simplify(F_norm*d))           # (E_n-E_p)/(2 m_mu)
    val = 2*mmu0*ev(expr)
    lim = sp.limit(sp.simplify(F_norm*d*sp.Symbol('V')/hbar**2), q, 1)  # with m_e*V pole factor
    res["arms"][name] = {"tau_n_minus_tau_p": str(sp.factor(d)),
        "E_over_2m_mu": str(expr), "E_over_2m_mu_at_q0": mp.nstr(ev(expr), 15),
        "E_n_minus_E_p_MeV_at_q0": mp.nstr(val, 12),
        "limit_q_to_1_of_E_over_(m_e*Vol)": str(sp.simplify(2*lim/sp.Symbol('V')))}
# E-pot: electron-calibrated, -S
for arm, (Tn, Tp, Te) in {
    "Epot_P_plain": (blk(DD - S, Wn).trace(), blk(DD - S, Wp).trace(), (D_e*D_e).trace()),
    "Epot_K_quantum": (blk(K3*(DD - S), Wn).trace()/two**3, blk(K3*(DD - S), Wp).trace()/two**3,
                       (K3*D_e*D_e).trace()/two**3)}.items():
    r = sp.simplify((Tn - Tp)/Te)
    res["arms"][arm] = {"E_over_m_e_at_q0": mp.nstr(ev(r), 15),
        "E_n_minus_E_p_keV_at_q0": mp.nstr(1000*me*ev(r), 12), "limit_q_to_1": str(sp.limit(r, q, 1))}
res["comparison_printed_after"] = "CODATA m_n - m_p = 1.29333 MeV (context only; nothing selected)"
s = json.dumps(res, indent=2); print(s)
open(__file__.replace('.py', '.out.json'), 'w').write(s + "\n")
