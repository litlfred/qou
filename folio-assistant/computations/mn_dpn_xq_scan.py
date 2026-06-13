#!/usr/bin/env python3
import sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import _path_bridge  # noqa: E402, F401

from _precision import set_compute_dps
from q_parameter import Q_50_DIGIT_STR

def hbar(q): return (q - 1) / q
def h(q): return q - 1 / q
def quantum_int(n, q): return (q**n - q**(-n)) / (q - 1/q)

def main():
    set_compute_dps()
    m_p_codata = mp.mpf("938.27208816")
    m_n_codata = mp.mpf("939.56542052")
    alpha_em = mp.mpf("0.0072973525693")
    
    q = mp.mpf(Q_50_DIGIT_STR)
    M_N = (m_p_codata + m_n_codata) / 2
    delta_pn_target = m_n_codata - m_p_codata
    
    X_0 = hbar(q)**2 * h(q) * quantum_int(2, q) / 3
    C_target = delta_pn_target / (M_N * X_0)
    correction = C_target - 1
    
    print(f"Correction needed: {mp.nstr(correction, 15)}")
    
    bases = {}
    for i in range(1, 5):
        bases[f"hbar^{i}"] = hbar(q)**i
        bases[f"h^{i}"] = h(q)**i
        bases[f"X_0^{i}"] = X_0**i
        
    for k in list(bases.keys()):
        bases[f"{k} * alpha"] = bases[k] * alpha_em
        
    q_ints = [1, quantum_int(2, q), quantum_int(3, q), quantum_int(4, q), quantum_int(5, q)]
    
    best = []
    
    for name, base_val in bases.items():
        for num_idx, num_q in enumerate(q_ints):
            for den_idx, den_q in enumerate(q_ints):
                for rational_num in range(1, 20):
                    for rational_den in range(1, 20):
                        coeff = mp.mpf(rational_num) / mp.mpf(rational_den) * num_q / den_q
                        if coeff == 0: continue
                        
                        C_test = 1 + coeff * base_val
                        err_ppm = float(abs(C_test - C_target) / C_target * 1e6)
                        
                        C_test_minus = 1 - coeff * base_val
                        err_ppm_minus = float(abs(C_test_minus - C_target) / C_target * 1e6)
                        
                        if err_ppm < 5:
                            best.append((err_ppm, f"1 + {rational_num}/{rational_den} * [{num_idx+1}]_q / [{den_idx+1}]_q * {name}"))
                        if err_ppm_minus < 5:
                            best.append((err_ppm_minus, f"1 - {rational_num}/{rational_den} * [{num_idx+1}]_q / [{den_idx+1}]_q * {name}"))
                            
    best.sort()
    for err, expr in best[:30]:
        print(f"{err:.2f} ppm : {expr}")
        
if __name__ == "__main__":
    main()
