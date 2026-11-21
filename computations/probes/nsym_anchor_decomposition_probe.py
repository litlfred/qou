#!/usr/bin/env python3
"""What the N_sym "anchor" 213.11 is made of, in exact arithmetic.

Block: conj:g-action-on-substrate.  Audit: docs/audits/2026-11-20-nsym-derivation.md.

computations/n_sym_numerical_anchor.py defines
    N_v^script = v / (E_x mu_0),  E_x = (q - q^-1)/2,  m_e = 3 E_x mu_0
so N_v^script = 3 v / m_e  (E_x cancels; the 3 is the trefoil crossing count of
observations/building-block-knots.md:40), and
    N_sym^anchor = N_v^script / prod_{k=2,3,4} [2k]^2/[2]
                 = 3 (m_p/m_e) (v/m_p) [2]^3 / ([4][6][8])^2.          (*)
The torus-link block (conj:electroweak-higgs-torus-link-triplet,
ElectroweakBringSchwingerBridge.lean) instead defines N_v = v/m_p and models it as
the fixed point N = T_EW - H/N + H hbar^2/N^2,
    T_EW = q([2]/2)[4][6][8] + 1/pi,  H = [2]/(8 pi),  hbar = 1 - 1/q.

This probe:
  1. checks (*) symbolically (sympy);
  2. evaluates (*) at the PROTON q0 with (i) experimental v/m_p, (ii) the block's
     fixed point, (iii) the block's tree term only;
  3. shows N_sym^anchor(q) -> infinity as q -> 1 under the proton-pin model
     m_p/m_e = F_p(q) = 2 Vol(4_1) F_Bor(q)/hbar^2 - 12, whereas every q-dimension
     of an object of Rep_q(SU(2)) (a non-negative integer combination of [n]_q)
     tends to an integer at q = 1;
  4. inverts the G_F decomposition: for each host candidate N_sym = X, the
     m_p/m_e it would require.
No value is selected by comparison with 213.11.  mpmath / sympy only.
"""
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools/qou-substrate/python"))
sys.path.insert(0, str(ROOT / "computations/substrate"))
from qou_substrate.constants import q_at, MASS_RATIO_P_E_STR  # noqa: E402
from experimental_constants import G_F_MEV, M_E_MEV  # noqa: E402

mp.mp.dps = 60

# ---- 1. symbolic identity (*) -------------------------------------------
q, v, me, mprot = sp.symbols("q v m_e m_p", positive=True)
qi = 1 / q
def Q(n):
    return (q**n - q**-n) / (q - qi)
Ex = (q - qi) / 2
mu0 = me / (3 * Ex)
Nv_script = v / (Ex * mu0)
prod_pl = (Q(4)**2 / Q(2)) * (Q(6)**2 / Q(2)) * (Q(8)**2 / Q(2))
lhs = Nv_script / prod_pl
rhs = 3 * (mprot / me) * (v / mprot) * Q(2)**3 / (Q(4) * Q(6) * Q(8))**2
assert sp.simplify(lhs - rhs) == 0
print("(*) N_sym^anchor = 3 (m_p/m_e)(v/m_p) [2]^3/([4][6][8])^2   [sympy: exact]")

# ---- 2. numerics at proton q0 -------------------------------------------
q0 = q_at(60)
def qn(n, x=q0):
    return (x**n - x**-n) / (x - 1 / x)
pe = mp.mpf(MASS_RATIO_P_E_STR)
GF = mp.mpf(str(G_F_MEV))          # MeV^-2
me_mev = mp.mpf(str(M_E_MEV))
v_mev = 1 / mp.sqrt(mp.sqrt(2) * GF)
mp_mev = pe * me_mev
Nv_exp = v_mev / mp_mev
hb = 1 - 1 / q0
T_tree = q0 * qn(2) / 2 * qn(4) * qn(6) * qn(8)
T_EW = T_tree + 1 / mp.pi
H = qn(2) / (8 * mp.pi)
Nv_fp = mp.findroot(lambda N: N - (T_EW - H / N + H * hb**2 / N**2), T_EW)
weak = qn(2)**3 / (qn(4) * qn(6) * qn(8))**2
print("proton q0         =", mp.nstr(q0, 30))
print("m_p/m_e (CODATA22)=", MASS_RATIO_P_E_STR)
for lab, Nv in [("exp v/m_p", Nv_exp), ("block fixed point", Nv_fp),
                ("block T_EW (tree+1/pi)", T_EW), ("block tree only", T_tree)]:
    print(f"N_v={mp.nstr(Nv, 15):>20}  [{lab}]  ->  N_sym^anchor = {mp.nstr(3*pe*Nv*weak, 15)}")
