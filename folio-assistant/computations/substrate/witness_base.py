"""witness_base — back-compat shim. The canonical module is now
``qou_substrate.witness`` in ``tools/qou-substrate/``.

This file is a thin re-export so the 362 scripts in this directory that
do ``from witness_base import WitnessBuilder`` keep working without
modification. New code should import from ``qou_substrate.witness``
directly once ``qou-substrate`` is on PyPI.

The shim adds ``tools/qou-substrate/python/`` to ``sys.path`` so it
works in the in-repo development environment before the package is
pip-installed.

Background: qou-substrate is Tier-2 item 2a of the library-reuse
workplan; promoting this module + ``_precision.py`` + ``q_parameter.py``
into a published package reaches 67% of QOU compute scripts. See
``docs/workplans/2026-05-24-library-reuse-production-readiness.md``.
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

# Bootstrap qou_substrate into sys.path when it isn't already installed
# (the editable install path or PyPI install will short-circuit this).
try:
    import qou_substrate.witness as _qs_witness  # noqa: F401
except ImportError:
    _QOU_SUBSTRATE_PYTHON = (
        Path(__file__).resolve().parent.parent.parent.parent  # was: ...parent.parent.parent (pre-Phase-6 — substrate moved into substrate/, added one more .parent to reach repo root)
        / "tools" / "qou-substrate" / "python"
    )
    if _QOU_SUBSTRATE_PYTHON.is_dir() and str(_QOU_SUBSTRATE_PYTHON) not in sys.path:
        sys.path.insert(0, str(_QOU_SUBSTRATE_PYTHON))

# Re-export everything public.
from qou_substrate.witness import *  # noqa: F401,F403,E402

# Re-export private helpers a handful of older scripts may use directly
# (the e0_calibration_audit comment cites _witnesses_substantively_equal;
# the others round out the previously-importable surface).
from qou_substrate.witness import (  # noqa: F401,E402
    _repo_root,
    _git_head_sha,
    _git_file_sha,
    _strip_ephemeral_fields,
    _witnesses_substantively_equal,
)
