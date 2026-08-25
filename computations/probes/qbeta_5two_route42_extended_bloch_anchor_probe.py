#!/usr/bin/env python3
"""Route 42 -- the 5_2 volume anchor, and WHY the ordinary Bloch group is blind
to the sum rule. Plus a correction to a branch assignment this session got wrong.

Bean `qou-0yqu`. Follows Routes 40 (the tower is the powers of one generator)
and 41 (the ladder family does not determine A).

THE ANCHOR
----------
The field is not merely "the cubic field of discriminant -23" -- it is the
**5_2 knot's trace field**, and the knot's hyperbolic volume is carried by the
very roots the sum rule is about:

    Vol(5_2) = 3 * D(y_1)          y_1 the complex root of y^3-2y^2+3y-1
    Vol(5_2) = 6 * D(c_1)          c_1 the complex root of X^3+X^2-1  (c = 1/rho)

with `D` the Bloch-Wigner dilogarithm (G1). Checked against a published value of
the volume, so it is an identification of `y_1` as the tetrahedron shape and not
a tautology.

WHY EVERY LADDER ROUTE FAILED -- now measured, not conjectured
-------------------------------------------------------------
`D(y_1)` is nonzero and carries the whole volume. But summed over the Galois
orbit it **cancels identically**: `y_2 = conj(y_1)` and `D(conj z) = -D(z)`,
while the real root gives `D = 0`. So `sum_sigma D(sigma y) = 0` (G4) -- for
every element of every number field, by conjugate symmetry, not by any accident
of this one.

The Bloch-Wigner function is precisely the regulator the ordinary Bloch group
computes. So the whole five-term / Bloch-group apparatus evaluates to zero on a
Galois-summed dilogarithm and can carry no information about `A`. That is a
structural reason for the failures of Routes 1-5, 40 and 41, replacing "it did
not close" with "it cannot".

And the sum rule itself lives entirely in the part `D` discards (G3):

    sum_j Re(V_j) = -3*pi^2/2                    (the sum rule)
    sum_j Im(V_j) = 2*pi*log(y_3)                (elementary -- NO volume)

Both halves elementary. The volume appears nowhere in the Galois sum.

⚠ A CORRECTION, recorded because the wrong value was asserted first
-------------------------------------------------------------------
`V_j = 3*Li2(y_j) + (log y_j + b_j*pi*i)^2` needs branch integers
`b = (-1, +1, +1)` -- with `+1` on the **real** root. A first attempt this
session assumed `b = (+1, -1, 0)`, taking the real root's branch to be trivial,
and got `-30.822` against a target of `-14.804`. A scan over `b in {-2..2}^3`
then FAILED to find the right answer as well, because it demanded
`Im(sum) = 0` -- which is false, the imaginary part being `2*pi*log(y_3) != 0`.
Two compounding errors, and the sum rule is a statement about `Re` only.
G2 gates the correct assignment AND gates that `(+1,-1,0)` fails.

WHAT THIS POINTS AT
-------------------
The branch integers `b_j` are **flattening data**. The extended Bloch group
(Neumann) is built from exactly such flattenings `(log z + p*pi*i,
log(1-z) + q*pi*i)`, its regulator is the complex volume `Vol + i*CS` rather
than `Vol` alone, and the Rogers dilogarithm is well defined on it. That is the
machinery that retains what `D` throws away, so it is where a proof of the sum
rule should be attempted. Sibling PR #4824 is already in that territory.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import (arg, fabs, im, log, mp, mpc, mpf, nstr, pi, polylog,
                    polyroots, re)
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

# Raise precision BEFORE the module-scope constant below is built.  Without
# this the `mpf` is constructed at the default dps=15 and truncated at birth --
# the `module-const precision` gate flags it LOSSY, correctly.  Setting it here
# is idempotent with the `mp.dps` assignment in `main()`.
mp.dps = 60

# Published hyperbolic volume of the 5_2 knot. Its precision -- not the
# identity's -- is what limits G1, so the gate is set at that scale.
#
# NOTE (2026-08-09): the corpus's authoritative value is `_SNAPPY_HP_50` in
# qou-mass/_internal/knot_volumes.py; Route 71 extended it to 79 dps. This
# probe only needs the 19 digits its own gate is set at, but the constant is
# now built at full precision rather than truncated.
VOL_5_2 = mpf("2.828122088330783162")
VOL_REF_DIGITS = 19


def bloch_wigner(z):
    z = mpc(z)
    if fabs(im(z)) < mpf(10) ** -40:
        return mpf(0)
    return im(polylog(2, z)) + arg(1 - z) * log(abs(z))


def saddle_V(y, branch):
    """The corpus's saddle value, byte-for-byte the definition in
    `qbeta_5two_saddle_sum_rule_and_provenance_probe.py`."""
    return 3 * polylog(2, y) + (log(y) + branch * pi * 1j) ** 2


def split_roots(coeffs):
    rs = polyroots(coeffs, maxsteps=600, extraprec=2000)
    up = [r for r in rs if im(r) > mpf(10) ** -40][0]
    dn = [r for r in rs if im(r) < -(mpf(10) ** -40)][0]
    real = [r for r in rs if fabs(im(r)) < mpf(10) ** -40][0].real
    return up, dn, real


def main() -> int:
    set_compute_dps()
    gates = []

    y1, y2, y3 = split_roots([1, -2, 3, -1])            # the 5_2 saddle cubic
    c1, _, _ = split_roots([1, 1, 0, -1])               # c = 1/rho

    # ---- G1: the volume anchor ---------------------------------------------
    r_y = VOL_5_2 / bloch_wigner(y1)
    r_c = VOL_5_2 / bloch_wigner(c1)
    # RELATIVE, not absolute: the deviation inherited from the reference
    # constant scales with the ratio itself (6.0e-18 at 3, 1.2e-17 at 6 -- the
    # same 2.0e-18 relative). An absolute tolerance passes one and fails the
    # other for no mathematical reason.
    rel_y = fabs(r_y / 3 - 1)
    rel_c = fabs(r_c / 6 - 1)
    tol = mpf(10) ** -(VOL_REF_DIGITS - 2)
    gates.append({
        "gate": "G1",
        "claim": "THE ANCHOR. The field is the 5_2 knot's TRACE FIELD, not merely a cubic field "
                 "of discriminant -23: the knot's hyperbolic volume is 3*D(y_1) at the complex "
                 "root of the saddle cubic, and 6*D(c_1) at the generator c = 1/rho. Checked "
                 "against a PUBLISHED volume, so this identifies y_1 as the tetrahedron shape "
                 "rather than restating a definition. The published constant's precision, not "
                 "the identity's, is what bounds this gate",
        "Vol_5_2_reference": nstr(VOL_5_2, 19),
        "D(y_1)": nstr(bloch_wigner(y1), 25),
        "Vol / D(y_1)": nstr(r_y, 25),
        "Vol / D(c_1)": nstr(r_c, 25),
        "relative_deviation_from_3": nstr(rel_y, 8),
        "relative_deviation_from_6": nstr(rel_c, 8),
        "both_consistent_with_the_reference_precision": bool(rel_y < tol and rel_c < tol),
        "pass": bool(rel_y < tol and rel_c < tol),
    })

    # ---- G2: the sum rule, and the branch assignment that FAILS -------------
    good = saddle_V(y1, -1) + saddle_V(y2, 1) + saddle_V(y3, 1)
    bad = saddle_V(y1, 1) + saddle_V(y2, -1) + saddle_V(y3, 0)
    target = -3 * pi ** 2 / 2
    gates.append({
        "gate": "G2",
        "claim": "the sum rule reproduces with branch integers b = (-1, +1, +1) -- note the "
                 "REAL root carries +1, not 0. The second half is the negative control and the "
                 "correction: b = (+1, -1, 0), assuming the real root's branch is trivial, "
                 "MISSES by more than 16. It is recorded because that is what this session "
                 "asserted first",
        "Re_sum_with_(-1,+1,+1)": nstr(re(good), 30),
        "target_-3pi^2/2": nstr(target, 30),
        "residual": nstr(fabs(re(good) - target), 12),
        "Re_sum_with_the_WRONG_(+1,-1,0)": nstr(re(bad), 25),
        "how_far_the_wrong_one_misses": nstr(fabs(re(bad) - target), 12),
        "pass": bool(fabs(re(good) - target) < mpf(10) ** -40
                     and fabs(re(bad) - target) > mpf(1)),
    })

    # ---- G3: the imaginary half is elementary too -- no volume in it --------
    im_expected = 2 * pi * log(y3)
    gates.append({
        "gate": "G3",
        "claim": "the imaginary half of the same sum is 2*pi*log(y_3) EXACTLY -- elementary, "
                 "with no volume in it. So both halves of sum V_j are elementary and the "
                 "hyperbolic volume appears nowhere in the Galois sum, even though it is 3*D(y_1) "
                 "at a single root. ⚠ A first pass reported this imaginary part as ZERO; that "
                 "was an artifact of the wrong branch assignment in G2, and a scan that demanded "
                 "Im = 0 therefore rejected the correct answer",
        "Im_sum": nstr(im(good), 30),
        "2_pi_log_y3": nstr(im_expected, 30),
        "residual": nstr(fabs(im(good) - im_expected), 12),
        "pass": bool(fabs(im(good) - im_expected) < mpf(10) ** -40
                     and fabs(im(good)) > mpf(1)),
    })

    # ---- G4: why the ordinary Bloch group is blind --------------------------
    galois_D = sum(bloch_wigner(r) for r in (y1, y2, y3))
    others = mpf(0)
    for co in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 2, -3), (2, -1, 5), (7, -2, 4)]:
        rs = polyroots([1, 1, 0, -1], maxsteps=600, extraprec=2000)
        others = max(others, fabs(sum(
            bloch_wigner(co[0] + co[1] * r + co[2] * r ** 2) for r in rs)))
    gates.append({
        "gate": "G4",
        "claim": "WHY EVERY LADDER ROUTE FAILED. D(y_1) alone carries the entire volume, but "
                 "summed over the Galois orbit D cancels IDENTICALLY -- y_2 = conj(y_1) with "
                 "D(conj z) = -D(z), and the real root gives 0. D is exactly the regulator the "
                 "ordinary Bloch group computes, so that whole apparatus evaluates to zero on a "
                 "Galois-summed dilogarithm and can carry no information about A. This is "
                 "general (conjugate symmetry, every number field), which is why Routes 1-5, 40 "
                 "and 41 could not have closed",
        "D(y_1)_alone": nstr(bloch_wigner(y1), 25),
        "sum_over_the_galois_orbit": nstr(galois_D, 12),
        "worst_over_other_field_elements": nstr(others, 12),
        "pass": bool(fabs(galois_D) < mpf(10) ** -40
                     and others < mpf(10) ** -40
                     and fabs(bloch_wigner(y1)) > mpf(1) / 2),
    })

    # ---- G5: the target is unmoved ------------------------------------------
    def gsum(co):
        f = (lambda z: mpf(co[1]) if z == 0
             else log(sum(co[k] * z ** k for k in range(len(co)))) / z)
        from mpmath import quad
        return -quad(f, [0, 1])
    A = gsum([1, -2, 3, -1])
    gates.append({
        "gate": "G5",
        "claim": "the target is unmoved. A = sum Li2(y_j) still has no proof, and nothing above "
                 "is progress toward one -- G1 is an anchor, G4 is an obstruction, G2 and G3 are "
                 "corrections. This gate exists so the anchor cannot be misread as the theorem",
        "A": nstr(A, 30),
        "pass": bool(fabs(A - mpf("0.9717306814686482591277741699")) < mpf(10) ** -25),
    })

    out = {
        "probe": "qbeta_5two_route42_extended_bloch_anchor",
        "bean": "qou-0yqu", "dps": mp.dps,
        "follows": ["Route 40 (distribution factors)", "Route 41 (ladder rank)"],
        "corrects": [
            "the branch assignment b = (+1,-1,0) for V_j -- the real root carries +1, not 0 (G2)",
            "'Im(sum V_j) = 0' -- it is 2*pi*log(y_3), and a scan demanding Im = 0 rejected the "
            "correct branch assignment (G3)",
        ],
        "gates": gates,
        "verdict": {
            "anchor": "the field is the 5_2 trace field: Vol(5_2) = 3*D(y_1) = 6*D(c_1).",
            "obstruction": "D cancels identically on a Galois sum, and D is the ordinary Bloch "
                           "group's regulator, so that machinery is structurally blind to A. "
                           "Both halves of sum V_j are elementary; the volume is absent.",
            "next": "the branch integers b_j are FLATTENING data. The extended Bloch group "
                    "(Neumann) is built from flattenings, its regulator is the complex volume "
                    "Vol + i*CS rather than Vol alone, and the Rogers dilogarithm is well "
                    "defined on it -- it retains exactly what D discards. Attempt the proof "
                    "there. Prerequisite: finish Route 41's G4 branch bookkeeping. Sibling "
                    "#4824 is already in extended-Bloch territory.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route42-extended-bloch-anchor.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:74]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + (
        "anchored (Vol = 3*D(y_1)) and the obstruction is now structural: the ordinary Bloch "
        "group's regulator vanishes on Galois sums, so the extended Bloch group is where to go. "
        "The 5_2 sum rule remains verified to 80 dps, unproved."
        if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
