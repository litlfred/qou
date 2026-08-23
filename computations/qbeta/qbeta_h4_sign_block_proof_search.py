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

from qou_substrate.constants import q_at, vol_4_1_at, MASS_RATIO_P_E_STR, MASS_RATIO_MU_E_STR, M_P_MEV, M_N_MEV, M_E_MEV

# `mp` is the mpmath MODULE here, so a bare `mp.dps = ...` sets a stray
# attribute and leaves the working context at the default 15. Precision
# lives on the context: `mp.mp.dps`.
mp.mp.dps = 50
q0 = q_at(50)
vol_4_1 = vol_4_1_at(50)

def q_num(n, q):
    return (q**n - q**(-n)) / (q - 1/q)

def q_fact(n, q):
    res = mp.mpf(1)
    for i in range(1, n+1):
        res *= q_num(i, q)
    return res

# The raw components
q_dim_4_fact = q_fact(4, q0)
W_1111 = mp.mpf(1) / q_dim_4_fact
w_term = (q0 - 1)
theoretical_base = W_1111 * w_term

delta_m_np_ratio = mp.mpf(M_N_MEV - M_P_MEV) / mp.mpf(M_P_MEV)

ratio = theoretical_base / delta_m_np_ratio

print(f"Target Ratio (Theoretical Base / Experimental Shift) = {ratio}")

# Let's use PSLQ to find an integer relation between log(ratio) and logs of basis constants
# This is equivalent to finding a multiplicative relation: Ratio = C1^a * C2^b * ...
# Basis constants:
basis_vals = [
    ratio,
    mp.pi,
    vol_4_1,
    q0,
    mp.sqrt(q0),
    q0 - 1/q0,       # HA
    1 - 1/q0,        # hbar_q
    mp.sqrt(mp.mpf(2)),
    mp.sqrt(mp.mpf(3)),
    q_num(2, q0),
    q_num(3, q0),
    q_num(4, q0)
]

basis_names = [
    "Ratio", "pi", "Vol(4_1)", "q", "sqrt(q)", "HA", "hbar_q", 
    "sqrt(2)", "sqrt(3)", "[2]_q", "[3]_q", "[4]_q"
]

print("Running Multiplicative PSLQ search...")
logs = [mp.log(abs(v)) for v in basis_vals]
# PSLQ finds integer relations: a0*L0 + a1*L1 + ... = 0
# So a0*log(Ratio) + a1*log(C1) + ... = 0
# Which means Ratio = C1^(-a1/a0) * C2^(-a2/a0) ...

try:
    rel = mp.pslq(logs, tol=1e-15, maxcoeff=100)
    if rel:
        print("Found relation!")
        print(f"Relation coefficients: {rel}")
        a0 = rel[0]
        if a0 != 0:
            print(f"Ratio = ", end="")
            for i in range(1, len(rel)):
                if rel[i] != 0:
                    power = -rel[i] / a0
                    print(f"({basis_names[i]})^{power} * ", end="")
            print()
    else:
        print("No simple multiplicative relation found via PSLQ at 1e-15.")
except Exception as e:
    print(f"PSLQ error: {e}")

# Let's also check additive PSLQ
print("\nRunning Additive PSLQ search...")
try:
    rel2 = mp.pslq(basis_vals, tol=1e-15, maxcoeff=100)
    if rel2:
        print("Found relation!")
        print(f"Relation coefficients: {rel2}")
        a0 = rel2[0]
        if a0 != 0:
            print(f"Ratio = ", end="")
            for i in range(1, len(rel2)):
                if rel2[i] != 0:
                    print(f"{-rel2[i]/a0} * {basis_names[i]} + ", end="")
            print()
    else:
        print("No simple additive relation found via PSLQ at 1e-15.")
except Exception as e:
    print(f"PSLQ error: {e}")

# Check specific suspected geometric normalizations:
print("\nSpecific geometric candidates:")
print(f"1 / pi      = {1/mp.pi}")
print(f"Ratio       = {ratio}")
print(f"Ratio * pi  = {ratio * mp.pi}")
print(f"Ratio / Vol = {ratio / vol_4_1}")
print(f"Ratio / [2]_q = {ratio / q_num(2, q0)}")
print(f"Ratio / [3]_q = {ratio / q_num(3, q0)}")

