import sys
import sympy as sp
from mpmath import mp, mpf

mp.dps = 50

# We want to evaluate the interaction between 3_1 (trefoil) and 4_1 (figure-eight).
# The missing 260 ppm in c_3 is ~ -0.000260
c_3_emp = mpf('-2.021623')
vol_4_1 = 2 * mp.im(mp.polylog(2, mp.exp(mp.j * mp.pi / 3)))
u_val = mpf('0.00852')

diff = c_3_emp - (-vol_4_1 + u_val)
print(f"Missing residual to explain: {diff}")

# The colored Jones polynomial of 3_1 (trefoil) at N=2 (fundamental) or its Habiro expansion.
# The Habiro expansion of 3_1 is:
# J(3_1; q) = \sum_{n=0}^\infty q^n (1-q^n)... wait, 
# The cyclotomic expansion of 3_1 (right-handed) is:
# J(3_1) = \sum_{n=0}^\infty q^n \prod_{k=1}^n (1 - q^{1+k})(1 - q^{1-k}) ? No.
# Actually, the simplest Habiro element is [3]_q / 25, mentioned in the cheat sheet for c_3.
# Let's check what the [3]_q / 25 evaluates to.
q_0 = mpf('1.1099892')
q3_25 = (q_0**2 + 1 + 1/q_0**2) / 25 # roughly 3/25 = 0.12, not 260 ppm.

# What about the volume of 3_1? It is 0. 
# But the Chern-Simons invariant of 3_1 is pi^2 / 3.
# Maybe the interaction is related to the linking number or the crossing number.
# 3_1 has 3 crossings.
# The correction is -0.00026. Note that u^2 = (0.00852)^2 = 0.0000725.
# -3 * u^2 = -0.000217. This is VERY close to -0.00026!
print(f"-3 * u^2: {-3 * u_val**2}")
print(f"-4 * u^2: {-4 * u_val**2}")

# Could the interaction be - n_crossings * u^2?
# For 3_1, n_crossings = 3.
# Let's check the exact value of u.
q_0_exact = mpf('1.1099892') # approximate, let's derive it from m_mu/m_e
# We know m_mu/m_e = Vol(4_1) / hbar_q^2.
hbar_q_sq = vol_4_1 / mpf('206.7682830')
h_0 = mp.sqrt(hbar_q_sq)
# h_0 = q - 1/q
# (q^2 - 1)/q = h_0 => q^2 - h_0 q - 1 = 0
# q = (h_0 + sqrt(h_0^2 + 4)) / 2
q_0_real = (h_0 + mp.sqrt(h_0**2 + 4)) / 2
print(f"Exact q_0: {q_0_real}")

# re-evaluate u
alpha_0 = 1/2 * (mp.sqrt(q_0_real)/(1+q_0_real) - 1) * h_0
b = mp.sqrt((h_0**2 + 3)/(h_0**2 + 4))
u_exact = b * hbar_q_sq # wait, hbar_q is ln q or q - 1/q ?
# Let's assume u_exact = b * (q_0_real - 1)**2 / q_0_real ... wait, u = b * h_0**2 ?
# In q_beta formulas, u = b * h_0^2.
u_exact = b * h_0**2
print(f"Exact u: {u_exact}")

# re-evaluate the difference
diff_exact = c_3_emp - (-vol_4_1 + u_exact)
print(f"Exact residual: {diff_exact}")

print(f"-3 * u_exact^2: {-3 * u_exact**2}")
print(f"-4 * u_exact^2: {-4 * u_exact**2}")
print(f"ratio residual / u_exact^2: {diff_exact / u_exact**2}")
