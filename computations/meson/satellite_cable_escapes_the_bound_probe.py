#!/usr/bin/env python3
"""The satellite escapes the branch-convexity bound — measured, 4.99x over.

Bean qou-6tcn. The test Addendum 24 said needed doing and did not do. It is the
first POSITIVE result in this arc, and it is exactly what
`QOU.MassTheory.larger_index_set_escapes_the_bound` predicted.

WHAT WAS TESTED
===============
The **2-parallel cable** of the deuteron braid: each strand is doubled and each
`sigma_i` becomes `s_{2i} s_{2i-1} s_{2i+1} s_{2i}` in `B_12`. Its closure is
the 2-parallel of the original closure -- a **genuine satellite**, pattern = the
2-parallel curve in the solid torus, companion = the original knot. So it is the
geometrically-motivated move, not an arbitrary longer word.

MEASURED (7 two-row blocks of H_12; the 2-cable is 92 letters on 12 strands)
===========================================================================
    min_b tr_M(2-cable)   0.147468
    max_b tr_M(2-cable)   7.448220
    convex atom 2-cable   see `atom_2cable_trace` in the data
    required sqrt(B_AME)  1.491498
    max / required        4.9938        -> EXCEEDS

Addendum 23 measured the same quantity WITHOUT cabling at `max_b = 1.018275`,
i.e. 0.683 of the requirement. Cabling takes it to 4.99x. **The trace magnitude
is no longer the binding constraint on the satellite route.**

WHY THIS IS THE PREDICTED ESCAPE, NOT A SURPRISE
================================================
`convex_comb_le_bound` bounds a reweighting of a FIXED branch set;
`larger_index_set_escapes_the_bound` shows a larger index set can exceed it. A
cable puts the branches in `H_12` rather than `H_6` -- a different index set,
outside the theorem's hypotheses. The Lean said this class escapes before the
number was computed; this measures that it actually does, and by how much.

**A longer word generally has a larger trace, so "the cable is bigger" is not by
itself interesting.** What is: that the geometrically-motivated satellite move
crosses the specific threshold, by 5x rather than marginally, and that the
threshold is a NECESSARY condition derived generically (a concentrated cost needs
`sum(t) = tr_M >= sqrt(B_AME)` at any `n`, so the comparison is valid across
algebras -- see control C1).

WHAT THIS DOES **NOT** SHOW
===========================
* **Binding is not reproduced.** Nothing here computes a binding contribution.
  The cost vector, support, Gram and the whole LP change at `n = 12`; none of
  that is redone. Exceeding a NECESSARY condition is not sufficiency.
* **The pattern is a choice.** 2-parallel with blackboard framing is one
  satellite among infinitely many; nothing derives it, and a different pattern
  gives different numbers.
* **`Geom` still assigns nothing to a satellite.** This shows the room exists,
  not that the framework can use it. The missing case is still missing.
* Scope (a). No claim that `conj:jsj-decomposition-linearity` is true.

COMPUTE NOTE -- a 2500x cost difference from asking for less
============================================================
The first attempt called `per_block_evaluation`, which builds ALL 77 partitions
of 12; it reached **9.99 GB RSS** and was killed before it could OOM the
session. Only the **7 two-row blocks** matter under convention D (max dimension
297), and `block_rep_braid_word` takes one partition at a time. The whole
32-branch sweep then ran in **3.6 seconds**. Recorded because it is the same
lesson as the formalize-first miss two addenda back: establish what you need
before you compute it.

`block_rep_braid_word` returns float64, so this is float64; the verdict turns on
a factor of 5, far above that resolution.
"""

from __future__ import annotations

import itertools
import pathlib
import sys
from math import factorial

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
import binding_k_solver as bks  # noqa: E402
import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from pyhecke.gram import h as _h_f  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from q_parameter import HA_MP, Q_MP  # noqa: E402 — exact mpf, not the f64 twin
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()
mp.mp.dps = max(mp.mp.dps, 40)

Q = Q_MP
H = HA_MP
TOL = mp.mpf("1e-9")


def hook_dim(lam):
    lam = tuple(x for x in lam if x)
    n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= (row - j) + (conj[j] - i) - 1
    return factorial(n) // prod


def qint(m):
    return (Q ** m - Q ** (-m)) / (Q - 1 / Q)


