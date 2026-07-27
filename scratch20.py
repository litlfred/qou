import mpmath as mp
import sys
mp.mp.dps = 50
sys.path.insert(0, '/Users/litlfred/space_cats/qou/computations/probes')
from hecke_channel_binding_probe import Q0, E0
from keystone_valuemap_qbessel_gate_s013 import channel_value

f_req = mp.exp(-mp.mpf("2.224566") / E0)

INV = 1/Q0

print("f_req:", f_req)
for e in [15, 16, 17, 18, 19]:
    v = channel_value(e, INV)
    print(f"channel {e}:", v)
