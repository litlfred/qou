"""Ratio of the flavour term to the EM term of m_n - m_p under one energy map.

Lean: QOU/Nuclear/NucleonSplitScaleRatio.lean (flavour_over_em): the ratio is
-2L/(a*Q), independent of the energy map E. Here L = log q0, a = alpha_em(q0)
(alpha_em_inv_derived, conditional on the Witten-kappa Gram sorry), Q = 1/3.
Literature values are comparison points only (papers in library/), printed last.
mpmath at 50 dps, proton pin.
"""
import sys
from pathlib import Path
from mpmath import mp, mpf, log

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "computations" / "substrate"))
sys.path.insert(0, str(ROOT / "computations"))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.dps = 50
q = mpf(Q_50_DIGIT_STR)
L = log(q)
alpha = 1 / mpf("137.0359350940")  # alpha_em_inv_derived, as in nucleon-split-gibbs-coulomb
Q = mpf(1) / 3
ratio = 2 * L / (alpha * Q)  # |flavour / EM|, any energy map
E0 = mpf("4.18598136329")

print("log q0               ", mp.nstr(L, 20))
print("|flavour/EM| (model) ", mp.nstr(ratio, 15))
print("E0 map: flavour      ", mp.nstr(2 * E0 * L, 12), "MeV")
print("E0 map: EM           ", mp.nstr(-E0 * alpha * Q, 12), "MeV")
print()
print("comparison only (n - p convention, MeV):")
for name, qcd, qed in [("BMW 2015 (1406.4088)", "2.52", "-1.00"),
                       ("Gasser-Leutwyler-Rusetsky 2020 (2008.05806)", "1.87", "-0.58"),
                       ("Walker-Loud-Carlson-Miller 2012 (1210.7777)", "2.53", "-1.30")]:
    qcd, qed = mpf(qcd), mpf(qed)
    lit = -qcd / qed
    E_em = -qed / (alpha * Q)       # map that gives EM its literature size
    print(f"  {name}: |QCD/QED| = {mp.nstr(lit, 4)}; model/lit = {mp.nstr(ratio / lit, 4)};"
          f" E for EM = {mp.nstr(E_em, 6)} MeV -> flavour = {mp.nstr(-qed * ratio, 6)} MeV;"
          f" E for QCD = {mp.nstr(qcd / (2 * L), 6)} MeV -> EM = {mp.nstr(-qcd / ratio, 6)} MeV")
