#!/usr/bin/env python3
"""The nuclear-jet level, the third of the three `prf:confined-knot-binding`
names (`qou-gpb5`). It HAS a word — and the word is the object the corpus
already retired as ill-posed, evaluated in a different trace family from the two
levels that work.

WHERE THE LEVEL IS ACTUALLY DEFINED
-----------------------------------
`confined-knot-binding` names it once and defines nothing:

    "For an A-nucleon system constructed sequentially through quark, nucleon,
     and nuclear jet levels, the character ratio measures the volume departure
     from the free constituents."

Searching the corpus for "nuclear jet" finds only that sentence, which is how
this bean nearly recorded "the level has no word". It does. Two blocks in the
same section define it, under a name the phrase does not contain:

  * `jet-filtered-knot-factor` gives the WORD — "the full bulk knot factor
    `a(Z,N)` equals the evaluated Jones polynomial of the nuclear quotient braid
    `J_bbeta(q)`", where the quotient "tracks exclusively the `A(A-1)/2`
    inter-nucleon crossings, suppressing internal nucleon structure".

  * `jet-convergence-classical-limit` gives the WEIGHTS — "at `k = 3` the
    jet-filtered knot invariant evaluates exactly using the q-deformed
    Wedderburn weights `W_lambda = d_q(lambda)^2 / [3]_q!`".

Both are labelled **Conjecture**. This probe measures what they specify.

FINDING 1 — AT A = 2 THE LEVEL IS WELL POSED, AND CONTRIBUTES EXACTLY 1
------------------------------------------------------------------------
`A(A-1)/2 = A-1 = 1` at two nucleons, so the quotient braid is a single crossing
on two strands and no ordering choice exists. Its closure is the **unknot** for
every bond type and for both resolutions of the averaged `pn` letter (which is
not a braid generator, so it must be resolved):

    2H  avg=+1  [(0,+1)]  J = 1      2He  J = 1      2n  J = 1
    2H  avg=-1  [(0,-1)]  J = 1

So the jet level multiplies the deuteron's knot factor by `1`. Where the
specification is evaluable, it adds **nothing**.

FINDING 2 — AT A >= 3 THE WORD IS NOT DETERMINED BY THE PAIR MULTISET
----------------------------------------------------------------------
`A(A-1)/2` inter-nucleon crossings is a MULTISET; a link needs a WORD, and the
non-adjacent pairs need bands that do not commute with the crossings they span.
Enumerated over every ordering of the pairs and both averaged resolutions:

    3H    A=3   12 orderings  ->   4 distinct Jones polynomials
    3He   A=3   12 orderings  ->   4 distinct Jones polynomials
    4He   A=4 1440 orderings  ->  30 distinct Jones polynomials

So `a(Z,N) = J_bbeta(q)` is **not a function of `(Z,N)`**. This is `qou-bygw`'s
ill-posedness — retired for the all-pairs bond model — reappearing as the
definition of the jet level, and measured here on the jet level's OWN object
(the `A`-strand quotient braid) rather than inherited from the `3A`-strand word.

FINDING 3 — THE WEIGHTS ARE A DIFFERENT FAMILY FROM THE TRACE THE OTHER LEVELS USE
-----------------------------------------------------------------------------------
The quark and nucleon levels are Markov traces: weights `y_lambda`, convention D
(Wenzl `r = 2`), which admits only `<= 2`-row shapes. The jet blocks specify
`w~_lambda = d_q(lambda)^2 / [n]_q!`, over ALL partitions. On `H_3`:

    lambda      y_lambda (D)          w~_lambda            ratio
    (3)         0.505404226503931     0.163383228056257    0.323
    (2,1)       0.247297886748035     0.660673773661173    2.672
    (1,1,1)     0                     0.163383228056257    infinite

`sum_lambda dim(lambda) y_lambda = 1` exactly (`tr_M(1) = 1`); `sum w~ =
0.98744`, so `w~` is not a normalised trace at `q0` (it is exactly 1 at `q = 1`).
The `(1,1,1)` row is structural, not numerical: convention D is the `sl_2` point
of the Ocneanu family, so `y_lambda = 0` identically once `lambda` has more than
two rows, while `w~` is a ratio of positive quantum integers. **The jet measure
charges a block the Markov trace annihilates.**

None of this is news to the corpus — `wedderburn-weight-canonical` tabulates
`y^D(q0) = 0.24729789` against `w~(q0) = 0.66067377` at `(2,1)`, the same two
numbers measured here, and states the two are distinct families on every
stratum. What is new is the consequence: **the three levels are not in one
convention, so their character ratios cannot simply be multiplied.**

FINDING 4 — THE TWO FAMILIES DISAGREE QUALITATIVELY ABOUT THE pn BOND
-----------------------------------------------------------------------
Not a rescale. On the single `pn` interface letter:

    tr_M(sigma + d_pn) under y  =  0.508229789376738963   (= z + d_pn)
    the same letter  under w~   =  0.000071511999728866   (7100x smaller)

`w~` weights the two `H_2` blocks EQUALLY, and `d_pn` is the midpoint of the two
eigenvalues up to `delta`, so `w~` sends the `pn` letter to
`w~ * (h + 2 d_pn) = w~ * h * delta/2` — a near-null vector. The `pn` bond is
the one the binding arc turns on, and the two families do not agree on whether
it is `0.51` or `0.00007`.

WHAT THIS SETTLES FOR qou-gpb5
------------------------------
The three-level character-ratio product `prf:confined-knot-binding` calls for is
**not evaluable as specified**, for two independent reasons either of which
suffices: its third factor is not a function of `(Z,N)` for `A >= 3`, and it is
defined in a trace family the other two factors do not use. Where it IS
evaluable, at `A = 2`, it contributes exactly `1`.

That closes the multi-level route as a derivation. It is a finding about the
specification, not a measurement of binding, and nothing here is tuned.

WHAT IS NOT CLAIMED
-------------------
No binding claim. Both jet blocks are labelled Conjecture and neither is
retracted here — a conjecture may be reformulated on a well-posed word and a
stated convention, and this probe says exactly what such a reformulation would
have to supply. Nothing about whether `w~` is the wrong weight; the corpus's own
`wedderburn-weight-canonical` establishes it as canonical for the BW and LP
scalings, which is a different job from being a trace. No claim that the k -> oo
convergence statement is false; it is untested here.
"""
from __future__ import annotations

