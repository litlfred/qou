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
m_e = mpf('0.51099895000')

h = q0 - 1/q0
scalar_diff = q0**3 - q0**(-3)

print(f"q0: {q0}")
print(f"h: {h}")
print(f"q0^3 - q0^-3 = {scalar_diff}")
print(f"m_e * (q0^3 - q0^-3) = {m_e * scalar_diff}")

# Trace difference
print(f"m_n - m_p target = {1.29333205}")

