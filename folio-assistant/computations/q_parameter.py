"""q_parameter — back-compat shim. The canonical module is now
``qou_substrate.constants`` in ``tools/qou-substrate/``.

This file is a thin re-export so the 265 scripts in this directory that
do ``from q_parameter import Q, HA, ...`` keep working without
modification. New code should import from ``qou_substrate`` directly
once ``qou-substrate`` is on PyPI.

The substrate parameter is derived from CODATA m_μ/m_e + SnapPy
Vol(4_1); see ``qou_substrate.constants`` for the full derivation
docstring.

Promotion rationale: ``docs/workplans/2026-05-24-library-reuse-production-readiness.md``
Tier-2 item 2a.
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import qou_substrate.constants as _qs_constants  # noqa: F401
except ImportError:
    _QOU_SUBSTRATE_PYTHON = (
        Path(__file__).resolve().parent.parent.parent
        / "tools" / "qou-substrate" / "python"
    )
    if _QOU_SUBSTRATE_PYTHON.is_dir() and str(_QOU_SUBSTRATE_PYTHON) not in sys.path:
        sys.path.insert(0, str(_QOU_SUBSTRATE_PYTHON))

from qou_substrate.constants import *  # noqa: F401,F403,E402