import importlib.util
import itertools
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))
import _path_bridge  # noqa: F401,E402

import gmpy2  # noqa: E402
from gmpy2 import mpfr  # noqa: E402

import _exact_trace_engine as E  # noqa: E402
from hecke_characters import dim_q, partitions_of, qfac  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "tc", HERE / "total_curvature_is_the_computable_half_probe.py")
tc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tc)

TOL = mpfr("1e-40")
Q, H = E.Q, E.H


def s(v, n=18):
    """Decimal string with the point in the right place. `gmpy2.digits` returns
    a bare mantissa, which cannot be read for magnitude — the display bug that
    briefly made `[3]_q! = 6.12` look like `0.612` while writing this."""
    m, e, _ = gmpy2.digits(mpfr(v), 10, n)
    neg = m.startswith("-")
    m = m.lstrip("-")
    body = ("0." + "0" * (-e) + m) if e <= 0 else (m[:e] + "." + m[e:])
    return ("-" if neg else "") + body


def _call(fn, *a):
    """`dim_q`/`qfac` take q in some builds and bake it in others."""
    try:
        return fn(*a)
    except TypeError:
        return fn(*a[:-1])


def band(i, j):
    """Pair `(i, j)`, `i < j`, on the A-strand quotient: bring `j` down to
    `i+1`, cross at `i`, bring it back. `None` marks the crossing itself, whose
    sign is the bond's."""
    ups = list(range(j - 1, i, -1))
    return ([(g, +1) for g in ups] + [(i, None)]
            + [(g, -1) for g in reversed(ups)])


