import sys
from pathlib import Path
import json
from mpmath import mp, mpf

mp.dps = 50
HERE = Path('.').resolve()
sys.path.insert(0, str(HERE / 'folio-assistant' / 'computations'))
import _path_bridge as _pb
Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE / 'folio-assistant' / 'computations')
q_data = json.load(Q_PIN.open())["derived_50_digit"]
q0 = mpf(q_data["q"])

def _x_baseline(q):
    return (q - 1)**2 * (1 - q**(-4)) / 3

print(f"X_baseline: {_x_baseline(q0)}")

M_e = mpf('0.51099895000')
M_p = mpf('938.27208816')
Q_n = mpf('0.7823432') # beta decay Q-value
M_n = M_p + M_e + Q_n

# Flavor split
delta_target = (M_n - M_p) / ((M_p + M_n)/2)
print(f"delta_target: {delta_target}")

resid = delta_target - _x_baseline(q0)
print(f"Residual: {resid} (ratio: {resid / delta_target})")

