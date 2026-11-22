"""Pre-registered in PREREGISTRATION-em-scale-derivation.md (be98c91fbf6, written before this file).

C1: word-level Coulomb channel 1/2 (n_+ + n_-)(q - q^-1) of def:coulomb-charge; p and n share V^3.
C2: tanh(ln q) * E_M1,  E_M1 = 2 m_mu ([3]!/q^3)(tau_n - tau_p)(D^2)   (weak: transport is a choice).
C3: M_QCD * (a_n - a_p),  M_QCD = 2 m_mu |tr_M(beta_Bor)| [3]!/q^3     (scalar_insertion_shift),
    a_W = alpha * tr_W(K S) / tr_W(K hol);  sector-share variant as a labelled diagnostic.
alpha = q^-1/([9]_q[10]_q); S = QPair*hol, adopted charges +2/3, -1/3; option A sign (+alpha*S).
Exact sympy over Q(q); mpmath 60 dps at the proton pin Q_50_DIGIT_STR. No float64.
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
h = q - 1/q
V = s0*s1.inv()
hol = sp.simplify(V**3)
D_N = (hol - I8)/q + (1 - 1/q)*T3
Wp = [i for i, b in enumerate(basis) if b.count(0) == 2]
Wn = [i for i, b in enumerate(basis) if b.count(0) == 1]
blk = lambda M, idx: M.extract(idx, idx)
S = QPair*hol
qint = lambda n: sp.cancel((q**n - q**-n)/(q - 1/q))
alpha = sp.cancel(q**-1/(qint(9)*qint(10)))
F_norm = two*three/q**3                                      # [3]_q!/q^3
trM_bor = (4 + h**2 - 3*h**4 - h**6)/(h**2 + 4)              # BorromeanMarkovTrace.lean, conv. D
tanh_lnq = (q**2 - 1)/(q**2 + 1)                             # prop:coulomb-strong-ratio-q-rational
hbar = 1 - 1/q

mp.mp.dps = 60
q0 = mp.mpf(C.Q_50_DIGIT_STR); me = mp.mpf(C.M_E_MEV_STR)
vol = 2*mp.clsin(2, mp.pi/3)
ev = lambda e, x=q0: sp.lambdify(q, e, "mpmath")(x)
mmu = lambda x: me*vol/(1 - 1/x)**2
lim1 = lambda e: sp.limit(sp.cancel(sp.together(e)), q, 1)
near = lambda f: {f"q=1+1e-{k}": mp.nstr(f(1 + mp.mpf(10)**-k), 15) for k in (2, 4, 8)}

res = {"preregistration": "PREREGISTRATION-em-scale-derivation.md (be98c91fbf6)",
       "q0_proton_pin": mp.nstr(q0, 25), "alpha_at_q0": mp.nstr(ev(alpha), 20),
       "tanh_ln_q0": mp.nstr(ev(tanh_lnq), 20), "trM_Bor_at_q0": mp.nstr(ev(trM_bor), 20),
       "checks": {}, "candidates": {}}
res["checks"]["Vol(4_1) matches constants"] = bool(abs(vol - mp.mpf(str(C.VOL_4_1_MP))) < mp.mpf('1e-40'))
res["checks"]["hol = 1 at q = 1"] = (hol.subs(q, 1) == I8)
res["checks"]["tanh(ln q0) = (q0^2-1)/(q0^2+1)"] = bool(abs(mp.tanh(mp.log(q0)) - ev(tanh_lnq)) < mp.mpf('1e-55'))

# ---- C1: word-level crossing-energy Coulomb channel ----
word = [(0, +1), (1, -1)]*3                                  # V^3 = (s0 s1^-1)^3, shared by p and n
n_plus = sum(1 for _, e in word if e > 0); n_minus = sum(1 for _, e in word if e < 0)
coul = sp.Rational(1, 2)*(n_plus + n_minus)*h
strong = sp.Rational(1, 2)*(n_plus - n_minus)*two
res["candidates"]["C1_crossing_energy_coulomb_channel"] = {
    "n_plus": n_plus, "n_minus": n_minus,
    "coulomb_channel_each_nucleon": str(sp.factor(coul)), "strong_channel_each_nucleon": str(strong),
    "Delta_n_minus_p_exact": "0 (same word for both nucleons)",
    "note": "word-level channel is blind to the weight-block label; ratio tanh(ln q) undefined "
            "here because the symmetric channel is 0 (n_+ = n_-)"}

# ---- C2: tanh(ln q) * E_M1 ----
dD2 = sp.cancel(sp.together((blk(K3*D_N*D_N, Wn).trace() - blk(K3*D_N*D_N, Wp).trace())/two**3))
eM1_over_2mmu = sp.cancel(F_norm*dD2)
c2_over_2mmu = sp.cancel(tanh_lnq*eM1_over_2mmu)
eps = sp.symbols('epsilon')
ser = sp.series(sp.cancel(2*c2_over_2mmu/hbar**2).subs(q, 1 + eps), eps, 0, 4).removeO()
res["candidates"]["C2_tanh_times_D2_arm_WEAK"] = {
    "E_M1_MeV_at_q0": mp.nstr(2*mmu(q0)*ev(eM1_over_2mmu), 15),
    "E_C2_MeV_at_q0": mp.nstr(2*mmu(q0)*ev(c2_over_2mmu), 15),
    "E_C2_over_(m_e Vol) series in eps=q-1": str(sp.expand(ser)),
    "E_C2_MeV_approaching_q=1": near(lambda x: 2*mmu(x)*ev(c2_over_2mmu, x)),
    "uses_quark_charges": False}

# ---- C3: degree-0 insertion on the canonical nucleon functional ----
trKhol_n = sp.cancel(blk(K3*hol, Wn).trace()); trKhol_p = sp.cancel(blk(K3*hol, Wp).trace())
a_n = sp.cancel(alpha*blk(K3*S, Wn).trace()/trKhol_n)
a_p = sp.cancel(alpha*blk(K3*S, Wp).trace()/trKhol_p)
MQCD_over_2mmu = sp.cancel(trM_bor*F_norm)
c3_over_2mmu = sp.cancel(MQCD_over_2mmu*(a_n - a_p))
pole = lim1(2*c3_over_2mmu)                                  # hbar^2 E/(m_e Vol) at q=1
share = sp.cancel(MQCD_over_2mmu*alpha*(blk(K3*S, Wn).trace() - blk(K3*S, Wp).trace())/two**3)
res["candidates"]["C3_insertion_on_canonical_functional"] = {
    "M_QCD_MeV_at_q0": mp.nstr(2*mmu(q0)*ev(MQCD_over_2mmu), 15),
    "tr_Wn(K hol)_at_q0": mp.nstr(ev(trKhol_n), 15), "tr_Wp(K hol)_at_q0": mp.nstr(ev(trKhol_p), 15),
    "a_n_over_alpha_at_q0": mp.nstr(ev(sp.cancel(a_n/alpha)), 15),
    "a_p_over_alpha_at_q0": mp.nstr(ev(sp.cancel(a_p/alpha)), 15),
    "a_n_at_q=1": str(lim1(a_n)), "a_p_at_q=1": str(lim1(a_p)),
    "E_C3_MeV_at_q0": mp.nstr(2*mmu(q0)*ev(c3_over_2mmu), 15),
    "E_C3_over_M_QCD_at_q0": mp.nstr(ev(sp.cancel(c3_over_2mmu/MQCD_over_2mmu)), 15),
    "E_C3_over_M_QCD_at_q=1": str(lim1(c3_over_2mmu/MQCD_over_2mmu)),
    "hbar_q^2*E_C3/(m_e*Vol(4_1)) at q=1 (pole coefficient)": str(pole),
    "E_C3_MeV_approaching_q=1": near(lambda x: 2*mmu(x)*ev(c3_over_2mmu, x)),
    "diagnostic_sector_share_variant_MeV_at_q0 (= EM-2 * |tr_M|)": mp.nstr(2*mmu(q0)*ev(share), 15)}

c2 = 2*mmu(q0)*ev(c2_over_2mmu); c3 = 2*mmu(q0)*ev(c3_over_2mmu)
res["predictions_checked"] = {
    "C1 Delta = 0 exactly": True,
    "C2 ~ +0.018 MeV at q0": mp.nstr(c2, 6),
    "C2 -> 0 like -(9/4) m_e Vol eps^2": str(sp.expand(ser).coeff(eps, 2)),
    "C3 negative": bool(c3 < 0),
    "C3 magnitude in [1.5, 3.5] MeV": bool(mp.mpf('1.5') <= abs(c3) <= mp.mpf('3.5')),
    "C3 pole coefficient = -2/45": str(pole),
}
res["comparison_printed_after"] = {
    "BMW2015_lattice_QED_part_MeV": "-1.00 (approx)", "CODATA_mn_minus_mp_MeV": "1.29333",
    "EM1_keV": "-0.358", "EM2_MeV": "-0.764",
    "C3_over_lattice_QED": mp.nstr(c3/mp.mpf('-1.00'), 6),
    "C2_over_lattice_QED": mp.nstr(c2/mp.mpf('-1.00'), 6),
    "note": "target known before registration; no candidate adopted; scope (a)"}
s = json.dumps(res, indent=2, default=str); print(s)
open(__file__.replace('.py', '.out.json'), 'w').write(s + "\n")
