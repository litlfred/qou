#!/usr/bin/env python3
"""The zero-weight sector is not unpriced -- it is the Temperley-Lieb ideal.

Bean qou-6tcn. Third correction in this arc to my own framing of the same
object, and this one comes from the corpus rather than from a new measurement.

WHAT I ASKED, AND WHY IT WAS THE WRONG QUESTION
===============================================
`deuteron_negative_occupation_locality_probe.py` found that the convention-D
zero-weight blocks are free in the objective (`t = 0`) AND free in the
Frobenius cone (`G = 0`), and I described the resulting kernel deficit as an
"unpriced overdraft" -- asking what could price it.

**Nothing can, and nothing should.** Per
`prop:markov-trace-frobenius-selection` (iii), stated there UNCONDITIONALLY:

    the radical of <x,y>_tau := tr_M(xy) is exactly the Temperley-Lieb ideal
    I_n = ker(H_n(q) --> TL_n(q)), neither larger nor smaller ... It is
    (TL_n(q), tr_M), NOT (H_n(R,q), tr_M), that is a symmetric Frobenius
    algebra.

So the seven zero-weight blocks are not blocks the trace forgot to charge for.
They span `I_6`, and the Frobenius algebra the trace actually lives on is the
quotient `TL_6(q) = H_6(q)/I_6`, where the pairing is NON-DEGENERATE. A
negative occupation of a zero-weight block is not a debt against the vacuum;
it is an occupation of a direction that is not in the algebra.

MEASURED HERE (the corpus states it; this checks it)
====================================================
If the convention-D support really is `TL_6`, its squared dimensions must sum
to the Catalan number, not merely to "less than 6!":

    sum over ell(lambda) <= 2  of (f^lambda)^2  =  132  =  Catalan(6) = dim TL_6
    sum over all lambda |- 6   of (f^lambda)^2  =  720  =  6!         = dim H_6
    sum over ell(lambda) >= 3  of (f^lambda)^2  =  588  =  720 - 132  = dim I_6

and it does, exactly. Checked at `n = 2..8` (7/7) so the identification is not
an `n = 6` coincidence.

WHAT THIS CLOSES
================
The signed-occupation escape, entirely -- and not by argument. On the support
`G` is STRICTLY positive, so `Gx >= 0` IS `x >= 0` there; the sector that
supplied the signs is `I_6`, which is not in the Frobenius algebra. There is
nothing left to sign. So the support projection reported in
`deuteron_support_reachability_probe.py` -- which I described as "a modelling
decision, stated not smuggled" -- is not a modelling decision at all. It is the
quotient map `H_6 --> TL_6`, and the six encodings are infeasible in the actual
Frobenius algebra rather than in a restricted model of it. The negative is
stronger than reported, not weaker.

It also inverts the search. "Widen the level to give the kernel a weight" is
backwards: (ii) of the same proposition makes the row cap the INPUT -- the
SU_q(2) fibre supplies no channel with ell(lambda) >= 3 -- and it is the row cap
that SELECTS `z = q^3/(q^2+1)`, i.e. convention D. And (i) rules out the other
route I had in mind: non-degeneracy "singles out nothing", since every weight
vector with all `w_lambda != 0` induces a non-degenerate form. A generic
Ocneanu `z` does make the pairing non-degenerate on all of `H_6` -- and that is
precisely why it cannot be a selection principle.

SCOPE -- (a) throughout
=======================
MEASURED: the dimension identities above at n = 2..8; that convention D's Gram
is strictly positive on the support and exactly zero off it; that the split is
exactly `ell(lambda) <= 2`.

NOT claimed: that `prop:markov-trace-frobenius-selection` (ii) holds -- its
antecedent (that the mass-channel trace IS the categorical trace of the fibre
action) is open, bean `qou-n1dj`, and this probe does not bear on it. (i) and
(iii), which are what is used here, are unconditional in the corpus. Nothing
here computes a binding contribution, refutes or supports any binding
conjecture, or claims the framework can or cannot reach AME.
"""

from __future__ import annotations

import json
import pathlib
import sys
from math import comb, factorial

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

