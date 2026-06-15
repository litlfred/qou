import sys
from pathlib import Path
import mpmath as mp

# Add repo tools to path
repo_root = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(repo_root / "tools" / "qou-substrate" / "python"))

from qou_substrate.constants import q_at, vol_4_1_at, M_P_MEV, M_N_MEV, M_E_MEV

mp.dps = 50
q0 = q_at(50)
alpha_em = mp.mpf(1) / mp.mpf('137.035999084')

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

print(f"Alpha_em = {alpha_em}")
print(f"Alpha_em / pi = {alpha_em / mp.pi}")
print(f"W_1111 = {W_1111}")
print(f"Plancherel H4 sign block (1/24) = {1/24}")

print(f"\nDelta m_np_ratio = {delta_m_np_ratio}")
print(f"W_1111 * (q0-1)  = {theoretical_base}")

# Let's check some simple electromagnetic couplings to the categorical base
print("\nEM geometric normalizations:")
print(f"Base * alpha_em        = {theoretical_base * alpha_em}")
print(f"Base * (alpha_em/pi)   = {theoretical_base * alpha_em / mp.pi}")
print(f"Base / (alpha_em/pi)   = {theoretical_base / (alpha_em / mp.pi)}")
print(f"Base / alpha_em        = {theoretical_base / alpha_em}")

print(f"Ratio (Base / Delta m) = {theoretical_base / delta_m_np_ratio}")
print(f"1 / (alpha_em / pi)    = {mp.pi / alpha_em}")

print(f"\nCould Delta m_np / m_p simply be related to Plancherel * alpha_em?")
print(f"(1/24) * alpha_em      = {(mp.mpf(1)/24) * alpha_em}")
print(f"(1/24) * alpha_em/pi   = {(mp.mpf(1)/24) * alpha_em / mp.pi}")

# Let's check classical charge squares
# Proton charge = 1. Neutron charge = 0.
# The shift is often proportional to alpha_em.
print(f"Delta m_np_ratio / alpha_em = {delta_m_np_ratio / alpha_em}")
print(f"Delta m_np_ratio / (alpha_em/pi) = {delta_m_np_ratio / (alpha_em / mp.pi)}")

# Wait, what if the shift is exactly (W_1111) * alpha_em ?
print(f"\nW_1111 * alpha_em      = {W_1111 * alpha_em}")
print(f"W_1111 * (alpha_em/pi) = {W_1111 * alpha_em / mp.pi}")

