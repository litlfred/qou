"""Path bridge — preserves flat-namespace imports across the
subdirectory refactor.

After [Phase 1+ of the subdirectory
refactor](../../docs/proposals/computations-subdirectory-refactor.md),
compute scripts live in cluster directories
(`probes/`, `habiro/`, `markov/`, `substrate/`, …) but the
existing 794-file cross-import surface uses bare-name imports:

    from q_parameter import Q
    from witness_base import WitnessBuilder
    from A_operator_extract_general import ...

This module, when imported, ensures every cluster subdirectory
of `folio-assistant/computations/` is on `sys.path`, so bare-name
imports continue to resolve regardless of which subdirectory the
importer or importee lives in. Skips `_deprecated/`,
`__pycache__/`, `data/`, and any other leading-underscore /
dot-prefixed directory by convention.

USAGE — every moved script begins with this 4-line bootstrap:

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    import _path_bridge  # noqa: F401

The first 3 lines add `folio-assistant/computations/` to sys.path
so that this module (`_path_bridge`) is findable. The fourth line
loads this module, which then adds every cluster subdir to
sys.path.

Why this pattern (instead of `from . import _path_bridge`)?
Python's relative-import resolution requires the script to be
loaded *as part of a package* — which `python3 path/to/script.py`
direct invocation does NOT provide (Python loads the script as
`__main__`, with `__package__ == None`). The CI workflows + the
content-block citations all use direct invocation, so the
relative-import form raises `ImportError: attempted relative
import with no known parent package`. The 4-line absolute-path
bootstrap above works for both `python3 path/script.py` AND
`python3 -m folio_assistant.computations.<cluster>.<script>`.

Idempotent: re-running the bridge is a no-op (each subdir is
checked against `sys.path` before insertion). Safe to import
from multiple subdirs in the same Python session.
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent


def _add_to_path(p: Path) -> None:
    s = str(p)
    if s not in sys.path:
        sys.path.insert(0, s)


# 1. Add the package root itself (so bare-name imports like
#    `from q_parameter import Q` work for the substrate cluster
#    and any remaining root-level scripts).
_add_to_path(_HERE)

# 2. Add every regular-package cluster subdirectory (so cross-
#    cluster bare-name imports work — e.g. a script in `probes/`
#    importing `from <substrate-module> import X` finds it once
#    `substrate/` is on sys.path).
#
#    Filter out: leading-underscore dirs (`_deprecated`,
#    `__pycache__`), leading-dot dirs, and any dir without
#    `__init__.py` (so untracked tmp dirs don't pollute sys.path).
for _child in _HERE.iterdir():
    if not _child.is_dir():
        continue
    name = _child.name
    if name.startswith("_") or name.startswith("."):
        continue
    if not (_child / "__init__.py").is_file():
        continue
    _add_to_path(_child)
