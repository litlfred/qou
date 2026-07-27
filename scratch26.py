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
dq2 = q + 1/q
dq3 = q**2 + 1 + 1/q**2
W_alg = dq2**2 / dq3
W_true = dq2**2 / (2 + dq2**2)

pi = mp.pi
bases = [f_req, 1, W_alg, W_true, 1/(8*pi), 2/(3*pi), mp.mpf(1)/8, 1/(12*pi**2)]
res = mp.pslq(bases, tol=1e-12)
print("PSLQ linear:", res)

log_bases = [mp.log(x) for x in bases if x > 0]
res_log = mp.pslq(log_bases, tol=1e-12)
print("PSLQ multiplicative:", res_log)

