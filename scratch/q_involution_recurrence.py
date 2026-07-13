import sys
from pathlib import Path
sys.path.insert(0, "computations")
from binding_manybody_jet_filtration import a_D
import mpmath as mp

q = mp.mpf("1.1099793132717013149866657930777598687799017684617")

print("n | S_n(q) = n * a_D(n)")
for n in range(1, 10):
    Sn = n * a_D(n)
    print(f"{n} | {float(Sn):.4f}")
