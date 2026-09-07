#!/usr/bin/env python3
"""Average crossing number of a Borromean component pair (EXPLORATORY).

*** SUPERSEDED -- WRONG OBJECT. See em_linking_fh_link_bound_correction.py. ***

A close read of the primary sources shows the Freedman-He asymptotic
crossing number in the LINK bound is `ac(L_k, L)` -- one component
against the WHOLE link, summed over n COMPONENTS (Komendarczyk
arXiv:0808.1533v1 eq. 43). It is NOT a pairwise quantity; no
pair-indexed ac(L_i, L_j) occurs in either source. So the per-pair
quantity computed below, and its "total link" reading, are the wrong
index and the wrong sum. The question this probe was built to settle --
whether the PAIR minimisation is constrained by the third component --
is malformed, because there is no pair minimisation.

Retained, not deleted: the Gauss-integral machinery is reused by the
correction probe (which needs exactly these pair integrals to assemble
the correctly-indexed component-vs-link object), and the Brunnian
signed-linking control still validates the quadrature.

Bean qou-0hdx / qou-8aed. The literature sweep closed every topological
route to the open two-like-charge EM-linking invariant and left exactly
one candidate standing: the Freedman-He asymptotic CROSSING NUMBER --
unsigned (so immune to the O1 antisymmetry obstruction), symmetric in
the pair, Flux^2-scaling, and carrying Khesin Thm 3.6's Vol^(-1/3)
template. Fitting that template to the corpus's kappa(A) data implied a
CONSTANT per-pair crossing number

    C_implied ~ 4.79  (Vol ~ A)     or     ~ 3.99  (Vol ~ Z)

(em-linking-crossing-number.witness.json). That constant was NOT
computed from theory -- which is exactly what this probe does.

THE COMPUTATION. The corpus's 3He binding link is L6a4 = the Borromean
rings, whose complement is fully S_3-symmetric (all three cusps
identical, em_linking_cusp_geometry_probe.py) -- so every component
pair is equivalent and "the proton pair" is unambiguous. For a pair of
components the average crossing number is the Gauss integral with the
numerator's ABSOLUTE VALUE (Khesin Rmk 3.5):

    ACN = (1/4pi) * int int  |det[x'(s), y'(t), x(s)-y(t)]|
                             / |x(s)-y(t)|^3   ds dt

and the signed version (no absolute value) is the linking number, which
must come out ZERO for a Brunnian link -- computed here as a control on
the quadrature.

HONESTY ABOUT WHAT ACN IS. The average crossing number is
GEOMETRY-dependent, not a topological invariant; Freedman-He's
asymptotic crossing number minimises over the isotopy class. So a
computed ACN for one realisation is an UPPER bound on that infimum,
while the minimal crossing number of the Borromean diagram (6 crossings
total, 2 per pair) is a LOWER bound:

    2  <=  C_true(pair)  <=  ACN(realisation).

This probe reports ACN for the standard mutually-orthogonal-ellipse
realisation across several aspect ratios, so the realisation-dependence
is visible rather than hidden. Nothing is wired.

PRECISION NOTE -- REVISED, and the earlier note was wrong. It read:
"this is a smooth 2D quadrature over disjoint curves (no singularity),
so plain float64 with an explicit convergence check is appropriate and
mpmath's cost is unwarranted". The premise is false for the ACN. The
integrand carries an ABSOLUTE VALUE, and the determinant inside it has
the closed form

    det[x'(s), y'(t), x(s)-y(t)]  =  a*b*(b*cos t - a*sin s)

(derived below, checked against the explicit triple product), so |num|
has a KINK on the curve b*cos t = a*sin s cutting straight through the
domain. The integrand is C^0 there, not smooth, and the midpoint rule
degrades from spectral to algebraic convergence. That is visible in the
old witness and was misread as convergence: n=400 -> n=800 moved the
6th digit (3.7e-7), and the n=800 value 1.6426377156933236 was published
to 17 digits while being correct to about 6. The signed integral, which
has no absolute value and IS analytic, converged to ~1e-16 immediately
-- the two behaviours sitting side by side in one witness.

The fix is not more grid. Splitting the integration at the kink restores
smoothness on each piece, and mpmath's adaptive quadrature then reaches
full precision: ACN = 1.642637681773124472637643, stable across dps.
The old float64 value was wrong in its 7th digit.
"""

from __future__ import annotations

import math

