import sympy as sp
import json
from pathlib import Path

def main():
    w = sp.Symbol('w')
    q = 1 + w
    v = sp.sqrt(q)
    
    b = sp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
    hbar_q = (q - 1)/q
    u_lad = b * hbar_q**2
    
    wit_path = Path('../habiro/habiro-coefficients-atomic.witness.json')
    if not wit_path.exists():
        wit_path = Path('computations/habiro/habiro-coefficients-atomic.witness.json')
    with open(wit_path) as f:
        data = json.load(f)
        
    p_data = data['results']['p (proton, A=1)']
    n_data = data['results']['n (neutron, A=1)']
    tr_p = sp.sympify(p_data['tr_M_in_q'].replace('sqrt(q)', 'v').replace('q', '(v**2)'), locals={'v':v})
    tr_n = sp.sympify(n_data['tr_M_in_q'].replace('sqrt(q)', 'v').replace('q', '(v**2)'), locals={'v':v})
    delta_tr = sp.simplify(tr_n - tr_p)
    
    chi_diff = -(q**4 + 1) * (q**2 - 1) / (4 * q**3)
    ratio = sp.simplify(delta_tr / chi_diff)
    
    order = 8
    ratio_w = ratio.subs(v, sp.sqrt(1+w)).series(w, 0, order).removeO()
    normalized_ratio_w = (ratio_w / sp.Rational(5, 4)).expand()
    
    # We ignore the w^2 term to see what c2 and c3 would be forced to be by w^4 and w^6
    c2, c3 = sp.symbols('c2 c3')
    ladder = 1 + c2 * u_lad**2 + c3 * u_lad**3
    ladder_w = ladder.series(w, 0, order).removeO()
    
    diff = sp.expand(normalized_ratio_w - ladder_w)
    
    eq4 = diff.coeff(w, 4)
    eq6 = diff.coeff(w, 6)
    
    print(f"Eq w^4: {eq4} = 0")
    print(f"Eq w^6: {eq6} = 0")
    
    sol = sp.solve([eq4, eq6], (c2, c3))
    print(f"Naive solver result: {sol}")

if __name__ == '__main__':
    main()
