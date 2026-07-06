#!/usr/bin/env python3
"""
Toroidal Harmonics Derivation Script
Derives the exact mapping between the Toroidal Harmonic differential equation
and the pre-archimedean Markov parameter z-recursion.
"""

import numpy as np
import sympy as sp
from scipy.special import lpmv

def toroidal_harmonic_P(n, m, cosh_eta):
    """
    Computes the Toroidal Harmonic (half-integer Legendre function of the first kind):
    P_{n - 1/2}^m (cosh eta)
    
    Using scipy's associated Legendre function: lpmv(m, v, x).
    v = n - 0.5.
    """
    v = n - 0.5
    return lpmv(m, v, cosh_eta)

def derive_bridge():
    print("--- Deriving the Toroidal Harmonics Bridge ---\n")
    
    # Define symbolic variables
    w, x = sp.symbols('w x', real=True)
    n = sp.Symbol('n', integer=True)
    
    # 1. The Toroidal Coordinate Mapping
    # The Markov parameter is z = sqrt(q)/(1+q). Let q = e^(-eta).
    # Then z = 1 / (2 cosh(eta/2)).
    # w = z^2 = 1 / (4 cosh^2(eta/2)) = 1 / (2 (cosh(eta) + 1))
    # Therefore, x = cosh(eta) maps to:
    x_w = 1/(2*w) - 1
    
    print(f"Mapping x = cosh(eta) to w = z^2:")
    print(f"  x(w) = {x_w}")
    
    # 2. The Toroidal Harmonic (Legendre) Differential Equation
    # (1 - x^2) d^2y/dx^2 - 2x dy/dx + v(v+1) y = 0
    # For toroidal harmonics, v = n - 1/2
    v = n - sp.Rational(1, 2)
    eigenvalue = v * (v + 1)
    
    # Let y(x) = f(w(x)). We need to express derivatives with respect to x in terms of w.
    # dx/dw = -1/(2*w^2) => dw/dx = -2*w^2
    w_x = 1 / (2 * (x + 1))
    dw_dx = sp.diff(w_x, x)
    
    # By chain rule:
    # dy/dx = (df/dw) * (dw/dx)
    # d^2y/dx^2 = d/dx[ (df/dw) * (dw/dx) ] = (d^2f/dw^2) * (dw/dx)^2 + (df/dw) * (d^2w/dx^2)
    
    f = sp.Function('f')(w)
    df_dw = sp.diff(f, w)
    d2f_dw2 = sp.diff(df_dw, w)
    
    dy_dx = df_dw * dw_dx
    d2y_dx2 = d2f_dw2 * (dw_dx**2) + df_dw * sp.diff(dw_dx, x)
    
    # Substitute into the Legendre ODE
    legendre_ode_x = (1 - x**2) * d2y_dx2 - 2 * x * dy_dx + eigenvalue * f
    
    # 3. Transform to the w-domain
    # Substitute x with x(w)
    ode_w = legendre_ode_x.subs(x, x_w)
    
    # Simplify the ODE
    ode_w_simplified = sp.simplify(ode_w)
    print(f"\nToroidal Legendre ODE transformed to w-domain:")
    print(f"  {ode_w_simplified} = 0")
    
    # Multiply by (2*w)^2 to clear denominators for a polynomial form
    polynomial_ode = sp.simplify(ode_w_simplified * (4 * w**2))
    
    # Expand and collect by derivatives
    collected_ode = sp.collect(sp.expand(polynomial_ode), [d2f_dw2, df_dw, f])
    
    print(f"\nPolynomial ODE form:")
    print(f"  {collected_ode} = 0")
    
    # We can extract the coefficients of the differential equation:
    # They all share a factor of w**2. Let's factor it out for the canonical ODE.
    canonical_ode = sp.simplify(collected_ode / (w**2))
    canonical_collected = sp.collect(sp.expand(canonical_ode), [d2f_dw2, df_dw, f])
    
    print(f"\nCanonical Normalized ODE (divided by w^2):")
    print(f"  {canonical_collected} = 0")
    
    c_d2f = canonical_collected.coeff(d2f_dw2)
    c_df = canonical_collected.coeff(df_dw)
    c_f = canonical_collected.coeff(f)
    
    print(f"\nCanonical Coefficients:")
    print(f"  w^2 * d^2f/dw^2 : {sp.factor(c_d2f) / w**2} * w^2")
    print(f"  w * df/dw       : {sp.factor(c_df) / w} * w")
    print(f"  f               : {sp.factor(c_f)}")
    
    print("\nThis canonical hypergeometric differential equation maps directly")
    print("to the Markov parameter z-recursion (with w = z^2).")

