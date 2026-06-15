import sys
from pathlib import Path
import json
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import _path_bridge as _bridge

from _precision import set_compute_dps
from experimental_constants import M_E_MEV, M_P_MEV, Q_NEUTRON_MEV
from qou_substrate.constants import q_at, q_muon_at
from sympy import Symbol, sqrt, cancel, sympify

from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_symbolic

def _delta_target():
    M_e = mp.mpf(repr(M_E_MEV))
    M_p = mp.mpf(repr(M_P_MEV))
    Q_n = mp.mpf(repr(Q_NEUTRON_MEV))
    M_n = M_p + M_e + Q_n
    M_N_avg = (M_p + M_n) / 2
    return (M_n - M_p) / M_N_avg

def main():
    set_compute_dps(60)
    q_p = q_at(60)
    q_m = q_muon_at(60)
    dt = _delta_target()
    
    chi_p_data = json.loads(Path(HERE.parent, "chi-proton-h3.witness.json").read_text())
    chi_n_data = json.loads(Path(HERE.parent, "chi-neutron-h3.witness.json").read_text())
    
    q_sym = Symbol("q", positive=True)
    
    y_sym = {}
    for part in [(3,), (2,1), (1,1,1)]:
        y_sym[part] = y_lambda_wenzl_bridge_symbolic(part)
        
    chi_p = {}
    for entry in chi_p_data["results"]:
        part = tuple(entry["partition"])
        chi_p[part] = sympify(entry["chi_symbolic"], locals={"q": q_sym})
        
    chi_n = {}
    for entry in chi_n_data["results"]:
        part = tuple(entry["partition"])
        chi_n[part] = sympify(entry["chi_symbolic"], locals={"q": q_sym})
        
    delta_tr = {}
    for part in [(3,), (2,1), (1,1,1)]:
        expr = y_sym[part] * (chi_n[part] - chi_p[part])
        delta_tr[part] = cancel(expr)
        
    for label, q_val in [("q_proton", q_p), ("q_muon", q_m)]:
        print(f"\n--- {label} ---")
        vals = {}
        total = mp.mpf(0)
        for part in [(3,), (2,1), (1,1,1)]:
            v = mp.mpf(str(delta_tr[part].subs(q_sym, q_val).evalf(60)))
            vals[part] = v
            total += v
            print(f"Δtr_{part} = {v}")
            
        print(f"Total Δtr_M = {total}")
        print(f"Target Δ    = {dt}")
        print(f"Ratio       = {dt / total}")
        
        xb = (q_val - 1)**2 * (1 - q_val**(-4)) / 3
        print(f"X_baseline  = {xb}")

if __name__ == "__main__":
    main()
