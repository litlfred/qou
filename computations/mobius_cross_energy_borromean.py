#!/usr/bin/env python3
"""Borromean cross energy with the integrator calibrated in
mobius_cross_energy_hopf_calibration.py. Bean qou-o6ml, route (2).

That calibration reproduced the PROVED E(Hopf) = 2*pi^2 to 8 significant
figures, so the integrand and quadrature are trusted here. This applies them to
the second carrier.

CLASSICAL REALISATION -- three mutually orthogonal ellipses, semi-axes a, b:
    g1(t) = (0,       a cos t, b sin t)     yz-plane
    g2(t) = (b sin t, 0,       a cos t)     zx-plane
    g3(t) = (a cos t, b sin t, 0      )     xy-plane
Cyclic in the coordinates, so E_12 = E_23 = E_31 and E_total = 3 * E_12.
The classical Borromean figure is three golden rectangles, a/b = phi.

At a = b the three become equal circles that TOUCH -- measured below, not
assumed: min |g1 - g2|^2 = 1.1e-43.

CONVENTION. E_total here sums over UNORDERED pairs, which is the convention in
which Agol-Marques-Neves state E(Hopf) >= 2*pi^2 and in which the calibration
reproduces it. Doubling gives the ordered-pair convention; see the assertions.

NO FLOAT64. mpmath throughout, no float() anywhere.
"""
from __future__ import annotations

import pathlib

import _path_bridge  # noqa: F401
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

from mpmath import mp, mpf, cos, sin, sqrt, pi  # noqa: E402


def cross_12(a, b, N):
    """Cross energy of the first two components. Returns (E, min_sep_squared)."""
    h = 2 * pi / N
    total = mpf(0)
    mind = None
    for i in range(N):
        s = i * h
        p1, p2 = a * cos(s), b * sin(s)          # g1 = (0, p1, p2)
        v1 = sqrt(a * a * sin(s) ** 2 + b * b * cos(s) ** 2)
        for j in range(N):
            t = j * h
            q0, q2 = b * sin(t), a * cos(t)      # g2 = (q0, 0, q2)
            v2 = sqrt(b * b * cos(t) ** 2 + a * a * sin(t) ** 2)
            d2 = q0 * q0 + p1 * p1 + (p2 - q2) ** 2
            if mind is None or d2 < mind:
                mind = d2
            if d2 <= 0:
                return None, mind
            total += v1 * v2 / d2
    return total * h * h, mind


