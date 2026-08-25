#!/usr/bin/env python3
"""The C and D Markov parameters coincide at `q = 1` — and only there (bean qou-cds1).

## The question this answers

`qou-cds1` has to re-derive the Q_β `c_k` ladder under the 2026-08-15 ruling
that convention **D** (`z_D = q³/(q²+1)`) is canonical and **C**
(`z_C = √q/(q+1)`) is excised.  The bean's own discipline note forbids opening
with a wide numerical re-fit:

    "Formalize-first: before any wide numerical re-fit of the ladder, state the
     structural constraint the D-frame ladder must satisfy and check whether it
     prunes the class."

This is that step for the N=3 rung.  It runs no extractor and proposes no `c_k`.

## The constraint

`z_C` and `z_D` are different functions, but they are not different everywhere.
Cleared of denominators in the substrate variable `s = √q`, their coincidence
locus is

    s·(s⁴ + 1) = s⁶·(s² + 1)   ⟺   s⁷ + s⁵ = s⁴ + 1                    (†)

`s = 1` is a root of (†), and the corpus already proves the complementary half:
`QOU.QBeta.decayLadder_zC_not_jones` (sorry-free) shows (†) has no root with
`s > 1`, since `z·[2]_q = q²` characterises `z_D`.  Assertion 3 below records
the cofactor explicitly — (†) factors as `(s−1)·(s⁶+s⁵+2s⁴+s³+s²+s+1)`, whose
second factor has all-positive coefficients and so has no positive root at all.

So: **C and D define the same Markov parameter at `q = 1`, and at no other
point of the substrate branch.**

## Where this sits relative to what is already proved

**Read `QOU.BraidKnot.Q_beta_categorical_ofPhase_tail_common` first** — it is
the primary result here and it is already in the corpus, sorry-free.  It proves
the convention enters the ladder at exactly one place, the N=1 eigenphase, so
the whole N=2..5 tail (`c₂`, `c₃`, `c₄`, `c₅`) is phase-blind and therefore
convention-blind *as written*.  `markovZ'` is hard-coded to `z_C` (assertion 7
below), so `alpha` is the C-frame phase and it is the only thing `z_D` touches.

This probe closes a different, narrower gap: `tail_common` is about the ladder's
**written form**, and says nothing about the **provenance** of the constants in
that form.  `c₃ = J_Hopf(q=1)` is a Markov trace of the Hopf link, and a Markov
trace *does* depend on `z` — so the written form being z-free does not by itself
establish that the constant `−2` survives the frame change.  The coincidence at
`q = 1` is what establishes that.  The two results are complementary; neither
subsumes the other.

## What it prunes, and what it does NOT

The ladder's N=3 rung is `1 + J_Hopf(q=1)·u³`, i.e. `c₃ = J_Hopf(q=1) = −2`.
That coefficient is a **classical-limit** (`q = 1`) evaluation of a Markov-trace
invariant.  By the constraint above it is evaluated exactly at the one point
where the two conventions agree, so:

  * `c₃ = −2` as a **proposed closed form** is convention-INVARIANT.  The C→D
    ruling does not move it, and it does not need re-deriving.  Same for the
    `jonesHopfClassicalLimit` prefactor carried into the N=4 rung.

  * `c₂ = −1` is likewise untouched, for a different and weaker reason: it is a
    `ring` identity (`1 − b²ℏ⁴ = 1 − (bℏ²)²`), independent of `z` altogether.

  * `c₄` and `c₅` are **also** unmoved — but by `tail_common`, not by anything
    here.  They sit in the phase-blind tail.  An earlier draft of this probe
    claimed they "must be re-derived because they are evaluated at `q₀ ≠ 1`";
    **that was wrong**, and it was wrong because it reasoned about where a
    coefficient is *evaluated* instead of whether `z` enters its rung at all.

  * What genuinely remains is the **N=1 phase itself**.  `alpha = (z−1)h/2` is
    *asserted* in both frames — a literal, derived in neither — so there is no
    C-frame derivation to port to D.  See
    `qbeta_ladder_required_phase_probe.py`, which already establishes that the
    reported `c₃ ≈ −974` under `z_D` is the N=1 phase residual magnified by the
    fixed `1/u³`, common to both frames, and not a statement about `c₃`.
    Reconstruction cross-check (this session, not committed as a claim): holding
    the tail fixed and pushing the N=1 phase ratio `cos(α_D − u/2)/cos(α_C − u/2)`
    into the N=3 rung reproduces `−974.4319` against the recorded `−974.43`, a
    relative agreement of 1.9e-6 — i.e. the recorded number is that phase
    residual, to the precision it is quoted at.

**This is a scope-(a) negative about the near-match, not a positive result.**
The proposed `c₃ = −2` surviving the ruling is *not* good news for it: the bean
records that re-extraction under D returns `c₃ ≈ −974`.  Under C the proposed
−2 sat 3.47 % from the extracted value, and that agreement was the entire
empirical case for the identification `c₃ = J_Hopf(1)`.  Under D the same
proposed value sits ~4.7·10⁴ % away.  So the ruling does not refute the closed
form; it **removes its supporting evidence**, which was C-frame.  The
identification is now an unsupported proposal, and this probe says so rather
than reporting "c₃ = −2 survives" as though that were a win.

Nothing here closes the numerical gap, proposes a D-frame `c₃`, or licenses
wiring −974 (a sensitivity measurement) anywhere.

## Method

Exact symbolic ℚ(q) and ℚ(s) via sympy — no float, no mpmath evaluation, no
fitting.  Per AGENTS.md §"PROBES ARE NOT EXEMPT".
"""
from __future__ import annotations

