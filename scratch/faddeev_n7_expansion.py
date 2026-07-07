import sys
import os
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

def main():
    q = h4.q
    h = q - 1 / q
    
    # We want to expand in t = hbar_q = (q-1)/q
    t = sp.symbols("t", real=True)
    q_sub = 1 / (1 - t)
    
    # Evaluate categorical GS net
    print("Computing categorical GS net...")
    dnet = sp.cancel(
        h4.augmentation(h4.nucleon_nf(["u", "d", "d"]))
        - h4.augmentation(h4.nucleon_nf(["u", "u", "d"]))
    )
    counit = h**2 / 2 - h
    ratio_A = sp.cancel(dnet / counit)
    
    # Express ratio_A in terms of t
    ratio_t = sp.series(ratio_A.subs(q, q_sub), t, 0, 16).removeO()
    
    print(f"Original GS Net Q_beta^GS / Q_A: \n{sp.expand(ratio_t)}\n")
    
    # Apply Faddeev Modular Double Transformation
    # The transformation is t -> I * t (since t ~ ln(q) and Faddeev is ln(q) -> i ln(q))
    # Or specifically hbar_q -> I * hbar_q. Let's apply t -> I * t.
    transformed_ratio = sp.expand(ratio_t.subs(t, sp.I * t))
    print(f"Faddeev Transformed GS Net: \n{transformed_ratio}\n")
    
    # The ladder formula is:
    # Q_beta / Q_A = cos(alpha - b * hbar_q^2 / 2) * (1 + sum_{k>=2} c_k u^k)
    # where u = b * hbar_q^2
    # So the transformed net MUST match the real part or something?
    # Wait, the transformed net has imaginary coefficients!
    # The Rogers dilogarithm maps the Bloch group element. Usually we take the real part, or 
    # there is a specific projection.
    
    # Let's extract the real part of the transformed ratio
    real_transformed = sp.re(transformed_ratio)
    print(f"Real part of Transformed GS Net: \n{real_transformed}\n")
    
    # Now divide by the cos base to find the ladder departure
    # z = sqrt(q) / (1+q)
    z_sub = sp.sqrt(q_sub) / (1 + q_sub)
    h_sub = q_sub - 1/q_sub
    alpha_sub = (z_sub - 1) * h_sub / 2
    b_sub = sp.sqrt((h_sub**2 + 3) / (h_sub**2 + 4))
    
    cos_arg = alpha_sub - b_sub * t**2 / 2
    cos_base = sp.series(sp.cos(cos_arg), t, 0, 16).removeO()
    
    ladder_departure = sp.series(real_transformed / cos_base, t, 0, 16).removeO()
    print(f"Ladder Departure (1 + c_k u^k): \n{ladder_departure}\n")
    
    # Extract c_k
    # u = b * t^2 -> t = sqrt(u/b). So we can substitute t^2 = u/b_sub
    u = sp.symbols("u", real=True)
    # To get c_k accurately, we can evaluate the coefficients of t^(2k)
    # Because u ~ b * t^2, u^k ~ b^k * t^(2k)
    # Let's just print the Taylor series in t to see the pattern
    pass

if __name__ == '__main__':
    main()
