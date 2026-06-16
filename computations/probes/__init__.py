"""Probes — cluster of self-contained verification scripts.

Each script in this directory is a `*_probe.py` that:
  • takes no command-line arguments,
  • computes one or more named assertions (typically against
    a published closed form, a numerical reference, or a
    cross-method consistency check),
  • emits exactly one `<slug>.witness.json` next to itself
    on success.

Phase 1 of the subdirectory refactor moves the 99 _probe.py
files from `computations/` flat into this
subdirectory.  See [`docs/proposals/computations-subdirectory-
refactor.md`](../../../docs/proposals/computations-subdirectory-refactor.md).
"""
