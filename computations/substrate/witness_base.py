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
    # SEARCH upward rather than counting `.parent`s. A fixed count cannot be
    # right for both layouts this shim lives in: 3 up in computations/substrate/,
    # 5 up once the vendor sync flattens it into qou-mass/.../_internal/. The
    # hardcoded 4 was wrong in BOTH, so the fallback never fired anywhere; it
    # only stayed invisible because `import _path_bridge` normally puts the
    # substrate on sys.path first — and the vendor sync STRIPS that import.
    _QOU_SUBSTRATE_PYTHON = None
    for _anc in Path(__file__).resolve().parents:
        _cand = _anc / "tools" / "qou-substrate" / "python"
        if _cand.is_dir():
            _QOU_SUBSTRATE_PYTHON = _cand
            break
    if _QOU_SUBSTRATE_PYTHON is not None and str(_QOU_SUBSTRATE_PYTHON) not in sys.path:
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
    # `_EPHEMERAL_META_FIELDS` was missing from this hand-listed set, so
    # `from witness_base import _EPHEMERAL_META_FIELDS` failed in-repo —
    # `import *` above does not pick up underscore-prefixed names, which is
    # the whole reason this explicit block exists.
    #
    # Nothing caught it because the one consumer,
    # tools/qou-substrate/tests/test_ephemeral_mask_sync.py, reads the name
    # from the VENDORED qou-mass mirror, and that mirror was a stale copy of
    # the pre-shim implementation which still defined it directly. The test
    # exists precisely to detect mirror divergence, and it was green only
    # because the mirror had not been updated: the drift was masking the
    # defect the test was written to find. Generating the mirror
    # (scripts/sync-qou-mass-vendor.py) made it faithful and the failure
    # surfaced immediately.
    _EPHEMERAL_META_FIELDS,
)
