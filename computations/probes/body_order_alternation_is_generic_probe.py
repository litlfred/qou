#!/usr/bin/env python3
"""Calibration: the SIGN ALTERNATION of the body-order coefficients is generic and
carries no information.  The GROWTH RATE is what is distinctive.

This refutes nothing.  It measures how much evidential weight one observed
feature can bear, which is the sort of thing the critical-distance license exists
for, and it is prompted by `QOU.Mass.JetFiltrationSignObstruction`, whose
argument takes the alternation as its measured input:

    "Measured, exactly and convention-invariantly (all 27 mirror conventions),
     the binomial-basis body-order coefficients B(A) = sum_k mu_k C(A,k)
     ALTERNATE ... any measured sign alternation in the body-order terms must be
     carried by a_D alone."

That file is careful — it states its identification of `mu n` with `a_D n * w n`
as unestablished, and everything downstream is conditional.  This probe supplies
the missing calibration for the *other* half: how surprising is the alternation?

## Three findings, in order of importance

**1. The corpus's pair-locality inference is SOUND.**  Verified, not assumed: a
strictly pairwise binding `B(A) = mu_2 * C(A,2)` has `mu_k = 0` for every k >= 3,
exactly.  So `CrossingModelPairLocality.not_pairLocal_of_b3_ne_zero` is valid and
nothing here touches it.

**2. The alternation is GENERIC.**  Every smooth non-pairwise toy model tested --
`A^2`, `A^3`, `A^(3/2)`, and an SEMF-like volume-minus-surface form -- alternates
in sign for k >= 4, with NO many-body content of any kind.  Pure `A^3` even
reproduces AME's exact sign pattern `+ + + - + -`.  Alternation is simply what
the finite-difference (Mobius) basis does to a smooth function that is not
proportional to `C(A,2)`; observing it is not evidence about many-body physics.

**3. The GROWTH RATE is the discriminator.**  Per-step geometric rate over
k = 4..7, `(|mu_7|/|mu_4|)^(1/3)`:

    A^2                       1.205
    A^3                       1.205
    A^(3/2)                   1.193
    SEMF aV*A - aS*A^(2/3)    2.174
    AME (measured)            3.431

The toy models cluster in 1.19-2.17; AME sits at 3.43, well outside.  That
separation is the informative measurement, and it is the one the alternation
argument does not use.

## Scope

Not a refutation, and explicitly NOT scope-(b): no invariant is violated and no
claim of the corpus is contradicted.  It is a scope-(a) calibration of one
feature's evidential weight.  In particular it does NOT weaken
`not_pairLocal_of_b3_ne_zero`, which finding 1 independently confirms.

Exact `Fraction`/integer arithmetic for every assertion; irrational toy models are
carried as exact rationals with a stated denominator.  `float()` appears only in
f-strings and in the reported growth rate, which is descriptive rather than
asserted.
"""
import sys
from fractions import Fraction as F
from math import comb

MEAS = {2: F("2.22457"), 3: F("1.42622"), 4: F("9.24338"),
        5: F("-55.77912"), 6: F("166.12507"), 7: F("-373.24295")}

DEN = 10 ** 9   # exact-rational denominator for the irrational toy models
CHECKS = []


def check(name, got, want, note=""):
    ok = got == want
    CHECKS.append(ok)
    print(f"  [{'ok ' if ok else 'FAIL'}] {name}: {got}" + (f"  ({note})" if note else ""))
    return ok


def mu_of(B, kmax=7):
    """Binomial-basis coefficients with the corpus convention B(0) = B(1) = 0."""
    return {k: sum((-1) ** (k - j) * comb(k, j) * B(j) for j in range(k + 1))
            for k in range(2, kmax + 1)}


def rat_pow(j, e):
    """Exact rational approximation of j**e to DEN."""
    return F(round(j ** e * DEN), DEN)


print("=" * 78)
print("The body-order sign ALTERNATION is generic; the GROWTH RATE is the signal")
print("=" * 78)

