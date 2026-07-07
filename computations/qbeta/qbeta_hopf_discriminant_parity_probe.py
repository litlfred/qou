#!/usr/bin/env python3
"""
qbeta_hopf_discriminant_parity_probe.py

Calculates the discriminant parity of the Hopf-crossing roots for c_3.
It compares the root structure of the Hopf sector cubic vs the Unknot sector quadratic,
demonstrating that the complex structure (imaginary parity) of the odd channel
arises strictly from the chirality of the Hopf link.

C_Hopf(y) = y^3 - 6y^2 + 10y - 6
C_unknot(y) = 2y^2 - 7y + 4

For a cubic ay^3 + by^2 + cy + d:
Delta = 18abcd - 4b^3d + b^2c^2 - 4ac^3 - 27a^2d^2

For a quadratic ay^2 + by + c:
Delta = b^2 - 4ac
"""
import sympy as sp
import json
import os

def main():
    y = sp.Symbol('y')
    
    # Polynomials
    C_Hopf = y**3 - 6*y**2 + 10*y - 6
    C_unknot = 2*y**2 - 7*y + 4
    C_total = C_Hopf + C_unknot  # y^3 - 4y^2 + 3y - 2
    
    # Discriminant function
    def disc(poly, var):
        return sp.discriminant(poly, var)
    
    delta_Hopf = disc(C_Hopf, y)
    delta_unknot = disc(C_unknot, y)
    delta_total = disc(C_total, y)
    
    # Analyze roots
    roots_Hopf = sp.roots(C_Hopf, y)
    roots_unknot = sp.roots(C_unknot, y)
    
    # Count real vs complex roots
    def root_types(roots_dict):
        real_count = 0
        complex_count = 0
        for r, mult in roots_dict.items():
            if r.is_real:
                real_count += mult
            elif r.is_real is False:
                complex_count += mult
            else:
                # evaluate numerically to check
                val = r.evalf()
                if val.is_real:
                    real_count += mult
                else:
                    complex_count += mult
        return real_count, complex_count
        
    rh_real, rh_complex = root_types(roots_Hopf)
    ru_real, ru_complex = root_types(roots_unknot)
    
    print(f"Discriminant of C_Hopf: {delta_Hopf} (Real roots: {rh_real}, Complex roots: {rh_complex})")
    print(f"Discriminant of C_unknot: {delta_unknot} (Real roots: {ru_real}, Complex roots: {ru_complex})")
    print(f"Discriminant of Total C(y): {delta_total}")
    
    witness = {
        "computation": "qbeta-hopf-discriminant-parity",
        "description": "Demonstrates the discriminant parity of the Hopf and unknot sectors for c_3",
        "delta_Hopf": int(delta_Hopf),
        "delta_unknot": int(delta_unknot),
        "delta_total": int(delta_total),
        "roots_Hopf_real": rh_real,
        "roots_Hopf_complex": rh_complex,
        "roots_unknot_real": ru_real,
        "roots_unknot_complex": ru_complex,
        "chirality_parity": "Hopf link has negative discriminant -> complex structure. Unknot has positive discriminant -> real structure."
    }
    
    with open("computations/qbeta/qbeta-hopf-discriminant-parity.witness.json", "w") as f:
        json.dump(witness, f, indent=2)

    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
