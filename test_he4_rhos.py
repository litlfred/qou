import math

q0 = 1.1099785955541805
m_e = 0.510998950
catalan = 0.915965594177
eight_G = 8 * catalan
A = 4
B_exp = 28.29566

target_rho = B_exp / (m_e * A * eight_G)
print(f"Target rho_F = {target_rho:.6f}")

print(f"3 - q0 = {3 - q0:.6f}")
print(f"2 / q0 = {2 / q0:.6f}")
print(f"[2]_q / q0 = {(q0 + 1/q0) / q0:.6f}")
print(f"[2]_q * (1 - (q0-1)/q0) = {(q0 + 1/q0) * (1/q0):.6f}")

print(f"q0^(1/2) + q0^(-1/2) = {math.sqrt(q0) + 1/math.sqrt(q0):.6f}")

print(f"1.8891... Let's look for q0-based forms:")
h = q0 - 1/q0
print(f"2 - h = {2 - h:.6f}")
print(f"2 - h/2 = {2 - h/2:.6f}")
print(f"2 / (1+h) = {2 / (1+h):.6f}")

hbar_q = (q0 - 1)/q0
print(f"2 - hbar_q = {2 - hbar_q:.6f}")
print(f"2 * (1 - hbar_q) = {2 * (1 - hbar_q):.6f}")

# Wait, if rho_F is a trace or categorical invariant
# Could it be [2]_{q^(1/2)} * something?
