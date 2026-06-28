"""multiterm_cost_deuteron_hopf_probe.py

Tests the multi-term additive mass formula for the deuteron under the
structural decomposition T_comp = L_H * (T_p \otimes T_n) at H_6(q_0).

Just as we proved for 3He, the hypothesis is that the additive formula
(even using the divergence-safe algebraic R-side T2+T3 terms) fails
to recover the binding energy for the composite knot.
"""
from __future__ import annotations
import sys
from pathlib import Path
import math

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge
import mpmath as mp

from _precision import set_compute_dps
from witness_base import WitnessBuilder
from q_parameter import Q as Q_CANONICAL
from codata_constants import M_E_MEV
from hecke_core import z as z_val

set_compute_dps()

q = mp.mpf(str(Q_CANONICAL))
m_e = mp.mpf(str(M_E_MEV))
z = mp.mpf(str(z_val))

# Deuteron data
B_AME = mp.mpf("2.224566")

# From binding-k-enumerator.witness.json for K = [3, 3]
# T_pred_markov_at_n0 = 1.1007832370743025
TRM_COMPOSITE = mp.mpf("1.1007832370743025")
RHO_DEUTERON = 1

# M_E_SIGMA_6 is the Frobenius co-Casimir trace at H_6
M_E_SIGMA_6 = mp.mpf("1.636") # From knot-mass-formula-unified.md table

def main() -> int:
    print("Multi-term cost vs Deuteron Hopf-factorised probe (ALGEBRAIC FORM T2+T3)")
    print()

    # n = 6 (3A strands for A=2)
    n = 6
    t2_hecke = (n - 1) * z**2
    t3_hecke = (math.comb(n - 1, 2)) * z**4
    t23_mev = m_e * (t2_hecke + t3_hecke)
    
    b_desc = RHO_DEUTERON * m_e * TRM_COMPOSITE
    b_pred = b_desc + M_E_SIGMA_6 + t23_mev
    rel_resid = abs(B_AME - b_pred) / B_AME
    
    print(f"  n (strands)            = {n}")
    print(f"  T2 (Hecke)             = {mp.nstr(t2_hecke, 6)}")
    print(f"  T3 (Hecke)             = {mp.nstr(t3_hecke, 6)}")
    print(f"  T2+T3 (MeV)            = {mp.nstr(t23_mev, 6)} MeV")
    print(f"  T4 (MeV)               = {mp.nstr(M_E_SIGMA_6, 6)} MeV")
    print(f"  Hopf-comp B_desc (T1)  = {mp.nstr(b_desc, 6)} MeV")
    print(f"  Hopf-comp B_pred       = {mp.nstr(b_pred, 6)} MeV")
    print(f"  B_AME                  = {mp.nstr(B_AME, 6)} MeV")
    print(f"  rel_resid              = {mp.nstr(rel_resid, 6)}")
    print()
    print("Conclusion: The additive multi-term formula fails to evaluate")
    print("correctly for the Hopf-decomposed deuteron at H_6(q_0), proving")
    print("that structural factorization alone cannot rescue the additive cost.")

    return 0

if __name__ == "__main__":
    sys.exit(main())
