#!/usr/bin/env python3
"""qbeta_error_budget_probe — where the scored Q_β (and so m_n − m_p) loses its factor 2.4.

Pre-registered in PREREGISTRATION.md (same directory) before this file was run.
Exact sympy over Q(q) on (C²)^{⊗3}, Jimbo braiding as in
qbeta_flavour_weight_split_probe.py / NucleonWeightSpaceTraces.lean; K = diag(q, q⁻¹), u = e₁.
Numbers: mpmath at 60 dps, proton q₀ (canonical), E₀ = qbeta_e0.canonical. No float64 in any
computed value; CODATA is read only in the last section, for comparison.
"""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "computations/qbeta", "computations/substrate", "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

import qbeta_e0  # noqa: E402
import qou_substrate.constants as C  # noqa: E402

mp.mp.dps = 60
FAILED: list = []
OUT: dict = {"checks": [], "numbers": {}}


def check(name, ok, note):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {note}", flush=True)
    OUT["checks"].append({"name": name, "ok": bool(ok), "note": note})
    if not ok:
        FAILED.append(name)


def nz(x, n=12):
    return mp.nstr(x, n)


q = sp.symbols("q", positive=True)
h = q - 1 / q
D2 = q + 1 / q
R2 = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]])
I2 = sp.eye(2)
S1 = sp.kronecker_product(R2, I2)
S2 = sp.kronecker_product(I2, R2)
GENS = {"1": S1, "-1": S1.inv(), "2": S2, "-2": S2.inv()}
Kq = sp.diag(q, 1 / q)
K3 = sp.kronecker_product(sp.kronecker_product(Kq, Kq), Kq)

# basis index b = 4*s1 + 2*s2 + s3, s = 0 for e1 (u), 1 for e2 (d)
Wp = [b for b in range(8) if bin(b).count("1") == 1]  # two u, one d  (T³ = +½)
Wn = [b for b in range(8) if bin(b).count("1") == 2]  # one u, two d  (T³ = −½)


def block_tr(M, idx):
    return sp.together(sum(M[i, i] for i in idx))


V = S1 * S2.inv()
V3 = V ** 3
tau = sp.factor(block_tr(V3, Wp))
tau_n = sp.factor(block_tr(V3, Wn))
P = q**12 - 3 * q**10 + 3 * q**8 - 5 * q**6 + 3 * q**4 - 3 * q**2 + 1

print("1. Closed form of the scored cell")
check("B0 plain traces equal on W_p, W_n", sp.simplify(tau - tau_n) == 0, f"tau = {tau}")
check("B0' tau(V^3) = -P(q)/q^6", sp.simplify(tau + P / q**6) == 0, "matches the #8586 closed form")
eps = sp.together((1 / q - q) * tau / D2**3)  # ε_n − ε_p
E0_over_me = 1 / (q * (q - 1))
T = 1 / (1 - (1 - 1 / q) ** 2)
Rq = sp.factor(sp.together(E0_over_me * T * (-eps)))
R_claim = -(q + 1) * P / (q**3 * (2 * q - 1) * (q**2 + 1) ** 3)
check("B1 Q_beta/m_e = -(q+1)P(q)/(q^3(2q-1)(q^2+1)^3)", sp.simplify(Rq - R_claim) == 0, f"R(q) = {Rq}")
check("B1' E0*h = m_e (q+1)/q^2 (the 1/h of E0 cancels the h of the split)",
      sp.simplify(E0_over_me * h - (q + 1) / q**2) == 0, "pin and E0 form drop out at O(1)")
R1 = sp.limit(Rq, q, 1)
check("B2 classical limit R(1) = 3/4", R1 == sp.Rational(3, 4), f"R(1) = {R1}; tau(1) = {tau.subs(q, 1)}")

q0 = mp.mpf(C.Q_50_DIGIT_STR)
qmu = mp.mpf(C.Q_MUON_50_DIGIT_STR)
me = mp.mpf(str(C.M_E_MEV))
Rf = sp.lambdify(q, Rq, "mpmath")
Qb = me * Rf(q0)
E0 = qbeta_e0.canonical()
check("B3 reproduces the scored cell 0.325433929 MeV", abs(Qb - mp.mpf("0.325433929")) < mp.mpf("1e-9"),
      f"Q_beta = {nz(Qb, 15)} MeV; via E0 route {nz(E0 * abs(sp.lambdify(q, eps, 'mpmath')(q0)), 15)}")

print("2. Link table at q0 and at q = 1")
links = {
    "E0^order0/m_e = 1/(q(q-1))": (1 / (q * (q - 1)), None),
    "h = q - 1/q": (h, None),
    "E0^order0 * h / m_e = (q+1)/q^2": ((q + 1) / q**2, 2),
    "tau(V^3) (plain trace on W_p)": (tau, 3),
    "1/[2]^3": (1 / D2**3, sp.Rational(1, 8)),
    "tower T = 1/(1 - hbar_q^2)": (T, 1),
}
OUT["numbers"]["links"] = {}
for k, (ex, cl) in links.items():
    v = sp.lambdify(q, ex, "mpmath")(q0)
    c1 = sp.limit(ex, q, 1) if cl is not None else "diverges" if k.startswith("E0^order0/m_e") else 0
    print(f"    {k:42s} q0: {nz(v, 12):>16s}   q=1: {c1}")
    OUT["numbers"]["links"][k] = {"q0": nz(v, 20), "q1": str(c1)}
