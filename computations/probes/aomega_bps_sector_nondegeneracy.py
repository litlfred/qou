#!/usr/bin/env python3
"""A_ω BPS-sector non-degeneracy check (bean qou-ujmw).

Gate question (owner directive 2026-08-02): does the BPS count of the
figure-eight 4₁ reproduce the GGM resurgent-Stokes / DT spectrum {3,4}
(reduced-Stokes 3) *through* the knot-homology↔BPS bridge?

The answer depends on WHICH published BPS sector:

  OPEN sector  — Gukov–Stošić (1112.0030): knot homology = space of OPEN
                 BPS states (conormal Lagrangian L_K ⊂ T*S³; colored HOMFLY
                 homology). The knots–quivers correspondence (1707.02991)
                 gives one quiver node per HOMFLY-PT generator, so the 4₁
                 count is det(4₁) = 5.  5 ∉ {3,4}  ⇒  FAILS.

  CLOSED sector — GPPV (1701.06567) + GGM peacock Conj 3(d) (2012.00062):
                 resurgent Stokes constant = DT invariant = dim of the BPS
                 Hilbert space of T[M₃]. Reproduces {3,4} / reduced-3
                 (corpus + StokesQZeroDTCount q→0 anchor).  ⇒  PASSES.

This script does pure integer bookkeeping (no fit, no mpmath): it records the
two sector counts and the honest verdict. det values via the Alexander
polynomial at t = -1 (calibrated on the trefoil against the KRSS worked example).
"""
import json
import datetime
from fractions import Fraction

from pathlib import Path as _PathW  # noqa: E402 — witness output root
_HERE_W = _PathW(__file__).resolve().parent


def det_from_alexander(coeffs_at_minus1):
    """|Δ_K(-1)| = knot determinant = rank of thin reduced HOMFLY/Kh homology
    = number of quiver nodes in the knots–quivers correspondence.

    Takes a Fraction, returns an int.  It used to take a float built with
    ``1 / (-1)``, which is float64 arithmetic in a ``computations/`` probe --
    harmless at these magnitudes but banned outright by AGENTS.md
    §"PROBES ARE NOT EXEMPT", and a probe's conclusion is an argument nothing
    re-derives.  Exact now.
    """
    v = abs(Fraction(coeffs_at_minus1))
    assert v.denominator == 1, f"non-integral determinant {v}"
    return v.numerator


