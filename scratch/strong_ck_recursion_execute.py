import sys
from pathlib import Path
sys.path.insert(0, "computations")
sys.path.insert(0, "computations/qbeta")
from binding_manybody_jet_filtration import a_D, AME_B, M_E
from qbeta_c_k_recursion_scaffold import CKRecursion
import mpmath as mp

mp.dps = 50
q0 = mp.mpf("1.1099793132717013149866657930777598687799017684617")
def qbracket(k):
    return (q0**k - q0**(-k)) / (q0 - 1/q0)

r_residual = qbracket(5) / qbracket(2)

print("==========================================================")
print("  Strong Sector CKRecursion: Depth-2 Kernel Evaluation")
print("==========================================================")
print(f"Base Kernel Element a_1 = r_residual = {float(r_residual):.6f}")

# Target seeds
w_2 = mp.mpf(AME_B["D"]) / (mp.mpf(M_E) * a_D(2))
B_avg_3 = (mp.mpf(AME_B["T"]) + mp.mpf(AME_B["3He"])) / 2
w_3 = (B_avg_3 - mp.mpf(M_E) * a_D(2) * w_2) / (mp.mpf(M_E) * a_D(3))

print(f"Derived seeds from lower bounds:")
print(f"  w_2 = {float(w_2):.6f}")
print(f"  w_3 = {float(w_3):.6f}")

# Apply CKRecursion engine
# w_{n+1} = a_0 * w_n + a_1 * w_{n-1}
# We test the bar-even a_0 = 1/2 prior alongside the exact topological a_1 = r_residual
a0 = mp.mpf("0.5")
a1 = r_residual

print(f"\n[Applying CKRecursion(depth=2, kernel=({float(a0):.1f}, {float(a1):.6f}))]")
engine = CKRecursion(depth=2, kernel=(a0, a1))

w_4_pred = engine.apply_recursion((w_3, w_2))
print(f"  Predicted w_4 = {float(w_4_pred):.6f}")

target_w_4 = (mp.mpf(AME_B["4He"]) - mp.mpf(M_E) * (a_D(2)*w_2 + a_D(3)*w_3)) / (mp.mpf(M_E) * a_D(4))
print(f"  Target w_4    = {float(target_w_4):.6f}")
print(f"  w_4 Error     = {float(abs(w_4_pred - target_w_4) / target_w_4)*100:.4f}%")

# Now let's calculate the predicted He4 binding
B_2 = mp.mpf(M_E) * a_D(2) * w_2
B_3 = mp.mpf(M_E) * a_D(3) * w_3
B_4_pred = mp.mpf(M_E) * a_D(4) * w_4_pred
B_He4_pred = B_2 + B_3 + B_4_pred

print("\n[Binding Closure for 4He]")
print(f"  B(4He) predicted = {float(B_He4_pred):.6f} MeV")
print(f"  B(4He) AME       = {float(AME_B['4He']):.6f} MeV")
print(f"  Absolute Error   = {(float(B_He4_pred) - float(AME_B['4He'])) * 1000:.2f} keV")

