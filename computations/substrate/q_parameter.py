"""q_parameter — back-compat shim. The canonical module is now
``qou_substrate.constants`` in ``tools/qou-substrate/``.

This file is a thin re-export so the 265 scripts in this directory that
do ``from q_parameter import Q, HA, ...`` keep working without
modification. New code should import from ``qou_substrate`` directly
once ``qou-substrate`` is on PyPI.

The substrate parameter is derived from CODATA m_p/m_e + SnapPy
Vol(4_1) (re-pinned 2026-05-28 from the muon anchor to the more precise
proton anchor — m_μ/m_e is now a prediction); see
``qou_substrate.constants`` for the full derivation docstring.

Promotion rationale: ``docs/workplans/2026-05-24-library-reuse-production-readiness.md``
Tier-2 item 2a.
"""

from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 6, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

def _solve_q_proton_f64(mp_me, vol, iters=80):
    """f64 Newton solve of  m_p/m_e = (2·(vol/ℏ_q²)·F_Bor(q) − 12) * habiro_ratio
    for q, with |tr_M(β_Bor)| = (4+h²−3h⁴−h⁶)/(h²+4). Self-contained
    (closed-form tr_M ⇒ no Hecke machinery)."""
    def _mp_of_q(q):
        h = q - 1.0 / q
        hbar_q = 1.0 - 1.0 / q
        hbar2 = hbar_q ** 2
        trM = abs((4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4))
        qf3 = (q**2 + 1 + q**-2) * (q + 1.0 / q)
        base_ratio = 2 * vol / hbar2 * (trM * qf3 / q**3) - 12
        
        b_val = ((q ** 4 + q ** 2 + 1) / (q ** 2 + 1) ** 2) ** 0.5
        u_val = b_val * hbar2
        habiro_ratio = (1 + 46 * u_val ** 4) * (1 + 4 * u_val ** 5) * (1 - 29 * u_val ** 6)
        return base_ratio * habiro_ratio

    q = 1.11
    # f64 central difference: dq = q·1e-10 is the right scale for f64
    # (machine ε ≈ 2.2e-16); a dps-scaled dq would underflow here. The
    # arbitrary-precision path is q_at() (mpmath findroot, no manual dq).
    for _ in range(iters):
        f = _mp_of_q(q) - mp_me
        dq = q * 1e-10
        fp = (_mp_of_q(q + dq) - _mp_of_q(q - dq)) / (2 * dq)
        if fp == 0:
            break
        step = f / fp
        q -= step
        if abs(step) < 1e-15:  # f64-converged in ~4-5 iters; skip the rest
            break
    return q

import sys
from pathlib import Path

try:
    import qou_substrate.constants as _qs_constants  # noqa: F401
except ImportError:
    _QOU_SUBSTRATE_PYTHON = (
        Path(__file__).resolve().parent.parent.parent.parent  # was: ...parent.parent.parent (pre-Phase-6 — substrate moved into substrate/, added one more .parent to reach repo root)
        / "tools" / "qou-substrate" / "python"
    )
    if _QOU_SUBSTRATE_PYTHON.is_dir() and str(_QOU_SUBSTRATE_PYTHON) not in sys.path:
        sys.path.insert(0, str(_QOU_SUBSTRATE_PYTHON))

from qou_substrate.constants import *  # noqa: F401,F403,E402
