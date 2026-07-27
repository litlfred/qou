import mpmath as mp
import sys
mp.mp.dps = 50
sys.path.insert(0, '/Users/litlfred/space_cats/qou/computations/probes')
from hecke_channel_binding_probe import Q0, E0
from deuteron_fpn_wlambda_wiring import gate_qdim, gate_qfact

f_req = mp.exp(-mp.mpf("2.224566") / E0)
W_alg = gate_qdim((2,1), Q0)**2 / gate_qfact(3, Q0)

q = Q0
z0 = mp.sqrt(q) - 1/mp.sqrt(q)
z = mp.sqrt(q) / (q + 1)
h = q - 1/q

print("f_req:", f_req)

# Try combinations with Bring measure 1/(8pi) or 2/(3pi)
pi = mp.pi
terms = [f_req, W_alg, W_alg*z0, W_alg*h, W_alg/pi, W_alg*z0/pi, W_alg*h/pi, mp.mpf(1)]
print(mp.pslq(terms, tol=1e-12))

# Let's search the repo for 0.587 or 0.588
