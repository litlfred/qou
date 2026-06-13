#!/usr/bin/env python3
import sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent.parent / "tools" / "qou-substrate" / "python"))

from qou_substrate.constants import q_at, q_muon_at

M_E_MEV = "0.51099895069"
M_P_MEV = "938.27208816"
Q_NEUTRON_MEV = "0.78233341"

def main():
    mp.mp.dps = 60
    q_p = q_at(60)
    q_m = q_muon_at(60)
    
    M_e = mp.mpf(M_E_MEV)
    M_p = mp.mpf(M_P_MEV)
    Q_n = mp.mpf(Q_NEUTRON_MEV)
    M_n = M_p + M_e + Q_n
    M_N_avg = (M_p + M_n) / 2
    dt = (M_n - M_p) / M_N_avg
    
    tr_p = mp.mpf("-0.142072914342812797696363491737018429024644797405271291145864")
    tr_m = mp.mpf("-0.142072931422805612689507689049352360006875755905981520839179")
    
    r_p = dt / tr_p
    r_m = dt / tr_m
    
    print(f"Ratio at q_p: {r_p}")
    print(f"Ratio at q_m: {r_m}")
    print(f"Diff: {r_m - r_p}")
    
    h_p = q_p - 1/q_p
    h_m = q_m - 1/q_m
    hbar_p = 1 - 1/q_p
    hbar_m = 1 - 1/q_m
    u_p = mp.sqrt(q_p)
    u_m = mp.sqrt(q_m)
    
    for name, f_p, f_m in [
        ("h", h_p, h_m),
        ("hbar_q", hbar_p, hbar_m),
        ("h^2", h_p**2, h_m**2),
        ("hbar_q^2", hbar_p**2, hbar_m**2),
        ("h * hbar_q", h_p * hbar_p, h_m * hbar_m),
        ("hbar_q^3", hbar_p**3, hbar_m**3),
        ("1/u^2", 1/u_p**2, 1/u_m**2),
    ]:
        print(f"\nDividing by {name}:")
        v_p = r_p / f_p
        v_m = r_m / f_m
        print(f"  q_p: {v_p}")
        print(f"  q_m: {v_m}")
        print(f"  diff: {v_m - v_p}")
        
        # Test if it's a multiple of 1/alpha or something
        alpha = mp.mpf(1)/mp.mpf("137.0359991")
        print(f"  v_p * alpha: {v_p * alpha}")

if __name__ == "__main__":
    main()
