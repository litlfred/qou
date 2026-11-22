"""Pre-registered in PREREGISTRATION-em-term.md (written before this file was run).
EM-1: E_n - E_p = m_e * alpha * [tr_Wn(K S) - tr_Wp(K S)] / tr(K D_e^2)   (electron map, +alpha*S,
      Coulomb sign imported); plain-trace variant reported as a labelled diagnostic.
EM-2: E_n - E_p = 2 m_mu ([3]!/q^3) * alpha * (tau_n - tau_p)(S)          (muon map, stated alternative).
alpha(q) = q^-1/([9]_q [10]_q)  (prop:em-coupling-projection; Lean isEmCoupling_iff, defining relation).
S = QPair*hol, adopted charges +2/3, -1/3 (conditional: owner ruling 2026-11-22, q_i must be derived).
Exact sympy in q; mpmath 60 dps at the proton pin Q_50_DIGIT_STR. No float64.
"""
import json, itertools, sympy as sp, mpmath as mp
from qou_substrate import constants as C

q = sp.symbols('q', positive=True)
Rc = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, q - 1/q, 0], [0, 0, 0, q]])
I2, I8 = sp.eye(2), sp.eye(8)
s0 = sp.kronecker_product(Rc, I2); s1 = sp.kronecker_product(I2, Rc)
basis = list(itertools.product([0, 1], repeat=3))          # 0 = u, 1 = d
T3 = sp.diag(*[sp.Rational(b.count(0) - b.count(1), 2) for b in basis])
K3 = sp.diag(*[q**(b.count(0) - b.count(1)) for b in basis])
ch = {0: sp.Rational(2, 3), 1: sp.Rational(-1, 3)}
QPair = sp.diag(*[sum(ch[b[i]]*ch[b[j]] for i in range(3) for j in range(i+1, 3)) for b in basis])
two = q + 1/q; three = q**2 + 1 + q**-2
hol_N = sp.simplify((s0*s1.inv())**3); X_e = sp.simplify(s0*s1*s0)
def D(hol, wr): return (hol - q**wr*I8)/q + (1 - 1/q)*T3
D_e = D(X_e, 3)
Wp = [i for i, b in enumerate(basis) if b.count(0) == 2]
Wn = [i for i, b in enumerate(basis) if b.count(0) == 1]
blk = lambda M, idx: M.extract(idx, idx)
S = QPair*hol_N
qint = lambda n: sp.cancel((q**n - q**-n)/(q - 1/q))
alpha = sp.cancel(q**-1/(qint(9)*qint(10)))
F_norm = two*three/q**3
hbar = 1 - 1/q

mp.mp.dps = 60
q0 = mp.mpf(C.Q_50_DIGIT_STR); me = mp.mpf(C.M_E_MEV_STR)
vol = 2*mp.clsin(2, mp.pi/3)
mmu0 = me*vol/(1 - 1/q0)**2
ev = lambda e, x=q0: sp.lambdify(q, e, "mpmath")(x)
at1 = lambda e: sp.cancel(sp.together(e)).subs(q, 1)

res = {"preregistration": "PREREGISTRATION-em-term.md", "q0_proton_pin": mp.nstr(q0, 25),
       "alpha_element": "q^-1/([9]_q[10]_q)",
       "alpha_at_q0": mp.nstr(ev(alpha), 20), "inv_alpha_at_q0": mp.nstr(1/ev(alpha), 20),
       "alpha_at_q=1": str(at1(alpha)),
       "checks": {}, "arms": {}}
res["checks"]["QPair_p_trace_over_Wp_diag_sum"] = str(sum(QPair[i, i] for i in Wp))
res["checks"]["QPair per basis state: p (uud) = 0, n (udd) = -1/3"] = (
    all(QPair[i, i] == 0 for i in Wp) and all(QPair[i, i] == sp.Rational(-1, 3) for i in Wn))
res["checks"]["K3 on W_p = q, W_n = 1/q"] = (blk(K3, Wp) == q*sp.eye(3) and blk(K3, Wn) == sp.eye(3)/q)

