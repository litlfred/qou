"""Tests for solver provenance and the false-infeasible rescue.

Both cover the same failure shape the LP-dual arc kept turning up: a check
that is absent rather than failing, so its absence is indistinguishable from
its passing.

  * `provenance()` — producers cherry-pick numeric fields off a result and
    `float()`-cast them, dropping `backend`, `precision_bits` and every
    `*_str` companion at the last step. A witness written that way cannot say
    which solver produced it, so a f64 solve reads exactly like an MPFR one.

  * the rescue — clarabel's interior-point method returns a false
    `infeasible` on cost vectors of large magnitude. `t` appears ONLY in the
    objective, so rescaling it cannot change the feasible set; a verdict that
    flips under rescaling was a numerical artifact. The rescue must correct
    those and must NEVER manufacture feasibility for a genuinely infeasible
    LP.
"""

from __future__ import annotations

import numpy as np
import pytest

from pyhecke.lp_dual_solver import (
    PROVENANCE_STR_FIELDS,
    LpDualResult,
    provenance,
    solve_frobenius_dual_lp,
    solve_operator_selection_lp,
)


def _clarabel_available() -> bool:
    try:
        r = solve_operator_selection_lp(
            np.array([2.0, 1.0]), np.eye(2), 1.0, backend="clarabel"
        )
    except Exception:
        return False
    return r.backend == "clarabel-mpfr"


needs_clarabel = pytest.mark.skipif(
    not _clarabel_available(), reason="clarabel-MPFR binary not built"
)


# ── provenance() ──────────────────────────────────────────────────────


def test_provenance_omits_absent_fields_rather_than_emitting_null():
    """A reader must be able to ask `"backend" in row` and get the truth."""
    bare = LpDualResult(
        x_star=[1.0], y0_star=0.0, y_star=[0.0], active_set=[],
        primal_obj=0.0, dual_obj=0.0, duality_gap=0.0, feasible=True,
    )
    assert provenance(bare) == {}


def test_provenance_accepts_dataclass_and_its_to_dict_identically():
    """Producers hold both forms; a helper that silently returned {} for the
    dict form would be exactly the absent check this exists to prevent."""
    res = LpDualResult(
        x_star=[1.0], y0_star=0.5, y_star=[0.25], active_set=[0],
        primal_obj=1.0, dual_obj=1.0, duality_gap=0.0, feasible=True,
        backend="clarabel-mpfr", precision_bits=167,
        y0_star_str="0.5000000000000000000000000000000000000000000000001",
    )
    assert provenance(res) == provenance(res.to_dict())
    assert provenance(res)["backend"] == "clarabel-mpfr"
    assert provenance(res)["precision_bits"] == 167
    assert provenance(res)["y0_star_str"].startswith("0.5")


def test_provenance_str_fields_tuple_covers_both_result_classes():
    """New `*_str` fields must be picked up here, not in ten producers."""
    for name in ("y0_star_str", "y_star_str", "X_star_str", "eigenvalues_str"):
        assert name in PROVENANCE_STR_FIELDS


# ── the false-infeasible rescue ───────────────────────────────────────


@needs_clarabel
def test_rescue_corrects_false_infeasible_on_large_costs():
    """Costs at the M_bound scale drive clarabel to a spurious infeasible."""
    d = 11
    rng = np.random.default_rng(0)
    t = np.abs(rng.standard_normal(d)) * 1e6 + 1.0
    G, n_target = np.eye(d), 1.0

    ref = solve_operator_selection_lp(t, G, n_target, backend="scipy")
    got = solve_operator_selection_lp(t, G, n_target, backend="clarabel")

    assert ref.feasible, "reference solve must succeed for this test to mean anything"
    assert got.feasible, "clarabel returned a false infeasible; rescue did not fire"
    assert got.rescaled_by_pow2 is not None, "rescue fired but did not record itself"
    assert list(got.active_set) == list(ref.active_set)
    assert got.primal_obj == pytest.approx(ref.primal_obj, rel=1e-12)


@needs_clarabel
def test_rescue_never_manufactures_feasibility():
    """x_i >= -M_bound, so sum(x) >= -d*M_bound. Asking for less is genuinely
    infeasible, and no amount of cost rescaling may change that."""
    d, M = 4, 1.0
    got = solve_operator_selection_lp(
        np.ones(d) * 1e7, np.eye(d), -d * M - 100.0,
        backend="clarabel", M_bound=M,
    )
    assert not got.feasible
    assert got.rescaled_by_pow2 is None


@needs_clarabel
def test_rescue_is_inert_on_a_well_conditioned_solve():
    """No rescue, and no stray field in the serialized row."""
    t = np.array([2.0, 1.0, 1.0])
    G = np.array([[2.0, 1.0, 0.0], [1.0, 3.0, 0.0], [0.0, 0.0, 1.0]])
    got = solve_operator_selection_lp(t, G, 1.0, backend="clarabel")
    assert got.feasible
    assert got.rescaled_by_pow2 is None
    assert "rescaled_by_pow2" not in got.to_dict()


# ── every construction site records its backend ───────────────────────


@needs_clarabel
def test_infeasible_results_still_name_their_solver():
    """An infeasible verdict is a claim about the LP, and the two backends
    disagree on badly-conditioned costs — so the verdict must say who made it.
    Previously the scipy SUCCESS path recorded nothing, which meant only a
    FAILED f64 solve was visible to the float64 gate."""
    d, M = 4, 1.0
    for backend, expected in (("scipy", "scipy-highs"), ("clarabel", "clarabel-mpfr")):
        got = solve_operator_selection_lp(
            np.ones(d), np.eye(d), -d * M - 100.0, backend=backend, M_bound=M,
        )
        assert not got.feasible
        assert got.backend == expected, f"{backend} infeasible verdict is anonymous"


def test_successful_scipy_solve_names_its_backend():
    """`solve_operator_selection_lp`'s scipy path already named itself."""
    got = solve_operator_selection_lp(
        np.array([2.0, 1.0]), np.eye(2), 1.0, backend="scipy",
    )
    assert got.feasible
    assert got.backend == "scipy-highs"


def test_frobenius_dual_lp_success_names_its_backend():
    """The actual hole this closes, and a separate entry point from
    `solve_operator_selection_lp` — testing that one instead would pass
    whether or not this were fixed.

    `solve_frobenius_dual_lp` set `backend` on its INFEASIBLE branch and not
    on its success branch, so a successful f64 solve through it was invisible
    to the float64 gate while only failures were caught. It is public and has
    live callers (`frobenius_repose_probe.py`,
    `all_nuclides_sdp_admissibility.py`).
    """
    # G x = u_demand with G = I makes x = u_demand the unique feasible point,
    # so the solve succeeds and sum(u_demand) is the n_target it must match.
    d = 3
    u_demand = np.array([0.25, 0.5, 0.25])
    got = solve_frobenius_dual_lp(
        np.array([1.0, 2.0, 3.0]), np.eye(d), float(u_demand.sum()), u_demand,
    )
    assert got.feasible, "fixture must reach the SUCCESS branch to test it"
    assert got.backend == "scipy-highs", (
        "successful f64 solve is anonymous — the float64 gate cannot see it"
    )
