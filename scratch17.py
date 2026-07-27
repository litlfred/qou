import mpmath as mp
import sys
mp.mp.dps = 50
sys.path.insert(0, '/Users/litlfred/space_cats/qou/computations/probes')
from hecke_channel_binding_probe import Q0, E0

f_req = mp.exp(-mp.mpf("2.224566") / E0)

q0 = Q0
tau0 = mp.log(q0)
A_bare_cont = 2 / mp.sqrt(5) * mp.sinh(tau0 / 5)

print("f_req:", f_req)
print("A_bare_cont:", A_bare_cont)

# What if the modulus is for m=2?
A_bare_m2 = 2 / mp.sqrt(5) * mp.sinh(2 * tau0 / 5)
print("A_bare_m2:", A_bare_m2)

# What if it's the squared modulus?
print("A_bare_cont^2:", A_bare_cont**2)
