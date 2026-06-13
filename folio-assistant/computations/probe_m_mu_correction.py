import mpmath as mp
import _path_bridge
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from q_parameter import Q_50_DIGIT_STR

def main():
    mp.mp.dps = 50
    q = mp.mpf(Q_50_DIGIT_STR)
    
    # 1. Quantum integers
    print("q =", q)
    def q_int(n):
        return (q**n - q**(-n)) / (q - 1/q)
    
    def q_fact(n):
        res = mp.mpf(1)
        for i in range(1, n+1):
            res *= q_int(i)
        return res
    
    m_e = mp.mpf('0.51099895069')
    m_mu_codata = mp.mpf('105.6583755')
    vol_4_1 = 2 * mp.clsin(2, mp.pi/3)
    m_mu_pred = m_e * vol_4_1 / (1 - 1/q)**2
    additive_gap = (m_mu_codata - m_mu_pred) / m_e
    
    print(f"\nAdditive gap (m_mu_codata/m_e - m_mu_pred/m_e): {additive_gap}")
    
    alpha_inv = mp.mpf('137.035999084')
    alpha = 1 / alpha_inv
    bring = (3*q**2 - 1) / (2*q**2)
    
    combinations3 = [
        ("-[8]_q! * 5/2", -(5/2) / q_fact(8)),
        ("-[8]_q! * linking_weight", -bring / q_fact(8)),  # wait, linking_weight is not bring
        ("-[8]_q! * (5/2 + 3/4 h^2)", -((5/2) + (3/4)*(q - 1/q)**2) / q_fact(8)),
        ("-[7]_q! * something", -1/q_fact(7)),
        ("-(1/[4]_q!)^3", -(1/q_fact(4))**3),
        ("-(1/[4]_q!) * alpha", -(1/q_fact(4)) * alpha),
    ]
    
    print("\nAdditive gap Wenzl Combinations:")
    for name, val in combinations3:
        print(f"{name}: {val}")
        print(f"  Ratio to gap: {val/additive_gap}")

        
if __name__ == '__main__':
    main()
