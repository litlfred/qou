#!/usr/bin/env python3
"""The prefactor FORM is DGLZ eq (2.3). The CONSTANT is not — it is convention.

Beans qou-fl4t / qou-pn5j. `docs/audits/2026-08-08-c-sigma-derivation-status.md`
records, as the single assumption the `c_sigma = 2^(-3/4)` derivation carries:

    c_sigma  ∝  |tau|^(-1/2)      "validated here, not proved"

with the universal constant `k = 2^(-1/2)` described as CALIBRATED on `4_1`, and
`docs/audits/2026-08-08-prefactor-form-what-is-actually-assumed.md` narrowing the
open part to "whether c_sigma depends on tau ALONE".

Both are answered by a paper that has been sitting in `library/` uncited.

WHAT DGLZ SAY. Dimofte-Gukov-Lenells-Zagier, "Exact Results for Perturbative
Chern-Simons Theory with Complex Gauge Group" (arXiv:0903.2472,
`library/arxiv-0903.2472v1/0903.2472v1.pdf`), write the perturbative partition function as

    Z^(rho)(M; hbar) = exp( S_0/hbar - (1/2) delta log hbar
                            + sum_{n>=0} S_{n+1} hbar^n )        (2.1)

and identify the one-loop coefficient with the Ray-Singer torsion of `M` twisted
by the flat bundle `E_rho`:

    S_1^(rho) = (1/2) log( T(M; E_rho) / 2 )                     (2.3)

so the one-loop factor in `Z` is

    exp(S_1) = ( T / 2 )^(1/2) = 2^(-1/2) * T^(1/2).

THE `/2` IS *NOT* THE CORPUS'S `k`, AND SAYING SO WAS WRONG. An earlier version
of this probe claimed the corpus's "universal constant k = 2^(-1/2), calibrated
on 4_1" simply IS the `/2` inside DGLZ's logarithm, and therefore was never a
fit. That does not survive reading further. DGLZ carry at least three distinct
additive offsets between conventions:

    eq (2.3)     S_1 = (1/2) log( T / 2 )                      a  /2
    eq (4.5)     S_1(0) = s_1 + log 2                          a  +log 2
    footnote 24  S_1 matches Gukov-Murakami "up to a shift by log pi"

and they say plainly that the integration constants of the S_n "have been fixed
by comparison to the asymptotics of the colored Jones polynomial" — the S_n are
determined by their hierarchy of differential equations only UP TO an additive
constant. So DGLZ calibrate too.

Worse for the old claim: the corpus measures c_sigma from the colored-Jones
asymptotic (DGLZ eq 4.4), which corresponds to `s_1`, not to `S_1`, and those
differ by exactly the `log 2` of eq (4.5). Carry that through and the very
identification below moves:

    identify c_sigma = exp(S_1)   ->   T = 1/|tau_DG|
    identify c_sigma = exp(s_1)   ->   T = 4/|tau_DG|

Same data, same paper, a factor of 4 in T depending on which normalisation you
match. What is NOT touched by any of it is the EXPONENT: a multiplicative
constant cannot change -1/2. That asymmetry is the whole result here.

THE `+1/2` vs `-1/2` SIGN *IS* A VARIABLE CHOICE, AND THAT PART SURVIVES. DGLZ
carry `T^(+1/2)` where the corpus carries `|tau_DG|^(-1/2)`; they agree when `T`
is the reciprocal of `tau_DG`. Since an exponent is invariant under the
normalisation offsets above, this conclusion is robust to them — unlike the
constant. It disposes of the `tau^(+1/2)` vs `|tau|^(-1/2)` discrepancy flagged
against the Ohtsuki-Takata registration: both are `+1/2` in the torsion, and the
corpus works in the reciprocal variable.

THE CORPUS DID INDEPENDENTLY WRITE DOWN SOMETHING OF THE SAME SHAPE.
`jones_1loop_c0_calibration_fig8.py` states `exp(2 c_0) = 1/(2 |tau_DG|)`, and
DGLZ (2.3) is `exp(2 S_1) = T/2`. Under ONE of the two convention choices these
coincide with `c_0 = S_1`; under the other they differ by the eq (4.5) `log 2`.
Worth recording as a structural echo, NOT as evidence that the corpus's constant
came from the literature.

WHAT THIS DOES AND DOES NOT SETTLE.

  * DGLZ eq (2.3) is stated for a 3-manifold `M` with a flat `G_C` bundle
    `E_rho`. It is NOT restricted to knots, to two-bridge knots, or to one cusp.
    So "the prefactor form is unknown for links" was never the right description
    of the gap — for the FORM. This is the part that transfers, because it is
    the exponent that transfers.
  * The CONSTANT does not transfer and is not derived here or there. The
    corpus's calibration on 4_1 is NOT made redundant by DGLZ; if anything the
    two calibrations are the same one done twice, since DGLZ fix theirs against
    colored-Jones asymptotics as well. Treating `2^(-1/2)` as a universal
    physical constant lifted from eq (2.3) is exactly the error this file used
    to make.
  * That `k` comes out the SAME at c = 1 and c = 2 (the corpus's k_1 = k_2 to
    17 digits) is an EMPIRICAL finding of this corpus. It is not read off DGLZ,
    and nothing in DGLZ says the constant is cusp-independent. Ray-Singer
    torsion on a cusped manifold needs a choice of basis in H^1, whose rank is
    the cusp number, so cusp-dependence of the normalisation is precisely where
    one would expect trouble — and it is where the retracted 2^((c-1)/2)
    per-cusp factor lived.
  * It is a PHYSICS derivation — one-loop saddle point / Feynman diagrams —
    citing Witten (1989), Bar-Natan-Witten (1991) and Gukov-Murakami (2006). It
    is not a rigorous theorem, and this probe does not make it one. The open
    problem is RIGOUR, not the content of the formula.
  * The identification `T = 1/|tau_DG|` is established HERE numerically, under
    the `c_sigma = exp(S_1)` reading, and is NOT read off DGLZ. Under the
    `c_sigma = exp(s_1)` reading it is `T = 4/|tau_DG|`. Pinning which is
    correct requires their `Delta(m)` and `hbar` conventions and is separate
    work; the table below therefore reports a CONSISTENCY relation, not a
    determination of `T`.

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
    print("\n  under the c_sigma = exp(S_1) reading these coincide iff")
    print("  T = 1/|tau_DG| (under c_sigma = exp(s_1) it is 4/|tau_DG| —")
    print("  DGLZ eq (4.5) puts a log 2 between S_1 and s_1). Testing the first:\n")

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

    # The same relation written forwards. NOT a zero-parameter prediction: the
    # constant inside it is a normalisation choice (see the /2, +log 2 and
    # log pi offsets above), so what this tests is that ONE constant serves
    # both cusp numbers — not that the constant came from DGLZ.
    print("\n  the relation forwards:  c_sigma = ( 1/(2|tau_DG|) )^(1/2)")
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
        "THE FORM IS DGLZ EQ (2.3); THE CONSTANT IS CONVENTION, AND CLAIMING "
        "OTHERWISE WAS AN OVERREACH THIS FILE PREVIOUSLY MADE. DGLZ write "
        "S_1 = (1/2) log(T/2), so exp(S_1) = 2^(-1/2) T^(1/2), and the "
        "dependence c_sigma ~ (torsion)^(-1/2) is theirs, for a general M. But "
        "the /2 is not the corpus's k. DGLZ carry a /2 in (2.3), a +log 2 in "
        "(4.5) relating S_1 to the colored-Jones coefficient s_1, and a log pi "
        "shift against Gukov-Murakami (fn 24); their S_n are fixed only up to "
        "an additive integration constant, set 'by comparison to the "
        "asymptotics of the colored Jones polynomial'. Since the corpus's "
        "c_sigma is measured from that same colored-Jones asymptotic, it "
        "corresponds to s_1 rather than S_1, and carrying the eq (4.5) log 2 "
        "through moves the identification from T = 1/|tau_DG| to "
        "T = 4/|tau_DG|. A factor of 4 in T, from one convention choice. "
        f"THE IDENTIFICATION T = 1/|tau_DG| holds to {mp.nstr(worst_indep, 3)} "
        "on the manifolds that can test it — 5_2, whose c_sigma comes from "
        "Ohtsuki's theorem, and L5a1, whose 20-digit c_sigma was measured from "
        "the colored Jones and was NOT used to fix k. 4_1 is excluded from that "
        "count: it is the calibration point and cannot be evidence for the "
        "constant it fixed. Read correctly, that agreement says ONE constant "
        "works at both cusp numbers — not that the constant was derived. "
        "WHAT IS UNTOUCHED BY ALL OF THAT IS THE EXPONENT. No multiplicative "
        "constant changes -1/2, so the SHAPE c_sigma ~ |tau|^(-1/2) transfers "
        "across every one of these conventions while the prefactor does not. "
        "That also settles the tau^(+1/2) vs |tau|^(-1/2) mismatch flagged "
        "against the Ohtsuki-Takata registration: both are +1/2 in the "
        "torsion and the corpus works in the reciprocal, which is a variable "
        "choice, not a disagreement. "
        "The corpus's own exp(2 c_0) = 1/(2|tau_DG|) "
        "(jones_1loop_c0_calibration_fig8.py) coincides with eq (2.3) under one "
        "convention reading and differs by the eq (4.5) log 2 under the other — "
        "a structural echo, not provenance for the constant. "
        "SO THE CORPUS'S CALIBRATION STANDS AND IS NOT REDUNDANT. k = 2^(-1/2) "
        "still has to be fixed against data; DGLZ fix theirs the same way. And "
        "that k is the SAME at c = 1 and c = 2 remains an empirical result of "
        "this corpus, not something read off DGLZ — nothing there asserts "
        "cusp-independence, and the Ray-Singer torsion of a cusped manifold "
        "needs a basis of H^1 whose rank IS the cusp number. "
        "WHAT REMAINS OPEN IS RIGOUR, NOT CONTENT — for the form. Eq (2.3) is a one-loop "
        "saddle-point/Feynman-diagram result citing Witten 1989, "
        "Bar-Natan-Witten 1991 and Gukov-Murakami 2006 — a physics derivation, "
        "not a theorem, and this probe does not make it one. But it is stated "
        "for a general 3-manifold M with a flat G_C bundle E_rho, with NO "
        "restriction to knots, two-bridge knots or cusp number. So 'the "
        "prefactor form is unknown for links' was the wrong description of the "
        "gap: the formula covers links, and what no theorem covers is its "
        "rigour, for links and knots alike. That statement is about the "
        "exponent. The normalisation for c >= 2 is a separate and still-open "
        "question, and it is the one with a track record of biting here. "
        "SCOPE: reads a paper and checks one identification against committed "
        "numbers. Proves nothing, derives nothing, and does NOT supply the "
        "constant. The T = 1/|tau_DG| orientation is a numerical statement "
        "under one convention choice, not read off DGLZ's Delta(m) "
        "convention, and it becomes T = 4/|tau_DG| under the other."
        if holds else
        "THE IDENTIFICATION T = 1/|tau_DG| DOES NOT HOLD on the independent "
        "manifolds — inspect the table before citing DGLZ for this form.")
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("one-loop-dglz-prefactor-identification", engine="mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)
    wb.set_description(
        "Identifies the SHAPE of the corpus's 1-loop prefactor with Dimofte-"
        "Gukov-Lenells-Zagier eq (2.3) (arXiv:0903.2472, "
        "library/arxiv-0903.2472v1/0903.2472v1.pdf), S_1 = (1/2) log(T/2). The dependence "
        "c_sigma ~ (torsion)^(-1/2) is theirs and holds for a general M with a "
        "flat G_C bundle, unrestricted by cusp number. The CONSTANT is NOT: "
        "DGLZ carry a /2 in (2.3), a +log 2 in (4.5) between S_1 and the "
        "colored-Jones coefficient s_1, and a log pi shift against "
        "Gukov-Murakami, and fix their integration constants against "
        "colored-Jones asymptotics — so they calibrate too, and the corpus's "
        "k = 2^(-1/2) is not made redundant. Since the corpus measures c_sigma "
        "from the colored-Jones asymptotic it corresponds to s_1, under which "
        "the identification is T = 4/|tau_DG| rather than 1/|tau_DG|. The "
        "exponent is invariant under all of this; the prefactor is not. "
        "Corrects an earlier version of this probe that claimed the constant "
        "was never a fit. Nothing fitted; nothing wired.")
    wb.set_audit_only("docs/audits/2026-08-08-prefactor-form-what-is-actually-assumed.md")
    wb.add_data("dglz_source", {
        "file": "library/arxiv-0903.2472v1/0903.2472v1.pdf",
        "arxiv": "0903.2472",
        "title": ("Exact Results for Perturbative Chern-Simons Theory with "
                  "Complex Gauge Group"),
        "authors": "Dimofte, Gukov, Lenells, Zagier",
        "eq_2_1": ("Z^(rho)(M;hbar) = exp( S_0/hbar - (1/2) delta log hbar "
                   "+ sum_{n>=0} S_{n+1} hbar^n )"),
        "eq_2_3": "S_1^(rho) = (1/2) log( T(M; E_rho) / 2 )",
        "one_loop_factor": "exp(S_1) = (T/2)^(1/2) = 2^(-1/2) T^(1/2)",
        "eq_4_5": "S_1(0) = s_1 + log 2  — s_1 is the COLORED-JONES coefficient",
        "footnote_24": ("their S_1 matches Gukov-Murakami 'up to a shift by "
                        "log pi'"),
        "integration_constants": ("the S_n are determined by the hierarchy of "
                                  "differential equations only up to an "
                                  "additive constant, 'fixed by comparison to "
                                  "the asymptotics of the colored Jones "
                                  "polynomial' — DGLZ calibrate too"),
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
    wb.add_data("consistency_relation_under_exp_S1_reading", rows)
    wb.add_data("the_constant_is_convention_not_physics", {
        "offsets_in_dglz": ["/2 in eq (2.3)",
                            "+log 2 in eq (4.5) between S_1 and s_1",
                            "log pi vs Gukov-Murakami (footnote 24)"],
        "corpus_measures": ("c_sigma from the colored-Jones asymptotic, i.e. "
                            "the s_1 normalisation, not S_1"),
        "T_under_exp_S1": "1/|tau_DG|",
        "T_under_exp_s1": "4/|tau_DG|",
        "consequence": ("a factor of 4 in T from one convention choice, so the "
                        "'/2' cannot be lifted as the corpus's k. The earlier "
                        "claim in this probe that k 'was never a fit' is "
                        "RETRACTED. The corpus's calibration on 4_1 stands and "
                        "is not redundant."),
        "what_is_invariant": ("the exponent. No multiplicative constant changes "
                              "-1/2, which is why the FORM transfers across all "
                              "of these conventions and the prefactor does not"),
        "cusp_independence_is_empirical": (
            "that k is the same at c=1 and c=2 (k_1 = k_2 to 17 digits) is this "
            "corpus's own measurement. DGLZ assert nothing about "
            "cusp-independence, and Ray-Singer torsion on a cusped manifold "
            "requires a basis of H^1 whose rank is the cusp number — the exact "
            "place the retracted 2^((c-1)/2) per-cusp factor lived"),
    })
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
    wb.add_data("structural_echo_not_provenance", (
        "computations/probes/jones_1loop_c0_calibration_fig8.py states "
        "exp(2 c_0) = 1/(2 |tau_DG|); DGLZ (2.3) is exp(2 S_1) = T/2. Under one "
        "of the two convention choices these coincide with c_0 = S_1; under the "
        "other they differ by the eq (4.5) log 2. Recorded as a structural "
        "echo, NOT as evidence that the corpus's constant came from the "
        "literature."))
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
        "consistency_relation_holds_on_independent_manifolds",
        computed="1" if holds else "0", expected="1", tolerance="0.5",
        source=("(c_sigma*sqrt2)^2 = 1/|tau_DG| to better than 1e-9 on 5_2 and "
                "L5a1. This is a CONSISTENCY relation under the exp(S_1) "
                "reading, not a determination of T — under exp(s_1) the same "
                "data give 4/|tau_DG|"))
    wb.add_assertion(
        "one_constant_works_at_both_cusp_numbers",
        computed=mp.nstr(worst_indep, 4), expected="0", tolerance="1e-9",
        source=("whatever the normalisation, a SINGLE constant reproduces the "
                "independently measured c_sigma at c=1 (5_2) and c=2 (L5a1). "
                "That cusp-independence is this corpus's empirical result; "
                "DGLZ assert nothing about it"))
    out = wb.save()
    print(f"  witness -> {out.name}")
    return 0 if holds else 1


if __name__ == "__main__":
    raise SystemExit(main())
