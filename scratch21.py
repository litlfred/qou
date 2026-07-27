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

print(mp.pslq([f_req, 1, z, z0, h, z*h, z0*h], tol=1e-12))
print(mp.pslq([f_req, 1, z, z**2, h, h**2], tol=1e-12))

