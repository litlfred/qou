#!/usr/bin/env python3
"""What does epsilon in Q_beta = |eps(Delta)| * E_0 actually measure? (bean qou-99qc)

Exact sympy in q, readout at the proton pin with mpmath (60 dps). No float64.
Writes NO witness. Selects nothing. Rows are never ranked by residual.

Claims checked:
  C1  Delta_S = n - p = -(h[2]/4)(J_0 + J_1), with J_i = (s_i + s_i^-1)/[2] the
      chirality grading P_L - P_R of crossing i (corpus: ud_letter_eq_grading).
      Equivalently Delta_S = -(q h [2]/4)(W_L^0 + W_L^1), W_L = q^-1 J the
      one-sided (left) weak vertex of OneSidedWeakVertex.lean.
  C2  For ANY trace tau on H_3: tau(Delta_S) = -(h[2]/2) tau(J_0).
  C3  On the Wedderburn blocks chi_(2,1)(J) = 0, so for a block-weighted trace
      tau(J) = y_3 - y_111. Under convention D (y_111 = 0): tau(J) = y_3, the
      weight of the trivial (all-left-line) block.
  C4  So for every normalised convention-D trace,
          Q_beta(Delta_S) = (h[2]_q/2) * y_3 * E_0,
      with y_3 in [0, 1] for positive weights. Markov points: y_3 = 1 (z = q,
      augmentation) and y_3 = (q^4+1)/(q^2+1)^2 = 1 - 2/[2]^2 (z_D).
  C5  For the long nucleon elements eps(Delta) is affine in y_3 (via chi_3, chi_21);
      reported per cell with the y_3 each reading gives.
"""
from __future__ import annotations

import importlib.util
import os
import sys
import warnings

import sympy as sp

warnings.filterwarnings("ignore")
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
for _p in ("computations/substrate", "computations", "tools/pyhecke/python",
           "tools/qou-substrate/python", "computations/qbeta"):
    sys.path.insert(0, os.path.join(ROOT, _p))

import mpmath as mp  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_2022_source import M_E_MEV, Q_BETA_MEV_AME  # noqa: E402

mp.mp.dps = 60
_spec = importlib.util.spec_from_file_location(
    "_census", os.path.join(ROOT, "computations/qbeta/qbeta_delta_candidate_census_probe.py"))
_census = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_census)
h_sym = _census.h

q = sp.Symbol("q", positive=True)
h = q - 1 / q
b2 = q + 1 / q
RES = []


def check(name, ok, detail=""):
    RES.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))


# ---- block images of the generators (same matrices as RightLineTraceObstruction.lean)
S0 = (q, sp.Matrix([[q, 0], [1, -1 / q]]), -1 / q)
S1 = (q, sp.Matrix([[-1 / q, 1], [0, q]]), -1 / q)
I2 = sp.eye(2)


def mul(a, b):
    return (a[0] * b[0], a[1] * b[1], a[2] * b[2])


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def smul(c, a):
    return (c * a[0], c * a[1], c * a[2])


ONE = (sp.Integer(1), I2, sp.Integer(1))
# basis order taken from the census: [gamma, s0, s1, L-, L+, e^-]
L_minus = mul(S1, S0)
L_plus = mul(S0, S1)
e_minus = mul(mul(S0, S1), S0)
BASIS = [ONE, S0, S1, L_minus, L_plus, e_minus]


def simp(a):
    return (sp.simplify(a[0]), sp.simplify(a[1]), sp.simplify(a[2]))


def chars(a):
    a = simp(a)
    return (a[0], sp.simplify(a[1].trace()), a[2])


def element(nf):
    acc = smul(0, ONE)
    for c, bvec in zip(nf, BASIS):
        acc = add(acc, smul(sp.sympify(c).subs(h_sym, h), bvec))
    return simp(acc)


def tr_markov(nf, z):
    hz = h * z + 1
    trb = [1, z, z, z ** 2, z ** 2, z * hz]
    return sp.simplify(sum(sp.sympify(c).subs(h_sym, h) * t for c, t in zip(nf, trb)))


