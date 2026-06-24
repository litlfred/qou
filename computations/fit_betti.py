import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from rho_w_crystal_vertex_trace import partitions_of, standard_young_tableaux
import numpy as np

def get_f_lam(n):
    res = {}
    for lam in partitions_of(n):
        res[lam] = len(standard_young_tableaux(lam))
    return res

betti_n4 = {
    (4,): 1,
    (3, 1): 3,
    (2, 1, 1): 3,
    (2, 2): 3,
    (1, 1, 1, 1): 1
}

betti_n5 = {
    (5,): 1,
    (4, 1): 4,
    (3, 1, 1): 6,
    (3, 2): 9,
    (2, 1, 1, 1): 4,
    (2, 2, 1): 10,
    (1, 1, 1, 1, 1): 1
}

betti_n6 = {
    (6,): 1,
    (5, 1): 5,
    (4, 1, 1): 10,
    (4, 2): 20,
    (3, 1, 1, 1): 10,
    (3, 2, 1): 41,
    (2, 1, 1, 1, 1): 5,
    (3, 3): 23,
    (2, 2, 1, 1): 21,
    (2, 2, 2): 21,
    (1, 1, 1, 1, 1, 1): 1
}

def analyze(n, betti):
    f_lam = get_f_lam(n)
    print(f"n={n}")
    for lam in partitions_of(n):
        print(f"  {lam}: Betti={betti[lam]}, f={f_lam[lam]}, diff={betti[lam] - f_lam[lam]}")

analyze(4, betti_n4)
analyze(5, betti_n5)
analyze(6, betti_n6)
