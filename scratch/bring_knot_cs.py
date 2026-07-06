import sys
import math
import snappy
try:
    import mpmath
    mpmath.mp.dps = 50
except ImportError:
    print("Please install mpmath")
    sys.exit(1)

knots = ["T(2,3)", "T(2,5)", "T(2,7)", "T(2,9)", "T(3,4)", "T(3,5)", "T(5,2)"]

def cl3(theta):
    # Cl_3(theta) = sum_{k=1}^infty cos(k theta) / k^3
    val = mpmath.mpf(0)
    for k in range(1, 10000):
        val += mpmath.cos(k * theta) / (k**3)
    return val

z3 = mpmath.zeta(3)
c1 = cl3(2*mpmath.pi/5)
c2 = cl3(4*mpmath.pi/5)

print(f"zeta(3)     = {z3}")
print(f"Cl_3(2pi/5) = {c1}")
print(f"Cl_3(4pi/5) = {c2}")

for k in knots:
    L = snappy.Link(k)
    M = L.exterior()
    cs = M.chern_simons()
    vol = M.volume()
    print(f"{k}: Vol = {vol}, CS = {cs}")
