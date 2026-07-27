import mpmath as mp
import sys
mp.mp.dps = 50
sys.path.insert(0, '/Users/litlfred/space_cats/qou/computations/probes')
from hecke_channel_binding_probe import Q0, E0
from deuteron_fpn_wlambda_wiring import gate_qdim, gate_qfact

W_alg = gate_qdim((2,1), Q0)**2 / gate_qfact(3, Q0)
f_req = mp.exp(-mp.mpf("2.224566") / E0)

z0 = mp.sqrt(Q0) - 1/mp.sqrt(Q0)
z = mp.sqrt(Q0) / (Q0 + 1)
h = Q0 - 1/Q0

print("ln f_req:", mp.log(f_req))
print("ln W_alg:", mp.log(W_alg))
diff = mp.log(f_req) - mp.log(W_alg)
print("diff:", diff)
print("z0:", z0)
print("h:", h)
print("diff / z0:", diff / z0)
print("diff / h:", diff / h)
print("diff / z:", diff / z)

print("What if the geometric W is W_alg * (1 - something) ?")
delta = 1 - f_req / W_alg
print("delta:", delta)
print("delta / z0:", delta / z0)

# Let's check Bring curve invariants. B3 = 3?
# The trace of the monodromy is 1.006730454652734
trM = mp.mpf("1.006730454652734")
print("delta * trM:", delta * trM)
print("delta / (z0 * trM):", delta / (z0 * trM))
