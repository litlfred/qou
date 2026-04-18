"""Legacy-compat shim.

Re-exports everything from the installed `pyhecke` package so scripts
that do `sys.path.insert(0, folio-assistant/computations)` continue to
work during the M1 carve-out.

After M1:
    from pyhecke import G, G_INV, hm_exact  # works whether pyhecke is
                                            # pip-installed or this shim
                                            # is picked up by sys.path

Removal schedule: retained through M2; removed in M3 once all callers
have migrated to the proper package import.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path


def _ensure_pyhecke_importable() -> None:
    """If the `pyhecke` package is not installed, add its source tree
    to sys.path so the fallback import works from a source checkout."""
    try:
        import pyhecke  # type: ignore[import-not-found]  # noqa: F401
        return
    except ImportError:
        pass

    # Walk up looking for tools/pyhecke/python/
    here = Path(__file__).resolve()
    for anc in here.parents:
        cand = anc / "tools" / "pyhecke" / "python"
        if (cand / "pyhecke" / "__init__.py").is_file():
            sys.path.insert(0, str(cand))
            return


_ensure_pyhecke_importable()

from pyhecke import *  # type: ignore[import-not-found]  # noqa: E402, F401, F403
from pyhecke import __version__ as __pyhecke_version__  # noqa: E402, F401
