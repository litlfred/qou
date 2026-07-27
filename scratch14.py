import mpmath as mp
import sys
mp.mp.dps = 50
sys.path.insert(0, '/Users/litlfred/space_cats/qou/computations/probes')
from hecke_channel_binding_probe import Q0, E0

f_req = mp.exp(-mp.mpf("2.224566") / E0)

q = Q0
A2_squared = ((q**2 - q**-2)**2) / 5
print("f_req:", f_req)
print("A2_squared:", A2_squared)

A3_squared = ((q**3 - q**-3)**2) / 5
print("A3_squared:", A3_squared)

A1_squared = ((q - q**-1)**2) / 5
print("A1_squared:", A1_squared)

print("A2_squared / f_req:", A2_squared / f_req)