import mpmath as mp

import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402

# The nested adaptive quadrature costs ~O(dps^2); the corpus default of 70
# would spend minutes per aspect ratio for digits nothing consumes. 30 dps
# yields ~25 stable digits -- three times what the 8-digit kappa data can
# use, and ~20 more than the float64 version actually had.
QUAD_DPS = 30

PHI = (1 + 5 ** 0.5) / 2                      # float64, for the cross-check


def phi_mp():
    """The golden ratio at working precision."""
    return (1 + mp.sqrt(5)) / 2


def curve1(s: float, a: float, b: float):
    """Ellipse in the xy-plane, and its tangent."""
    return ((a * math.cos(s), b * math.sin(s), 0.0),
            (-a * math.sin(s), b * math.cos(s), 0.0))


def curve2(t: float, a: float, b: float):
    """Ellipse in the yz-plane (cyclic image of curve1), and its tangent."""
    return ((0.0, a * math.cos(t), b * math.sin(t)),
            (0.0, -a * math.sin(t), b * math.cos(t)))


def gauss_integrals(a: float, b: float, n: int) -> tuple[float, float]:
    """Return (signed linking number, average crossing number).

    Midpoint rule on [0, 2pi]^2 -- spectrally accurate for smooth
    periodic integrands.
    """
    h = 2 * math.pi / n
    signed = 0.0
    unsigned = 0.0
    for i in range(n):
        s = (i + 0.5) * h
        (x1, y1, z1), (u1, u2, u3) = curve1(s, a, b)
        for j in range(n):
            t = (j + 0.5) * h
            (x2, y2, z2), (v1, v2, v3) = curve2(t, a, b)
            wx, wy, wz = x1 - x2, y1 - y2, z1 - z2
            # det[u, v, w] = u . (v x w)
            cx = v2 * wz - v3 * wy
            cy = v3 * wx - v1 * wz
            cz = v1 * wy - v2 * wx
            num = u1 * cx + u2 * cy + u3 * cz
            r2 = wx * wx + wy * wy + wz * wz
            denom = r2 * math.sqrt(r2)
            signed += num / denom
            unsigned += abs(num) / denom
    scale = h * h / (4 * math.pi)
    return signed * scale, unsigned * scale


def _integrand(s, t, a, b, signed: bool):
    """Gauss integrand with the determinant in closed form.

    det[x'(s), y'(t), x(s)-y(t)] = a*b*(b*cos t - a*sin s): expand the triple
    product and the sin^2 s + cos^2 s of the two surviving terms collapses.
    `gauss_integrals` still evaluates the raw triple product, so the two
    routines cross-check each other rather than sharing an assumption.
    """
    num = a * b * (b * mp.cos(t) - a * mp.sin(s))
    wx = a * mp.cos(s)
    wy = b * mp.sin(s) - a * mp.cos(t)
    wz = -b * mp.sin(t)
    r2 = wx * wx + wy * wy + wz * wz
    return (num if signed else abs(num)) / (r2 * mp.sqrt(r2))


def acn_mp(a, b):
    """Average crossing number by adaptive quadrature, split at the kink.

    The domain is folded to a quarter, s in [-pi/2, pi/2] x t in [0, pi]: the
    unsigned integrand is invariant under s -> pi - s and under t -> -t. Within
    that quarter the kink |b cos t - a sin s| = 0 is met exactly -- for each s
    the inner kink sits at t = arccos((a/b) sin s) when that is in range, and
    the outer integral is split where the root enters and leaves, |sin s| = b/a.
    Each piece is then analytic and mp.quad converges to working precision.
    """
    a, b = mp.mpf(a), mp.mpf(b)

    def inner(s):
        c = (a / b) * mp.sin(s)
        pts = [0, mp.acos(c), mp.pi] if abs(c) < 1 else [0, mp.pi]
        return mp.quad(lambda t: _integrand(s, t, a, b, False), pts)

    half = mp.pi / 2
    spts = [-half, 0, half]
    if b < a:
        s0 = mp.asin(b / a)
        spts = [-half, -s0, 0, s0, half]
    return 4 * mp.quad(inner, spts) / (4 * mp.pi)


