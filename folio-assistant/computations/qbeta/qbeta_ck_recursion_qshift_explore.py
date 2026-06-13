import sympy as sp

def main():
    q, u, S = sp.symbols('q u S')
    # c_k coefficients
    c3, c4, c5, c6 = sp.symbols('c3 c4 c5 c6')
    
    # Ladder up to O(u^6)
    ladder_u = (1 + c3*u**3) * (1 + c4*u**4) * (1 + c5*u**5) * (1 + c6*u**6)
    ladder_qu = (1 + c3*(q*u)**3) * (1 + c4*(q*u)**4) * (1 + c5*(q*u)**5) * (1 + c6*(q*u)**6)
    
    # Ratio F(qu)/F(u)
    kappa = (q-1)**3 * (q+1) / q**2
    
    # F(qu)/F(u) - 1
    ratio = sp.series(ladder_qu / ladder_u - 1, u, 0, 7)
    print("F(qu)/F(u) - 1 series expansion:")
    sp.pprint(ratio)
    
    print("\nIf t = S * u^3:")
    # Leading term is u^3: c3*(q^3 - 1)*u^3
    # We want this to match -kappa * S * u^3
    c3_sol = sp.solve(c3*(q**3 - 1) - (-kappa * S), c3)[0]
    print(f"c3 = {sp.simplify(c3_sol)}")
    
    print("\nLet's find c4, c5 by setting higher order terms to zero:")
    coeff4 = ratio.coeff(u, 4)
    coeff5 = ratio.coeff(u, 5)
    coeff6 = ratio.coeff(u, 6)
    
    c4_sol = sp.solve(coeff4, c4)[0]
    print(f"c4 = {sp.simplify(c4_sol.subs(c3, c3_sol))}")
    
    c5_sol = sp.solve(coeff5, c5)[0]
    print(f"c5 = {sp.simplify(c5_sol.subs({c4: c4_sol, c3: c3_sol}))}")
    
    c6_sol = sp.solve(coeff6, c6)[0]
    print(f"c6 = {sp.simplify(c6_sol.subs({c5: c5_sol, c4: c4_sol, c3: c3_sol}))}")

if __name__ == "__main__":
    main()
