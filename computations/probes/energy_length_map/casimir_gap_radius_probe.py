"""Radius factor D from the U_q(sl2) Casimir gap on the nucleon charge sectors.

Pre-stated before running (no fitting): gap operator = quantum Casimir
C = fe + (qK + q^-1 K^-1)/h^2, h = q - q^-1, whose restriction to the charge
sectors of V^{x3} is proved in QOU/Nuclear/BlockChargeSectorTrace.lean.
On spin j, h^2 C = q^(2j+1) + q^-(2j+1). Gap between isospin 3/2 and 1/2:
  dC = (q^4 + q^-4 - q^2 - q^-2) / h^2   (classical limit 15/4 - 3/4 = 3).
The h^2-scaled operator h^2 C (as written in BlockChargeSectorTrace) is
also reported; its gap vanishes at q = 1, so it has no classical limit.
Energy unit (owner card 2026-11-27, PR #9718): the DERIVED per-nat unit
m_e/(-ln tau_e) (qbeta_e0.electron_log_unit_scaled), listed first. Reading a Casimir
eigenvalue as an energy PER NAT is an assumption carried over from #9708, not derived.
Comparison only: E0 = m_e/(q(q-1)) and the linear-trace unit E0/R, R = tau_e/hbar_q^2.
Radius: SU_q(2) route D = sqrt(q/2)/sqrt(eps), eps = gap/M.
Measured values printed last, comparison only. mpmath 50 dps.
"""
import sys
from pathlib import Path
from mpmath import mp, mpf, sqrt

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "computations" / "substrate"))
sys.path.insert(0, str(ROOT / "computations"))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
sys.path.insert(0, str(ROOT / "computations" / "qbeta"))
import qbeta_e0  # noqa: E402

mp.dps = 50
q = mpf(Q_50_DIGIT_STR)
h = q - 1 / q


def h2C(two_j_plus_1):
    return q**two_j_plus_1 + q**(-two_j_plus_1)


dC_h2 = h2C(4) - h2C(2)          # gap of h^2 C
dC = dC_h2 / h**2                # gap of C
E0 = 1 / (q * (q - 1))           # units of m_e
hbar = 1 - 1 / q
tau_e = q**3 * (q**4 + 1) / (q**2 + 1)**2
R = tau_e / hbar**2
M = mpf("1836.152673426")        # model m_p / m_e under the proton pin
me_MeV = mpf("0.51099895069")
lbar_p_fm = mpf("0.21030891")

print("q0", mp.nstr(q, 20), " h", mp.nstr(h, 15))
print("dC (classical limit 3)  ", mp.nstr(dC, 15))
print("d(h^2 C)                ", mp.nstr(dC_h2, 15))
print("sign: isospin 3/2 above 1/2 (dC > 0):", dC > 0)
rows = []
for opname, d in (("C", dC), ("h^2 C", dC_h2)):
    for uname, unit in (("DERIVED log unit", qbeta_e0.electron_log_unit_scaled(1, q)),
                        ("cmp: E0", E0), ("cmp: trace E0/R", E0 / R)):
        gap = unit * d
        eps = gap / M
        D = sqrt(q / 2) / sqrt(eps)
        rows.append((opname, uname, gap, eps, D))
        print(f"{opname:6s} {uname:16s} gap/m_e {mp.nstr(gap, 10):>14s}"
              f"  eps {mp.nstr(eps, 8):>12s}  D {mp.nstr(D, 8):>10s}")
print()
print("-- comparison boundary (Delta - N ~ 293 MeV, r_p 0.8409 fm) --")
for opname, uname, gap, eps, D in rows:
    print(f"{opname:6s} {uname:16s} gap {mp.nstr(gap * me_MeV, 6):>10s} MeV"
          f"  r_rms {mp.nstr(D * lbar_p_fm, 6):>8s} fm")
