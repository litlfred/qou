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
    
    xp = _x_baseline(q_p)
    xm = _x_baseline(q_m)
    
    dq = q_m - q_p
    dx = xm - xp
    
    print(f"delta_target = {dt}")
    print(f"X(q_p) = {xp}")
    print(f"X(q_m) = {xm}")
    print(f"dq = {dq}")
    print(f"dx = {dx}")
    print(f"dX/dq = {dx/dq}")

    # To make X_pred(q) = dt at both, we need X_pred'(q) ≈ 0.
    # What if X_pred(q) = X_baseline(q) - (dx/dq)/(dH/dq) * H(q)?

if __name__ == "__main__":
    main()
