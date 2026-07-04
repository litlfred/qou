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

# NOTE (2026-07-04): a local duplicate `_solve_q_proton_f64` used to live
# here, but it was dead code (underscore-private, uncalled — `from … import *`
# below does not re-export underscore names) and had drifted: it still
# embedded the fitted `(1 + 46u⁴)(1 + 4u⁵)(1 − 29u⁶)` habiro tower that the
# owner ruling 2026-07-03 stripped from the canonical solver and PR #3280
# dropped from the m_p producer. Removed to leave a single source of truth —
# the canonical `qou_substrate.constants._solve_q_proton_f64` (tower-free) —
# which can be imported directly from the canonical module if needed. This does
# NOT change `Q` / `Q_50_DIGIT_STR` (both are public names, so they DO come
# through the `import *` below); the owner-gated pin re-pin is bean 2i8g.

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
