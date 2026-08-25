#!/usr/bin/env python3
"""Which Wedderburn blocks the Markov trace can actually see.

## The word this module exists to supply

A **block** is a Wedderburn component `λ ⊢ n` of `H_n(q)`. A **channel** is a
block the trace can see. Under the excised convention C those were the same set,
so no code ever needed to tell them apart — and none does. Producers enumerate

    parts = partitions_of(n)

which is a correct *block* list and was, under C, also a correct *channel* list.

Under convention D they come apart. `tr_M` restricted to block `λ` is
`y_λ · χ^λ`, and

    y_λ = 0   for every λ with ℓ(λ) ≥ 3

exactly — the fibre `V` is the two-dimensional fundamental of `SU_q(2)`, so by
Schur–Weyl no partition with three or more rows survives (a two-dimensional fibre
cannot antisymmetrise three ways). Those blocks contribute nothing to any trace,
mass or binding. They are not small. They are absent.

    n     blocks    live    dead
    3        3        2       1
    4        5        3       2
    5        7        3       4
    6       11        4       7

## Why this was invisible

`rho_k_h3a_gg_trajectory.py` priced its LP as

    _yc_floor = 1e-15
    t_λ = 1 / (dim_q(λ) · max(|y_λ χ^λ|, _yc_floor))

with the comment *"Guard against near-zero |y_λ χ^λ| (set to a large finite cost
so the LP naturally avoids that channel)."* Under C that branch never executed.
Under D it executes on every dead channel — 7 of 11 at `n = 6`. A numerical
safety net became the semantic mechanism for excluding dead channels, silently,
by pricing them at `1e15`. The sentinel was then published in a field named
`y_star`, where it reads exactly like a diverging dual. (It fooled the author of
this module for one full report.)

The defect is not the guard. It is that "live channel" had no name, so the guard
was the only place the concept could live.

## The definition, and why it is the weight and not the row count

`is_live` is defined by `y_λ ≠ 0`, **not** by `len(λ) <= 2`.

The row bound is a *consequence* of convention D via Schur–Weyl, not a definition
of observability. Hardcoding it would bake today's convention into what looks
like a structural fact — which is the whole class of mistake this excision has
been unpicking. Defining liveness by the weight keeps it correct if the
convention moves again, and keeps the reason visible at the point of use.

`live_shapes_by_rows` is provided for the cases where the row bound is genuinely
what is wanted (enumerating before any weight is available), and it says in its
name that it is a *consequence*, not the definition.

## Lean

The same statements, proved:
`QOU/QBeta/MarkovGramDegenerate.lean` §LiveChannels —

* `IsLive y i := y i ≠ 0`                        the definition, same choice
* `wedderburnGram y := Matrix.diagonal y`        `G` is diagonal in this basis
* `wedderburnGram_det`                           `det G = ∏ y_λ`
* `wedderburnGram_det_eq_zero_of_dead`           one dead channel kills `det G`
* `wedderburnGram_det_ne_zero_iff_all_live`      `G` inverts **iff** all live
* `wedderburnGram_restrict_live_det_ne_zero`     restricted to live, invertible

So a producer that wants `G⁻¹` is asserting `∀ λ, IsLive λ`, which convention D
denies for every `n ≥ 3`. That is now a statement to check against rather than a
guard to fall through.
"""

from __future__ import annotations

__all__ = [
    "is_live", "live_channels", "dead_channels", "partition_channels",
    "live_shapes_by_rows", "assert_all_live", "DeadChannelError",
]

#: A weight this small is taken as dead. Convention D gives exact zeros
#: symbolically, but a float/mpf pipeline can deliver 1e-300 instead; treating
#: that as live is how a dead channel gets a cost of 1e300 rather than being
#: excluded. Deliberately far below any live weight — the smallest live weight
#: at n = 3 is y_(2,1) ≈ 0.247.
DEAD_TOL = 1e-30


class DeadChannelError(ValueError):
    """A dead channel reached code that requires a live one.

    Raised rather than absorbed. The pattern this replaces is a cost floor that
    silently prices the channel out — which produces a plausible-looking number
    instead of a stack trace, and that number then gets published.
    """


