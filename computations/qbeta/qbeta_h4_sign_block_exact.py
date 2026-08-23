import sys
from pathlib import Path
import mpmath as mp

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

from qou_substrate.constants import q_at, MASS_RATIO_P_E_STR, MASS_RATIO_MU_E_STR, M_P_MEV, M_N_MEV, M_E_MEV

# `mp` is the mpmath MODULE here, so a bare `mp.dps = ...` sets a stray
# attribute and leaves the working context at the default 15. Precision
# lives on the context: `mp.mp.dps`.
mp.mp.dps = 50
q0 = q_at(50)

def q_num(n, q):
    return (q**n - q**(-n)) / (q - 1/q)

def q_fact(n, q):
    res = mp.mpf(1)
    for i in range(1, n+1):
        res *= q_num(i, q)
    return res

# 1. Delta tr_M(q) from the Habiro Ladder Bridge
# Δtr_M(q) = (−2q^{9/2} + 4q^{5/2} − 2√q − q⁵ − q⁴ − 2q³ + 2q² + q + 1) / [4q²(q+1)]
def delta_tr_M(q):
    sqrt_q = mp.sqrt(q)
    num = (-2 * sqrt_q**9 + 4 * sqrt_q**5 - 2 * sqrt_q 
           - q**5 - q**4 - 2 * q**3 + 2 * q**2 + q + 1)
    den = 4 * q**2 * (q + 1)
    return num / den

delta_trace = delta_tr_M(q0)

# 2. H_4(q) Sign Block (1,1,1,1) Weight
# The quantum dimension of (1^4) is 1. The Wenzl weight is 1 / [4]_q!
q_dim_4_fact = q_fact(4, q0)
W_1111 = mp.mpf(1) / q_dim_4_fact

print(f"--- Q_beta Shift / H_4(q) Sign Block Exact Subtraction ---")
print(f"q0 (anchor)      = {q0}")
print(f"Delta tr_M(q0)   = {delta_trace}")
print(f"W_(1,1,1,1)      = {W_1111}")

# 3. Ratio / Categorical Relationship
print(f"\nRatio (Delta tr_M / W_1111) = {delta_trace / W_1111}")

# 4. Experimental mass split Delta m_np / m_p
delta_m_np_ratio = (M_N_MEV - M_P_MEV) / M_P_MEV
print(f"\nExperimental Delta m_np / m_p = {delta_m_np_ratio}")

# Let's check how the exact subtraction compares to the Q_beta tension (1 ppq)
# Evaluate the exact expressions
w_term = (q0 - 1)
print(f"(q0 - 1) = {w_term}")
print(f"W_1111 * (q0 - 1) = {W_1111 * w_term}")
