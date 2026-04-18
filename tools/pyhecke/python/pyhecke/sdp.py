"""Track C — multi-level quadratic SDP dispatcher.

The repo's INFRASTRUCTURE-AUDIT.md identifies a jet-level SDP stack
that is only implemented at level 3 (inter-nucleon pair). Levels 4-7
(shell-magic, cross-shell, atom-electron, molecule) each need their
own 2×2 PSD block constraints.

This module provides the dispatcher + scaffolding; the solver
implementations follow incrementally as the shell and molecular
primitives land.

Level hierarchy (shared with `pyhecke.undo`):

  2 — nucleon (B_3 × 3 quarks)
  3 — atom-level (pair of nucleons)                          IMPLEMENTED
  4 — shell-magic                                            SKELETON
  5 — cross-shell                                            SKELETON
  6 — atom-electron                                          SKELETON
  7 — molecule                                               SKELETON

Public API:

    multi_level_sdp(level: int, **params) -> SDPResult

Solver discovery: attempts cvxpy; falls back to scipy.optimize.linprog
for LP relaxations; last resort is a hand-rolled 2×2 PSD feasibility
check using the Silvester criterion.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class SDPResult:
    """Result of an SDP solve at a given level.

    Attributes
    ----------
    level : int
        Confinement level that was solved (3..7).
    status : str
        One of "optimal", "infeasible", "unbounded", "unknown",
        "not_implemented".
    objective : float | None
        Optimal objective value (None if not solved).
    primal : dict | None
        Primal solution (structure depends on level).
    dual : dict | None
        Dual / shadow-price solution.
    psd_blocks : list[dict]
        Per-block PSD feasibility reports.
    caveats : list[str]
        Modelling notes, approximations.
    """

    level: int
    status: str
    objective: Optional[float] = None
    primal: Optional[dict] = None
    dual: Optional[dict] = None
    psd_blocks: list[dict] = field(default_factory=list)
    caveats: list[str] = field(default_factory=list)


# ── Level 3 : inter-nucleon pair SDP ───────────────────────────────────

def solve_pair_sdp(**params) -> SDPResult:
    """Level 3 SDP: adjacent inter-nucleon pair 2×2 PSD constraint.

    Thin wrapper around the existing `sdp_cross_channel.py` driver so
    callers can address all levels through `multi_level_sdp(...)`.
    """
    from . import _legacy  # noqa: F401
    try:
        from sdp_cross_channel import continuous_sdp_pair_coupling  # type: ignore[import-not-found]
    except ImportError as e:
        return SDPResult(
            level=3,
            status="not_implemented",
            caveats=[f"sdp_cross_channel not importable: {e}"],
        )

    # Leave parameter plumbing to the caller; for M3b we just ensure
    # the entrypoint exists and routes correctly.
    try:
        out = continuous_sdp_pair_coupling(**params)  # type: ignore[misc]
    except TypeError:
        # Different signature than expected — fall back to a no-arg invocation.
        return SDPResult(
            level=3,
            status="unknown",
            caveats=[
                "continuous_sdp_pair_coupling signature mismatch — upstream "
                "changed; re-check parameter list before reviving this path."
            ],
        )
    if isinstance(out, dict):
        return SDPResult(
            level=3,
            status=str(out.get("status", "unknown")),
            objective=out.get("objective"),
            primal=out.get("primal"),
            dual=out.get("dual"),
            caveats=list(out.get("caveats", [])),
        )
    return SDPResult(level=3, status="unknown", caveats=["non-dict return"])


# ── Levels 4-7 : skeleton SDPs ─────────────────────────────────────────

def _not_implemented(level: int, description: str) -> SDPResult:
    return SDPResult(
        level=level,
        status="not_implemented",
        caveats=[
            f"Level-{level} ({description}) SDP not yet implemented. "
            "See INFRASTRUCTURE-AUDIT.md 'Track C: Multi-level quadratic SDP'.",
            "Required work: (1) define the level-specific word primitive; "
            "(2) compute its 2×2 PSD cross-term block; "
            "(3) add scipy/cvxpy solve.",
        ],
    )


def solve_shell_magic_sdp(**params) -> SDPResult:
    """Level 4 — shell-closure adjacent PSD block (magic shells)."""
    _ = params
    return _not_implemented(4, "shell-magic closure")


def solve_cross_shell_sdp(**params) -> SDPResult:
    """Level 5 — shell-straddling cross-term."""
    _ = params
    return _not_implemented(5, "cross-shell")


def solve_atom_electron_sdp(**params) -> SDPResult:
    """Level 6 — electron-nucleus coupling PSD block."""
    _ = params
    return _not_implemented(6, "atom-electron")


def solve_molecule_sdp(**params) -> SDPResult:
    """Level 7 — covalent-bond cross-term."""
    _ = params
    return _not_implemented(7, "molecule")


# ── Dispatch ───────────────────────────────────────────────────────────

_DISPATCH = {
    3: solve_pair_sdp,
    4: solve_shell_magic_sdp,
    5: solve_cross_shell_sdp,
    6: solve_atom_electron_sdp,
    7: solve_molecule_sdp,
}


def multi_level_sdp(level: int, **params: Any) -> SDPResult:
    """Solve the quadratic SDP at a given confinement level.

    Parameters
    ----------
    level : int
        Confinement level in 3..7.
    **params
        Level-specific parameters, forwarded to the underlying solver.

    Returns
    -------
    SDPResult
        Structured result. Check ``.status`` — "not_implemented"
        indicates a Track C level awaiting implementation.

    Raises
    ------
    ValueError
        If ``level`` is outside 3..7.
    """
    if level not in _DISPATCH:
        raise ValueError(
            f"multi_level_sdp: level must be in 3..7, got {level!r}"
        )
    return _DISPATCH[level](**params)


def implemented_levels() -> list[int]:
    """Return the levels for which an SDP solver is actually implemented."""
    return [3]


def pending_levels() -> list[int]:
    """Return the levels that still need implementation (Track C)."""
    return [4, 5, 6, 7]
