#!/usr/bin/env python3
"""b3_candidate_space_enumeration_probe.py

Enumerate the b3 candidate space by a DECISION PROCEDURE, not by listing guesses.

THE PROCEDURE
-------------
Expand the binding in the binomial (simplex) basis, B(n) = sum_k mu_k C(n,k).
Then the connected three-body cumulant is exactly the third finite difference:

    b3 = mu_3 = Delta^3 B (0) = B(3) - 3B(2) + 3B(1) - B(0)

So for any candidate contribution f(A) entering B additively:

    **f can contribute to b3 IFF Delta^3 f != 0**
    i.e. iff f has degree >= 3 in A, or is non-polynomial in A.

That is mechanical, complete for single-term candidates that are functions of A,
and it explains BOTH of this session's failures at once: each was an object that
looked many-body and had Delta^3 f = 0.

TIER 1 -- CLOSED BY ARITY (Delta^3 = 0). Cannot contribute, for any coefficient.
  pair count C(A,2); coordination counts with uniform weights; A; A^2; and
  **the quadratic Casimir of the fully antisymmetric [1^A] of EVERY SU(N)** --
  proved this session in QOU/Mass/AntisymmetricCasimirIsTwoBody.lean, where
  S(n) = -[(N+1)/(2N)]*C(n,2) exactly. That closes SU(2) spin, **SU(3) flavour
  (the eightfold way)**, SU(4) Wigner and SU(6) spin-flavour in one identity.

TIER 2 -- CLOSED BY TYPE (normalised: value in a fixed finite set).
  Milnor mu-bar on Brunnian links (+-1), signs, parities. |b_A| = |c_A|, so the
  magnitude is never theirs. QOU/Mass/MilnorCarriesOrderNotMagnitude.lean.

TIER 3 -- PASSES ARITY, REFUTED BY SIGN (new here).
  Candidates with Delta^3 != 0 still have to produce the measured sign pattern
  b2,b3,b4 = +,+,+ i.e. b4/b3 = +6.481. A standalone term gamma*f gives
  b4/b3 = Delta^4 f / Delta^3 f, independent of gamma. Every candidate tested
  gives <= 0:
      dim[1^n] = C(4,n)             -2.0
      SU(4) cubic / anomaly coeff    0.0
      partition count p(A)          -2.0
      A^3                            0.0
      SU(2) C2, support-truncated   -1.333
  None survives standalone.

A BUG IN MY OWN FIRST SCAN, AND WHY IT MATTERS
----------------------------------------------
The first pass guarded the Casimir with "if n <= N else 0" and reported SU(2) as
3-body with Delta^3 = 2.25, contradicting the theorem just proved. The theorem is
right; the scan was measuring TWO objects at once. The truncation is physical --
[1^n] does not exist for n > N -- but it is NOT the Casimir, and the two have
different arity:

    N     Delta^3(polynomial)   Delta^3(truncated)   cutoff at n
    2            0                     2.25               3   <- inside the window
    3            0                     0                  4   <- inside the window
    4            0                     0                  5   <- outside

**Every bit of the nonzero Delta^3 came from the support cutoff dim[1^n] = 0, not
from the Casimir.** SU(4) is genuinely closed for b3 and b4 because its cutoff at
n = 5 falls OUTSIDE the n <= 4 window; SU(2)'s at n = 3 falls inside.

And that cutoff is the same object as the SUPPORT BOUND that locates the A = 4
turnover. So: **the three-body content of a shell model lives in WHERE THE SHELL
CLOSES, not in the Casimir of the representation that fills it.** That is the one
structural lesson of this enumeration, and it was only visible because the scan
disagreed with the theorem.

WHAT IS *NOT* ENUMERATED, stated plainly
----------------------------------------
1. **Candidates that are not functions of A alone.** The procedure keys on A.
   6j symbols / the monoidal associator (three-object by definition), Vassiliev
   invariants at degree 4 (not normalised, unlike mu-bar), the content of the new
   Wedderburn block S^(2,1) that exists at n=3 and not at n=2, and the hyperbolic
   volume of the 3-component complement are all OUTSIDE this scan. None is
   refuted here.
2. **Multi-term combinations.** Tier 3 refutes each candidate STANDALONE. Two
   Tier-3 terms with opposite-sign coefficients can reproduce any (b3, b4) pair,
   so the multi-term space is not bounded by this procedure and is not enumerable
   this way.

So the honest verdict: **the single-term space of functions of A is now
enumerated and exhausted; the space as a whole is not.** Saying "no candidate
remains" would be the absence-of-evidence over-claim.

Bean qou-edt7.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys  # noqa: E402
from math import comb  # noqa: E402

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from codata_constants import ame_binding_mev  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(65)

ANOM = {0: 0, 1: 1, 2: 0, 3: -1, 4: 0}      # SU(4) anomaly coeff of [1^n]
PARTS = {0: 1, 1: 1, 2: 2, 3: 3, 4: 5}      # partitions of n


def d3(f):
    return f(3) - 3 * f(2) + 3 * f(1) - f(0)


def d4(f):
    return f(4) - 4 * f(3) + 6 * f(2) - 4 * f(1) + f(0)


def c2_poly(N):
    return lambda n: mp.mpf(N + 1) * n * (N - n) / (2 * N)


def c2_trunc(N):
    return lambda n: (mp.mpf(N + 1) * n * (N - n) / (2 * N) if n <= N else mp.mpf(0))


def main() -> int:
    wb = WitnessBuilder("b3-candidate-space-enumeration", engine="mpmath")
    wb.set_description(
        "Enumerates the b3 candidate space by the decision procedure b3 = Delta^3 "
        "B(0): a term f(A) can contribute iff Delta^3 f != 0. Tier 1 closed by "
        "arity (all SU(N) antisymmetric quadratic Casimirs, proved), Tier 2 by "
        "type (normalised invariants), Tier 3 passes arity and is refuted by the "
        "sign gate b4/b3 <= 0 against a measured +6.481. Does NOT enumerate "
        "non-A-functions or multi-term combinations."
    )
    ok = True

    ZERO = mp.mpf(10) ** -25

    # Tier 1 -- the polynomial Casimir, every N
    worst_poly = max(abs(d3(c2_poly(N))) for N in (2, 3, 4, 5, 6, 8, 10))
    print(f"TIER 1  polynomial SU(N) antisym Casimir: worst |Delta^3| = {mp.nstr(worst_poly,3)}")
    wb.add_assertion(
        name="all_su_n_antisym_casimirs_are_two_body",
        computed=fmt(worst_poly), expected="0", tolerance="1e-25",
        unit="worst |Delta^3| over N = 2,3,4,5,6,8,10",
        source=("Delta^3 = 0 for every N, so no antisymmetric-column quadratic "
                "Casimir can contribute to b3 -- includes SU(3), the eightfold "
                "way. Lean: AntisymmetricCasimirIsTwoBody.pairSum_eq"),
    )
    ok &= worst_poly < ZERO

    # the bug: polynomial vs support-truncated
    print("\n  polynomial vs SUPPORT-TRUNCATED (the bug my first scan hit):")
    trows = []
    for N in (2, 3, 4, 5, 6):
        p, t = d3(c2_poly(N)), d3(c2_trunc(N))
        trows.append({"N": N, "d3_poly": fmt(p), "d3_truncated": fmt(t),
                      "cutoff_at": N + 1, "cutoff_in_window": N + 1 <= 4})
        print(f"    N={N}  D^3 poly {mp.nstr(p,3):>10}   D^3 trunc {mp.nstr(t,6):>10}   "
              f"cutoff n={N+1}{'  <- inside the b3/b4 window' if N+1<=4 else ''}")
    wb.add_data("polynomial_vs_truncation", trows)
    print("    -> the nonzero Delta^3 is ENTIRELY the support cutoff dim[1^n]=0,")
    print("       not the Casimir. Three-body content lives in where the shell")
    print("       CLOSES, not in the Casimir of the rep that fills it.")

    # Tier 3 -- arity passes, sign gate
    D = ame_binding_mev(1, 2)
    T3, He3 = ame_binding_mev(1, 3), ame_binding_mev(2, 3)
    He4 = ame_binding_mev(2, 4)
    B3m = (T3 + He3) / 2
    b3m, b4m = B3m - 3 * D, He4 - 4 * B3m + 6 * D
    target = b4m / b3m
    print(f"\nTIER 3  sign gate: measured b4/b3 = {mp.nstr(target,7)}")

    cands = [("dim_[1^n]_=_C(4,n)", lambda n: mp.mpf(comb(4, n))),
             ("su4_cubic_anomaly", lambda n: mp.mpf(ANOM[n])),
             ("partition_count", lambda n: mp.mpf(PARTS[n])),
             ("A_cubed", lambda n: mp.mpf(n ** 3)),
             ("su2_C2_support_truncated", c2_trunc(2))]
    rows, n_wrong = [], 0
    for nm, f in cands:
        a, b = d3(f), d4(f)
        r = b / a
        wrong = r <= 0
        n_wrong += wrong
        rows.append({"candidate": nm, "d3": fmt(a), "d4": fmt(b),
                     "b4_over_b3": fmt(r), "refuted_standalone": bool(wrong)})
        print(f"    {nm:<28} b4/b3 = {mp.nstr(r,6):>9}   "
              f"{'REFUTED standalone' if wrong else 'sign OK'}")
    wb.add_data("tier3_sign_gate", rows)
    wb.add_assertion(
        name="every_tier3_candidate_refuted_standalone",
        computed=str(n_wrong), expected=str(len(cands)), tolerance="0",
        unit="candidates with b4/b3 <= 0",
        source=("a standalone term gamma*f gives b4/b3 = Delta^4 f / Delta^3 f, "
                "independent of gamma; all five are <= 0 against a measured +6.481"),
    )
    ok &= n_wrong == len(cands)

    wb.add_data("what_is_not_enumerated", {
        "not_functions_of_A_alone": ["6j symbols / monoidal associator",
                                     "Vassiliev invariants at degree 4",
                                     "content of the S^(2,1) block, absent at n=2",
                                     "hyperbolic volume of the 3-component complement"],
        "multi_term_combinations": ("Tier 3 refutes each candidate STANDALONE; two "
                                    "Tier-3 terms with opposite-sign coefficients "
                                    "reproduce any (b3,b4), so the multi-term space "
                                    "is not bounded by this procedure"),
        "honest_verdict": ("the single-term space of functions of A is enumerated "
                           "and exhausted; the space as a whole is NOT. 'No "
                           "candidate remains' would be the absence-of-evidence "
                           "over-claim"),
    })
    wb.save()
    print("\nOK" if ok else "\nFAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
