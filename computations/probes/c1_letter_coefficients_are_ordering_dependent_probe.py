"""`c1_from_letters` SURVIVES the Borromean ruling — only its two letter weights move.

BEAN qou-j1e5, STEP 3 — the step the bean called the research part
------------------------------------------------------------------
`7db032fb48` (owner ruling, bean `qou-hu1f`) flipped `atom_braid_word_3A`'s
default intra ordering from `grouped` to `borromean`, and the six recorded `c1`
values stopped matching what the probe computes. `qou-j1e5` scoped the repair in
four steps and flagged step 3 as the one that "cannot be scoped without
attempting it":

> Establish whether `c1_from_letters` survives. Its per-letter derivation is
> measured grouped-specific ... So the DERIVATION, not merely the numbers, may
> need rebuilding.

IT SURVIVES, WHOLE. The closed form

    c1(Z,N) = (a.Z + b.N)(2^-(A+1) - 2^-2A) - 4(i_pp - i_nn).2^-2A
    with i_pp = max(Z-1,0), i_nn = max(N-1,0), A = Z+N

is correct under BOTH orderings. Only the pair (a, b) moves:

    grouped     (a, b) = ( 21,  16)
    borromean   (a, b) = (  3,  -2)      <- the neutron weight goes NEGATIVE

WHERE (a, b) COMES FROM — measured, not fitted
----------------------------------------------
PR #6919 established that the word-level `f1/f0` is exactly additive across the
two nucleons: they occupy disjoint strand sets, so `tr_M` factorises
(`braids-and-knots/markov-axioms-primitive.md`). Measured here, that additivity
holds under BOTH orderings -- it comes from INTER-nucleon disjointness and is
untouched by the INTRA ordering. So each ordering has its own per-nucleon pair

    phi_p = v(pp)/2 ,  phi_n = v(nn)/2 ,  with  phi_p + phi_n = v(pn)

and (a, b) = (2.phi_p, 2.phi_n). Both pairs are READ OFF two like-nucleon words,
not tuned against the six targets. Then the six targets are checked.

    grouped     v(pp)=21  v(pn)=37/2  v(nn)=16   ->  (21, 16)
    borromean   v(pp)= 3  v(pn)= 1/2  v(nn)=-2   ->  ( 3, -2)

THE `37` CANCELLATION IS STRUCTURAL, NOT NUMEROLOGY -- and that is the sharper
result here. `PairwiseChainLeadingOrder.lean` calls the 4He ratio "the striking
one -- 259 = 7.37 and 888 = 24.37, so the 37 cancels and the ratio is exactly
24/7". Symbolically, for ANY (a, b):

    sum of pair c1   = 3(a+b)/16                 (pp + pn + nn, the interface
                                                  terms +1 and -1 cancelling)
    4He atom c1      = 2(a+b).7/256 = 7(a+b)/128
    ratio            = 24/7,  the (a+b) cancelling IDENTICALLY

So `37` is just `a + b`, `259 = 7.37` holds by construction, and **24/7 is
ordering-invariant**. The Lean file's headline conclusion is therefore STRONGER
than it was stated to be -- it is a structural identity of the closed form, not a
coincidence of six measured rationals. The T and 3He ratios are NOT invariant
(they depend on a and b separately), which is what makes the 4He cancellation
worth naming rather than a general fact about all three.

SCOPE
-----
Scope-(a). Two orderings, A = 2 and 3 measured directly and A = 4 by the closed
form; `include_inter=False` for the per-nucleon reads, matching #6919. This says
the closed form's SHAPE survives; it does not re-derive the shape from the
permutation count, which is `LeadingOrderTraceCoefficient`'s job and unchanged.

NO FLOAT: exact `fractions.Fraction` throughout.
"""
from __future__ import annotations

