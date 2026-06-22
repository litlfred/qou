import sympy as sp
import mpmath as mp

def main():
    mp.mp.dps = 60
    q = mp.mpf("1.1099785955573347198997632204832250266562084087801536866079811461")
    m_e = mp.mpf("0.51099895069")
    m_mu_codata = mp.mpf("105.6583755")
    
    vol_4_1 = 2 * mp.clsin(2, mp.pi / 3)
    hbar_q = 1 - 1/q
    m_mu_pred = m_e * vol_4_1 / (hbar_q**2)
    
    residual_mev = m_mu_pred - m_mu_codata
    residual_ppb = (residual_mev / m_mu_codata) * 1e9
    
    print(f"Residual ppb: {residual_ppb}")
    
    # We want a multiplicative factor F such that m_mu_pred * F = m_mu_codata
    F_target = m_mu_codata / m_mu_pred
    print(f"Target factor F: {F_target}")
    
    gap_factor = F_target - 1
    print(f"Target F - 1: {gap_factor}")
    
    # Let's test Wedderburn quantum dimensions
    # dim_q(3,2)
    def q_int(k):
        return (q**k - 1) / (q - 1)
    
    dim_32 = (q**5 - 1) / (q - 1)
    print(f"dim_q(3,2) = {dim_32}")
    
    # Are there any simple algebraic expressions matching the gap_factor?
    # e.g., c * (q-1)^k / dim_q
    
    for k in range(1, 10):
        val = (q - 1)**k
        print(f"(q-1)^{k} = {val}")

if __name__ == "__main__":
    main()
