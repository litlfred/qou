import sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import _path_bridge as _bridge

from _precision import set_compute_dps, fmt
from experimental_constants import M_E_MEV, M_P_MEV, Q_NEUTRON_MEV
from qou_substrate.constants import q_at, q_muon_at

def _delta_target():
    M_e = mp.mpf(repr(M_E_MEV))
    M_p = mp.mpf(repr(M_P_MEV))
    Q_n = mp.mpf(repr(Q_NEUTRON_MEV))
    M_n = M_p + M_e + Q_n
    M_N_avg = (M_p + M_n) / 2
    return (M_n - M_p) / M_N_avg

def _x_baseline(q):
    return (q - 1)**2 * (1 - q**(-4)) / 3

def main():
    set_compute_dps(50)
    q_p = q_at(50)
    q_m = q_muon_at(50)
    dt = _delta_target()
    
    print(f"Target: {dt}")
    
    for label, q in [("q_proton", q_p), ("q_muon", q_m)]:
        print(f"\n--- {label} ---")
        X_base = _x_baseline(q)
        print(f"X_baseline: {X_base}")
        
        hbar_q = 1 - 1/q
        h_q = q - 1/q
        q2 = q + 1/q
        
        # Original X(q) numerator
        num = hbar_q**2 * h_q * q2
        
        # Classical weight: 1/3
        print(f"Classical: {num / 3}")
        
        # Q-deformed weights
        # V_trivial: 1, V_sign: 1, V_standard: [2]_q
        # Sum of squares = 2 + [2]_q^2
        # Weight of 1-dim blocks = 2 / (2 + [2]_q^2)
        q_weight_1 = mp.mpf(2) / (2 + q2**2)
        print(f"Q-deformed 1-dim weight (2 / (2 + [2]_q^2)): {num * q_weight_1}")
        
        # What about [3]_q? 
        # [3]_q = q^2 + 1 + q^{-2} = [2]_q^2 - 1
        # Sum of q-dims = 1 + [2]_q + 1 = 2 + [2]_q
        # Sum of squares = 2 + [2]_q^2
        q3 = q**2 + 1 + q**(-2)
        
        # [3]_q! = [3]_q [2]_q [1]_q
        
        print(f"num / [3]_q: {num / q3}")
        
        # Wait, the total dimension of H_3 is 3! = 6 classically.
        # Q-deformed total dimension is [3]_q! = [3]_q [2]_q.
        # Q-weight of 1-dim blocks: 2 / [3]_q! = 2 / ([3]_q [2]_q)
        q_weight_2 = mp.mpf(2) / (q3 * q2)
        print(f"Q-deformed weight (2 / [3]_q!): {num * q_weight_2}")
        
        # Let's test combinations
        print(f"num / 2.99... : {num / (dt * 3 / X_base)}") # Reverse engineer denominator

if __name__ == "__main__":
    main()
