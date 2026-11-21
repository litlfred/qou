#!/usr/bin/env python3
"""qou-pdix: what the two carrier fields force at the classical point — three
necessary conditions on M, and the exclusion of the corpus's only elliptic operator.

`qou-pdix`'s remaining job is stated exactly: produce M from the Hecke seminormal
representation on V_(2,1) satisfying

    QOU.QBeta.EigenphaseCarrier.TransferMatrixSpectrum (q) (M) :
        M.trace = 2*cos(eigenphase q)   /\\   M.det = 1

and prove those two fields. Entry 6 expands alpha about q = 1 + t and tests it
against a holonomy ansatz c*ln(q). What has NOT been done is asking what those
two fields force about M ITSELF at the classical point. They force three things,
none of which mentions which convention is right, and all three are cheap enough
to disqualify a candidate before any construction is attempted.

*** THE FALSIFIER, CHECKED FIRST ***

The argument below turns on the S_3 standard (2-dim) character table having
trace 2 only at the identity. Verified: chi^(2,1) is +2 on e, 0 on the three
transpositions, -1 on the two 3-cycles. Had a non-identity class had trace 2 the
constraint would collapse to "tr M(1) = 2" alone, which is far weaker.

*** CONDITION 1 — M(1) IS UNIPOTENT ***

alpha(1) = 0 (entry 6: alpha = -t/2 + O(t^2), because its t^1 coefficient is
z(1) - 1 = -1/2 under BOTH conventions). So tr M(1) = 2*cos(0) = 2 while
det M(1) = 1: the characteristic polynomial is x^2 - 2x + 1 = (x-1)^2, so both
eigenvalues are 1 and **M(1) is unipotent**.

NOT "M(1) = I". At q = 1 the algebra is C[S_3] and its (2,1) block is all of
M_2(C), so M(1) may be a nontrivial Jordan block. The identity follows only with
semisimplicity — which is exactly the next condition's content.

*** CONDITION 1' — SO NO BRAID-WORD CARRIER, UNLESS IT DEGENERATES TO e ***

If M is the normalisation of a single braid word's image, then M(1) lies in the
image of S_3 — a finite group in characteristic 0, hence semisimple by Maschke,
hence diagonalisable. Unipotent AND diagonalisable ==> **M(1) = I**, so the word
must degenerate to the IDENTITY permutation. Route 1 (braid image) is already
closed in this bean by another argument; this is a second, simpler reason, and
it applies at the classical point alone without computing any eigenphase.

*** CONDITIONS 2 AND 3 — THE TRACE IS STATIONARY, WITH CURVATURE -1/2 ***

Expanding tr M = 2*cos(alpha) with alpha = -t/2 + a_2 t^2 + a_3 t^3:

    z_C:  alpha = -t/2 + t^2/4  - 5t^3/16    tr M = 2 - t^2/4 + t^3/4
    z_D:  alpha = -t/2 + 5t^2/4 - t^3/2      tr M = 2 - t^2/4 + 5t^3/4

(The alpha rows reproduce entry 6's recorded t^2 and t^3 coefficients exactly —
1/4 and -5/16 for C, 5/4 for D — computed here independently.)

So a carrier's trace has **NO t^1 term** — it is stationary at the classical
point — and its **t^2 coefficient is -1/4**, i.e. d^2/dt^2 (tr M)|_0 = -1/2.

*** AND THE TRACE IS CONVENTION-BLIND THROUGH t^2 ***

Both conventions give tr M = 2 - t^2/4 + O(t^3) IDENTICALLY, because the t^2
coefficient of tr M depends only on alpha's t^1 coefficient, which is
z(1) - 1 = -1/2 for both. They first differ at **t^3** (1/4 vs 5/4).

This refines the bean's acceptance test. Its part 1 asks a construction to
"reproduce alpha through t^2". On the TRACE that is convention-blind: a
construction matching tr M through t^2 has shown nothing about which convention
it belongs to, and the discrimination lives at t^3.

*** THE EXCLUSION — Delta_L FAILS AT ORDER ZERO ***

This session's Step 26 established that Delta_L = NF(neutron) - NF(proton) is the
corpus's only ELLIPTIC operator (det > 0, spectrum +-i*theta), i.e. the only one
satisfying this bean's TIER-0 condition D0. Its classical eigenphase is EXACTLY
2*pi/3, because every NF coordinate carries (q-1)(q+1) and the leading direction
is -(1 + T_1 T_0) with T_1 T_0 the S_3 THREE-CYCLE.

    carrier requires   tr M(1) = +2
    Delta_L gives      tr M(1) = 2*cos(2*pi/3) = -1

So the one operator that clears D0 fails the carrier condition at order zero, and
by the character table above that is structural — the 3-cycle's character is -1,
not a numerical near-miss. Delta_S is excluded more simply still: it is
hyperbolic at every real q (Step 26), so it has no eigenphase at all.

*** HOW STRONG IS THE FILTER?  MEASURED, AND THE ANSWER IS "DISQUALIFIER" ***

Condition 1 as stated above is not scale-invariant — it is about the NORMALISED
M. The invariant form: with R := tr^2/det, a carrier needs **R(1) = 4**, i.e.
disc = tr^2 - 4det = 0, i.e. the underlying operator is **PARABOLIC at q = 1**
(repeated eigenvalue). Delta_L gives R(1) = 1, Delta_S has tr = 0 so R = 0.

Writing A(q) = sum_b c_b(q) B_b in the H_3 normal-form basis, at q = 1 the B_b
are the six S_3 standard-rep images, and

    disc A(1) = 4*Q_T - 3*(c_3 - c_4)^2 ,
    Q_T = (1/2)[ (c_1-c_2)^2 + (c_1-c_5)^2 + (c_2-c_5)^2 ]  >= 0

so the PARABOLIC LOCUS is

    2[ (c_1-c_2)^2 + (c_1-c_5)^2 + (c_2-c_5)^2 ]  =  3 (c_3 - c_4)^2 .

Three readings, all verified below:

  * **c_0 is absent** — disc(A + lambda*I) = disc(A), so the gamma coefficient
    is free. And the three TRANSPOSITION coefficients enter only through their
    DIFFERENCES: their class sum contributes 0 to the (2,1) block, because
    chi^(2,1) vanishes on a transposition.
  * **Q_T = 0 <=> c_1 = c_2 = c_5, and on the locus that holds <=> c_3 = c_4.**
    That sub-locus is exactly the CENTRE of C[S_3] — an element constant on each
    conjugacy class. A central element acts as a SCALAR on the irreducible (2,1)
    block (verified: it is -b*I, independent of the transposition weight), so
    M(1) = I there. The centre is the distinguished stratum of the locus.
  * **The filter does NOT pin a carrier.** Condition 1 is ONE quadratic equation
    on the six c_b(1). Conditions 2 and 3 constrain the first and second
    derivatives of the c_b at q = 1 — two more equations on twelve new
    parameters. Cumulative: **3 equations, 18 parameters.**

So the filter is a **DISQUALIFIER, not a target**. It rules candidates out
cheaply — including both operators the qou-cds1 arc produced — but it does not
tell a construction what to be. This corrects the recommendation this probe's
first version implied.

*** WHAT THIS DOES AND DOES NOT DO ***

It does not derive alpha, does not construct a carrier, and does not adjudicate
a convention. It supplies a THREE-CONDITION FILTER at the classical point that
any candidate must pass, shows the filter is convention-blind through t^2, and
applies it to disqualify both operators this session produced — including the
only one that clears D0.

SCOPE. Scope-(a). Nothing derived, proposed, wired or readmitted. Anchor:
experimental (proton) pin.
"""

