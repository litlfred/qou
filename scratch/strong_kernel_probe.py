import mpmath as mp

mp.dps = 50
q0 = mp.mpf("1.1099793132717013149866657930777598687799017684617")
def qbracket(k):
    return (q0**k - q0**(-k)) / (q0 - 1/q0)

r_residual = qbracket(5) / qbracket(2)
r_gluonic = qbracket(9) / qbracket(3)

# Target weights
w_2 = mp.mpf("4.35336338")
w_3 = mp.mpf("8.59989938")
w_4 = mp.mpf("15.60416399")

# Test depth-2 relation: w_4 = a0 * w_3 + a1 * w_2
# If a1 = r_residual
a1 = r_residual
a0 = (w_4 - a1 * w_2) / w_3

print(f"If a1 = r_residual ({a1}), then a0 = {a0}")

# What if a1 = r_gluonic?
a1_g = r_gluonic
a0_g = (w_4 - a1_g * w_2) / w_3
print(f"If a1 = r_gluonic ({a1_g}), then a0 = {a0_g}")

# What if we use NA-Stokes constants exactly instead of traces at q0?
# NA-stokes: r_res = 2.5, r_glu = 3
a1_limit = mp.mpf("2.5")
a0_limit = (w_4 - a1_limit * w_2) / w_3
print(f"If a1 = 2.5, then a0 = {a0_limit}")

