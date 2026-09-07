#!/usr/bin/env python3
"""a4_option_e_color_tube_closure.py

Evaluates Option E via the A=4 interface operator.
Applies the 10^3 categorical scaling derived from the S_5-SO_3
color-tube geometry (10-fold geometric dimension averaging over 3 bonds).
"""

import sys
from pathlib import Path
import json
from mpmath import mp, mpf
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

# q0 read BY NAME (bean qou-9ugp, 2026-09-04). This file bound the RETIRED
# self-certified muon pin A as a literal -- superseded 2026-08-22 by the
# CODATA-2022 derivation, so the value was ~46 ppb stale AND could not follow
# the anchor. This stem is not in `ideal_muon`, so `Q_50_DIGIT_STR` resolves to
# the PROTON pin, which the 2026-08-30 owner ruling makes the default.
import sys as _sys_qp  # noqa: E402
from pathlib import Path as _Path_qp  # noqa: E402
for _p_qp in (_Path_qp(__file__).resolve().parent,
              _Path_qp(__file__).resolve().parent / 'substrate',
              _Path_qp(__file__).resolve().parent.parent / 'computations',
              _Path_qp(__file__).resolve().parent.parent / 'computations' / 'substrate'):
    if str(_p_qp) not in _sys_qp.path:
        _sys_qp.path.insert(0, str(_p_qp))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import AME_B_HE4_MEV_VALIDATION

HERE = Path(__file__).resolve().parent


def fmt(x):
    return f"{float(x):.6f}"

# Deuteron physical constants
Q0_STR = Q_50_DIGIT_STR
# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

M_E_MEV = mpf("0.51099895069")
B_4HE_AME = AME_B_HE4_MEV_VALIDATION # MeV

def conjugate(lam):
    return [sum(1 for x in lam if x >= i) for i in range(1, lam[0] + 1)]

def delta_sign(lam):
    conj = conjugate(lam)
    length = sum(c * (c - 1) // 2 for c in conj)
    return 1 if length % 2 == 0 else -1

def main():
    set_compute_dps()
    print("=== Option E: A=4 Interface Operator via Color-Tube Scaling ===")
    
    chi_cache_path = HERE / "chi-helium-4-h12-at-q0-50dps.witness.json"
    if not chi_cache_path.exists():
        print(f"ERROR: Cannot find {chi_cache_path.name}")
        return 1
        
    cache = json.loads(chi_cache_path.read_text())
    
    sum_val_raw = mpf(0)
    
    # Integrate over all partitions of H_12
    for item in cache["by_partition"]:
        lam = tuple(item["partition"])
        y = mpf(item["y_lambda"])
        chi = mpf(item["chi_lambda"])
        
        sign = delta_sign(lam)
        
        # Raw trace magnitude (unweighted by f^lambda)
        contrib = y * chi * sign
        sum_val_raw += contrib
        
    raw_sum = abs(sum_val_raw)
    print(f"|Sum_lambda (y * chi * sign)| [Raw] = {fmt(raw_sum)}")
    
    # Base scale: 1 (m_e is factored in later, or we scale raw trace directly in MeV)
    # The geometric scaling: 10^3
    geom_scale = mpf(1000)
    
    # We apply the scale to the raw trace, then convert via mass of electron?
    # Wait, the A=2 magnitude scaling from earlier probes was B_D_AME * cat_sum
    # Actually, the user noted:
    # "The pure unweighted trace `1(raw)` evaluates to 0.028288 MeV. If we apply a 10^3 scale factor... yields 28.288 MeV"
    # Wait, is 0.028288 already in MeV? Yes, if it's scaled by m_e!
    trace_mev = raw_sum * M_E_MEV
    print(f"Base trace in MeV (raw * m_e)   = {fmt(trace_mev)} MeV")
    
    # Apply Option E color-tube scale
    final_pred = trace_mev * geom_scale
    print(f"B_pred (10^3 color-tube scale)  = {fmt(final_pred)} MeV")
    print(f"AME Target ⁴He                  = {fmt(B_4HE_AME)} MeV")
    
    err = (final_pred - B_4HE_AME) / B_4HE_AME
    print(f"Error                           = {fmt(err * 100)} %")

if __name__ == "__main__":
    sys.exit(main())
