import sys
from pathlib import Path
import mpmath as mp

HERE = Path("/Users/litlfred/space_cats/qou/computations")
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE))
from q_parameter import q_at
from _precision import set_compute_dps

set_compute_dps()
q = q_at(mp.mp.dps)
qint2 = (q**2 - q**(-2)) / (q - 1/q)
qint2_alt = q + 1/q

w2 = mp.mpf("3.256155117016104679351106404894297704361814764980251767711060353758519")
w3 = mp.mpf("4.925300296113157119292095762146104277120860749377513541864134506680845")
w4 = mp.mpf("7.499872527503504696441367518672237575403461246138818127348445509559206")

print("qint2:", qint2_alt)
print("qint2 * w3 - w2:", qint2_alt * w3 - w2)
print("w4:", w4)
print("Diff:", qint2_alt * w3 - w2 - w4)

