#!/usr/bin/env python3
"""N3 (bean qou-99qc, 2026-11-20): the beta-decay amplitude as a T+ matrix element.

Pre-registration: computations/probes/qbeta_n3/PREREGISTRATION.md (committed first).
Lean twin: QOU/QuarkState/TPlusChargedCurrentElement.lean (sorry-free).

Everything symbolic is exact sympy over Q(q); numbers are mpmath at 70 dps at the
PROTON q0 (qou_substrate.constants.q_at). CODATA Q_beta and tau_n appear only in the
comparison block. No float arithmetic.

Readings (pre-registered ids):
  A  Hecke-energy difference across T+  (expected 0 identically)
  B  normalised |<p|T+|n>|^2 per isospin (expected 1 and [2]^2)
  C  charged-current exchange amplitude of the weak insertion -h P_L on one
     quark-lepton crossing (expected -h q^{+-1}/[2])
  D  |M|^2 = B * C^2 cells, q->1 order, bar parity, monotonicity
  E  Q_beta from the construction (expected: not produced)
"""
from __future__ import annotations

import json
import os
import sys

import sympy as sp
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools", "qou-substrate", "python"))
from qou_substrate import constants as C  # noqa: E402

mp.mp.dps = 70
q = sp.symbols("q", positive=True)
h = q - 1 / q
b2 = q + 1 / q
checks: list[tuple[str, bool]] = []


def check(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)


# ---------------------------------------------------------------- 8x8 model
# V = span(u, d); basis of V^{(x)3} indexed by tuples, u=0, d=1.
Rc = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]])  # uu,ud,du,dd
I2 = sp.eye(2)
s1 = sp.kronecker_product(Rc, I2)
s2 = sp.kronecker_product(I2, Rc)
E = sp.Matrix([[0, 1], [0, 0]])
Fm = sp.Matrix([[0, 0], [1, 0]])
Km = sp.diag(q, 1 / q)
# Delta^2(E) = E(x)K(x)K + 1(x)E(x)K + 1(x)1(x)E  (Delta(E)=E(x)K+1(x)E)
DE = (sp.kronecker_product(E, Km, Km) + sp.kronecker_product(I2, E, Km)
      + sp.kronecker_product(I2, I2, E))
DF = (sp.kronecker_product(Fm, I2, I2) + sp.kronecker_product(Km.inv(), Fm, I2)
      + sp.kronecker_product(Km.inv(), Km.inv(), Fm))
check("sigma1 commutes with Delta^2(E)", sp.simplify(s1 * DE - DE * s1) == sp.zeros(8))
check("sigma2 commutes with Delta^2(E)", sp.simplify(s2 * DE - DE * s2) == sp.zeros(8))

idx = {(a, b, c): 4 * a + 2 * b + c for a in (0, 1) for b in (0, 1) for c in (0, 1)}
Wm = [idx[(0, 1, 1)], idx[(1, 0, 1)], idx[(1, 1, 0)]]  # udd, dud, ddu  (neutron)
Wp = [idx[(1, 0, 0)], idx[(0, 1, 0)], idx[(0, 0, 1)]]  # duu, udu, uud  (proton)
Eu = DE.extract(Wp, Wm)
Fd = DF.extract(Wm, Wp)
sm1, sm2 = s1.extract(Wm, Wm), s2.extract(Wm, Wm)
sp1, sp2 = s1.extract(Wp, Wp), s2.extract(Wp, Wp)
check("Fd == Eu^T (T- is the transpose of T+ in the weight basis)",
      sp.simplify(Fd - Eu.T) == sp.zeros(3))
check("Hecke generators symmetric on W-, W+",
      all(sp.simplify(M - M.T) == sp.zeros(3) for M in (sm1, sm2, sp1, sp2)))

# ---- A: Hecke energies across T+. beta_Bor = V^3, V = sigma1 sigma2^{-1}
Vm = sm1 * sm2.inv()
Vp = sp1 * sp2.inv()
Bm, Bp = sp.simplify(Vm ** 3), sp.simplify(Vp ** 3)
check("Eu * beta_Bor(W-) == beta_Bor(W+) * Eu", sp.simplify(Eu * Bm - Bp * Eu) == sp.zeros(3))
x = sp.symbols("x")
cpm = sp.factor(Bm.charpoly(x).as_expr())
cpp = sp.factor(Bp.charpoly(x).as_expr())
check("A: char poly of beta_Bor equal on W- and W+ (Hecke energy difference 0)",
      sp.simplify(cpm - cpp) == 0)

# ---- B: hadronic normalised |<p|T+|n>|^2
FE = sp.simplify(Fd * Eu)
ev = {sp.simplify(k): v for k, v in FE.eigenvals().items()}
check("B: T-T+ eigenvalues on W- are {[2]^2 (x1), 1 (x2)}",
      sorted(ev.values()) == [1, 2] and any(sp.simplify(k - b2 ** 2) == 0 for k in ev)
      and any(sp.simplify(k - 1) == 0 for k in ev))
B_half, B_32 = sp.Integer(1), sp.simplify(b2 ** 2)

# ---- C: lepton crossing, weak insertion -h P_L with P_L = P+ = (R + q^-1)/[2]
Pp = (Rc + sp.eye(4) / q) / b2
check("P+ idempotent and q-eigen", sp.simplify(Pp * Pp - Pp) == sp.zeros(4)
      and sp.simplify(Rc * Pp - q * Pp) == sp.zeros(4))
