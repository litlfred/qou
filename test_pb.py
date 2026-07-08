import sys
from pathlib import Path
sys.path.insert(0, "/Users/litlfred/space_cats/qou/computations/sweeps")
from paper_six_term_isotope_sweep import paper_six_term_mass

# 178Pb
try:
    res = paper_six_term_mass(82, 96, tower_mode="r-side-bare", term5_mode="additive", isotope_label="178Pb")
    print(res)
except Exception as e:
    print(e)
