"""_precision — back-compat shim. The canonical module is now
``qou_substrate.precision`` in ``tools/qou-substrate/``.

This file is a thin re-export so the 121 scripts in this directory that
do ``from _precision import set_compute_dps, fmt`` keep working without
modification. New code should import from ``qou_substrate`` directly
once ``qou-substrate`` is on PyPI.

See ``docs/workplans/2026-05-24-library-reuse-production-readiness.md``
Tier-2 item 2a for the promotion rationale.
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

import sys
from pathlib import Path

try:
    import qou_substrate.precision as _qs_precision  # noqa: F401
except ImportError:
    _QOU_SUBSTRATE_PYTHON = (
        Path(__file__).resolve().parent.parent.parent.parent  # was: ...parent.parent.parent (pre-Phase-6 — substrate moved into substrate/, added one more .parent to reach repo root)
        / "tools" / "qou-substrate" / "python"
    )
    if _QOU_SUBSTRATE_PYTHON.is_dir() and str(_QOU_SUBSTRATE_PYTHON) not in sys.path:
        sys.path.insert(0, str(_QOU_SUBSTRATE_PYTHON))

from qou_substrate.precision import *  # noqa: F401,F403,E402
from qou_substrate.precision import (  # noqa: F401,E402
    _env_int,
)