def main():
    _t = Fraction(-1)
    # Δ_{3_1}(t) = t - 1 + t^{-1} ; at t=-1: -1 -1 -1 = -3  -> det 3  (KRSS: 3-node quiver)
    det_trefoil = det_from_alexander(_t - 1 + 1 / _t)
    # Δ_{4_1}(t) = -t + 3 - t^{-1} ; at t=-1: 1 + 3 + 1 = 5   -> det 5  (5-node quiver)
    det_fig8 = det_from_alexander(-_t + 3 - 1 / _t)

    # CONFIRMED, not inferred (bean qou-48dw).  The 5 below used to reach the
    # witness only through the knots-quivers rule "#nodes = #HOMFLY generators
    # = det".  It is now READ off the quiver Singh et al. print for 4_1
    # (physrevd108106023, sections/sec-005-1-u2-r2.md): a 5x5 matrix over a
    # motivic sum in five indices d1..d5.  See
    # computations/qbeta/d1b_published_41_quiver_confirms_node_count_probe.py.
    open_count_4_1 = det_fig8                        # Gukov–Stošić / knots-quivers
    published_nodes_4_1 = 5                          # read off C_41
    ggm_dt_spectrum = [3, 4]                          # GGM peacock eq 98 (closed sector)
    reduced_stokes = 3                                # (S₁₂+S₂₁)/S₁₁, all q (corpus q^400)
    qzero_anchor = 3                                  # StokesQZeroDTCount: S⁺(0)₀₁ = 3

    open_reproduces = open_count_4_1 in ggm_dt_spectrum
    closed_reproduces = (reduced_stokes in ggm_dt_spectrum) and (qzero_anchor == reduced_stokes)

    assertions = [
        {
            "name": "trefoil_calibration_det_eq_quiver_nodes",
            "computed": int(round(det_trefoil)),
            "expected": 3,
            "passed": int(round(det_trefoil)) == 3,
            "source": "det(3_1)=3 = # KRSS trefoil quiver nodes = # HOMFLY generators (1707.02991)",
        },
        {
            "name": "open_HOMFLY_count_4_1_is_det_five",
            "computed": open_count_4_1,
            "expected": 5,
            "passed": open_count_4_1 == 5,
            "source": "Gukov–Stošić open-BPS / knots-quivers: 4_1 count = det(4_1) = 5",
        },
        {
            "name": "open_count_confirmed_against_published_quiver",
            "computed": published_nodes_4_1,
            "expected": open_count_4_1,
            "passed": published_nodes_4_1 == open_count_4_1,
            "source": (
                "CONFIRMED, not inferred (bean qou-48dw). The count is read off "
                "the explicit C_41 that Singh et al. print (physrevd108106023, "
                "Phys. Rev. D 108, 106023, sections/sec-005-1-u2-r2.md): a 5x5 "
                "symmetric matrix over a motivic sum in five indices. The OCR "
                "transcription is cross-validated -- all 15 independent entries "
                "are reproduced from the quadratic form in the exponent of the "
                "motivic series printed in the same passage. The rule '#nodes = "
                "det' is confirmed at FOUR knots (3_1->3, 4_1->5, 6_1->9, "
                "8_1->13), so this probe is right for the right reason rather "
                "than by a one-knot coincidence."
            ),
        },
        {
            "name": "open_sector_does_NOT_reproduce_GGM_spectrum",
            "computed": int(open_reproduces),
            "expected": 0,
            "passed": open_reproduces is False,
            "source": "5 ∉ {3,4}: the open-HOMFLY Gukov–Stošić bridge FAILS the gate",
        },
        {
            "name": "closed_sector_reproduces_reduced_stokes_three",
            "computed": int(closed_reproduces),
            "expected": 1,
            "passed": closed_reproduces is True,
            "source": "GGM Conj 3(d)+GPPV: reduced-Stokes 3 ∈ {3,4}; q→0 anchor 3 (StokesQZeroDTCount) PASSES",
        },
    ]
    all_passed = all(a["passed"] for a in assertions)

    witness = {
        "engine": "python-int",
        "engineVersion": "python-stdlib",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "computation": "aomega-bps-sector-nondegeneracy",
        "scriptFile": "aomega_bps_sector_nondegeneracy.py",
        "contentBlock": "conj:stokes-dt-bps-bridge",
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "open_sector": {
                "bridge": "Gukov–Stošić 1112.0030 (open BPS / colored HOMFLY homology)",
                "count_4_1": open_count_4_1,
                "route": "knots–quivers 1707.02991: #nodes = #HOMFLY generators = det",
                "count_provenance": {
                    "status": "CONFIRMED against a published explicit quiver",
                    "was": "inferred from det(4_1) via the knots-quivers rule",
                    "now": "read off C_41, a 5x5 symmetric matrix over a motivic "
                           "sum in five indices",
                    "source": "physrevd108106023 (Singh et al., Phys. Rev. D 108, "
                              "106023), sections/sec-005-1-u2-r2.md",
                    "transcription_cross_validated": "all 15 independent entries "
                        "agree with the quadratic form in the motivic series "
                        "exponent, a separately-typeset object in the same passage",
                    "rule_confirmed_at": {"3_1": 3, "4_1": 5, "6_1": 9, "8_1": 13},
                    "probe": "computations/qbeta/"
                             "d1b_published_41_quiver_confirms_node_count_probe.py",
                    "effect_on_verdict": "NONE, and the direction matters: "
                        "confirming that the 5 is real makes this sector's FAIL "
                        "stronger, not weaker. 5 is still not in {3,4}.",
                    "bean": "qou-48dw",
                },
                "reproduces_GGM_3_4": open_reproduces,
                "verdict": "FAIL — 5 ∉ {3,4}; wrong BPS sector for A_ω",
            },
            "closed_sector": {
                "bridge": "GPPV 1701.06567 + GGM peacock Conj 3(d) 2012.00062",
                "ggm_dt_spectrum": ggm_dt_spectrum,
                "reduced_stokes_constant": reduced_stokes,
                "qzero_anchor_lean": qzero_anchor,
                "reproduces_GGM_3_4": closed_reproduces,
                "verdict": "PASS — reduced-Stokes 3 ∈ {3,4}; licenses A_ω(4_1)=3 (theorem for 4_1)",
            },
        },
        "discipline": (
            "Honest non-degeneracy gate. The owner-named Gukov–Stošić OPEN-HOMFLY "
            "bridge does NOT reproduce the GGM resurgent-Stokes spectrum {3,4}: the "
            "4_1 open-BPS/quiver count is det(4_1)=5, a DISTINCT BPS sector. The "
            "conditional A_ω=3 is therefore adopted on the CLOSED-sector bridge "
            "(GGM Conj 3(d) + GPPV), which reproduces {3,4}/reduced-3. No fit; no "
            "production wiring (L2/Q_β untouched); conditional (theorem for 4_1), "
            "internal QOU-driver derivation still open (qou-qnnq)."
        ),
    }
    out = _HERE_W / "aomega-bps-sector-nondegeneracy.witness.json"
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)
    print(f"open-sector 4_1 count = {open_count_4_1} (det); reproduces {{3,4}}? {open_reproduces}")
    print(f"closed-sector reduced-Stokes = {reduced_stokes} ∈ {ggm_dt_spectrum}? {closed_reproduces}")
    print(f"allPassed={all_passed}  ->  {out}")


if __name__ == "__main__":
    main()
