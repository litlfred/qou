import sys
from pathlib import Path
from mpmath import mp, mpf
import json

# Adjust path to import _li_2_q_util
sys.path.append(str(Path(__file__).parent))
from _li_2_q_util import load_q_50dps, li_2_q
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

def euler_coeff_limit(z_val: mpf, q: mpf, max_k: int = 2000, eps: mpf | None = None) -> mpf:
    if eps is None:
        eps = mpf(10) ** (5 - mp.dps)
    total = mpf(0)
    z_pow = mpf(1)
    for n in range(1, max_k + 1):
        z_pow *= z_val
        qn = q**n
        term = z_pow / (mpf(n) * (mpf(1) - qn))
        total += term
        if mp.fabs(term) < eps:
            break
    return total

def main():
    set_compute_dps()
    q, q_inv, z_anchor = load_q_50dps()
    
    # physical z_i from the doc
    z_val = mpf("0.989")
    
    s_z = euler_coeff_limit(z_val, q)
    rogers = -li_2_q(-z_val, q, q_inv)
    
    residual = s_z - rogers
    
    out = {
        "q": str(q),
        "z_val": str(z_val),
        "S_z": str(s_z),
        "rogers": str(rogers),
        "residual": str(residual),
        "fork": "A" if mp.fabs(residual) < 1e-25 else "B"
    }
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
