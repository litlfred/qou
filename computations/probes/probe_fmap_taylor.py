import sympy as sp
import json
from pathlib import Path

def main():
    q = sp.Symbol('q', positive=True)
    v = sp.Symbol('v', positive=True)
    w = sp.Symbol('w')
    
    wit_path = Path('computations/habiro/habiro-coefficients-atomic.witness.json')
    with open(wit_path) as f:
        data = json.load(f)
        
    p_expr_str = data['results']['p (proton, A=1)']['tr_M_in_q']
    n_expr_str = data['results']['n (neutron, A=1)']['tr_M_in_q']
    
    # Evaluate at q = v**2 to eliminate square roots
    p_expr_str = p_expr_str.replace('sqrt(q)', 'v').replace('q', '(v**2)')
    n_expr_str = n_expr_str.replace('sqrt(q)', 'v').replace('q', '(v**2)')
    
    tr_M_p = sp.sympify(p_expr_str, locals={'v': v})
    tr_M_n = sp.sympify(n_expr_str, locals={'v': v})
    
    delta_tr = sp.simplify(tr_M_n - tr_M_p)
    
    # Form A net winding factor, substituting q = v**2
    delta_net = (v**2)**2 - 2*(v**2) - 1
    
    F_v = sp.simplify(delta_net / delta_tr)
    
    # Let w = q-1. Since q = v**2, v = sqrt(1+w). Expand in w.
    F_w = F_v.subs(v, sp.sqrt(1+w)).series(w, 0, 6)
    print("F(w) = delta_net / delta_tr_M:")
    print(F_w)

    # Let's also expand the Hexagon V_(2,1) ratio
    chi_diff = -((v**2)**4 + 1) * ((v**2)**2 - 1) / (4 * (v**2)**3)
    F_hex_v = sp.simplify(delta_net / chi_diff)
    F_hex_w = F_hex_v.subs(v, sp.sqrt(1+w)).series(w, 0, 6)
    print("\nF_hex(w) = delta_net / chi_diff_V(2,1):")
    print(F_hex_w)
    
if __name__ == '__main__':
    main()
