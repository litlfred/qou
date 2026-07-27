import mpmath as mp
import sys
mp.mp.dps = 50
sys.path.insert(0, '/Users/litlfred/space_cats/qou/computations/probes')
from hecke_channel_binding_probe import Q0, E0
from deuteron_fpn_wlambda_wiring import gate_qdim, gate_qfact, gate_Z
from keystone_valuemap_qbessel_gate_s013 import channel_value

f_req = mp.exp(-mp.mpf("2.224566") / E0)

INV = 1/Q0

print("f_req:", f_req)
for e in [1, 7, 11, 13]:
    v = channel_value(e, INV)
    print(f"channel {e}:", v)
    print(f"ratio {e} to f_req:", v / f_req)

