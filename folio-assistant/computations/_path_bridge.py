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

This bridge ensures `folio-assistant/computations/` (the package
root) stays on `sys.path`, so bare-name imports continue to
resolve regardless of which subdirectory the importer or importee
lives in. Every moved script's FIRST import is:

    from . import _path_bridge  # noqa: F401

That `from . import` form requires `__init__.py` in both the
moved-script's subdir and the package root (provided by Phase 0).

Idempotent: re-running the bridge is a no-op (`sys.path` is
checked before mutation). Safe to import from multiple subdirs in
the same Python session.
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent

if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))
