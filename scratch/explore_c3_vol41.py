import os
import sys
from mpmath import mp, mpf

mp.dps = 50

# The empirical value for c_3 at Q_beta
# Extracted from probe_q_beta_operator_valued_N3.py and c3_hopf_habiro_analysis.py
c_3_emp = mpf('-2.021623') # Approximate value, let me compute it more precisely if possible

# But I know the exact constants. Let's load the QOU constants if we can, or just use mpmath.
# The volume of 4_1 is exactly 2 * Im(Li_2(e^{i \pi / 3}))
# Let's compute Vol(4_1)
pi3 = mp.pi / 3
z = mp.exp(mp.j * pi3)
vol_4_1 = 2 * mp.im(mp.polylog(2, z))

print(f"Vol(4_1): {vol_4_1}")
print(f"-Vol(4_1): {-vol_4_1}")
print(f"c_3_emp (approx): {c_3_emp}")

diff = c_3_emp - (-vol_4_1)
print(f"Difference: {diff}")

# Also let's check the ratio
ratio = c_3_emp / (-vol_4_1)
print(f"Ratio: {ratio}")

# Let's see if this difference is related to some small parameter like h or u
# The substrate u is ~0.00852
# Wait! diff is 0.00826. That is very close to u!
# Let's check u. u = b * hbar_q^2.
q_0 = mpf('1.1099892') # Approximate q_0
h_0 = q_0 - 1/q_0
alpha_0 = 1/2 * (mp.sqrt(q_0)/(1+q_0) - 1) * h_0
b = mp.sqrt((h_0**2 + 3)/(h_0**2 + 4))
u = b * (q_0 - 1)**2 / q_0 # wait, hbar_q is ln(q)? No, the registry says u = b * hbar_q^2. In q_beta_predicted.py, u = b * hbar_q^2 where hbar_q = q - 1 ? No, hbar_q = q - 1/q is h.
# Let's just output the numbers.
