import sympy as sp
from mpmath import mp, mpf

mp.dps = 100

from qbeta_utils import substrate_ladder_quantities, c3_target_at

# Proton anchor (from docs/audits/2026-07-06-c3-not-exact-cross-anchor-verdict.md)
# wait, I don't have the explicit strings for Q_CODATA and M_E.
# Let's import them or define them.
# The Q_codata is the neutron beta decay Q value.
Q_CODATA_MEV = mpf("0.782333583274213580521634562479207") # approx
M_E_MEV = mpf("0.51099895000") # approx
Q_PROTON = mpf("1.1099785827513808075916690956107688798744991218736")

# Let's just use the exact C3_PROTON value from w_compute_test.py
C3_PROTON = mpf("-2.06934257711516784")

# Let's get the substrate quantities
sub = substrate_ladder_quantities(Q_PROTON)
h_val = sub["h"]
u_val = sub["u"]
b_val = sub["b"]
hbar_q_val = sub["hbar_q"]

# We know that w(u) - 1 = - (h - 2)/2 * (-u^2 + c3 * u^3 + c4 * u^4 + ...)
# So w(u) at the proton root is:
w_p = mpf('1') - (h_val - mpf('2')) / mpf('2') * (-u_val**2 + C3_PROTON * u_val**3) # truncated at u^3

print(f"w(q_proton) approx from series up to u^3: {w_p}")

# What if w(q)^2 is some simple fractional linear function of y or h^2?
# The affine narrowing audit states:
# L(w) = (h - 2w) / (h - 2w_0)
# w_0 = 1
# Let's compute L(w)
L_w = (h_val - mpf('2') * w_p) / (h_val - mpf('2'))
print(f"L(w_p) = {L_w}")

# The ladder factor L(w) should be exactly 1 - u^2 + c3*u^3 + c4*u^4 ...
# Indeed, L(w) = 1 + (-u^2 + c3*u^3)
ladder_expected = mpf('1') - u_val**2 + C3_PROTON * u_val**3
print(f"Expected ladder: {ladder_expected}")

# We want an exact rational function for L(w_p) or w_p
# Let's run PSLQ on w_p against h_val, u_val, b_val, etc.
basis = [w_p, mpf('1'), h_val, h_val**2, u_val, u_val**2, u_val**3]
try:
    rel = mp.pslq(basis)
    print(f"PSLQ on w_p: {rel}")
except:
    print("No simple PSLQ relation for w_p")

# PSLQ on c3? The problem is we don't have the EXACT c3, it's empirical from CODATA.
# But wait! If c3 is exact in some algebraic extension, PSLQ might find it if we give it high precision.
# However, C3_PROTON = -2.06934... is only 17 digits. We can't PSLQ 17 digits against many terms.
