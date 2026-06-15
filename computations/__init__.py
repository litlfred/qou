"""folio-assistant/computations — root namespace for the QOU
compute scripts.

Phase 0 of the subdirectory refactor (see
[`docs/proposals/computations-subdirectory-refactor.md`](../../docs/proposals/computations-subdirectory-refactor.md)).

This `__init__.py` is intentionally minimal: it makes the directory
a regular package so that subdirectories (`probes/`, `substrate/`,
`habiro/`, etc.) introduced in later phases are importable as
`folio_assistant.computations.<subdir>.<module>` when needed by
external tooling, while leaving the flat-namespace pattern
(`from q_parameter import Q`, `from witness_base import
WitnessBuilder`, …) intact for in-repo scripts via the path bridge
in `_path_bridge.py`.

Adding this file is a no-op for every existing import pattern in
the repo:

  • `python3 folio-assistant/computations/X.py` keeps working —
    Python prepends the script's dir to sys.path automatically.
  • `from X import Y` from a sibling script keeps working — that
    dir is already on sys.path from the run above.
  • Tools that scan `folio-assistant/computations/*.py` (audit-
    wiring, witness-pipeline.yml, run-pipeline.py, …) keep
    finding every script; `__init__.py` doesn't change directory
    listing semantics.
"""
