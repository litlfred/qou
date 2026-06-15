import sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import _path_bridge as _bridge

from _precision import set_compute_dps, fmt
from qou_substrate.constants import q_at, q_muon_at

def evaluate_basis(q):
    h = q - 1/q
    q2 = q + 1/q
    hbar = 1 - 1/q
    alpha_em = mp.mpf(1)/mp.mpf("137.0359991")
    
    basis = {
        "h^2": h**2,
        "h^4": h**4,
        "h^6": h**6,
        "h^8": h**8,
        "hbar^4": hbar**4,
        "hbar^6": hbar**6,
        "h^2 / [2]_q": h**2 / q2,
        "h^4 / [2]_q": h**4 / q2,
        "h^6 / [2]_q": h**6 / q2,
        "h^8 / [2]_q": h**8 / q2,
        "alpha_em * h^2": alpha_em * h**2,
        "alpha_em * h^4": alpha_em * h**4,
        "alpha_em * h^6": alpha_em * h**6
    }
    return basis

def main():
    set_compute_dps(50)
    q_p = q_at(50)
    q_m = q_muon_at(50)
    
    bp = evaluate_basis(q_p)
    bm = evaluate_basis(q_m)
    
    dq = q_m - q_p
    
    print(f"{'Basis':<20} {'Value':<20} {'Slope':<20} {'Slope/Value':<20}")
    print("-" * 80)
    for k in bp:
        val = bp[k]
        slope = (bm[k] - bp[k]) / dq
        ratio = slope / val if val != 0 else 0
        print(f"{k:<20} {float(val):<20.2e} {float(slope):<20.2e} {float(ratio):<20.2e}")

if __name__ == "__main__":
    main()
