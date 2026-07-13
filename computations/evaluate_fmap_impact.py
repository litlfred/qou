import derived_masses as dm
import math

q0 = dm._q_0()
b = math.sqrt(q0**4 + q0**2 + 1) / (q0**2 + 1)
hbar_q = (q0 - 1)/q0
u_lad = b * hbar_q**2

# Our FMap returned c_2 = -1, all others 0.
c2 = -1
ladder_factor = (1 + c2 * u_lad**2)

base_Q = float(dm.q_beta_predicted_mev())
codata_Q = 0.7823336  # Approximate CODATA

new_Q = float(base_Q * ladder_factor)

err_base = (base_Q - codata_Q)/codata_Q * 100
err_new = (new_Q - codata_Q)/codata_Q * 100

print(f"Base Q_beta: {base_Q:.6f} MeV (Error: {err_base:+.4f}%)")
print(f"New Q_beta (with FMap c_2=-1): {new_Q:.6f} MeV (Error: {err_new:+.4f}%)")