# ------------------------------------------------------------------ finding 1
print("\n1. SOUNDNESS CHECK — a strictly pairwise binding kills every mu_k, k >= 3")
for c in (F(7, 3), F(1), F(-5, 2)):
    mu = mu_of(lambda j, c=c: c * comb(j, 2))
    check(f"B(A) = {c}*C(A,2): mu_k = 0 for k>=3",
          [mu[k] for k in range(3, 8)], [F(0)] * 5)
    check(f"B(A) = {c}*C(A,2): mu_2 = {c}", mu[2], c)
print("       -> not_pairLocal_of_b3_ne_zero is SOUND; nothing here touches it.")

# ------------------------------------------------------------------ finding 2
print("\n2. GENERICITY — smooth non-pairwise models alternate, with no many-body content")
models = {
    "A^2                   ": lambda j: F(0) if j < 2 else F(j * j),
    "A^3                   ": lambda j: F(0) if j < 2 else F(j ** 3),
    "A^(3/2)               ": lambda j: F(0) if j < 2 else rat_pow(j, 1.5),
    "SEMF aV*A - aS*A^(2/3)": lambda j: (F(0) if j < 2 else
                                         F(1554, 100) * j - F(1683, 100) * rat_pow(j, 2 / 3)),
}
mus = {n: mu_of(B) for n, B in models.items()}
for n, mu in mus.items():
    alt = all((mu[k] > 0) != (mu[k + 1] > 0) for k in range(4, 7))
    check(f"{n} alternates for k>=4", alt, True)
sig = lambda m: "".join("+" if m[k] > 0 else "-" for k in range(2, 8))  # noqa: E731
check("pure A^3 reproduces AME's exact sign pattern", sig(mus["A^3                   "]),
      sig(MEAS), sig(MEAS))
check("AME alternates for k>=4",
      all((MEAS[k] > 0) != (MEAS[k + 1] > 0) for k in range(4, 7)), True)
print("       -> alternation is what the Mobius basis does to any smooth")
print("          B(A) not proportional to C(A,2).  It is not evidence.")

# ------------------------------------------------------------------ finding 3
print("\n3. THE DISCRIMINATOR — per-step growth rate over k = 4..7")
rate = lambda m: (abs(float(m[7])) / abs(float(m[4]))) ** (1 / 3)  # noqa: E731
for n, mu in mus.items():
    print(f"       {n}  {rate(mu):>6.3f}")
print(f"       {'AME (measured)        '}  {rate(MEAS):>6.3f}")
# The assertions are exact: compare |mu_7|*|mu_4|^-1 as rationals, no cube roots.
toy_max = max(abs(mu[7]) / abs(mu[4]) for mu in mus.values())
ame_ratio = abs(MEAS[7]) / abs(MEAS[4])
check("AME |mu_7/mu_4| exceeds every toy model's", ame_ratio > toy_max, True,
      f"AME {float(ame_ratio):.2f} vs max toy {float(toy_max):.2f}")
check("and by more than 3x", ame_ratio > 3 * toy_max, True,
      f"{float(ame_ratio / toy_max):.2f}x")

ok = all(CHECKS)
print("\n" + "=" * 78)
print(f"{sum(CHECKS)}/{len(CHECKS)} checks pass")
print("=" * 78)
print("""
VERDICT (scope-(a) calibration; nothing refuted):

  1. The pair-locality inference is SOUND -- verified independently here.
     B(A) = mu_2*C(A,2) kills every mu_k for k >= 3, exactly, at three values
     of mu_2 including a negative one.

  2. The SIGN ALTERNATION carries no information.  A^2, A^3, A^(3/2) and an
     SEMF-like form all alternate for k >= 4 with no many-body content, and
     pure A^3 reproduces AME's exact sign pattern + + + - + -.

  3. The GROWTH RATE is the real signal: toy models 1.19-2.17 per step, AME
     3.43 -- a ratio |mu_7/mu_4| more than 3x any toy model's.

  Consequence for JetFiltrationSignObstruction: its conditional structure is
  untouched, but the alternation it takes as measured input is generic.  An
  argument that would be equally satisfied by B(A) = A^3 is not constraining
  the many-body content.  The growth rate is the measurement that does.
""")
sys.exit(0 if ok else 1)
