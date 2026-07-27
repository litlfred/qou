import mpmath as mp
import sys
mp.mp.dps = 50
sys.path.insert(0, '/Users/litlfred/space_cats/qou/computations/probes')
from hecke_channel_binding_probe import Q0, E0
from deuteron_fpn_wlambda_wiring import gate_qdim, gate_qfact, gate_Z

f_req = mp.exp(-mp.mpf("2.224566") / E0)
W_alg = gate_qdim((2,1), Q0)**2 / gate_qfact(3, Q0)
W_true = W_alg / gate_Z(3, Q0)

print("f_req:", f_req)
print("sqrt(W_true):", mp.sqrt(W_true))
print("sqrt(W_alg):", mp.sqrt(W_alg))
print("W_true / sqrt(2):", W_true / mp.sqrt(2))
