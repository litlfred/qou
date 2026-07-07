import sympy as sp
import json
from pathlib import Path

def main():
    w = sp.Symbol('w')
    q = 1 + w
    v = sp.sqrt(q)
    
    # Load habiro coefficients
    wit_path = Path('computations/habiro/habiro-coefficients-atomic.witness.json')
    with open(wit_path) as f:
        data = json.load(f)
        
    p_data = data['results']['p (proton, A=1)']
    n_data = data['results']['n (neutron, A=1)']
    
    # Let's use the full trace rational functions because they are exact
    p_expr_str = p_data['tr_M_in_q'].replace('sqrt(q)', 'v').replace('q', '(v**2)')
    n_expr_str = n_data['tr_M_in_q'].replace('sqrt(q)', 'v').replace('q', '(v**2)')
    
    tr_p = sp.sympify(p_expr_str, locals={'v':v})
    tr_n = sp.sympify(n_expr_str, locals={'v':v})
    delta_tr = sp.simplify(tr_n - tr_p)
    
    # chi_diff for Hexagon
    chi_diff = -(q**4 + 1) * (q**2 - 1) / (4 * q**3)
    
    # Ratio
    ratio = sp.simplify(delta_tr / chi_diff)
    
    # Expand ratio in w
    ratio_w = ratio.subs(v, sp.sqrt(1+w)).series(w, 0, 8)
    print("Ratio delta_tr / chi_diff in w:")
    print(ratio_w)
    
if __name__ == '__main__':
    main()
