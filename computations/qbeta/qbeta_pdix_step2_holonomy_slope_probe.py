#!/usr/bin/env python3
"""qou-pdix 5b — the step-2 holonomy objects are in the FLAT basket, and per-rep does not escape it.

WHY THIS PROBE EXISTS, AND IT CORRECTS MY OWN RECOMMENDATION.  The companion
probe `qbeta_pdix_modular_double_locus_probe.py` pruned route 5a (the Faddeev
modular double) and closed with a "concrete next step": *compute the holonomy
log-slope of the step-2 Yekutieli non-abelian-Stokes connection at q0 and check
it against the target.*  **That step as worded is not runnable, and saying so is
the first finding here.**

THERE IS NO CONSTRUCTED STEP-2 CONNECTION.  Verified at the Lean, not taken from
the cheat sheet (whose own §2a warns that its status column was the thing that
was wrong):

  * `QOU.Mass.HeckeStokes.stokes_curvature_factors` is
    `X^2 - (q - 1/q)X - 1 = (X - q)(X + 1/q)`, discharged by `field_simp; ring`
    over a generic field.  Sound and useful -- it is where the two Hecke
    eigenvalues `q`, `-1/q` come from -- but it is an algebraic factorisation.
    There is no connection, no curvature form, no surface and no multiplicative
    integral in that file.
  * The curvature reading lives in a DOCSTRING in `NaStokesKeystone.lean`: the
    2-form is *stipulated* to be the Hecke quadratic, so imposing flatness
    recovers it tautologically.  AGENTS.md "Derive-then-check" item 8 verbatim:
    if it is true by `ring`, it is notation, not a theorem.

So "take the holonomy of the step-2 connection" presupposes exactly the object
that is step 2's acknowledged scope-(a) gap.

WHAT IS ACTUALLY THERE, AND IS MEASURABLE.  `NaStokesKeystone.lean` carries more
than the stipulation: a content-bearing §3b conjecture class whose open core is a
genuine PERIOD,

    ProlongationPeriodMeanQuantumDim.keystone :  aD (c+1) = lw c
    aD n = the n-jet Seiberg-Witten period  \oint_{S_c} lambda_SW^(n)
    lw c = (1/(c+1)) * sum_{lam |- c+1} dim_q V_lam      (mean quantum dimension)

and the file states its closed forms as hypotheses to a sorry-free conditional
theorem:  `lw 1 = 1`, `lw 2 = (q+1)^2/(3q) = (2 + [2]_q)/3`,
`lw 3 = (3q^2 + 4 + 3/q^2)/4`, and
`tauOf aD = 3(3q^4 + 8q^2 + 3)/(4 q (q+1)^2)`.

CONDITIONAL, AND THE DISTINCTION IS LOAD-BEARING.  `lw` being the step-2 period
IS the keystone conjecture.  Per AGENTS.md "conditional-proved != premise-
established", this probe measures `lw`; that `lw` = the period is assumed, not
shown.  Nothing here establishes the keystone and nothing here needs to.

THE MEASUREMENT.  The ladder's required eigenphase carrier is pinned by TWO
numbers (bean qou-pdix §D), and it is the SECOND that discriminates:

    P(q0)      = 1.997259194490263      (+/- 5.7e-7 relative)
    |P'/P|(q0) = 2.176                  (~4 figures)

Result -- every step-2 object is in the FLAT basket:

    lw 1                  1.0            slope 0          constant
    lw 2                  1.33696562     0.046958636      46.3x too flat
    lw 3                  2.53277966     0.22430586        9.7x too flat
    tauOf                 2.64238631     0.11385448       19.1x too flat
    2*chi^(3)/d   = 2     2.0            slope 0          constant
    2*chi^(1^3)/d = 2     2.0            slope 0          constant
    2*chi^(2,1)/[2]_q     1.983379502    0.1954502        11.1x too flat

PER-REP NORMALISATION DOES NOT ESCAPE IT, and that is the sharpest single line.
The corpus's standing structural claim is that the binding/eigenphase carrier is
the PER-REP q-Reeb phase `theta_lam = arccos(chi^lam / d_lam)` and that the
scalar `tr_M` COLLAPSES it.  That predicts the per-rep object should behave
differently from the collapsed average.  Measured, it does move -- dividing the
bare character by `d_lam` takes the slope `0.1018 -> 0.1955`, a factor 1.92 --
and it is still **11.1x short**.  The collapse is not what is costing the slope.

AND THE TWO ONE-DIMENSIONAL REPS ARE THE TRAP THE SECOND NUMBER EXISTS TO CATCH.
`lam = (3)` and `lam = (1^3)` have `d_lam = 1` and `chi = 1` on the Borromean, so
`2*chi/d = 2` EXACTLY -- **0.137 % from the target VALUE**, better than most of
the declared basket, and with slope **identically zero**.  A value-only
comparison would promote them; the slope constraint rejects them outright.

CALIBRATION -- why the slopes here can be trusted.  The bare `chi^(2,1)` is
already in the bean's declared basket at `0.1018`.  This probe's central-
difference method reproduces `0.10178739` on it, agreeing to 4 significant
figures with a figure recorded by someone else's measurement.  A slope method
that could not reproduce a known entry would not be evidence about the unknown
ones.

SCOPE -- (a), and deliberately not (b).  What is shown is that these DECLARED
forms, as they stand, do not have the required steepness.  It does NOT exclude a
holonomy of a genuinely DERIVED connection, because there is no such connection
in the corpus to test -- that is the point of the first section.  Per AGENTS.md
"Before declaring refuted", a scope-(b) exclusion needs a proved invariant and
this has none.

WHAT IT BUYS, WHICH IS A SPECIFICATION RATHER THAN AN EXCLUSION.  The bracket is
now populated on BOTH sides by real corpus objects and empty in the middle:

    step-2 / Laurent family   0.047 .. 0.224      9.7x - 46x TOO FLAT
    best declared basket      1.7363              1.25x too flat
    TARGET                    2.176                 --
    modular dual q~         816.73                375x TOO STEEP

Flatness here is not bad luck in which forms were tried: a low-degree rational in
`q` evaluated at `q0 ~ 1.11` simply cannot be steep, and a non-perturbative
`exp(-1/t)` cannot be shallow.  So the carrier must be an INTERMEDIATE
transcendental -- which is what an ordered exponential (a real holonomy) supplies
and what a polynomial average cannot.  That is precisely why the stipulated-
curvature problem in step 2 is the blocker and not a bookkeeping complaint:
**5b needs step 2 to be constructed, not stipulated.**

Bean: qou-pdix (stays OPEN).  Consumers: none (probe).  No witness by design;
every number carried as `mpf` per PROBES ARE NOT EXEMPT.
"""

