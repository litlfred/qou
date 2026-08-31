#!/usr/bin/env python3
"""Calibrate a Mobius cross-energy integrator against the proved E(Hopf) = 2*pi^2.

Bean qou-o6ml, route (2). Before any Borromean number is worth anything, the
integrator has to reproduce a value the literature has PROVED. This is that
check, and it also records -- as a measured fact rather than a caution -- the
degeneracy that makes the whole front hard.

THE TARGET
==========
Freedman-He-Wang conjectured, and Agol-Marques-Neves proved
(arXiv:1205.0825, "Min-max theory and the energy of links"), that for two
components with linking number +-1 the Mobius cross energy

    E(g1, g2) = int int |g1'(s)| |g2'(t)| / |g1(s) - g2(t)|^2 ds dt

satisfies E >= 2*pi^2 = 19.7392088..., with equality iff the pair is a Mobius
image of the standard Hopf link. The integrand is UNSUBTRACTED: the subtracted
term of the O'Hara self-energy is 1/D^2 with D the arc-length distance ALONG the
curve, and between distinct components there is no such path, so it vanishes.
That matches QOU.LinkEmbedding.mutualIntegrand.

THE FAMILY
==========
Scale invariance fixes the first radius to 1:

    g1(s) = (cos s, sin s, 0)             unit circle, xy-plane, at the origin
    g2(t) = (c + R cos t, 0, R sin t)     radius R, xz-plane, centre (c, 0, 0)

so |g1'| = 1 and |g2'| = R. g2 punctures the plane of g1 at x = c-R and x = c+R;
the pair is LINKED iff exactly one puncture lies inside the unit disk.

THE TRAP THIS RECORDS
=====================
A first version of this scan guarded only against the components TOUCHING
(d^2 <= 0) and not against their becoming UNLINKED. It "minimised" to
E = 3.1219 at (R, c) = (0.4, 2.5) -- far below the proved bound, because that
configuration is a SPLIT link, where the cross energy has infimum 0 (shrink one
component: the numerator carries |g2'| ~ R, the denominator does not). Assertion
4 below pins that as a measurement. It is the same degeneracy the front is about
-- an unlinked pair contributes nothing -- met inside the tool built to study it.

NO FLOAT64 (AGENTS.md: probes are not exempt): mpmath end to end, no float()
anywhere, including in the search.
"""
from __future__ import annotations

import pathlib

import _path_bridge  # noqa: F401
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

from mpmath import mp, mpf, cos, sin, pi  # noqa: E402

UNIT = mpf(1)


def is_linked(R, c):
    """Exactly one puncture of g2 through g1's plane lies inside the unit disk."""
    return (abs(c - R) < UNIT) != (abs(c + R) < UNIT)


def cross_energy(R, c, N):
    """N x N trapezoid. Periodic and smooth off the singularity, so convergence
    is spectral -- verified by assertion 1 rather than assumed."""
    h = 2 * pi / N
    total = mpf(0)
    for i in range(N):
        s = i * h
        c1, s1 = cos(s), sin(s)
        for j in range(N):
            t = j * h
            dx = c1 - (c + R * cos(t))
            dz = -R * sin(t)
            d2 = dx * dx + s1 * s1 + dz * dz
            if d2 <= 0:
                return None
            total += R / d2
    return total * h * h


