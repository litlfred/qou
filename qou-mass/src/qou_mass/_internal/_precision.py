"""_precision — back-compat shim. The canonical module is now
``qou_substrate.precision`` in ``tools/qou-substrate/``.

This file is a thin re-export so the 121 scripts in this directory that
do ``from _precision import set_compute_dps, fmt`` keep working without
modification. New code should import from ``qou_substrate`` directly
once ``qou-substrate`` is on PyPI.

See ``docs/workplans/2026-05-24-library-reuse-production-readiness.md``
Tier-2 item 2a for the promotion rationale.


    IMPORTING THIS MODULE DOES NOT SET `mp.dps`
    -------------------------------------------
    Measured: `import _precision` leaves `mpmath.mp.dps` at mpmath's default
    **15**, i.e. float64-grade.  `set_compute_dps()` must be called explicitly
    before any `mpf` arithmetic you intend to be high-precision.

    This matters because `fmt()` will happily render a 53-bit value out to the
    full serialization width, so the number *reads* as measured while carrying
    ~15 significant digits.  The float64-padding ratchet is what catches it
    (worked case: `nonet_mixing_purity.py`, PR #5023).

    Note the mirror hazard in the other direction: a module that calls
    `set_compute_dps(N)` at module scope ASSIGNS the global `mp.dps` as an
    import side effect, which can LOWER a caller already running higher.
    `y_lambda_su_n` did exactly this (`set_compute_dps(50)`) until 2026-10-13;
    it now builds its constants inside a local `mp.workdps`.  Library modules
    should do the same.  So an unset dps can be silently too low, and an
    import-assigned one silently lower than the caller set.  Both present as
    "the number looks fine, at the wrong precision".
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
del _sys, _Path

import sys
from pathlib import Path

try:
    import qou_substrate.precision as _qs_precision  # noqa: F401
except ImportError:
    # SEARCH upward for the substrate checkout rather than counting `.parent`s.
    # A fixed count cannot be right for both layouts this file lives in:
    #   computations/substrate/_precision.py            -> repo root is 3 up
    #   qou-mass/src/qou_mass/_internal/_precision.py   -> repo root is 5 up
    # (the vendor sync copies this file verbatim into a flatter tree). The
    # hardcoded 4 was wrong in BOTH: it resolved to the parent of the repo in
    # the source layout and to `qou-mass/tools/...` in the vendored one, so the
    # fallback never fired anywhere. It only stayed invisible because
    # `import _path_bridge` normally puts the substrate on sys.path first --
    # and the vendor sync STRIPS that import, which is exactly where it bit.
    _QOU_SUBSTRATE_PYTHON = None
    for _anc in Path(__file__).resolve().parents:
        _cand = _anc / "tools" / "qou-substrate" / "python"
        if _cand.is_dir():
            _QOU_SUBSTRATE_PYTHON = _cand
            break
    if _QOU_SUBSTRATE_PYTHON is not None and str(_QOU_SUBSTRATE_PYTHON) not in sys.path:
        sys.path.insert(0, str(_QOU_SUBSTRATE_PYTHON))

from qou_substrate.precision import *  # noqa: F401,F403,E402
from qou_substrate.precision import (  # noqa: F401,E402
    _env_int,
)
