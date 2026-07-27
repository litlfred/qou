import mpmath as mp
import sys
mp.mp.dps = 50
sys.path.insert(0, '/Users/litlfred/space_cats/qou/computations/probes')
from hecke_channel_binding_probe import Q0, E0
from deuteron_fpn_wlambda_wiring import gate_qdim, gate_qfact

f_req = mp.exp(-mp.mpf("2.224566") / E0)
G = mp.catalan

# Try to find a simple relation for f_req
res = mp.pslq([f_req, mp.mpf(1), mp.pi, G, mp.sqrt(2), mp.sqrt(3), mp.sqrt(5)], tol=1e-12)
print("PSLQ f_req:", res)
