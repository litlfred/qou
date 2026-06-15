#!/usr/bin/env python3
import sys
from pathlib import Path
import json
from mpmath import mp, mpf, mpc, pi, polylog, re, im
import itertools

mp.dps = 50

# Target definition
HERE = Path('.').resolve()
sys.path.insert(0, str(HERE))
import _path_bridge as _pb

Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
q_data = json.load(Q_PIN.open())["derived_50_digit"]
q0 = mpf(q_data["q"])

def q_int(n, q):
    return (q**n - q**(-n)) / (q - 1/q)

q9 = q_int(9, q0)
q10 = q_int(10, q0)
alpha_inv = q0 * q9 * q10 + mpf(2)/(mpf(3)*pi)
alpha = 1 / alpha_inv

h = q0 - 1/q0
q_dim_2 = q0 + 1/q0

# The O(alpha^2) Schwinger target
target = (alpha * q_dim_2) / (mpf(8)*pi) * (1 - h**2 * alpha)

print("="*72)
print("Subgoal-2 D_3 Goncharov Probe")
print(f"Target: {target}")
print("="*72)

# Candidate algebraic points:
# 1. 5th roots of unity (Bring symmetries)
z_5 = mp.exp(mpc(0,1) * 2*pi/5)
li3_z5 = polylog(3, z_5)
re_li3_z5 = re(li3_z5)
im_li3_z5 = im(li3_z5)

# 2. Golden ratio (from icosahedron/Bring tiling)
phi = (mp.sqrt(5) + 1)/2
li3_phi = polylog(3, 1/phi)
li3_phi2 = polylog(3, 1/phi**2)

# Combinations to test
candidates = {
    "Re Li3(z5)": re_li3_z5,
    "Im Li3(z5)": im_li3_z5,
    "Li3(1/phi)": li3_phi,
    "Li3(1/phi^2)": li3_phi2,
    "zeta(3)": mp.zeta(3),
    "pi^3": pi**3
}

print("Candidate values:")
for name, val in candidates.items():
    print(f"  {name:15}: {val}")
    ratio = target / val
    print(f"    ratio: {ratio}")

# Test simple rational multipliers
def test_rational(val, name):
    ratio = target / val
    # Check if ratio is close to a simple rational or pi * rational
    for denom in range(1, 200):
        num = ratio * denom
        if abs(num - mp.nint(num)) < 1e-6:
            print(f"MATCH: {name} * {mp.nint(num)}/{denom} = Target")
        
        num_pi = ratio * denom * pi
        if abs(num_pi - mp.nint(num_pi)) < 1e-6:
            print(f"MATCH: {name} * {mp.nint(num_pi)}/({denom}*pi) = Target")
            
        num_pi2 = ratio * denom * (pi**2)
        if abs(num_pi2 - mp.nint(num_pi2)) < 1e-6:
            print(f"MATCH: {name} * {mp.nint(num_pi2)}/({denom}*pi^2) = Target")

for name, val in candidates.items():
    test_rational(val, name)

