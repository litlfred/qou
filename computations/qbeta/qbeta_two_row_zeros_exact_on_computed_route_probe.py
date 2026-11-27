#!/usr/bin/env python3
"""
qbeta_two_row_zeros_exact_on_computed_route_probe.py — qou-e9le: the trap is in
the CACHED route; the COMPUTED route gives exact zeros, structurally, at every n.

# Ref: .beans/qou-e9le--three-producers-compute-70-provably-zero-character.md
# Ref: https://github.com/litlfred/qou/pull/5337#issuecomment-5431292678

THE TRAP, as reported by a sibling on #5337:

    "_load_y_lambda(12, .) returns all 77 shapes as nonzero -- the two-row ones
     at 2.3e-4...4.0e-3 and the other 70 at <=1.03e-73, solver residue against a
     value the Lean says is exactly zero. So any consumer relying on a None/zero
     check to prune is silently computing all 77. A row-count test is needed."

Correct, and this probe adds the other half: WHICH route carries the residue, and
that a drop-in without it already exists.

TWO DISTINCT ROUTES, and they are not variants of one implementation.

  * CACHED -- `wedderburn_jones_markov._load_y_lambda_at_q0_witness` reads
    `y-lambda-at-q0.witness.json`, built once by `y_lambda_at_q0_cache.py`. The
    values there are solver output, so a provably-zero weight arrives as a
    residue near 1e-73 rather than as 0. This is the route the sibling measured.
  * COMPUTED -- `y_lambda_su_n(n, q, N)` evaluates `schur_principal(sh, N, q)`
    directly. A Schur function of a shape with MORE ROWS THAN VARIABLES is
    identically zero, so the zero is structural and arrives as literal `0.0`.

MEASURED at N = 2 (convention D), n = 2..9 -- 0, 1, 2, 4, 7, 11, 17, 25 over-row
shapes respectively: EVERY one is exactly `0.0`. Not "below tolerance": `v == 0`.

Checked across n on purpose. I had just been burned by treating an n = 3 identity
as general (`qbeta_rank_one_identity_is_n3_only_probe`), so a single n would not
have been evidence here either.

WHAT THIS MEANS FOR qou-e9le. The sibling's remedy -- a row-count test -- is
right and remains the safe general fix, because a consumer cannot know which
route its `y` came from. But the three affected producers have a second option
that removes the question: on the computed route a truthiness check is already
CORRECT, because the zeros are exact by construction rather than by convergence.
Worth knowing before rewriting three call sites around a predicate.

NOT CLAIMED: that the cached witness is wrong. Its residues are ~1e-73 and do not
move any number; the defect is only that they defeat a `None`/truthiness prune.

NO fit, NO wiring. Read-only: this probe runs no producer and writes no cache.
Scope-(a).
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from y_lambda_su_n import y_lambda_su_n  # noqa: E402

set_compute_dps(50)

N_ROWS = 2  # convention D


def main() -> int:
    w = WitnessBuilder("qbeta-two-row-zeros-exact-computed-route", engine="mpmath")
    w.set_description(
        "The >N-row Markov weights are EXACTLY zero on the computed route "
        "(y_lambda_su_n) at every n from 2 to 9 — structural, since a Schur "
        "function of a shape with more rows than variables vanishes "
        "identically. The residues qou-e9le tracks are on the cached route."
    )
    ok, notes, rows = [], [], []

    def check(name, passed, note=""):
        ok.append(bool(passed))
        w.add_assertion(name, computed="1" if passed else "0",
                        expected="1", tolerance="0")
        if note:
            notes.append({"assertion": name, "note": note})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name} {note}")

    q0 = Q_MP
    all_exact, total_over = True, 0
    for n in range(2, 10):
        d = y_lambda_su_n(n, q0, N_ROWS)
        over = {k: v for k, v in d.items() if len(k) > N_ROWS}
        exact = all(v == 0 for v in over.values())
        all_exact = all_exact and exact
        total_over += len(over)
        rows.append({"n": n, "shapes": len(d), "over_row_shapes": len(over),
                     "all_exactly_zero": bool(exact),
                     "sum_of_kept_weights_times_dim": fmt(
                         mp.fsum(v for k, v in d.items() if len(k) <= N_ROWS))})
        print(f"    n={n:<3} shapes={len(d):<3} >{N_ROWS}-row={len(over):<3} "
              f"all exactly 0? {exact}")

    check("over_row_weights_are_EXACTLY_zero_at_every_n_tested", all_exact,
          f"(n = 2..9, {total_over} over-row shapes in total; `v == 0`, not "
          "'below tolerance')")
    check("the_test_spans_many_n_not_just_one",
          len(rows) >= 8 and total_over >= 25,
          "(checked across n deliberately — an n=3-only check would not be "
          "evidence, as qbeta_rank_one_identity_is_n3_only_probe showed)")
    check("the_over_row_population_actually_grows",
          rows[-1]["over_row_shapes"] > rows[1]["over_row_shapes"],
          f"(1 at n=3 -> {rows[-1]['over_row_shapes']} at n=9, so the result is "
          "not carried by a near-empty set)")

    w.add_data("per_n", rows)
    w.add_data("N_variables", N_ROWS)
    w.add_data("cached_route", "wedderburn_jones_markov._load_y_lambda_at_q0_witness "
                               "→ y-lambda-at-q0.witness.json (solver output; "
                               "carries ~1e-73 residues — the qou-e9le trap)")
    w.add_data("computed_route", "y_lambda_su_n → schur_principal (structural "
                                 "zero: a Schur function of a shape with more "
                                 "rows than variables vanishes identically)")
    w.add_data("markov_convention", "D (N = 2)")
    w.add_data("assertion_notes", notes)

    verdict = (
        "The qou-e9le trap is a property of the CACHED route, not of the "
        "weights. `_load_y_lambda_at_q0_witness` reads solver output, so a "
        "provably-zero weight arrives as a ~1e-73 residue and defeats a "
        "None/truthiness prune. The COMPUTED route `y_lambda_su_n` evaluates "
        "`schur_principal` directly, and a Schur function of a shape with more "
        "rows than variables is identically zero — measured at N = 2 for "
        "n = 2..9, every one of 67 over-row shapes is exactly `0.0`, not "
        "below-tolerance. So the sibling's row-count remedy is right and stays "
        "the safe general fix (a consumer cannot tell which route its `y` came "
        "from), but the affected producers also have the option of a route on "
        "which a truthiness check is already correct. Checked across n on "
        "purpose: a single-n check would not have been evidence. NOT claimed: "
        "that the cached witness is wrong — its residues move no number."
        if all(ok) else
        "INCONCLUSIVE -- an assertion failed; re-derive before citing.")
    w.add_data("verdict", verdict)
    path = w.save()
    print(f"\n{verdict}\n\nWitness: {path}")
    return 0 if all(ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
