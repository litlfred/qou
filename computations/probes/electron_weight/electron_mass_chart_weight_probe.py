"""Electron weight on the mass-formula scale, by the mass formula's own rule (no fitting).

Rule (Lean: QOU/Transcendental/MassTheory/ElectronMassChartWeight.lean). Additive local
readings of a trace germ are (q d/dq)^k log Z. The quantum dilogarithm has log P ~ 1/hbar_q,
and each q d/dq raises the pole order by one (hbar_pole_raise). The mass formula's carrier
is order hbar_q^-2, so k = 1: the weight is the energy reading w = q d/dq log Z. That is the
muon's q-volume G (#9692). The same rule on the electron trace gives
  w_e(q) = q d/dq log tau_e = 3 + 4 q^2 (q^2 - 1) / ((q^4 + 1)(q^2 + 1)),   w_e(1) = 3,
in place of the hand-placed weight 1 (the unit m_e/hbar_q^2 of m = m_e Vol rho / hbar_q^2).
Measured values enter only in the comparison block; MU_E is used there to show what CAL-2
WOULD give if re-solved in the derived chart. That q0' is not adopted. mpmath 30 dps.
"""
import sys
from pathlib import Path
import mpmath as mp

ROOT = Path(__file__).resolve().parents[3]
for p in ("computations/substrate", "computations", "tools/qou-substrate/python"):
    sys.path.insert(0, str(ROOT / p))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from qou_substrate.constants import MASS_RATIO_MU_E_STR  # noqa: E402

mp.mp.dps = 30
q0 = mp.mpf(Q_50_DIGIT_STR)
VOL41 = 2 * mp.clsin(2, mp.pi / 3)
Z41 = mp.expjpi(mp.mpf(1) / 3)
MU_E = mp.mpf(MASS_RATIO_MU_E_STR)   # comparison only
ME_MEV = mp.mpf("0.51099895069")

checks = []


def check(name, ok):
    checks.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + name)


def hbar(q):
    return 1 - 1 / q


def tau_e(q):
    return q**3 * (q**4 + 1) / (q**2 + 1) ** 2


def w_e(q):
    return 3 + 4 * q**2 * (q**2 - 1) / ((q**4 + 1) * (q**2 + 1))


def G(z, q):
    return mp.nsum(lambda m: (m + 1) * z * q ** (-m) / (1 - z * q ** (-m)), [0, mp.inf])


def W_mu(q):
    return 2 * mp.im(G(Z41, q))


# closed form against numerical q d/dq log tau_e
num = q0 * mp.diff(lambda x: mp.log(tau_e(x)), q0)
check("w_e closed form = q d/dq log tau_e at q0", abs(num - w_e(q0)) < mp.mpf(10) ** -20)
check("w_e(1) = 3 (writhe)", w_e(mp.mpf(1)) == 3)
# pole raise: q d/dq hbar^-n = -n q^-1 hbar^-(n+1)
for n in (1, 2):
    lhs = q0 * mp.diff(lambda x: hbar(x) ** (-n), q0)
    check(f"q d/dq hbar^-{n} = -{n} q^-1 hbar^-{n+1}", abs(lhs + n / (q0 * hbar(q0) ** (n + 1))) < mp.mpf(10) ** -15)
# n-p cell in the derived chart: reading(q^-1 x) - reading(q x) = -2 for any x
check("n-p cell reading = -2", abs(q0 * mp.diff(lambda x: mp.log(x**-2), q0) + 2) < mp.mpf(10) ** -20)

we = w_e(q0)
W = W_mu(q0)
print()
print("q0                        ", mp.nstr(q0, 20))
print("w_e(q0)                   ", mp.nstr(we, 15), "(hand-placed: 1)")
print("mass-chart unit, derived  ", mp.nstr(1 / we, 15), "m_e per weight unit (hand-placed: 1)")
print("W_mu(q0) = 2 Im G         ", mp.nstr(W, 15))
print("m_mu/m_e in derived chart ", mp.nstr(W / we, 12))
print("n-p cell, derived chart   ", mp.nstr(2 / we, 12), "m_e")

# comparison: CAL-2 re-solved in the derived chart (NOT adopted)
f = lambda q: W_mu(q) / w_e(q) - MU_E
q0p = mp.findroot(f, mp.mpf("1.06"))
print()
print("-- comparison boundary (measured values enter only here) --")
print("m_mu/m_e (CODATA)         ", mp.nstr(MU_E, 12))
print("derived chart at q0 / CODATA", mp.nstr(W / we / MU_E, 8))
print("n-p cell derived chart    ", mp.nstr(2 / we * ME_MEV, 8), "MeV  (m_n - m_p 1.293)")
print("CAL-2 re-solved q0'       ", mp.nstr(q0p, 15), " hbar", mp.nstr(hbar(q0p), 10),
      " (q0", mp.nstr(q0, 10), " hbar", mp.nstr(hbar(q0), 10), ")")
print("w_e(q0')                  ", mp.nstr(w_e(q0p), 12))
print()
print(f"{sum(checks)}/{len(checks)} checks pass")
sys.exit(0 if all(checks) else 1)
