"""n - p electromagnetic term in the two-scale class (bean qou-mbfv).

Pre-stated before running (no fitting, nothing selected against a target):
  Coulomb n - p   = f * alpha * Q_np * M / D          (NucleonSplitTwoScale.coulomb_hc_cancels)
  f    = 0.520011, q-Hankel 0s shape factor (#9699, scale-free)
  Q_np = -1/3, Coulomb charge-pair factor (#9654 probe, exact)
  M    = model nucleon rest energy (proton pin)
  D    = radius factor r / (hbar c / M) from the derived routes already on main:
         SU_q(2) Casimir gap route, D = sqrt(q/2)/sqrt(eps), eps = [3]_q-gap / M,
         every (operator, electron unit) row of casimir_gap_radius_probe.py, plus the
         Bekenstein-saturated route A (D = 3 S_1 / 2 pi) of the radius-routes audit.
  flavour = 2 log q * u, per-nat unit u
Units (per nat): E0 = m_e/(q(q-1)) (mass-formula), E0/R (trace), and the DERIVED unit
  |c| = m_e / (-ln tau_e) of #9718 (ElectronCategoricalEnergy: additivity + CAL-1).
  The derived unit is the settled one; E0 and E0/R are kept for comparison only.
  Gaps: Casimir C ([3]_q) and h^2 C read per nat (as #9708; that reading is not derived),
  and the beta-dictionary isospin block gap ln(q^2 + q^-2), a trace-derived energy.
alpha_em^-1 = 137.0359350940, conditional on the Witten-kappa Gram sorry (as in #9654).
Measured values are printed last, under the comparison boundary only. mpmath 50 dps.
"""
import sys
from pathlib import Path
from mpmath import mp, mpf, sqrt, log, pi

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "computations" / "substrate"))
sys.path.insert(0, str(ROOT / "computations"))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.dps = 50
q = mpf(Q_50_DIGIT_STR)
h = q - 1 / q
L = log(q)
f = mpf("0.520011")
Q_np = -mpf(1) / 3
alpha = 1 / mpf("137.0359350940")
M = mpf("1836.152673426")            # model m_p / m_e under the proton pin
E0 = 1 / (q * (q - 1))               # m_e units
hbar = 1 - 1 / q
tau_e = q**3 * (q**4 + 1) / (q**2 + 1)**2
Rr = tau_e / hbar**2

dC_h2 = (q**4 + q**-4) - (q**2 + q**-2)
dC = dC_h2 / h**2
p_plus = q**2 / (1 + q**2)
S1 = -(p_plus * log(p_plus) + (1 - p_plus) * log(1 - p_plus))

cder = 1 / (-log(tau_e))            # derived per-nat unit |c| / m_e (#9718)
UNITS = (("derived", cder), ("mass-formula E0", E0), ("trace E0/R", E0 / Rr))
flav = {u: 2 * L * v for u, v in UNITS}
flavour = flav["derived"]
dBeta = log(q**2 + q**-2)
rows = []
for opname, d in (("beta gap", dBeta), ("Casimir C", dC), ("Casimir h^2 C", dC_h2)):
    for uname, unit in UNITS:
        gap = unit * d
        D = sqrt(q / 2) / sqrt(gap / M)
        rows.append((f"{opname}, {uname}", D, gap, uname))
rows.append(("Bekenstein saturated (route A)", 3 * S1 / (2 * pi), None, "derived"))
print("derived unit |c|/m_e", mp.nstr(cder, 12), " |c|/E0", mp.nstr(cder / E0, 12))

print("q0", mp.nstr(q, 20), " log q", mp.nstr(L, 20))
print("flavour 2 log q |c| / m_e (derived unit)", mp.nstr(flavour, 15))
print()
print(f"{'route':42s} {'D':>10s} {'EM n-p / m_e':>14s} {'flavour/|EM|':>13s}")
out = []
for name, D, gap, uname in rows:
    em = f * alpha * Q_np * M / D
    if gap is not None:   # check the geometric-mean identity of the Lean file
        assert abs(em**2 - 2 * f**2 * alpha**2 * Q_np**2 * M * gap / q) < mpf(10)**-40
    out.append((name, D, em, uname))
    print(f"{name:42s} {mp.nstr(D, 8):>10s} {mp.nstr(em, 10):>14s} "
          f"{mp.nstr(flav[uname] / abs(em), 6):>13s}")

print()
print("-- comparison boundary (data enter only here) --")
me = mpf("0.51099895069")
lbar_p = mpf("0.21030891")
print("m_n - m_p measured 1.29333 MeV; literature QED part -0.58 (GLR 2020),"
      " -1.00 (BMW 2015), -1.30 (WCM 2012); QCD/QED 1.95-3.22")
for u, _ in UNITS:
    print(f"flavour ({u})   {mp.nstr(flav[u] * me, 6)} MeV")
for name, D, em, uname in out:
    print(f"{name:42s} r {mp.nstr(D * lbar_p, 5):>7s} fm  EM {mp.nstr(em * me, 5):>9s} MeV"
          f"  total {mp.nstr((flav[uname] + em) * me, 5):>8s} MeV")
D_meas = mpf("0.8409") / lbar_p
em_meas = f * alpha * Q_np * M / D_meas
print(f"{'(reference) measured r_p 0.8409 fm':42s} D {mp.nstr(D_meas, 5)}  EM"
      f" {mp.nstr(em_meas * me, 5)} MeV")
for lit in (mpf("0.58"), mpf("1.00"), mpf("1.30")):
    print(f"  D that literature QED -{lit} MeV would need (Coulomb only):"
          f" {mp.nstr(f * alpha * M / 3 / (lit / me), 5)}")
