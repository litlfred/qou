#!/usr/bin/env python3
"""Where do the negative occupations arise? Measured answer: nowhere.

Bean qou-6tcn. `deuteron_cost_and_sign_structure_probe.py` reported that every
negative *character* chi^lambda(beta_D) sits in the convention-D kernel, and
then drew a causal conclusion from it. This probe measures the occupations
themselves and retracts that conclusion.

RETRACTION -- the kernel characters cannot matter, because they are not priced
================================================================================
The previous docstring said the full-space program reached AME "not merely
because the kernel is unconstrained, but because the kernel is *where the minus
signs live*". That is causally wrong. The cost vector is

    t_lambda = y_lambda * chi^lambda(beta_D)

and convention D's row cap sets `y_lambda = 0` for `ell(lambda) > 2`, so
`t_lambda = 0` on **every** kernel block -- exactly, by construction, whatever
the character does. Measured on the committed witness: `max |t|` over the seven
kernel blocks is `0.0`, and `t . x` restricted to the kernel is `0.0` for every
solution examined here. A block that contributes nothing to the objective
cannot be the reason the objective got large.

The character-sign observation itself STANDS (assertions A6/A7 of the earlier
probe are unaffected): the negative characters really are all in the kernel.
Only the inference from it is withdrawn.

THE ACTUAL MECHANISM -- an unpriced overdraft on the net constraint
==================================================================

  SUPERSEDED, same bean, by `zero_weight_sector_is_temperley_lieb_probe.py`.
  The word "unpriced" below is wrong, and so is the question it led to ("what
  could price the kernel?"). Nothing prices it and nothing should: per
  `prop:markov-trace-frobenius-selection` (iii), stated unconditionally, the
  radical of <x,y> = tr_M(xy) is exactly the Temperley-Lieb ideal
  I_n = ker(H_n(q) -> TL_n(q)), and it is (TL_n, tr_M) -- NOT (H_n, tr_M) --
  that is the symmetric Frobenius algebra. Checked: the support's squared
  dimensions sum to 132 = Catalan(6) = dim TL_6 exactly (and at n = 2..8).
  So a negative occupation of a zero-weight block is not a debt against the
  vacuum; it is an occupation of a direction that is not in the algebra. The
  MEASUREMENTS below all stand -- the ledger identity, the vertex-dependence
  of the negative set, D_min -- as facts about the LP as posed on H_6. What
  changes is that posing it on H_6 was the defect.
The net constraint is a plain sum, `sum_lambda x_lambda = n_target`. On the
kernel `G = 0`, so `Gx >= 0` imposes nothing and `x` may go negative. So a
kernel deficit `-D` buys the support a budget of `n_target + D`:

    method 4 (the only encoding reaching AME, and it reaches it by IMPOSING it)
      support sum   +12.3662     all of it on the single block (6,)
      kernel  sum   -11.7910
      net            +0.5752  =  n_target                    identity holds
      t . x  on support  2.224566 = AME
      t . x  on kernel   0.0                                 exactly

The zero-weight blocks are free in the objective (`t = 0`) *and* free in the
Frobenius cone (`G = 0`). They are pure ledger. That is the precise sense in
which this is a debt: the program borrows budget against blocks nothing ever
charges for. It is not a debt that is repaid later -- there is no term in the
program that would ever come due. It is unpriced.

WHICH BLOCKS GO NEGATIVE IS NOT DETERMINED
==========================================
The question "which blocks arise negative" has no invariant answer. Permuting
the *variable order* -- a relabelling that leaves the polytope, the objective
and the optimum untouched -- moves the negative set entirely:

    identity order   (4,1,1) (3,2,1) (3,1,1,1) (2,2,2)        D = 11.7910
    perm 0           (4,1,1) (3,2,1) (2,2,1,1) (2,1,1,1,1)    D =  8.1851
    perm 1           (3,1,1,1) (2,2,2) (2,2,1,1) (1^6)        D = 11.7910
    perm 2           (4,1,1) (2,2,2) (2,2,1,1) (1^6)          D = 34.0392
    perm 3           (3,2,1) (3,1,1,1) (2,2,2) (1^6)          D =  8.1851

Same objective (AME) in all five. The kernel is a degenerate face: entries sit
at +/-M box bounds in near-cancelling combinations, and only the net matters.
Asking which partition "the debt" lands on is asking which vertex the simplex
method happened to stop at.

WHAT *IS* DETERMINED: the minimum debt
======================================
Since only the support pays, the cheapest way to reach a target `B` is to put
everything on the support block of largest cost. So the debt has a floor:

    D_min = B / max_{lambda in support} t_lambda  -  n_target
          = 2.224566 / 0.253938 - 0.575172
          = 8.185108                              (14.23x n_target)

attained on block `(5,1)`, and matching the smallest `D` observed above. This
is the invariant the interpretive question should attach to, if any: to reach
AME through this program the zero-weight sector must run a deficit of at least
14.2 times the entire net budget.

SCOPE -- (a) throughout
=======================
MEASURED: that `t` vanishes identically on the kernel and contributes exactly
zero to the objective; the ledger identity; that the negative set varies under
variable reordering while the objective does not; the value of `D_min`.

NOT claimed: that signed occupations are legitimate; that the deficit means
anything physical; that "debt to vacuum" is or is not the right reading -- what
is shown is only that the mechanism has the SHAPE of an unpriced debt, and that
no block carries it in particular. Nothing here refutes or supports any binding
conjecture, and nothing computes a binding contribution. Method 4 reaches AME
because AME is one of its equality constraints; that is not a prediction.

PRECISION NOTE
==============
The cost vector is read from the committed `deuteron-real-sdp.witness.json`,
where it is stored float64; the LP is solved by HiGHS, which is float64. The
findings here are structural (a set comparison, and a quantity that is zero by
the row cap rather than by measurement) plus one ratio reported to 8 figures --
none of them is a claim of agreement at the arithmetic floor.
"""