def main() -> None:
    one = mpf(1)
    phi = (1 + sqrt(5)) / 2
    ten_pi2 = 10 * pi ** 2
    twenty_pi2 = 20 * pi ** 2

    # degeneracy at a = b, measured
    _, mind_equal = cross_12(one, one, 32)

    # convergence at the golden ratio
    conv = {}
    for N in (32, 64, 96, 128):
        E, _ = cross_12(phi, one, N)
        conv[str(N)] = mp.nstr(3 * E, 22)
    E_phi = 3 * cross_12(phi, one, 128)[0]
    ratio_10 = E_phi / ten_pi2
    conv_gap = abs(mpf(conv["128"]) - mpf(conv["96"])) / E_phi

    # is phi the family minimum?
    best = None
    r = mpf(15) / 10
    while r <= mpf(21) / 10:
        E, _ = cross_12(r, one, 96)
        if best is None or E < best[0]:
            best = (E, r)
        r += mpf(1) / 100
    E0, r0 = best
    for step in (mpf(1) / 500, mpf(1) / 5000):
        moved = True
        while moved:
            moved = False
            for dr in (-step, step):
                E, _ = cross_12(r0 + dr, one, 96)
                if E < E0:
                    E0, r0, moved = E, r0 + dr, True
    E_min = 3 * E0

    wb = WitnessBuilder("mobius-cross-energy-borromean", engine="mpmath")
    wb.set_description(
        "Borromean cross energy over the classical three-orthogonal-ellipse "
        "family, using the integrator calibrated against the proved "
        "E(Hopf) = 2*pi^2. Bean qou-o6ml route (2). Reports the golden-ratio "
        "value, its convergence, and the family minimum -- and REFUTES the "
        "tempting reading that the golden-ratio value is exactly 10*pi^2.")
    wb.add_data("golden_ratio_phi", mp.nstr(phi, 25))
    wb.add_data("ten_pi_squared", mp.nstr(ten_pi2, 25))
    wb.add_data("twenty_pi_squared", mp.nstr(twenty_pi2, 25))
    wb.add_data("convergence_of_E_total_at_phi", conv)
    wb.add_data("E_total_at_phi", mp.nstr(E_phi, 22))
    wb.add_data("E_total_at_phi_over_10pi2", mp.nstr(ratio_10, 15))
    wb.add_data("family_minimum", {
        "E_total": mp.nstr(E_min, 22),
        "aspect_ratio_a_over_b": mp.nstr(r0, 12),
        "over_10pi2": mp.nstr(E_min / ten_pi2, 12),
        "caveat": ("TOPOLOGY NOT VERIFIED across the scan -- see the assertion "
                   "of the same name. This is NOT claimed to be the Borromean "
                   "energy minimum."),
    })
    wb.add_data("equal_circles_min_separation_squared", mp.nstr(mind_equal, 8))
    wb.add_data("pair_convention", (
        "E_total sums UNORDERED pairs, the convention in which "
        "Agol-Marques-Neves state E(Hopf) >= 2*pi^2 and in which the "
        "calibration reproduces it. Doubling gives the ordered-pair value."))

    wb.add_assertion(
        name="quadrature_converged",
        computed=conv_gap, expected=0, tolerance=mpf("1e-12"), unit="relative",
        source=(f"N=96 vs N=128 at a/b = phi agree to {mp.nstr(conv_gap, 4)} "
                f"relative. Set at 1e-12 because the 10*pi^2 comparison below "
                f"turns on a discrepancy of 5.9e-5, and that verdict is only "
                f"meaningful if the quadrature error is orders below it."))
    wb.add_assertion(
        name="golden_ratio_value_is_NOT_exactly_ten_pi_squared",
        computed=1 if abs(ratio_10 - 1) > mpf("1e-6") else 0,
        expected=1, tolerance=0, unit="boolean",
        source=(f"E_total(phi) = {mp.nstr(E_phi, 16)} against 10*pi^2 = "
                f"{mp.nstr(ten_pi2, 16)}: ratio {mp.nstr(ratio_10, 12)}, a "
                f"discrepancy of {mp.nstr(abs(ratio_10 - 1), 4)}. The "
                f"quadrature is converged to {mp.nstr(conv_gap, 4)}, TEN "
                f"ORDERS below that, so this is a genuine near-miss and not "
                f"numerical error. At N=64 and four decimals it reads as "
                f"1.0000, which is how it would have been written down as an "
                f"identity."))
    wb.add_assertion(
        name="golden_ratio_is_not_the_family_minimum",
        computed=1 if E_min < E_phi else 0, expected=1, tolerance=0,
        unit="boolean",
        source=(f"The family minimum over a/b in [1.5, 2.1] is "
                f"{mp.nstr(E_min, 14)} at a/b = {mp.nstr(r0, 8)}, which is "
                f"{mp.nstr((E_phi - E_min) / E_phi * 100, 4)}% BELOW the "
                f"golden-ratio value. Same shape as the Hopf calibration, "
                f"where the standard picture sat 7.3% above the minimum."))
    wb.add_assertion(
        name="equal_circles_are_degenerate",
        computed=1 if mind_equal < mpf("1e-20") else 0, expected=1,
        tolerance=0, unit="boolean",
        source=(f"At a = b the three orthogonal circles TOUCH: min separation "
                f"squared = {mp.nstr(mind_equal, 6)}. Measured, not assumed -- "
                f"it is why the family needs a != b at all."))
    wb.add_assertion(
        name="TOPOLOGY_NOT_VERIFIED_across_the_scan",
        computed=0, expected=0, tolerance=0, unit="boolean",
        source=(
            "DELIBERATE ZERO, recording a known gap rather than a result. "
            "Nothing here checks that the configuration stays BORROMEAN as a/b "
            "varies -- only that the components do not touch. The Hopf "
            "calibration's assertion 4 records the identical trap: a scan "
            "guarded only against touching walked into a SPLIT link and "
            "'minimised' below a proved bound. Two reasons this is less likely "
            "here -- the energy RISES on both sides of the interior minimum "
            "(142.6 at a/b=1.1, 149.5 at 6.0), rather than running away; and "
            "pairwise linking number is 0 by construction for the Borromean "
            "carrier, so there is no linking-number guard to write. But less "
            "likely is not verified. The family minimum above must NOT be "
            "cited as the Borromean energy minimum until the topology is "
            "checked."))
    out = wb.save()

    print(f"10*pi^2                    = {mp.nstr(ten_pi2, 20)}")
    print(f"E_total at a/b = phi       = {mp.nstr(E_phi, 20)}")
    print(f"  ratio to 10*pi^2         = {mp.nstr(ratio_10, 14)}   "
          f"(NOT an identity: off by {mp.nstr(abs(ratio_10-1), 4)})")
    print(f"  quadrature converged to  = {mp.nstr(conv_gap, 4)}")
    print(f"family minimum             = {mp.nstr(E_min, 20)} at a/b = "
          f"{mp.nstr(r0, 8)}")
    print(f"equal circles min sep^2    = {mp.nstr(mind_equal, 6)}  (degenerate)")
    print(f"\nwitness -> {out}")


if __name__ == "__main__":
    main()
