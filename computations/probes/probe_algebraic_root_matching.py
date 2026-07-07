import sympy as sp
import json
from pathlib import Path

def main():
    w = sp.Symbol('w')
    q = 1 + w
    v = sp.sqrt(q)
    
    # Precision ladder variable
    b = sp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
    hbar_q = (q - 1)/q
    u_lad = b * hbar_q**2
    
    # 1. Expand u_lad in terms of w
    u_lad_w = sp.series(u_lad, w, 0, 8)
    
    # 2. We want to express w in terms of u_lad?
    # Because u_lad ~ w^2, we can only express w^2 in terms of u_lad.
    # What if the LHS has odd powers of w?
    
    # Let's expand the exact delta_tr_M
    wit_path = Path('computations/habiro/habiro-coefficients-atomic.witness.json')
    with open(wit_path) as f:
        data = json.load(f)
        
    p_data = data['results']['p (proton, A=1)']
    n_data = data['results']['n (neutron, A=1)']
    p_str = p_data['tr_M_in_q'].replace('sqrt(q)', 'v').replace('q', '(v**2)')
    n_str = n_data['tr_M_in_q'].replace('sqrt(q)', 'v').replace('q', '(v**2)')
    tr_p = sp.sympify(p_str, locals={'v':v})
    tr_n = sp.sympify(n_str, locals={'v':v})
    delta_tr = sp.simplify(tr_n - tr_p)
    
    delta_tr_w = delta_tr.subs(v, sp.sqrt(1+w)).series(w, 0, 8)
    print("delta_tr_M(w):")
    print(delta_tr_w)
    
    # Q_A (Form A) winding factor is Q_A = delta_net = q^2 - 2q - 1
    delta_net = q**2 - 2*q - 1
    delta_net_w = delta_net.series(w, 0, 8)
    print("\ndelta_net(w):")
    print(delta_net_w)
    
    # What if the Hexagon normalization is applied?
    # chi_diff = -(q^4+1)*(q^2-1)/(4q^3)
    chi_diff = -(q**4 + 1) * (q**2 - 1) / (4 * q**3)
    chi_diff_w = chi_diff.series(w, 0, 8)
    print("\nchi_diff(w):")
    print(chi_diff_w)
    
    # The F-map projects delta_tr onto the ladder:
    # Option 3 (Hexagon Hybrid): we use chi_diff as the base instead of delta_net!
    # If chi_diff is the base, then the ladder equation is:
    # delta_tr_M / chi_diff = Q_ladder = 1 + c_1 u_lad + c_2 u_lad^2 + ...
    ratio = sp.simplify(delta_tr / chi_diff)
    ratio_w = ratio.subs(v, sp.sqrt(1+w)).series(w, 0, 8)
    
    print("\nratio = delta_tr_M / chi_diff (in w):")
    print(ratio_w)
    
    # Since ratio has a leading constant 5/4, it means the base normalization is (5/4) chi_diff!
    # Let's normalize it so the constant is 1:
    normalized_ratio_w = (ratio_w / (sp.Rational(5, 4))).expand().series(w, 0, 8)
    print("\nnormalized_ratio (starts with 1):")
    print(normalized_ratio_w)
    
    print("\nu_lad(w):")
    print(u_lad_w)

if __name__ == '__main__':
    main()
