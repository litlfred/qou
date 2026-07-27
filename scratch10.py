import mpmath as mp
import sys
mp.mp.dps = 50
sys.path.insert(0, '/Users/litlfred/space_cats/qou/computations/probes')
from hecke_channel_binding_probe import Q0, E0
from deuteron_fpn_wlambda_wiring import gate_qdim, gate_qfact

f_req = mp.exp(-mp.mpf("2.224566") / E0)
W_alg = gate_qdim((2,1), Q0)**2 / gate_qfact(3, Q0)
W_true = W_alg / 0.98744022702718964051192237850624283357591026346132

z0 = mp.sqrt(Q0) - 1/mp.sqrt(Q0)

print("f_req:", f_req)
print("W_alg:", W_alg)
print("W_true:", W_true)
print("Diff W_alg - f_req:", W_alg - f_req)
print("Diff W_true - f_req:", W_true - f_req)

print("W_alg * (1 - z0^2 * ...)")