def quotient_braid(order, pair_order, avg_sign):
    """`jet-filtered-knot-factor`'s nuclear quotient braid: A strands, one per
    nucleon, carrying only the inter-nucleon crossings. `avg_sign` resolves the
    averaged `pn` letter, which is not a braid generator."""
    sign = {("p", "p"): +1, ("n", "n"): -1}
    w = []
    for (i, j) in pair_order:
        sg = sign.get((order[i], order[j]), avg_sign)
        for g, t in band(i, j):
            w.append((g, sg if t is None else t))
    return w


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    print(__doc__.split("\n")[0])
    print(f"\nengine: {E.BITS} bits, q from Q_50_DIGIT_STR")

    print("\n" + "=" * 76)
    print("§1  A = 2: THE LEVEL IS WELL POSED, AND ITS CLOSURE IS THE UNKNOT")
    print("=" * 76)
    unknot = {0: 1}
    all_unknot = True
    for order, nm in (("pn", "2H"), ("pp", "2He"), ("nn", "2n")):
        for avg in (+1, -1):
            w = quotient_braid(order, [(0, 1)], avg)
            J = tc.jones_closure(2, w)
            all_unknot &= (dict(J) == unknot)
            print(f"    {nm:5s} avg={avg:+d}   word {w}   J = {dict(J)}")
    check("at A = 2 the quotient braid closes to the UNKNOT (J = 1) for every "
          "bond type and both averaged resolutions — the jet level multiplies "
          "the knot factor by 1, i.e. contributes nothing", all_unknot)

    print("\n" + "=" * 76)
    print("§2  A >= 3: THE PAIR MULTISET DOES NOT DETERMINE THE JONES POLYNOMIAL")
    print("=" * 76)
    ndist = {}
    for order, nm in (("pnn", "3H"), ("ppn", "3He"), ("ppnn", "4He")):
        A = len(order)
        pairs = [(i, j) for i in range(A) for j in range(i + 1, A)]
        seen = set()
        n_ord = 0
        for perm in itertools.permutations(pairs):
            for avg in (+1, -1):
                n_ord += 1
                seen.add(tuple(sorted(
                    tc.jones_closure(A, quotient_braid(order, perm, avg)).items())))
        ndist[nm] = len(seen)
        print(f"    {nm:5s} A={A}  {len(pairs)} pairs  {n_ord:5d} orderings"
              f"  ->  {len(seen):3d} DISTINCT Jones polynomials")
    check("a(Z,N) = J(quotient braid) is NOT a function of (Z,N) at A >= 3 — the "
          "jet level's word is the ill-posed all-pairs object (qou-bygw)",
          all(v > 1 for v in ndist.values()))

    print("\n" + "=" * 76)
    print("§3  THE WEIGHTS ARE A DIFFERENT FAMILY FROM THE MARKOV TRACE")
    print("=" * 76)
    ps, ys = E.weights(3)
    y = {tuple(p): w for p, w in zip(ps, ys)}
    dims = {(3,): 1, (2, 1): 2, (1, 1, 1): 1}
    fac3 = mpfr(str(_call(qfac, 3, Q)))
    wt = {}
    for p in [tuple(p) for p in partitions_of(3)]:
        d = mpfr(str(_call(dim_q, list(p), Q)))
        wt[p] = d * d / fac3
    print(f"    [3]_q! = {s(fac3)}")
    print(f"    {'lambda':10s} {'y_lambda (D)':>22s} {'w~_lambda':>22s}")
    for p in [(3,), (2, 1), (1, 1, 1)]:
        yv = y.get(p, mpfr(0))
        print(f"    {str(p):10s} {s(yv):>22s} {s(wt[p]):>22s}")
    tr1 = sum(y[p] * dims[p] for p in y)
    sw = sum(wt.values())
    print(f"    sum dim*y = {s(tr1)}   <- tr_M(1) = 1")
    print(f"    sum w~    = {s(sw)}   <- not a normalised trace at q0")
    check("convention D EXCLUDES (1,1,1) (y = 0, the sl_2 point of the Ocneanu "
          "family) while w~ charges it — the jet measure weights a block the "
          "Markov trace annihilates",
          (1, 1, 1) not in y and wt[(1, 1, 1)] > mpfr("0.1"))
    check("sum_lambda dim(lambda) y_lambda = 1 exactly", abs(tr1 - 1) < TOL)
    check("sum w~ != 1 at q0, so w~ is not a normalised trace",
          abs(sw - 1) > mpfr("0.01"))
    check("and on the shapes BOTH admit the weights differ by more than 3x "
          "between the extremes — a different measure, not a correction",
          (wt[(2, 1)] / y[(2, 1)]) / (wt[(3,)] / y[(3,)]) > mpfr(3))

    print("\n" + "=" * 76)
    print("§4  AND THEY DISAGREE QUALITATIVELY ABOUT THE pn BOND")
    print("=" * 76)
    ps2, ys2 = E.weights(2)
    y2 = {tuple(p): w for p, w in zip(ps2, ys2)}
    fac2 = mpfr(str(_call(qfac, 2, Q)))
    wt2 = {}
    for p in [(2,), (1, 1)]:
        d = mpfr(str(_call(dim_q, list(p), Q)))
        wt2[p] = d * d / fac2
    chi = {(2,): Q + E.D_PN, (1, 1): -1 / Q + E.D_PN}
    mk = sum(y2[p] * chi[p] for p in chi)
    jt = sum(wt2[p] * chi[p] for p in chi)
    zpd = Q ** 3 / (Q ** 2 + 1) + E.D_PN
    print(f"    tr_M(sigma + d_pn) under y   = {s(mk)}   (z + d_pn = {s(zpd)})")
    print(f"    the same letter    under w~  = {s(jt)}")
    print(f"    ratio y/w~ = {s(mk / jt, 10)}")
    print(f"    w~ is EQUAL on both blocks ({s(wt2[(2,)], 12)}), and "
          f"h + 2 d_pn = {s(H + 2 * E.D_PN)} = h*delta/2")
    check("the Markov value is z + d_pn exactly", abs(mk - zpd) < TOL)
    check("under w~ the pn letter is more than 1000x smaller — w~ weights the "
          "two blocks equally and d_pn is their midpoint up to delta, so pn is "
          "w~'s near-null vector", mk / jt > mpfr(1000))

    print("\n" + "=" * 76)
    print("§S  WHAT THIS SETTLES FOR qou-gpb5")
    print("=" * 76)
    print("  The nuclear-jet level HAS a word — the corpus defines it, under a")
    print("  name the phrase 'nuclear jet' does not contain. The three-level")
    print("  product is nevertheless NOT evaluable as specified, for two")
    print("  independent reasons either of which suffices:")
    print("    1. its third factor is not a function of (Z,N) for A >= 3;")
    print("    2. it is defined in a trace family the other two do not use,")
    print("       one that charges a block the Markov trace annihilates.")
    print("  Where it IS evaluable, at A = 2, it contributes exactly 1.")
    print("  Both jet blocks are Conjectures and neither is retracted: this")
    print("  says what a reformulation would have to supply.")

    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="python")
        # Declared 2026-09-05 (qou-i229). This probe IS the producer
        # `prop:confined-knot-binding` names in its own text, but declared no
        # contentBlock, so nothing could check the block against it.
        wb.set_content_block("prop:confined-knot-binding")
        wb.set_description(
            "Evaluates the nuclear-jet level, the third of the three levels "
            "prf:confined-knot-binding names. It is defined by jet-filtered-knot-factor "
            "(word: the Jones polynomial of the nuclear quotient braid on the A(A-1)/2 "
            "inter-nucleon crossings) and jet-convergence-classical-limit (weights "
            "w~_lambda = d_q(lambda)^2/[n]_q!). At A = 2 the quotient braid closes to the "
            "unknot, J = 1, for every bond type and both resolutions of the averaged pn "
            "letter, so the level contributes exactly 1. At A >= 3 the pair multiset does "
            "not determine the word: 4 distinct Jones polynomials over 12 orderings at "
            "A = 3, 30 over 1440 at A = 4, so a(Z,N) = J is not a function of (Z,N). And "
            "the weights are a different family from the Markov trace the quark and "
            "nucleon levels use: convention D excludes (1,1,1) with y = 0 while w~ charges "
            "it at 0.1634, sum dim*y = 1 but sum w~ = 0.98744, and on the single pn letter "
            "y gives 0.508229789376739 against w~'s 0.000071511999729, a factor of 7105. "
            "The three-level product is therefore not evaluable as specified. No binding "
            "claim; both jet blocks are Conjectures and neither is retracted.")
        for nm, v in ndist.items():
            wb.add_data(f"distinct_jones_{nm}", str(v))
        wb.add_data("pn_letter_under_y", s(mk, 25))
        wb.add_data("pn_letter_under_wtilde", s(jt, 25))
        wb.add_data("sum_wtilde_H3", s(sw, 25))
        # Added 2026-09-05 (qou-i229). This probe computed the H_3 weight table
        # and PRINTED it, and `prop:confined-knot-binding` publishes all six of
        # its entries -- but the witness recorded only the two pn-letter values,
        # so four published figures had no provenance. My own gap, from the same
        # day, and the same class this bean recorded for 1.064088425325:
        # witness the figure, do not delete it.
        wb.add_data("h3_weight_table", {
            str(p): {
                "y_lambda_conventionD": s(y.get(p, mpfr(0)), 25),
                "w_tilde_lambda": s(wt[p], 25),
            }
            for p in [(3,), (2, 1), (1, 1, 1)]
        })
        wb.add_data("sum_dim_times_y_H3", s(tr1, 25))
        for name, ok in checks:
            wb.add_assertion(name=name, computed=str(int(ok)), expected="1")
        wb.add_caveat(
            "Both source blocks are labelled Conjecture. Neither is retracted here; the "
            "probe reports what they specify and what a well-posed reformulation would "
            "have to supply.")
        wb.add_caveat(
            "The k -> infinity convergence claim of jet-convergence-classical-limit is "
            "NOT tested. Only the k = 3 exactness claim's weights are.")
        wb.add_caveat(
            "No binding claim. B = alpha L remains the open interpretation of "
            "rem:bond-log-ratio-is-a-free-energy.")
        print(f"\nWitness: {wb.save()}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok in checks if not ok]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
