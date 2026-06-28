"""multiterm_cost_he3_l6a4_probe_algebraic.py

Tests the hypothesis: "using the R-side algebraic form (symbolic form) for T2 and T3
rescues the multi-term mass formula for He3 and allows L6a4 to win."

For the algebraic form:
T2 = (n-1) * z^2
T3 = binomial(n-1, 2) * z^4
where n is the strand count (n=9 for He3 full atom, or n=3 for interface).
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
from codata_constants import M_E_MEV, AME_B_HE3_MEV_VALIDATION
from hecke_core import z as z_val

set_compute_dps()

q = mp.mpf(str(Q_CANONICAL))
m_e = mp.mpf(str(M_E_MEV))
z = mp.mpf(str(z_val))

# He3 data
B_AME = mp.mpf(str(AME_B_HE3_MEV_VALIDATION))
ALPHA_GAP_L6A4 = mp.mpf("0.0")
TRM_L6A4 = mp.mpf("0.998367")
RHO_L6A4 = 3
M_E_SIGMA_9 = mp.mpf("1.2999219630934102")

def main() -> int:
    print("Multi-term cost vs He3 L6a4 probe (ALGEBRAIC FORM T2+T3)")
    print()

    # n = 9 (3A strands for A=3)
    n = 9
    t2_hecke = (n - 1) * z**2
    t3_hecke = (math.comb(n - 1, 2)) * z**4
    t23_mev = m_e * (t2_hecke + t3_hecke)
    
    b_desc = RHO_L6A4 * m_e * TRM_L6A4
    b_pred = b_desc + M_E_SIGMA_9 + t23_mev
    rel_resid = abs(B_AME - b_pred) / B_AME
    
    print(f"  n (strands)            = {n}")
    print(f"  T2 (Hecke)             = {mp.nstr(t2_hecke, 6)}")
    print(f"  T3 (Hecke)             = {mp.nstr(t3_hecke, 6)}")
    print(f"  T2+T3 (MeV)            = {mp.nstr(t23_mev, 6)} MeV")
    print(f"  T4 (MeV)               = {mp.nstr(M_E_SIGMA_9, 6)} MeV")
    print(f"  L6a4 B_desc (T1)       = {mp.nstr(b_desc, 6)} MeV")
    print(f"  L6a4 B_pred (T1+T23+T4)= {mp.nstr(b_pred, 6)} MeV")
    print(f"  B_AME                  = {mp.nstr(B_AME, 6)} MeV")
    print(f"  rel_resid              = {mp.nstr(rel_resid, 6)}")
    print()

    # Try interface n=3
    n3 = 3
    t2_3 = (n3 - 1) * z**2
    t3_3 = (math.comb(n3 - 1, 2)) * z**4
    t23_3_mev = m_e * (t2_3 + t3_3)
    b_pred_3 = b_desc + M_E_SIGMA_9 + t23_3_mev
    print(f"  If n=3 (interface):")
    print(f"  T2+T3 (MeV)            = {mp.nstr(t23_3_mev, 6)} MeV")
    print(f"  L6a4 B_pred            = {mp.nstr(b_pred_3, 6)} MeV")

    return 0

if __name__ == "__main__":
    sys.exit(main())
