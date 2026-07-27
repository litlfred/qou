import mpmath as mp
import sys
import itertools
mp.mp.dps = 50
sys.path.insert(0, '/Users/litlfred/space_cats/qou/computations/probes')
from hecke_channel_binding_probe import Q0, E0
from deuteron_fpn_wlambda_wiring import gate_qdim, gate_qfact, gate_Z

Z3 = gate_Z(3, Q0)
W_alg = gate_qdim((2,1), Q0)**2 / gate_qfact(3, Q0)
W_true = W_alg / Z3
f_req = mp.exp(-mp.mpf("2.224566") / E0)

q = Q0
z0 = mp.sqrt(q) - 1/mp.sqrt(q)
z = mp.sqrt(q) / (q + 1)
h = q - 1/q

sqrt2 = mp.sqrt(2)
sqrt3 = mp.sqrt(3)
sqrt5 = mp.sqrt(5)
pi = mp.pi

bases = [
    W_alg, W_true, f_req, z0, z, h, sqrt2, sqrt3, sqrt5, pi, mp.mpf(1)
]

print("f_req:", f_req)
print("W_alg:", W_alg)
print("W_true:", W_true)

# Ratio check
ratio1 = f_req / W_alg
ratio2 = f_req / W_true
print("f_req / W_alg:", ratio1)
print("f_req / W_true:", ratio2)

# Check PSLQ on ratio1 with sqrt2, sqrt3, sqrt5, pi, z0
res = mp.pslq([ratio1, 1, sqrt2, sqrt3, sqrt5, z0, h], tol=1e-12)
print("PSLQ ratio1:", res)
res = mp.pslq([ratio2, 1, sqrt2, sqrt3, sqrt5, z0, h], tol=1e-12)
print("PSLQ ratio2:", res)

# Check algebraic combinations
for terms in [
    [ratio1, 1, z0, z0**2, z0**3, h, h**2],
    [ratio2, 1, z0, z0**2, z0**3, h, h**2],
]:
    print("PSLQ:", mp.pslq(terms, tol=1e-12))

# What if f_req = z - something?
print("f_req - z:", f_req - z)
print("z - f_req:", z - f_req)

