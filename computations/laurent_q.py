"""laurent_q — back-compat re-export shim.

The canonical implementation moved to pyhecke.laurent_q per workplan
v2 item 2c (PR #1136 / 2c). This file is a thin shim that keeps
from laurent_q import X working unchanged for the existing
external importers in computations/.

For new code, import directly from pyhecke:

    from pyhecke.laurent_q import ...

(works in both the editable-install dev path and after
pip install pyhecke).
"""

from __future__ import annotations

# pyhecke is on sys.path via the bootstrap in hecke_core.py (which
# almost every consumer already imports). For consumers that don't
# import hecke_core, fall back to adding the path here.
try:
    from pyhecke.laurent_q import *  # noqa: F401, F403
except ImportError:
    import sys as _sys
    from pathlib import Path as _Path
    # SEARCH upward for the pyhecke checkout rather than counting `..`s.
    # The hardcoded `../..` was wrong in BOTH layouts this file lives in:
    #   computations/laurent_q.py                          -> tools/ is 1 up,
    #       so `../..` walked out of the repo entirely;
    #   qou-mass/src/qou_mass/_internal/laurent_q.py       -> tools/ is 4 up.
    # `os.path.isdir` was therefore False in both, so the fallback never
    # fired anywhere -- invisible because `_path_bridge` normally puts
    # pyhecke on sys.path first, and the vendor sync STRIPS that import.
    # Same defect class as the fixed `.parent` counts in
    # `substrate/_precision.py` (bean qou-rug0).
    _PYHECKE_PATH = None
    for _anc in _Path(__file__).resolve().parents:
        _cand = _anc / "tools" / "pyhecke" / "python"
        if _cand.is_dir():
            _PYHECKE_PATH = str(_cand)
            break
    if _PYHECKE_PATH is not None and _PYHECKE_PATH not in _sys.path:
        _sys.path.insert(0, _PYHECKE_PATH)
    from pyhecke.laurent_q import *  # noqa: F401, F403
