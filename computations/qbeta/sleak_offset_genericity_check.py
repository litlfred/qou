#!/usr/bin/env python3
"""Is the S_leak sign flip specific to Vol(4_1)?  No -- it is offset-generic.

S_leak(q0) := c_3(q0) + Vol(4_1) is DEFINED, not derived.  The "genuine sign
change" S_leak(mu) > 0 > S_leak(p) that the SLeakZeroCrossing theorems take as
their empirical input holds for ANY constant V strictly between -c_3(mu) and
-c_3(p).  Vol(4_1) lies in that window, but so do many unrelated constants, so
the flip is a restatement of "c_3 differs between anchors" -- not evidence
about Vol(4_1).
"""
from mpmath import mp, mpf
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
# Anchors DERIVED and PAIRED (qou-cds1 / qou-t39x, 2026-08-31). These were
# hand-typed as -2.02020024 / -2.06934258; the muon literal was the CODATA-2018
# extraction, superseded when fca08de7d2 (2026-08-22) moved the pin to CODATA
# 2022 (-2.01986031). The window moves with it -- (2.01986, 2.06934) rather than
# (2.02020, 2.06934) -- and Vol(4_1) = 2.02988 is still strictly inside, so the
# conclusion is unchanged and now cannot silently straddle an anchor again.
from qbeta_utils import c3_target_at  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as _C  # noqa: E402

_ME, _QB = mpf(str(_C.M_E_MEV)), mpf(str(_C.Q_BETA_MEV))
c3_mu = c3_target_at(mpf(str(q_muon_at(50))), _QB, _ME, convention="C")
c3_p = c3_target_at(mpf(str(q_at(50))), _QB, _ME, convention="C")
assert abs(c3_p - mpf('-2.06934258')) < mpf('1e-6'), c3_p  # extractor licensed
lo, hi = -c3_mu, -c3_p
CANDS = [('Vol(4_1)', mpf('2.029883212819307')), ('2 + 1/36', 2 + mpf(1)/36),
         ('2 + 1/30', 2 + mpf(1)/30), ('2 + 1/25', 2 + mpf(1)/25),
         ('2 + 1/24', 2 + mpf(1)/24), ('63/31', mpf(63)/31),
         ('e^0.708', mp.e**mpf('0.708'))]
print(f'window (-c3(mu), -c3(p)) = ({mp.nstr(lo,12)}, {mp.nstr(hi,12)})')
print(f'width = {mp.nstr(hi-lo,6)}\n')
n_flip = 0
for nm, V in CANDS:
    flip = (c3_mu + V > 0) and (c3_p + V < 0)
    assert flip == (lo < V < hi), f'{nm}: flip != in-window'
    n_flip += flip
    print(f'  {nm:10s} V={mp.nstr(V,10):14s} sign-flip={flip}')
assert n_flip == len(CANDS), 'expected every in-window constant to flip'
print(f'\n{n_flip}/{len(CANDS)} unrelated constants reproduce the SAME sign flip.')
print('=> the flip is offset-generic; it is not evidence about Vol(4_1).')
