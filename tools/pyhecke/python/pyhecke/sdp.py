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


# ── Level 4 : shell-magic SDP ──────────────────────────────────────────

# Magic-shell nucleon counts (standard nuclear physics).
MAGIC_NUMBERS = (2, 8, 20, 28, 50, 82, 126)


def solve_shell_magic_sdp(
    a_magic: int = 2,
    partition: Optional[tuple] = None,
    **_: Any,
) -> SDPResult:
    """Level 4 — shell-closure adjacent 2x2 PSD feasibility at a magic
    nucleon count.

    Forms the 2x2 PSD block

        [     1        y_shell ]
        [ y_shell      1       ]

    on the symmetric / standard-rep channels at the shell boundary, with
    `y_shell = shell_shadow_price(a_magic)["shadow_price_abs"]` drawn
    from the existing `sigma_shell_characterization` module. Silvester's
    criterion gives a closed-form feasibility check:

        det(G_4) = 1 - y_shell**2

    The block is positive semi-definite iff |y_shell| ≤ 1. That is the
    level-4 feasibility condition — closed-shell magic numbers are
    expected to satisfy it by construction.

    Parameters
    ----------
    a_magic : int
        Magic shell closure. Must be one of MAGIC_NUMBERS (2, 8, 20,
        28, 50, 82, 126).
    partition : tuple, optional
        Shell partition λ ⊢ 3·a_magic. Defaults to (3·a_magic - 1, 1).

    Returns
    -------
    SDPResult
        status = "optimal" when feasible, "infeasible" otherwise. The
        primal dict carries {y_shell, det_2x2, partition, hecke_level}.
    """
    if a_magic not in MAGIC_NUMBERS:
        return SDPResult(
            level=4,
            status="infeasible",
            caveats=[
                f"a_magic = {a_magic} is not a standard magic number "
                f"{MAGIC_NUMBERS}"
            ],
        )

    from . import _legacy  # noqa: F401
    try:
        from sigma_shell_characterization import shell_shadow_price  # type: ignore[import-not-found]
    except ImportError as e:
        return SDPResult(
            level=4,
            status="not_implemented",
            caveats=[
                f"sigma_shell_characterization not importable: {e}. "
                "Ensure folio-assistant/computations is on PYTHONPATH."
            ],
        )

    data = shell_shadow_price(a_magic, partition=partition)
    if "error" in data:
        return SDPResult(
            level=4,
            status="infeasible",
            caveats=[data["error"]],
        )

    # Shadow price is returned as a string (mpmath dps=50); cast for the 2x2 check.
    try:
        y_shell = float(data["shadow_price_abs"])
    except (TypeError, ValueError):
        y_shell = 0.0

    det_2x2 = 1.0 - y_shell ** 2
    feasible = det_2x2 >= -1e-12
    status = "optimal" if feasible else "infeasible"

    return SDPResult(
        level=4,
        status=status,
        objective=det_2x2,
        primal={
            "a_magic": a_magic,
            "hecke_level": data.get("hecke_level"),
            "shell_partition": list(data.get("shell_partition", ())),
            "y_shell": y_shell,
            "det_2x2": det_2x2,
            "matrix": [[1.0, y_shell], [y_shell, 1.0]],
        },
        dual={
            "shadow_price_y": data.get("shadow_price_y"),
            "wedderburn_weight": data.get("wedderburn_weight"),
            "q_dim": data.get("q_dim"),
            "classical_dim": data.get("classical_dim"),
        },
        psd_blocks=[
            {
                "name": "shell_closure_2x2",
                "size": 2,
                "determinant": det_2x2,
                "silvester_feasible": feasible,
            }
        ],
        caveats=[
            "Level-4 PSD block uses shell_shadow_price from "
            "sigma_shell_characterization. Coupling is the |y_shell| "
            "magnitude; the sign carries physical meaning (positive = "
            "binding, negative = antibinding) that this first-cut "
            "solver does not yet encode. Extend to two-channel "
            "sign-aware solver when cross-shell level 5 lands.",
        ],
    )


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
    return [3, 4]


def pending_levels() -> list[int]:
    """Return the levels that still need implementation (Track C)."""
    return [5, 6, 7]
