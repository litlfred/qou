"""Overall-scale gap of m_n - m_p in the derived electron unit (bean qou-mbfv, follow-up).

Pre-stated: the flavour cell is |c| * ln(tau_n/tau_p) with tau_p/tau_n = q^k.
k = 2 is forced for one nucleon block in convention D (NucleonSplitFullTower:
markov_forces_K; audit 2026-11-27-nucleon-split-full-tower.md). The per-nat unit is
|c| = m_e/(-ln tau_e) (#9718, ElectronCategoricalEnergy); E0 kept for comparison.
This probe derives nothing new: it states, at the comparison boundary only, which
exponent k the measured / literature numbers would need, and how many nats the model
proton mass is in the same log chart. mpmath 50 dps.
"""
import sys
from pathlib import Path
from mpmath import mp, mpf, log

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "computations" / "substrate"))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.dps = 50
q = mpf(Q_50_DIGIT_STR)
L = log(q)
tau_e = q**3 * (q**4 + 1) / (q**2 + 1)**2
c = 1 / (-log(tau_e))
E0 = 1 / (q * (q - 1))
M = mpf("1836.152673426")
print("model, derived unit: flavour cell (k=2) / m_e", mp.nstr(2 * L * c, 15))
print("model, log chart: proton mass in nats M/|c|", mp.nstr(M / c, 12))
print()
print("-- comparison boundary (data enter only here) --")
me = mpf("0.51099895069")
for uname, u in (("derived |c|", c), ("E0 (comparison)", E0)):
    for lab, t in (("CODATA m_n-m_p 1.29333", mpf("1.29333205")),
                   ("GLR 2020 QCD 1.87", mpf("1.87")),
                   ("BMW 2015 QCD 2.52", mpf("2.52"))):
        nats = t / me / u
        print(f"{uname:16s} {lab:24s} needs {mp.nstr(nats, 6):>8s} nats, k = {mp.nstr(nats / L, 6)}")
