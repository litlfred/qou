import sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import _path_bridge as _bridge

from _precision import set_compute_dps
from experimental_constants import M_E_MEV, M_P_MEV, Q_NEUTRON_MEV
from qou_substrate.constants import q_at, q_muon_at

def quantum_int(n: int, q: mp.mpf) -> mp.mpf:
    return (q ** n - q ** (-n)) / (q - q ** (-1))

def c3_habiro(q: mp.mpf) -> mp.mpf:
    hbar = (q - 1) / q
    base = -(q ** 2 + q ** (-2))
    rung1 = hbar * quantum_int(3, q) / 25
    rung2 = hbar ** 3 / quantum_int(2, q)
    return base * (1 + rung1 + rung2)

def main():
    set_compute_dps(60)
    q_p = q_at(60)
    q_m = q_muon_at(60)
    
    Q_N2 = mp.mpf("0.782334410277840137760143636388")
    Q_N3_CAL = mp.mpf("0.78233341")
    C3_TARGET = mp.mpf("-2.06934257711516783787971951725")
    
    c3_rung_factor_cal = Q_N3_CAL / Q_N2 - 1
    
    # We want Q_beta as a function of q
    # We know c3_rung_factor_cal is c_3_cal * u^3
    # So u^3 = c3_rung_factor_cal / c_3_cal
    # Since u = b * hbar_q^2, we can find u(q) if we know u(q_0).
    # Actually, u is proportional to hbar_q^2.
    # So u(q) = u(q_p) * (hbar(q)^2 / hbar(q_p)^2)
    
    hbar_p = (q_p - 1) / q_p
    u_p_cubed = c3_rung_factor_cal / C3_TARGET
    
    def Q_beta(q):
        hbar_q = (q - 1) / q
        u_q_cubed = u_p_cubed * (hbar_q / hbar_p)**6
        c3_hab = c3_habiro(q)
        return Q_N2 * (1 + c3_hab * u_q_cubed)
    
    # Target X(q) = (Q_beta(q) + m_e) / M_N_avg
    m_e = mp.mpf(repr(M_E_MEV))
    m_p = mp.mpf(repr(M_P_MEV))
    
    # Wait, M_N_avg is (m_p + m_n)/2 = m_p + (Q_beta + m_e)/2
    def X_target(q):
        qb = Q_beta(q)
        m_n = m_p + qb + m_e
        m_N_avg = (m_p + m_n) / 2
        return (m_n - m_p) / m_N_avg
        
    def X_baseline(q):
        return (q - 1)**2 * (1 - q**(-4)) / 3

    for label, q in [("q_proton", q_p), ("q_muon", q_m)]:
        xt = X_target(q)
        xb = X_baseline(q)
        print(f"\n--- {label} ---")
        print(f"X_target   = {xt}")
        print(f"X_baseline = {xb}")
        print(f"Residual   = {xt - xb}")

if __name__ == "__main__":
    main()
