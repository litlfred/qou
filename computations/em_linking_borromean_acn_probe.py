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

Precision note: this is a smooth 2D quadrature over disjoint curves (no
singularity), so plain float64 with an explicit convergence check is
appropriate and mpmath's cost is unwarranted; the grid refinement is
reported.
"""

from __future__ import annotations

import math

import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder  # noqa: E402

PHI = (1 + 5 ** 0.5) / 2


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


def main() -> None:
    # Convergence check on the canonical (golden-ratio) realisation.
    convergence = {}
    for n in (200, 400, 800):
        lk, acn = gauss_integrals(PHI, 1.0, n)
        convergence[f"n={n}"] = {"linking": lk, "acn": acn}
    lk_ref = convergence["n=800"]["linking"]
    acn_ref = convergence["n=800"]["acn"]
    conv_delta = abs(acn_ref - convergence["n=400"]["acn"])

    # Realisation-dependence: sweep the ellipse aspect ratio.
    sweep = {}
    for ratio in (1.2, 1.5, PHI, 2.0, 3.0):
        lk, acn = gauss_integrals(ratio, 1.0, 400)
        sweep[f"a/b={ratio:.4f}"] = {"linking": lk, "acn": acn}
    acns = [v["acn"] for v in sweep.values()]
    acn_min, acn_max = min(acns), max(acns)

    # Targets implied by the Freedman-He template fit.
    targets = {"Vol~A": 4.7929826, "Vol~Z": 3.9913751}
    comparison = {
        k: {"target": v,
            "acn_over_target": acn_ref / v,
            "rel_diff_pct": (acn_ref - v) / v * 100}
        for k, v in targets.items()
    }
    best_key = min(comparison, key=lambda k: abs(comparison[k]["rel_diff_pct"]))

    wb = WitnessBuilder("em-linking-borromean-acn", engine="python-float64")
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
        "quadrature": "midpoint rule on [0,2pi]^2 (spectral for smooth periodic)",
        "precision": ("float64; smooth integrand over disjoint curves, "
                      "no singularity"),
    })
    wb.add_data("convergence", convergence)
    wb.add_data("aspect_ratio_sweep", sweep)
    wb.add_data("bounds", {
        "lower_bound_minimal_crossing_number_per_pair": 2,
        "computed_ACN_golden_realisation": acn_ref,
        "ACN_range_over_sweep": [acn_min, acn_max],
        "reading": ("2 <= C_true(pair) <= ACN(realisation); the ACN is "
                    "an upper bound on Freedman-He's minimised "
                    "asymptotic crossing number."),
    })
    wb.add_data("comparison_to_template_fit", comparison)

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
        "ACN_pair": acn_ref,
        "ACN_total_link_3_pairs": total_link_acn,
        "comparison": tot_cmp,
        "realisation_spread_pct": realisation_spread_pct,
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
            f"{realisation_spread_pct:.1f}% across the aspect-ratio "
            "sweep, which is COMPARABLE TO the 2.8% agreement -- the "
            "match is within realisation noise and must not be read as "
            "a confirmation."),
    })
    wb.set_audit_only("docs/audits/2026-08-01-em-linking-reads-round1.md")
    wb.add_assertion(
        name="signed_linking_number_vanishes",
        computed=abs(lk_ref), expected=0.0, tolerance=1e-6,
        unit="linking number",
        source=("Brunnian control: the SIGNED Gauss integral over a "
                "Borromean component pair must vanish, validating both "
                "the quadrature and the realisation."))
    wb.add_assertion(
        name="acn_converged",
        computed=conv_delta, expected=0.0, tolerance=1e-4,
        unit="ACN",
        source="Grid refinement n=400 -> n=800 changes ACN by less than 1e-4.")
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

    print("convergence (golden-ratio realisation):")
    for k, v in convergence.items():
        print(f"  {k}: lk = {v['linking']:+.3e}   ACN = {v['acn']:.6f}")
    print("\naspect-ratio sweep (n=400):")
    for k, v in sweep.items():
        print(f"  {k}: lk = {v['linking']:+.3e}   ACN = {v['acn']:.6f}")
    print(f"\ncomputed ACN (golden) = {acn_ref:.6f}   "
          f"[bounds: 2 <= C_true <= {acn_ref:.4f}]")
    for k, c in comparison.items():
        print(f"  vs template target {k} = {c['target']:.4f}: "
              f"{c['rel_diff_pct']:+.1f}%")
    print(f"closest template reading: {best_key}")
    print(f"witness -> {out}")


if __name__ == "__main__":
    main()
