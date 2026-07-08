import sys
from pathlib import Path
sys.path.insert(0, "computations")
from binding_manybody_jet_filtration import a_D, AME_B, M_E
import mpmath as mp

mp.dps = 50
q0 = mp.mpf("1.1099793132717013149866657930777598687799017684617")
def qbracket(k):
    return (q0**k - q0**(-k)) / (q0 - 1/q0)
r_residual = qbracket(5) / qbracket(2)

# B_2 is exactly B(D)
B_2 = mp.mpf(AME_B["D"])
# B_3 is the additional binding from A=2 to A=3 (avg)
B_avg_3 = (AME_B["T"] + AME_B["3He"]) / 2
B_3 = mp.mpf(B_avg_3) - B_2
# B_4 is the additional binding from A=3 to A=4
B_4 = mp.mpf(AME_B["4He"]) - (B_2 + B_3)

print(f"B_2 = {B_2}")
print(f"B_3 = {B_3}")
print(f"B_4 = {B_4}")

# Test depth-2 relation: B_4 = a0 * B_3 + a1 * B_2
a1 = r_residual
a0 = (B_4 - a1 * B_2) / B_3
print(f"If a1 = r_residual ({a1}), a0 = {a0}")

a1_limit = mp.mpf("2.5")
a0_limit = (B_4 - a1_limit * B_2) / B_3
print(f"If a1 = 2.5, a0 = {a0_limit}")

