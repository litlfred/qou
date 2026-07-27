import mpmath as mp
import sys
mp.mp.dps = 50
sys.path.insert(0, '/Users/litlfred/space_cats/qou/computations/probes')
from hecke_channel_binding_probe import Q0, E0
from keystone_valuemap_qbessel_gate_s013 import channel_value

f_req = mp.exp(-mp.mpf("2.224566") / E0)
INV = 1/Q0

exponents = [1, 7, 11, 13, 17, 19, 23, 29]
channels = [channel_value(e, INV) for e in exponents]

# linear combinations
bases = [f_req, 1] + channels
res = mp.pslq(bases, tol=1e-12)
print("linear:", res)

# linear combinations without 1
res_no1 = mp.pslq([f_req] + channels, tol=1e-12)
print("linear without 1:", res_no1)

# try simple ratios
for i, c1 in enumerate(channels):
    for j, c2 in enumerate(channels):
        if i != j:
            if abs(c1/c2 - f_req) < 1e-4:
                print(f"Ratio {exponents[i]}/{exponents[j]} = {c1/c2} (diff {c1/c2 - f_req})")

