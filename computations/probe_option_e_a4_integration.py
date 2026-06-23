import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from mpmath import mp, mpf
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric
from rho_w_crystal_vertex_trace import standard_young_tableaux
from a_operator.a_operator_categorical import q0_mp

def main():
    mp.dps = 50
    q = q0_mp(50)
    m_e = 0.510998950
    
    traces = {
        (10, 2): 10.8018,
        (11, 1): 1.35022,
        (9, 3): 37.8062,
        (8, 4): 74.2623,
        (8, 2, 1, 1): 151.225
    }
    
    sum_val = mpf(0)
    for lam, tr in traces.items():
        y = y_lambda_wenzl_bridge_numeric(lam, q)
        
        # hook formula dimension
        dim = len(standard_young_tableaux(lam))
        
        # We don't have the exact sign, so we'll just sum the absolute magnitudes to get an upper bound
        term = y * tr * dim
        sum_val += abs(term)
        
        print(f"λ={lam}: y_λ={float(y):.4e}, tr={tr}, dim={dim}, term={float(term):.4e}")
        
    B_4He = m_e * sum_val
    print(f"\nUpper bound B(4He) = {float(B_4He):.4f} MeV (using dim(V_λ))")
    print(f"Target B(4He) ~ 28.3 MeV")

if __name__ == '__main__':
    main()
