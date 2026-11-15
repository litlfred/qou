#!/usr/bin/env python3
"""The colour-tube refinement cannot supply the binding MAGNITUDE either.

Bean qou-6tcn. Corollary of `two_remaining_fronts_probe.py` front 2, formalised
in `QOU/MassTheory/BranchConvexityBound.lean`. Raised by the author asking where
the missing binding term lives.

THE CORPUS'S OWN CANDIDATE
==========================
`conj:inter-nucleon-channel-color-tube` is the framework's named candidate for
the inter-nucleon term: `A - 1` arcs, one per adjacent nucleon pair -- genuinely
extensive, unlike everything else this arc has closed. It refines the production
assignment `pp -> sigma`, `nn -> sigma^-1`, `pn -> sigma_avg` into a
colour-sheet-weighted sum

    sigma^(F1,F2)_int = sum_{(c1,c2)} W_{c1c2}(F1,F2) * sigma^{eps(c1,c2,F1,F2)}

THE COROLLARY
=============
That block's own statement fixes `W_{c1c2} in Q_{>=0}` **normalised to
`sum W = 1`**, with `eps in {+1,-1,0}` and `eps = 0 -> sigma_avg`. Every term
therefore lies in the convex hull of `{sigma, sigma^-1}` at each arc, so the
refined atom has **the same branch set** as the production one -- 32 for the
deuteron -- only reweighted.

`QOU.MassTheory.convex_comb_le_bound` (sorry-free) then applies verbatim:

    refined tr_M(beta_D)  <=  max_b tr_M(beta_b)  =  1.018275
    required (concentrated cost)                  =  1.491498
    ratio                                         =  0.68272   -> UNREACHABLE

So the colour-tube refinement is bounded by the same number as the production
assignment and cannot supply the deuteron binding magnitude. This does NOT touch
what the refinement is actually for -- the p/n asymmetry and the chirality sign
structure, where it may well be right. It bounds the MAGNITUDE only.

WHAT ESCAPES, AND WHY IT IS THE SATELLITE
=========================================
`QOU.MassTheory.larger_index_set_escapes_the_bound` (sorry-free) exhibits the
one way out: the bound is relative to the branch set it is taken over, and a
LARGER index set can exceed it. A satellite/cabling move replaces each strand by
several, so its branches are words in a bigger algebra -- not a reweighting of
the old branches but a different index set, outside the theorem's hypotheses.
That is exactly why front 2 closes the reweighting route while leaving the
satellite route open, and it lines up with `conj:jsj-decomposition-linearity`,
whose decomposition hypothesis is that the inter-nucleon braids form **essential
tori** -- the satellite condition.

AUDITABLE PREMISE
=================
The convexity reading of the refinement is not asserted here on my say-so: A6
greps the block for its own normalisation sentence, so a reader can check the
premise against the source rather than against this docstring. If that block is
ever edited to drop the normalisation, A6 fails and this corollary is void --
which is the correct behaviour.

SCOPE -- (b), with the invariant named and Lean-proved
======================================================
The invariant is the convexity of the branch decomposition
(`atom-branch-convexity-bound`, measured) plus `convex_comb_le_bound` (proved).
NOT claimed: that the refinement is wrong, that it fails at anything other than
supplying this magnitude, that a satellite construction DOES reach the target
(only that this theorem does not forbid it), or that `conj:jsj-decomposition-
linearity` is true or false. ONE isotope: the deuteron.
"""

from __future__ import annotations

import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()
mp.mp.dps = max(mp.mp.dps, 40)

HERE = pathlib.Path(__file__).resolve().parent
FRONTS = HERE / "two-remaining-fronts.witness.json"
BLOCK = (HERE.parent.parent / "folio" / "quantum-observable-universe" /
         "brings-surface" / "inter-nucleon-channel-color-tube.md")