ins = -h * Pp
C_left = sp.simplify(ins[2, 2])   # input du (quark d left, lepton nu right) -> du
C_right = sp.simplify(ins[1, 1])  # input ud (lepton nu left, quark d right) -> ud
check("C: left amplitude == -h q/[2]", sp.simplify(C_left + h * q / b2) == 0)
check("C: right amplitude == -h q^-1/[2]", sp.simplify(C_right + h / (q * b2)) == 0)
check("C: bar sends left to -right",
      sp.simplify(C_left.subs(q, 1 / q) + C_right) == 0)
# bare letter carries exchange h on du only (no weak insertion needed for a label swap)
check("bare sigma exchange amplitudes (du: h, ud: 0)",
      sp.simplify(Rc[2, 2] - h) == 0 and Rc[1, 1] == 0)

# ---- D: |M|^2 cells and properties
cells = {}
for iso, Bv in (("isospin_1/2", B_half), ("isospin_3/2", B_32)):
    for pl, Cv in (("quark_left", C_left), ("quark_right", C_right)):
        cells[f"{iso}|{pl}"] = sp.factor(sp.simplify(Bv * Cv ** 2))
lam = sp.symbols("lam")
for k, v in cells.items():
    ser = sp.series(v.subs(q, sp.exp(lam)), lam, 0, 4).removeO()
    print(f"  |M|^2 {k} = {v}   ~ {sp.simplify(ser)}")
lead = sp.series(C_left.subs(q, sp.exp(lam)), lam, 0, 2).removeO()
check("q->1: amplitude = -lam + O(lam^2) = -tanh(lam)e^lam (order h^1), rate order h^2",
      sp.simplify(lead + lam) == 0)
avg = sp.simplify((C_left ** 2 + C_right ** 2) / 2)
check("placement-averaged |C|^2 is bar-even", sp.simplify(avg - avg.subs(q, 1 / q)) == 0)
dL = sp.factor(sp.diff(C_left ** 2, q))
dR = sp.factor(sp.diff(C_right ** 2, q))
print("  d|C_left|^2/dq =", dL)
print("  d|C_right|^2/dq =", dR)

# ---------------------------------------------------------------- numbers
q0 = mp.mpf(C.q_at(70))


def at_q0(expr):
    return sp.lambdify(q, expr, "mpmath")(q0)


nums = {k: at_q0(v) for k, v in cells.items()}
amp = {"C_left": at_q0(C_left), "C_right": at_q0(C_right)}
check("tanh(ln q0) cross-check: -C_left/q0 == tanh(ln q0)",
      abs(-amp["C_left"] / q0 - mp.tanh(mp.log(q0))) < mp.mpf(10) ** -60)
# Comparison only (CODATA / PDG): NOT inputs.
m_e = mp.mpf("0.51099895069")
Qb = mp.mpf("0.78233")             # MeV, comparison
tau_n = mp.mpf("878.4")            # s
hbar = mp.mpf("6.582119569e-22")   # MeV s
D_n = hbar / tau_n
comparison = {
    "D_n_MeV (hbar/tau_n)": mp.nstr(D_n, 12),
    "D_n/m_e": mp.nstr(D_n / m_e, 12),
    "Q_beta_CODATA/m_e": mp.nstr(Qb / m_e, 12),
}
for k, v in nums.items():
    comparison[f"(D_n/m_e) / |M|^2[{k}]"] = mp.nstr((D_n / m_e) / v, 8)
print("q0 =", mp.nstr(q0, 30))
for k, v in nums.items():
    print(f"  |M|^2[{k}](q0) = {mp.nstr(v, 30)}")
for k, v in comparison.items():
    print(f"  {k} = {v}")

ok = all(c for _, c in checks)
print(f"{sum(c for _, c in checks)}/{len(checks)} checks pass")
wit = {
    "schema": "qou-probe-witness/v1",
    "name": "qbeta-n3-tplus-matrix-element",
    "bean": "qou-99qc",
    "producer": "computations/probes/qbeta_n3/n3_tplus_matrix_element_probe.py",
    "lean": "QOU/QuarkState/TPlusChargedCurrentElement.lean",
    "q0_anchor": "proton",
    "q0Value": mp.nstr(q0, 60),
    "dps": 70,
    "closed_forms": {
        "C_left (quark left)": str(sp.factor(C_left)),
        "C_right (quark right)": str(sp.factor(C_right)),
        "B isospin 1/2": "1", "B isospin 3/2": str(sp.factor(B_32)),
        **{f"|M|^2 {k}": str(v) for k, v in cells.items()},
        "beta_Bor charpoly W- == W+": str(cpm),
    },
    "values_at_q0": {**{k: mp.nstr(v, 60) for k, v in amp.items()},
                     **{f"|M|^2 {k}": mp.nstr(v, 60) for k, v in nums.items()}},
    "comparison_only": comparison,
    "reading_E": "Q_beta not produced: every H3 operator has equal spectrum on n and T+ n",
    "checks": [{"name": n, "pass": c} for n, c in checks],
}
with open(os.path.join(ROOT, "computations", "probes", "qbeta_n3",
                       "qbeta-n3-tplus-matrix-element.witness.json"), "w") as f:
    json.dump(wit, f, indent=2, ensure_ascii=False)
sys.exit(0 if ok else 1)
