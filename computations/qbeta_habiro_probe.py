import sys
from pathlib import Path
import json
from mpmath import mp, mpf

import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
HERE = Path('.').resolve()
sys.path.insert(0, str(HERE))
import _path_bridge as _pb
from codata_constants import M_P_MEV_VALIDATION  # noqa: E402 (codata sweep)

Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
q_data = json.load(Q_PIN.open())["derived_50_digit"]
q0 = mpf(q_data["q"])

h = q0 - 1/q0

def q_num(n, q):
    return (q**n - q**(-n)) / (q - 1/q)

def q_fact(n, q):
    res = mp.mpf(1)
    for i in range(1, n+1):
        res *= q_num(i, q)
    return res

M_e = mpf('0.51099895000')
M_p = mpf(M_P_MEV_VALIDATION)
Q_n = mpf('0.7823432')
M_n = M_p + M_e + Q_n
M_scale = (M_p + M_n)/2

# Target is Q_beta in dimensionless units
qbeta_target = Q_n / M_scale

print(f"Q_beta target = {qbeta_target}")

# Test algebraic terms
# We know the bare splitting was X = (q-1)^2 * (1 - q^-4)/3
# Let's test combinations of h, q, W_111, W_3 etc.

W_3 = 1 / q_fact(3, q0)
W_111 = 1 / q_fact(3, q0)  # In magnitude, [3]! = [3]!

# Maybe Q_beta is related to h^3 or h^4 ?
h2 = h**2
h3 = h**3
h4 = h**4

print("\nAlgebraic scalars:")
print(f"h^3 = {h3}")
print(f"h^4 = {h4}")
print(f"h^4 / [3]! = {h4 * W_3}")
print(f"h^3 / [3]! = {h3 * W_3}")
print(f"h^3 / [4]! = {h3 / q_fact(4, q0)}")
print(f"h^2 / [4]! = {h2 / q_fact(4, q0)}")

print("\nRatios to Q_beta:")
print(f"Q_beta / h^3 = {qbeta_target / h3}")
print(f"Q_beta / h^4 = {qbeta_target / h4}")
print(f"Q_beta / (h^4 / [3]!) = {qbeta_target / (h4 * W_3)}")
print(f"Q_beta / (h^3 / [3]!) = {qbeta_target / (h3 * W_3)}")
print(f"Q_beta / (h^3 / [4]!) = {qbeta_target / (h3 / q_fact(4, q0))}")

