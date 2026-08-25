from mpmath import mp
import sys
sys.path.append('.')
from computations.q_parameter import Q_50_DIGIT_STR
from computations.codata_constants import Q_BETA_MEV
from computations.experimental_constants import M_E_MEV
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
q0 = mp.mpf(Q_50_DIGIT_STR)
m_e = mp.mpf(M_E_MEV)
Q_beta_codata = mp.mpf(str(Q_BETA_MEV))

tr_M_p = mp.mpf('1.06530622861316626170946619823')
tr_M_n = mp.mpf('0.923233297186152879199028120638')

delta_tr = tr_M_p - tr_M_n
print(f"delta_tr: {delta_tr}")

Q_A = m_e * abs(q0**2 - 2*q0 - 1) * (q0 + 1) / (2 * q0**3)
print(f"Q_A: {Q_A}")
print(f"Q_beta_codata: {Q_beta_codata}")

E_0 = (q0 + 1) / (2 * q0**3)
print(f"E_0: {E_0}")

delta_net = q0**2 - 2*q0 - 1
print(f"delta_net (Form A): {delta_net}")

# Test if Q_beta could just be m_e * E_0 * f(delta_tr)
# What is the ratio Q_beta_codata / (m_e * E_0)?
ratio = Q_beta_codata / (m_e * E_0)
print(f"Required value of |delta_net|: {ratio}")

print(f"Ratio of required / delta_tr: {ratio / delta_tr}")

