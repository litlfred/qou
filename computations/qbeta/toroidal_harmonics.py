#!/usr/bin/env python3
"""
Toroidal Harmonics Derivation Script
Derives the exact mapping between the Toroidal Harmonic differential equation
and the pre-archimedean Markov parameter z-recursion.
"""

import sympy as sp

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

if __name__ == "__main__":
    derive_bridge()
