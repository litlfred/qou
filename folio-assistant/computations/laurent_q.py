"""laurent_q — back-compat re-export shim.

The canonical implementation moved to pyhecke.laurent_q per workplan
v2 item 2c (PR #1136 / 2c). This file is a thin shim that keeps
from laurent_q import X working unchanged for the existing
external importers in folio-assistant/computations/.

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
    import os as _os
    import sys as _sys
    _PYHECKE_PATH = _os.path.normpath(
        _os.path.join(_os.path.dirname(__file__), "..", "..", "tools", "pyhecke", "python")
    )
    if _os.path.isdir(_PYHECKE_PATH) and _PYHECKE_PATH not in _sys.path:
        _sys.path.insert(0, _PYHECKE_PATH)
    from pyhecke.laurent_q import *  # noqa: F401, F403
