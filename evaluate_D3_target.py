import sys
from pathlib import Path
import json
import math
from mpmath import mp, mpf, pi, polylog, sin, cos

mp.dps = 50

# Load q0
HERE = Path('.').resolve()
sys.path.insert(0, str(HERE / 'folio-assistant' / 'computations'))
import _path_bridge as _pb
Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE / 'folio-assistant' / 'computations')
q_data = json.load(Q_PIN.open())["derived_50_digit"]
q0 = mpf(q_data["q"])

# Constants
h = q0 - 1/q0
alpha_em = mpf(1) / mpf('137.035999084')  # AME2020 value, or use derived value
# The canonical derived alpha_em at q0:
# 1/alpha = q0 * [9] * [10] + 2/(3pi)
def q_int(n, q):
    return (q**n - q**(-n)) / (q - 1/q)

q9 = q_int(9, q0)
q10 = q_int(10, q0)
alpha_inv_derived = q0 * q9 * q10 + mpf(2) / (mpf(3) * pi)
alpha = 1 / alpha_inv_derived

q_dim_2 = q0 + 1/q0

# Target
target = (alpha * q_dim_2) / (mpf(8) * pi) * (1 - h**2 * alpha)
print(f"Target = {target}")

# Compare with Li3(zeta_5)
theta = 2 * pi / 5
z5 = mp.exp(mp.mpc(0,1) * theta)
li3 = polylog(3, z5)
print(f"Re Li3(zeta_5) = {mp.re(li3)}")
print(f"Im Li3(zeta_5) = {mp.im(li3)}")

print(f"Ratio Re: {target / mp.re(li3)}")
print(f"Ratio Im: {target / mp.im(li3)}")

