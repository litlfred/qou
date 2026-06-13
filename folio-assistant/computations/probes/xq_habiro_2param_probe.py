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
    
    xp = _x_baseline(q_p)
    xm = _x_baseline(q_m)
    
    dp = dt - xp
    dm = dt - xm
    
    hp = q_p - 1/q_p
    hm = q_m - 1/q_m
    
    # We want alpha * hp^A + beta * hp^B = dp
    # and alpha * hm^A + beta * hm^B = dm
    
    pairs = [(2,4), (4,6), (6,8), (4,8), (2,6)]
    print(f"Target dp: {dp}")
    print(f"Target dm: {dm}")
    
    for A, B in pairs:
        # Solve the 2x2 linear system
        det = hp**A * hm**B - hp**B * hm**A
        if det == 0:
            continue
        alpha = (dp * hm**B - dm * hp**B) / det
        beta = (hp**A * dm - hm**A * dp) / det
        
        print(f"\n--- Basis h^{A}, h^{B} ---")
        print(f"alpha = {alpha}")
        print(f"beta  = {beta}")
        
        # Are alpha, beta close to rational numbers or known constants?
        # Let's PSLQ them individually
        print("PSLQ alpha:")
        res_a = mp.pslq([alpha, 1, mp.mpf(1)/mp.mpf("137.0359991"), mp.catalan, mp.pi], tol=1e-5)
        print(res_a)
        
        print("PSLQ beta:")
        res_b = mp.pslq([beta, 1, mp.mpf(1)/mp.mpf("137.0359991"), mp.catalan, mp.pi], tol=1e-5)
        print(res_b)

if __name__ == "__main__":
    main()
