import mpmath

mpmath.mp.dps = 50

def cl3(theta):
    val = mpmath.mpf(0)
    for k in range(1, 100000):
        val += mpmath.cos(k * theta) / (k**3)
    return val

z3 = mpmath.zeta(3)
c1 = cl3(2 * mpmath.pi / 5)
c2 = cl3(4 * mpmath.pi / 5)

# Known CS values from snappy for the knots
cs_vals = {
    "T(2,3)": mpmath.mpf("0.08333333333333333333333333333333333333333333333333"),
    "T(2,5)": mpmath.mpf("0.05000000000000000000000000000000000000000000000000"),
    "T(2,7)": mpmath.mpf("0.10714285714285714285714285714285714285714285714285"),
    "T(2,9)": mpmath.mpf("0.13888888888888888888888888888888888888888888888888")
}

for name, cs in cs_vals.items():
    print(f"--- {name} ---")
    print(f"CS = {cs}")
    # Try to find integers a, b, c, d such that a*CS + b*z3 + c*c1 + d*c2 = 0
    # Wait, the problem says "fit as Q-linear combination of {zeta(3), c1, c2}"
    # Meaning CS = A*z3 + B*c1 + C*c2.
    # So we look for relation [cs, z3, c1, c2]
    rel = mpmath.pslq([cs, z3, c1, c2])
    print(f"PSLQ [CS, zeta(3), Cl_3(2pi/5), Cl_3(4pi/5)] -> {rel}")
    
    # Let's also include 1 to show it's rational
    rel_with_1 = mpmath.pslq([cs, 1, z3, c1, c2])
    print(f"PSLQ [CS, 1, zeta(3), Cl_3(2pi/5), Cl_3(4pi/5)] -> {rel_with_1}")

