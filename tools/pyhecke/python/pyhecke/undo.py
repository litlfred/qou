"""Track B — word-shortcut undo infrastructure.

Every composite word in the Hecke confinement hierarchy can be
re-expanded to a lower level, ultimately to the quark (level 1)
primitive. This module provides a single dispatching entrypoint
`undo_to_quark(level, …)` so every call site that applies a shortcut
has an explicit, auditable undo.

Level hierarchy (per INFRASTRUCTURE-AUDIT.md)::

  1 — quark                 (bare Hecke generator at strand level)
  2 — nucleon               (B_3 × 3 quarks + gluon self-coupling)
  3 — atom (nucleon-level)  (Z + N nucleons + inter-nucleon + electrons)
  4 — shell-magic           (closed-shell atom composite)
  5 — cross-shell           (shell-straddling composite)
  6 — atom-electron         (atom + electron cloud)
  7 — molecule              (Σ atoms + covalent bonds)

Currently implemented:

  2 → 1:   `nucleon_gen_chains(quarks)` from hecke_core (existing)
  3 → 2:   `atom_gen_chains(Z, N)` from hecke_core (existing)

Missing (returns NotImplementedError with an actionable message):

  4 → 3, 5 → 3, 6 → 3, 7 → 3

These will be filled by M3 Track B/C work as the shell and molecular
structure definitions land.
"""

from __future__ import annotations

from typing import Any

from . import _legacy  # noqa: F401


LEVEL_NAMES: dict[int, str] = {
    1: "quark",
    2: "nucleon",
    3: "atom",
    4: "shell-magic",
    5: "cross-shell",
    6: "atom-electron",
    7: "molecule",
}


def level_name(level: int) -> str:
    """Return the human-readable name of a confinement level."""
    if level not in LEVEL_NAMES:
        raise ValueError(
            f"unknown level {level!r}; expected one of {sorted(LEVEL_NAMES)}"
        )
    return LEVEL_NAMES[level]


# ── Level 2 → 1 : nucleon → quarks ─────────────────────────────────────

def undo_nucleon_to_quarks(quarks: list[str]) -> tuple[list, list]:
    """Expand a nucleon (level 2) to its quark-level crossing chains.

    Delegates to hecke_core.nucleon_gen_chains. Returns (g0_chain,
    g1_chain) — per-generator lists of (c, d) tuples.

    Parameters
    ----------
    quarks : list[str]
        Three-element list drawn from {"u", "d"}. For a proton use
        ["u", "u", "d"]; for a neutron ["u", "d", "d"].
    """
    from hecke_core import nucleon_gen_chains  # type: ignore[import-not-found]
    return nucleon_gen_chains(quarks)


# ── Level 3 → 2 : atom → nucleons ──────────────────────────────────────

def undo_atom_to_nucleons(Z: int, N: int) -> tuple[list, list]:
    """Expand an atom (level 3) to its per-generator nucleon chains.

    Delegates to hecke_core.atom_gen_chains. Returns (g0_chain,
    g1_chain) including intra-nucleon, inter-nucleon, and
    electron-nucleus crossings.
    """
    from hecke_core import atom_gen_chains  # type: ignore[import-not-found]
    return atom_gen_chains(Z, N)


# ── Levels 4-7 : awaiting Track B/C implementation ────────────────────

# Track B milestone names for levels 4-7. Each entry is the human name
# used in the NotImplementedError message; the dispatcher below
# produces the actual exception so there is no per-level stub to keep
# in sync.
_PENDING_LEVELS: dict[int, str] = {
    4: "shell-magic",
    5: "cross-shell",
    6: "atom-electron",
    7: "molecule",
}


def _raise_pending(level: int) -> None:
    """Raise a ``NotImplementedError`` for a Track B/C level that has
    not yet been implemented. Centralised so every pending level gives
    a consistent message + pointer to the audit doc."""
    raise NotImplementedError(
        f"undo: level {level} → 3 ({_PENDING_LEVELS[level]}) is not "
        "yet implemented. See "
        "folio-assistant/computations/INFRASTRUCTURE-AUDIT.md "
        "section 'Track B: Shortcut infrastructure'."
    )


# ── Dispatch ───────────────────────────────────────────────────────────

_DISPATCH = {
    2: undo_nucleon_to_quarks,
    3: undo_atom_to_nucleons,
}


def undo_to_quark(level: int, *args: Any, **kwargs: Any) -> Any:
    """Dispatch to the appropriate level-ℓ → level-(ℓ-1) expansion.

    For levels 4-7 the expansion is to level 3 (atom-level NF), not
    all the way to the quark: the hierarchy flattens at level 3 for
    now because atomic composites compose at that layer. A full
    atom-to-quark expansion is available by calling
    ``undo_atom_to_nucleons(...)`` on the result for levels 3+.

    Parameters
    ----------
    level : int
        Source level (2..7).

    Returns
    -------
    The expansion as returned by the per-level helper. Shape depends
    on the level:

      - 2 → 1 : ``(g0_chain, g1_chain)`` — see :func:`undo_nucleon_to_quarks`
      - 3 → 2 : ``(g0_chain, g1_chain)`` — see :func:`undo_atom_to_nucleons`
      - 4..7  : ``NotImplementedError`` (Track B/C pending)
    """
    if level in _DISPATCH:
        return _DISPATCH[level](*args, **kwargs)
    if level in _PENDING_LEVELS:
        _raise_pending(level)
    raise ValueError(
        f"undo_to_quark: level must be 2..7, got {level!r}"
    )


def is_implemented(level: int) -> bool:
    """True if `undo_to_quark(level, ...)` will succeed for well-formed input."""
    return level in (2, 3)
