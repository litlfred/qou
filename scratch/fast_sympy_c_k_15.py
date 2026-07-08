import sys
import json
import sympy as sp

def main():
    q = sp.symbols("q")
    h = q - 1/q
    t = sp.symbols("t", real=True)
    q_sub = 1/(1-t)
    
    # TR_ONE = [1, 1, 1, 1, 1, 1]
    # nf_p and nf_n logic
    def hm_formal(nf, A, B, C):
        n0, n1, n2, n3, n4, n5 = nf
        return [
            A*n0 + B*n1 + C*n2,
            A*n1 + B*n0 + C*n4,
            A*n2 + B*n3 + C*n0,
            A*n3 + B*n2 + C*n5,
            A*n4 + B*n5 + C*n1,
            A*n5 + B*n4 + C*n3
        ]

    nf_p = [1, 0, 0, 0, 0, 0]
    for _ in range(2):
        nf_p = hm_formal(nf_p, 1, 0, 0)
        nf_p = hm_formal(nf_p, 1, -h, 1)
    nf_p = hm_formal(nf_p, 1, -h/2, 0)
    nf_p = hm_formal(nf_p, 1, -h/2, 0)
    nf_p = hm_formal(nf_p, 1, -h, 1)
    
    nf_n = [1, 0, 0, 0, 0, 0]
    for _ in range(3):
        nf_n = hm_formal(nf_n, 1, 0, 0)
        nf_n = hm_formal(nf_n, 1, -h, 1)
    nf_n = hm_formal(nf_n, 1, -h/2, 0)
    nf_n = hm_formal(nf_n, 1, -h/2, 0)
    nf_n = hm_formal(nf_n, 1, -h, 1)
    
    tr_one = [1, 1, 1, 1, 1, 1]
    def trace(nf):
        return sum(nf[i]*tr_one[i] for i in range(6))
        
    net_n = trace(nf_n)
    net_p = trace(nf_p)
    dnet = sp.cancel(net_n - net_p)
    
    counit = h**2/2 - h
    ratio_A = sp.cancel(dnet / counit)
    
    MAX_ORDER = 15
    ratio_t = sp.series(ratio_A.subs(q, q_sub), t, 0, 2*MAX_ORDER + 2).removeO()
    transformed_ratio = ratio_t.subs(t, sp.I * t)
    real_transformed = sp.re(sp.expand(transformed_ratio))
    
    z_sub = sp.sqrt(q_sub)/(1+q_sub)
    h_sub = q_sub - 1/q_sub
    alpha_sub = (z_sub - 1)*h_sub/2
    b_sub = sp.sqrt((h_sub**2 + 3)/(h_sub**2 + 4))
    
    cos_arg = sp.series(alpha_sub - b_sub*t**2/2, t, 0, 2*MAX_ORDER + 2).removeO()
    cos_base = sp.series(sp.cos(cos_arg), t, 0, 2*MAX_ORDER + 2).removeO()
    
    ladder_departure = sp.series(real_transformed / cos_base, t, 0, 2*MAX_ORDER + 2).removeO()
    
    cache = {}
    for N in range(1, MAX_ORDER + 1):
        coeff_raw = ladder_departure.coeff(t, 2*N)
        scale = (4*sp.sqrt(3)/3)**N
        c_k_witness = sp.expand(coeff_raw * scale)
        print(f"c_{N} = {c_k_witness}")
        cache[f"c_{N}"] = str(c_k_witness)
        
    with open("scratch/c_k_scaled_cache.json", "w") as f:
        json.dump(cache, f, indent=4)

if __name__ == '__main__':
    main()