# ---- EM-1 (candidate): electron map, +alpha*S, K-weighted; plain as labelled diagnostic ----
TeK = (K3*D_e*D_e).trace()/two**3; TeP = (D_e*D_e).trace()
for name, (num, Te) in {
        "EM1_K_weighted_CANDIDATE": ((blk(K3*S, Wn).trace() - blk(K3*S, Wp).trace())/two**3, TeK),
        "EM1_plain_diagnostic": (blk(S, Wn).trace() - blk(S, Wp).trace(), TeP),
        "diag_QPair_without_hol_K_NOT_A_CANDIDATE": (
            (blk(K3*QPair, Wn).trace() - blk(K3*QPair, Wp).trace())/two**3, TeK)}.items():
    r_noalpha = sp.cancel(sp.together(num/Te))
    r = sp.cancel(alpha*r_noalpha)
    v = ev(r); v1 = at1(r)
    near = {f"q=1+1e-{k}": mp.nstr(1000*me*ev(r, 1 + mp.mpf(10)**-k), 15) for k in (2, 4, 8)}
    res["arms"][name] = {
        "S_part_without_alpha_E_over_m_e_at_q0": mp.nstr(ev(r_noalpha), 15),
        "E_over_m_e_at_q0": mp.nstr(v, 15),
        "E_n_minus_E_p_keV_at_q0": mp.nstr(1000*me*v, 12),
        "E_over_m_e_at_q=1_exact": str(v1),
        "E_n_minus_E_p_keV_at_q=1": mp.nstr(1000*me*mp.mpf(sp.Rational(v1).p)/sp.Rational(v1).q, 12)
            if v1.is_rational else str(v1),
        "keV_approaching_q=1": near}

# ---- EM-2 (stated alternative): muon map ----
d = sp.cancel(sp.together((blk(K3*S, Wn).trace() - blk(K3*S, Wp).trace())/two**3))
expr = sp.cancel(F_norm*alpha*d)                      # (E_n - E_p)/(2 m_mu)
pole_coeff = at1(expr)                                # E*hbar^2/(2 m_e Vol) at q=1
res["arms"]["EM2_muon_map_ALTERNATIVE"] = {
    "E_over_2m_mu_at_q0": mp.nstr(ev(expr), 15),
    "E_n_minus_E_p_MeV_at_q0": mp.nstr(2*mmu0*ev(expr), 12),
    "hbar_q^2*E/(m_e*Vol(4_1)) at q=1 (pole coefficient)": str(2*pole_coeff),
    "divergence": "E ~ 2 m_e Vol(4_1) * coeff / hbar_q^2 as q -> 1" if pole_coeff != 0 else "none",
    "MeV_approaching_q=1": {f"q=1+1e-{k}": mp.nstr(
        2*me*vol/(1 - 1/(1 + mp.mpf(10)**-k))**2*ev(expr, 1 + mp.mpf(10)**-k), 12) for k in (2, 4, 8)}}

# ---- predictions vs results ----
em1 = ev(sp.cancel(alpha*sp.together(((blk(K3*S, Wn).trace() - blk(K3*S, Wp).trace())/two**3)/TeK)))
em1P = ev(sp.cancel(alpha*sp.together((blk(S, Wn).trace() - blk(S, Wp).trace())/TeP)))
em2 = 2*mmu0*ev(expr)
res["predictions_checked"] = {
    "P1 EM-1 negative": bool(em1 < 0),
    "P2 EM-1 ~ -0.36 keV (K) / -0.40 keV (plain)": [mp.nstr(1000*me*em1, 6), mp.nstr(1000*me*em1P, 6)],
    "P3 EM-1 at q=1 = -1/720 m_e": str(at1(sp.cancel(alpha*sp.together(((blk(K3*S, Wn).trace()
                                    - blk(K3*S, Wp).trace())/two**3)/TeK)))),
    "P4 |EM-1| outside [0.1, 10] MeV => refuted as the EM part": bool(abs(me*em1) < mp.mpf('0.1')),
    "P5 EM-2 ~ -0.76 MeV and divergent": [mp.nstr(em2, 6), pole_coeff != 0],
}
res["comparison_printed_after"] = {
    "CODATA_mn_minus_mp_MeV": "1.29333",
    "BMW2015_lattice_QED_part_MeV": "-1.00 (approx)",
    "EM1_K_over_lattice_QED": mp.nstr(me*em1/mp.mpf('-1.00'), 6),
    "EM2_over_lattice_QED": mp.nstr(em2/mp.mpf('-1.00'), 6),
    "note": "EM-2 agreement was foreseeable at pre-registration and carries no evidential weight; "
            "EM-2 rides the hbar_q^-2 pole and is not adopted."}
s = json.dumps(res, indent=2, default=str); print(s)
open(__file__.replace('.py', '.out.json'), 'w').write(s + "\n")
