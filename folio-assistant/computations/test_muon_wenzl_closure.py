import mpmath as mp
import _path_bridge
from codata_constants import M_E_MEV, M_MU_MEV_VALIDATION  # noqa: E402
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from q_parameter import Q_50_DIGIT_STR
from witness_base import WitnessBuilder

def main():
    mp.mp.dps = 100
    q = mp.mpf(Q_50_DIGIT_STR)
    m_e = M_E_MEV
    m_mu_codata = M_MU_MEV_VALIDATION
    vol_4_1 = 2 * mp.clsin(2, mp.pi/3)
    
    m_mu_base_pred = m_e * vol_4_1 / (1 - 1/q)**2
    residual_base_ppb = (m_mu_base_pred - m_mu_codata) / m_mu_codata * 1e9
    
    def q_int(n):
        return (q**n - q**(-n)) / (q - 1/q)
    
    def q_fact(n):
        res = mp.mpf(1)
        for i in range(1, n+1):
            res *= q_int(i)
        return res

    # New hypothesis: subtract (5/2) / [8]_q!
    correction = mp.mpf('2.5') / q_fact(8)
    m_mu_new_pred = m_e * (vol_4_1 / (1 - 1/q)**2 - correction)
    
    residual_new_ppb = (m_mu_new_pred - m_mu_codata) / m_mu_codata * 1e9
    
    print(f"Base residual: {residual_base_ppb} ppb")
    print(f"New residual:  {residual_new_ppb} ppb")
    print(f"Ratio: {abs(residual_new_ppb / residual_base_ppb)}")
    
    w = WitnessBuilder("mu-wenzl-closure-probe", engine="python")
    w.set_description("Tests if 5/2 / [8]_q! closes the muon mass tension")
    w.add_data("base_residual_ppb", mp.nstr(residual_base_ppb, 10))
    w.add_data("new_residual_ppb", mp.nstr(residual_new_ppb, 10))
    w.add_assertion(name="improves_prediction", expected=True, computed=abs(residual_new_ppb) < abs(residual_base_ppb), tolerance=0)
    w.save()

if __name__ == '__main__':
    main()
