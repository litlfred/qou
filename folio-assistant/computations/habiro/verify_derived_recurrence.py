import sympy as sp
import json

def main():
    with open("folio-assistant/computations/habiro/habiro-coefficients-atomic.witness.json") as f:
        data = json.load(f)
        
    proton = data['results']['p (proton, A=1)']
    coeffs_raw = proton['habiro_coefficients']
    
    q = sp.Symbol('check_q')
    q_nu = sp.Symbol('q_nu') # We'll see if it's a specific value or just a constant
    
    a_m = []
    for c in coeffs_raw:
        expr = sp.sympify(c['a_m'], locals={'check_q': q})
        a_m.append(expr)
        
    # The derived coefficients C_k(u) for P_{m+k}
    u = sp.Symbol('u')
    C0 = -(q - u)*(u - 1)/u**2
    C1 = (u - 1)*(q**2 - q*q_nu*u - q*u + q + 1)/(q*u**2)
    C2 = (q**2*q_nu*u**2 - q**2*q_nu*u - q**2*u + q**2 - q*u + q + 1)/(q**2*u**2)
    C3 = -1/(q**2*u**2)
    
    # The recurrence for a_n is:
    # C0(u=q^n) a_n + C1(u=q^{n-1}) a_{n-1} + C2(u=q^{n-2}) a_{n-2} + C3(u=q^{n-3}) a_{n-3} = 0
    # Let's verify for n = 3, 4, 5
    for n in range(3, len(a_m)):
        term0 = C0.subs(u, q**n) * a_m[n]
        term1 = C1.subs(u, q**(n-1)) * a_m[n-1]
        term2 = C2.subs(u, q**(n-2)) * a_m[n-2]
        term3 = C3.subs(u, q**(n-3)) * a_m[n-3]
        
        residue = sp.cancel(sp.simplify(term0 + term1 + term2 + term3))
        
        print(f"Residue for n={n}:")
        if residue == 0:
            print("  0")
        else:
            # Maybe q_nu can be solved?
            # It's a linear equation in q_nu
            print("  Non-zero.")
            # Let's solve for q_nu
            sol = sp.solve(residue, q_nu)
            print(f"  If set to 0, q_nu = {sol}")

if __name__ == "__main__":
    main()