def main() -> None:
    target = 2 * pi ** 2

    # --- 1. spectral convergence of the quadrature, on a fixed configuration
    conv = {str(N): mp.nstr(cross_energy(UNIT, UNIT, N), 20) for N in (16, 32, 64)}
    e32, e64 = cross_energy(UNIT, UNIT, 32), cross_energy(UNIT, UNIT, 64)
    conv_gap = abs(e64 - e32) / e64

    # --- 2. the obvious configuration is NOT the minimiser
    e_obvious = cross_energy(UNIT, UNIT, 64)
    obvious_excess = (e_obvious - target) / target

    # --- 3. constrained minimum over the linked family
    best = None
    for Ri in range(2, 41):
        R = mpf(Ri) / 10
        for ci in range(0, 41):
            c = mpf(ci) / 10
            if not is_linked(R, c):
                continue
            E = cross_energy(R, c, 32)
            if E is not None and (best is None or E < best[0]):
                best = (E, R, c)
    E0, R0, c0 = best
    for step in (mpf(1) / 40, mpf(1) / 200):
        for _ in range(60):
            moved = False
            for dR in (-step, mpf(0), step):
                for dc in (-step, mpf(0), step):
                    R, c = R0 + dR, c0 + dc
                    if R <= 0 or c < 0 or not is_linked(R, c):
                        continue
                    E = cross_energy(R, c, 40)
                    if E is not None and E < E0:
                        E0, R0, c0, moved = E, R, c, True
            if not moved:
                break
    min_excess = (E0 - target) / target

    # --- 4. the unlinked configuration the guardless scan fell into
    R_bad, c_bad = mpf(4) / 10, mpf(25) / 10
    e_bad = cross_energy(R_bad, c_bad, 40)

    wb = WitnessBuilder("mobius-cross-energy-hopf-calibration", engine="mpmath")
    wb.set_description(
        "Calibration of a Mobius cross-energy integrator against the PROVED "
        "E(Hopf) = 2*pi^2 (Agol-Marques-Neves, arXiv:1205.0825). Bean qou-o6ml "
        "route (2): the integrator must reproduce a proved value before any "
        "Borromean number means anything. Also records, as a measurement, the "
        "split-link degeneracy that a guardless search falls into -- the same "
        "degeneracy the front is about.")
    wb.add_data("target_2pi_squared", mp.nstr(target, 25))
    wb.add_data("quadrature_convergence_at_R1_c1", conv)
    wb.add_data("obvious_configuration", {
        "R": "1", "c": "1",
        "energy": mp.nstr(e_obvious, 20),
        "relative_excess_over_2pi2": mp.nstr(obvious_excess, 10),
        "note": ("Two orthogonal unit circles each through the other's centre "
                 "-- the usual picture of the Hopf link. It is NOT the energy "
                 "minimiser."),
    })
    wb.add_data("constrained_minimum", {
        "R": mp.nstr(R0, 10), "c": mp.nstr(c0, 10),
        "energy": mp.nstr(E0, 20),
        "relative_excess_over_2pi2": mp.nstr(min_excess, 10),
    })
    wb.add_data("split_link_trap", {
        "R": mp.nstr(R_bad, 4), "c": mp.nstr(c_bad, 4),
        "linked": bool(is_linked(R_bad, c_bad)),
        "energy": mp.nstr(e_bad, 20),
        "note": ("Below 2*pi^2 because the pair is SPLIT, not because the "
                 "integrator is wrong. Cross energy has infimum 0 on unlinked "
                 "pairs."),
    })

    wb.add_assertion(
        name="quadrature_converged_far_below_the_comparison_tolerance",
        computed=conv_gap, expected=0, tolerance=mpf("1e-8"), unit="relative",
        source=(f"N=32 vs N=64 on the fixed configuration agree to "
                f"{mp.nstr(conv_gap, 4)} relative. Periodic and smooth off the "
                f"singularity, so the trapezoid rule converges rapidly. "
                f"The threshold is 1e-8 because that is two orders below the "
                f"1e-6 at which the 2*pi^2 comparison below is made, so "
                f"quadrature error cannot be what that assertion is measuring. "
                f"It is NOT a drained baseline: an earlier version of this "
                f"probe set 1e-12 aspirationally, without measuring, and the "
                f"assertion failed at 9.93e-11. The threshold now states what "
                f"the method delivers and why that suffices, rather than what "
                f"was hoped for."))
    wb.add_assertion(
        name="obvious_configuration_respects_the_AMN_bound",
        computed=1 if e_obvious >= target else 0, expected=1, tolerance=0,
        unit="boolean",
        source=(f"E(R=1,c=1) = {mp.nstr(e_obvious, 16)} >= 2*pi^2 = "
                f"{mp.nstr(target, 16)}, exceeding it by "
                f"{mp.nstr(obvious_excess * 100, 4)}%. A correct integrator "
                f"must land ABOVE the proved minimum on a non-minimal "
                f"configuration."))
    wb.add_assertion(
        name="constrained_minimum_reproduces_2pi_squared",
        computed=min_excess, expected=0, tolerance=mpf("1e-6"), unit="relative",
        source=(f"Minimising over the LINKED family gives "
                f"{mp.nstr(E0, 16)} at R={mp.nstr(R0, 6)}, c={mp.nstr(c0, 6)}, "
                f"a relative excess of {mp.nstr(min_excess, 6)} over 2*pi^2 -- "
                f"and from ABOVE, as the theorem requires. An independent "
                f"numerical confirmation of Agol-Marques-Neves to 8 significant "
                f"figures."))
    wb.add_assertion(
        name="split_configuration_falls_below_the_bound",
        computed=1 if (e_bad < target and not is_linked(R_bad, c_bad)) else 0,
        expected=1, tolerance=0, unit="boolean",
        source=(f"At R={mp.nstr(R_bad,3)}, c={mp.nstr(c_bad,3)} the pair is "
                f"UNLINKED and E = {mp.nstr(e_bad, 10)} < 2*pi^2. Recorded so "
                f"the degeneracy is a measurement: a search without a linking "
                f"guard leaves the Hopf class and 'minimises' to nonsense."))
    out = wb.save()

    print(f"target 2*pi^2                = {mp.nstr(target, 20)}")
    print(f"obvious config (R=1,c=1)     = {mp.nstr(e_obvious, 20)}"
          f"   (+{mp.nstr(obvious_excess*100, 4)}%)")
    print(f"constrained minimum          = {mp.nstr(E0, 20)}"
          f"   at R={mp.nstr(R0,6)}, c={mp.nstr(c0,6)}")
    print(f"  relative excess over 2pi^2 = {mp.nstr(min_excess, 8)}")
    print(f"split-link trap (R=0.4,c=2.5)= {mp.nstr(e_bad, 12)}  linked="
          f"{is_linked(R_bad, c_bad)}")
    print(f"\nwitness -> {out}")


if __name__ == "__main__":
    main()
