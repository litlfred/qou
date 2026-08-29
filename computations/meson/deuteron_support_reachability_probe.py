#!/usr/bin/env python3
"""The deuteron binding is not reachable from the convention-D supported blocks.

Bean qou-6tcn. Follow-on to the convention-D excision in the deuteron SDP
(PR #5817): that PR left an open item saying the six Phase-B encodings still
solved on the full 11-block space and so returned `primal_obj = 0.0` through a
"kernel free lunch". This probe measures what happens when the constraint rows
are projected onto the support, and the answer is sharper than the open item
predicted.

THE SETUP
=========
Convention D caps the Markov weights at two rows, so at `n = 6` exactly four of
eleven Wedderburn blocks carry weight. Both the Frobenius Gram diagonal and the
cost vanish on the other seven:

    G_ll = tr_M(P_l) = y_l(q0)          zero for ell(l) > 2
    t_l  = y_l * chi^l(beta_D)          zero for the same l

The operator-selection LP is `min t.x` over `{x : sum x = n_target, Gx >= 0,
|x| <= M}`.

WHAT THE KERNEL ACTUALLY BUYS
=============================
PR #5817 described the kernel as absorbing the net constraint at zero cost.
Measured here, it does more than that. On the support `G` is strictly positive,
so `Gx >= 0` IS `x >= 0` there. On the kernel `G = 0`, so `Gx >= 0` imposes
NOTHING and `x` may go **negative** down to the `-M` bound.

So the kernel does not merely absorb `sum x = n_target` — it supplies negative
occupations, and those are what let `t.x` reach values no non-negative
occupation of the visible blocks can produce.

THE BOUND
=========
With `x >= 0` on the support and `sum x = n_target`, the objective is a convex
combination scaled by `n_target`:

    t.x <= max_{l in support} t_l * n_target

Measured: `0.253938 * 0.575172 = 0.146058`, against `B_D(AME2020) = 2.224566`.
The AME binding is **15.2x** above the reachable ceiling.

SCOPE — (a), scope-limited, per AGENTS.md
=========================================
MEASURED: the support, the cost vector on it, the reachability ceiling, and
that all six Phase-B encodings are infeasible once projected.

NOT claimed: that `conj:jsj-decomposition-linearity` or any binding conjecture
is false; that the encodings are wrong; that the framework cannot reproduce the
deuteron binding. What is shown is narrower and exact: **this cost vector, on
this program, with non-negative occupations of the convention-D supported
blocks, cannot reach the AME value.** A different cost, a different level `r`,
or a program admitting signed occupations with a stated reason are all
untouched by this.

In particular the full-space numbers this replaces were NOT wrong arithmetic —
they were the correct optimum of a program whose kernel is unconstrained. The
finding is that that program does not mean what its field names suggest.

NO FLOAT64 in the analysis: the bound is computed in `mpmath.mpf` from the
committed witness strings; `float()` appears only for display and for the
witness assertion API, which takes strings.
"""

from __future__ import annotations

import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

SDP = pathlib.Path(__file__).resolve().parent.parent / "deuteron-real-sdp.witness.json"
ZERO = mp.mpf("1e-40")


