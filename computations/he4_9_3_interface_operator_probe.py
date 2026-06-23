"""Option E PROBE 2: 4He (9,3) Interface Operator Target.

Computes the per-block A^(9,3)_{ξν}(I) interface operator for A=4,
targeting the (2,1) block of ν (S3) which corresponds to the h^4 = -3/4
coefficient of the Borromean H3(q) Markov trace (S5-SO3 fiber action).
"""
import mpmath as mp
mp.mp.dps = 60

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent / "a_operator"))

from a_operator.a_operator_categorical import q0_mp
from a_operator.a_operator_recursive import interface_blocks
from lr_coefficients import partitions_of

def run_probe():
    dps = 50
    q = q0_mp(dps)
    q_str = mp.nstr(q, dps)
    h = q - 1/q
    bridge_coef = -h / 2

    print("=== Option E PROBE 2: A=4 (9,3) Interface Operator ===", flush=True)
    print(f"Targeting ν = (2, 1) block of H_3(q) (Borromean h^4 trace coefficient)")
    print(f"Bridge generator coefficient: -h/2 = {mp.nstr(bridge_coef, 6)}")

    target_nu = (2, 1)
    
    # Compute A-operator interface blocks for 4He (λ ⊢ 12, inner=9, block=3)
    results = {}
    
    # In order to be practical, we only run on a few dominant partitions of 12
    # that are typically relevant (e.g. ones with few rows, since A=4).
    lams = [(10, 2), (11, 1), (9, 3), (8, 4), (12,), (8, 2, 1, 1)]
    for lam in lams:
        try:
            A_dict = interface_blocks(lam, 9, 3, q_str, bridge_coef, dps=dps)
            
            # Filter for ν = (2, 1)
            matching_blocks = {k: v for k, v in A_dict.items() if k[1] == target_nu}
            if matching_blocks:
                results[lam] = matching_blocks
                print(f"  λ={lam} contains {len(matching_blocks)} sub-blocks with ν=(2, 1)")
        except Exception as e:
            print(f"  λ={lam} skipped due to error: {e}")

    print("\n--- Interface Block Traces for ν = (2, 1) ---")
    for lam, blocks in results.items():
        total_trace = mp.mpf(0)
        for (xi, nu), info in blocks.items():
            A_mat = info["A"]
            # Compute trace of A
            tr_A = sum(A_mat[i, i] for i in range(A_mat.rows))
            total_trace += tr_A
            print(f"  λ={lam}, ξ={xi}: tr(A) = {mp.nstr(tr_A, 6)} (dim={A_mat.rows}x{A_mat.cols})")
        
        print(f"  => Total (2,1) trace for λ={lam}: {mp.nstr(total_trace, 6)}")

if __name__ == "__main__":
    run_probe()