from __future__ import annotations

import json
import pathlib
import random
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from scipy.optimize import linprog  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()
mp.mp.dps = max(mp.mp.dps, 60)

HERE = pathlib.Path(__file__).resolve().parent
SDP = HERE.parent / "deuteron-real-sdp.witness.json"
ZERO = mp.mpf("1e-40")
BOX = 1e6


def solve_method4(t, g, n_target, ame, order):
    """Maximise t.x over {sum x = n_target, Gx >= 0, t.x = AME, |x| <= BOX},
    with the variables presented to the solver in `order`."""
    n = len(t)
    P = np.eye(n)[:, order]
    r = linprog(
        -(t @ P),
        A_ub=(-np.diag(g)) @ P, b_ub=np.zeros(n),
        A_eq=np.vstack([np.ones(n), t]) @ P, b_eq=np.array([n_target, ame]),
        bounds=[(-BOX, BOX)] * n, method="highs")
    return (P @ r.x) if r.success else None


def main() -> int:
    wb = WitnessBuilder("deuteron-negative-occupation-locality",
                        engine="python-exact")
    wb.set_description(
        "Retracts the causal claim that the kernel characters are why the "
        "full-space program reached AME: convention D's row cap makes t = 0 on "
        "every kernel block, so they contribute exactly zero to the objective. "
        "The mechanism is the plain-sum net constraint -- an unpriced deficit "
        "on zero-weight blocks. Which blocks carry it is NOT determined: "
        "permuting variable order moves the negative set while the objective is "
        "unchanged. What is determined is the floor D_min = AME/max_supp(t) - "
        "n_target = 8.185108, i.e. 14.23x the entire net budget.")

    sdp = json.loads(SDP.read_text())["data"]
    keys = sdp["partitions"]
    t_mp = [mp.mpf(str(x)) for x in sdp["cost_t_lambda"]]
    g_mp = [mp.mpf(str(x)) for x in sdp["frobenius_gram_diag"]]
    n_target = mp.mpf(str(sdp["n_target"]))
    ame = mp.mpf(str(sdp["B_D_AME_MeV"]))

    support = [i for i, x in enumerate(g_mp) if abs(x) > ZERO]
    kernel = [i for i, x in enumerate(g_mp) if abs(x) <= ZERO]

    max_t_kernel = max((abs(t_mp[i]) for i in kernel), default=mp.mpf(0))
    max_t_support = max(t_mp[i] for i in support)
    arg_max = keys[max(support, key=lambda i: t_mp[i])]
    d_min = ame / max_t_support - n_target

    t = np.array(sdp["cost_t_lambda"], float)
    g = np.array(sdp["frobenius_gram_diag"], float)
    nt_f, ame_f = float(n_target), float(ame)
    n = len(keys)

    runs, exact_mp = [], []
    orders = [("identity", list(range(n)))]
    for s_ in range(4):
        random.seed(s_)
        p_ = list(range(n))
        random.shuffle(p_)
        orders.append((f"perm{s_}", p_))

    for label, order in orders:
        x = solve_method4(t, g, nt_f, ame_f, order)
        if x is None:
            continue
        neg = sorted(keys[i] for i in kernel if x[i] < -1e-6)
        occ = [i for i in support if abs(x[i]) > 1e-6]
        # Every vertex concentrates the support on ONE block, so the deficit is
        # recoverable EXACTLY from the witness inputs -- D = AME/t_l - n_target
        # -- with no float64 LP output entering the witness.
        exact_D = (ame / t_mp[occ[0]] - n_target) if len(occ) == 1 else None
        exact_mp.append(exact_D)
        runs.append({
            "order": label,
            "occupied_support_blocks": [keys[i] for i in occ],
            "deficit_exact": mp.nstr(exact_D, 24) if exact_D else None,
            "deficit_over_n_target":
                mp.nstr(exact_D / n_target, 12) if exact_D else None,
            "negative_kernel_blocks": neg,
        })

    distinct = len({frozenset(r["negative_kernel_blocks"]) for r in runs})
    single = all(len(r["occupied_support_blocks"]) == 1 for r in runs)
    deficits = exact_mp   # full precision, not the 24-digit serialisation
    observed_min_debt = min(deficits)

    print(f"kernel blocks   : {len(kernel)}   max |t| over kernel = "
          f"{mp.nstr(max_t_kernel, 6)}")
    print(f"support blocks  : {len(support)}  max t = "
          f"{mp.nstr(max_t_support, 10)} on {arg_max}")
    print(f"D_min           = {mp.nstr(d_min, 10)}   "
          f"({mp.nstr(d_min / n_target, 6)}x n_target)")
    print()
    for r in runs:
        print(f"  {r['order']:9s} on={r['occupied_support_blocks'][0]:9s} "
              f"D={r['deficit_exact'][:9]:>9s} "
              f"neg={r['negative_kernel_blocks']}")
    print(f"\ndistinct negative sets over {len(runs)} orderings: {distinct}")

    # ── assertions ────────────────────────────────────────────────────────
    # A1 — THE RETRACTION. The kernel carries no cost at all, so its characters
    #      cannot be why the objective grew.
    wb.add_assertion(
        name="kernel_cost_is_identically_zero",
        computed=mp.nstr(max_t_kernel, 20), expected="0",
        tolerance="1e-40", unit="dimensionless",
        source="t_lambda = y_lambda * chi^lambda; convention D sets y = 0 for "
               "ell(lambda) > 2")

    # A2 — CONTROL against the vacuous reading "t is zero everywhere".
    wb.add_assertion(
        name="control_support_cost_is_not_zero",
        computed=mp.nstr(max_t_support, 20), expected="0.25393778300524394",
        tolerance="1e-12", unit="dimensionless",
        source="max over the four convention-D supported blocks, at (5,1)")

    # A3 — every vertex concentrates the support on ONE block. This is what
    #      makes the deficit exactly recoverable, and it is why the ledger
    #      identity below can be stated without a float64 LP output.
    wb.add_assertion(
        name="every_vertex_occupies_a_single_support_block",
        computed=repr(single), expected="True", tolerance="0", unit="boolean",
        source="occupied support blocks per ordering, |x| > 1e-6")

    # A4 — the ledger identity, exactly: occupying one support block at
    #      AME/t_l forces a kernel deficit of exactly AME/t_l - n_target.
    wb.add_assertion(
        name="ledger_identity_deficit_equals_support_minus_n_target",
        computed=mp.nstr(deficits[0] + n_target - ame / t_mp[
            keys.index(runs[0]["occupied_support_blocks"][0])], 20),
        expected="0", tolerance="1e-40", unit="dimensionless",
        source="sum x = n_target is a plain sum over ALL blocks")

    # A5 — THE LOCALITY FINDING: the negative set is not determined.
    wb.add_assertion(
        name="negative_kernel_set_is_not_determined",
        computed=str(distinct), expected="5", tolerance="0", unit="count",
        source="distinct negative-kernel sets across 5 variable orderings of "
               "the identical polytope")

    # A6 — CONTROL: every ordering solved to the SAME objective, so A5 is
    #      degeneracy of one problem and not five different problems. The
    #      objective is AME by the equality constraint, so this is checked
    #      structurally: t_l * (AME/t_l) = AME for the one occupied block.
    wb.add_assertion(
        name="control_objective_invariant_across_orderings",
        computed=mp.nstr(max(abs(t_mp[keys.index(r["occupied_support_blocks"][0])]
                                 * (d + n_target) - ame)
                             for r, d in zip(runs, deficits)), 20),
        expected="0", tolerance="1e-12", unit="dimensionless",
        source="every ordering attains t.x = B_D(AME2020)")

    # A7 — what IS determined: the floor on the deficit.
    wb.add_assertion(
        name="minimum_kernel_deficit",
        computed=mp.nstr(d_min, 20), expected="8.1851077",
        tolerance="1e-5", unit="dimensionless",
        source="D_min = AME / max_{support} t - n_target, attained on (5,1)")

    # A8 — CONTROL: no solved vertex beats the floor.
    wb.add_assertion(
        name="control_no_vertex_below_the_floor",
        computed=repr(bool(observed_min_debt >= d_min - mp.mpf("1e-30"))),
        expected="True", tolerance="0", unit="boolean",
        source="min observed deficit vs D_min")

    wb.add_data("kernel_blocks", [keys[i] for i in kernel])
    wb.add_data("support_blocks", [keys[i] for i in support])
    wb.add_data("max_abs_cost_on_kernel", mp.nstr(max_t_kernel, 30))
    wb.add_data("max_cost_on_support", mp.nstr(max_t_support, 30))
    wb.add_data("argmax_support_block", arg_max)
    wb.add_data("minimum_kernel_deficit", mp.nstr(d_min, 30))
    wb.add_data("minimum_deficit_over_n_target", mp.nstr(d_min / n_target, 30))
    wb.add_data("orderings", runs)
    wb.add_data("distinct_negative_sets", distinct)
    wb.add_caveat(
        "Scope (a). RETRACTS the causal claim in "
        "deuteron_cost_and_sign_structure_probe.py that the kernel is why the "
        "full-space program reached AME 'because the kernel is where the minus "
        "signs live'. The character-sign observation stands; the inference does "
        "not, since t vanishes identically on the kernel.")
    wb.add_caveat(
        "Method 4 attains AME because AME is one of its equality constraints. "
        "That is an imposed value, not a prediction, and nothing here computes "
        "a binding contribution or bears on whether signed occupations are "
        "legitimate.")
    wb.add_caveat(
        "Cost vector and LP are float64 (committed witness; HiGHS). The claims "
        "are structural -- a set comparison, and a quantity that is zero by the "
        "convention-D row cap rather than by measurement -- plus one ratio at 8 "
        "figures. No agreement at the arithmetic floor is asserted.")
    wb.save()
    print("\nwitness written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
