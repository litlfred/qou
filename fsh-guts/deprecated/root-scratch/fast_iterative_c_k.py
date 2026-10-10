import sys
import os
import json
import sympy as sp
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, ".."))
for _p in (
    _ROOT,
    os.path.join(_ROOT, "tools", "pyhecke", "python"),
    os.path.join(_ROOT, "tools", "qou-substrate", "python"),
):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import computations.qbeta.qbeta_h4_nucleon_assembly as h4

def fast_series(expr, var, order):
    """Fast series expansion of a rational function."""
    expr = sp.cancel(expr)
    num, den = sp.fraction(expr)
    num_s = sp.series(num, var, 0, order).removeO()
    den_s = sp.series(den, var, 0, order).removeO()
    # Polynomial division
    res = sp.series(num_s / den_s, var, 0, order).removeO()
    return res

def main():
    q = h4.q
    h = q - 1 / q
    t = sp.symbols("t", real=True)
    q_sub = 1 / (1 - t)
    
    t0 = time.time()
    print("Evaluating Groebner-Shirshov dnet...")
    net_n = h4.augmentation(h4.nucleon_nf(["u", "d", "d"]))
    net_p = h4.augmentation(h4.nucleon_nf(["u", "u", "d"]))
    dnet = sp.cancel(net_n - net_p)
    counit = h**2 / 2 - h
    ratio_A = sp.cancel(dnet / counit)
    print(f"Assembly took {time.time() - t0:.2f}s")
    
    # We want to substitute q = 1/(1-t)
    print("Substituting q -> 1/(1-t)...")
    ratio_t_expr = sp.cancel(ratio_A.subs(q, q_sub))
    
    # Pre-form cos base components
    z_sub = sp.sqrt(q_sub) / (1 + q_sub)
    h_sub = q_sub - 1/q_sub
    alpha_sub = (z_sub - 1) * h_sub / 2
    b_sub = sp.sqrt((h_sub**2 + 3) / (h_sub**2 + 4))
    
    cos_arg = alpha_sub - b_sub * t**2 / 2
    
    for N in range(1, 4):
        print(f"\n--- Extracting c_{N} (O(t^{2*N})) ---")
        order = 2 * N + 1
        t_start = time.time()
        
        ratio_t = fast_series(ratio_t_expr, t, order)
        
        transformed_ratio = sp.expand(ratio_t.subs(t, sp.I * t))
        real_transformed = sp.re(transformed_ratio)
        
        cos_base = sp.series(sp.cos(cos_arg), t, 0, order).removeO()
        ladder_departure = sp.series(real_transformed / cos_base, t, 0, order).removeO()
        
        coeff = ladder_departure.coeff(t, 2 * N)
        print(f"c_{N} raw t^(2*{N}) coeff: {coeff}")
        print(f"Took {time.time() - t_start:.2f}s")

if __name__ == '__main__':
    main()
