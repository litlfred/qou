import sympy as sp
import sys

def main():
    print("Testing Faddeev/Rogers modular double transformation on GS Net")
    hbar_q = sp.Symbol('hbar_q', real=True)
    
    # Categorical net augmentation departure (cosh-like)
    # GS/Q_A - 1 = 9/8 hbar_q^2 + ...
    gs_departure = (sp.Rational(9, 8) * hbar_q**2)
    
    print(f"GS Departure: {gs_departure}")
    
    # Faddeev transformation (analytic continuation / crossing the saddle)
    # hbar_q -> i * hbar_q
    transformed_departure = gs_departure.subs(hbar_q, sp.I * hbar_q)
    
    print(f"Transformed Departure: {transformed_departure}")
    
    # We expect a sign flip to match the cos-like structure (negative leading term)
    if transformed_departure.coeff(hbar_q**2) < 0:
        print("PASS: Transformation produces negative (cos-like) leading term.")
    else:
        print("FAIL: No sign flip observed.")

if __name__ == '__main__':
    main()