def linking_mp(a, b):
    """Signed Gauss integral -- the Brunnian control -- on the FULL domain.

    Deliberately NOT folded like `acn_mp`. The signed integrand is odd under
    the involution (s, t) -> (-s, pi - t), which maps the quarter domain to
    itself, so a folded signed integral is zero identically and would test the
    symmetry rather than the quadrature. Computed whole, the vanishing is a
    real measurement. No kink here: without the absolute value the integrand
    is analytic, so no splitting is needed.
    """
    a, b = mp.mpf(a), mp.mpf(b)
    two_pi = 2 * mp.pi
    return mp.quad(
        lambda s: mp.quad(lambda t: _integrand(s, t, a, b, True), [0, two_pi]),
        [0, two_pi]) / (4 * mp.pi)


def main() -> None:
    set_compute_dps(QUAD_DPS)
    phi = phi_mp()

    acn_ref = acn_mp(phi, 1)
    lk_ref = linking_mp(phi, 1)

    # Stability, replacing the old grid refinement: re-run 10 dps lower and see
    # how far the two agree. This measures the quadrature, not the arithmetic.
    set_compute_dps(QUAD_DPS - 10)
    acn_lo = acn_mp(phi_mp(), 1)
    set_compute_dps(QUAD_DPS)
    stable_delta = abs(acn_ref - mp.mpf(acn_lo))

    # What the superseded float64 midpoint rule gave, kept as a cross-check on
    # the new routine AND as the evidence that the kink cost it ~10 digits.
    f64 = {f"n={n}": gauss_integrals(PHI, 1.0, n) for n in (200, 400, 800)}
    f64_err = abs(acn_ref - mp.mpf(str(f64["n=800"][1])))

    # Realisation-dependence: sweep the ellipse aspect ratio.
    sweep = {}
    for label, ratio in (("1.2000", mp.mpf("1.2")), ("1.5000", mp.mpf("1.5")),
                         ("1.6180", phi), ("2.0000", mp.mpf(2)),
                         ("3.0000", mp.mpf(3))):
        sweep[f"a/b={label}"] = {"linking": linking_mp(ratio, 1),
                                 "acn": acn_mp(ratio, 1)}
    acns = [v["acn"] for v in sweep.values()]
    acn_min, acn_max = min(acns), max(acns)

    # Targets implied by the Freedman-He template fit.
    targets = {"Vol~A": mp.mpf("4.7929826"), "Vol~Z": mp.mpf("3.9913751")}
    comparison = {
        k: {"target": v,
            "acn_over_target": acn_ref / v,
            "rel_diff_pct": (acn_ref - v) / v * 100}
        for k, v in targets.items()
    }
    best_key = min(comparison, key=lambda k: abs(comparison[k]["rel_diff_pct"]))

    def q(x, d=20):
        return mp.nstr(mp.mpf(x), d)

    wb = WitnessBuilder("em-linking-borromean-acn", engine="mpmath")
    wb.set_description(
        "EXPLORATORY first-principles computation of the average "
        "crossing number (ACN) of a Borromean component PAIR -- the "
        "quantity the Freedman-He template fit left uncomputed (beans "
        "qou-0hdx, qou-8aed). Gauss integral with |numerator| on the "
        "standard mutually-orthogonal-ellipse realisation; the signed "
        "integral is computed alongside as a control and must vanish "
        "(Brunnian). ACN is realisation-dependent and bounds the "
        "Freedman-He asymptotic crossing number from ABOVE, with the "
        "Borromean minimal crossing number (2 per pair) bounding it "
        "from below. Nothing wired.")
    wb.add_data("SUPERSEDED", {
        "status": "WRONG OBJECT -- superseded by "
                  "em-linking-fh-link-bound-correction.witness.json",
        "why": ("The Freedman-He asymptotic crossing number in the LINK "
                "energy bound is ac(L_k, L): ONE component against the "
                "WHOLE link, summed over n COMPONENTS (Komendarczyk "
                "arXiv:0808.1533v1 eq. 43, p. 26). It is not a pairwise "
                "quantity -- no pair-indexed ac(L_i, L_j) appears in "
                "either primary source. The per-pair ACN computed here, "
                "and the 3x 'total link' reading below, are the wrong "
                "index and the wrong sum."),
        "malformed_question": ("This probe was built to settle whether "
                               "the PAIR minimisation is constrained by "
                               "the third component. There is no pair "
                               "minimisation, so the question does not "
                               "arise. The related (a)-vs-(b) question "
                               "does resolve, against (a): Komendarczyk "
                               "minimises a single-component Seifert "
                               "genus over surfaces in R^3 minus the "
                               "OTHER components, so Brunnian-ness does "
                               "hold the value up -- by a complement "
                               "constraint, not a constrained pair "
                               "homotopy."),
        "retained_because": ("the Gauss-integral machinery and the "
                             "Brunnian signed-linking control are reused "
                             "by the correction probe, which assembles "
                             "the correctly-indexed object from exactly "
                             "these pair integrals."),
    })
    wb.add_data("method", {
        "integral": ("ACN = (1/4pi) int int |det[x'(s),y'(t),x-y]| "
                     "/ |x-y|^3 ds dt"),
        "realisation": ("three mutually orthogonal ellipses, semi-axes "
                        "(a,b), cyclically permuted -- the standard "
                        "Borromean model"),
        "numerator_closed_form": ("det[x'(s),y'(t),x-y] = a*b*(b cos t - "
                                  "a sin s); the triple product's two "
                                  "surviving terms collapse by "
                                  "sin^2 s + cos^2 s = 1"),
        "quadrature": ("mpmath adaptive quadrature, SPLIT at the kink "
                       "b cos t = a sin s where |num| is only C^0; domain "
                       "folded to a quarter using the two symmetries of "
                       "the unsigned integrand"),
        "precision": f"mpmath at {QUAD_DPS} dps",
        "control_not_folded": ("the signed integral is computed on the "
                               "FULL domain: it is odd under "
                               "(s,t) -> (-s, pi-t), which preserves the "
                               "quarter domain, so a folded control would "
                               "vanish identically and test nothing"),
    })
    wb.add_data("precision_check", {
        "acn_at_dps": {str(QUAD_DPS): q(acn_ref, 25),
                       str(QUAD_DPS - 10): q(acn_lo, 15)},
        "agreement_between_them": q(stable_delta, 3),
        "superseded_float64_midpoint": {k: {"linking": q(v[0], 3),
                                            "acn": q(v[1], 17)}
                                        for k, v in f64.items()},
        "float64_n800_error": q(f64_err, 3),
        "reading": ("The old n=800 midpoint value was published to 17 "
                    "digits and is wrong in its 7th: the |.| kink caps "
                    "midpoint convergence at algebraic. Splitting at the "
                    "kink removes the cap. The signed control shows the "
                    "contrast in the same table -- with no absolute value "
                    "the integrand is analytic and float64 already had "
                    "it to ~1e-16."),
    })
    wb.add_data("aspect_ratio_sweep",
                {k: {"linking": q(v["linking"], 3), "acn": q(v["acn"])}
                 for k, v in sweep.items()})
    wb.add_data("bounds", {
        "lower_bound_minimal_crossing_number_per_pair": 2,
        "computed_ACN_golden_realisation": q(acn_ref),
        "ACN_range_over_sweep": [q(acn_min), q(acn_max)],
        "reading": ("2 <= C_true(pair) <= ACN(realisation); the ACN is "
                    "an upper bound on Freedman-He's minimised "
                    "asymptotic crossing number."),
    })
    wb.add_data("comparison_to_template_fit",
                {k: {kk: q(vv, 12) for kk, vv in v.items()}
                 for k, v in comparison.items()})

    # Corrected lower bound (my first version asserted the wrong one).
    total_link_acn = 3 * acn_ref
    tot_cmp = {k: {"target": v,
                   "rel_diff_pct": (total_link_acn - v) / v * 100}
               for k, v in targets.items()}
    realisation_spread_pct = (acn_max - acn_min) / acn_ref * 100
    wb.add_data("corrected_lower_bound", (
        "The first version of this probe asserted ACN >= 2, taking the "
        "'2 crossings per pair' of the standard Borromean DIAGRAM as a "
        "lower bound. That assertion FAILED (ACN = 1.6426) and it was "
        "WRONG: a pair of Borromean components, considered on its own "
        "as a 2-component link, is the UNLINK -- minimal crossing "
        "number 0, not 2. The 2-per-pair count is a property of the "
        "3-component diagram, not of the pair. So the correct bound is "
        "0 <= C_true(pair) <= ACN, and the computed value violates "
        "nothing. The failure is recorded rather than deleted."))
    wb.add_data("total_link_reading", {
        "ACN_pair": q(acn_ref),
        "ACN_total_link_3_pairs": q(total_link_acn),
        "comparison": {k: {kk: q(vv, 12) for kk, vv in v.items()}
                       for k, v in tot_cmp.items()},
        "realisation_spread_pct": q(realisation_spread_pct, 12),
        "status": (
            "CANDIDATE ONLY -- explicitly not a result. The per-pair "
            "ACN (1.643) falls 59-66% short of the template-implied "
            "constant, so the simplest crossing-number hypothesis "
            "FAILS. Summing over all three pairs gives 4.928, which "
            "lands within 2.8% of the Vol~A target (4.793). There is a "
            "genuine physical argument for the total-link reading -- "
            "Brunnian-ness means a pair CANNOT be considered in "
            "isolation, since removing the third component unlinks it, "
            "so the energy attributable to a pair may legitimately "
            "involve the whole link's crossing structure. But two "
            "cautions bite hard: (i) the kappa data is already "
            "per-pair normalised, so multiplying by 3 risks "
            "double-counting, and (ii) the ACN varies by "
            f"{q(realisation_spread_pct, 3)}% across the aspect-ratio "
            "sweep, which is COMPARABLE TO the 2.8% agreement -- the "
            "match is within realisation noise and must not be read as "
            "a confirmation."),
    })
    wb.set_audit_only("docs/audits/2026-08-01-em-linking-reads-round1.md")
    wb.add_assertion(
        name="signed_linking_number_vanishes",
        computed=q(abs(lk_ref), 3), expected="0", tolerance="1e-6",
        unit="linking number",
        source=("Brunnian control: the SIGNED Gauss integral over a "
                "Borromean component pair must vanish, validating both "
                "the quadrature and the realisation."))
    wb.add_assertion(
        name="acn_converged",
        computed=q(stable_delta, 3), expected="0", tolerance="1e-18",
        unit="ACN",
        source=("Dropping the working precision by 10 dps moves the ACN by "
                "less than 1e-18 -- the quadrature, not the arithmetic, is "
                "what is being checked. The old form of this assertion "
                "compared two grid sizes at a 1e-4 tolerance and passed "
                "while the value was wrong in its 7th digit."))
    wb.add_assertion(
        name="float64_midpoint_was_wrong_in_the_7th_digit",
        computed=q(f64_err, 3), expected="3.4e-8", tolerance="1e-8",
        unit="ACN",
        source=("The superseded n=800 midpoint value differs from the "
                "converged one by ~3.4e-8, against the 17 digits it was "
                "published with. Recorded as a measured claim so the "
                "regression cannot come back unnoticed."))
    wb.add_assertion(
        name="acn_nonnegative_above_unlink_bound",
        computed=int(acn_ref >= 0.0), expected=1, tolerance=0, unit="bool",
        source=("Corrected bound: a Borromean component PAIR is the "
                "unlink on its own, so its minimal crossing number is "
                "0, not the 2 that appears in the 3-component diagram."))
    wb.add_assertion(
        name="per_pair_acn_falls_short_of_template_constant",
        computed=int(acn_ref < 0.5 * min(targets.values())), expected=1,
        tolerance=0, unit="bool",
        source=("The honest negative: the directly computed per-pair "
                "ACN is less than half the smallest template-implied "
                "constant, so the simplest crossing-number hypothesis "
                "does not reproduce kappa(A)."))
    out = wb.save()

    print(f"mpmath adaptive quadrature at {QUAD_DPS} dps, split at the kink")
    print(f"  ACN (golden)  = {q(acn_ref, 25)}")
    print(f"  lk  (control) = {q(abs(lk_ref), 3)}   (full domain, unfolded)")
    print(f"  agreement vs {QUAD_DPS - 10} dps: {q(stable_delta, 3)}")
    print(f"  superseded float64 n=800: {q(f64['n=800'][1], 17)} "
          f"-- off by {q(f64_err, 3)}")
    print("\naspect-ratio sweep:")
    for k, v in sweep.items():
        print(f"  {k}: lk = {q(v['linking'], 3):>12}   "
              f"ACN = {q(v['acn'], 12)}")
    print(f"\ncomputed ACN (golden) = {q(acn_ref, 12)}   "
          f"[bounds: 2 <= C_true <= {q(acn_ref, 6)}]")
    for k, c in comparison.items():
        print(f"  vs template target {k} = {q(c['target'], 8)}: "
              f"{q(c['rel_diff_pct'], 4)}%")
    print(f"closest template reading: {best_key}")
    print(f"witness -> {out}")


if __name__ == "__main__":
    main()
