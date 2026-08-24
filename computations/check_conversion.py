import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: F401
from mpmath import mp, mpf
from q_parameter import Q_50_DIGIT_STR

mp.dps = 50
# Was a bare float64 literal 1.109978033355325x — a value that is NEITHER pin,
# 495 ppb from proton and 506 ppb from muon, i.e. ~44x the ~11.5 ppb mu-p
# substrate tension. It was also float64 in a computations/ script, which
# AGENTS.md forbids outright. Both are fixed by reading the declared pin.

q0 = mpf(Q_50_DIGIT_STR)
h = q0 - 1/q0
dim_q = q0 + 1/q0
hbar_q = (q0 - 1)/q0
print(f"q0: {q0}, h: {h}, dim_q: {dim_q}, hbar_q: {hbar_q}")

# L_pred for H2O
L_pred = 40.20932898181625 # kJ/mol
print(f"L_pred: {L_pred} kJ/mol")

# Try to find 369 K
T_boil_1 = L_pred * 1000 / (dim_q * 8.31446)
print(f"L_pred * 1000 / (dim_q * R) = {T_boil_1} K")

T_boil_2 = L_pred / hbar_q
print(f"L_pred / hbar_q = {T_boil_2}")

T_boil_3 = (L_pred * 1000 / 8.31446) / (dim_q / hbar_q)
print(f"(L_pred * 1000 / R) / (dim_q / hbar_q) = {T_boil_3} K")

# Let's brute force the factor connecting 40.209 to 369
factor = (40.20932898181625 * 1000) / 369
print(f"Required Delta S_vap for 369 K: {factor} J/(mol K)")

print(f"Is it R * dim_q / hbar_q? {8.31446 * dim_q / hbar_q}")
