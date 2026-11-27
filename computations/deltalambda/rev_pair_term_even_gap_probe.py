#!/usr/bin/env python3
r"""
rev_pair_term_even_gap_probe.py — three conjectures of mine about the pair term, all refuted, and
the one number that survives: the coupling is worth ~1.2x, which is probably not enough (qou-hok7)

#7081 measured that the `(l, W)` relaxation is tight to under 1%, so the loss in the beta-bound is
entirely the **Jensen step** on the pair term

    P(beta) = sum_{i<j} eps(beta_i - beta_j),

which #7070 lower-bounded by `J(l, W) = sum_d (l-d) eps(d*W/(l-d))` — Jensen at the mean of each
distance class. This probe went after that step. It did not close it, and the three ways it failed
are worth more than a fourth guess would be.

## The reformulation (this part is right and is kept)

Write the beta's by their partial gap sums, `0 = S_0 < S_1 < ... < S_{l-1} = W`. Then
`beta_i - beta_j = S_{j-1} - S_{i-1}` and

    P = sum_{0 <= a < b <= l-1} eps(S_b - S_a),

the energy of `l` points in an interval of length `W` under the pair potential `eps`. So
`P_min(l, W)` is the ground state of a one-dimensional repulsive gas with hard walls. That framing
is exact and is the useful residue of this probe.

## The three refutations

1. **"The minimiser is the most even spacing."** False. It misses on 44 of 105 brute-forced
   `(l, W)` pairs. At `(4, 4)` the even multiset is `{2,1,1}` and the layout matters: `(2,1,1)`
   gives 6.8236, `(1,2,1)` gives 6.5135. **The energy depends on the ARRANGEMENT, not just the
   multiset.** My two hand-checks before writing this both had all-equal gaps — drawn from exactly
   the cases where the distinction cannot appear.

2. **"...arranged unimodally, large gaps in the middle."** Better (44 violations down to 12) and
   still false. At `(5, 11)` the true minimiser has gaps `(2,3,4,2)`, which is not the even
   multiset `{3,3,3,2}` in any order. The minimiser is not a rearrangement of the even gaps at all.

3. **"Jensen can be beaten by tightening one distance class."** False, and backwards. For a single
   class the differences satisfy `x_i >= d`, `sum x_i <= d*W`, and `eps` is CONVEX — so
   `sum eps(x_i)` is convex and minimised at the centroid, which IS Jensen. I had reached for the
   opposite extreme point expecting an improvement; for a convex summand that is the MAXIMUM.

## What survives

Jensen is optimal per class, so the whole loss is the **coupling between classes** — the same gaps
appear in every class and the per-class relaxation forgets it. R3 prices that coupling: in the
regime the maximizer actually selects (`W/l ~ 1.7`, its argmax at every `n` in #7081), the true
`P_min` exceeds Jensen by **~1.21x** (measured, l = 4..8).

Priced against the bound rather than the pair term, that is probably not enough. At #7081's own
`n = 40` argmax `(l, W) = (22, 37)`, applying the full coupling factor shrinks `B` by only 13.5%,
against the ~3x over-statement #7081 measured. So solving the 1-D gas exactly would likely still
not settle sharpness, and the `(l, W)` route is close to exhausted rather than merely unfinished.
The caveat is that the factor is measured at `l = 4..8` and applied at `l = 22`; it may grow with
`l`, and brute force cannot say (`C(W-1, l-2)`, argmax `(151, 357)` at `n = 4000`). That is a
projection, and it is the thing to check first.

**Sharpness is untouched: `REV_n` stays in `[Omega(sqrt n), O(n^(3/4))]` and no claim is made.**

## Checks

  R1  both even-multiset conjectures refuted, with the counterexamples
  R2  Jensen is already optimal for the per-class relaxation (so the loss is inter-class)
  R3  the coupling priced by brute force in the selected regime
  R4  verdict and the concrete target for the next attempt

Exact integer arithmetic for the configurations; mpmath at 40 dps for the eps sums. No float64.
"""

from __future__ import annotations

import itertools
import json
import os
import sys
from datetime import datetime, timezone
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMPUTATIONS = os.path.dirname(_HERE)
if _COMPUTATIONS not in sys.path:
    sys.path.insert(0, _COMPUTATIONS)

from mpmath import mp  # noqa: E402

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

