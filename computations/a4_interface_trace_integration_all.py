import sys
import re
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from mpmath import mp, mpf
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric
from rho_w_crystal_vertex_trace import standard_young_tableaux
from a_operator.a_operator_categorical import q0_mp
from codata_constants import M_E_MEV  # noqa: E402  (drain qou-7ot6-a)
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

def conjugate(lam):
    if not lam: return []
    return [sum(1 for x in lam if x >= i) for i in range(1, lam[0] + 1)]

def delta_sign(lam):
    conj = conjugate(lam)
    length = sum(c * (c - 1) // 2 for c in conj)
    return 1 if length % 2 == 0 else -1

def syt_depth(T_dict):
    return sum(r for (r, c) in T_dict.values())

def get_total_depth(lam):
    syts = standard_young_tableaux(lam)
    return sum(syt_depth(T) for T in syts)

def main():
    set_compute_dps()
    q = q0_mp(50)
    m_e = float(M_E_MEV)  # registry (was the truncated literal 0.510998950)
    
    traces = {}
    
    log_content = Path("/tmp/a4_trace.log").read_text()
    for line in log_content.splitlines():
        match = re.search(r'Total \(2,1\) trace for λ=\((.*?)\): ([\-\.0-9e]+)', line)
        if match:
            lam_str = match.group(1)
            if not lam_str.strip():
                continue
            lam = tuple(int(x.strip()) for x in lam_str.split(',') if x.strip())
            tr = mpf(match.group(2))
            traces[lam] = tr
            
    print(f"Loaded {len(traces)} traces from log.")
    
    sum_val_f = mpf(0)
    sum_val_depth = mpf(0)
    for lam, tr in traces.items():
        y = y_lambda_wenzl_bridge_numeric(lam, q)
        dim = len(standard_young_tableaux(lam))
        depth = get_total_depth(lam)
        
        sign = delta_sign(lam)
        sum_val_f += y * tr * sign * dim
        sum_val_depth += y * tr * sign * depth
        
    B_4He_f = m_e * abs(sum_val_f)
    B_4He_depth = m_e * abs(sum_val_depth)
    print(f"\nExact Upper bound B(4He) = {float(B_4He_f):.6f} MeV (using dim(V_λ))")
    print(f"Proxy B(4He) = {float(B_4He_depth):.6f} MeV (using Total Depth)")
    print(f"Target B(4He) = 28.30 MeV")

if __name__ == '__main__':
    main()
