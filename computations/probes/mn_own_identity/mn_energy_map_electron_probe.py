"""Pre-registered in PREREGISTRATION-energy-map-electron-calibration.md (f3df20ab89a).
Exact sympy; pin evaluation with mpmath at 60 dps. No float64.
"""
import json, itertools, sympy as sp, mpmath as mp
from qou_substrate import constants as C

q = sp.symbols('q', positive=True)
Rc = sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,q-1/q,0],[0,0,0,q]])
I2, I8 = sp.eye(2), sp.eye(8)
s0 = sp.kronecker_product(Rc, I2); s1 = sp.kronecker_product(I2, Rc)
basis = list(itertools.product([0,1], repeat=3))           # 0 = up
T3 = sp.diag(*[sp.Rational(b.count(0) - b.count(1), 2) for b in basis])
K3 = sp.diag(*[q**(b.count(0) - b.count(1)) for b in basis])  # K^{(x)3}, K = q^{2 T3} per strand
two = q + 1/q
hol_N = sp.simplify((s0*s1.inv())**3)                      # writhe 0
X_e = sp.simplify(s0*s1*s0)                                # writhe 3
def D(hol, wr): return (hol - q**wr*I8)/q + (1 - 1/q)*T3
D_N, D_e = D(hol_N, 0), D(X_e, 3)
Wp = [i for i,b in enumerate(basis) if b.count(0) == 2]
Wn = [i for i,b in enumerate(basis) if b.count(0) == 1]
def blk(M, idx): return M.extract(idx, idx)
DN2, De2 = D_N*D_N, D_e*D_e
arms = {}
# P: plain
Tp, Tn = sp.simplify(blk(DN2, Wp).trace()), sp.simplify(blk(DN2, Wn).trace())
Te = sp.simplify(De2.trace())
arms["P_plain"] = (Tp, Tn, Te)
# K: Tr(K^3 .)/[2]^3
KTp = sp.simplify((blk(K3*DN2, Wp)).trace()/two**3)
KTn = sp.simplify((blk(K3*DN2, Wn)).trace()/two**3)
KTe = sp.simplify((K3*De2).trace()/two**3)
arms["K_quantum"] = (KTp, KTn, KTe)
mp.mp.dps = 60
q0 = mp.mpf(C.Q_50_DIGIT_STR)
me = mp.mpf(C.M_E_MEV_STR)
res = {"preregistration": "f3df20ab89a", "q0_proton_pin": mp.nstr(q0, 20), "arms": {},
       "checks": {"hecke": sp.simplify((Rc-q*sp.eye(4))*(Rc+sp.eye(4)/q)) == sp.zeros(4),
                  "Wp, Wn invariant under D_N": all(
                      sp.simplify(D_N.extract([i for i in range(8) if i not in W], W)) == sp.zeros(5,3)
                      for W in (Wp, Wn))}}
for name, (Tp_, Tn_, Te_) in arms.items():
    ratio = sp.factor(sp.simplify((Tn_ - Tp_)/Te_))
    f = sp.lambdify(q, ratio, "mpmath"); fe = sp.lambdify(q, Te_, "mpmath")
    Te0 = fe(q0); r0 = f(q0)
    res["arms"][name] = {
        "T_e": str(sp.factor(Te_)), "T_e_at_q0": mp.nstr(Te0, 15),
        "lambda_sign": "+" if Te0 > 0 else ("-" if Te0 < 0 else "0"),
        "Delta_N": str(sp.factor(sp.simplify(Tn_ - Tp_))),
        "E_n_minus_E_p_over_m_e": str(ratio),
        "E_n_minus_E_p_over_m_e_at_q0": mp.nstr(r0, 15),
        "E_n_minus_E_p_MeV_at_q0": mp.nstr(r0*me, 15),
        "limit_q_to_1_of_ratio": str(sp.limit(ratio, q, 1)),
    }
res["m_e_MeV"] = mp.nstr(me, 15)
res["comparison_printed_after"] = "CODATA m_n - m_p = 1.29333 MeV (context only; nothing selected)"
s = json.dumps(res, indent=2); print(s)
open(__file__.replace('.py', '.out.json'), 'w').write(s + "\n")
