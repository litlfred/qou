import sys
from pathlib import Path
import json
from mpmath import mp, mpf

import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
HERE = Path('.').resolve()
sys.path.insert(0, str(HERE))
import _path_bridge as _pb
from codata_constants import M_P_MEV_VALIDATION  # noqa: E402 (codata sweep)
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
M_p = mpf(M_P_MEV_VALIDATION)
Q_n = mpf('0.7823432')
M_n = M_p + M_e + Q_n

# Flavor split target
delta_target = (M_n - M_p) / ((M_p + M_n)/2)

# X baseline
def _x_baseline(q):
    return (q - 1)**2 * (1 - q**(-4)) / 3

x_base = _x_baseline(q0)
resid = delta_target - x_base
ratio = resid / x_base

print(f"delta_target: {delta_target}")
print(f"X_baseline:   {x_base}")
print(f"Residual:     {resid}")
print(f"Ratio (residual/X_base): {ratio}")

# H4 factors
q_fact_4 = q_fact(4, q0)
W_1111 = 1 / q_fact_4

# Sym channel: sigma^-2 = 1 - h*q^-1
# Alt channel: sigma^-2 = 1 + h*q
sym_correction = 1 - h/q0
alt_correction = 1 + h*q0

print("\n--- Testing H4 Habiro Projections ---")
print(f"W_1111 weight = {W_1111}")
print(f"h^2 = {h**2}")

# Test 1: X * (1 + h^2 / [4]_q!)
test1 = x_base * (1 + h**2 * W_1111)
print(f"Test 1 (X * (1 + h^2 * W_1111)): {test1} (diff: {delta_target - test1})")

# Test 2: X * (1 + (1 - h/q0) * W_1111)  # Sym vertex insertion
test2 = x_base * (1 + (1 - h/q0) * W_1111)
print(f"Test 2 (Sym insertion): {test2} (diff: {delta_target - test2})")

# Test 3: X * (1 + (1 + h*q0) * W_1111)  # Alt vertex insertion
test3 = x_base * (1 + (1 + h*q0) * W_1111)
print(f"Test 3 (Alt insertion): {test3} (diff: {delta_target - test3})")

# What exactly matches the residual?
exact_habiro_factor = delta_target / x_base
print(f"\nExact required Habiro factor: {exact_habiro_factor}")
print(f"Required Habiro - 1 = {exact_habiro_factor - 1}")
print(f"h^2 * W_1111 = {h**2 * W_1111}")
print(f"h^2 / [4]_q  = {h**2 / q_num(4, q0)}")
print(f"(1 - h/q0) * W_1111 = {(1 - h/q0) * W_1111}")
print(f"(1 + h*q0) * W_1111 = {(1 + h*q0) * W_1111}")

# How about h^3 / [3]! ?
print(f"h^3 * W_111 = {h**3 / q_fact(3, q0)}")

