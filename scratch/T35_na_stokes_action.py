import sys
import sympy as sp

# We implement the standard Hecke algebra H_3(q) basis multiplication.
# Generators: s1, s2. Relations: s1^2 = h*s1 + 1, s2^2 = h*s2 + 1, s1 s2 s1 = s2 s1 s2.
# Basis:
# 0: 1
# 1: s1
# 2: s2
# 3: s1 s2
# 4: s2 s1
# 5: s1 s2 s1

def mul_s1(nf, h):
    # Multiply basis elements by s1 on the right:
    # 0 (1) * s1 = s1 (1)
    # 1 (s1) * s1 = s1^2 = h s1 + 1 = h(1) + 1(0)
    # 2 (s2) * s1 = s2 s1 (4)
    # 3 (s1 s2) * s1 = s1 s2 s1 (5)
    # 4 (s2 s1) * s1 = s2 s1^2 = s2(h s1 + 1) = h s2 s1 + s2 = h(4) + (2)
    # 5 (s1 s2 s1) * s1 = s1 s2 s1^2 = s1 s2 (h s1 + 1) = h s1 s2 s1 + s1 s2 = h(5) + (3)
    n0, n1, n2, n3, n4, n5 = nf
    return [
        n1,
        n0 + h*n1,
        n4,
        n5,
        n2 + h*n4,
        n3 + h*n5
    ]

def mul_s2(nf, h):
    # Multiply by s2 on the right:
    # 0 * s2 = s2 (2)
    # 1 * s2 = s1 s2 (3)
    # 2 * s2 = s2^2 = h s2 + 1 = h(2) + (0)
    # 3 * s2 = s1 s2^2 = s1(h s2 + 1) = h s1 s2 + s1 = h(3) + (1)
    # 4 * s2 = s2 s1 s2 = s1 s2 s1 (5)
    # 5 * s2 = s1 s2 s1 s2 = s1 s1 s2 s1 ? No, s1(s2 s1 s2) = s1(s1 s2 s1) = s1^2 s2 s1 = (h s1 + 1) s2 s1 = h s1 s2 s1 + s2 s1 = h(5) + (4)
    n0, n1, n2, n3, n4, n5 = nf
    return [
        n2,
        n3,
        n0 + h*n2,
        n1 + h*n3,
        n5,
        n4 + h*n5
    ]

def trace_H3(nf, q):
    # Standard Markov trace for H_3(q).
    # tr(1) = 1
    # tr(s1) = z
    # tr(s2) = z
    # tr(s1 s2) = z^2
    # tr(s2 s1) = z^2
    # tr(s1 s2 s1) = z^2 s1? Actually, Markov trace tr(X s_{n-1}) = z tr(X).
    # So tr(s1 s2 s1) = z tr(s1 s2) = z^3 ? 
    # Wait, tr(s1 s2 s1) = tr(s1^2 s2) ? No, tr(AB) = tr(BA).
    # tr(s1 s2 s1) = tr(s1^2 s2) = tr((h s1 + 1) s2) = h tr(s1 s2) + tr(s2) = h z^2 + z.
    h = q - 1/q
    # The normalization is tr(1) = 1.
    # What is z? z = 1 / (1 + q^2) ?
    # Usually z is the parameter for the Markov trace. In Jones polynomial, z = -(q - q^{-1}) / (q^2 - q^{-2}) ...
    # Let's check the Rosso-Jones formula.
    # For now, let's just evaluate the coefficient directly from the trace formula.
    # Actually, the user's framework (QOU) uses `tr_one = [1,1,1,1,1,1]` for the unnormalized topological trace?
    # In `fast_sympy_c_k_15.py`: `tr_one = [1, 1, 1, 1, 1, 1]`.
    return sum(nf)

def main():
    q = sp.symbols("q")
    h = q - 1/q
    t = sp.symbols("t", real=True)
    q_sub = 1/(1-t)
    
    # 3_1 knot (trefoil): (s1 s2)^2? Wait, 3_1 as a 3-braid is s1 s2 s1 s2 = (s1 s2)^2.
    # Actually, trefoil is T_{2,3} which is s1^3. But T_{3,2} is (s1 s2)^2.
    # T_{3,5} is (s1 s2)^5.
    
    # Let's compute (s1 s2)^k
    def apply_braid(k):
        nf = [1, 0, 0, 0, 0, 0]
        for _ in range(k):
            nf = mul_s1(nf, h)
            nf = mul_s2(nf, h)
        return nf

    nf_T35 = apply_braid(5)
    nf_3_1 = apply_braid(2)
    
    tr_T35 = trace_H3(nf_T35, q)
    tr_3_1 = trace_H3(nf_3_1, q)
    
    # We construct the ratio of the traces (as is done in the framework for the operator)
    # In QOU, it's usually (tr(interaction) - tr(baseline)) / counit, etc.
    # Let's look at the difference:
    dnet = sp.cancel(tr_T35 - tr_3_1)
    
    counit = h**2/2 - h  # Use the same counit as before to match the normalization
    ratio_A = sp.cancel(dnet / counit)
    
    MAX_ORDER = 4
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
    
    for N in range(1, MAX_ORDER + 1):
        coeff_raw = ladder_departure.coeff(t, 2*N)
        scale = (4*sp.sqrt(3)/3)**N
        c_k_witness = sp.expand(coeff_raw * scale)
        print(f"c_{N} = {c_k_witness}")

if __name__ == '__main__':
    main()