import sys

import sympy as sp

s = sp.symbols("s", positive=True)          # substrate variable, q = s²
q = sp.symbols("q", positive=True)


def z_C(qq):
    """Convention C Markov parameter: z = √q/(q+1)."""
    return sp.sqrt(qq) / (qq + 1)


def z_D(qq):
    """Convention D Markov parameter (canonical): z = q³/(q²+1)."""
    return qq ** 3 / (qq ** 2 + 1)


def qbracket(n, qq):
    """[n]_q = q^{n-1} + q^{n-3} + ... + q^{-(n-1)}."""
    return sum(qq ** (n - 1 - 2 * i) for i in range(n))


def main() -> int:
    failures: list[str] = []

    def check(name: str, ok: bool, detail: str) -> None:
        status = "PASS" if ok else "FAIL"
        print(f"  [{status}] {name}: {detail}")
        if not ok:
            failures.append(name)

    print("Assertions (exact symbolic; no float anywhere):")

    # ---- 1. The two parameters agree at q = 1, with the common value 1/2. ----
    zc1 = sp.nsimplify(sp.simplify(z_C(sp.Integer(1))))
    zd1 = sp.nsimplify(sp.simplify(z_D(sp.Integer(1))))
    check(
        "1. z_C(1) = z_D(1) = 1/2",
        zc1 == sp.Rational(1, 2) and zd1 == sp.Rational(1, 2),
        f"z_C(1) = {zc1}, z_D(1) = {zd1}",
    )

    # ---- 2. They are NOT the same function. ----
    diff = sp.simplify(z_C(q) - z_D(q))
    check(
        "2. z_C != z_D as functions",
        sp.simplify(diff) != 0,
        f"z_C - z_D = {sp.simplify(sp.together(diff))} (not identically 0)",
    )

    # ---- 3a. (dagger) is DERIVED as the coincidence locus, not asserted. ----
    # In the substrate variable (q = s²):  z_C = s/(s²+1),  z_D = s⁶/(s⁴+1).
    # Over the common denominator (s²+1)(s⁴+1) the numerator is
    #     s(s⁴+1) − s⁶(s²+1) = −s·(s⁷ + s⁵ − s⁴ − 1),
    # so on s > 0 the coincidence locus is exactly (dagger): s⁷+s⁵ = s⁴+1.
    zc_s = sp.cancel(z_C(s ** 2))
    zd_s = sp.cancel(z_D(s ** 2))
    dagger = sp.expand(s ** 7 + s ** 5 - s ** 4 - 1)
    numer = sp.expand(sp.numer(sp.cancel(sp.together(zc_s - zd_s))))
    check(
        "3a. numerator of (z_C - z_D) in s is  -s*(dagger)",
        sp.expand(numer + s * dagger) == 0,
        f"z_C = {zc_s}, z_D = {zd_s}; numerator = {numer}",
    )

    # ---- 3b. Factorisation of (dagger); the cofactor is positive-coefficient.
    factored = sp.factor(dagger)
    cofactor = sp.expand(sp.cancel(dagger / (s - 1)))
    cofactor_coeffs = sp.Poly(cofactor, s).all_coeffs()
    check(
        "3b. (dagger) factors as (s-1)(s^6+s^5+2s^4+s^3+s^2+s+1)",
        sp.expand(factored - (s - 1) * cofactor) == 0
        and all(c > 0 for c in cofactor_coeffs),
        f"cofactor = {cofactor}; coeffs {cofactor_coeffs} all positive",
    )

    # ---- 4. s = 1 is the ONLY positive root of (†). ----
    roots = sp.solve(sp.Eq(dagger, 0), s)
    positive_real = [r for r in roots if r.is_real and r.is_positive]
    check(
        "4. s = 1 is the only positive real root of (dagger)",
        positive_real == [sp.Integer(1)],
        f"positive real roots = {positive_real}",
    )

    # ---- 5. z_D is exactly the Jones/TL pin z*[2]_q = q^2; z_C is not. ----
    pin_D = sp.simplify(z_D(q) * qbracket(2, q) - q ** 2)
    pin_C = sp.simplify(z_C(q) * qbracket(2, q) - q ** 2)
    check(
        "5. z_D satisfies z*[2]_q = q^2 identically; z_C does not",
        pin_D == 0 and sp.simplify(pin_C) != 0,
        f"D residual = {pin_D}; C residual = {sp.simplify(sp.together(pin_C))}",
    )

    # ---- 6. The divergence is genuine at the substrate, not a rounding effect.
    # Exact rational lower bound: at q = 11/10 (below any substrate q0 in use),
    # the two parameters already differ by more than 1/100.
    q_lo = sp.Rational(11, 10)
    gap = sp.nsimplify(sp.simplify(sp.Abs(z_C(q_lo) - z_D(q_lo))))
    check(
        "6. |z_C - z_D| > 1/100 already at q = 11/10 (exact)",
        sp.simplify(gap - sp.Rational(1, 100)) > 0,
        f"gap = {gap} = {sp.nsimplify(gap)} > 1/100",
    )

    # ---- 7. The ladder's own markovZ' is z_C, so `alpha` is the C-frame phase.
    # QOU.BraidKnot.markovZ' q = 1/(sqrt q + (sqrt q)^-1). This is the reason the
    # convention question reaches the ladder at all -- and, with tail_common, the
    # reason it reaches ONLY the N=1 rung.
    markovZ_prime = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))
    check(
        "7. the ladder's markovZ' equals z_C exactly (so alpha is C-frame)",
        sp.simplify(markovZ_prime - z_C(q)) == 0,
        f"1/(sqrt q + 1/sqrt q) = {sp.simplify(markovZ_prime)} = z_C",
    )

    print()
    if failures:
        print(f"FAILED {len(failures)}/8: {', '.join(failures)}")
        return 1
    print("8/8 assertions hold (exact symbolic).")
    print()
    print("CONSEQUENCE (scope-(a)): the C->D ruling leaves the PROPOSED c_3 = -2")
    print("unchanged, because J_Hopf is evaluated at q = 1 -- the single point")
    print("where the conventions agree. It simultaneously removes that value's")
    print("empirical support, which was the 3.47% C-frame near-match. No D-frame")
    print("c_3 is proposed here, and -974 is a sensitivity measurement, not a value.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
