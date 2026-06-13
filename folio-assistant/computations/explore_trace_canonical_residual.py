#!/usr/bin/env python3
import sys
import math
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from mass_table_comprehensive import try_binding_canonical, AME_BINDING
from q_parameter import Q_50_DIGIT_STR

atoms = [
    ("D", 1, 1),
    ("T", 1, 2),
    ("3He", 2, 1),
    ("4He", 2, 2)
]

q = float(Q_50_DIGIT_STR)

print(f"q_0 = {q:.6f}")
print("Exploring trace-canonical residual: Delta_lambda(K) = B_AME / B_pred ≈ q_0^(10A - 5)")
print("-" * 80)
print(f"{'Atom':>5} {'A':>2} | {'B_pred':>8} {'B_AME':>8} | {'Ratio':>8} | {'log_q(Ratio)':>12} | {'10A-5':>7} | {'Diff':>7}")
print("-" * 80)

for name, Z, N in atoms:
    A = Z + N
    r = try_binding_canonical(Z, N, Q_50_DIGIT_STR)
    if r is None or not r.get("B_pred_MeV"):
        continue
    
    b_pred = r["B_pred_MeV"]
    b_ame = AME_BINDING[name]
    
    ratio = b_ame / b_pred
    log_q_ratio = math.log(ratio) / math.log(q)
    expected_power = 10 * A - 5
    diff = log_q_ratio - expected_power
    
    print(f"{name:>5} {A:>2} | {b_pred:>8.4f} {b_ame:>8.4f} | {ratio:>8.4f} | {log_q_ratio:>12.4f} | {expected_power:>7} | {diff:>7.4f}")

print("-" * 80)
print("Note: The 'Diff' shows how close the empirical ratio's power is to the expected 10A-5.")
