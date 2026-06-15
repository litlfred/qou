import sys
import time
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))

from _precision import set_compute_dps, fmt
from witness_base import WitnessBuilder
from experimental_constants import M_E_MEV, M_P_MEV, Q_NEUTRON_MEV

try:
    from qou_substrate.constants import q_at, q_muon_at
except ImportError:
    sys.exit(1)

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
    
    # Try finding an integer relation for delta_target at q_p
    # using basis: 1, h^2, h^4, h^6, h^8
    h_p = q_p - 1/q_p
    basis = [mp.mpf(1), h_p**2, h_p**4, h_p**6, h_p**8]
    
    print("PSLQ on basis: 1, h^2, h^4, h^6, h^8, delta_target")
    res = mp.pslq(basis + [dt], tol=1e-30)
    print("Result at q_p:", res)
    
    # Let's also include [2]_q and [3]_q and alpha_em
    alpha_em = mp.mpf(1)/mp.mpf("137.0359991")
    basis2 = [mp.mpf(1), h_p**2, h_p**4, h_p**6, alpha_em, alpha_em * h_p**2, alpha_em * h_p**4]
    res2 = mp.pslq(basis2 + [dt], tol=1e-30)
    print("Result2 at q_p:", res2)

    # Let's check classical Habiro elements: (1-q)(1-q^-1) = 2 - [2]_q = - h^2 / q? No, (1-q)(1-1/q) = 2 - q - 1/q
    # Actually, 2 - [2]_q = -(q^{1/2} - q^{-1/2})^2 = - h_{1/2}^2
    
    # Wait, the target is 0.001382...
    # Let's just run this to see.

if __name__ == "__main__":
    main()
