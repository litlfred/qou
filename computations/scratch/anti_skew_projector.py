import sys
import math
from pathlib import Path

# Add the substrate module
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

import mpmath as mp
from q_parameter import Q as q0_float

q = mp.mpf(str(q0_float))

def anti_skew_projector_cn(n):
    # c_n = sum_{w in S_n} q^{-2 L(w)}
    t = q**(-2)
    cn = mp.mpf(1)
    for i in range(1, n+1):
        factor = mp.mpf(0)
        for j in range(i):
            factor += t**j
        cn *= factor
    return cn

for n in range(1, 5):
    print(f"c_{n} = {anti_skew_projector_cn(n)}")
