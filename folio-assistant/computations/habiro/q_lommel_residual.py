import sympy as sp
import json

def main():
    with open("folio-assistant/computations/habiro/habiro-coefficients-atomic.witness.json") as f:
        data = json.load(f)
        
    proton = data['results']['p (proton, A=1)']
    coeffs_raw = proton['habiro_coefficients']
    
    q = sp.Symbol('check_q')
    
    a_m = []
    for c in coeffs_raw:
        expr = sp.sympify(c['a_m'], locals={'check_q': q})
        a_m.append(expr)
        
    # q-Bessel contiguity relation (q-Lommel recurrence):
    # J_{m+2} - (x + q^{m+2}) J_{m+1} + q^{m+1} J_m = 0
    # Let's apply this operator to a_m:
    # R_m = a_{m+2} - (x + q^{m+2}) a_{m+1} + q^{m+1} a_m
    
    x = sp.Symbol('x')
    
    R = []
    for m in range(len(a_m) - 2):
        res = a_m[m+2] - (x + q**(m+2)) * a_m[m+1] + q**(m+1) * a_m[m]
        R.append(sp.simplify(res))
        
    print("Residuals R_m(x):")
    for m, r in enumerate(R):
        print(f"R_{m}: {r}")
        
    # Solve for x using R_0 = 0
    x_sol = sp.solve(R[0], x)
    if x_sol:
        x_val = x_sol[0]
        print(f"\nIf R_0 = 0, x = {x_val}")
        
        # Evaluate R_1, R_2, ... with this x
        print("\nEvaluating residuals with x_val:")
        for m in range(1, len(R)):
            r_eval = sp.simplify(R[m].subs(x, x_val))
            print(f"R_{m}(x_val) = {r_eval}")
            
if __name__ == "__main__":
    main()
