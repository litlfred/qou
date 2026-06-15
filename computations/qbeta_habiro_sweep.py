import sys
from pathlib import Path
import json
from mpmath import mp, mpf

mp.dps = 50
HERE = Path('.').resolve()
sys.path.insert(0, str(HERE))
import _path_bridge as _pb

Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
q_data = json.load(Q_PIN.open())["derived_50_digit"]
q0 = mpf(q_data["q"])

h = q0 - 1/q0

def q_num(n, q):
    return (q**n - q**(-n)) / (q - 1/q)

def q_fact(n, q):
    res = mp.mpf(1)
    for i in range(1, n+1):
        res *= q_num(i, q)
    return res

M_e = mpf('0.51099895000')
M_p = mpf('938.27208816')
Q_n = mpf('0.7823432')
M_n = M_p + M_e + Q_n
M_scale = (M_p + M_n)/2

m_e_dim = M_e / M_scale
qbeta_dim = Q_n / M_scale
x_base = (q0 - 1)**2 * (1 - q0**(-4)) / 3
x_bar = (1 - 1/q0)**2 * (q0**4 - 1) / 3

print(f"Q_beta dim   = {qbeta_dim}")
print(f"m_e dim      = {m_e_dim}")
print(f"X            = {x_base}")
print(f"X_bar        = {x_bar}")

# Evaluate Habiro elements
W2 = 1 / q_fact(2, q0)
W3 = 1 / q_fact(3, q0)
W4 = 1 / q_fact(4, q0)
W5 = 1 / q_fact(5, q0)

elements = [
    ("h", h),
    ("h^2", h**2),
    ("h^3", h**3),
    ("h^4", h**4),
    ("X", x_base),
    ("X_bar", x_bar),
    ("W2", W2),
    ("W3", W3),
    ("W4", W4),
    ("W5", W5),
]

print("\n--- Sweeping direct combinations ---")
for name, val in elements:
    ratio = qbeta_dim / val
    if 0.1 < ratio < 10:
        print(f"Q_beta / {name:5s} = {ratio}")
    ratio_e = m_e_dim / val
    if 0.1 < ratio_e < 10:
        print(f"m_e / {name:5s} = {ratio_e}")

print("\n--- Testing Q_beta vs X - m_e ---")
print(f"X - m_e = {x_base - m_e_dim}")
print(f"Ratio (Q_beta / (X - m_e)) = {qbeta_dim / (x_base - m_e_dim)}")
print(f"Ratio (Q_beta / (X_bar - m_e)) = {qbeta_dim / (x_bar - m_e_dim)}")

print("\n--- Looking for Q_beta isolated block ---")
# If Q_beta comes from a trace on the neutron-proton boundary,
# maybe it is X * W3 or something similar.
print(f"X * W3 = {x_base * W3}")
print(f"X_bar * W3 = {x_bar * W3}")
print(f"Q_beta / (X * W3) = {qbeta_dim / (x_base * W3)}")
print(f"Q_beta / (X_bar * W3) = {qbeta_dim / (x_bar * W3)}")

