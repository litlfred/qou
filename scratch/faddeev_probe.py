import sympy as sp
from mpmath import mp, mpf, cos, sin, sqrt, log

mp.dps = 100

from qbeta_utils import substrate_ladder_quantities, c3_target_at

Q_PROTON = mpf("1.1099785827513808075916690956107688798744991218736")
Q_CODATA_MEV = mpf("0.782333583274213580521634562479207") # approximate value used previously
M_E_MEV = mpf("0.51099895000")

# 1. Classical Substrate
sub_p = substrate_ladder_quantities(Q_PROTON)
h_p = sub_p["h"]
hbar_q_p = sub_p["hbar_q"]
u_p = sub_p["u"]
b_p = sub_p["b"]

# 2. Let's do the Faddeev Transformation t -> i*t
# q = exp(t)
t_p = log(Q_PROTON)
# Under t -> i*t, the new q is q_fad = exp(i*t_p) = cos(t_p) + i*sin(t_p)
# But we can just use the transformation rules directly on hbar_q.
# hbar_q = 2 sinh(t/2) ? No, hbar_q = (q-1)/q = 1 - e^-t.
# Wait, standard h = q - 1/q = 2 sinh(t). 
# Under t -> i*t, h -> 2 i sin(t)
h_fad_sq = -4 * (sin(t_p))**2

print(f"Original h^2: {h_p**2}")
print(f"Faddeev h^2: {h_fad_sq}")

# If the categorical GS net departure is + 9/8 hbar_q^2
# The transformation flips the sign.

# Let's see if we can extract exactly c3 = -2.06934257711516784 from this transformation.
# Let c3 be exactly determined by the Rogers dilogarithm volume or similar.
C3_PROTON = c3_target_at(Q_PROTON, Q_CODATA_MEV, M_E_MEV)
print(f"Exact empirical c3 at proton: {C3_PROTON}")

# What is the formula for c3?
# The shadow is -2. The departure from -2 is -0.069342...
# Is c3 = -2 - 2 * h^2?
# -2 - 2 * (0.0437) = -2.0874 (close)
# Is c3 = -2 * q ?
print(f"-2 * q_proton = {-2 * Q_PROTON}") # -2.219
# Is c3 = -2 * b ?
print(f"-2 * b_proton = {-2 * b_p}") # -1.72
# Is c3 = -2 - hbar_q^2 ?
print(f"-2 - hbar_q_p^2 = {-2 - hbar_q_p**2}") # -2.009
# Is c3 = -2 / q ?
print(f"-2 / q = {-2 / Q_PROTON}") # -1.80

# What if w(q)^2 is analytically just the modular double of something?
