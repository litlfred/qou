import sympy as sp
import mpmath as mp

# q0 read BY NAME (bean qou-9ugp, 2026-09-04). This held the RETIRED
# self-certified pin A as a literal -- retired 2026-08-22 for the CODATA-2022
# derivation, so the value was stale AND could not follow the anchor.
#
# MIGRATED TO PROTON on the owner ruling of 2026-08-30: proton is the default,
# and the burden is on the exception. Neither exception applies here -- this
# probe makes no explicit proton-vs-muon comparison (E1), and it is not about
# the CAL-1/2/3 triple as mathematics (E2). "It has always been muon" is
# expressly not a reason. This stem is not in `ideal_muon`, so `Q_50_DIGIT_STR`
# resolves to the proton pin.
import sys as _sys_qp  # noqa: E402
from pathlib import Path as _Path_qp  # noqa: E402
for _p_qp in (_Path_qp(__file__).resolve().parent,
              _Path_qp(__file__).resolve().parent.parent,
              _Path_qp(__file__).resolve().parent.parent / 'substrate'):
    if str(_p_qp) not in _sys_qp.path:
        _sys_qp.path.insert(0, str(_p_qp))
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

def main():
    mp.mp.dps = 60
    q = Q_MP
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
