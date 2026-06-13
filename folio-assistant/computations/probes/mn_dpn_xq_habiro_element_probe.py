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
    set_compute_dps()
    q_p = q_at()
    q_m = q_muon_at()
    dt = _delta_target()
    
    print(f"delta_target: {dt}")
    print(f"X_baseline(q_p): {_x_baseline(q_p)}")
    print(f"X_baseline(q_m): {_x_baseline(q_m)}")
    
    h_p = q_p - 1/q_p
    h_m = q_m - 1/q_m
    alpha_em = mp.mpf(1)/mp.mpf("137.0359991")
    
    basis = [mp.mpf(1), h_p**2, h_p**4, h_p**6, h_p**8]
    print("PSLQ on basis: 1, h^2, h^4, h^6, h^8, delta_target at q_p")
    res = mp.pslq(basis + [dt], tol=1e-30)
    print("Result:", res)
    
    basis2 = [mp.mpf(1), h_p**2, h_p**4, alpha_em, alpha_em * h_p**2]
    res2 = mp.pslq(basis2 + [dt], tol=1e-30)
    print("Result2:", res2)

    # Let's compute delta_target - X_baseline to see the residual
    resid_p = dt - _x_baseline(q_p)
    resid_m = dt - _x_baseline(q_m)
    print(f"resid_p: {resid_p}")
    print(f"resid_m: {resid_m}")

if __name__ == "__main__":
    main()
