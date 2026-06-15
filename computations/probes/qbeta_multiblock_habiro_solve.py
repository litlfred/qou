#!/usr/bin/env python3
import sys
from pathlib import Path
import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import _path_bridge as _bridge

from habiro.habiro_coefficients_atomic import to_u_polynomial, cyclotomic_expansion
from canonical_braid_crossings import atom_canonical_crossings
from hecke_character_symbolic import q_character_on_braid_word
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_symbolic

def main():
    q_sym = sp.Symbol("q", positive=True)
    check_q = sp.Symbol("check_q", positive=True, real=True)
    
    p_crossings = atom_canonical_crossings(1, 0, include_inter=False)
    n_crossings = atom_canonical_crossings(0, 1, include_inter=False)
    
    blocks = [(3,), (2,1), (1,1,1)]
    
    for lam in blocks:
        print(f"\n{'='*78}")
        print(f" Block {lam}")
        print(f"{'='*78}")
        
        chi_p = q_character_on_braid_word(lam, p_crossings, q_sym)
        chi_n = q_character_on_braid_word(lam, n_crossings, q_sym)
        y_w = y_lambda_wenzl_bridge_symbolic(lam)
        
        q_pos = sp.Symbol("q", positive=True)
        y_w = y_w.subs(q_pos, q_sym)
        
        delta_tr = sp.cancel(y_w * (chi_n - chi_p))
        
        p_u, shift, denom = to_u_polynomial(delta_tr, q_sym, check_q)
        
        print(f"  shift: {shift}")
        print(f"  denom: {denom}")
        
        coeffs = cyclotomic_expansion(p_u, check_q, max_m=12)
        print("  Habiro coefficients Δa_{m, λ}:")
        for entry in coeffs:
            print(f"    m={entry['m']}: {entry['a_m']}")
            
if __name__ == "__main__":
    main()
