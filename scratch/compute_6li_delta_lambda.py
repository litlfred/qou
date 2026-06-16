import sys
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "computations"))
sys.path.insert(0, str(HERE.parent / "computations" / "substrate"))
sys.path.insert(0, str(HERE.parent / "tools" / "qou-substrate" / "python"))

import _path_bridge
from _precision import set_compute_dps
set_compute_dps()

import mpmath as mp
from tr_m_atom_via_transfer import tr_m_atom_zn
from experimental_constants import Q_BETA_N_MEV

mp.mp.dps = 50

# A=6 (3, 3) 6Li
Z, N = 3, 3
tr_atom_mp, tr_free_mp, chi_atom, wall = tr_m_atom_zn(Z, N, dps=50)

delta_tr = tr_free_mp - tr_atom_mp
B_pred = float(mp.mpf(str(Q_BETA_N_MEV)) * delta_tr)
print(f"6Li tr_atom = {tr_atom_mp}")
print(f"6Li tr_free = {tr_free_mp}")
print(f"6Li B_pred_canonical = {B_pred}")

# B_AME = 31.994 MeV
B_ame = 31.994
delta_lambda = B_ame / B_pred
print(f"6Li delta_lambda = {delta_lambda}")

# A=5 (3, 2) 5Li
Z, N = 3, 2
tr_atom_mp, tr_free_mp, chi_atom, wall = tr_m_atom_zn(Z, N, dps=50)

delta_tr = tr_free_mp - tr_atom_mp
B_pred = float(mp.mpf(str(Q_BETA_N_MEV)) * delta_tr)
print(f"5Li tr_atom = {tr_atom_mp}")
print(f"5Li tr_free = {tr_free_mp}")
print(f"5Li B_pred_canonical = {B_pred}")

# B_AME = 26.33 MeV (approx, 5Li is unstable but let's see)
# AME B for 5Li is 26.33 MeV or we can just print B_pred
print(f"5Li B_pred_canonical = {B_pred}")
