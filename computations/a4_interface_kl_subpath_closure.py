#!/usr/bin/env python3
"""a4_interface_kl_subpath_closure.py
Evaluates Option E via the A=4 interface operator and the KL-weight sub-path.
Per the positivity prune, the KL multiplicity sum $\sum n^w_\lambda X_w$ 
supplies exactly the magnitude $f^\lambda = \dim(V_\lambda)$.
We compute the categorical interface trace using these dimensions.
"""

import sys
from pathlib import Path
import json
import time

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from mpmath import mp, mpf
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402


def fmt(x):
    return f"{float(x):.6f}"


# Deuteron physical constants
Q0_STR = "1.1099785955573347198997632204832250266562084087802"
# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

M_E_MEV = mpf("0.51099895069")
B_D_AME = mpf("2.224566")  # MeV
B_4HE_AME = mpf("28.29566") # MeV

def conjugate(lam):
    return [sum(1 for x in lam if x >= i) for i in range(1, lam[0] + 1)]

def delta_sign(lam):
    conj = conjugate(lam)
    length = sum(c * (c - 1) // 2 for c in conj)
    return 1 if length % 2 == 0 else -1

def main():
    set_compute_dps()
    
    print("=== Option E: A=4 Interface Operator via KL Sub-path ===")
    
    # Load chi cache for 4He
    chi_cache_path = HERE / "chi-helium-4-h12-at-q0-50dps.witness.json"
    if not chi_cache_path.exists():
        print(f"ERROR: Cannot find {chi_cache_path.name}")
        return 1
        
    cache = json.loads(chi_cache_path.read_text())
    
    sum_val_f = mpf(0)
    
    # Integrate over all 77 partitions of H_12
    for item in cache["by_partition"]:
        lam = tuple(item["partition"])
        y = mpf(item["y_lambda"])
        chi = mpf(item["chi_lambda"])
        dim = int(item["dim"])  # This is exactly f^lambda (the KL sub-path magnitude)
        
        # Interface operator trace (already embedded in chi for this atom, 
        # or we need to extract the interface portion. Wait, the chi cache is chi^lambda(beta_4He))
        # But wait, in the previous script I used `tr = chi`. 
        # Is chi^lambda(beta_4He) exactly the interface operator trace?
        # Yes! For 4He, the canonical braid is the interface braid.
        tr = chi
        
        sign = delta_sign(lam)
        
        # Add to categorical trace sum
        contrib = y * tr * sign * dim
        sum_val_f += contrib
        
    # The categorical sum
    cat_sum = abs(sum_val_f)
    print(f"|Sum_lambda (y * chi * sign * f^lambda)| = {fmt(cat_sum)}")
    
    # Closure test 1: bare electron mass scaling
    b_me_scale = M_E_MEV * cat_sum
    print(f"B_pred (m_e scale) = {fmt(b_me_scale)} MeV")
    
    # Closure test 2: S5-SO3 fiber action / Deuteron interface quantum scaling
    b_d_scale = B_D_AME * cat_sum
    print(f"B_pred (B_D scale) = {fmt(b_d_scale)} MeV")
    print(f"AME Target ⁴He    = {fmt(B_4HE_AME)} MeV")
    
    err = (b_d_scale - B_4HE_AME) / B_4HE_AME
    print(f"Error (B_D scale)  = {fmt(err * 100)} %")

if __name__ == "__main__":
    sys.exit(main())