print("script form 3v/m_e / prod  =", mp.nstr(3 * v_mev / me_mev /
      ((qn(4)**2/qn(2))*(qn(6)**2/qn(2))*(qn(8)**2/qn(2))), 15))
print("weak factor N_v^fp [2]^3/([4][6][8])^2 =", mp.nstr(Nv_fp * weak, 15))
print("leading (3/2)(m_p/m_e) q [2]^4/([4][6][8]) =",
      mp.nstr(mp.mpf(3) / 2 * pe * q0 * qn(2)**4 / (qn(4) * qn(6) * qn(8)), 15))
print("block N_v residual vs exp (ppb):", mp.nstr((Nv_fp / Nv_exp - 1) * 10**9, 6))

# ---- 3. q -> 1 behaviour --------------------------------------------------
Vol = 2 * mp.clsin(2, mp.pi / 3)
def Fp(x):
    h = x - 1 / x
    hbx = 1 - 1 / x
    trM = abs((4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4))
    qf3 = (x**2 + 1 + x**-2) * (x + 1 / x)
    return 2 * Vol / hbx**2 * (trM * qf3 / x**3) - 12
assert abs(Fp(q0) / pe - 1) < mp.mpf("1e-40")   # q0 is the root of F_p = m_p/m_e
def anchor_model(x):
    T = x * qn(2, x) / 2 * qn(4, x) * qn(6, x) * qn(8, x) + 1 / mp.pi
    Hx = qn(2, x) / (8 * mp.pi)
    hbx = 1 - 1 / x
    N = mp.findroot(lambda N: N - (T - Hx / N + Hx * hbx**2 / N**2), T)
    return 3 * Fp(x) * N * qn(2, x)**3 / (qn(4, x) * qn(6, x) * qn(8, x))**2
print("q -> 1 (proton-pin model, m_p/m_e = F_p(q)):")
for e in ["1e-1", "1e-2", "1e-3", "1e-4"]:
    x = 1 + mp.mpf(e)
    val = anchor_model(x)
    print(f"  q=1+{e}: N_sym^anchor = {mp.nstr(val, 10)};  (q-1)^2 * it = "
          f"{mp.nstr(val * (x - 1)**2, 10)}")
lim = 3 * 12 * Vol * (192 + 1 / mp.pi) * 8 / 192**2  # crude q=1 tree check
print("  host q-dims at q=1: [3]^2 -> 9, [4][6] -> 24, [4]^2[6] -> 96, 2[4]+[6] -> 14")

# ---- 4. inversion: required m_p/m_e for each host candidate ---------------
cands = {
    "[3]^2 (slot derivation)": qn(3)**2,
    "[3]^3 (E(+,+,+))": qn(3)**3,
    "(a) [4]^2[6]": qn(4)**2 * qn(6),
    "(b) 2[4]+[6]": 2 * qn(4) + qn(6),
    "(c) [4][6]": qn(4) * qn(6),
}
print("If N_sym = X and N_v = v/m_p is the block fixed point, G_F requires")
print("m_p/m_e = X ([4][6][8])^2 / (3 [2]^3 N_v):")
for k, X in cands.items():
    req = X / (3 * Nv_fp * weak)
    print(f"  {k:28s} X={mp.nstr(X, 12):>14}  m_p/m_e_req={mp.nstr(req, 10):>12}"
          f"  ({mp.nstr((req/pe-1)*100, 5)} % vs CODATA)")