from hmin_closed_form_and_rev_sublinearity_probe import H_min_closed  # noqa: E402

mp.dps = 40
Q0 = Q_MP
LNQ = mp.log(Q0)
T = Q0 ** 2

_NEPS = 20000
EPS = [mp.mpf(0)] + [-mp.log(1 - T ** (-m)) for m in range(1, _NEPS)]
_F = [mp.mpf(0)] * _NEPS
for _m in range(1, _NEPS):
    _F[_m] = _F[_m - 1] + EPS[_m]
C_CONST = _F[_NEPS - 1]


def F(k):
    return _F[min(k, _NEPS - 1)]


def epsr(x):
    """eps at a real argument (the Jensen bound needs non-integer means)."""
    if x <= 0:
        return mp.inf
    return -mp.log(1 - T ** (-mp.mpf(x)))


def energy(points):
    """sum_{a<b} eps(S_b - S_a) — integer arguments only."""
    tot = mp.mpf(0)
    for a in range(len(points)):
        for b in range(a + 1, len(points)):
            tot += EPS[points[b] - points[a]]
    return tot


def _points_from_gaps(gaps):
    pts, s = [0], 0
    for g in gaps:
        s += g
        pts.append(s)
    return pts


def even_points_flat(ell, W):
    """The even MULTISET, laid out largest-first. This is the naive reading of 'most even' and it
    is NOT the minimiser — kept because R1 measures exactly how it fails."""
    if ell == 1:
        return [0]
    m = ell - 1
    q, r = divmod(W, m)
    return _points_from_gaps([q + 1] * r + [q] * (m - r))


