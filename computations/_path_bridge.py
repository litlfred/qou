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
of `computations/` is on `sys.path`, so bare-name
imports continue to resolve regardless of which subdirectory the
importer or importee lives in. Skips `_deprecated/`,
`__pycache__/`, `data/`, and any other leading-underscore /
dot-prefixed directory by convention.

USAGE — every moved script begins with this 4-line bootstrap:

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    import _path_bridge  # noqa: F401

The first 3 lines add `computations/` to sys.path
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

_add_to_path(_HERE.parent / "tools" / "qou-substrate" / "python")
# `pyhecke` is the other in-repo package computations/ scripts import by
# bare name, and it was NOT wired here — 35 of the 72 producers that the
# importability audit found unable to run fail on exactly this, and 44 of
# those 72 already import this bridge. Adding the path here fixes them at
# the shared point instead of repeating a 3-line bootstrap 35 times.
_add_to_path(_HERE.parent / "tools" / "pyhecke" / "python")

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
#
#    SORTED, and that is load-bearing rather than cosmetic. `iterdir()`
#    yields in `os.scandir` order — filesystem-dependent, and NOT sorted.
#    Measured on this checkout before the fix, the cluster tail came out
#    `phase5, a_operator, markov, probes, substrate, alpha, audits,
#    habiro, sweeps, qbeta, hecke`. Since `witness_path` returns the FIRST
#    existing match, an unsorted search order means a stem duplicated
#    across two cluster dirs resolves differently on different machines,
#    and can flip on the same machine after unrelated file churn — the
#    worst failure shape for a witness read: silent, and not reproducible
#    from the source. `_HERE` stays first so the package root keeps
#    priority over every cluster; only the tail is ordered.
#
#    Today exactly one duplicated stem is cluster-vs-cluster — the qβ Φ_b
#    two-loop b-dictionary probe, which exists in both `probes/` and
#    `qbeta/` — and `probes` precedes `qbeta` under both the old fs order
#    and the sorted one, so this changes no resolution on this checkout:
#    it removes the nondeterminism, it does not move a number.
#
#    (That stem is described rather than spelled on purpose. The
#    duplicate-stem audit's consumer scan is TEXTUAL, so writing the
#    literal filename here would register this module as one of its
#    "consumers" and pollute the very report that tracks it.)
#    Bean `qou-kcii`.
_WITNESS_DIRS: list[Path] = [_HERE]
for _child in sorted(_HERE.iterdir()):
    if not _child.is_dir():
        continue
    name = _child.name
    if name.startswith("_") or name.startswith("."):
        continue
    if not (_child / "__init__.py").is_file():
        continue
    _add_to_path(_child)
    _WITNESS_DIRS.append(_child)


def witness_path(name: str, prefer_dir: "Path | None" = None) -> Path:
    """Locate a `*.witness.json` / `*.derivation.json` file by
    bare name (no directory prefix). Searches in order:

      1. ``prefer_dir`` — typically ``Path(__file__).parent``,
         so a script's own emitted witness is found in its own
         directory first (post-cluster-refactor convention).
      2. Every cluster subdirectory of
         ``computations/``, then the package
         root.

    Returns the first existing match. If nothing matches, returns
    ``prefer_dir / name`` (or the package root / name when
    ``prefer_dir`` is None) so the caller gets a sensible error
    message pointing at where the witness *would* be written.

    Use this when a moved script needs to LOAD an upstream
    witness produced by a different cluster — replaces the
    pre-refactor ``HERE / "<name>.witness.json"`` idiom, which
    after Phase 4 silently resolved to the wrong cluster dir.
    """
    search: list[Path] = []
    if prefer_dir is not None:
        search.append(prefer_dir)
    for d in _WITNESS_DIRS:
        if d not in search:
            search.append(d)
    for d in search:
        candidate = d / name
        if candidate.exists():
            return candidate

    # LAST RESORT: `_deprecated/`.
    #
    # `_WITNESS_DIRS` skips `_`-prefixed directories on purpose, so a witness
    # moved to `_deprecated/` becomes invisible here and every live reader dies
    # on `FileNotFoundError`. That is not hypothetical:
    # `beta-decay-energy-scale.witness.json` was deprecated while NINE live
    # scripts still read it, and `derived_masses.py` / `q_beta_predicted.py`
    # have been failing outright with "Run the beta-decay-energy-scale compute
    # first" while `derive_e_0_lp_dual_h3.py` could not run at all — its
    # witness sat frozen for three months carrying a maximally-violated duality
    # certificate because nothing could refresh it.
    #
    # `_deprecated/README.md` requires that NOTHING live consume a witness
    # before it moves, and documents the same failure once already
    # (`hecke_core_legacy.py`, moved back out because nine importers depended
    # on it). So this is a policy violation upstream, not a resolution rule —
    # but a resolver that turns it into a crash helps nobody, and a live
    # directory always wins because it is searched first.
    #
    # Deliberately NOT a general un-deprecation: it fires only when no live
    # copy exists, which is precisely the broken-dependency case. Bean
    # `qou/ftuv`.
    deprecated = _HERE / "_deprecated" / name
    if deprecated.exists():
        return deprecated

    return (prefer_dir if prefer_dir is not None else _HERE) / name
