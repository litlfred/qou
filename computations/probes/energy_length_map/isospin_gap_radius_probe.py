"""Radius factor D from the corpus-derived isospin block gap (no fitting).

Map (Lean QOU/InformationTheory/EnergyLengthMap.lean): l(E) = hbar c / E.
SU_q(2) Casimir route (q-Bessel thread): r_rms = sqrt(q/2) / sqrt(eps) * l(M),
eps = E1 / M c^2.

E1 is taken, blind to any radius, from the beta = ln q dictionary
(QOU/Core/QBetaEnergyDictionary.lean) on the convention-D block weights of
V^{x3}, V = C^2 (isospin): y_(3) = [4]/[2]^3, y_(2,1) = [2]/[2]^3
(Clebsch-Gordan: [2]^3 = [4] + 2[2]). Energy unit is the quantum temperature
k_B T_q = E0 = m_e / (q(q-1)) (def:quantum-temperature, SpectatorEnergyMap.e0).
So E1 = E0 * ln([4]/[2]). M is the model proton mass (proton pin).
Measured values are printed last, as comparison only. mpmath 50 dps.
"""
import sys
from pathlib import Path
from mpmath import mp, mpf, log, sqrt

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "computations" / "substrate"))
sys.path.insert(0, str(ROOT / "computations"))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.dps = 50
q = mpf(Q_50_DIGIT_STR)


def qint(n):
    return (q**n - q**(-n)) / (q - 1 / q)


E0 = 1 / (q * (q - 1))                 # units of m_e
ratio = qint(4) / qint(2)              # y_(3) / y_(2,1) = q^2 + q^-2
assert abs(qint(2)**3 - qint(4) - 2 * qint(2)) < mpf(10)**-40
gap = E0 * log(ratio)                  # |E_(2,1) - E_(3)|, units of m_e
M = mpf("1836.152673426")              # model m_p / m_e under the proton pin
eps = gap / M
D = sqrt(q / 2) / sqrt(eps)

print("q0                       ", mp.nstr(q, 20))
print("y(3)/y(2,1) = q^2+q^-2   ", mp.nstr(ratio, 15))
print("sign: (3) has the larger weight, so the dictionary puts it LOWER")
print("E0 / m_e                 ", mp.nstr(E0, 15))
print("|gap| / m_e              ", mp.nstr(gap, 15))
print("eps = gap / M            ", mp.nstr(eps, 15))
print("D = r_rms / lbar_M       ", mp.nstr(D, 15))

# Second corpus unit (ElectronUnitSplit): trace-pipeline electron weight
# tau_e = q^3 y_(3) instead of the hand-placed hbar_q^2. Units differ by
# R = tau_e / hbar_q^2, so E0_trace = E0 / R. Reported, not chosen.
hbar = 1 - 1 / q
tau_e = q**3 * (q**4 + 1) / (q**2 + 1)**2
R = tau_e / hbar**2
gap_t = gap / R
eps_t = gap_t / M
D_t = sqrt(q / 2) / sqrt(eps_t)
print()
print("trace-pipeline unit: R = tau_e/hbar_q^2", mp.nstr(R, 15))
print("  |gap| / m_e            ", mp.nstr(gap_t, 15))
print("  eps                    ", mp.nstr(eps_t, 15))
print("  D                      ", mp.nstr(D_t, 15))
print()
print("-- comparison boundary --")
me_MeV = mpf("0.51099895069")
lbar_p_fm = mpf("0.21030891")
print("|gap| MeV                ", mp.nstr(gap * me_MeV, 8), " (Delta - N measured ~293)")
print("r_rms fm                 ", mp.nstr(D * lbar_p_fm, 8), " (r_p measured 0.8409)")
print("trace unit: |gap| MeV    ", mp.nstr(gap_t * me_MeV, 8))
print("trace unit: r_rms fm     ", mp.nstr(D_t * lbar_p_fm, 8))