HERE = pathlib.Path(__file__).resolve().parent
SDP = HERE.parent / "deuteron-real-sdp.witness.json"
ZERO = mp.mpf("1e-40")


def partitions(n, mx=None):
    mx = mx or n
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def hook_dim(lam):
    """Number of standard Young tableaux of shape lam (exact integer)."""
    n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= (row - j) + (conj[j] - i) - 1
    return factorial(n) // prod


def catalan(n):
    return comb(2 * n, n) // (n + 1)


def main() -> int:
    wb = WitnessBuilder("zero-weight-sector-is-temperley-lieb",
                        engine="python-exact")
    wb.set_description(
        "The convention-D zero-weight sector is the Temperley-Lieb ideal I_n, "
        "not an unpriced sector: the support's squared dimensions sum to "
        "Catalan(n) = dim TL_n exactly, at n = 2..8. Per "
        "prop:markov-trace-frobenius-selection (iii), (TL_n, tr_M) is the "
        "symmetric Frobenius algebra and the pairing is non-degenerate there. "
        "This closes the signed-occupation escape -- G is strictly positive on "
        "the support, so Gx >= 0 IS x >= 0 -- and makes the support projection "
        "the quotient map H_n -> TL_n rather than a modelling choice.")

    # ── the dimension identity, n = 6 and then generally ──────────────────
    n = 6
    lams = list(partitions(n))
    dims = {lam: hook_dim(lam) for lam in lams}
    two_row = [lam for lam in lams if len(lam) <= 2]
    deep = [lam for lam in lams if len(lam) >= 3]
    sum_sup = sum(dims[l] ** 2 for l in two_row)
    sum_all = sum(dims[l] ** 2 for l in lams)
    sum_ker = sum(dims[l] ** 2 for l in deep)

    general = [(m,
                sum(hook_dim(l) ** 2 for l in partitions(m) if len(l) <= 2),
                catalan(m)) for m in range(2, 9)]
    n_match = sum(1 for _, a, b in general if a == b)

    # ── convention D's Gram, from the committed witness ───────────────────
    sdp = json.loads(SDP.read_text())["data"]
    keys = sdp["partitions"]
    g = {k: mp.mpf(str(v)) for k, v in
         zip(keys, sdp["frobenius_gram_diag"])}
    pos = [k for k in keys if g[k] > ZERO]
    zer = [k for k in keys if abs(g[k]) <= ZERO]
    min_g_support = min(g[k] for k in pos)
    max_abs_g_kernel = max((abs(g[k]) for k in zer), default=mp.mpf(0))
    # does the sign of G track the row count, block for block?
    cap_agrees = sum(
        1 for k in keys
        if (len(eval(k)) <= 2) == (g[k] > ZERO))   # noqa: S307 -- our own data

    print(f"n = {n}:  dim H_n = {sum_all} = {n}!")
    print(f"          support (ell<=2)  sum f^2 = {sum_sup} "
          f"= Catalan({n}) = {catalan(n)} = dim TL_{n}")
    print(f"          kernel  (ell>=3)  sum f^2 = {sum_ker} = dim I_{n}")
    print()
    print(f"  {'n':>2} {'n!':>7} {'sum f^2 (l<=2)':>15} {'Catalan(n)':>11}")
    for m, a, b in general:
        print(f"  {m:>2} {factorial(m):>7} {a:>15} {b:>11}   {a == b}")
    print()
    print(f"Gram: min over support = {mp.nstr(min_g_support, 10)} > 0  "
          f"=> Gx >= 0 IS x >= 0 on TL_{n}")
    print(f"      max |G| over kernel = {mp.nstr(max_abs_g_kernel, 6)}")

    # ── assertions ────────────────────────────────────────────────────────
    # A1 — THE IDENTIFICATION. Not "smaller than 6!" but exactly Catalan.
    wb.add_assertion(
        name="support_dimension_is_temperley_lieb",
        computed=str(sum_sup), expected=str(catalan(n)),
        tolerance="0", unit="dimension",
        source="sum of (f^lambda)^2 over ell(lambda) <= 2, vs Catalan(6)")

    # A2 — CONTROL. The same sum over ALL blocks is 6!, so A1 is a genuine
    #      proper subalgebra dimension and not an artefact of the dimension
    #      formula being wrong.
    wb.add_assertion(
        name="control_all_blocks_give_the_full_algebra",
        computed=str(sum_all), expected=str(factorial(n)),
        tolerance="0", unit="dimension",
        source="Wedderburn: sum of (f^lambda)^2 over all lambda |- 6 = 6!")

    # A3 — so the kernel is exactly the ideal's dimension.
    wb.add_assertion(
        name="kernel_dimension_is_the_temperley_lieb_ideal",
        computed=str(sum_ker), expected=str(factorial(n) - catalan(n)),
        tolerance="0", unit="dimension",
        source="dim I_6 = dim H_6 - dim TL_6")

    # A4 — CONTROL against an n = 6 coincidence: the identity is general.
    wb.add_assertion(
        name="control_catalan_identification_holds_for_n_2_to_8",
        computed=str(n_match), expected="7", tolerance="0", unit="count",
        source="sum f^2 over two-row partitions vs Catalan(n), n = 2..8")

    # A5 — CONTROL against the vacuous reading "there is no kernel".
    wb.add_assertion(
        name="control_kernel_is_nonempty_at_n_6",
        computed=str(len(deep)), expected="7", tolerance="0", unit="count",
        source="partitions of 6 with at least three rows")

    # A6 — WHAT IT CLOSES: on TL the cone constraint is plain non-negativity,
    #      so no signed occupation is available there.
    wb.add_assertion(
        name="gram_strictly_positive_on_the_support",
        computed=repr(bool(min_g_support > ZERO)), expected="True",
        tolerance="0", unit="boolean",
        source="min of frobenius_gram_diag over the convention-D support")

    # A7 — CONTROL: and exactly zero off it, so the split is sharp.
    wb.add_assertion(
        name="control_gram_exactly_zero_on_the_kernel",
        computed=mp.nstr(max_abs_g_kernel, 20), expected="0",
        tolerance="1e-40", unit="dimensionless",
        source="max |frobenius_gram_diag| over the zero-weight blocks")

    # A8 — and the two ways of naming the split agree block for block.
    wb.add_assertion(
        name="row_cap_and_gram_support_agree_blockwise",
        computed=str(cap_agrees), expected=str(len(keys)),
        tolerance="0", unit="count",
        source="(ell(lambda) <= 2) iff (G_lambdalambda > 0), over all 11 blocks")

    wb.add_data("n", n)
    wb.add_data("dim_H_n", sum_all)
    wb.add_data("dim_TL_n", sum_sup)
    wb.add_data("dim_I_n", sum_ker)
    wb.add_data("support_partitions", [str(l) for l in two_row])
    wb.add_data("kernel_partitions", [str(l) for l in deep])
    wb.add_data("catalan_check",
                [{"n": m, "sum_f_squared_two_row": a, "catalan": b,
                  "match": a == b} for m, a, b in general])
    wb.add_data("min_gram_on_support", mp.nstr(min_g_support, 30))
    wb.add_caveat(
        "Scope (a). Uses parts (i) and (iii) of "
        "prop:markov-trace-frobenius-selection, which the corpus states "
        "UNCONDITIONALLY. Part (ii) -- that the row cap follows from the "
        "mass-channel trace being the categorical trace of the SU_q(2) fibre "
        "action -- has an OPEN antecedent (bean qou-n1dj) and is neither used "
        "nor supported here.")
    wb.add_caveat(
        "Corrects this arc's own framing twice over: the zero-weight sector is "
        "not an 'unpriced overdraft' (nothing prices a radical -- the algebra "
        "is the quotient), and the support projection is not a modelling "
        "decision but the quotient map H_6 -> TL_6.")
    wb.add_caveat(
        "Nothing here computes a binding contribution or bears on whether the "
        "framework can reach AME. It establishes WHERE the program lives, not "
        "what it yields.")
    wb.save()
    print("\nwitness written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
