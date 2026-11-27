"""Electron categorical energy from additivity (no fitting).

Derivation (Lean: QOU/Observations/ElectronWeightAdditivity.lean and
QOU/Transcendental/MassTheory/ElectronCategoricalEnergy.lean):
  * the convention-D trace is multiplicative on disjoint strand sets;
  * energy is additive over non-interacting parts (the corpus premise behind S);
  => a continuous energy map on trace values is Phi = c*log (no constant);
  => CAL-1 (Phi(tau_e) = m_e) fixes c = m_e/log(tau_e). No other choice is left.
So the electron's categorical energy in dictionary units is
  E_e = -log_q(tau_e) = -3 - log_q(y3),  tau_e = q^3 (q^4+1)/(q^2+1)^2,
and every trace-derived energy is m_e * log(y)/log(tau_e).
The two linear candidates (hbar_q^2 and tau_e) are printed for comparison only.
Measured values are used only in the last block (comparison boundary), and M
(model m_p/m_e under the proton pin) as in the sibling radius probes.
mpmath 50 dps.
"""
import sys
from pathlib import Path
from mpmath import mp, mpf, sqrt, log

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "computations" / "substrate"))
sys.path.insert(0, str(ROOT / "computations"))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.dps = 50
q = mpf(Q_50_DIGIT_STR)
h = q - 1 / q
hbar = 1 - 1 / q
y3 = (q**4 + 1) / (q**2 + 1)**2
tau_e = q**3 * y3
E0 = 1 / (q * (q - 1))                 # E0/m_e
R = tau_e / hbar**2
M = mpf("1836.152673426")
me_MeV = mpf("0.51099895069")
lbar_p_fm = mpf("0.21030891")

checks = []


def check(name, ok):
    checks.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name)


# derived unit per nat: |c| = m_e / (-ln tau_e)
c_nat = 1 / (-log(tau_e))              # in m_e
E_e = -log(tau_e) / log(q)             # categorical energy, dictionary units
mult_E0 = c_nat / E0                   # = q(q-1)/(-ln tau_e)

print("q0          ", mp.nstr(q, 20))
print("tau_e       ", mp.nstr(tau_e, 15))
print("y3          ", mp.nstr(y3, 15))
print("-ln tau_e   ", mp.nstr(-log(tau_e), 15))
print("E_e = -log_q tau_e", mp.nstr(E_e, 15), " (= -3 - log_q y3:",
      mp.nstr(-3 - log(y3) / log(q), 15), ")")
print("|c|/m_e per nat     ", mp.nstr(c_nat, 15))
print("|c| as multiple of E0", mp.nstr(mult_E0, 15))
print("classical limit |c|/m_e -> 1/ln2 =", mp.nstr(1 / log(2), 15))

check("tau_e < 1 at q0 (so c < 0: neutron above proton)", tau_e < 1)
check("E_e = -3 - log_q y3", abs(E_e - (-3 - log(y3) / log(q))) < mpf(10)**-40)
check("multiple of E0 equals q(q-1)/(-ln tau_e)",
      abs(mult_E0 - q * (q - 1) / (-log(tau_e))) < mpf(10)**-40)
# additivity check: two disjoint electrons
check("Phi(tau_e^2) = 2 m_e (log chart)",
      abs(c_nat * (-log(tau_e**2)) - 2) < mpf(10)**-40)
check("linear trace chart is not additive at q0 (tau_e != 2)", abs(tau_e - 2) > mpf("0.1"))

# gaps
beta_gap_nats = log(q**2 + q**-2)            # ln(y3/y21) = ln([4]/[2])
cas_gap = (q**4 + q**-4 - q**2 - q**-2) / h**2   # [3]_q, read per nat as in sibling probe
np_cell_nats = 2 * log(q)

units = (("mass-formula E0 (hbar^2)", E0),
         ("trace E0/R (linear tau_e)", E0 / R),
         ("derived log unit", c_nat))
rows = []
print()
print("unit per nat (m_e):")
for uname, u in units:
    print(f"  {uname:28s} {mp.nstr(u, 10)}")
print()
for gname, g in (("beta-dictionary gap", beta_gap_nats), ("Casimir C gap", cas_gap)):
    for uname, u in units:
        gap = u * g
        eps = gap / M
        D = sqrt(q / 2) / sqrt(eps)
        rows.append((gname, uname, gap, D))
        print(f"{gname:20s} {uname:28s} gap/m_e {mp.nstr(gap, 8):>12s}  D {mp.nstr(D, 7):>9s}")
print()
for uname, u in units:
    print(f"n-p log cell, {uname:28s} {mp.nstr(u * np_cell_nats, 8)} m_e")

print()
print("-- comparison boundary (data enters only here) --")
for gname, uname, gap, D in rows:
    print(f"{gname:20s} {uname:28s} gap {mp.nstr(gap * me_MeV, 6):>9s} MeV  r_rms {mp.nstr(D * lbar_p_fm, 5):>7s} fm")
for uname, u in units:
    print(f"n-p cell {uname:28s} {mp.nstr(u * np_cell_nats * me_MeV, 6)} MeV  (m_n - m_p = 1.293 MeV)")

print()
n_ok = sum(ok for _, ok in checks)
print(f"{n_ok}/{len(checks)} checks pass")
sys.exit(0 if n_ok == len(checks) else 1)
