import sympy as sp
import sys

def main():
    q = sp.Symbol('q', positive=True)
    # Define exact forms for chi_lambda from Lean theorems
    chi_3 = -(q**2 - 1) * (q**2 + 1)**2 / (4 * q)
    chi_21 = (q**2 - 1) * (-q**4 - 1) / (4 * q**3)
    chi_111 = -(q**2 - 1) * (q**2 + 1)**2 / (4 * q**5)

    # Define the canonical Wenzl-Markov weights y_lambda
    # The actual weights involve the Markov parameter z(q) = sqrt(q)/(1+q)
    # Using the surrogate for now just to test the expansion algebra
    y_3_surr = q**2 / ((1 + q) * (1 + q + q**2))
    y_21_surr = q / ((1 + q) * (1 + q + q**2))
    y_111_surr = 1 / ((1 + q) * (1 + q + q**2))

    delta_tau_surr = sp.simplify(y_3_surr * chi_3 + y_21_surr * chi_21 + y_111_surr * chi_111)
    
    print("Surrogate Delta tau_M:", delta_tau_surr)
    
    # Try to express this in terms of u = b * hbar_q^2
    # First, let's look at the actual expansion of surrogate in w = q - 1
    w = sp.Symbol('w')
    delta_tau_surr_w = delta_tau_surr.subs(q, 1 + w).series(w, 0, 6)
    print("Taylor in w:", delta_tau_surr_w)
    
    # Let's see if we can substitute u
    b = sp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
    hbar_q = (q - 1)/q
    u = b * hbar_q**2
    u_w = u.subs(q, 1 + w).series(w, 0, 6)
    print("u in terms of w:", u_w)

if __name__ == '__main__':
    main()
