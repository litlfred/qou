"""Pre-registered EM ring factor mu for gap G3 (bean qou-tcl3).

Route: one Coulomb pair = one photon exchanged between two proton blocks = one
chirality-summed vertex pair. PR #9841 (EmVertexPairScalarChain) proves every such
pair is the scalar -h^2, h = q - 1/q, and that each extra pair in the polarisation
chain carries one alpha. So the pre-registered factor is

    mu_1   = 1 - alpha * h^2            (one exchange; Lean CoulombRingMu)
    mu_lad = 1 / (1 + alpha * h^2)      (ladder resummation; differs at O(alpha^2))

with alpha the corpus-derived alpha_EM (conditional on the Witten-kappa Gram sorry).
Readings (Lean CoulombRingLedger.reading_ledger): eps = rho(mu).
  log reading    eps_log = E0 * (-ln mu)
  energy reading eps_U   = (m_e / U_e) * U(mu),  U(mu_1) = 2 alpha h [2] / (1 - alpha h^2)

Nothing is selected. AME mirror splits enter ONLY in the comparison block.
All arithmetic mpmath at 50 dps.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[3]
for p in ("computations/substrate", "computations", "tools/qou-substrate/python"):
    sys.path.insert(0, str(ROOT / p))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from meson_em_sinh_closed_form import _alpha_em_inv_derived  # noqa: E402

mp.mp.dps = 50
q = mp.mpf(Q_50_DIGIT_STR)
ME = mp.mpf("0.51099895069")  # MeV; the corpus energy unit (same as ring_binding_probe)

h = q - 1 / q
two = q + 1 / q
int4 = q**3 + q + 1 / q + q**-3
dint4 = 3 * q**3 + q - 1 / q - 3 * q**-3
U_e = 3 - dint4 / int4
hbar = 1 - 1 / q  # as in ring_binding_probe (tower E0)
E0 = ME / (q * (q - 1) * (1 - hbar**2))
alpha = 1 / _alpha_em_inv_derived(q)

checks = []

# exact checks
mu1 = 1 - alpha * h**2
U_mu1 = 2 * alpha * h * two / mu1
# numerical derivative cross-check of the closed form at 50 dps
f = lambda x: mp.log(1 - alpha * (x - 1 / x) ** 2)
U_num = -q * mp.diff(f, q)
checks.append(("U(mu_1) closed form = -q d/dq ln mu_1", abs(U_num - U_mu1) < mp.mpf(10) ** -40))
checks.append(("mu_1 at q = 1 is exactly 1", (1 - alpha * (1 - 1) ** 2) == 1))

mulad = 1 / (1 + alpha * h**2)
U_lad = 2 * alpha * h * two / (1 + alpha * h**2)

rows = []
for name, mu, U in (("mu_1 (one exchange)", mu1, U_mu1), ("mu_lad (ladder)", mulad, U_lad)):
    eps_log = E0 * (-mp.log(mu))
    eps_U = ME / U_e * U
    rows.append((name, eps_log, eps_U))

print("q0 =", mp.nstr(q, 15), " h =", mp.nstr(h, 15), " [2] =", mp.nstr(two, 15))
print("alpha (derived) = 1/", mp.nstr(1 / alpha, 15), " E0 =", mp.nstr(E0, 12), "MeV  U_e =", mp.nstr(U_e, 12))
print()
for name, el, eu in rows:
    print(f"{name:22s} eps_log = {mp.nstr(el * 1000, 8)} keV   eps_U = {mp.nstr(eu * 1000, 8)} keV")

# comparison only: AME mirror splits Delta B (MeV); eps needed = 2 Delta B / (A - 1)
AME = [("3H/3He", 3, "0.763760"), ("7Li/7Be", 7, "1.643920"), ("11B/11C", 11, "2.763600"),
       ("13C/13N", 13, "3.003000"), ("15N/15O", 15, "3.536700"), ("17O/17F", 17, "3.542700"),
       ("39K/39Ca", 39, "7.306800"), ("41Ca/41Sc", 41, "7.278000")]
print("\nCOMPARISON ONLY (AME2020 mirror splits; values from the #9691 audit table):")
el1, eu1 = rows[0][1], rows[0][2]
for name, A, dB in AME:
    need = 2 * mp.mpf(dB) / (A - 1)
    print(f"  {name:10s} eps needed = {mp.nstr(need, 6)} MeV   need/eps_log = {mp.nstr(need / el1, 6)}"
          f"   need/eps_U = {mp.nstr(need / eu1, 6)}   need*A^(1/3) = {mp.nstr(need * mp.cbrt(A), 6)}")

print()
ok = all(c for _, c in checks)
for n, c in checks:
    print(("PASS " if c else "FAIL ") + n)
sys.exit(0 if ok else 1)
