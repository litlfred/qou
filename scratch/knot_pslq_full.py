import mpmath
import snappy

mpmath.mp.dps = 50

def cl3(theta):
    val = mpmath.mpf(0)
    for k in range(1, 100000):
        val += mpmath.cos(k * theta) / (k**3)
    return val

z3 = mpmath.zeta(3)
c1 = cl3(2 * mpmath.pi / 5)
c2 = cl3(4 * mpmath.pi / 5)

knots = ["3_1", "5_1", "7_1", "9_1", "8_19", "10_124"] # T(2,3), T(2,5), T(2,7), T(2,9), T(3,4), T(3,5)
# Note: SnapPy names for T(3,4) is 8_19, T(3,5) is 10_124

for k in knots:
    print(f"--- {k} ---")
    try:
        M = snappy.Manifold(k)
        cs = M.chern_simons()
        print(f"CS = {cs}")
        cs_mp = mpmath.mpf(str(cs))
        rel = mpmath.pslq([cs_mp, 1, z3, c1, c2])
        print(f"PSLQ [CS, 1, zeta(3), Cl_3(2pi/5), Cl_3(4pi/5)] -> {rel}")
    except Exception as e:
        print(f"Error: {e}")
