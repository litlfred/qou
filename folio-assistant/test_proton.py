import sys
from pathlib import Path
import mpmath as mp
sys.path.insert(0, 'computations')
from chi_monotone_transfer import chi_all_lambda
from chi_free_via_lr import load_nucleon_chi

mp.mp.dps = 50
import json

word = []
# Need to construct the proton word exactly as atom_braid_word_3A does for a single proton
from hecke_core import _PROTON_G0, _PROTON_G1
for c, d in _PROTON_G0: word.append((float(c), float(d), 0))
for c, d in _PROTON_G1: word.append((float(c), float(d), 1))

chf = chi_all_lambda(word, 3)
nuc = load_nucleon_chi(50)['p']

for lam in chf:
    print(f"{lam}: diff={abs(chf[lam] - nuc.get(lam, 0))}")
