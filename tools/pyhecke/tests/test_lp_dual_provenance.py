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



# ── the loosened-solve certificate ────────────────────────────────────


@needs_clarabel
def test_rescue_rejects_a_wrong_answer_it_would_otherwise_return():
    """The rescue's own duality gap cannot police it.

    Scaling `t` cannot change the feasible set, but on a cost vector spanning
    1.1 … 1e15 it pushes the small entries to ~1e-15, where a finite-precision
    solver treats them as zero and optimises a DIFFERENT objective. It then
    solves that one well: measured 2026-08-23, the rescue returned
    `primal_obj = 1.4571747644416917` with a relative duality gap of 1.2e-30,
    where the true optimum is 1.2745481388661641. A gap test would pass it.
    Dual feasibility in the ORIGINAL `t` is what rejects it.
    """
    d = 3
    # A cost vector with the shape that breaks it: one entry ~1, one at the
    # 1e-15-floor reciprocal, i.e. 15 orders of dynamic range.
    t = np.array([1.112, 5.0, 1e15])
    got = solve_operator_selection_lp(t, np.eye(d), 1.0, backend="clarabel")
    if got.feasible:
        # If it IS returned, it must at least be dual-feasible in the real t.
        y = np.asarray(got.y_star, dtype=float)
        viol = float(np.max(got.y0_star * np.ones(d) + np.eye(d).T @ y - t))
        assert viol <= 1e-9 * max(abs(got.primal_obj), 1.0), (
            f"accepted a solve whose dual violates the original t by {viol:.3e}"
        )


@needs_clarabel
def test_rescue_still_accepts_the_case_it_was_built_for():
    """Certification must not throw out the correct rescue with the wrong one."""
    d = 11
    rng = np.random.default_rng(0)
    t = np.abs(rng.standard_normal(d)) * 1e6 + 1.0
    ref = solve_operator_selection_lp(t, np.eye(d), 1.0, backend="scipy")
    got = solve_operator_selection_lp(t, np.eye(d), 1.0, backend="clarabel")
    assert ref.feasible and got.feasible, "the correct rescue was rejected"
    assert got.primal_obj == pytest.approx(ref.primal_obj, rel=1e-12)
    assert got.rescaled_by_pow2 is not None


@needs_clarabel
def test_a_small_scale_lp_is_solved_not_declared_infeasible():
    """`tol_gap_abs` / `tol_feas` are ABSOLUTE, so a precision-derived 1e-40
    is unreachable on a problem whose optimum is ~1e-9. That returned
    `InsufficientProgress`, which the Rust collapsed into `feasible=false`,
    and 72 NaNs went into a committed witness as though the LP had no
    solution. The tolerance ladder loosens instead of ruling."""
    d = 28
    rng = np.random.default_rng(7)
    A = rng.standard_normal((d, d))
    G = A @ A.T + d * np.eye(d)          # well-conditioned Gram
    t = (np.abs(rng.standard_normal(d)) + 0.5) * 1e-5
    n_target = 3.19e-4
    ref = solve_operator_selection_lp(t, G, n_target, M_bound=0.0, backend="scipy")
    got = solve_operator_selection_lp(t, G, n_target, M_bound=0.0, backend="clarabel")
    if ref.feasible:
        assert got.feasible, (
            "small-scale LP declared infeasible; the tolerance ladder did not "
            "loosen, so 'solver gave up' is again reading as 'no solution'"
        )
        assert got.primal_obj == pytest.approx(ref.primal_obj, rel=1e-5)


# ── the singular Gram ─────────────────────────────────────────────────


def test_pseudo_inverse_refuses_an_out_of_range_rhs():
    """`Gx = b` with `b` outside `range(G)` has NO solution, and returning a
    vector would present "no solution" as an answer — the failure this arc
    keeps finding. `frobenius_repose_probe` recorded exactly that for every
    census nucleus, via an inverse of an exactly-singular matrix."""
    from pyhecke.lp_dual_solver import gram_pseudo_inverse_solve

    # A rank-1 Gram in 2D: kernel is (1, -1)/sqrt(2), range is span(1, 1).
    G = [["1", "1"], ["1", "1"]]
    ok_str, ok_f64, kernel_dim = gram_pseudo_inverse_solve(G, ["2", "2"], dps=30)
    assert kernel_dim == 1
    assert ok_f64 == pytest.approx([1.0, 1.0])

    with pytest.raises(ValueError, match="not in range"):
        gram_pseudo_inverse_solve(G, ["1", "-1"], dps=30)


def test_pseudo_inverse_returns_the_minimum_norm_representative():
    """The solution is unique only up to a kernel vector; the representative
    with no kernel component is the canonical one."""
    from pyhecke.lp_dual_solver import gram_pseudo_inverse_solve

    G = [["1", "1"], ["1", "1"]]
    _s, y, _k = gram_pseudo_inverse_solve(G, ["2", "2"], dps=30)
    kernel = np.array([1.0, -1.0]) / np.sqrt(2.0)
    assert abs(float(np.dot(y, kernel))) < 1e-20, "solution carries a kernel component"


def test_pseudo_inverse_carries_full_precision_strings():
    """The f64 view and the decimal string must agree, and the string must
    actually carry more than f64 — otherwise it is f64 wearing a string, which
    the audit's laundering guard counts rather than excuses."""
    from pyhecke.lp_dual_solver import gram_pseudo_inverse_solve

    # det must not be of the form 2^a·5^b, or the exact answer is a short
    # terminating decimal and the digit count is legitimately tiny: the
    # first draft used one whose answer is 0.4, which `mp.nstr` renders
    # as "0.4". That is the test being wrong, not the companions.
    G = [["4", "1"], ["1", "6"]]        # det 23, so 1/det never terminates
    s, f, kernel_dim = gram_pseudo_inverse_solve(G, ["1", "1"], dps=50)
    assert kernel_dim == 0, "this G is nonsingular; no kernel expected"
    for si, fi in zip(s, f):
        assert float(si) == pytest.approx(fi, rel=1e-15)
    digits = max(len(x.replace("-", "").replace(".", "").lstrip("0")) for x in s)
    assert digits > 17, f"companions carry only {digits} digits — not full precision"


def test_pseudo_inverse_rank_is_stable_across_working_precision():
    """Rank is a property of the DATA, so raising `dps` above the input's own
    precision must not change the answer. It did: at dps=80 against 50-dps
    input strings the exactly-zero eigenvalue read as ~1e-50 invented noise,
    the kernel was missed, and the H_3 solve returned `y[0] = 1.0` with its
    exact `y[1] == y[2]` symmetry broken."""
    from pyhecke.lp_dual_solver import gram_pseudo_inverse_solve

    # A rank-1 Gram whose entries carry ~50 significant digits.
    a = "1." + "3" * 49
    G = [[a, a], [a, a]]
    seen = set()
    for dps in (30, 50, 80, 120):
        _s, y, kernel_dim = gram_pseudo_inverse_solve(
            G, [a, a], dps=dps
        )
        seen.add(kernel_dim)
        assert kernel_dim == 1, (
            f"kernel missed at dps={dps}: rank changed with working precision"
        )
    assert seen == {1}
