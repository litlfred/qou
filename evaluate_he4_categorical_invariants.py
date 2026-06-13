import sys
import math
from pathlib import Path
import json

HERE = Path('.').resolve()
sys.path.insert(0, str(HERE / 'folio-assistant' / 'computations'))
import pyhecke_native as pn
import _path_bridge as _pb
from y_lambda_wenzl_bridge import get_y_lambda_wenzl

# get q values
Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE / 'folio-assistant' / 'computations')
q_data = json.load(Q_PIN.open())["derived_50_digit"]
q0 = float(q_data["q"])
q_mu = float(q_data["q_muon"])

m_e = 0.510998950
catalan = 0.915965594177
eight_G = 8 * catalan
A = 4
B_exp = 28.29566
target_rho = B_exp / (m_e * A * eight_G)

print(f"Target rho_F = {target_rho:.6f}")

def evaluate_anchor(q_val, label):
    print(f"\n--- {label} anchor: q = {q_val} ---")
    
    # Let's test the q-dimension from Wenzl weights.
    # Wenzl weight y_lambda is related to q-dimension by dim_q = 1 / y_lambda ? No.
    # Wenzl trace of identity in block lambda is d_lambda * y_lambda
    # Or maybe we can just calculate y_lambda directly
    shapes = [(9,3), (8,4), (10,2), (4,4,4), (11,1), (12,)]
    
    try:
        y_vals = {shape: float(get_y_lambda_wenzl(list(shape), q_val)) for shape in shapes}
        
        # d_lambda (classical dimension)
        d_vals = {shape: float(pn.chi_lambda_braid(list(shape), [], q_val)) for shape in shapes}
        
        # Let's see some invariants
        for shape in shapes:
            print(f"{shape}: y_lambda = {y_vals[shape]:.6e}, d_lambda = {d_vals[shape]}")
            
        print("\nPossible rho_F ratios:")
        # Test y_lambda ratios
        print(f"y(9,3) / y(12) = {y_vals[(9,3)] / y_vals[(12,)]:.6f}")
        print(f"y(8,4) / y(12) = {y_vals[(8,4)] / y_vals[(12,)]:.6f}")
        
        # Test weighted ratios
        sum_2row_y_d = sum(y_vals[s] * d_vals[s] for s in [(12,), (11,1), (10,2), (9,3), (8,4)])
        print(f"sum(y*d) 2-row = {sum_2row_y_d:.6f}")
        
        # Test if rho_F relates to y_lambda of (9,3)
        # 1.8891 could be related to something in the Wenzl weights?
        
    except Exception as e:
        print(f"Error evaluating Wenzl: {e}")

evaluate_anchor(q0, "proton")
evaluate_anchor(q_mu, "muon")

