#!/usr/bin/env python3
"""The two remaining escapes, quantified — and a correction to the first.

Bean qou-6tcn. `deuteron_support_reachability_probe.py` bounded the deuteron
objective at `max(t)*n_target = 0.146058` against `B_D(AME2020) = 2.224566`,
and `deuteron_reachability_vs_level_probe.py` closed the "different level"
escape. Two escapes remain: a **different cost**, and **signed occupations**.
This probe measures what each actually requires. It chooses neither.

CORRECTION TO THE COST ESCAPE AS PREVIOUSLY STATED
==================================================
It was reported as "at the canonical level a cost reaching AME needs
`max(t) >= AME/n_target = 3.8677` against the actual `0.2539`, a factor of
15.23x -- the same ratio read from either end with `n_target` fixed."

**`n_target` cannot be held fixed.** It is not an independent input:

    n_target = tr_M(beta_D) = sum_lambda y_lambda chi^lambda = sum_lambda t_lambda

The net-constraint target IS the sum of the cost vector, verified below to
8e-17. So the ceiling is

    ceiling = max(t) * sum(t)

-- quadratic in the cost, not linear. A uniform rescale `t -> c*t` scales it by
`c^2`, so it needs `c = sqrt(15.2307) = 3.903`, not 15.23. The 15.23 was
correct only for an impossible variation that moves `max(t)` while pinning
`sum(t)`.

WHAT A COST CHANGE CAN AND CANNOT BUY
=====================================
Since `ceiling = max(t) * sum(t)`, a redistribution of the cost at FIXED total
`sum(t)` is maximised by concentrating everything on a single block, giving
`ceiling = (sum t)^2`. That is the best any reshaping can do:

    actual ceiling        0.146058
    concentrated ceiling  0.330823      (2.265x better -- the whole budget)
    AME                   2.224566      STILL SHORT BY 6.72x

So the constraint is not on the cost's SHAPE. It is on `tr_M(beta_D)` itself:
even a perfectly concentrated cost needs `sum(t) >= sqrt(AME) = 1.491`, against
the actual `0.575` -- the Markov trace of the deuteron braid would have to be
**2.59x larger**. That is a derived quantity, not a free parameter.

WHERE THE SIGN STRUCTURE WENT
=============================
`chi^lambda(beta_D)` at `n = 6` takes both signs. Sorted by whether convention
D gives the block a nonzero weight:

    support (4 blocks)   chi = +1.560, +3.216, +1.674, +4.249   ALL POSITIVE
    kernel  (7 blocks)   chi = -0.470, -1.972, -0.490, -3.497,
                               -0.820, +2.156, -0.677           SIX NEGATIVE

**Every negative character is in the kernel; the support has none.** The
convention-D row cap `ell(lambda) <= 2` zeroes exactly the blocks carrying the
sign structure.

  RETRACTED, same bean, by `deuteron_negative_occupation_locality_probe.py`.
  This paragraph continued: "That is why the full-space program could reach AME
  and the projected one cannot: not merely because the kernel is unconstrained,
  but because the kernel is *where the minus signs live*." That inference is
  causally wrong. Since `t_lambda = y_lambda * chi^lambda` and the row cap sets
  `y_lambda = 0` on every kernel block, `t` vanishes IDENTICALLY there --
  `max |t|` over the kernel is `0.0`, and `t . x` restricted to the kernel is
  `0.0` in every solution measured. A block contributing nothing to the
  objective cannot be why the objective grew. The actual mechanism is the
  plain-sum net constraint: a kernel deficit buys the support extra budget, and
  the characters play no part in it. The observation above -- that the negative
  characters all sit in the kernel -- stands, and assertions A6/A7 below are
  unaffected; only the causal reading is withdrawn.

SCOPE -- (a) throughout
=======================
MEASURED: the identity `n_target = sum(t)`; that the committed
support-restricted optimum is exactly `min(t)*n_target`; the concentration
bound; the trace factor required; the character signs by sector.

NOT claimed: that a cost with a larger trace exists or is derivable; that
signed occupations are justified; that the kernel characters SHOULD be
occupied; that any binding conjecture is true or false. In particular the
sign observation is a statement about **where the negative characters sit**,
not an argument that a program should reach them. Nothing here computes a
binding contribution.
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
mp.mp.dps = max(mp.mp.dps, 60)

HERE = pathlib.Path(__file__).resolve().parent
SDP = HERE.parent / "deuteron-real-sdp.witness.json"
COST = HERE.parent / "iterative-lp-dual-h6-deuteron.witness.json"
ZERO = mp.mpf("1e-40")


def main() -> int:
    wb = WitnessBuilder("deuteron-cost-and-sign-structure", engine="python-exact")
    wb.set_description(
        "Quantifies the two escapes left after the level sweep. Corrects the "
        "cost figure: n_target = sum(t), so the ceiling is max(t)*sum(t), "
        "quadratic in the cost -- a uniform rescale needs 3.903x, not 15.23x. "
        "Even a perfectly concentrated cost at the current trace falls 6.72x "
        "short, so the constraint is on tr_M(beta_D) itself (2.59x larger). "
        "And every negative character sits in the convention-D kernel: the row "
        "cap zeroes exactly the blocks carrying the sign structure.")

    sdp = json.loads(SDP.read_text())["data"]
    chi = {k: mp.mpf(str(v)) for k, v in
           json.loads(COST.read_text())["data"]["chi_lambda_beta_D_at_q0"].items()}
    keys = sdp["partitions"]
    t = [mp.mpf(str(x)) for x in sdp["cost_t_lambda"]]
    g = [mp.mpf(str(x)) for x in sdp["frobenius_gram_diag"]]
    n_target = mp.mpf(str(sdp["n_target"]))
    ame = mp.mpf(str(sdp["B_D_AME_MeV"]))

    support = [i for i, x in enumerate(g) if abs(x) > ZERO]
    kernel = [i for i, x in enumerate(g) if abs(x) <= ZERO]
    sum_t = mp.fsum(t)
    t_min = min(t[i] for i in support)
    t_max = max(t[i] for i in support)
    ceiling = t_max * n_target
    floor_ = t_min * n_target
    concentrated = sum_t ** 2

    neg_sup = sum(1 for i in support if chi[keys[i]] < 0)
    neg_ker = sum(1 for i in kernel if chi[keys[i]] < 0)

    print(f"n_target        = {mp.nstr(n_target, 22)}")
    print(f"sum(t)          = {mp.nstr(sum_t, 22)}     <- the same object")
    print(f"reachable t.x   = [{mp.nstr(floor_, 12)}, {mp.nstr(ceiling, 12)}]")
    print(f"concentrated    =  {mp.nstr(concentrated, 12)}  (best possible shape)")
    print(f"AME             =  {mp.nstr(ame, 12)}")
    print(f"\nuniform rescale needed : {mp.nstr(mp.sqrt(ame / ceiling), 8)}x  (NOT 15.23)")
    print(f"short even concentrated: {mp.nstr(ame / concentrated, 8)}x")
    print(f"tr_M would need        : {mp.nstr(mp.sqrt(ame) / n_target, 8)}x larger")
    print(f"\nnegative chi in support: {neg_sup}   in kernel: {neg_ker}")

    # ── assertions ────────────────────────────────────────────────────────
    # A1 — THE CORRECTION. n_target is not independent of t; it IS sum(t).
    wb.add_assertion(
        name="n_target_equals_sum_of_cost",
        computed=mp.nstr(abs(n_target - sum_t), 20), expected="0",
        tolerance="1e-15", unit="dimensionless",
        source="tr_M(beta_D) = sum_l y_l chi^l = sum_l t_l")

    # A2 — CONTROL, and an independent validation of the whole picture: the
    #      committed support-restricted optimum is exactly min(t)*n_target,
    #      which is what a convex combination over the support must give.
    committed = mp.mpf(str(
        sdp["support_restricted"]["lp"]["primal_obj"]))
    wb.add_assertion(
        name="control_committed_optimum_is_min_t_times_n_target",
        computed=mp.nstr(abs(committed - floor_), 20), expected="0",
        tolerance="1e-12", unit="dimensionless",
        source="deuteron-real-sdp.witness.json support_restricted.lp")

    # A3 — a uniform rescale needs sqrt, not the linear factor.
    wb.add_assertion(
        name="uniform_rescale_factor_is_sqrt_of_shortfall",
        computed=mp.nstr(mp.sqrt(ame / ceiling), 20), expected="3.9026538",
        tolerance="1e-5", unit="ratio",
        source="ceiling = max(t)*sum(t) is quadratic under t -> c*t")

    # A4 — reshaping the cost at fixed total cannot close it either.
    wb.add_assertion(
        name="concentrated_cost_still_short",
        computed=mp.nstr(ame / concentrated, 20), expected="6.7243369",
        tolerance="1e-5", unit="ratio",
        source="ceiling <= (sum t)^2, attained by concentrating on one block")

    # A5 — so the constraint is on the trace itself.
    wb.add_assertion(
        name="required_trace_growth_factor",
        computed=mp.nstr(mp.sqrt(ame) / n_target, 20), expected="2.5931326",
        tolerance="1e-5", unit="ratio",
        source="sum(t) >= sqrt(AME) even for a concentrated cost")

    # A6 — THE SIGN FINDING: no negative character survives in the support.
    wb.add_assertion(
        name="no_negative_character_in_support",
        computed=str(neg_sup), expected="0", tolerance="0", unit="count",
        source="chi^lambda(beta_D) over the convention-D supported blocks")

    # A7 — and they are not merely absent: six of them are in the kernel.
    #      CONTROL against the vacuous reading "there are no negative chi".
    wb.add_assertion(
        name="control_negative_characters_exist_in_kernel",
        computed=str(neg_ker), expected="6", tolerance="0", unit="count",
        source="chi^lambda(beta_D) over the zero-weight blocks")

    wb.add_data("n_target", mp.nstr(n_target, 30))
    wb.add_data("sum_t", mp.nstr(sum_t, 30))
    wb.add_data("reachable_interval",
                [mp.nstr(floor_, 30), mp.nstr(ceiling, 30)])
    wb.add_data("concentrated_ceiling", mp.nstr(concentrated, 30))
    wb.add_data("uniform_rescale_factor", mp.nstr(mp.sqrt(ame / ceiling), 30))
    wb.add_data("required_trace_growth", mp.nstr(mp.sqrt(ame) / n_target, 30))
    wb.add_data("chi_by_sector", {
        "support": {keys[i]: mp.nstr(chi[keys[i]], 20) for i in support},
        "kernel": {keys[i]: mp.nstr(chi[keys[i]], 20) for i in kernel},
    })
    wb.add_caveat(
        "Scope (a). The sign observation locates WHERE the negative characters "
        "sit; it is not an argument that a program should occupy them, and it "
        "does not justify signed occupations. Nothing here claims a cost with "
        "a larger trace exists or is derivable, and nothing computes a binding "
        "contribution.")
    wb.add_caveat(
        "Supersedes the '15.23x on max(t)' figure reported earlier for the "
        "cost escape. That held n_target fixed, which is impossible since "
        "n_target = sum(t). The correct uniform-rescale factor is 3.903x, and "
        "reshaping at fixed total cannot close the gap at all.")
    wb.save()
    print("\nwitness written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
