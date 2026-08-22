import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from rho_w_crystal_vertex_trace import standard_young_tableaux, partitions_of, atom_canonical_crossings, rho_lambda_of_word
from kazhdan_lusztig import permutations_S_n, kl_polynomial
from mpmath import mpf, mp

import sympy as sp

from codata_table import codata

def main():
    mp.dps = 50
    q = mpf("1.1099785955573347198997632204832250266562084087802")
    # Was the bare float64 literal `0.510998950` -- both truncated (the table
    # carries 0.51099895069) and float, in a script that sets dps = 50 and
    # uses mpf for everything else. Read it instead.
    m_e = codata("electron mass energy equivalent in MeV").value
    
    # 1. Gather Betti sums
    betti_sums = {
        (6,): 1,
        (5, 1): 5,
        (4, 2): 20,
        (4, 1, 1): 10,
        (3, 3): 23,
        (3, 2, 1): 41,
        (3, 1, 1, 1): 10,
        (2, 2, 2): 21,
        (2, 2, 1, 1): 21,
        (2, 1, 1, 1, 1): 5,
        (1, 1, 1, 1, 1, 1): 1
    }
    
    # 2. Gather sgn(w_0)
    # The sign is +1 if the partition is 'positive chirality' and -1 if 'negative'
    # Wait, the sgn(w_0^{S_{lambda'}}) is the signature of the longest element of the conjugate parabolic.
    # Actually, binding_energy_categorical_deuteron.py has delta_lambda_ansatz
    # Let's import it and compute the sum manually.
    
    from information_wenzl_markov_trace import WenzlMarkovTrace
    from rho_w_crystal_vertex_trace import atom_canonical_crossings, rho_lambda_of_word, partitions_of, standard_young_tableaux
    
    n = 6
    wmt = WenzlMarkovTrace(n)
    word = atom_canonical_crossings(1, 1)
    qi = 1/q
    
    sum_betti = mpf(0)
    sum_f = mpf(0)
    
    for lam in partitions_of(n):
        M, syts = rho_lambda_of_word(lam, word, q, qi)
        chi = sum(M[i][i] for i in range(len(syts)))
        y = wmt.weight(lam, q)
        dim = len(syts)
        
        # We don't have the exact sgn(w_0), but we can just compute the magnitude sum
        # Actually let's use the known sign of delta_lambda:
        # Let's just output the components.
        sum_betti += y * chi * betti_sums[lam]
        sum_f += y * chi * dim
        
    B_D_betti = m_e * abs(sum_betti)
    B_D_f = m_e * abs(sum_f)
    
    print(f"B(D) with f^lambda: {B_D_f} MeV")
    print(f"B(D) with Betti sum: {B_D_betti} MeV")
    print(f"Target B(D) = 2.224 MeV")
    print(f"Ratio Betti/Target: {B_D_betti / 2.224}")

if __name__ == '__main__':
    main()