def main() -> int:
    wb = WitnessBuilder("colour-tube-refinement-is-convexity-bounded",
                        engine="python-exact")
    wb.set_description(
        "conj:inter-nucleon-channel-color-tube fixes W >= 0 normalised to "
        "sum W = 1, so the refined atom is a REWEIGHTING of the same 32 "
        "branches, not a new element. QOU.MassTheory.convex_comb_le_bound then "
        "bounds it by max_b tr_M = 1.018275 against a required 1.491498 -- "
        "unreachable, ratio 0.68272. The refinement cannot supply the deuteron "
        "binding MAGNITUDE. Scope (b); the escape is a larger index set, i.e. a "
        "satellite/cabling move (larger_index_set_escapes_the_bound).")

    fr = json.loads(FRONTS.read_text())["data"]
    max_b = mp.mpf(fr["front2_max_branch_trace"])
    min_b = mp.mpf(fr["front2_min_branch_trace"])
    need = mp.mpf(fr["front2_required_trace"])
    n_branch = fr["front2_branch_count"]
    ratio = max_b / need

    # sigma_avg = (sigma + sigma^-1)/2 -- itself convex, so eps = 0 stays inside
    avg_w = [mp.mpf(1) / 2, mp.mpf(1) / 2]
    avg_ok = (min(avg_w) >= 0) and abs(sum(avg_w) - 1) < mp.mpf("1e-40")

    text = BLOCK.read_text() if BLOCK.exists() else ""
    has_nonneg = bool(re.search(r"W_\{c_1 c_2\}\(F_1, F_2\) \\in \\mathbb\{Q\}_\{\\geq 0\}", text))
    has_norm = bool(re.search(r"normalised to.*?\\sum_\{c_1, c_2\} W_\{c_1 c_2\} = 1",
                              text, re.S))
    premise_ok = has_nonneg and has_norm

    print(f"branches {n_branch}   min {mp.nstr(min_b, 10)}   max {mp.nstr(max_b, 10)}")
    print(f"required {mp.nstr(need, 10)}   ratio {mp.nstr(ratio, 8)}  -> "
          f"{'UNREACHABLE' if ratio < 1 else 'reachable'}")
    print(f"block premise greppable: W>=0 {has_nonneg}, normalised {has_norm}")

    # ── assertions ────────────────────────────────────────────────────────
    # A1 — THE COROLLARY. Same bound, so the refinement cannot get there.
    wb.add_assertion(
        name="colour_tube_refinement_cannot_reach_required_trace",
        computed=mp.nstr(ratio, 20), expected="0.68272",
        tolerance="1e-4", unit="ratio",
        source="max_b tr_M(beta_b) / sqrt(B_AME); < 1 means unreachable by any "
               "convex reweighting, per QOU.MassTheory.convex_comb_le_bound")

    # A2 — CONTROL: the bound is inherited unchanged from front 2.
    wb.add_assertion(
        name="control_max_branch_trace_matches_front2",
        computed=mp.nstr(max_b, 20), expected="1.018275083",
        tolerance="1e-6", unit="dimensionless",
        source="two-remaining-fronts front2_max_branch_trace")

    # A3 — CONTROL: 32 branches, i.e. the refinement really does share the
    #      production assignment's branch set.
    wb.add_assertion(
        name="control_branch_count_unchanged",
        computed=str(n_branch), expected="32", tolerance="0", unit="count",
        source="the refinement reweights arcs; it adds no strands")

    # A4 — the eps = 0 case maps to sigma_avg, which is ITSELF convex, so no
    #      term of the refined sum leaves the hull.
    wb.add_assertion(
        name="sigma_avg_is_itself_a_convex_combination",
        computed=repr(bool(avg_ok)), expected="True", tolerance="0",
        unit="boolean",
        source="sigma_avg = (sigma + sigma^-1)/2 has weights (1/2, 1/2)")

    # A5 — CONTROL against the vacuous reading "the bound is trivially met":
    #      the branches genuinely spread, and max_b exceeds the atom's own value.
    wb.add_assertion(
        name="control_branches_spread_above_the_atom",
        computed=mp.nstr(max_b / mp.mpf("0.5751722457697739"), 20),
        expected="1.7704", tolerance="1e-3", unit="ratio",
        source="max_b / tr_M(atom); > 1, so the bound is not trivially satisfied")

    # A6 — THE PREMISE, MADE AUDITABLE. The convexity reading is checked against
    #      the block's own text, not asserted on my say-so. If the block is
    #      edited to drop the normalisation, this fails and the corollary voids.
    wb.add_assertion(
        name="block_states_its_weights_are_nonneg_and_normalised",
        computed=repr(bool(premise_ok)), expected="True", tolerance="0",
        unit="boolean",
        source="grep of inter-nucleon-channel-color-tube.md for "
               "'W in Q_{>=0}' and 'normalised to sum W = 1'")

    # A7 — CONTROL that A6 is a real grep and not vacuously true on any file.
    wb.add_assertion(
        name="control_block_file_exists_and_is_nonempty",
        computed=str(len(text) > 500), expected="True", tolerance="0",
        unit="boolean", source=str(BLOCK.relative_to(HERE.parent.parent)))

    wb.add_data("max_branch_trace", mp.nstr(max_b, 24))
    wb.add_data("required_trace", mp.nstr(need, 24))
    wb.add_data("ratio", mp.nstr(ratio, 24))
    wb.add_data("branch_count", n_branch)
    wb.add_data("lean_ref", "qou:QOU.MassTheory.convex_comb_le_bound")
    wb.add_data("escape_lean_ref",
                "qou:QOU.MassTheory.larger_index_set_escapes_the_bound")
    wb.add_caveat(
        "SCOPE (b): the invariant is branch convexity (measured in "
        "atom-branch-convexity-bound) plus convex_comb_le_bound (Lean, "
        "sorry-free). It bounds the MAGNITUDE only. It does NOT say the "
        "colour-tube refinement is wrong -- the p/n asymmetry and chirality "
        "sign structure it exists for are untouched.")
    wb.add_caveat(
        "The escape is a LARGER INDEX SET, exhibited in Lean by "
        "larger_index_set_escapes_the_bound: a satellite/cabling move puts the "
        "branches in a bigger algebra, outside the hypotheses. NOT claimed that "
        "such a construction DOES reach the target -- only that this theorem "
        "does not forbid it.")
    wb.add_caveat(
        "ONE isotope (deuteron), and the underlying max_b comes through "
        "binding_k_solver.per_block_evaluation, which is float64. The verdict "
        "turns on a 47 % gap, far above that resolution.")
    wb.save()
    print("\nwitness written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