def main() -> int:
    wb = WitnessBuilder("deuteron-support-reachability", engine="python-exact")
    wb.set_description(
        "Under convention D the deuteron operator-selection LP, restricted to "
        "the four supported (two-row) Wedderburn blocks with non-negative "
        "occupations, cannot reach the AME2020 binding: the objective is "
        "bounded by max(t)*n_target = 0.146058 against B_D = 2.224566, short "
        "by 15.2x. The full-space program met the AME value only because the "
        "seven zero-Gram kernel blocks carry no positivity constraint and so "
        "admit NEGATIVE occupations.")

    d = json.loads(SDP.read_text())["data"]
    keys = d["partitions"]
    t = [mp.mpf(str(x)) for x in d["cost_t_lambda"]]
    g = [mp.mpf(str(x)) for x in d["frobenius_gram_diag"]]
    n_target = mp.mpf(str(d["n_target"]))
    ame = mp.mpf(str(d["B_D_AME_MeV"]))

    support = [i for i, x in enumerate(g) if abs(x) > ZERO]
    kernel = [i for i, x in enumerate(g) if abs(x) <= ZERO]
    t_max = max(t[i] for i in support)
    ceiling = t_max * n_target
    shortfall = ame / ceiling

    print(f"support ({len(support)}): {[keys[i] for i in support]}")
    print(f"kernel  ({len(kernel)}): {[keys[i] for i in kernel]}")
    print(f"\nt on support : {[mp.nstr(t[i], 8) for i in support]}")
    print(f"t on kernel  : {[mp.nstr(t[i], 8) for i in kernel]}")
    print(f"\nn_target     = {mp.nstr(n_target, 12)}")
    print(f"max t (supp) = {mp.nstr(t_max, 12)}")
    print(f"ceiling      = {mp.nstr(ceiling, 12)}   (= max(t) * n_target)")
    print(f"B_D AME2020  = {mp.nstr(ame, 12)}")
    print(f"shortfall    = {mp.nstr(shortfall, 8)}x")

    # Which encodings survive projection, read from the committed witness.
    methods = d.get("phase_B_full_methods", {})
    proj_feasible = {k: bool((v.get("result_support_projected") or {}).get("feasible"))
                     for k, v in methods.items()}
    degenerate_rows = {
        k: [r for r in (v.get("projection_row_report") or [])
            if r.get("degenerate_under_projection")]
        for k, v in methods.items()
    }
    print("\nprojected feasibility per encoding:")
    for k in sorted(proj_feasible):
        dg = degenerate_rows.get(k) or []
        note = f"   degenerate rows: {[r['row'] for r in dg]} ({dg[0]['verdict']})" if dg else ""
        print(f"  {k:<38} feasible={proj_feasible[k]}{note}")

    # ── assertions ────────────────────────────────────────────────────────
    # A1 — the support is the four two-row blocks. CONTROL: if this failed the
    #      run would not be convention D and every number below is meaningless.
    wb.add_assertion(
        name="control_support_is_four_two_row_blocks",
        computed=str(len(support)), expected="4", tolerance="0", unit="count",
        source="convention D row cap: y_lambda = 0 for ell(lambda) > 2")

    # A2 — the cost vanishes identically on the kernel. This is what makes the
    #      full-space objective insensitive to kernel occupation.
    max_t_kernel = max((abs(t[i]) for i in kernel), default=mp.mpf(0))
    wb.add_assertion(
        name="cost_vanishes_on_kernel",
        computed=mp.nstr(max_t_kernel, 20), expected="0", tolerance="1e-40",
        unit="dimensionless", source="t_l = y_l * chi^l, and y_l = 0 on the kernel")

    # A3 — THE BOUND. Asserted as the ratio so a wrong scale fails.
    wb.add_assertion(
        name="ame_exceeds_support_reachability_ceiling",
        computed=mp.nstr(shortfall, 20), expected="15.2307",
        tolerance="1e-3", unit="ratio",
        source="t.x <= max(t)*n_target for x >= 0, sum x = n_target")

    # A4 — the ceiling is strictly below the target (the qualitative claim,
    #      independent of the exact ratio).
    wb.add_assertion(
        name="ceiling_strictly_below_ame",
        computed="1" if ceiling < ame else "0", expected="1", tolerance="0",
        unit="boolean", source="direct comparison")

    # A5 — every encoding is infeasible once projected. This is the result the
    #      probe exists to record; it is a NEGATIVE and is scoped as (a).
    n_feasible = sum(1 for v in proj_feasible.values() if v)
    wb.add_assertion(
        name="no_encoding_feasible_under_projection",
        computed=str(n_feasible), expected="0", tolerance="0", unit="count",
        source="deuteron-real-sdp.witness.json result_support_projected")

    # A6 — CONTROL that projection is not vacuously breaking everything: the
    #      canonical LR encoding has a row whose weight is ENTIRELY on the
    #      kernel, which is a specific, locatable reason rather than a blanket
    #      failure. Its verdict is the infeasible one.
    lr = degenerate_rows.get("5_lr_branching_canonical") or []
    wb.add_assertion(
        name="lr_canonical_has_a_fully_kernel_row",
        computed=str(len(lr)), expected="1", tolerance="0", unit="count",
        source="projection_row_report: row 2, mu = (1,1,1), 100% on kernel")

    wb.add_data("support_blocks", [keys[i] for i in support])
    wb.add_data("kernel_blocks", [keys[i] for i in kernel])
    wb.add_data("t_on_support", [mp.nstr(t[i], 30) for i in support])
    wb.add_data("n_target", mp.nstr(n_target, 30))
    wb.add_data("reachability_ceiling", mp.nstr(ceiling, 30))
    wb.add_data("B_D_AME_MeV", mp.nstr(ame, 30))
    wb.add_data("shortfall_factor", mp.nstr(shortfall, 30))
    wb.add_data("projected_feasible", proj_feasible)
    wb.add_caveat(
        "Scope (a). This bounds THIS cost vector on THIS program with "
        "non-negative occupations of the convention-D supported blocks. It "
        "does not refute any binding conjecture, does not say the encodings "
        "are wrong, and says nothing about a different cost, a different "
        "Wenzl level r, or a program that admits signed occupations for a "
        "stated reason.")
    wb.add_caveat(
        "The full-space numbers this replaces were not wrong arithmetic. They "
        "were the correct optimum of a program whose kernel is unconstrained, "
        "and the finding is that such a program does not mean what its field "
        "names suggest.")
    wb.save()
    print("\nwitness written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
