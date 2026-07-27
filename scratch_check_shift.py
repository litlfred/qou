import mpmath as mp
import sys
sys.path.insert(0, '/Users/litlfred/space_cats/qou/computations/probes')
from hecke_channel_binding_probe import Q0, E0
mp.mp.dps = 50
f_req = mp.exp(-mp.mpf("2.224566") / E0)
pi = mp.pi

W_true = (Q0+1/Q0)**2 / (2 + (Q0+1/Q0)**2)
print("W_true - 1/(8pi):", W_true - 1/(8*pi))
print("W_true - 2/(3pi):", W_true - 2/(3*pi))
print("W_alg - 1/(8pi):", 0.660673 - 1/(8*pi))
print("f_req:", f_req)
