#!/usr/bin/env python3
import sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
# Repo root by LANDMARK SEARCH, not by counting `.parent`s: the fixed
# count was off by one and resolved OUTSIDE the repo, so this bootstrap
# never fired -- masked because `_path_bridge`/PYTHONPATH already supplies
# the same directory in every in-repo run. Bean qou-rug0.
_QOU_REPO_ROOT = next(
    (_a for _a in Path(__file__).resolve().parents
     if (_a / "tools").is_dir() and (_a / "computations").is_dir()),
    Path(__file__).resolve().parent,
)
sys.path.insert(0, str(_QOU_REPO_ROOT / "tools" / "qou-substrate" / "python"))

from qou_substrate.constants import q_at, q_muon_at

M_E_MEV = "0.51099895069"
M_P_MEV = "938.27208816"
Q_NEUTRON_MEV = "0.78233341"

def main():
    mp.mp.dps = 60
    q_p = q_at(60)
    
    M_e = mp.mpf(M_E_MEV)
    M_p = mp.mpf(M_P_MEV)
    Q_n = mp.mpf(Q_NEUTRON_MEV)
    M_n = M_p + M_e + Q_n
    M_N_avg = (M_p + M_n) / 2
    
    h_p = q_p - 1/q_p
    hbar_p = 1 - 1/q_p
    q2_p = q_p + 1/q_p
    
    X_base = (1/mp.mpf(3)) * hbar_p**2 * h_p * q2_p
    DeltaM_Xbase = X_base * M_N_avg
    
    Q_base_N2 = mp.mpf("0.782334410277840137760143636388")
    DeltaM_Qbase = Q_base_N2 + M_e
    
    print(f"DeltaM from X_baseline : {DeltaM_Xbase} MeV")
    print(f"DeltaM from Q_N2_base  : {DeltaM_Qbase} MeV")
    print(f"Diff: {DeltaM_Qbase - DeltaM_Xbase} MeV")
    print(f"Diff/DeltaM: {(DeltaM_Qbase - DeltaM_Xbase) / DeltaM_Qbase}")

if __name__ == "__main__":
    main()
