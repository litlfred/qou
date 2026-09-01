#!/usr/bin/env python3
"""Close the TOPOLOGY_NOT_VERIFIED gap left by mobius_cross_energy_borromean.py.

Bean qou-o6ml, route (2). That probe recorded a deliberate zero-valued assertion
saying nothing checked the three-ellipse configuration stays BORROMEAN as the
aspect ratio a/b varies -- only that the components do not touch. Without that,
its family minimum could not be cited, because the identical trap in the Hopf
calibration (assertion 4 there) shows a scan guarded only against touching can
walk out of the link type and "minimise" below a proved bound.

THE ARGUMENT, which is cheaper than computing mu-bar_123 geometrically
=====================================================================
Link type is an isotopy invariant. The three-ellipse family

    g1(t) = (0,       a cos t, b sin t)
    g2(t) = (b sin t, 0,       a cos t)
    g3(t) = (a cos t, b sin t, 0      )

is continuous in a/b, and each component is an ellipse, hence embedded for any
a, b > 0 -- no self-intersection to check. So IF no two components meet anywhere
along the path, the deformation is an ambient isotopy and the link type is
CONSTANT across the whole range. It then equals its value at any one point.

So the guard is: bound the pairwise separation away from zero across the range.
That is a positive statement about the whole family, not a spot check.

WHAT IS AND IS NOT ESTABLISHED HERE
===================================
ESTABLISHED: (i) the link type does not change across the scanned range, so the
family minimum and the golden-ratio point are the SAME link; (ii) all three
pairwise Gauss linking numbers are 0 throughout, which is necessary for Brunnian
and rules out the pair-linked alternatives.

NOT ESTABLISHED HERE: that the type IS the Borromean rings. That rests on the
classical three-mutually-orthogonal-golden-rectangles construction, which this
probe takes as the definition of its a/b = phi point rather than deriving. What
the probe adds is that the rest of the family inherits it.

RESIDUAL: a/b is sampled on a grid, so in principle the separation could dip
between samples. The separation is smooth in a/b and the measured margin is
reported, so the claim is "no dip at the sampled resolution with margin X", not
a proof over the continuum.

NO FLOAT64. mpmath throughout, no float() anywhere.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

from mpmath import mp, mpf, cos, sin, sqrt, pi  # noqa: E402


def comp(k, t, a, b):
    """Component k in {0,1,2} at parameter t: cyclic in the coordinates."""
    if k == 0:
        return (mpf(0), a * cos(t), b * sin(t))
    if k == 1:
        return (b * sin(t), mpf(0), a * cos(t))
    return (a * cos(t), b * sin(t), mpf(0))


def dcomp(k, t, a, b):
    if k == 0:
        return (mpf(0), -a * sin(t), b * cos(t))
    if k == 1:
        return (b * cos(t), mpf(0), -a * sin(t))
    return (-a * sin(t), b * cos(t), mpf(0))


def min_sep_sq(k, l, a, b, N):
    h = 2 * pi / N
    m = None
    for i in range(N):
        p = comp(k, i * h, a, b)
        for j in range(N):
            q = comp(l, j * h, a, b)
            d2 = sum((p[c] - q[c]) ** 2 for c in range(3))
            if m is None or d2 < m:
                m = d2
    return m


def gauss_linking(k, l, a, b, N):
    """lk = (1/4pi) int int (g_k - g_l) . (g_k' x g_l') / |g_k - g_l|^3."""
    h = 2 * pi / N
    tot = mpf(0)
    for i in range(N):
        s = i * h
        p, dp = comp(k, s, a, b), dcomp(k, s, a, b)
        for j in range(N):
            t = j * h
            q, dq = comp(l, t, a, b), dcomp(l, t, a, b)
            r = (p[0] - q[0], p[1] - q[1], p[2] - q[2])
            cr = (dp[1] * dq[2] - dp[2] * dq[1],
                  dp[2] * dq[0] - dp[0] * dq[2],
                  dp[0] * dq[1] - dp[1] * dq[0])
            n = sqrt(r[0] ** 2 + r[1] ** 2 + r[2] ** 2)
            tot += (r[0] * cr[0] + r[1] * cr[1] + r[2] * cr[2]) / n ** 3
    return tot * h * h / (4 * pi)


def main() -> None:
    one = mpf(1)
    phi = (1 + sqrt(5)) / 2
    pairs = ((0, 1), (1, 2), (0, 2))

    # --- 1. separation bounded away from zero across the scanned range
    lo, hi, step = mpf(15) / 10, mpf(21) / 10, mpf(1) / 100
    worst = None
    r = lo
    while r <= hi:
        for (k, l) in pairs:
            d2 = min_sep_sq(k, l, r, one, 48)
            if worst is None or d2 < worst[0]:
                worst = (d2, r, (k, l))
        r += step
    worst_d2, worst_r, worst_pair = worst
    worst_d = sqrt(worst_d2)

    # --- 2. pairwise Gauss linking numbers, at three points across the range
    lks = {}
    for label, rr in (("1.5", lo), ("phi", phi), ("1.817", mpf(1817) / 1000),
                      ("2.1", hi)):
        lks[label] = {f"{k}{l}": mp.nstr(gauss_linking(k, l, rr, one, 64), 10)
                      for (k, l) in pairs}
    max_abs_lk = max(abs(mpf(v)) for d in lks.values() for v in d.values())

    # --- 3. the a=b degeneracy, for contrast
    d2_equal = min_sep_sq(0, 1, one, one, 48)

    wb = WitnessBuilder("mobius-borromean-topology-guard", engine="mpmath")
    wb.set_description(
        "Closes the TOPOLOGY_NOT_VERIFIED gap in "
        "mobius-cross-energy-borromean.witness.json. Link type is an isotopy "
        "invariant and each component is an embedded ellipse, so bounding the "
        "pairwise separation away from zero across the a/b range proves the "
        "link type is CONSTANT there -- the family minimum and the "
        "golden-ratio point are the same link. Also computes all three "
        "pairwise Gauss linking numbers, which are 0 throughout as Brunnian "
        "requires.")
    wb.add_data("scanned_range", {"a_over_b_min": mp.nstr(lo, 6),
                                  "a_over_b_max": mp.nstr(hi, 6),
                                  "step": mp.nstr(step, 6)})
    wb.add_data("worst_case_separation", {
        "min_distance": mp.nstr(worst_d, 12),
        "min_distance_squared": mp.nstr(worst_d2, 12),
        "at_a_over_b": mp.nstr(worst_r, 8),
        "pair": f"{worst_pair[0]}{worst_pair[1]}",
    })
    wb.add_data("pairwise_gauss_linking_numbers", lks)
    wb.add_data("equal_circles_min_sep_squared", mp.nstr(d2_equal, 8))
    wb.add_data("what_is_not_established", (
        "That the type IS the Borromean rings. That rests on the classical "
        "three-mutually-orthogonal-golden-rectangles construction, taken here "
        "as the definition of the a/b = phi point. What this probe adds is "
        "that the REST of the family inherits it."))
    # --- 4. how the separation behaves across a wider range, which is what
    #        actually disposes of the grid-sampling worry
    profile = {}
    for r10 in (110, 150, 180, 200, 250, 300, 400):
        rr = mpf(r10) / 100
        profile[mp.nstr(rr, 4)] = mp.nstr(sqrt(min_sep_sq(0, 1, rr, one, 96)), 14)
    vals = [mpf(v) for v in profile.values()]
    monotone = all(vals[i] < vals[i + 1] for i in range(len(vals) - 1))

    wb.add_data("separation_profile_over_a_wider_range", profile)
    wb.add_data("separation_is_monotone_increasing", bool(monotone))
    wb.add_data("closed_form_check", (
        "The worst case sits at a/b = 1.5 with separation exactly 0.5 = a - b, "
        "and a - b also matches exactly at a/b = 1.1 (0.1). It does NOT hold "
        "generally: at a/b = 1.8 the separation is 0.74415 against a - b = 0.8, "
        "and by a/b = 4 it is 0.96657 against 3. So `min sep = a - b` is a "
        "low-end coincidence -- the minimising pair of points on the two "
        "ellipses changes -- and is recorded here because it is the obvious "
        "wrong generalisation to draw from the worst-case row."))
    wb.add_data("residual_limitation", (
        "a/b is sampled on a grid of step 0.01, so the separation could in "
        "principle dip between samples. What actually disposes of this is that "
        "the separation is monotone increasing across the sampled profile, so "
        "the minimum over any interval sits at its LEFT endpoint -- and the "
        "grid scan independently found exactly that. Monotonicity is itself "
        "read off seven sample points, not proved, so the honest claim is a "
        "strong one about the sampled profile rather than a theorem."))

    wb.add_assertion(
        name="separation_bounded_away_from_zero_across_the_range",
        computed=1 if worst_d > mpf("0.1") else 0, expected=1, tolerance=0,
        unit="boolean",
        source=(f"Worst pairwise separation over a/b in "
                f"[{mp.nstr(lo,4)}, {mp.nstr(hi,4)}] is "
                f"{mp.nstr(worst_d, 10)} (at a/b = {mp.nstr(worst_r, 6)}, pair "
                f"{worst_pair[0]}{worst_pair[1]}) -- not a near miss. Since "
                f"link type is an isotopy invariant and each component is an "
                f"embedded ellipse, the type is CONSTANT across the range."))
    wb.add_assertion(
        name="all_pairwise_linking_numbers_vanish",
        computed=max_abs_lk, expected=0, tolerance=mpf("1e-6"), unit="integer",
        source=(f"All three Gauss linking integrals evaluate to 0 at every "
                f"sampled a/b (largest |lk| = {mp.nstr(max_abs_lk, 6)}). "
                f"Necessary for Brunnian, and it rules out the pair-linked "
                f"alternatives the isotopy argument alone would permit."))
    wb.add_assertion(
        name="family_minimum_is_the_same_link_as_the_golden_ratio_point",
        computed=1 if worst_d > mpf("0.1") else 0, expected=1, tolerance=0,
        unit="boolean",
        source=(f"a/b = 1.817 (the family minimum of "
                f"mobius-cross-energy-borromean) and a/b = phi = "
                f"{mp.nstr(phi, 8)} are joined by a path inside the scanned "
                f"range along which no two components meet. This is what the "
                f"earlier probe could not assert, and it is the reason its "
                f"family minimum may now be cited."))
    wb.add_assertion(
        name="equal_circles_remain_the_degenerate_boundary",
        computed=1 if d2_equal < mpf("1e-20") else 0, expected=1, tolerance=0,
        unit="boolean",
        source=(f"At a = b the components touch (min separation squared = "
                f"{mp.nstr(d2_equal, 6)}), which is why the scanned range "
                f"starts at 1.5 and the argument above does not extend to "
                f"a/b = 1."))
    wb.add_assertion(
        name="separation_minimum_sits_at_the_left_endpoint",
        computed=1 if monotone else 0, expected=1, tolerance=0, unit="boolean",
        source=(f"Separation over a/b in [1.1, 4.0] is monotone increasing: "
                f"{', '.join(f'{k}->{v[:7]}' for k, v in profile.items())}. So "
                f"the minimum over any sub-interval is at its left endpoint, "
                f"which is where the grid scan independently found it. This is "
                f"what weakens the grid-sampling caveat, NOT the closed form "
                f"`a - b`, which holds only at the low end (see "
                f"closed_form_check)."))
    out = wb.save()

    print(f"scanned a/b in [{mp.nstr(lo,4)}, {mp.nstr(hi,4)}] step {mp.nstr(step,4)}")
    print(f"worst pairwise separation = {mp.nstr(worst_d, 12)}  at a/b = "
          f"{mp.nstr(worst_r, 6)}  pair {worst_pair[0]}{worst_pair[1]}")
    print(f"max |Gauss lk| over samples = {mp.nstr(max_abs_lk, 8)}")
    print(f"a=b min sep^2 = {mp.nstr(d2_equal, 6)}  (degenerate boundary)")
    print(f"\nwitness -> {out}")


if __name__ == "__main__":
    main()
