#!/usr/bin/env python3
"""The prefactor form is DGLZ eq (2.3) — constant included. It was never a fit.

Beans qou-fl4t / qou-pn5j. `docs/audits/2026-08-08-c-sigma-derivation-status.md`
records, as the single assumption the `c_sigma = 2^(-3/4)` derivation carries:

    c_sigma  ∝  |tau|^(-1/2)      "validated here, not proved"

with the universal constant `k = 2^(-1/2)` described as CALIBRATED on `4_1`, and
`docs/audits/2026-08-08-prefactor-form-what-is-actually-assumed.md` narrowing the
open part to "whether c_sigma depends on tau ALONE".

Both are answered by a paper that has been sitting in `uploads/` uncited.

WHAT DGLZ SAY. Dimofte-Gukov-Lenells-Zagier, "Exact Results for Perturbative
Chern-Simons Theory with Complex Gauge Group" (arXiv:0903.2472,
`uploads/0903.2472v1.pdf`), write the perturbative partition function as

    Z^(rho)(M; hbar) = exp( S_0/hbar - (1/2) delta log hbar
                            + sum_{n>=0} S_{n+1} hbar^n )        (2.1)

and identify the one-loop coefficient with the Ray-Singer torsion of `M` twisted
by the flat bundle `E_rho`:

    S_1^(rho) = (1/2) log( T(M; E_rho) / 2 )                     (2.3)

so the one-loop factor in `Z` is

    exp(S_1) = ( T / 2 )^(1/2) = 2^(-1/2) * T^(1/2).

THE `2^(-1/2)` IS THE `/2` INSIDE THEIR LOG. The corpus's "universal constant,
calibrated on 4_1" is written down in the literature it already cites for the
form. It is not a calibration.

THE EXPONENT SIGN IS A VARIABLE CHOICE, NOT A DISAGREEMENT. DGLZ carry `T^(+1/2)`
where the corpus carries `|tau_DG|^(-1/2)`; the two agree exactly when
`T = 1 / |tau_DG|`, i.e. when the Ray-Singer torsion is the RECIPROCAL of the
corpus's 1-loop invariant. This probe tests that identification rather than
assuming it, and it also disposes of the `tau^(+1/2)` vs `|tau|^(-1/2)`
discrepancy flagged against the Ohtsuki-Takata registration: both are `+1/2` in
the torsion, and the corpus simply works in the reciprocal variable.

AND THE CORPUS ALREADY WROTE IT DOWN WITHOUT NOTICING. `jones_1loop_c0_calibration_fig8.py`
states `exp(2 c_0) = 1 / (2 |tau_DG|)`. DGLZ (2.3) is `exp(2 S_1) = T / 2`. Under
`T = 1/|tau_DG|` these are the same equation and `c_0` IS `S_1`.

WHAT THIS DOES AND DOES NOT SETTLE.

  * DGLZ eq (2.3) is stated for a 3-manifold `M` with a flat `G_C` bundle
    `E_rho`. It is NOT restricted to knots, to two-bridge knots, or to one cusp.
    So "the prefactor form is unknown for links" was never the right description
    of the gap.
  * It is a PHYSICS derivation — one-loop saddle point / Feynman diagrams —
    citing Witten (1989), Bar-Natan-Witten (1991) and Gukov-Murakami (2006). It
    is not a rigorous theorem, and this probe does not make it one. The open
    problem is RIGOUR, not the content of the formula.
  * The identification `T = 1/|tau_DG|` is established HERE numerically, not
    read off DGLZ. Pinning it from their `Delta(m)` convention is separate work.

Nothing is fitted. Every number below is read from a committed witness.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent
                       / "substrate"))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

_UPSTREAM_RECORDS: list = []

from mpmath import mp, mpf, sqrt  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
COMP = HERE.parent
DISSOLUTION = COMP / "one-loop-c-sigma-percusp-dissolution.witness.json"
OHTSUKI = COMP / "one-loop-ohtsuki-5-2-crosscheck.witness.json"

# Which manifolds are INDEPENDENT evidence. `k = 2^(-1/2)` was calibrated on
# 4_1, so 4_1 cannot test the constant — it can only test that the calibration
# was self-consistent. 5_2 and L5a1 are independent: 5_2's c_sigma comes from
# Ohtsuki's theorem, L5a1's from a 20-digit colored-Jones measurement, and
# neither was used to fix k.
CALIBRATION_POINT = "4_1"
INDEPENDENT = ("5_2", "L5a1")


def main() -> int:
    set_compute_dps()
    dis = record_upstream(DISSOLUTION, _UPSTREAM_RECORDS)
    oht = record_upstream(OHTSUKI, _UPSTREAM_RECORDS)

    tau = {k: mpf(v) for k, v in dis["tau_dg"].items()}
    csig = {k: mpf(v) for k, v in dis["c_sigma_measured"].items()}
    tau["5_2"] = mpf(oht["tau_dg_5_2"])
    csig["5_2"] = mpf(oht["ohtsuki_abs_omega"])
    names = ["4_1", "5_2", "L5a1", "L6a4"]

    print("=" * 78)
    print(" DGLZ eq (2.3) vs the corpus's 'calibrated' prefactor")
    print("=" * 78)
    print("\n  DGLZ (2.1)/(2.3):  S_1 = (1/2) log( T / 2 )")
    print("                     => one-loop factor exp(S_1) = 2^(-1/2) T^(1/2)")
    print("  corpus:            c_sigma = k |tau_DG|^(-1/2), k = 2^(-1/2)")
    print("                     (k described as CALIBRATED on 4_1)")
    print("\n  these are the same statement iff  T = 1/|tau_DG|.  Testing:\n")

    rows = {}
    print(f"  {'manifold':8s} {'T := (c_sigma*sqrt2)^2':>26s} "
          f"{'1/|tau_DG|':>26s} {'rel diff':>11s}")
    for n in names:
        T_from_c = (csig[n] * sqrt(2)) ** 2      # invert exp(S_1) = (T/2)^(1/2)
        T_pred = 1 / tau[n]
        rel = abs(T_from_c - T_pred) / T_pred
        rows[n] = {"T_from_c_sigma": mp.nstr(T_from_c, 20),
                   "one_over_tau_DG": mp.nstr(T_pred, 20),
                   "rel_diff": mp.nstr(rel, 4),
                   "role": ("calibration point — NOT independent evidence"
                            if n == CALIBRATION_POINT else
                            "independent" if n in INDEPENDENT else
                            "supporting only (known normalisation offset)")}
        print(f"  {n:8s} {mp.nstr(T_from_c, 20):>26s} "
              f"{mp.nstr(T_pred, 20):>26s} {mp.nstr(rel, 3):>11s}")

    # The whole relation, predicted with NOTHING calibrated: c_sigma from DGLZ
    # alone is (1/(2|tau|))^(1/2). On the independent manifolds this is a
    # zero-parameter prediction.
    print("\n  DGLZ with no calibration at all:  c_sigma = ( 1/(2|tau_DG|) )^(1/2)")
    pred = {}
    for n in names:
        c_pred = sqrt(1 / (2 * tau[n]))
        rel = abs(c_pred - csig[n]) / csig[n]
        pred[n] = {"c_sigma_from_DGLZ": mp.nstr(c_pred, 20),
                   "c_sigma_measured": mp.nstr(csig[n], 20),
                   "rel_diff": mp.nstr(rel, 4)}
        print(f"     {n:6s} predicted {mp.nstr(c_pred, 18):>21s}   "
              f"measured {mp.nstr(csig[n], 18):>21s}   rel {mp.nstr(rel, 3)}")

    worst_indep = max(mpf(pred[n]["rel_diff"]) for n in INDEPENDENT)
    holds = bool(worst_indep < mpf("1e-9"))

    verdict = (
        "THE PREFACTOR FORM IS DGLZ EQ (2.3), CONSTANT INCLUDED — it was never "
        "a fit and the audits' 'validated, not proved' understates what is "
        "known. DGLZ write S_1 = (1/2) log(T/2) for the one-loop coefficient of "
        "the perturbative Chern-Simons partition function, so exp(S_1) = "
        "2^(-1/2) T^(1/2). The corpus's 'universal constant k = 2^(-1/2), "
        "calibrated on 4_1' is the /2 inside their logarithm. Reading the paper "
        "the form was already attributed to would have found it. "
        f"THE IDENTIFICATION T = 1/|tau_DG| holds to {mp.nstr(worst_indep, 3)} "
        "on the manifolds that can test it — 5_2, whose c_sigma comes from "
        "Ohtsuki's theorem, and L5a1, whose 20-digit c_sigma was measured from "
        "the colored Jones and was NOT used to fix k. 4_1 is excluded from that "
        "count: it is the calibration point and cannot be evidence for the "
        "constant it fixed. With nothing calibrated, DGLZ alone predicts "
        "c_sigma = (1/(2|tau_DG|))^(1/2), which is a zero-parameter prediction "
        "on those two. "
        "THE SIGN DISCREPANCY DISSOLVES. DGLZ carry T^(+1/2) and the corpus "
        "|tau|^(-1/2); they agree because T is the RECIPROCAL of tau_DG. The "
        "same resolves the tau^(+1/2) vs |tau|^(-1/2) mismatch flagged against "
        "the Ohtsuki-Takata registration — both are +1/2 in the torsion. "
        "AND THE CORPUS HAD ALREADY WRITTEN IT: "
        "jones_1loop_c0_calibration_fig8.py's exp(2 c_0) = 1/(2|tau_DG|) IS "
        "eq (2.3) rearranged, with c_0 = S_1 identically. "
        "WHAT REMAINS OPEN IS RIGOUR, NOT CONTENT. Eq (2.3) is a one-loop "
        "saddle-point/Feynman-diagram result citing Witten 1989, "
        "Bar-Natan-Witten 1991 and Gukov-Murakami 2006 — a physics derivation, "
        "not a theorem, and this probe does not make it one. But it is stated "
        "for a general 3-manifold M with a flat G_C bundle E_rho, with NO "
        "restriction to knots, two-bridge knots or cusp number. So 'the "
        "prefactor form is unknown for links' was the wrong description of the "
        "gap: the formula covers links, and what no theorem covers is its "
        "rigour, for links and knots alike. "
        "SCOPE: reads a paper and checks an identification against committed "
        "numbers. Proves nothing, derives nothing, and the T = 1/|tau_DG| "
        "orientation is established numerically here rather than read off "
        "DGLZ's Delta(m) convention."
        if holds else
        "THE IDENTIFICATION T = 1/|tau_DG| DOES NOT HOLD on the independent "
        "manifolds — inspect the table before citing DGLZ for this form.")
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("one-loop-dglz-prefactor-identification", engine="mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)
    wb.set_description(
        "Identifies the corpus's 1-loop prefactor form with Dimofte-Gukov-"
        "Lenells-Zagier eq (2.3) (arXiv:0903.2472, uploads/0903.2472v1.pdf), "
        "S_1 = (1/2) log(T/2), whose one-loop factor is 2^(-1/2) T^(1/2). The "
        "constant the corpus calls 'calibrated on 4_1' is the /2 inside that "
        "logarithm. Verifies T = 1/|tau_DG| against committed measurements, "
        "counting only 5_2 and L5a1 as evidence since 4_1 fixed the constant. "
        "Resolves the tau^(+1/2) vs |tau|^(-1/2) sign discrepancy: both are "
        "+1/2 in the torsion, the corpus works in the reciprocal. DGLZ's "
        "statement is for a general M with flat bundle E_rho, unrestricted by "
        "cusp number, so the open problem is the rigour of a physics "
        "derivation rather than the form being unknown for links. Nothing "
        "fitted; nothing wired.")
    wb.set_audit_only("docs/audits/2026-08-08-prefactor-form-what-is-actually-assumed.md")
    wb.add_data("dglz_source", {
        "file": "uploads/0903.2472v1.pdf",
        "arxiv": "0903.2472",
        "title": ("Exact Results for Perturbative Chern-Simons Theory with "
                  "Complex Gauge Group"),
        "authors": "Dimofte, Gukov, Lenells, Zagier",
        "eq_2_1": ("Z^(rho)(M;hbar) = exp( S_0/hbar - (1/2) delta log hbar "
                   "+ sum_{n>=0} S_{n+1} hbar^n )"),
        "eq_2_3": "S_1^(rho) = (1/2) log( T(M; E_rho) / 2 )",
        "one_loop_factor": "exp(S_1) = (T/2)^(1/2) = 2^(-1/2) T^(1/2)",
        "status": ("PHYSICS DERIVATION, not a theorem: one-loop saddle "
                   "point / Feynman diagrams, citing Witten 1989 [52], "
                   "Bar-Natan-Witten 1991 [5], Gukov-Murakami 2006 [23]"),
        "generality": ("stated for a 3-manifold M with a flat G_C bundle "
                       "E_rho — NOT restricted to knots, two-bridge knots, or "
                       "cusp number"),
        "citation_status_before_this_probe": (
            "one references.bib entry was its ONLY occurrence in the "
            "repository — no audit, probe, bean or Lean file cited it"),
    })
    wb.add_data("identification_T_equals_one_over_tau", rows)
    wb.add_data("zero_parameter_prediction_from_dglz", pred)
    wb.add_data("evidence_accounting", {
        "calibration_point": CALIBRATION_POINT,
        "why_excluded": ("k = 2^(-1/2) was fixed on 4_1, so 4_1 cannot be "
                         "evidence for it; its agreement tests only that the "
                         "calibration was self-consistent"),
        "independent": list(INDEPENDENT),
        "worst_relative_deviation_on_independent": mp.nstr(worst_indep, 4),
        "L6a4": ("supporting only — carries a documented normalisation+cusp "
                 "offset flagged in its own witness"),
    })
    wb.add_data("resolves_sign_discrepancy", (
        "docs/audits/2026-08-08-prefactor-form-what-is-actually-assumed.md "
        "flagged that the ohtsuki-takata-2015 registration says 'square root "
        "of the twisted Reidemeister torsion' (tau^(+1/2)) while the corpus "
        "uses |tau|^(-1/2). DGLZ have the same +1/2. The discrepancy is a "
        "choice of variable, not a disagreement: the corpus's tau_DG is the "
        "reciprocal of the torsion appearing in both papers."))
    wb.add_data("corpus_already_had_it", (
        "computations/probes/jones_1loop_c0_calibration_fig8.py states "
        "exp(2 c_0) = 1/(2 |tau_DG|). DGLZ (2.3) is exp(2 S_1) = T/2. Under "
        "T = 1/|tau_DG| these are the same equation, so the corpus's c_0 is "
        "DGLZ's S_1 identically — written down independently and never "
        "connected to the source."))
    wb.add_data("what_remains_open", (
        "RIGOUR, not content. Eq (2.3) is a physics one-loop result, and "
        "nothing here upgrades it. But it is stated for general M, so the "
        "repeated corpus line 'no theorem covers the link case' describes the "
        "proof status, not the formula's reach — the formula covers links "
        "already. Restating that line accordingly is a documentation fix, not "
        "a research result."))
    wb.add_data("scope", (
        "reads one paper and checks one identification against committed "
        "numbers. Derives nothing. The T = 1/|tau_DG| orientation is "
        "established numerically here, not read off DGLZ's Delta(m) "
        "convention; pinning it from their conventions is separate work."))
    wb.add_assertion(
        "T_equals_one_over_tau_on_independent_manifolds",
        computed="1" if holds else "0", expected="1", tolerance="0.5",
        source=("(c_sigma*sqrt2)^2 = 1/|tau_DG| to better than 1e-9 on 5_2 and "
                "L5a1, the two whose c_sigma did not fix the constant"))
    wb.add_assertion(
        "dglz_predicts_c_sigma_with_no_free_parameter",
        computed=mp.nstr(worst_indep, 4), expected="0", tolerance="1e-9",
        source=("c_sigma = (1/(2|tau_DG|))^(1/2) straight from eq (2.3), "
                "nothing calibrated, against the independently measured "
                "c_sigma on 5_2 and L5a1"))
    out = wb.save()
    print(f"  witness -> {out.name}")
    return 0 if holds else 1


if __name__ == "__main__":
    raise SystemExit(main())
