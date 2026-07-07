import sys
import os
import json
import sympy as sp

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

CACHE_FILE = os.path.join(_HERE, "c_k_faddeev_cache.json")

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=4)

def main():
    q = h4.q
    h = q - 1 / q
    t = sp.symbols("t", real=True)
    q_sub = 1 / (1 - t)
    
    print("Evaluating Groebner-Shirshov dnet...")
    dnet = sp.cancel(
        h4.augmentation(h4.nucleon_nf(["u", "d", "d"]))
        - h4.augmentation(h4.nucleon_nf(["u", "u", "d"]))
    )
    counit = h**2 / 2 - h
    ratio_A = sp.cancel(dnet / counit)
    
    cache = load_cache()
    
    for N in range(1, 8):
        key = f"c_{N}"
        if key in cache:
            print(f"Skipping {key}, already in cache")
            continue
            
        print(f"\n--- Extracting {key} (O(t^{2*N})) ---")
        order = 2 * N + 1
        
        # 1. Expand ratio
        print("  1. Series expanding base ratio...")
        ratio_t = sp.series(ratio_A.subs(q, q_sub), t, 0, order).removeO()
        
        # 2. Apply Faddeev Modular Double Transformation t -> I*t
        print("  2. Applying Faddeev modular double (t -> i*t)...")
        transformed_ratio = sp.expand(ratio_t.subs(t, sp.I * t))
        real_transformed = sp.re(transformed_ratio)
        
        # 3. Form cos base
        print("  3. Forming cos base and ladder departure...")
        z_sub = sp.sqrt(q_sub) / (1 + q_sub)
        h_sub = q_sub - 1/q_sub
        alpha_sub = (z_sub - 1) * h_sub / 2
        b_sub = sp.sqrt((h_sub**2 + 3) / (h_sub**2 + 4))
        
        cos_arg = alpha_sub - b_sub * t**2 / 2
        cos_base = sp.series(sp.cos(cos_arg), t, 0, order).removeO()
        
        ladder_departure = sp.series(real_transformed / cos_base, t, 0, order).removeO()
        
        # 4. Extract coefficient
        print("  4. Extracting coefficient...")
        coeff_t2n = ladder_departure.coeff(t, 2 * N)
        
        c_N_expr = str(coeff_t2n)
        
        cache[key] = c_N_expr
        save_cache(cache)
        print(f"  => {key} raw t^(2*{N}) coeff: {c_N_expr}")

if __name__ == '__main__':
    main()
