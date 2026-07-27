import mpmath as mp
import sys
mp.mp.dps = 50
sys.path.insert(0, '/Users/litlfred/space_cats/qou/computations/probes')
from hecke_channel_binding_probe import Q0, E0
from keystone_valuemap_qbessel_gate_s013 import channel_value

f_req = mp.exp(-mp.mpf("2.224566") / E0)
INV = 1/Q0

sum_a1 = sum(channel_value(e, INV) for e in [1, 11, 19, 29])
sum_a2 = sum(channel_value(e, INV) for e in [7, 13, 17, 23])

print("f_req:", f_req)
print("sum_a1:", sum_a1)
print("sum_a2 / sum_a1:", sum_a2 / sum_a1)
print("sum_a1 / sum_a2:", sum_a1 / sum_a2)