ratio = Rf(q0) / mp.mpf(3) * 4
print(f"    R(q0)/R(1) = {nz(ratio, 12)}  (all O(h) effects together)")
OUT["numbers"]["R_q0"] = nz(Rf(q0), 20)
OUT["numbers"]["R_q0_over_R1"] = nz(ratio, 20)

print("3/4. Pin sensitivity")
dlnR = sp.lambdify(q, sp.diff(sp.log(Rq), q) * q, "mpmath")(q0)
dQ = me * (Rf(qmu) - Rf(q0))
check("B4 pin lever is ppb-scale", abs(dQ / Qb) < mp.mpf("1e-7"),
      f"dlnQ/dlnq = {nz(dlnR, 8)}; muon pin moves Q_beta by {nz(dQ / Qb * 10**9, 6)} ppb")
qs = [mp.mpf(1) + mp.mpf(i) / 100 for i in range(0, 16)]
Rmax = max(Rf(x) if x != 1 else mp.mpf(3) / 4 for x in qs)
check("B4' R(q) <= 3/4 on [1, 1.15] (grid of 0.01)", Rmax <= mp.mpf(3) / 4 + mp.mpf("1e-30"),
      f"max R on grid = {nz(Rmax, 10)}; so Q_beta <= 0.75 m_e = {nz(me * 3 / 4, 8)} MeV for ANY pin in range")

print("5. Element lever: plain trace on W_p over all words of length <= 6")
q0s = sp.nsimplify(sp.Rational(str(mp.nstr(q0, 40))))
num = {}
for g, M in GENS.items():
    num[g] = (M.subs(q, 1), M.subs(q, q0s))
best1, best0, n = -10**9, -10**9, 0
worst0 = 10**9
for L in range(1, 7):
    for w in itertools.product(GENS, repeat=L):
        M1 = sp.eye(8)
        M0 = sp.eye(8)
        for g in w:
            M1 = M1 * num[g][0]
            M0 = M0 * num[g][1]
        t1 = sum(M1[i, i] for i in Wp)
        t0 = mp.mpf(sp.N(sum(M0[i, i] for i in Wp), 30))
        best1 = max(best1, t1)
        best0 = max(best0, t0)
        worst0 = min(worst0, t0)
        n += 1
check("B5 tau at q=1 is a fixed-point count, <= 3 for every word", best1 == 3,
      f"{n} words; max tau(q=1) = {best1}; tau(q0) in [{nz(worst0, 8)}, {nz(best0, 8)}]")
OUT["numbers"]["tau_q0_range_len_le_6"] = [nz(worst0, 15), nz(best0, 15)]

print("6. Normalisation of the T3 split, q = 1 coefficient of Q_beta/m_e (diagnostic, none selected)")
chi21 = sp.factor(tau - 1)  # W_p = V_{3/2} ⊗ M(3) ⊕ V_{1/2} ⊗ M(2,1); chi_(3)(V^3) = 1
norms = {
    "global [2]^3 (scored)": (1 / (q * (q - 1))) * (q - 1 / q) * tau / D2**3,
    "per-sector (own trace)": sp.Integer(0),
    "W_p + W_n quantum dim 3[2]": (1 / (q * (q - 1))) * (q - 1 / q) * tau / (3 * D2),
    "isospin-1/2 isotypic part, global [2]^3": (1 / (q * (q - 1))) * (q - 1 / q) * chi21 / D2**3,
}
OUT["numbers"]["normalisations_q1"] = {}
for k, ex in norms.items():
    c1 = sp.limit(ex, q, 1)
    print(f"    {k:42s} q=1 coefficient: {c1}")
    OUT["numbers"]["normalisations_q1"][k] = str(c1)

print("7. Comparison (CODATA, outside any proof)")
QB = mp.mpf("0.78233341")  # CODATA 2022 m_n - m_p - m_e
NP = mp.mpf("1.29333251")
F = QB / Qb
c_needed = (QB / me) / ratio
hv = q0 - 1 / q0
print(f"    Q_beta/m_e  model {nz(Qb / me, 10)}   CODATA {nz(QB / me, 10)}   F_required {nz(F, 8)}")
print(f"    m_n-m_p     model {nz(me + Qb, 10)} MeV ({nz((me + Qb) / NP * 100 - 100, 5)} %)")
print(f"    m_n error = Q_beta error: {nz(QB - Qb, 10)} MeV")
print(f"    classical coefficient needed, keeping the same O(h) shape: {nz(c_needed, 8)} (scored: 3/4)")
for k in range(1, 7):
    print(f"    single correction 1 + c h^{k}: |c| = {nz((F - 1) / hv**k, 8)}")
OUT["numbers"].update({"Q_beta": nz(Qb, 20), "F_required": nz(F, 12),
                       "classical_coefficient_needed": nz(c_needed, 12)})
(_HERE / "qbeta-error-budget.witness.json").write_text(json.dumps(OUT, indent=2, ensure_ascii=False) + "\n")
print(f"\n{len(OUT['checks']) - len(FAILED)}/{len(OUT['checks'])} checks pass")
sys.exit(1 if FAILED else 0)
