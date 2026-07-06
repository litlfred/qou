import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from kazhdan_lusztig import permutations_S_n, kl_polynomial
from probe_option_e_probe4_kl_batch import rsk, get_shape, syt_to_tuple, canonical_Q
import sympy as sp

def main():
    n = 7
    perms = permutations_S_n(n)
    
    left_cells = {}
    for w in perms:
        P, Q = rsk(w)
        lam = get_shape(P)
        Q_tup = syt_to_tuple(Q)
        if lam not in left_cells:
            left_cells[lam] = {}
        if Q_tup not in left_cells[lam]:
            left_cells[lam][Q_tup] = []
        left_cells[lam][Q_tup].append(w)
        
    s = sp.Symbol('s')
    for lam, cells in left_cells.items():
        Q_can = canonical_Q(lam)
        if Q_can not in cells:
            Q_can = list(cells.keys())[0]
        cell_w = cells[Q_can]
        
        sum_betti = 0
        for w in cell_w:
            p_poly = kl_polynomial(tuple(range(1, n+1)), w)
            betti = int(p_poly.subs({s: 1 for s in p_poly.free_symbols}))
            sum_betti += betti
            
        print(f"({lam}): {sum_betti},")

if __name__ == '__main__':
    main()
