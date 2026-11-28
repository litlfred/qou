#!/usr/bin/env python3
"""One scale for masses and mass differences: the Euler derivative bridges the two charts.

Lean: QOU/Observations/EnergyScaleBridge.lean (generic commutative ring / strict ordered ring),
      QOU/Transcendental/MassTheory/EnergyScaleBridge.lean (Real.log form).
Audit: docs/audits/2026-11-27-energy-scale-bridge.md.

Two CAL-1 charts are on main (#9718, #9733):
  k = 0, log chart:   E0(X) = m_e * L_X / L_e,        L = log tau
  k = 1, mass chart:  E1(X) = m_e * w_X / w_e,        w = q d/dq log tau = q tau'/tau
Bridge (proved in Lean): w = delta L with delta = q d/dq (beta = ln q, delta = d/dbeta), and
  E1(X) - E0(X) = m_e * (L_e / w_e) * delta(L_X / L_e).
The charts agree on X iff the log-chart ratio L_X/L_e is stationary in q.
Masses come from the mass formula, whose rule is k = 1 (#9692, #9733). A mass difference
(binding, n - p, a Delta - N gap) is a difference of masses, so it is read with k = 1.
This probe re-reads the three k = 0 quantities on the k = 1 chart. Nothing is tuned.
Measured values enter only in the comparison block. mpmath 80+ dps, physical proton pin
(muon pin on hold per 2026-11-28 owner ruling until rederivation).
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ.setdefault("QOU_OUTPUT_DPS", "80")
os.environ.setdefault("QOU_COMPUTE_DPS", "95")
os.environ["QOU_Q0_ANCHOR"] = "proton"

import mpmath as mp

ROOT = Path(__file__).resolve().parents[3]
for p in ("computations", "tools/pyhecke/python"):
    sys.path.insert(0, str(ROOT / p))

import _path_bridge  # noqa: F401, E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps(95)
mp.mp.dps = max(mp.mp.dps, 95)

from codata_constants import M_E_MEV, M_P_MEV_VALIDATION, ame_binding_mev  # noqa: E402
from pyhecke.constants import pn_interface_offset  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

q0 = q_at(80)  # physical_proton anchor (q0Anchor == "proton")
checks = []


def check(name, ok):
    checks.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + name)


def delta(F, q):
    """Euler derivative q d/dq."""
    return q * mp.diff(F, q)


def tau_e(q):
    return q**3 * (q**4 + 1) / (q**2 + 1) ** 2


def w_e(q):
    return 3 + 4 * q**2 * (q**2 - 1) / ((q**4 + 1) * (q**2 + 1))


def L_e(q):
    return mp.log(tau_e(q))


def z(q):
    return q**3 / (q**2 + 1)


def h(q):
    return q - 1 / q


def f_like(q):          # T_z-even pp / nn bond letter (PR #9675)
    return z(q) - h(q) / 2


def f_pn(q):            # pn bond letter, bring_color_weighted convention
    return z(q) + pn_interface_offset(q)


def ratio42(q):          # y_(3) / y_(2,1) = [4]/[2] = q^2 + q^-2
    return q**2 + q**-2


# ---- structural checks -------------------------------------------------------
tol = mp.mpf(10) ** -50
check("w_e = delta log tau_e at q0", abs(delta(L_e, q0) - w_e(q0)) < tol)
# bridge identity on a sample X (the deuteron bond letter)
LX = lambda q: mp.log(abs(f_pn(q)))
lhs = delta(LX, q0) / w_e(q0) - LX(q0) / L_e(q0)
rhs = (L_e(q0) / w_e(q0)) * delta(lambda q: LX(q) / L_e(q), q0)
check("bridge: E1 - E0 = m_e (L_e/w_e) delta(L_X/L_e)", abs(lhs - rhs) < tol)
# Legendre: L = S + beta * w  defines S; S of a product adds
S = lambda F, q: F(q) - mp.log(q) * delta(F, q)
prod = lambda q: L_e(q) + LX(q)
check("Legendre S additive on products", abs(S(prod, q0) - S(L_e, q0) - S(LX, q0)) < tol)
check("delta log(q^2+q^-2) closed form 2(q^2-q^-2)/(q^2+q^-2)",
      abs(delta(lambda q: mp.log(ratio42(q)), q0)
          - 2 * (q0**2 - q0**-2) / (q0**2 + q0**-2)) < tol)

# ---- units --------------------------------------------------------------------
we = w_e(q0)
Le = L_e(q0)
u0 = 1 / (-Le)                 # k = 0 unit, m_e per nat (#9718)
u1 = 1 / we                    # k = 1 unit, m_e per Euler unit (#9733)
alpha_prod = 8 * mp.catalan    # production log-law scale, m_e per nat (mass_table_comprehensive)
print()
print("q0 (physical_proton)       ", mp.nstr(q0, 20))
print("k=0 unit m_e/(-ln tau_e)   ", mp.nstr(u0, 12), "m_e per nat")
print("k=1 unit m_e/w_e           ", mp.nstr(u1, 12), "m_e per Euler unit")
print("production alpha = 8G      ", mp.nstr(alpha_prod, 12), "m_e per nat")


# ---- binding, ruled log law, re-read on each chart -----------------------------
def bond_sums(Z, N):
    A = Z + N
    if Z >= 1 and N >= 1:
        pieces = [(A - 2, f_like), (1, f_pn)]
    else:
        pieces = [(A - 1, f_like)]
    s0 = sum(n * mp.log(abs(f(q0))) for n, f in pieces)
    s1 = sum(n * delta(lambda q, f=f: mp.log(abs(f(q))), q0) for n, f in pieces)
    return s0, s1


print()
print("bond letters at q0: f_like", mp.nstr(f_like(q0), 12), " f_pn", mp.nstr(f_pn(q0), 12))
print("  delta ln|f_like|", mp.nstr(delta(lambda q: mp.log(abs(f_like(q))), q0), 12),
      "  delta ln|f_pn|", mp.nstr(delta(lambda q: mp.log(abs(f_pn(q))), q0), 12))
ME = M_E_MEV  # MeV, CAL-1
NUCLIDES = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1),
            ("4He", 2, 2), ("6Li", 3, 3), ("7Li", 3, 4)]
rows = []
print()
print("B = -E(bonds).  prod: alpha = 8G, |c| orientation.  k=0: m_e L_f/L_e.  k=1: m_e w_f/w_e")
print("nucleus   B(prod 8G) B(k=0)    B(k=1)     MeV")
for name, Z, N in NUCLIDES:
    s0, s1 = bond_sums(Z, N)
    rows.append((name, -alpha_prod * s0 * ME, -(s0 / Le) * ME, -u1 * s1 * ME))
    print(f"{name:6s} {mp.nstr(rows[-1][1], 7):>10s} {mp.nstr(rows[-1][2], 7):>10s} {mp.nstr(rows[-1][3], 7):>10s}")

check("bond letters shrink (f < 1) and grow with q (delta ln f > 0)",
      f_like(q0) < 1 and f_pn(q0) < 1
      and delta(lambda q: mp.log(abs(f_like(q))), q0) > 0 and delta(lambda q: mp.log(abs(f_pn(q))), q0) > 0)
check("CAL-1 signed binding is negative in both charts (bond_unbinds_*)", all(r[2] < 0 and r[3] < 0 for r in rows))

# ---- Delta - N gap and the radius factor D -------------------------------------
M = M_P_MEV_VALIDATION / ME    # proton-pin m_p/m_e ratio (as isospin_gap_radius_probe)
g0 = u0 * mp.log(ratio42(q0))
g1 = u1 * delta(lambda q: mp.log(ratio42(q)), q0)
D = lambda g: mp.sqrt(q0 / 2) / mp.sqrt(g / M)
print()
# signed: E_(3) - E_(2,1), i.e. Delta - N, with L_(3) - L_(2,1) = ln(q^2 + q^-2) > 0
dN0 = mp.log(ratio42(q0)) / Le
dN1 = delta(lambda q: mp.log(ratio42(q)), q0) / we
print("Delta - N signed k=0", mp.nstr(dN0, 10), "m_e;  k=1", mp.nstr(dN1, 10), "m_e")
check("Delta - N: log chart puts Delta below N, mass chart puts it above", dN0 < 0 < dN1)
print("Delta-N gap k=0", mp.nstr(g0, 10), "m_e  D", mp.nstr(D(g0), 8))
print("Delta-N gap k=1", mp.nstr(g1, 10), "m_e  D", mp.nstr(D(g1), 8))

# ---- n - p cell, SIGNED (tau_n = q^-2 tau_p: L_n - L_p = -2 ln q, w_n - w_p = -2) ---------
np0 = -2 * mp.log(q0) / Le       # E0 = m_e L_X / L_e
np1 = mp.mpf(-2) / we            # E1 = m_e w_X / w_e
print("n-p cell signed  k=0", mp.nstr(np0, 10), "m_e;  k=1", mp.nstr(np1, 10), "m_e")
check("n-p bridge: E1 - E0 = (L_e/w_e) delta(-2 ln q / L_e)",
      abs((np1 - np0) - (Le / we) * delta(lambda q: -2 * mp.log(q) / L_e(q), q0)) < tol)
check("n-p: log chart puts n above p", np0 > 0)
check("n-p: mass chart puts n below p (sign flip, pure_power_sign_flip)", np1 < 0)
check("pure-power ratio E1/E0 = L_e/(ln q w_e) < 0", abs(np1 / np0 - Le / (mp.log(q0) * we)) < tol
      and np1 / np0 < 0)

print()
print("-- comparison boundary (measured values enter only here) --")
for (name, Z, N), r in zip(NUCLIDES, rows):
    b = ame_binding_mev(Z, Z + N)
    print(f"{name:6s} AME {mp.nstr(b, 7):>9s}  prod/AME {mp.nstr(r[1]/b, 4):>7s}  k0/AME {mp.nstr(r[2]/b, 4):>7s}  k1/AME {mp.nstr(r[3]/b, 4):>7s}")
hbar_c_mev_fm = mp.mpf("197.3269804")
lbar = hbar_c_mev_fm / M_P_MEV_VALIDATION
print("gap MeV  k=0", mp.nstr(g0 * ME, 6), " k=1", mp.nstr(g1 * ME, 6), " (Delta - N ~293)")
print("r_rms fm k=0", mp.nstr(D(g0) * lbar, 6), " k=1", mp.nstr(D(g1) * lbar, 6), " (0.8409)")
print("n-p MeV  k=0", mp.nstr(np0 * ME, 6), " k=1", mp.nstr(np1 * ME, 6), " (+1.29333)")
print()
print(f"{sum(checks)}/{len(checks)} checks pass")
sys.exit(0 if all(checks) else 1)
