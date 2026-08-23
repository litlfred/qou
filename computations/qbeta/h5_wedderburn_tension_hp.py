import sys
from pathlib import Path

# Add repo tools to path
# Repo root by LANDMARK SEARCH, not by counting `.parent`s: the fixed
# count was off by one and resolved OUTSIDE the repo, so this bootstrap
# never fired -- masked because `_path_bridge`/PYTHONPATH already supplies
# the same directory in every in-repo run. Bean qou-rug0.
repo_root = next(
    (_a for _a in Path(__file__).resolve().parents
     if (_a / "tools").is_dir() and (_a / "computations").is_dir()),
    Path(__file__).resolve().parent,
)
sys.path.insert(0, str(repo_root / "tools" / "qou-substrate" / "python"))

import mpmath as mp
from qou_substrate.constants import q_at, vol_4_1_at, MASS_RATIO_P_E_STR, MASS_RATIO_MU_E_STR

# `mp` is the mpmath MODULE here, so a bare `mp.dps = ...` sets a stray
# attribute and leaves the working context at the default 15. Precision
# lives on the context: `mp.mp.dps`.
mp.mp.dps = 50

# Substrate parameters
q0 = q_at(50)
vol = vol_4_1_at(50)

# 1. Evaluate the base mass formula for muon
hbar_q = 1 - 1/q0
hbar_q_sq = hbar_q**2
m_mu_pred_bare = vol / hbar_q_sq
m_mu_true = mp.mpf(MASS_RATIO_MU_E_STR)

tension_ratio = m_mu_true / m_mu_pred_bare
print(f"Bare prediction: m_mu/m_e = {m_mu_pred_bare}")
print(f"CODATA 2022:     m_mu/m_e = {m_mu_true}")
print(f"Ratio (True/Bare) = {tension_ratio}")
print(f"Tension (ppb)     = {(tension_ratio - 1) * 10**9}")

def q_num(n, q):
    return (q**n - q**(-n)) / (q - 1/q)

def q_fact(n, q):
    res = mp.mpf(1)
    for i in range(1, n+1):
        res *= q_num(i, q)
    return res

# 2. H_5(q) Trace components
q_dim_5_fact = q_fact(5, q0)
print(f"\n[5]_q! = {q_dim_5_fact}")

d_311 = q_num(4, q0) * q_num(3, q0) / q_num(2, q0)
d_32 = q_num(5, q0)

print(f"d_q(3,1,1) = {d_311}")
print(f"d_q(3,2)   = {d_32}")

w_311 = d_311 / q_dim_5_fact
w_32 = d_32 / q_dim_5_fact

print(f"W_{(3,1,1)} = {w_311}")
print(f"W_{(3,2)}   = {w_32}")

# Let's explore the tension ratio in terms of H_5(q) Wenzl weights
# Tension ratio is ~ 1.0000002127...
print(f"\nTension off 1: {tension_ratio - 1}")

# Any natural relations?
print(f"(q0 - 1)^7 = {(q0 - 1)**7}")
print(f"q0*(q0 - 1)^7 = {q0 * (q0 - 1)**7}")

# Are there any simple functions of w_32 and w_311 matching this?
print(f"w_311 - w_32 = {w_311 - w_32}")
print(f"(w_311 - w_32)^3 = {(w_311 - w_32)**3}")