# Markov weights y_lambda(z): solve TR(z) = y3 chi3 + y21 chi21 + y111 chi111 on basis
y3, y21, y111, z = sp.symbols("y3 y21 y111 z")
basis_chars = [chars(bv) for bv in BASIS]
hz = h * z + 1
TRZ = [1, z, z, z ** 2, z ** 2, z * hz]
sol = sp.solve([sp.simplify(y3 * c[0] + y21 * c[1] + y111 * c[2] - t)
                for c, t in zip(basis_chars, TRZ)][0:4:3] + [sp.simplify(y3 * basis_chars[1][0] + y21 * basis_chars[1][1] + y111 * basis_chars[1][2] - TRZ[1])], [y3, y21, y111], dict=True)[0]
ok_all = all(sp.simplify(sol[y3] * c[0] + sol[y21] * c[1] + sol[y111] * c[2] - t) == 0
             for c, t in zip(basis_chars, TRZ))
print("Markov weights from the six basis traces (exact in q, z)")
check("markov_trace_is_block_weighted_on_whole_basis", ok_all)
zD = q ** 3 / (q ** 2 + 1)
check("zD_kills_sign_block", sp.simplify(sol[y111].subs(z, zD)) == 0)
alpha = (q ** 4 + 1) / (q ** 2 + 1) ** 2
check("zD_trivial_weight_is_alpha", sp.simplify(sol[y3].subs(z, zD) - alpha) == 0,
      "y3(z_D) = (q^4+1)/(q^2+1)^2 = 1 - 2/[2]^2")
check("z_eq_q_is_augmentation", sp.simplify(sol[y3].subs(z, q) - 1) == 0
      and sp.simplify(sol[y21].subs(z, q)) == 0 and sp.simplify(sol[y111].subs(z, q)) == 0)
y111_at_1 = sp.factor(sol[y111].subs(z, 1))
check("z_eq_1_does_not_kill_sign_block", sp.simplify(y111_at_1) != 0, f"y111(1) = {y111_at_1}")

# ---- C1: Delta_S as a sum of chirality gradings / one-sided vertices
print("\nC1  Delta_S and the chirality grading")
S0inv = add(S0, smul(-h, ONE))
S1inv = add(S1, smul(-h, ONE))
J0 = simp(smul(1 / b2, add(S0, S0inv)))
J1 = simp(smul(1 / b2, add(S1, S1inv)))
P_n = mul(add(S0, smul(-h / 2, ONE)), S1inv)      # (s0 - h/2)(s1 - h)
P_p = mul(S0, add(S1, smul(-h / 2, ONE)))         # s0 (s1 - h/2)
dS = simp(add(P_n, smul(-1, P_p)))
rhs = simp(smul(-h * b2 / 4, add(J0, J1)))
check("Delta_S_eq_minus_h_b2_over_4_sum_J",
      all(sp.simplify(x - y) == 0 for x, y in [(dS[0], rhs[0]), (dS[2], rhs[2])])
      and sp.simplify(dS[1] - rhs[1]) == sp.zeros(2, 2))
dS_nf = element([h_sym ** 2 / 2, -h_sym / 2, -h_sym / 2, 0, 0, 0])
check("Delta_S_matches_census_NF_vector",
      sp.simplify(dS_nf[0] - dS[0]) == 0 and sp.simplify(dS_nf[1] - dS[1]) == sp.zeros(2, 2))
WL0 = smul(1 / q, J0)
WL1 = smul(1 / q, J1)
rhs2 = simp(smul(-q * h * b2 / 4, add(WL0, WL1)))
check("Delta_S_is_sum_of_one_sided_left_vertices",
      sp.simplify(dS[1] - rhs2[1]) == sp.zeros(2, 2) and sp.simplify(dS[0] - rhs2[0]) == 0)