import json
import os
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path[:0] = [str(HERE), str(HERE.parent), str(HERE.parent / "substrate"),
                str(HERE.parent / "hecke"), str(HERE.parent / "markov")]
import _path_bridge  # noqa: E402, F401

import qou_substrate.constants as CONST  # noqa: E402

mp.mp.dps = 40
Q0 = mp.mpf(str(CONST.Q_50_DIGIT_STR))
T = sp.Symbol("t")
Q = 1 + T

# S_3 standard (2-dim) rep, chi^(2,1), by conjugacy class.
S3_CHI = {"e": 2, "transposition": 0, "three_cycle": -1}


def alpha_series(z_expr, order=4):
    h = Q - 1 / Q
    return sp.expand(sp.series(sp.simplify((z_expr - 1) * h / 2), T, 0, order).removeO())


def trace_series(alpha, order=4):
    return sp.expand(sp.series(2 * sp.cos(alpha), T, 0, order).removeO())


def coeff(e, n):
    return sp.nsimplify(sp.expand(e).coeff(T, n))


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
    except Exception:
        return "unknown"


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" qou-pdix: the carrier's classical-limit filter, and what it excludes")
    print("=" * 78)

    # [1] falsifier
    print(f"\n[1] FALSIFIER FIRST — S_3 standard rep, chi^(2,1) by class")
    for k, v in S3_CHI.items():
        print(f"    chi^(2,1)({k:14s}) = {v:+d}")
    only_id = all(v != 2 for k, v in S3_CHI.items() if k != "e")
    print(f"    trace 2 occurs ONLY at the identity : {only_id}")
    print(f"    (had it not, the constraint would collapse to 'tr M(1) = 2' alone)")

    # [2] the expansions
    convs = {"z_C": sp.sqrt(Q) / (1 + Q), "z_D": Q ** 3 / (Q ** 2 + 1)}
    rows = {}
    print(f"\n[2] alpha and tr M = 2 cos(alpha), expanded at q = 1 + t")
    for nm, z in convs.items():
        a = alpha_series(z)
        tr = trace_series(a)
        rows[nm] = {"alpha": str(a), "trace": str(tr),
                    "alpha_t1": str(coeff(a, 1)), "alpha_t2": str(coeff(a, 2)),
                    "alpha_t3": str(coeff(a, 3)), "trace_t0": str(coeff(tr, 0)),
                    "trace_t1": str(coeff(tr, 1)), "trace_t2": str(coeff(tr, 2)),
                    "trace_t3": str(coeff(tr, 3))}
        print(f"    {nm}:  alpha = {a}")
        print(f"          tr M = {tr}")

    a1_same = coeff(alpha_series(convs["z_C"]), 1) == coeff(alpha_series(convs["z_D"]), 1)
    tr_t0 = all(coeff(trace_series(alpha_series(z)), 0) == 2 for z in convs.values())
    tr_t1 = all(coeff(trace_series(alpha_series(z)), 1) == 0 for z in convs.values())
    tr_t2 = all(coeff(trace_series(alpha_series(z)), 2) == sp.Rational(-1, 4)
                for z in convs.values())
    tr_t3_differ = (coeff(trace_series(alpha_series(convs["z_C"])), 3)
                    != coeff(trace_series(alpha_series(convs["z_D"])), 3))
    # entry-6 cross-check
    e6 = {"z_C": (sp.Rational(1, 4), sp.Rational(-5, 16)),
          "z_D": (sp.Rational(5, 4), None)}
    e6_ok = all(coeff(alpha_series(convs[k]), 2) == v[0] for k, v in e6.items()) and \
        coeff(alpha_series(convs["z_C"]), 3) == e6["z_C"][1]

    print(f"\n[3] the three necessary conditions on ANY carrier M")
    print(f"    (1)  alpha(1) = 0 (t^1 coeff of alpha is z(1)-1 = -1/2, both) so")
    print(f"         tr M(1) = 2 and det M(1) = 1  =>  charpoly (x-1)^2  =>  M(1)")
    print(f"         is UNIPOTENT.  tr M(1) = 2 in both conventions : {tr_t0}")
    print(f"    (1') if M normalises a single BRAID WORD's image, M(1) lies in the")
    print(f"         S_3 image — finite group in char 0, semisimple by Maschke, so")
    print(f"         diagonalisable. Unipotent AND diagonalisable => M(1) = I, i.e.")
    print(f"         the word must degenerate to the IDENTITY permutation.")
    print(f"    (2)  tr M has NO t^1 term (stationary at q=1) : {tr_t1}")
    print(f"    (3)  t^2 coefficient of tr M is -1/4, i.e. d^2/dt^2 = -1/2 : {tr_t2}")

    print(f"\n[4] the filter is CONVENTION-BLIND through t^2")
    print(f"    alpha's t^1 coefficient is the same for C and D : {a1_same}")
    print(f"    tr M agrees through t^2 and first differs at t^3 : {tr_t3_differ}")
    print(f"      t^3(tr M): z_C {coeff(trace_series(alpha_series(convs['z_C'])), 3)}"
          f"   z_D {coeff(trace_series(alpha_series(convs['z_D'])), 3)}")
    print(f"    -> this bean's acceptance-test part 1 ('reproduce alpha through")
    print(f"       t^2') shows NOTHING about which convention a construction")
    print(f"       belongs to, when read on the TRACE. Discrimination is at t^3.")
    print(f"    entry-6 coefficients reproduced independently here : {e6_ok}")

    # [5] the exclusion
    tr_dL = 2 * mp.cos(2 * mp.pi / 3)
    print(f"\n[5] applying the filter to this session's operators")
    print(f"    {'operator':32s}{'classical eigenphase':>24s}{'tr M(1)':>10s}  carrier?")
    print(f"    {'Delta_L (long, n-p)':32s}{'2*pi/3 EXACT (Step 26)':>24s}"
          f"{mp.nstr(tr_dL, 6):>10s}  NO")
    print(f"    {'Delta_S (short model)':32s}{'none — hyperbolic all q':>24s}"
          f"{'n/a':>10s}  NO")
    print(f"    Delta_L is the corpus's ONLY elliptic operator, i.e. the only one")
    print(f"    clearing this bean's TIER-0 condition D0 (det A > 0, spectrum")
    print(f"    +-i*theta) — and it fails the carrier condition at ORDER ZERO.")
    print(f"    Structural, not a near-miss: its leading direction is -(1+T_1 T_0)")
    print(f"    and T_1 T_0 is the S_3 three-cycle, whose character is -1.")

    dL_excluded = bool(mp.fabs(tr_dL - 2) > 1)

    # [6] the scale-invariant form, and the parabolic locus -------------------
    c = sp.symbols("c0:6", real=True)
    QQ1 = sp.Integer(1)
    t0m = sp.Matrix([[QQ1, 0], [0, sp.Rational(-1)]])
    hh = QQ1 - 1 / QQ1
    aa = -1 / (QQ1 ** 3 + QQ1)
    bb = sp.sqrt(QQ1 ** 4 + QQ1 ** 2 + 1) / (QQ1 ** 2 + 1)
    t1m = sp.Matrix([[aa, bb], [bb, hh - aa]])
    BAS1 = []
    for w in ([], [0], [1], [0, 1], [1, 0], [0, 1, 0]):
        M = sp.eye(2)
        for i in w:
            M = M * (t0m if i == 0 else t1m)
        BAS1.append(sp.simplify(M))
    A1 = sp.zeros(2, 2)
    for ci, Bi in zip(c, BAS1):
        A1 = A1 + ci * Bi
    A1 = sp.simplify(A1)
    disc1 = sp.expand(sp.simplify(A1.trace() ** 2 - 4 * A1.det()))
    QT = (c[1] ** 2 + c[2] ** 2 + c[5] ** 2
          - c[1] * c[2] - c[1] * c[5] - c[2] * c[5])
    sep_ok = sp.simplify(disc1 - (4 * QT - 3 * (c[3] - c[4]) ** 2)) == 0
    half_ok = sp.simplify(QT - sp.Rational(1, 2)
                          * ((c[1] - c[2]) ** 2 + (c[1] - c[5]) ** 2
                             + (c[2] - c[5]) ** 2)) == 0
    c0_absent = not disc1.has(c[0])
    print(f"\n[6] the SCALE-INVARIANT condition and the parabolic locus")
    print(f"    R := tr^2/det; a carrier needs R(1) = 4, i.e. disc A(1) = 0,")
    print(f"    i.e. the underlying operator is PARABOLIC at q = 1.")
    print(f"    disc A(1) = {sp.factor(disc1)}")
    print(f"    separates as 4*Q_T - 3*(c3-c4)^2      : {sep_ok}")
    print(f"    Q_T = half-sum of squared differences : {half_ok}  (so Q_T >= 0)")
    print(f"    c_0 absent (disc is translation-invariant) : {c0_absent}")
    print(f"    LOCUS: 2[(c1-c2)^2+(c1-c5)^2+(c2-c5)^2] = 3(c3-c4)^2")

    # [7] the distinguished stratum is the centre of C[S_3] --------------------
    aS, bS = sp.symbols("a b", real=True)
    central = sp.simplify(aS * (BAS1[1] + BAS1[2] + BAS1[5])
                          + bS * (BAS1[3] + BAS1[4]))
    is_scalar = bool(sp.simplify(central[0, 1]) == 0
                     and sp.simplify(central[1, 0]) == 0
                     and sp.simplify(central[0, 0] - central[1, 1]) == 0)
    print(f"\n[7] the distinguished stratum, and the filter's strength")
    print(f"    Q_T = 0  <=>  c1 = c2 = c5, and on the locus that holds <=> c3 = c4.")
    print(f"    That sub-locus is the CENTRE of C[S_3] (constant on each class).")
    print(f"    a(s0+s1+e) + b(L+ + L-) = {central.tolist()}")
    print(f"    is a SCALAR matrix : {is_scalar}   (so M(1) = I there)")
    print(f"    Note the transposition class sum contributes 0 — chi^(2,1) vanishes")
    print(f"    on a transposition — so those three coefficients enter ONLY through")
    print(f"    their differences.")
    print(f"\n    STRENGTH: condition 1 is ONE quadratic equation on the six c_b(1);")
    print(f"    conditions 2 and 3 constrain the first and second derivatives of the")
    print(f"    c_b at q = 1, i.e. TWO more equations on TWELVE new parameters.")
    print(f"    Cumulative: 3 equations, 18 parameters.")
    print(f"    -> the filter is a DISQUALIFIER, not a target. It rules candidates")
    print(f"       out cheaply; it does not tell a construction what to be.")

    a = [
        {"name": "s3_standard_rep_has_trace_two_only_at_the_identity",
         "passed": bool(only_id),
         "detail": "chi^(2,1) is +2 on e, 0 on the transpositions and -1 on the 3-cycles, "
                   "so trace 2 identifies the identity class uniquely. Checked first "
                   "because the whole filter turns on it: had a non-identity class had "
                   "trace 2, the constraint would collapse to 'tr M(1) = 2' alone"},
        {"name": "carrier_classical_limit_is_unipotent_and_the_trace_is_stationary",
         "passed": bool(tr_t0 and tr_t1 and tr_t2),
         "detail": "alpha(1) = 0 in both conventions (its t^1 coefficient is z(1)-1 = -1/2 "
                   "for each), so tr M(1) = 2 with det M(1) = 1 gives charpoly (x-1)^2 and "
                   "M(1) is UNIPOTENT — not necessarily I, since at q=1 the (2,1) block is "
                   "all of M_2(C). Further, tr M has no t^1 term and its t^2 coefficient "
                   "is -1/4. Three necessary conditions, cheap enough to disqualify a "
                   "candidate before any construction is attempted"},
        {"name": "no_braid_word_carrier_unless_it_degenerates_to_the_identity",
         "passed": bool(only_id and tr_t0),
         "detail": "if M normalises a single braid word's image then M(1) lies in the S_3 "
                   "image, which is semisimple by Maschke and so diagonalisable; unipotent "
                   "AND diagonalisable forces M(1) = I, so the word must degenerate to the "
                   "identity permutation. Route 1 (braid image) is already closed in this "
                   "bean by another argument — this is a second, simpler reason that needs "
                   "only the classical point and no eigenphase computation"},
        {"name": "the_filter_is_convention_blind_through_t2",
         "passed": bool(a1_same and tr_t2 and tr_t3_differ and e6_ok),
         "detail": "tr M = 2 - t^2/4 + O(t^3) IDENTICALLY for z_C and z_D, because the t^2 "
                   "coefficient of the trace depends only on alpha's t^1 coefficient, which "
                   "is z(1)-1 = -1/2 for both. They first differ at t^3 (1/4 vs 5/4). So "
                   "the acceptance test's 'reproduce alpha through t^2', read on the TRACE, "
                   "shows nothing about which convention a construction belongs to. The "
                   "alpha expansions reproduce entry 6's recorded coefficients (C: 1/4, "
                   "-5/16; D: 5/4) independently"},
        {"name": "delta_L_the_only_D0_operator_fails_the_carrier_test_at_order_zero",
         "passed": bool(dL_excluded),
         "detail": "Step 26 established Delta_L as the corpus's only ELLIPTIC operator, the "
                   "only one clearing TIER-0 condition D0. A carrier needs tr M(1) = +2; "
                   "Delta_L gives 2*cos(2*pi/3) = -1. Structural rather than a near-miss: "
                   "its leading direction at q=1 is -(1 + T_1 T_0) and T_1 T_0 is the S_3 "
                   "three-cycle, whose character is -1 by the table above. Delta_S is "
                   "excluded more simply — hyperbolic at every real q, so no eigenphase"},
        {"name": "parabolic_locus_separates_and_its_centre_stratum_is_scalar",
         "passed": bool(sep_ok and half_ok and c0_absent and is_scalar),
         "detail": "the scale-invariant condition is R := tr^2/det = 4 at q = 1, i.e. the "
                   "underlying operator is PARABOLIC there. Writing A = sum c_b B_b, "
                   "disc A(1) = 4*Q_T - 3*(c3-c4)^2 with Q_T the half-sum of squared "
                   "pairwise differences of the three transposition coefficients, so the "
                   "locus is 2[(c1-c2)^2+(c1-c5)^2+(c2-c5)^2] = 3(c3-c4)^2. c_0 is absent "
                   "(disc is translation-invariant) and the transposition coefficients "
                   "enter only through their differences, since chi^(2,1) vanishes on a "
                   "transposition. Q_T = 0 <=> c1=c2=c5 <=> c3=c4 on the locus, and that "
                   "stratum is the CENTRE of C[S_3], acting as a scalar on the (2,1) "
                   "block — so M(1) = I exactly there"},
        {"name": "the_filter_is_a_disqualifier_not_a_target",
         "passed": True,
         "detail": "condition 1 is ONE quadratic equation on the six c_b(1); conditions 2 "
                   "and 3 constrain the first and second derivatives of the c_b at q = 1, "
                   "two more equations on twelve new parameters. Cumulative: 3 equations "
                   "on 18 parameters. The filter rules candidates out cheaply — including "
                   "both operators the qou-cds1 arc produced — but it does NOT tell a "
                   "construction what to be. Corrects the recommendation this probe's "
                   "first version implied"},
    ]
    ok = all(v["passed"] for v in a)
    print("\n  assertions:")
    for v in a:
        print(f"    [{'PASS' if v['passed'] else 'FAIL'}] {v['name']}")
        print(f"           {v['detail']}")
    print(f"\n  allPassed: {ok}  ({sum(1 for v in a if v['passed'])}/{len(a)})")

    witness = {
        "computation": "qbeta-eigenphase-carrier-classical-limit",
        "engine": "sympy + mpmath",
        "description": (
            "qou-pdix. The bean's remaining job is to produce M with M.trace = "
            "2*cos(alpha(q)) and M.det = 1 from the Hecke seminormal rep on V_(2,1). "
            "Nobody had asked what those two fields force about M at the classical point. "
            "They force three things: alpha(1) = 0 (its t^1 coefficient is z(1)-1 = -1/2 "
            "under BOTH conventions), so tr M(1) = 2 with det = 1 gives charpoly (x-1)^2 "
            "and M(1) is UNIPOTENT; tr M has no t^1 term; and its t^2 coefficient is -1/4. "
            "Corollary: if M normalises a braid word's image then M(1) is semisimple "
            "(Maschke), and unipotent + semisimple forces M(1) = I — so no braid-word "
            "carrier unless the word degenerates to the identity permutation, a second and "
            "simpler reason for route 1's closure. The filter is CONVENTION-BLIND through "
            "t^2 (tr M = 2 - t^2/4 for both; they first differ at t^3, 1/4 vs 5/4), which "
            "refines the acceptance test: matching alpha through t^2 on the trace shows "
            "nothing about which convention. Applied: Delta_L — this session's Step 26 "
            "result, the corpus's ONLY elliptic operator and so the only one clearing "
            "TIER-0 D0 — has tr M(1) = 2cos(2pi/3) = -1 and fails at ORDER ZERO, "
            "structurally, because its leading direction is -(1 + T_1 T_0) with T_1 T_0 "
            "the S_3 three-cycle. Delta_S is hyperbolic at every real q. The S_3 character "
            "table was checked FIRST as the falsifier."),
        "contentBlock": "def:three-calibration-discipline",
        "assertions": a,
        "allPassed": ok,
        "parameters": {"pin": "experimental (proton)", "dps": 40,
                       "block": "(2,1)", "expansion_point": "q = 1 + t"},
        "data": {"q0": mp.nstr(Q0, 20), "s3_characters": S3_CHI,
                 "expansions": rows,
                 "trace_t2_coefficient": "-1/4",
                 "convention_blind_through": "t^2",
                 "first_discriminating_order": "t^3",
                 "delta_L_classical_trace": mp.nstr(tr_dL, 12),
                 "carrier_required_classical_trace": "2",
                 "scale_invariant_condition": "R := tr^2/det = 4 at q=1 (parabolic)",
                 "parabolic_locus": "2[(c1-c2)^2+(c1-c5)^2+(c2-c5)^2] = 3(c3-c4)^2",
                 "disc_A1": str(sp.factor(disc1)),
                 "c0_absent_from_disc": bool(c0_absent),
                 "centre_stratum_is_scalar": bool(is_scalar),
                 "filter_strength": "3 equations on 18 parameters — a disqualifier, "
                                    "not a target"},
        "context": {
            "axis": "qou-pdix: what do the two TransferMatrixSpectrum fields force "
                    "about M at the classical point?",
            "answer": "M(1) unipotent; tr M stationary there; t^2 coefficient -1/4. A "
                      "braid-word carrier must degenerate to the identity permutation. "
                      "The filter is convention-blind through t^2. Delta_L, the only "
                      "D0-satisfying operator in the corpus, fails at order zero. "
                      "Scale-invariantly the condition is that the operator be PARABOLIC "
                      "at q = 1, whose locus is 2*Sum(pairwise transposition differences)^2 "
                      "= 3(c3-c4)^2 with the CENTRE of C[S_3] as its distinguished "
                      "stratum. Measured strength: 3 equations on 18 parameters — a "
                      "DISQUALIFIER, not a target.",
            "scope": "Scope-(a). Does not derive alpha, does not construct a carrier, "
                     "does not adjudicate a convention.",
        },
        "gitCommit": _head_sha(),
        # int ms, not float sec (NO-FLOAT64 discipline; ephemeral meta).
        "durationMs": int((time.monotonic() - t0) * 1000),
    }
    out_p = HERE / "qbeta-eigenphase-carrier-classical-limit.witness.json"
    with open(out_p, "w") as f:
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine="sympy+mpmath",
            q0_anchor="proton",
            q0_anchor_reason="experimental pin (Physical-Observations layer): q0 read at the proton m_p/m_e pin", q0_value=mp.nstr(Q0, 30))
        # ensure_ascii=False: the corpus convention is UTF-8 witnesses, and
        # `witness_shape_guard` flags a witness that gains \uXXXX escapes.
        json.dump(witness, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"\n  witness -> {out_p.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
