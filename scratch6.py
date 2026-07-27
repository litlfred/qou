import mpmath as mp
import sys
mp.mp.dps = 50
sys.path.insert(0, '/Users/litlfred/space_cats/qou/computations/probes')
from hecke_channel_binding_probe import Q0, E0
from deuteron_fpn_wlambda_wiring import gate_qdim, gate_qfact, gate_partitions, gate_Z

Z3 = gate_Z(3, Q0)
W_alg = gate_qdim((2,1), Q0)**2 / gate_qfact(3, Q0)
W_true_plancherel = W_alg / Z3

print("Z3:", Z3)
print("W_alg:", W_alg)
print("W_true_plancherel:", W_true_plancherel)

f_req = mp.exp(-mp.mpf("2.224566") / E0)
print("f_req:", f_req)