cJ = chars(J0)
check("J_on_blocks", cJ[0] == 1 and cJ[1] == 0 and cJ[2] == -1, f"chi(J) = {cJ}")
cdS = chars(dS)
print(f"  chi(Delta_S) = trivial {sp.factor(cdS[0])}, (2,1) {sp.factor(cdS[1])}, sign {sp.factor(cdS[2])}")
check("chi21_Delta_S_is_zero", cdS[1] == 0)

# ---- C2/C3: any normalised D-trace: tau(Delta_S) = -(h b2/2) y3
print("\nC2-C4  tau(Delta_S) for a generic block-weighted trace")
tau_dS = sp.simplify(y3 * cdS[0] + y21 * cdS[1] + y111 * cdS[2])
check("tau_Delta_S_eq_minus_h_b2_over_2_times_tauJ",
      sp.simplify(tau_dS + h * b2 / 2 * (y3 - y111)) == 0)

# ---- numbers at the proton pin
Q0 = sp.Rational(Q_50_DIGIT_STR)
mq = Q_MP
me = mp.mpf(str(M_E_MEV))
QB = mp.mpf(str(Q_BETA_MEV_AME))
E0 = {"order_zero": me / (mq * (mq - 1))}
E0["tower"] = E0["order_zero"] / (1 - (1 - 1 / mq) ** 2)


def N(e):
    return mp.mpf(str(sp.N(sp.sympify(e).subs(q, Q0), 70)))


print("\nPer-cell table (eps affine in y3 on the normalised D line y21 = (1-y3)/2)")
deltas = {
    "delta_S": [h_sym ** 2 / 2, -h_sym / 2, -h_sym / 2, 0, 0, 0],
}
for name, fn in (("nuc9", _census.nuc9), ("nuc11_interleaved", _census.nuc11_interleaved),
                 ("nuc11_gen_grouped", _census.nuc11_gen_grouped)):
    n, p = fn("n"), fn("p")
    deltas[name] = [sp.expand(a - b) for a, b in zip(n, p)]

rows = []
for name, nf in deltas.items():
    c = chars(element(nf))
    c3, c21 = N(c[0]), N(c[1])
    # eps(y3) = y3*c3 + (1-y3)/2*c21
    def eps(yv):
        return yv * c3 + (1 - yv) / 2 * c21
    yD, yA = N(alpha), mp.mpf(1)
    # cross-check against the TR(z) route
    trD = N(tr_markov(nf, zD))
    check(f"{name}_block_route_matches_TR_zD", abs(eps(yD) - trD) < mp.mpf("1e-40"))
    out = {"name": name, "chi3": c3, "chi21": c21}
    for e0n, e0 in E0.items():
        tgt = QB / e0
        # solve |eps(y)| = tgt on the line (both signs), keep y in [0,1]
        req = []
        for s in (1, -1):
            denom = c3 - c21 / 2
            if denom != 0:
                yv = (s * tgt - c21 / 2) / denom
                req.append(yv)
        out[e0n] = {
            "zD_pct": (abs(eps(yD)) * e0 / QB - 1) * 100,
            "aug_pct": (abs(eps(yA)) * e0 / QB - 1) * 100,
            "y3_required": [r for r in req],
        }
    rows.append(out)

print(f"\n  y3(z_D) = alpha = {mp.nstr(N(alpha), 15)};  y3(aug) = 1")
for r in rows:
    print(f"\n  {r['name']}: chi3 = {mp.nstr(r['chi3'], 15)}, chi21 = {mp.nstr(r['chi21'], 15)}")
    for e0n in E0:
        d = r[e0n]
        req = ", ".join(mp.nstr(v, 12) for v in d["y3_required"])
        print(f"    E0 {e0n:10s}: z_D {mp.nstr(d['zD_pct'], 8):>12s} %   aug {mp.nstr(d['aug_pct'], 8):>12s} %"
              f"   y3 needed for Q_beta(AME): {req}")

npass = sum(ok for _, ok in RES)
print(f"\n{npass}/{len(RES)} checks pass")
sys.exit(0 if npass == len(RES) else 1)
