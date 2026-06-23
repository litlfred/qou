import sys
import time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / "a_operator"))

import mpmath as mp
mp.mp.dps = 60

from a_operator.a_operator_categorical import q0_mp
from a_operator.a_operator_recursive import interface_blocks
from lr_coefficients import partitions_of

def main():
    dps = 50
    q = q0_mp(dps)
    q_str = mp.nstr(q, dps)
    h = q - 1/q
    bridge_coef = -h / 2

    target_nu = (2, 1)
    
    print("=== A=4 (9,3) Interface Operator Trace (All 77 Partitions) ===", flush=True)
    t0 = time.perf_counter()
    
    all_lams = list(partitions_of(12))
    
    total_completed = 0
    
    for idx, lam in enumerate(all_lams):
        t_lam_start = time.perf_counter()
        print(f"[{idx+1}/{len(all_lams)}] Processing λ={lam}...", flush=True)
        try:
            A_dict = interface_blocks(lam, 9, 3, q_str, bridge_coef, dps=dps)
            
            matching_blocks = {k: v for k, v in A_dict.items() if k[1] == target_nu}
            
            total_trace = mp.mpf(0)
            for (xi, nu), info in matching_blocks.items():
                A_mat = info["A"]
                tr_A = sum(A_mat[i, i] for i in range(A_mat.rows))
                total_trace += tr_A
                
            print(f"  -> Total (2,1) trace for λ={lam}: {mp.nstr(total_trace, 6)} (time: {time.perf_counter()-t_lam_start:.2f}s)", flush=True)
            total_completed += 1
            
        except Exception as e:
            print(f"  -> ERROR on λ={lam}: {e}", flush=True)
            
        elapsed = time.perf_counter() - t0
        print(f"  [Progress: {idx+1}/{len(all_lams)} completed. Elapsed: {elapsed:.2f}s. ETA: {elapsed/(idx+1)*(len(all_lams)-idx-1):.2f}s]", flush=True)

    print(f"\nCompleted {total_completed}/{len(all_lams)} partitions in {time.perf_counter()-t0:.2f}s", flush=True)

if __name__ == '__main__':
    main()
