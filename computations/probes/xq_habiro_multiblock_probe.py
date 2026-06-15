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
    set_compute_dps(60)
    q_p = q_at(60)
    q_m = q_muon_at(60)
    dt = _delta_target()
    
    # Let's find the exact epsilon required at q_p and q_m
    for label, q in [("q_proton", q_p), ("q_muon", q_m)]:
        xb = _x_baseline(q)
        residual = dt - xb
        # full trace = X_baseline + P_std * tr_std(O) * epsilon
        # X_baseline = P_triv * O_triv + P_sign * O_sign
        # O_scalar = [2]_q * h * hbar^2
        q2 = q + 1/q
        h = q - 1/q
        hbar = 1 - 1/q
        O_scalar = q2 * h * hbar**2
        
        # P_std = 4/6, tr_std(O) = 2 * O_scalar
        std_coeff = (mp.mpf(4)/6) * 2 * O_scalar
        epsilon = residual / std_coeff
        
        print(f"\n--- {label} ---")
        print(f"X_baseline = {xb}")
        print(f"residual   = {residual}")
        print(f"std_coeff  = {std_coeff}")
        print(f"epsilon    = {epsilon}")
        
        # Test values
        h_3_sq = (q**3 - q**(-3))**2
        c = (1 - epsilon) / h_3_sq
        print(f"If epsilon = 1 - c * h_(3)^2, then c = {c}")
        
        # Let's check PSLQ on epsilon
        print("PSLQ on epsilon:")
        res = mp.pslq([epsilon, 1, h**2, h**4, h**6, h**8, mp.mpf(1)/mp.mpf("137.0359991")], tol=1e-6)
        print(res)

if __name__ == "__main__":
    main()