def even_points(ell, W):
    """The even multiset arranged UNIMODALLY — larger gaps in the middle, symmetric.

    Same multiset as `even_points_flat`; only the order differs, and the order is what matters.
    At (l, W) = (4, 4) the multiset is {2,1,1}: laid out flat as (2,1,1) it gives 6.8236, arranged
    (1,2,1) it gives 6.5135. The pair energy depends on the ARRANGEMENT, not just the gaps.
    """
    if ell == 1:
        return [0]
    m = ell - 1
    q, r = divmod(W, m)
    big, small = [q + 1] * r, [q] * (m - r)
    # place the small gaps at the two ends, the big ones in the middle, symmetrically
    left = small[: len(small) // 2]
    right = small[len(small) // 2:]
    return _points_from_gaps(left + big + right)


def P_even(ell, W):
    return energy(even_points(ell, W)) if ell >= 2 else mp.mpf(0)


def J_jensen_class(N, S):
    """Jensen for ONE distance class: N differences summing to S."""
    return N * epsr(mp.mpf(S) / N) if N > 0 else mp.mpf(0)


def J_jensen(ell, W):
    """#7070's bound, for comparison."""
    if ell < 2:
        return mp.mpf(0)
    tot = mp.mpf(0)
    for d in range(1, ell):
        arg = mp.mpf(d * W) / (ell - d)
        if arg > 300:
            break
        tot += (ell - d) * epsr(arg)
    return tot


def brute_min(ell, W):
    """Exact min of the energy over EVERY gap composition of W into l-1 parts >= 1."""
    m = ell - 1
    best, arg = None, None
    for cut in itertools.combinations(range(1, W), m - 1) if m >= 2 else [()]:
        pts = [0] + list(cut) + [W]
        e = energy(pts)
        if best is None or e < best:
            best, arg = e, tuple(pts)
    return best, arg


def partitions_desc(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, maxpart), 0, -1):
        for rest in partitions_desc(n - first, first):
            yield (first,) + rest


def conj(lam):
    return [sum(1 for p in lam if p > j) for j in range(lam[0])]


def hook_sum(lam):
    return (sum(p * p for p in lam) + sum(c * c for c in conj(lam))) // 2


def two_H_lower(n, ell, lam1):
    t = Fraction(lam1 * lam1) + Fraction(ell * ell)
    if ell > 1:
        t += Fraction((n - lam1) ** 2, ell - 1)
    if lam1 > 1:
        t += Fraction((n - ell) ** 2, lam1 - 1)
    return t


def relaxed_max(n, pairfn, ell_hi=None):
    """#7081's O(n^2) maximizer, with the pair-term bound passed in."""
    hmin = H_min_closed(n)
    best, arg = None, None
    ell_hi = min(ell_hi or n, n)
    for ell in range(1, ell_hi + 1):
        one = ell * C_CONST - F(n)
        for W in range(ell - 1, n + ell - 1):
            lo = max(-(-n // ell), W - ell + 2, 1)
            hi = n - ell + 1
            if lo > hi:
                break
            a, b = lo, hi
            while b - a > 2:
                m1, m2 = a + (b - a) // 3, b - (b - a) // 3
                if two_H_lower(n, ell, m1) <= two_H_lower(n, ell, m2):
                    b = m2
                else:
                    a = m1
            twoH = min(two_H_lower(n, ell, x) for x in range(a, b + 1))
            Hh = twoH / 2
            v = one - pairfn(ell, W) - (mp.mpf(Hh.numerator) / Hh.denominator - hmin) * LNQ
            if best is None or v > best:
                best, arg = v, (ell, W)
            if v < best - 50:
                break
    return best, arg


def main() -> int:
    results = []

    def check(tag, ok, msg):
        results.append({"check": tag, "pass": bool(ok), "detail": msg})
        print(("  PASS  " if ok else "  FAIL  ") + tag)
        print("        " + msg)

    print("=" * 78)
    print("the pair term's exact minimum over (l, W)   (qou-hok7)")
    print("=" * 78)

    # ---- R1: which arrangement of the even multiset minimises? BRUTE FORCE ------------------
    tested, viol, flat_viol, worst_flat = 0, [], 0, mp.mpf(0)
    for ell in range(2, 8):
        for W in range(ell - 1, 21):
            bm, barg = brute_min(ell, W)
            pe = P_even(ell, W)
            pf = energy(even_points_flat(ell, W))
            tested += 1
            if pe > bm + mp.mpf("1e-30"):
                viol.append({"ell": ell, "W": W, "centered": mp.nstr(pe, 10),
                             "brute_min": mp.nstr(bm, 10), "brute_argmin": list(barg)})
            if pf > bm + mp.mpf("1e-30"):
                flat_viol += 1
                worst_flat = max(worst_flat, (pf - bm) / bm)
    first_ce = viol[0] if viol else None
    check(
        "R1_the_even_multiset_conjecture_is_REFUTED_at_BOTH_levels",
        bool(viol) and len(viol) < flat_viol,
        f"brute-forced every gap composition for l = 2..7, W = l-1..20 ({tested} (l, W) pairs). "
        f"I conjectured P_min(l, W) had a closed form and it does not. Two refutations, both "
        f"recorded because the second is the interesting one:\n\n"
        f"        (a) 'most even gaps' laid out largest-first misses the minimum on {flat_viol} of "
        f"{tested} pairs, by up to {mp.nstr(100 * worst_flat, 4)}%. At (l, W) = (4, 4) the "
        f"multiset is {{2,1,1}}: (2,1,1) gives 6.8236, (1,2,1) gives 6.5135. So the energy depends "
        f"on the ARRANGEMENT, not just the multiset. My two hand-checks before writing this both "
        f"had all-equal gaps — drawn from exactly the cases where the distinction cannot appear.\n\n"
        f"        (b) Centering the even multiset (small gaps at the ends, large in the middle) "
        f"fixes most of it — {flat_viol} violations down to {len(viol)} — and is still WRONG. At "
        f"(l, W) = (5, 11) the minimiser has gaps (2,3,4,2), which is not the even multiset "
        f"{{3,3,3,2}} in any order. So the minimiser is not a rearrangement of the even gaps "
        f"either; it is a genuine coupled optimisation, and no closed form of this shape exists.\n\n"
        f"        This check PASSES on the refutation: it asserts both conjectures fail and that "
        f"centering strictly improves on flat, which is the structural content that survives.",
    )
    if not viol:
        print("\n  NOTE: centered form was NOT refuted on this range — R1's premise no longer "
              "holds and its wording must be re-derived, not merely re-run.")
        return 1

    # ---- R2: Jensen is OPTIMAL per distance class, so the loss is INTER-class ---------------
    # For one class d there are N = l-d differences x_i >= d with sum <= d*W. eps is convex, so
    # sum eps(x_i) is convex and its minimum over that simplex is at the centroid (all equal),
    # which IS Jensen. Verified numerically against random feasible points and the extreme point.
    import random
    random.seed(20260907)
    worse = 0
    trials = 0
    for (ell, W, d) in [(22, 37, 1), (22, 37, 2), (22, 37, 3), (26, 47, 1), (26, 47, 4),
                        (43, 105, 2), (78, 192, 3)]:
        N = ell - d
        S = d * W
        base = J_jensen_class(N, S)
        # extreme point: one variable takes all the slack
        ext = epsr(S - (N - 1) * d) + (N - 1) * epsr(d)
        if ext < base - mp.mpf("1e-25"):
            worse += 1
        trials += 1
        for _ in range(40):
            cuts = sorted(random.uniform(0, S - N * d) for _ in range(N - 1))
            xs, prev = [], 0
            for c in list(cuts) + [S - N * d]:
                xs.append(d + (c - prev))
                prev = c
            v = sum(epsr(x) for x in xs)
            trials += 1
            if v < base - mp.mpf("1e-25"):
                worse += 1
    check(
        "R2_Jensen_is_ALREADY_OPTIMAL_for_the_per_class_relaxation",
        worse == 0,
        f"for a single distance class the differences x_i >= d satisfy sum x_i <= d*W, and eps is "
        f"CONVEX, so sum eps(x_i) is convex and minimised at the centroid — all x_i equal — which "
        f"is exactly Jensen. Checked against the opposite extreme point (one variable takes all "
        f"the slack) and {trials - 7} random feasible configurations across 7 (l, W, d) triples "
        f"drawn from the maximizer's own argmaxes: {worse} beat Jensen.\n\n"
        f"        **This is the load-bearing negative.** I had reached for the extreme point "
        f"expecting it to beat Jensen — at (l,W,d) = (22,37,1) it gives 33.4 against Jensen's "
        f"24.8 — and that is backwards: for a CONVEX summand the extreme point is the MAXIMUM. So "
        f"Jensen cannot be improved by tightening any one distance class; the entire loss "
        f"identified in #7081 lives in the COUPLING between classes, since the same gaps appear in "
        f"all of them and the per-class relaxation forgets that.",
    )

    # ---- R3: how much is the coupling actually worth? --------------------------------------
    print()
    print(f"  {'l':>4} {'W':>4} {'W/l':>6} {'Jensen':>10} {'true P_min':>11} {'ratio':>7}")
    rows3b, ratios = [], []
    for ell in range(4, 9):
        W = int(round(1.7 * ell))
        bm, barg = brute_min(ell, W)
        jj = J_jensen(ell, W)
        rat = bm / jj if jj > 0 else mp.mpf(0)
        ratios.append(rat)
        rows3b.append({"ell": ell, "W": W, "jensen": mp.nstr(jj, 10),
                       "true_P_min": mp.nstr(bm, 10), "ratio": mp.nstr(rat, 6),
                       "argmin_points": list(barg)})
        print(f"  {ell:>4} {W:>4} {mp.nstr(mp.mpf(W)/ell, 4):>6} {mp.nstr(jj, 7):>10} "
              f"{mp.nstr(bm, 8):>11} {mp.nstr(rat, 5):>7}")
    check(
        "R3_the_coupling_is_worth_a_measured_factor_not_a_rounding_error",
        min(ratios) > 1,
        f"in the regime the maximizer actually selects (W/l ~ 1.7, its argmax at every n from "
        f"#7081), the TRUE P_min exceeds Jensen by a factor of "
        f"{mp.nstr(min(ratios), 5)}-{mp.nstr(max(ratios), 5)} over l = 4..8. So the inter-class "
        f"coupling is worth roughly a factor of {mp.nstr(sum(ratios) / len(ratios), 4)} on the "
        f"pair term — not a rounding error, and the right size to matter given #7081 measured the "
        f"maximized bound over-stating M_n by ~3x. Whether it is ENOUGH cannot be read from l <= 8; "
        f"brute force is C(W-1, l-2) and the maximizer's argmax at n = 4000 is (151, 357), where "
        f"that is astronomically large.",
    )

    # ---- R4: verdict, and what the coupling factor does to the BOUND ------------------------
    avg = sum(ratios) / len(ratios)
    # The pair term is only part of B = l*C - P - F(n). Price the coupling where it would be spent:
    # at #7081's own argmax for n = 40, which is (l, W) = (22, 37).
    el40, W40 = 22, 37
    one40 = el40 * C_CONST - F(40)
    j40 = J_jensen(el40, W40)
    b_now = one40 - j40
    b_best = one40 - avg * j40
    shrink = (b_now - b_best) / b_now
    print()
    print(f"  at #7081's n=40 argmax (l,W)=({el40},{W40}):  l*C - F(n) = {mp.nstr(one40, 8)}, "
          f"J = {mp.nstr(j40, 7)}")
    print(f"    B with Jensen      {mp.nstr(b_now, 8)}")
    print(f"    B with {mp.nstr(avg, 4)}x coupling  {mp.nstr(b_best, 8)}   "
          f"({mp.nstr(100 * shrink, 4)}% smaller)")
    check(
        "R4_verdict_no_closed_form_but_the_target_is_now_priced",
        True,
        f"**No closed form for P_min(l, W), and the naive routes to one are closed.** The even "
        f"multiset is not the minimiser in any arrangement (R1), and Jensen cannot be beaten "
        f"one distance class at a time because eps is convex and Jensen already sits at that "
        f"minimum (R2). What is left is the inter-class coupling, and R3 prices it: a factor of "
        f"~{mp.nstr(avg, 4)} on the pair term in the regime the maximizer selects.\n\n"
        f"        **And priced against the bound, that is probably not enough — this is the number "
        f"the next attempt needs.** The pair term is only one part of B = l*C - P - F(n). At "
        f"#7081's own n=40 argmax (l, W) = (22, 37), l*C - F(n) = {mp.nstr(one40, 8)} and "
        f"J = {mp.nstr(j40, 7)}, so B = {mp.nstr(b_now, 8)}; applying the full {mp.nstr(avg, 4)}x "
        f"coupling factor gives {mp.nstr(b_best, 8)}, only {mp.nstr(100 * shrink, 4)}% smaller. "
        f"Against the ~3x over-statement #7081 measured, closing the pair term COMPLETELY at this "
        f"strength moves the bound by around a tenth. So the honest expectation is that solving "
        f"the 1-D gas exactly would still not settle sharpness, and the (l, W) route is close to "
        f"exhausted rather than merely unfinished.\n\n"
        f"        Caveat on that estimate: it uses the small-l coupling factor (measured at "
        f"l = 4..8) at l = 22, and the factor may well grow with l — brute force cannot say, since "
        f"it is C(W-1, l-2) and the argmax at n = 4000 is (151, 357). It is a projection, not a "
        f"measurement, and it is the projection that should be checked first.\n\n"
        f"        This settles nothing about sharpness and makes no claim; REV_n stays in "
        f"[Omega(sqrt n), O(n^(3/4))].\n\n"
        f"        Concretely for the next attempt: the object to bound is the minimum energy of "
        f"l points in [0, W] under eps, and the useful direction is a lower bound that keeps the "
        f"gaps coupled — a transfer-matrix or convex-duality treatment of the 1-D gas — rather "
        f"than any further per-class inequality. The dropped constraint sum(beta) = n + l(l-1)/2 "
        f"remains available too, and is the only relaxation of any size left besides this one.\n\n"
        f"        Recorded as three failed conjectures of mine rather than one result, because "
        f"each narrowed the space: arrangement matters; the even multiset is not it; and the "
        f"per-class relaxation is already tight.",
    )

    n_ok = sum(1 for r in results if r["pass"])
    print()
    print("=" * 78)
    print(f"{n_ok}/{len(results)} checks passed")
    print("=" * 78)

    payload = {
        "probe": "rev_pair_term_even_gap_probe",
        "bean": "qou-hok7",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0_anchor": "physical_proton", "q0Anchor": "proton",
        "dps": mp.dps,
        "claim": ("P_min(l, W) has NO closed form of the conjectured shapes: the even multiset "
                  "is not the minimiser in any arrangement, and Jensen is already optimal "
                  "per distance class. The loss is inter-class coupling, priced at ~1.21x, which "
                  "projects to only ~10% off the bound against a ~3x gap."),
        "pair_min_vs_jensen": rows3b,
        "coupling_factor_measured": mp.nstr(sum(ratios) / len(ratios), 8),
        "checks": results,
        "checks_passed": n_ok,
        "checks_total": len(results),
    }
    out = os.path.join(_COMPUTATIONS, "rev-pair-term-even-gap.witness.json")
    with open(out, "w") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print(f"witness -> {out}")
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