import os
import sys
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMP = os.path.dirname(_HERE)
for _p in (_COMP, _HERE, os.path.join(_COMP, "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from word_level_trace_entry_point import log_derivative        # noqa: E402
from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402

CASES = (("pp", (2, 0)), ("pn", (1, 1)), ("nn", (0, 2)),
         ("T", (1, 2)), ("3He", (2, 1)), ("4He", (2, 2)))

# The six c1 values each ordering must reproduce.
#
# GROUPED: the values recorded on main (PairwiseChainLeadingOrder.lean, RECORDED
# in the c1 probe). All six are independent of anything computed here, so all six
# rows are a genuine test.
#
# BORROMEAN: FIVE are measured -- re-running `c1_leading_coefficient_derived_probe`
# on main gives pp 1/8, pn 1/16, nn 0, T 1/64, 3He 1/8, and those five are what
# the closed form is tested against.
#
# 4He: PREDICTED 7/128 from the closed form at (a,b) = (3,-2) BEFORE it was
# measured, then CONFIRMED by the n=12 run — twice over, since that probe
# computes it two independent ways and both agree:
#
#     4He  A=4   a0=c0 = 7/128   c1 exact = 7/128   c1 [permutation count] = 7/128
#
# An earlier revision of this file marked that row circular, because the
# confirming run had not returned when it was written. It has; the row is a real
# test and the caveat is withdrawn. Recorded rather than quietly deleted: the
# prediction came first, which is the only reason it is worth anything.

TARGETS = {
    "grouped": {"pp": F(19, 8), "pn": F(37, 16), "nn": F(9, 4),
                "T": F(163, 64), "3He": F(85, 32), "4He": F(259, 128)},
    "borromean": {"pp": F(1, 8), "pn": F(1, 16), "nn": F(0),
                  "T": F(1, 64), "3He": F(1, 8), "4He": F(7, 128)},
}


def closed_form(a: F, b: F, Z: int, N: int) -> F:
    A = Z + N
    i_pp, i_nn = max(Z - 1, 0), max(N - 1, 0)
    return (a * Z + b * N) * (F(2) ** (-A - 1) - F(2) ** (-2 * A)) \
        - 4 * (i_pp - i_nn) * F(2) ** (-2 * A)


def main() -> int:
    failures = []

    print("per-nucleon weights, READ OFF the two like-nucleon words "
          "(not fitted to the six targets):")
    weights = {}
    for order in ("grouped", "borromean"):
        v = {}
        for lbl, (Z, N) in (("pp", (2, 0)), ("pn", (1, 1)), ("nn", (0, 2))):
            v[lbl] = log_derivative(
                atom_canonical_crossings(Z, N, include_inter=False,
                                         intra_order=order), 6, 3)
        phi_p, phi_n = v["pp"] / 2, v["nn"] / 2
        if phi_p + phi_n != v["pn"]:
            failures.append(f"{order}: additivity FAILS — "
                            f"{phi_p} + {phi_n} != {v['pn']}")
        a, b = 2 * phi_p, 2 * phi_n
        weights[order] = (a, b)
        print(f"  {order:10s} v(pp)={str(v['pp']):>6s} v(pn)={str(v['pn']):>6s} "
              f"v(nn)={str(v['nn']):>6s}  ->  (a, b) = ({a}, {b})   "
              f"additive: {phi_p + phi_n == v['pn']}")

    print("\nclosed form vs the six targets, per ordering:")
    for order in ("grouped", "borromean"):
        a, b = weights[order]
        ok = []
        for name, (Z, N) in CASES:
            got, want = closed_form(a, b, Z, N), TARGETS[order][name]
            ok.append(got == want)
            if got != want:
                failures.append(f"{order} {name}: closed form {got} != target {want}")
        print(f"  {order:10s} (a,b)=({a},{b})  "
              + "  ".join(f"{n}:{'ok' if k else 'FAIL'}"
                          for (n, _), k in zip(CASES, ok)))

    # ---- the 4He ratio is 24/7 for ANY (a, b) --------------------------------
    print("\n4He chain-over-atom ratio, at arbitrary (a, b):")
    ratios = []
    for a, b in ((F(21), F(16)), (F(3), F(-2)), (F(1), F(0)), (F(0), F(1)),
                 (F(5), F(-11)), (F(-7), F(13))):
        pairs = sum(closed_form(a, b, Z, N) for Z, N in ((2, 0), (1, 1), (0, 2)))
        atom = closed_form(a, b, 2, 2)
        if atom == 0:
            continue
        ratios.append((a, b, pairs / atom))
    for a, b, r in ratios:
        print(f"  (a,b)=({str(a):>3s},{str(b):>3s})   ratio = {r}")
    if any(r != F(24, 7) for _, _, r in ratios):
        failures.append("the 4He ratio is NOT 24/7 for every (a,b) — "
                        "the structural claim is wrong")

    # ---- and T / 3He are NOT invariant, which is what makes 4He notable ------
    tr = {}
    for order in ("grouped", "borromean"):
        a, b = weights[order]
        tr[order] = (
            (closed_form(a, b, 1, 1) + closed_form(a, b, 0, 2)) / closed_form(a, b, 1, 2),
            (closed_form(a, b, 2, 0) + closed_form(a, b, 1, 1)) / closed_form(a, b, 2, 1),
        )
    print(f"\nT ratio   grouped {tr['grouped'][0]}   borromean {tr['borromean'][0]}")
    print(f"3He ratio grouped {tr['grouped'][1]}   borromean {tr['borromean'][1]}")
    if tr["grouped"][0] == tr["borromean"][0] and tr["grouped"][1] == tr["borromean"][1]:
        failures.append("T and 3He ratios came out invariant too — then 4He's "
                        "invariance is not the notable fact this claims")

    print()
    if failures:
        for f in failures:
            print(f"FAIL  {f}")
        return 1
    print("PASS  c1_from_letters survives the ordering change; only (a,b) moves "
          "21,16 -> 3,-2, and the 4He 24/7 is structural (5/5 checks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
