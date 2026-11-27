import sympy as sp
import mpmath as mp

# q0 read BY NAME (bean qou-9ugp, 2026-09-04). This held the RETIRED
# self-certified pin A as a literal -- retired 2026-08-22 for the CODATA-2022
# derivation, so the value was stale AND could not follow the anchor.
#
# MIGRATED TO PROTON on the owner ruling of 2026-08-30: proton is the default,
# and the burden is on the exception. Neither exception applies here -- this
# probe makes no explicit proton-vs-muon comparison (E1), and it is not about
# the CAL-1/2/3 triple as mathematics (E2). "It has always been muon" is
# expressly not a reason. This stem is not in `ideal_muon`, so `Q_50_DIGIT_STR`
# resolves to the proton pin.
import sys as _sys_qp  # noqa: E402
from pathlib import Path as _Path_qp  # noqa: E402
for _p_qp in (_Path_qp(__file__).resolve().parent,
              _Path_qp(__file__).resolve().parent.parent,
              _Path_qp(__file__).resolve().parent.parent / 'substrate'):
    if str(_p_qp) not in _sys_qp.path:
        _sys_qp.path.insert(0, str(_p_qp))
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

def main():
    mp.mp.dps = 60
    q_val = Q_MP
    q = sp.Symbol('q')
    
    # Hook length formula for quantum dimension:
    # dim_q(lambda) = n!_q / prod_{cells} [hook]_q
    # where [k]_q = (q^k - 1) / (q - 1)
    
    def q_int(k):
        return (q**k - 1) / (q - 1)
    
    def q_fact(n):
        res = 1
        for i in range(1, n + 1):
            res *= q_int(i)
        return res
    
    def hook_length(lam, i, j):
        # lam is a list of row lengths
        # cell (i, j)
        col_length = sum(1 for row in lam if row > j)
        return lam[i] - j + col_length - i - 1
    
    def q_dim(lam):
        n = sum(lam)
        num = q_fact(n)
        den = 1
        for i, row in enumerate(lam):
            for j in range(row):
                den *= q_int(hook_length(lam, i, j))
        return sp.simplify(num / den)
    
    partitions_5 = [
        (5,),
        (4, 1),
        (3, 2),
        (3, 1, 1),
        (2, 2, 1),
        (2, 1, 1, 1),
        (1, 1, 1, 1, 1)
    ]
    
    print(f"Quantum dimensions for H_5(q) at q_0 = {q_val}:\n")
    for lam in partitions_5:
        dim = q_dim(lam)
        dim_val = dim.subs(q, sp.Float(str(q_val), 60))
        print(f"Partition {lam}:")
        print(f"  Symbolic: {dim}")
        print(f"  Numeric:  {dim_val}")
        
        # We want to see if any of these can explain a 210 ppb shift.
        # Maybe the true mass is multiplied by something like: (dim_q(gen2) / dim_q(gen1)) ?
        # Or maybe (1 + something / dim_q) ?

if __name__ == "__main__":
    main()