def two_row(n):
    return [(n,)] + [(n - k, k) for k in range(1, n // 2 + 1)]


def weights(n):
    return {l: qint(n - 2 * (l[1] if len(l) > 1 else 0) + 1) / qint(2) ** n
            for l in two_row(n)}


def tr_M(word, n):
    y = weights(n)
    tot = mp.mpf(0)
    for lam in two_row(n):
        M = (bks.block_rep_braid_word(lam, word, q=float(Q)) if word
             else np.eye(hook_dim(lam)))
        tot += y[lam] * mp.mpf(str(float(np.trace(M))))
    return tot


def slots(word):
    out = []
    for (_c, d, g) in word:
        t = -mp.mpf(str(d)) / H
        if abs(t) < TOL:
            out.append([(g + 1, mp.mpf(1))])
        elif abs(t - 1) < TOL:
            out.append([(-(g + 1), mp.mpf(1))])
        else:
            out.append([(g + 1, 1 - t), (-(g + 1), t)])
    return out


def cable2(braid):
    """2-parallel: strand i -> {2i-1, 2i}; sigma_i -> s_{2i} s_{2i-1} s_{2i+1} s_{2i}."""
    out = []
    for x in braid:
        i, s = abs(x), (1 if x > 0 else -1)
        for g in (2 * i, 2 * i - 1, 2 * i + 1, 2 * i):
            out.append(s * g)
    return out


def main() -> int:
    wb = WitnessBuilder("satellite-cable-escapes-the-bound",
                        engine="python-exact")
    wb.set_description(
        "The 2-parallel cable of the deuteron braid -- a genuine satellite -- "
        "reaches max_b tr_M = 7.448220 against the required 1.491498, i.e. "
        "4.99x over, where the uncabled word reached only 1.018275 (0.683x). The "
        "atom's OWN convex-weighted 2-cable also clears it, at 1.657034 = "
        "1.111x -- a thin margin. "
        "The satellite escapes the branch-convexity bound exactly as "
        "QOU.MassTheory.larger_index_set_escapes_the_bound predicted. Does NOT "
        "reproduce binding: the cost, support, Gram and LP all change at n=12 "
        "and none of that is redone; exceeding a NECESSARY condition is not "
        "sufficiency.")

    branches = list(itertools.product(*slots(atom_braid_word_3A(1, 1))))
    uncabled, cabled, w_atom = [], [], mp.mpf(0)
    cab_atom = mp.mpf(0)
    for combo in branches:
        b = [g for g, _ in combo]
        w = mp.mpf(1)
        for _, wt in combo:
            w *= wt
        u = tr_M(b, 6)
        c = tr_M(cable2(b), 12)
        uncabled.append(u)
        cabled.append(c)
        w_atom += w * u
        cab_atom += w * c

    max_u, max_c, min_c = max(uncabled), max(cabled), min(cabled)
    need = mp.sqrt(mp.mpf("2.224566"))
    ratio_c, ratio_u = max_c / need, max_u / need
    norm12 = mp.fsum(weights(12)[l] * hook_dim(l) for l in two_row(12))
    norm6 = mp.fsum(weights(6)[l] * hook_dim(l) for l in two_row(6))
    id12 = tr_M([], 12)
    max_gen = max(abs(x) for x in cable2([g for g, _ in branches[0]]))

    print(f"branches {len(branches)}   cable = "
          f"{len(cable2([g for g, _ in branches[0]]))} letters on 12 strands")
    print(f"  uncabled  max {mp.nstr(max_u, 10):<16} ratio {mp.nstr(ratio_u, 6)}")
    print(f"  2-cable   max {mp.nstr(max_c, 10):<16} ratio {mp.nstr(ratio_c, 6)}"
          f"   -> {'EXCEEDS' if ratio_c >= 1 else 'below'}")
    print(f"  atom 2-cable (convex) {mp.nstr(cab_atom, 10)}")

    # ── assertions ────────────────────────────────────────────────────────
    # A1 — THE RESULT.
    wb.add_assertion(
        name="satellite_cable_exceeds_required_trace",
        computed=mp.nstr(ratio_c, 20), expected="4.99378",
        tolerance="1e-4", unit="ratio",
        source="max_b tr_M(2-cable) / sqrt(B_AME); >= 1 means the necessary "
               "condition is met")

    # A2 — CONTROL, and the reason A1 is a change rather than a restatement:
    #      the SAME quantity without cabling falls short.
    wb.add_assertion(
        name="control_uncabled_word_falls_short",
        computed=mp.nstr(ratio_u, 20), expected="0.68272",
        tolerance="1e-4", unit="ratio",
        source="max_b tr_M(beta_b) / sqrt(B_AME) at n = 6")

    # A3 — CONTROL tying this code path to the committed front-2 number, so the
    #      cable result is computed by a validated route.
    wb.add_assertion(
        name="control_uncabled_max_matches_front2",
        computed=mp.nstr(max_u, 20), expected="1.018275083",
        tolerance="1e-6", unit="dimensionless",
        source="two-remaining-fronts front2_max_branch_trace, via "
               "block_rep_braid_word rather than per_block_evaluation")

    # A4 — CONTROL, the load-bearing one: M1 holds at BOTH n, so tr_M values are
    #      comparable across the two algebras and A1's comparison is licit.
    wb.add_assertion(
        name="control_M1_normalisation_at_n12",
        computed=mp.nstr(abs(norm12 - 1), 20), expected="0",
        tolerance="1e-30", unit="dimensionless",
        source="sum_l y_l f^l over the two-row blocks of 12")
    wb.add_assertion(
        name="control_M1_normalisation_at_n6",
        computed=mp.nstr(abs(norm6 - 1), 20), expected="0",
        tolerance="1e-30", unit="dimensionless",
        source="the same sum at n = 6")

    # A5 — CONTROL: the identity at n=12 traces to 1, so the n=12 path is sane.
    wb.add_assertion(
        name="control_identity_trace_is_one_at_n12",
        computed=mp.nstr(abs(id12 - 1), 20), expected="0",
        tolerance="1e-30", unit="dimensionless",
        source="tr_M(1) = 1 is Markov axiom M1")

    # A6 — CONTROL: the convex average still reproduces the committed atom trace,
    #      so the branch weights used for the cable are the right ones.
    wb.add_assertion(
        name="control_convex_average_reproduces_atom_trace",
        computed=mp.nstr(abs(w_atom - mp.mpf("0.5751722457697739")), 20),
        expected="0", tolerance="1e-7", unit="dimensionless",
        source="sum_b w_b tr_M(beta_b) vs deuteron-real-sdp n_target")

    # A6b — THE PHYSICALLY MEANINGFUL NUMBER, and it is NOT just the max: the
    #       atom's OWN convex-weighted 2-cable clears the requirement too, at
    #       1.657034 -- though by only 1.11x, so the margin is thin and the
    #       achievable objective still depends on the n=12 cost shape, which is
    #       NOT computed here.
    wb.add_assertion(
        name="atom_convex_2cable_also_clears_the_requirement",
        computed=mp.nstr(cab_atom / need, 20), expected="1.11099",
        tolerance="1e-4", unit="ratio",
        source="sum_b w_b tr_M(2-cable of beta_b) / sqrt(B_AME), the framework's "
               "own branch weights -- not the max over branches")

    # A7 — CONTROL: the cabling map respects H_12's generator range.
    wb.add_assertion(
        name="control_cable_generators_within_h12",
        computed=str(max_gen), expected="11", tolerance="0", unit="index",
        source="max |generator| of the 2-cable; H_12 admits 1..11")

    wb.add_data("branch_count", len(branches))
    wb.add_data("cable_word_length",
                len(cable2([g for g, _ in branches[0]])))
    wb.add_data("uncabled_max_trace", mp.nstr(max_u, 24))
    wb.add_data("cable_min_trace", mp.nstr(min_c, 24))
    wb.add_data("cable_max_trace", mp.nstr(max_c, 24))
    wb.add_data("atom_2cable_trace", mp.nstr(cab_atom, 24))
    wb.add_data("required_trace", mp.nstr(need, 24))
    wb.add_data("ratio_cabled", mp.nstr(ratio_c, 24))
    wb.add_data("lean_predicted_by",
                "qou:QOU.MassTheory.larger_index_set_escapes_the_bound")
    wb.add_caveat(
        "Scope (a). This does NOT reproduce binding. The cost vector, support, "
        "Gram and the whole LP change at n = 12 and none of it is redone here; "
        "exceeding a NECESSARY condition (a concentrated cost needs "
        "tr_M >= sqrt(B_AME)) is not sufficiency, and nothing here computes a "
        "binding contribution.")
    wb.add_caveat(
        "The pattern is a CHOICE. 2-parallel with blackboard framing is one "
        "satellite among infinitely many; nothing derives it, and a different "
        "pattern gives different numbers. And Geom still assigns nothing to a "
        "satellite -- this shows the room exists, not that the framework can "
        "use it.")
    wb.add_caveat(
        "A longer word generally has a larger trace, so 'the cable is bigger' "
        "is not by itself interesting. What is: the geometrically-motivated "
        "move crosses the threshold by 5x rather than marginally, and the Lean "
        "predicted this class escapes before the number was computed.")
    wb.add_caveat(
        "block_rep_braid_word returns float64, so this is float64; the verdict "
        "turns on a factor of 5. The first attempt used per_block_evaluation, "
        "which builds all 77 partitions of 12 and reached 9.99 GB RSS before "
        "being killed; restricting to the 7 two-row blocks that matter under "
        "convention D ran the whole sweep in 3.6 s.")
    wb.save()
    print("\nwitness written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
