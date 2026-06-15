import sys
from pathlib import Path
import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import _path_bridge as _bridge

from _precision import set_compute_dps
from experimental_constants import M_E_MEV, M_P_MEV, Q_NEUTRON_MEV
from qou_substrate.constants import q_at, q_muon_at

from canonical_braid_crossings import atom_canonical_crossings
from hecke_character_symbolic import q_character_on_braid_word
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_symbolic

def _delta_target():
    M_e = mp.mpf(repr(M_E_MEV))
    M_p = mp.mpf(repr(M_P_MEV))
    Q_n = mp.mpf(repr(Q_NEUTRON_MEV))
    M_n = M_p + M_e + Q_n
    M_N_avg = (M_p + M_n) / 2
    return (M_n - M_p) / M_N_avg

def main():
    set_compute_dps(60)
    q_p = q_at(60)
    q_m = q_muon_at(60)
    dt = _delta_target()
    
    q_sym = sp.Symbol("q", positive=True)
    
    # Proton (Z=1, N=0) and Neutron (Z=0, N=1)
    p_crossings = atom_canonical_crossings(1, 0, include_inter=False)
    n_crossings = atom_canonical_crossings(0, 1, include_inter=False)
    
    blocks = [(3,), (2,1), (1,1,1)]
    
    delta_tr_sym = {}
    for lam in blocks:
        # compute character
        chi_p = q_character_on_braid_word(lam, p_crossings, q_sym)
        chi_n = q_character_on_braid_word(lam, n_crossings, q_sym)
        y_w = y_lambda_wenzl_bridge_symbolic(lam)
        
        # wait, y_lambda uses Symbol("q"), need to substitute q_sym if different
        q_pos = sp.Symbol("q", positive=True)
        y_w = y_w.subs(q_pos, q_sym)
        
        delta_tr_sym[lam] = sp.cancel(y_w * (chi_n - chi_p))

    for label, q_val in [("q_proton", q_p), ("q_muon", q_m)]:
        print(f"\n--- {label} ---")
        vals = {}
        total = mp.mpf(0)
        for lam in blocks:
            v_expr = delta_tr_sym[lam].subs(q_sym, q_val)
            v = mp.mpf(str(v_expr.evalf(60)))
            vals[lam] = v
            total += v
            print(f"Δtr_{lam} = {v}")
            
        print(f"Total Δtr_M = {total}")
        print(f"Target Δ    = {dt}")
        print(f"Ratio       = {dt / total}")
        
        xb = (q_val - 1)**2 * (1 - q_val**(-4)) / 3
        print(f"X_baseline  = {xb}")

if __name__ == "__main__":
    main()