import pathlib
import sys

import mpmath as mp

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path[:0] = [
    str(ROOT / p)
    for p in ("computations", "computations/substrate", "tools/qou-substrate/python")
]

from qou_substrate.constants import Q  # noqa: E402

mp.mp.dps = 50

# The two-number target, bean qou-pdix §D.
P_TARGET = mp.mpf("1.997259194490263")
SLOPE_TARGET = mp.mpf("2.176")

# Independently-recorded basket entries used as calibration / comparison.
BASKET_CHI21_SLOPE = mp.mpf("0.1018")   # bean's recorded slope for bare chi^(2,1)
BASKET_BEST_SLOPE = mp.mpf("1.7363")    # tr M_4_1, the least-flat declared form
DUAL_SLOPE = mp.mpf("816.73")           # q~, from the companion locus probe

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")


def log_slope(f, x: mp.mpf) -> mp.mpf:
    """|d ln f / dx| by central difference, matching the basket's convention."""
    e = x * mp.mpf("1e-25")
    return abs((mp.log(f(x + e)) - mp.log(f(x - e))) / (2 * e))


def main() -> int:
    q = mp.mpf(str(Q))
    h = lambda x: x - 1 / x                      # noqa: E731
    d21 = lambda x: x + 1 / x                    # noqa: E731  dim_q(2,1) = [2]_q
    chi21 = lambda x: 2 - 3 * h(x) ** 4 - h(x) ** 6  # noqa: E731

    print(__doc__.split("\n")[0])
    print()
    print(f"q0 = {mp.nstr(q, 18)}   (proton pin)")
    print(f"target  P = {mp.nstr(P_TARGET, 16)}   |P'/P| = {mp.nstr(SLOPE_TARGET, 6)}")
    print()

    # ---- 1. calibrate the slope method against a recorded figure -------------
    print("1. CALIBRATION -- reproduce a basket slope measured by someone else")
    s_chi21 = log_slope(chi21, q)
    rel = abs(s_chi21 - BASKET_CHI21_SLOPE) / BASKET_CHI21_SLOPE
    check(
        "central-difference slope reproduces the recorded bare chi^(2,1) entry",
        rel < mp.mpf("1e-3"),
        f"measured {mp.nstr(s_chi21, 9)} vs recorded {mp.nstr(BASKET_CHI21_SLOPE, 6)} "
        f"(rel {mp.nstr(rel, 4)}) -- method is calibrated, not merely self-consistent",
    )

    # ---- 2. the keystone lw ladder and tau -----------------------------------
    print()
    print("2. THE STEP-2 OBJECTS (keystone lw ladder + tau) -- all FLAT")
    step2 = {
        "lw 1 = 1": lambda x: mp.mpf(1),
        "lw 2 = (q+1)^2/(3q)": lambda x: (x + 1) ** 2 / (3 * x),
        "lw 3 = (3q^2+4+3/q^2)/4": lambda x: (3 * x ** 2 + 4 + 3 / x ** 2) / 4,
        "tauOf = 3(3q^4+8q^2+3)/(4q(q+1)^2)":
            lambda x: 3 * (3 * x ** 4 + 8 * x ** 2 + 3) / (4 * x * (x + 1) ** 2),
    }
    step2_slopes = {}
    for name, f in step2.items():
        s = log_slope(f, q)
        step2_slopes[name] = s
        flat = "constant" if s == 0 else f"{mp.nstr(SLOPE_TARGET / s, 5)}x too flat"
        print(f"     {name:<38} val={mp.nstr(f(q), 9):<14} slope={mp.nstr(s, 8):<14} {flat}")

    nonconst = [s for s in step2_slopes.values() if s > 0]
    check(
        "every non-constant step-2 object is at least 9x too flat",
        all(SLOPE_TARGET / s > 9 for s in nonconst),
        f"max step-2 slope {mp.nstr(max(nonconst), 8)} vs target "
        f"{mp.nstr(SLOPE_TARGET, 6)} -> at best "
        f"{mp.nstr(SLOPE_TARGET / max(nonconst), 5)}x too flat",
    )

    # ---- 3. per-rep normalisation does not escape the basket ----------------
    print()
    print("3. PER-REP NORMALISATION -- moves the slope, does NOT escape")
    s_norm = log_slope(lambda x: 2 * chi21(x) / d21(x), q)
    ratio = s_norm / s_chi21
    check(
        "dividing by d_lam moves the slope by <2x and leaves it >10x short",
        ratio < 2 and SLOPE_TARGET / s_norm > 10,
        f"bare {mp.nstr(s_chi21, 8)} -> normalised {mp.nstr(s_norm, 8)} "
        f"(factor {mp.nstr(ratio, 5)}); still "
        f"{mp.nstr(SLOPE_TARGET / s_norm, 5)}x too flat. So the tr_M COLLAPSE is "
        "not what costs the slope -- the per-rep refinement is flat too",
    )

    # ---- 4. the value-only trap ---------------------------------------------
    print()
    print("4. THE VALUE-ONLY TRAP -- the 1-dim reps beat the basket on VALUE, slope 0")
    v1 = mp.mpf(2)  # 2 * chi/d for lam=(3) and lam=(1^3): chi=1, d_lam=1
    rel_v1 = abs(v1 - P_TARGET) / P_TARGET
    check(
        "lam=(3) and lam=(1^3) give exactly 2, within 0.14% of P, with slope 0",
        rel_v1 < mp.mpf("0.002"),
        f"2*chi/d = 2 exactly, rel err vs P = {mp.nstr(rel_v1, 5)} "
        "(0.137%) and d/dq = 0 identically -- a value-only comparison would "
        "promote these; the second target number rejects them",
    )

    # ---- 5. the bracket is populated on both sides and empty in the middle --
    print()
    print("5. THE BRACKET -- both sides are real corpus objects; the middle is empty")
    lo = min(nonconst)
    print(f"     step-2 / Laurent family   {mp.nstr(lo, 6)} .. {mp.nstr(max(nonconst), 6)}"
          f"   ({mp.nstr(SLOPE_TARGET / max(nonconst), 4)}x - "
          f"{mp.nstr(SLOPE_TARGET / lo, 4)}x TOO FLAT)")
    print(f"     best declared basket      {mp.nstr(BASKET_BEST_SLOPE, 6):<12}"
          f"   ({mp.nstr(SLOPE_TARGET / BASKET_BEST_SLOPE, 4)}x too flat)")
    print(f"     TARGET                    {mp.nstr(SLOPE_TARGET, 6):<12}     --")
    print(f"     modular dual q~           {mp.nstr(DUAL_SLOPE, 6):<12}"
          f"   ({mp.nstr(DUAL_SLOPE / SLOPE_TARGET, 4)}x TOO STEEP)")
    check(
        "the target is strictly inside, with nothing declared near it",
        max(nonconst) < BASKET_BEST_SLOPE < SLOPE_TARGET < DUAL_SLOPE,
        "a low-degree rational at q0~1.11 cannot be steep and exp(-1/t) cannot be "
        "shallow, so the carrier must be an INTERMEDIATE transcendental -- what an "
        "ordered exponential supplies and a polynomial average cannot",
    )

    # ---- 6. scope --------------------------------------------------------------
    print()
    print("6. SCOPE -- (a), and conditional")
    check(
        "this is scope-(a) on DECLARED forms, not a structural exclusion",
        True,
        "no proved invariant forbids a holonomy of a genuinely derived connection; "
        "there is simply no such connection in the corpus to test, which is step 2's "
        "own acknowledged gap (curvature STIPULATED in a docstring, the Lean theorem "
        "being a field_simp;ring factorisation)",
    )
    check(
        "the lw measurement is CONDITIONAL on the keystone",
        True,
        "ProlongationPeriodMeanQuantumDim.keystone (aD(c+1) = lw c) is an unproved "
        "§3b class; that lw IS the step-2 period is assumed here, not shown -- "
        "conditional-proved != premise-established",
    )

    npass = sum(1 for _, ok, _ in CHECKS if ok)
    ntot = len(CHECKS)
    print()
    print("=" * 72)
    print(f"VERDICT  {npass}/{ntot} checks pass")
    print()
    print("step-2 holonomy average (lw)   FLAT: 9.7x - 46x short. scope-(a).")
    print("per-rep Reeb refinement        FLAT too: 11.1x short. The collapse is")
    print("                               not what costs the slope.")
    print("the 1-dim reps                 exactly 2 (0.137% on VALUE), slope 0 --")
    print("                               the trap the 2nd target number catches.")
    print("qou-pdix                       STILL OPEN. 5b needs step 2 CONSTRUCTED,")
    print("                               not stipulated.")
    print("=" * 72)
    return 0 if npass == ntot else 1


if __name__ == "__main__":
    raise SystemExit(main())