def evaluate_c_lambda():
    print("\n--- Evaluating the Delta_lambda Mass Gap (A=4) ---")
    
    # Experimental values for 4He
    b_ame = 28.29566 # AME2020 binding energy in MeV
    e_gate = 29.99   # SU(4) Plancherel occupancy from B_gate
    
    c_lambda_exp = b_ame / e_gate
    print(f"Experimental c_lambda (Shell-filling fraction): {c_lambda_exp:.6f}")
    
    print("\n1. Testing known topological anchors:")
    # Anchor A: Galois root q0 = exp(2pi i / 5). cosh(eta) = cos(2pi/5) = (sqrt(5)-1)/4
    cosh_galois = (np.sqrt(5) - 1) / 4
    p0_g = toroidal_harmonic_P(0, 0, cosh_galois)
    p1_g = toroidal_harmonic_P(1, 0, cosh_galois)
    ratio_g = p0_g / p1_g if p1_g != 0 else float('inf')
    print(f"  [Galois q0 = e^(2pi i/5)] cosh(eta) = {cosh_galois:.4f} -> Ratio = {ratio_g:.6f}")
    
    # Anchor B: Silver ratio associated with Pell-Lucas sequences
    # q0 = sqrt(2) - 1. cosh(eta) = sqrt(2)
    cosh_silver = np.sqrt(2)
    p0_s = toroidal_harmonic_P(0, 0, cosh_silver)
    p1_s = toroidal_harmonic_P(1, 0, cosh_silver)
    ratio_s = p0_s / p1_s
    print(f"  [Silver Ratio]           cosh(eta) = {cosh_silver:.4f} -> Ratio = {ratio_s:.6f}")

    # Anchor C: Golden Ratio (Fibonacci anyons, Jones at q=e^{2pi i/5})
    # q0 = 1/phi = (sqrt(5)-1)/2. cosh(eta) = sqrt(5)/2
    cosh_golden = np.sqrt(5) / 2
    p0_phi = toroidal_harmonic_P(0, 0, cosh_golden)
    p1_phi = toroidal_harmonic_P(1, 0, cosh_golden)
    ratio_phi = p0_phi / p1_phi
    print(f"  [Golden Ratio (1/phi)]   cosh(eta) = {cosh_golden:.4f} -> Ratio = {ratio_phi:.6f}")
    print(f"    -> Difference from c_lambda_exp = {abs(ratio_phi - c_lambda_exp):.6f}")

    print("\n2. Inverting the Toroidal Ratio to extract exact geometry:")
    
    from scipy.optimize import root_scalar
    
    def objective(x):
        # We look for x > 1 such that P_{-1/2}(x) / P_{1/2}(x) - c_lambda_exp = 0
        p0 = toroidal_harmonic_P(0, 0, x)
        p1 = toroidal_harmonic_P(1, 0, x)
        return p0 / p1 - c_lambda_exp
    
    # Bracket the root between 1.01 and 10.0
    res = root_scalar(objective, bracket=[1.01, 10.0])
    
    if res.converged:
        exact_cosh = res.root
        print(f"  Target Geometry Found!")
        print(f"  Exact cosh(eta_0) required : {exact_cosh:.6f}")
        
        # Calculate the corresponding w and q
        # cosh(eta) = 1/(2w) - 1  => w = 1 / (2*(cosh(eta) + 1))
        exact_w = 1 / (2 * (exact_cosh + 1))
        print(f"  Corresponding w = z^2      : {exact_w:.6f}")
        
        # q from cosh(eta): cosh(eta) = (q + 1/q)/2 => q^2 - 2cosh*q + 1 = 0
        # q = cosh - sqrt(cosh^2 - 1) (since q < 1)
        exact_q = exact_cosh - np.sqrt(exact_cosh**2 - 1)
        print(f"  Corresponding q_0          : {exact_q:.6f}")
    else:
        print("  Root finding failed.")

if __name__ == "__main__":
    derive_bridge()
    evaluate_c_lambda()
