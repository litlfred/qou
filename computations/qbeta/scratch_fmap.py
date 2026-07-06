#!/usr/bin/env python3
import sys
import os
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
for _sub in ("", "hecke", "markov"):
    _p = str(HERE.parent / _sub) if _sub else str(HERE.parent)
    if _p not in sys.path:
        sys.path.insert(0, _p)
        
import _path_bridge as _pb

from qbeta_utils import substrate_ladder_quantities, c3_target_at
from experimental_constants import Q_NEUTRON_MEV, M_E_MEV
from q_parameter import Q_50_DIGIT_STR, q_muon_at

mp.mp.dps = 65

def main():
    q_p = mp.mpf(Q_50_DIGIT_STR)
    q_m = mp.mpf(q_muon_at(50))
    
    sub_p = substrate_ladder_quantities(q_p)
    sub_m = substrate_ladder_quantities(q_m)
    
    u_p = sub_p["u"]
    u_m = sub_m["u"]
    
    c3_p = c3_target_at(q_p, mp.mpf(Q_NEUTRON_MEV), mp.mpf(M_E_MEV))
    c3_m = c3_target_at(q_m, mp.mpf(Q_NEUTRON_MEV), mp.mpf(M_E_MEV))
    
    dt_p = mp.mpf("-0.142072931427013502260031150440686517511999552233807196315064")
    dt_m = mp.mpf("-0.142072931422805612689507689049352360006875755905981505789682")
    
    print(f"u_p = {u_p}")
    print(f"u_m = {u_m}")
    print(f"c3_p = {c3_p}")
    print(f"c3_m = {c3_m}")
    
    # We want a map f(dt_M) -> c3.
    # What if c3 is proportional to d(dt_M)/du ?
    # Let's check numerical derivative.
    ddt_du = (dt_m - dt_p) / (u_m - u_p)
    print(f"d(dt_M)/du ≈ {ddt_du}")
    
    dc3_du = (c3_m - c3_p) / (u_m - u_p)
    print(f"dc3/du ≈ {dc3_du}")
    
    # F(u) ODE is F'' + (A + B u + C u^2)F = 0.
    # We found A=2, B = -6 c3 = 12.13.
    # Maybe dt_M is related to the conjugate momentum? F' ?
    # F' = -2u + 3 c3 u^2 + ...
    F_p_prime = -2*u_p + 3*c3_p*u_p**2
    F_m_prime = -2*u_m + 3*c3_m*u_m**2
    
    print(f"F'_p ≈ {F_p_prime}")
    print(f"F'_m ≈ {F_m_prime}")
    
    # Is F'_p proportional to dt_p?
    ratio_p = F_p_prime / dt_p
    ratio_m = F_m_prime / dt_m
    print(f"F'_p / dt_p = {ratio_p}")
    print(f"F'_m / dt_m = {ratio_m}")
    
    # What about F''? F'' = -2 + 6 c3 u
    F_p_dp2 = -2 + 6*c3_p*u_p
    F_m_dp2 = -2 + 6*c3_m*u_m
    print(f"F''_p / dt_p = {F_p_dp2 / dt_p}")
    print(f"F''_m / dt_m = {F_m_dp2 / dt_m}")

if __name__ == "__main__":
    main()
