"""Pre-registered in PREREGISTRATION-static-charge-term.md (ea8659cff5a).
L' = D^2 + S, S = QPair * hol (QPair = 0 on W_p, -1/3 on W_n); electron S = 0 (no quark strands).
E = lambda * T(L'), lambda = m_e / T(L'_e). Exact sympy; mpmath 60 dps at the proton pin. No float64.
"""
import json, itertools, sympy as sp, mpmath as mp
from qou_substrate import constants as C

q = sp.symbols('q', positive=True)
Rc = sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,q-1/q,0],[0,0,0,q]])
I2, I8 = sp.eye(2), sp.eye(8)
s0 = sp.kronecker_product(Rc, I2); s1 = sp.kronecker_product(I2, Rc)
basis = list(itertools.product([0,1], repeat=3))            # 0 = up
T3 = sp.diag(*[sp.Rational(b.count(0) - b.count(1), 2) for b in basis])
K3 = sp.diag(*[q**(b.count(0) - b.count(1)) for b in basis])
ch = {0: sp.Rational(2,3), 1: sp.Rational(-1,3)}
QPair = sp.diag(*[sum(ch[b[i]]*ch[b[j]] for i in range(3) for j in range(i+1,3)) for b in basis])
two = q + 1/q
hol_N = sp.simplify((s0*s1.inv())**3)
X_e = sp.simplify(s0*s1*s0)
def D(hol, wr): return (hol - q**wr*I8)/q + (1 - 1/q)*T3
D_N, D_e = D(hol_N, 0), D(X_e, 3)
Wp = [i for i,b in enumerate(basis) if b.count(0) == 2]
Wn = [i for i,b in enumerate(basis) if b.count(0) == 1]
blk = lambda M, idx: M.extract(idx, idx)
LN = D_N*D_N + QPair*hol_N          # L' for the nucleon
Le = D_e*D_e                        # electron: S = 0 (pre-registered assumption)
arms = {
  "P_plain": (blk(LN, Wp).trace(), blk(LN, Wn).trace(), Le.trace(),
              blk(QPair*hol_N, Wn).trace() - blk(QPair*hol_N, Wp).trace()),
  "K_quantum": (blk(K3*LN, Wp).trace()/two**3, blk(K3*LN, Wn).trace()/two**3, (K3*Le).trace()/two**3,
                (blk(K3*QPair*hol_N, Wn).trace() - blk(K3*QPair*hol_N, Wp).trace())/two**3),
}
mp.mp.dps = 60
q0 = mp.mpf(C.Q_50_DIGIT_STR); me = mp.mpf(C.M_E_MEV_STR)
h = q - 1/q
res = {"preregistration": "ea8659cff5a", "q0_proton_pin": mp.nstr(q0, 20), "m_e_MeV": mp.nstr(me, 15),
       "checks": {
         "QPair on W_p is 0": blk(QPair, Wp) == sp.zeros(3),
         "QPair on W_n is -1/3": blk(QPair, Wn) == -sp.Rational(1,3)*sp.eye(3),
         "plain Delta_S = -1 + h^4[3]/3 (Lean delta_static)": sp.simplify(arms["P_plain"][3]
              - (-1 + h**4*(q**2+1+q**-2)/3)) == 0,
       }, "arms": {}}
for name, (Tp, Tn, Te, DS) in arms.items():
    ratio = sp.simplify((Tn - Tp)/Te)
    f = sp.lambdify(q, ratio, "mpmath")
    r0 = f(q0)
    res["arms"][name] = {
        "Delta_S": str(sp.factor(sp.simplify(DS))),
        "T_e_at_q0": mp.nstr(sp.lambdify(q, Te, "mpmath")(q0), 15),
        "E_n_minus_E_p_over_m_e": str(sp.factor(ratio)),
        "E_n_minus_E_p_over_m_e_at_q0": mp.nstr(r0, 15),
        "E_n_minus_E_p_keV_at_q0": mp.nstr(1000*r0*me, 12),
        "limit_q_to_1": str(sp.limit(ratio, q, 1)),
    }
res["comparison_printed_after"] = "CODATA m_n - m_p = 1293.33 keV (context only; nothing selected)"
s = json.dumps(res, indent=2); print(s)
open(__file__.replace('.py', '.out.json'), 'w').write(s + "\n")
