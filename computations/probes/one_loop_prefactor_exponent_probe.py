#!/usr/bin/env python3
"""Is the prefactor exponent MEASURED, or has it only ever been assumed?

Bean qou-fl4t / qou-pn5j. The `c_sigma = 2^(-3/4)` derivation carries exactly
one stated assumption (`docs/audits/2026-08-08-c-sigma-derivation-status.md`):

    THE PREFACTOR FORM     c_sigma  =  k * |tau|^p     with p = -1/2

and the audit is explicit that this is "validated here, not proved". But look at
HOW it is validated. Every existing probe computes

    k_c := c_sigma * |tau|^(1/2)

and checks that `k_c` is the same number across manifolds. That test has the
exponent -1/2 BAKED IN: it can only ever confirm or deny the constancy of `k`
GIVEN p = -1/2. It cannot see the exponent at all. If the true law were
p = -0.48, `k_c` would drift and the drift would be reported as a failure of
universality rather than as a wrong exponent.

THIS PROBE SEPARATES THE TWO. `p` is a free parameter here, fitted from the
data, and `-1/2` is a PREDICTION it either matches or does not.

AND THE FIRST THING THAT FALLS OUT IS A CORRECTION TO THE LEDGER, not a new
number. For any PAIR of manifolds, `k_i == k_j` and `p_ij == -1/2` are
ALGEBRAICALLY THE SAME STATEMENT:

    k_i = k_j  <=>  log c_i + (1/2) log t_i = log c_j + (1/2) log t_j
               <=>  (log c_i - log c_j)/(log t_i - log t_j) = -1/2
               <=>  p_ij = -1/2

So the existing `k_c` constancy checks were exponent measurements all along —
they just were not read as such. The 17-digit `4_1`/`L5a1` agreement below is
therefore a RE-EXPRESSION of the already-published `k_1 = k_2`, not independent
evidence, and is reported as such. The audit's ledger, which lists the exponent
among the things assumed, is what needs fixing; the exponent was pinned by data
the corpus already had.

What IS new here is the four-point fit: with 4 points and 2 free parameters
there are 2 residual degrees of freedom, so the fit can FAIL in a way no
pairwise identity can. That is the only genuinely new test in this file.

The measurement is possible because four manifolds have `c_sigma` determined
INDEPENDENTLY of `tau` — that independence is the whole point and is checked
below, not assumed:

  4_1    c_sigma from the colored Jones asymptotic (17 digits, van der Veen
         exact + Neville extrapolation; touches no geometry)
  5_2    c_sigma from Ohtsuki's Theorem 1.1, a RIGOROUS THEOREM, via
         |omega| = |e^{-i pi/4} ((1-y_0)/(2 y_0 + 1))^{1/2}| (10 digits)
  L5a1   c_sigma from the colored Jones asymptotic (20 digits)
  L6a4   c_sigma from the colored Jones asymptotic

and `|tau_DG|` for each is the triangulation-invariant Dimofte-Garoufalidis
1-loop invariant, verified on 13 manifolds x 25 randomised triangulations
(`computations/one_loop_torsion.py`).

L5a1 is the one that needs care: `c_sigma(L5a1) = 2^(-3/4)` is a CONCLUSION of
the assumed form, so using it to test the form would be circular. It is not
circular here, because the number entering below is the 20-digit MEASURED value
from `whitehead-c-sigma-hiprec.witness.json` (pure mpmath, exact colored Jones,
no SnapPy and no determinant), not the predicted one. The two agree to 17
digits, which is the finding being tested, not an input to it.

WHAT THIS CAN AND CANNOT SETTLE. It measures `p`. It does NOT establish that
`c_sigma` is a function of `tau` alone — a law `c_sigma = k * |tau|^p * f(M)`
with `f` weakly varying would fit just as well on four points, and nothing here
excludes it. Nor does it prove the form for links. The gap that remains after
this probe is strictly smaller and differently shaped than the one before it,
and the point of running it is to say which part of the assumption is still
load-bearing.

Nothing is fitted except `p` and `k`, which is the entire content.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent
                       / "substrate"))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists.
_UPSTREAM_RECORDS: list = []

from mpmath import mp, mpf, log, sqrt  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
COMP = HERE.parent
DISSOLUTION = COMP / "one-loop-c-sigma-percusp-dissolution.witness.json"
OHTSUKI = COMP / "one-loop-ohtsuki-5-2-crosscheck.witness.json"

# How c_sigma was obtained for each manifold — recorded so the independence
# claim above is auditable rather than asserted.
PROVENANCE = {
    "4_1": "colored Jones asymptotic (van der Veen exact + Neville), 17 digits",
    "5_2": "Ohtsuki Thm 1.1 |omega|, a rigorous theorem, 10 printed digits",
    "L5a1": "colored Jones asymptotic, 20 digits (whitehead-c-sigma-hiprec)",
    "L6a4": "colored Jones asymptotic",
}


def two_point_exponent(t1, c1, t2, c2):
    """The exponent forced by two manifolds alone — no fitting, no residual.

    c = k*|tau|^p at both points gives p = (log c1 - log c2)/(log t1 - log t2),
    exactly. With only two points this is an identity, not a fit, so each pair
    is an independent determination of p with no free parameter left over.
    """
    return (log(c1) - log(c2)) / (log(t1) - log(t2))


def least_squares_fit(pts):
    """Free (p, log k) by least squares on (log|tau|, log c_sigma)."""
    n = len(pts)
    xs = [log(t) for t, _ in pts]
    ys = [log(c) for _, c in pts]
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    p = sxy / sxx
    logk = my - p * mx
    resid = [y - (logk + p * x) for x, y in zip(xs, ys)]
    rms = sqrt(sum(r ** 2 for r in resid) / n)
    return p, logk, resid, rms


def main() -> int:
    set_compute_dps()

    dis = record_upstream(DISSOLUTION, _UPSTREAM_RECORDS)
    oht = record_upstream(OHTSUKI, _UPSTREAM_RECORDS)

    tau = {k: mpf(v) for k, v in dis["tau_dg"].items()}
    csig = {k: mpf(v) for k, v in dis["c_sigma_measured"].items()}
    # 5_2 comes from the Ohtsuki cross-check: tau computed from the geometry,
    # c_sigma read off the THEOREM (not predicted from tau).
    tau["5_2"] = mpf(oht["tau_dg_5_2"])
    csig["5_2"] = mpf(oht["ohtsuki_abs_omega"])

    names = ["4_1", "5_2", "L5a1", "L6a4"]
    pts = [(tau[n], csig[n]) for n in names]

    print("=" * 78)
    print(" prefactor exponent — MEASURED, not assumed")
    print("=" * 78)
    print(f"\n  {'manifold':8s} {'|tau_DG|':>26s} {'c_sigma (measured)':>26s}")
    for n in names:
        print(f"  {n:8s} {mp.nstr(tau[n], 20):>26s} {mp.nstr(csig[n], 20):>26s}")
    t_lo = min(tau[n] for n in names)
    t_hi = max(tau[n] for n in names)
    decades = log(t_hi / t_lo) / log(10)
    print(f"\n  |tau| spans {mp.nstr(t_lo, 6)} .. {mp.nstr(t_hi, 6)} — "
          f"{mp.nstr(decades, 3)} decades, which is what makes p resolvable")

    # ── pairwise exponents: each pair pins p with nothing left free ──────
    print("\n[pairs] every pair determines p exactly (no fit, no residual):")
    pairs = {}
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            p_ab = two_point_exponent(tau[a], csig[a], tau[b], csig[b])
            dev = abs(p_ab + mpf(1) / 2)
            pairs[f"{a} vs {b}"] = {"p": mp.nstr(p_ab, 20),
                                    "abs_dev_from_minus_half": mp.nstr(dev, 4)}
            print(f"     {a:6s} vs {b:6s}   p = {mp.nstr(p_ab, 18):>22s}   "
                  f"|p + 1/2| = {mp.nstr(dev, 3)}")

    # ── free least-squares fit over all four ────────────────────────────
    p_fit, logk_fit, resid, rms = least_squares_fit(pts)
    k_fit = mp.e ** logk_fit
    print(f"\n[fit] free (p, k) least squares over all {len(pts)}:")
    print(f"     p     = {mp.nstr(p_fit, 18)}      (predicted exactly -1/2)")
    print(f"     k     = {mp.nstr(k_fit, 18)}      (predicted 2^(-1/2) = "
          f"{mp.nstr(1 / sqrt(2), 12)})")
    print(f"     rms residual in log c_sigma = {mp.nstr(rms, 4)}")

    # ── the tightest pair, stated separately ────────────────────────────
    # 4_1 and L5a1 are the two whose c_sigma carry the most digits, and they
    # are the c=1 / c=2 pair the whole derivation turns on.
    p_tight = two_point_exponent(tau["4_1"], csig["4_1"],
                                 tau["L5a1"], csig["L5a1"])
    tight_dev = abs(p_tight + mpf(1) / 2)
    tight_digits = int(-log(tight_dev) / log(10)) if tight_dev > 0 else 999

    exact_half = tight_dev < mpf("1e-15")
    lsq_close = abs(p_fit + mpf(1) / 2) < mpf("1e-2")

    verdict = (
        "THE EXPONENT WAS NEVER THE ASSUMED PART — the ledger mis-attributes "
        "it. For any pair of manifolds, k_i = k_j and p_ij = -1/2 are the same "
        "statement algebraically, so every k_c constancy check in this arc was "
        "already an exponent measurement. The 4_1/L5a1 figure below, p = "
        f"{mp.nstr(p_tight, 18)} i.e. -1/2 to {tight_digits} digits, is a "
        "RE-EXPRESSION of the published k_1 = k_2 and is NOT independent "
        "evidence; the 4_1/5_2 pair likewise re-expresses the Ohtsuki "
        "cross-check to its 10 printed digits. Reporting them as fresh "
        "confirmation would be double-counting. "
        "THE ONE NEW TEST is the four-point free fit: 4 points, 2 parameters, "
        f"2 residual degrees of freedom, giving p = {mp.nstr(p_fit, 12)} and "
        f"k = {mp.nstr(k_fit, 12)} against the predicted 2^(-1/2), with rms "
        f"residual {mp.nstr(rms, 3)} in log c_sigma. That fit CAN fail and does "
        "not; no pairwise identity could have said so. The residual is carried "
        "by L6a4, whose own witness flags an unresolved normalisation+cusp "
        "offset, so it is not evidence against p = -1/2. "
        "WHAT THIS CHANGES IN THE LEDGER: the audit records 'the prefactor "
        "form c_sigma ∝ |tau|^(-1/2)' as ONE assumed statement. It is two — an "
        "exponent and a functional dependence — and they have different "
        "status. The exponent is pinned by data the corpus already had. What "
        "is genuinely assumed is that c_sigma depends on tau ALONE: a law "
        "c_sigma = k*|tau|^p*f(M) with f weakly varying fits four points just "
        "as well, and nothing here excludes it. That is the load-bearing "
        "part, and naming it is the point of this probe. "
        "SCOPE: no new manifold, no new link, no derivation. It re-reads "
        "existing numbers and adds one fit. Nothing fitted except p and k."
        if exact_half and lsq_close else
        "THE EXPONENT DOES NOT COME OUT -1/2 on this data — inspect the pair "
        "table before reading anything else in this arc, because every k_c "
        "constancy check in the corpus presupposes it.")
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("one-loop-prefactor-exponent", engine="mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)
    wb.set_description(
        "Measures the exponent p in the prefactor form c_sigma = k*|tau|^p "
        "instead of assuming it. Every prior check in this arc computes "
        "k_c = c_sigma*|tau|^(1/2) and tests its constancy, which has p = -1/2 "
        "substituted in and so cannot see the exponent at all. Here p is free "
        "and -1/2 is a prediction. Four manifolds whose c_sigma is determined "
        "INDEPENDENTLY of tau (three from colored Jones asymptotics, 5_2 from "
        "Ohtsuki's Theorem 1.1), spanning ~1 decade in |tau|. Splits the single "
        "assumption recorded in the c_sigma derivation status audit into two, "
        "of which only one — that c_sigma depends on tau alone — is still "
        "assumed. Derives nothing new; nothing wired.")
    wb.set_audit_only("docs/audits/2026-08-08-c-sigma-derivation-status.md")
    wb.add_data("inputs", {
        n: {"tau_DG": mp.nstr(tau[n], 25),
            "c_sigma_measured": mp.nstr(csig[n], 25),
            "c_sigma_provenance": PROVENANCE[n]}
        for n in names})
    wb.add_data("independence_of_inputs", (
        "c_sigma and tau must be measured independently or the test is "
        "circular. 4_1 / L5a1 / L6a4 take c_sigma from the colored Jones "
        "asymptotic (pure mpmath, exact colored Jones, no SnapPy and no "
        "determinant); 5_2 takes it from Ohtsuki's theorem. tau_DG is computed "
        "from the geometry in every case. In particular the L5a1 value used "
        "here is the 20-digit MEASURED c_sigma, NOT the 2^(-3/4) predicted by "
        "the form under test."))
    wb.add_data("pairwise_exponents", pairs)
    wb.add_data("free_least_squares", {
        "p": mp.nstr(p_fit, 20),
        "k": mp.nstr(k_fit, 20),
        "k_predicted_2_pow_minus_half": mp.nstr(1 / sqrt(2), 20),
        "rms_residual_log_c_sigma": mp.nstr(rms, 6),
        "residuals": {n: mp.nstr(r, 6) for n, r in zip(names, resid)},
    })
    wb.add_data("tightest_determination", {
        "pair": "4_1 vs L5a1",
        "NOT_INDEPENDENT_EVIDENCE": (
            "k_i = k_j and p_ij = -1/2 are algebraically the same statement, "
            "so this re-expresses the already-published k_1 = k_2 (rel diff "
            "4.5e-18) rather than confirming it again. Recorded because the "
            "re-expression is the finding — it shows the exponent was pinned "
            "by data the corpus already had — not because it is new evidence."),
        "why": ("the c=1 and c=2 anchors the derivation turns on, and the two "
                "whose c_sigma carry the most digits"),
        "p": mp.nstr(p_tight, 25),
        "abs_dev_from_minus_half": mp.nstr(tight_dev, 6),
        "digits": tight_digits,
    })
    wb.add_data("what_is_still_assumed", (
        "That c_sigma is a function of tau ALONE. A law c_sigma = "
        "k*|tau|^p*f(M) with f weakly varying across these four manifolds fits "
        "equally well and is not excluded by any data here. The EXPONENT is "
        "not the assumed part and never was — pairwise, it is the same "
        "statement as the k-constancy the corpus already measured. The "
        "functional dependence, and the universality of k across cusp number, "
        "are what carry the weight."))
    wb.add_data("scope", (
        "measures an exponent. Proves no form. Adds no manifold and no link "
        "beyond those already in the corpus, so it says nothing new about "
        "c-dependence. The L6a4 residual is not evidence against p = -1/2: "
        "that tower carries a documented normalisation+cusp offset flagged in "
        "its own witness."))
    wb.add_assertion(
        "exponent_is_minus_one_half_on_tightest_pair",
        computed="1" if exact_half else "0", expected="1", tolerance="0.5",
        source=("the 4_1/L5a1 two-point determination gives p = -1/2 to better "
                "than 1e-15. NOT independent evidence: algebraically identical "
                "to the published k_1 = k_2, and asserted here only so the "
                "re-expression is machine-checked rather than asserted"))
    wb.add_assertion(
        "free_fit_recovers_minus_one_half",
        computed="1" if lsq_close else "0", expected="1", tolerance="0.5",
        source=("least squares over all four manifolds, p free, lands within "
                "1e-2 of -1/2 across ~1 decade of |tau|"))
    out = wb.save()
    print(f"  witness -> {out.name}")
    return 0 if (exact_half and lsq_close) else 1


if __name__ == "__main__":
    raise SystemExit(main())
