import math
from _codata_constants import AME_B_DEUTERON_MEV_VALIDATION, M_E_MEV
from q_parameter import Q as q0
from knot_volumes import VOL_BORROMEAN

# Target
target = AME_B_DEUTERON_MEV_VALIDATION

# Known Constants
me = float(M_E_MEV)
q0 = float(q0)
E0 = me / (q0 * (q0 - 1.0))
g8 = float(VOL_BORROMEAN)
quaternion_quantum = 2.277455
kashiwara = 1.0 / 32.0

print(f"Target: {target}")
print(f"E0: {E0}")
print(f"me: {me}")
print(f"q0: {q0}")
print(f"g8: {g8}")
print(f"quaternion_quantum: {quaternion_quantum}")
print(f"kashiwara: {kashiwara}")

print("\n--- Testing combinations ---")
# Let's test combinations of E0, me, g8, quaternion_quantum, kashiwara
# Form: A * B * C
scales = [("E0", E0), ("me", me), ("g8", g8), ("1", 1.0)]
for name, scale in scales:
    val = quaternion_quantum * scale
    print(f"quaternion_quantum * {name} = {val} (error: {val/target - 1:.4f})")
    
    val2 = quaternion_quantum * kashiwara * scale
    print(f"quaternion_quantum * kashiwara * {name} = {val2} (error: {val2/target - 1:.4f})")
    
    val3 = (quaternion_quantum - kashiwara) * scale
    print(f"(quaternion_quantum - kashiwara) * {name} = {val3} (error: {val3/target - 1:.4f})")

    val4 = quaternion_quantum * (1 - kashiwara) * scale
    print(f"quaternion_quantum * (1 - kashiwara) * {name} = {val4} (error: {val4/target - 1:.4f})")

    val5 = scale / (quaternion_quantum * kashiwara)
    print(f"{name} / (quaternion_quantum * kashiwara) = {val5} (error: {val5/target - 1:.4f})")
    
    val6 = quaternion_quantum * scale / kashiwara
    print(f"quaternion_quantum * {name} / kashiwara = {val6} (error: {val6/target - 1:.4f})")
