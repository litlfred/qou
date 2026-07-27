import mpmath as mp
import sys
mp.mp.dps = 50
sys.path.insert(0, '/Users/litlfred/space_cats/qou/computations/probes')
from hecke_channel_binding_probe import Q0, E0
from deuteron_fpn_wlambda_wiring import gate_qdim, gate_qfact, gate_Z

f_req = mp.exp(-mp.mpf("2.224566") / E0)
W_alg = gate_qdim((2,1), Q0)**2 / gate_qfact(3, Q0)
W_true = W_alg / gate_Z(3, Q0)

q = Q0
z0 = mp.sqrt(q) - 1/mp.sqrt(q)
h = q - 1/q

print(mp.pslq([f_req, W_alg, W_alg*z0, W_alg*z0**2, W_alg*h, W_alg*h**2], tol=1e-12))
print(mp.pslq([f_req, W_true, W_true*z0, W_true*z0**2, W_true*h, W_true*h**2], tol=1e-12))

print(mp.pslq([f_req, 1, z0, z0**2, h, h**2], tol=1e-12))

# What about sqrt(f_req) ?
print(mp.pslq([mp.sqrt(f_req), mp.sqrt(W_true), mp.sqrt(W_true)*z0], tol=1e-12))

