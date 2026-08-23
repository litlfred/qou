"""Q_beta Form-A shape probe, evaluated at the muon (ideal CAL-2) anchor.

The anchor is READ, not retyped. It used to be the 50-char literal

    1.1099785955573347596001309852899479366668383822292

which is not the muon pin, not the proton pin, and not the CODATA-2018
derivation either: it tracks the muon anchor for 17 digits and then goes its
own way from the 18th. No pin in the corpus produces it, so it was a
transcription slip that nothing could ever detect, because a transcribed
constant is exactly the thing the anchor machinery cannot re-pin or flip.
"""
import sys
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parent),
                str(Path(__file__).resolve().parent / "substrate")]
import _path_bridge  # noqa: F401,E402

from mpmath import mp  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1]
                       / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import _q0_value_for_anchor  # noqa: E402

mp.dps = 50
q0 = mp.mpf(_q0_value_for_anchor("muon"))
m_e = mp.mpf('0.51099895000')
Q_beta_codata = mp.mpf('0.78233341000')

tr_M_p = mp.mpf('1.06530622861316626170946619823')
tr_M_n = mp.mpf('0.923233297186152879199028120638')

delta_tr = tr_M_p - tr_M_n
print(f"delta_tr (Habiro exact): {delta_tr}")

Q_A = m_e * abs(q0**2 - 2*q0 - 1) * (q0 + 1) / (2 * q0**3)
print(f"Q_A (Form A): {Q_A}")
print(f"Q_beta_codata: {Q_beta_codata}")

E_0 = (q0 + 1) / (2 * q0**3)
print(f"E_0: {E_0}")

delta_net = q0**2 - 2*q0 - 1
print(f"delta_net (Form A): {delta_net}")

ratio = Q_beta_codata / (m_e * E_0)
print(f"Required value of |delta_net|: {ratio}")
print(f"Ratio of required / delta_tr: {ratio / delta_tr}")

chi_diff_exact = -(q0**4 + 1) * (q0**2 - 1) / (4 * q0**3)
print(f"chi_diff_exact: {chi_diff_exact}")
print(f"Ratio of required / abs(chi_diff_exact): {ratio / abs(chi_diff_exact)}")
