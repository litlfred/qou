import sys
from pathlib import Path
import math

HERE = Path('.').resolve()
sys.path.insert(0, str(HERE / 'folio-assistant' / 'computations'))
import pyhecke_native as pn

# q0 is ~1.10997859555
q0 = 1.1099785955541805
# q_muon is ~1.055
q_mu = 1.0550186

def dim_q(shape, q):
    return float(pn.chi_lambda_braid(shape, [], q))

for q_val, label in [(q0, "proton"), (q_mu, "muon")]:
    print(f"\n--- {label} anchor: q = {q_val} ---")
    d_444 = dim_q([4, 4, 4], q_val)
    d_3 = dim_q([3], q_val)
    print(f"dim_q(4,4,4) = {d_444}")
    print(f"dim_q(3) = {d_3}")
    
    rho_1 = d_444 / (d_3**4)
    print(f"d(4,4,4) / d(3)^4 = {rho_1}")

    print(f"[2]_q = {q_val + 1/q_val}")
    
    # Let's check some other invariants related to (4,4,4)
    # The length of the first column is 3. 
    # Maybe ratio of [dim_q(4,4,4) / something] 

