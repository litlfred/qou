#!/usr/bin/env python3
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
    p_crossings = atom_canonical_crossings(1, 0, include_inter=False)
    n_crossings = atom_canonical_crossings(0, 1, include_inter=False)
    
    blocks = [(3,), (2,1), (1,1,1)]
    delta_tr_sym = {}
    for lam in blocks:
        chi_p = q_character_on_braid_word(lam, p_crossings, q_sym)
        chi_n = q_character_on_braid_word(lam, n_crossings, q_sym)
        y_w = y_lambda_wenzl_bridge_symbolic(lam)
        q_pos = sp.Symbol("q", positive=True)
        y_w = y_w.subs(q_pos, q_sym)
        delta_tr_sym[lam] = sp.cancel(y_w * (chi_n - chi_p))

    vals_p = {}
    vals_m = {}
    
    for lam in blocks:
        vals_p[lam] = float(delta_tr_sym[lam].subs(q_sym, q_p).evalf(60))
        vals_m[lam] = float(delta_tr_sym[lam].subs(q_sym, q_m).evalf(60))
        
    print("Values at q_proton:")
    for lam in blocks:
        print(f"  {lam}: {vals_p[lam]}")
        
    print("Values at q_muon:")
    for lam in blocks:
        print(f"  {lam}: {vals_m[lam]}")
        
    import numpy as np
    A = np.array([
        [vals_p[(3,)], vals_p[(2,1)]],
        [vals_m[(3,)], vals_m[(2,1)]]
    ])
    
    print(f"\nDeterminant of A: {np.linalg.det(A)}")
    
    target = float(dt)
    
    print("\nExpressing C_3 and C_21 in terms of C_111:")
    for c_111 in [0, 1, -1, 0.5, -0.5, 1/6, 1/3, -1/6, -1/3]:
        B = np.array([
            target - c_111 * vals_p[(1,1,1)],
            target - c_111 * vals_m[(1,1,1)]
        ])
        try:
            res = np.linalg.solve(A, B)
            print(f"If C_111 = {c_111:6.3f} => C_3 = {res[0]:12.3f}, C_21 = {res[1]:12.3f}")
        except np.linalg.LinAlgError:
            print("Singular matrix!")

if __name__ == "__main__":
    main()
