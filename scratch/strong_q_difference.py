import sys
from pathlib import Path
sys.path.insert(0, "computations")
from binding_manybody_jet_filtration import a_D, NUCLEONS, AME_B, M_E

# We want to find w_n such that B(K) = sum_{n=2}^A m_e a_D^(n) w_n matches AME_B
# Let's see what w_n values perfectly match the binding for D, T, 4He.
# We have 3 unknowns: w_2, w_3, w_4.
# D (A=2): B = m_e a_D^(2) w_2  => w_2 = B(D) / (m_e a_D^(2))
w_2 = AME_B["D"] / (M_E * a_D(2))
print(f"w_2 required for D = {float(w_2):.4f}")

# T/3He (A=3). Let's use average of T and 3He for A=3:
B_3_avg = (AME_B["T"] + AME_B["3He"]) / 2
# B(A=3) = m_e * (a_D^(2) w_2 + a_D^(3) w_3)
B_3_residual = B_3_avg - M_E * a_D(2) * w_2
w_3 = B_3_residual / (M_E * a_D(3))
print(f"w_3 required for A=3 = {float(w_3):.4f}")

# 4He (A=4):
# B(4He) = m_e * (a_D^(2) w_2 + a_D^(3) w_3 + a_D^(4) w_4)
B_4_residual = AME_B["4He"] - M_E * (a_D(2) * w_2 + a_D(3) * w_3)
w_4 = B_4_residual / (M_E * a_D(4))
print(f"w_4 required for A=4 = {float(w_4):.4f}")

print("\nRequired weights sequence (w_n):")
print(f"w_2 = {float(w_2):.4f}")
print(f"w_3 = {float(w_3):.4f}")
print(f"w_4 = {float(w_4):.4f}")

