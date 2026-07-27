import mpmath as mp
import sys
mp.mp.dps = 50
sys.path.insert(0, '/Users/litlfred/space_cats/qou/computations/probes')
from hecke_channel_binding_probe import Q0, E0

f_req = mp.exp(-mp.mpf("2.224566") / E0)

q = Q0
z = mp.sqrt(q)/(q+1)
z0 = mp.sqrt(q) - 1/mp.sqrt(q)
h = q - 1/q
q2 = q**2
q3 = q**3
dq2 = q + 1/q
dq3 = q**2 + 1 + 1/q**2
W_alg = dq2**2 / dq3
W_true = dq2**2 / (2 + dq2**2)
W_true2 = dq2**2 / (1 + dq2**2 + 1)
dq4 = (q**2 - q**-2)/(q - q**-1)

bases = [f_req, 1, z, z0, h, dq2, dq3, dq4, W_alg, W_true]
# search for rational relation
res = mp.pslq(bases, tol=1e-12)
print("PSLQ linear:", res)

# search for multiplicative relation
log_bases = [mp.log(x) for x in bases]
res_log = mp.pslq(log_bases, tol=1e-12)
print("PSLQ multiplicative:", res_log)

