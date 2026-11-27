"""Electron energy reading on the RING mass (def:mass-identity), no fitting.

Ring mass (framing-corrected, braid-class invariant): m(beta) = [2]^n q^{-2w} tr_D(beta).
Electron (Hopf, n = 3 strands as in tau_e, w = 3): m_e = [2]^3 q^-6 tau_e = [4]/q^3,
value 4 at q = 1. Lean: QOU/Observations/ElectronRingMassReading.lean (massE_eq) and
QOU/Transcendental/MassTheory/ElectronRingMassReading.lean (uE_eq_neg_log_deriv).

Energy reading (thermodynamic sign): U = -q d/dq log m.
  U_e = 3 - D[4]/[4],  D = q d/dq,  U_e(1) = 3.
Relation to the trace chart: U_e = 6 - w_e - 3 D[2]/[2]  (w_e = q d/dq log tau_e).
The 3 at q = 1 survives the framing correction, so it is not a writhe artefact.
n-p cell: eps_n = q^-2 eps_p gives U_n - U_p = +2 (np_cell_U), i.e. +2/U_e in electron units.
Measured values enter only in the comparison block. mpmath 30 dps.
"""
import sys
from pathlib import Path
import mpmath as mp

ROOT = Path(__file__).resolve().parents[3]
for p in ("computations/substrate", "computations", "tools/qou-substrate/python"):
    sys.path.insert(0, str(ROOT / p))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.mp.dps = 30
q0 = mp.mpf(Q_50_DIGIT_STR)
ME_MEV = mp.mpf("0.51099895069")   # comparison only

checks = []


def check(name, ok):
    checks.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + name)


def tau_e(q):
    return q**3 * (q**4 + 1) / (q**2 + 1) ** 2


def int2(q):
    return q + 1 / q


def int4(q):
    return q**3 + q + 1 / q + q**-3


def d_int4(q):
    return 3 * q**3 + q - 1 / q - 3 * q**-3


def m_e(q):
    return int2(q) ** 3 * q**-6 * tau_e(q)


def U_e(q):
    return 3 - d_int4(q) / int4(q)


def w_e(q):
    return 3 + 4 * q**2 * (q**2 - 1) / ((q**4 + 1) * (q**2 + 1))


def D(f, q):
    return q * mp.diff(f, q)


eps = mp.mpf(10) ** -20
check("m_e = [4]/q^3 at q0", abs(m_e(q0) - int4(q0) / q0**3) < eps)
check("m_e(1) = 4", m_e(mp.mpf(1)) == 4)
check("U_e = -q d/dq log m_e at q0", abs(-D(lambda x: mp.log(m_e(x)), q0) - U_e(q0)) < eps)
check("U_e(1) = 3", U_e(mp.mpf(1)) == 3)
check("U_e = 6 - w_e - 3 D[2]/[2] at q0",
      abs(U_e(q0) - (6 - w_e(q0) - 3 * D(lambda x: mp.log(int2(x)), q0))) < eps)
check("framing: [2] q^-2 z_D = 1", abs(int2(q0) * q0**-2 * q0**3 / (q0**2 + 1) - 1) < eps)
check("framing: [2] q^2 zbar_D = 1", abs(int2(q0) * q0**2 / (q0 * (q0**2 + 1)) - 1) < eps)
# n-p cell: reading(q^-2 x) - reading(x) = +2 for any germ x
check("n-p cell U_n - U_p = +2", abs(-D(lambda x: mp.log(x**-2), q0) - 2) < eps)

ue = U_e(q0)
print()
print("q0                         ", mp.nstr(q0, 20))
print("m_e ring = [4]/q^3         ", mp.nstr(m_e(q0), 15), "(4 at q=1)")
print("U_e(q0)                    ", mp.nstr(ue, 15), "(3 at q=1)")
print("w_e(q0) trace chart        ", mp.nstr(w_e(q0), 15))
print("n-p cell, ring reading     ", mp.nstr(2 / ue, 12), "m_e  (sign: neutron ABOVE proton)")
print()
print("-- comparison boundary (measured values enter only here) --")
print("n-p cell ring reading      ", mp.nstr(2 / ue * ME_MEV, 8), "MeV  (m_n - m_p 1.293)")
print()
print(f"{sum(checks)}/{len(checks)} checks pass")
sys.exit(0 if all(checks) else 1)
