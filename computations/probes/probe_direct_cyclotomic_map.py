import sympy as sp
import json
from pathlib import Path

def main():
    u = sp.Symbol('u')
    q = u**2  # since u = sqrt(q) in the witness
    
    # Load habiro coefficients
    wit_path = Path('computations/habiro/habiro-coefficients-atomic.witness.json')
    with open(wit_path) as f:
        data = json.load(f)
        
    p_data = data['results']['p (proton, A=1)']
    n_data = data['results']['n (neutron, A=1)']
    
    def eval_habiro(atom_data):
        D_u = sp.sympify(atom_data['denom_in_u'].replace('check_q', 'u'))
        total = 0
        for term in atom_data['habiro_coefficients']:
            m = term['m']
            a_m = sp.sympify(term['a_m'].replace('check_q', 'u'))
            poch = 1
            for k in range(1, m + 1):
                poch *= (1 - u**k)
            total += a_m * poch
        return sp.simplify(total / D_u)
        
    tr_M_p = eval_habiro(p_data)
    tr_M_n = eval_habiro(n_data)
    
    delta_tr = sp.simplify(tr_M_n - tr_M_p)
    
    # Form A net winding factor: delta(net) = q^2 - 2q - 1 = u^4 - 2u^2 - 1
    delta_net = u**4 - 2*u**2 - 1
    
    # The F-map ratio F(u) = delta_net / delta_tr
    F_u = sp.simplify(delta_net / delta_tr)
    
    # We want to expand F(u) around u=1 since u = sqrt(q) and q is near 1?
    # Wait, the precision ladder is in terms of u_ladder = b * hbar_q^2.
    # The ladder is Pi (1 + c_k u_ladder^k).
    # That means F is expanded in u_ladder, which is small when q -> 1.
    # So we need to map F(q) into a power series in u_ladder.
    
    b = sp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
    hbar_q = (q - 1)/q
    u_ladder = b * hbar_q**2
    
    # Let w = q - 1.
    w = sp.Symbol('w')
    
    # Expand u_ladder in w
    u_lad_w = u_ladder.subs(q, 1+w).series(w, 0, 6)
    print("u_ladder(w):", u_lad_w)
    
    # Expand F(q) in w
    F_w = F_u.subs(u, sp.sqrt(1+w)).series(w, 0, 6)
    print("\nF(w):", F_w)
    
if __name__ == '__main__':
    main()