def is_live(y_lambda, tol: float = DEAD_TOL) -> bool:
    """Can the trace see this block? `y_λ ≠ 0`.

    Accepts float, mpmath.mpf or sympy — anything `abs()` and a comparison work
    on. Defined by the weight, not by the row count; see the module docstring.
    """
    try:
        return abs(float(y_lambda)) > tol
    except (TypeError, ValueError):
        return bool(y_lambda != 0)


def partition_channels(shapes, weights, tol: float = DEAD_TOL):
    """Split `shapes` into (live, dead) using `weights`.

    `weights` is a mapping `shape -> y_λ`, or a callable `shape -> y_λ`.
    Returns two lists, order preserved, so a caller can report the dead ones
    rather than merely skip them.
    """
    get = weights if callable(weights) else weights.__getitem__
    live, dead = [], []
    for s in shapes:
        (live if is_live(get(s), tol) else dead).append(s)
    return live, dead


def live_channels(shapes, weights, tol: float = DEAD_TOL):
    """The blocks the trace can see."""
    return partition_channels(shapes, weights, tol)[0]


def dead_channels(shapes, weights, tol: float = DEAD_TOL):
    """The blocks the trace cannot see. Worth reporting, not just dropping."""
    return partition_channels(shapes, weights, tol)[1]


def live_shapes_by_rows(shapes, max_rows: int = 2):
    """Blocks with at most `max_rows` rows.

    A CONSEQUENCE of convention D (Schur–Weyl on a two-dimensional fibre), not
    the definition of liveness — hence the name. Use `live_channels` when the
    weights are available; use this only when they are not, and expect it to
    need revisiting if the fibre dimension ever changes.
    """
    return [s for s in shapes if len(tuple(s)) <= max_rows]


def assert_all_live(shapes, weights, context: str = "", tol: float = DEAD_TOL):
    """Raise if any block is dead. For code that genuinely requires `G⁻¹`.

    `wedderburnGram_det_ne_zero_iff_all_live` says inverting the full Wedderburn
    Gram is *equivalent* to every channel being live. A producer that inverts it
    should say so here and fail loudly under convention D, rather than invert a
    singular matrix or lean on a floor.
    """
    _, dead = partition_channels(shapes, weights, tol)
    if dead:
        raise DeadChannelError(
            f"{context + ': ' if context else ''}"
            f"{len(dead)} of {len(list(shapes))} blocks are dead under the "
            f"production trace convention — {[list(d) for d in dead]}. "
            "det G = 0 exactly (MarkovGramDegenerate.wedderburnGram_det_eq_zero_of_dead), "
            "so the full Wedderburn Gram is singular and G^-1 does not exist. "
            "Restrict to live_channels(...) — that is H_n/rad = TL_n — or, if "
            "this code really needs all blocks, it needs a different trace."
        )


if __name__ == "__main__":  # pragma: no cover - self-check
    import sys
    sys.path[:0] = [".", "hecke", "substrate"]
    from murnaghan_nakayama import partitions_of  # noqa: E402
    from wedderburn_jones_markov import y_lambda_at  # noqa: E402

    Q0 = 1.1099785827513808075916690956107688798744991218736
    print("block vs channel under the production convention\n")
    print(f"  {'n':>2}  {'blocks':>6}  {'live':>4}  {'dead':>4}   dead shapes")
    for n in (3, 4, 5, 6):
        shapes = [tuple(p) for p in partitions_of(n)]
        try:
            w = {tuple(k): v for k, v in y_lambda_at(n, q_val=Q0).items()}
        except Exception as exc:                       # noqa: BLE001
            print(f"  {n:>2}  weights unavailable: {exc}")
            continue
        live, dead = partition_channels(shapes, w)
        print(f"  {n:>2}  {len(shapes):>6}  {len(live):>4}  {len(dead):>4}   "
              f"{[list(d) for d in dead]}")
        by_rows = live_shapes_by_rows(shapes)
        assert set(live) == set(by_rows), (
            f"n={n}: weight-defined live set {live} disagrees with the "
            f"row-count consequence {by_rows} — one of them is wrong")
    print("\n  weight-defined liveness agrees with the <=2-row consequence at "
          "every n checked.")
