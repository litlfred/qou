import mpmath as mp
import sys
mp.mp.dps = 50
sys.path.insert(0, '/Users/litlfred/space_cats/qou/computations/probes')
from hecke_channel_binding_probe import Q0, E0
from deuteron_fpn_wlambda_wiring import gate_qdim, gate_qfact

W_alg = gate_qdim((2,1), Q0)**2 / gate_qfact(3, Q0)
f_req = mp.exp(-mp.mpf("2.224566") / E0)
ratio = f_req / W_alg

z0 = mp.sqrt(Q0) - 1/mp.sqrt(Q0)
z = mp.sqrt(Q0) / (Q0 + 1)
h = Q0 - 1/Q0

print("ratio:", ratio)
print("z0:", z0)
print("h:", h)
print("1 - ratio:", 1 - ratio)

terms = [1 - ratio, z0, z0**2, z0**3, h, h**2, h**3, z0*h, mp.mpf(1)]
res = mp.pslq(terms, tol=1e-15)
print("PSLQ (1 - ratio, z0, z0^2, z0^3, h, h^2, h^3, z0*h, 1):", res)

# What about just a polynomial in z0?
res = mp.pslq([1 - ratio, z0, z0**2, z0**3, z0**4, z0**5, mp.mpf(1)], tol=1e-15)
print("PSLQ (1-ratio, z0, z0^2, z0^3, 1):", res)

# Let's try to match f_req directly with W_alg, z0, z0**2, etc.
terms = [f_req, W_alg, W_alg*z0, W_alg*z0**2, W_alg*z0**3]
res = mp.pslq(terms, tol=1e-15)
print("PSLQ f_req, W_alg * poly(z0):", res)

