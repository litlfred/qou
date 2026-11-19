#!/usr/bin/env python3
"""The body-order coefficients above k = 3 are dominated by TWO data points: the
He-4 binding spike and the mass-5 gap.

The companion probe `body_order_alternation_is_generic_probe` found that the sign
ALTERNATION of the mu_k carries no information, and that the GROWTH RATE is what
separates AME (3.43 per step) from smooth toy models (1.19-2.17).  This probe
localises that growth, and it turns out to sit almost entirely on A = 4 and A = 5.

## What is measured

The mu_k determine B(A) exactly: `B(A) = sum_k mu_k C(A,k)`.  Reconstructed, the
mirror-averaged binding is

    A=2  B= 2.2246   B/A=1.1123
    A=3  B= 8.0999   B/A=2.7000
    A=4  B=28.2957   B/A=7.0739   <- He-4: doubly magic N=Z=2, alpha clustering
    A=5  B=26.9457   B/A=5.3891   <- B DECREASES; no bound A=5 nucleus
    A=6  B=31.9940   B/A=5.3323
    A=7  B=38.4230   B/A=5.4890

(reconstruction verified against known AME values at A = 2, 3, 4 to 1e-4 MeV.)

The second difference of B has its extremum exactly there: `Delta^2 B` runs
`+14.320, -21.546, +6.398, +1.381`, and the outlier is the triple
B(3), B(4), B(5) -- the only one above 15 in magnitude.

## The null model

Replace B(4) and B(5) by linear interpolation between the UNTOUCHED B(3) and
B(6).  Nothing else changes.  This removes the alpha spike and the mass-5 gap and
leaves every other feature of the data in place.

    growth rate   measured 3.431   null 1.289
    |mu_7|        measured 373.24  null 6.40      -- 58.3x

The null model's 1.289 lands inside the smooth-toy-model band (1.19-2.17), i.e.
indistinguishable from a function with no many-body content at all.

## What this does NOT touch

`mu_2` and `mu_3` involve only A <= 3 and are **exactly unchanged** by the null
model.  So `b_3 = +1.4262 != 0` stands, and with it
`CrossingModelPairLocality.not_pairLocal_of_b3_ne_zero`.  The pair-locality
refutation is untouched; this probe is about k >= 4.

## Why it matters

It relocates the target.  The dramatic numbers (mu_5 = -55.8, mu_6 = +166.1,
mu_7 = -373.2) are not a diffuse many-body effect originating in the
substrate -- they are two points of textbook nuclear shell structure, the
alpha-particle binding maximum and the A = 5 gap.  Any framework term aimed at
"the growing body-order coefficients" would be aiming at those two points.

What no interpolation at A = 4, 5 can move is `mu_3 = +1.4262`.

## 🛑 But `mu_3` is NOT "robust" in the sense that matters — corrected

An earlier draft of this docstring, and the PR comment written from it, called
`mu_3` the robust survivor.  That conflates two different robustnesses, and the
corpus had already measured the one that matters.

`binding_magnitude_is_not_validatable_probe.py` computes the whole tower under
ALL 27 mirror conventions -- A=3 (3H/3He), A=5 (5He/5Li), A=7 (7Li/7Be) -- and
finds `b_3` has a **53.6% band, 0.271 significant digits**.  Reproduced
independently here: 3He alone gives 1.04435, 3H alone gives 1.80810, and the
1.42622 used throughout is the mirror AVERAGE.

So `mu_3` is invariant under *this* probe's A=4,5 interpolation and is the
**least determined magnitude in the tower** under the mirror conventions.  Those
are different axes, and only the second one bears on testing a mechanism.

That probe also inverts the natural next step: resolution IMPROVES with order,
and `b_7/b_6 = 2.2468 +- 5.0%` (1.305 digits) is the best-determined quantity in
the tower -- while `b_4/b_3`, which the arc has actually been scoring candidates
against, spans 4.267..10.314, a 93.3% band.  The high-order ratio is the target
with resolution, not `mu_3`.

## Scope

(a).  A localisation of where an observed quantity comes from.  It refutes
nothing, contradicts no corpus claim, and names no mechanism.  Linear
interpolation is a crude null and is not asserted to be the right smooth
continuation -- the argument does not depend on it, since `Delta^2 B` independently
picks out A = 4 as the outlier before any interpolation is chosen.

Exact `Fraction` arithmetic for every assertion; `float()` only in f-strings and
in the descriptive growth rate.
"""
import sys
from fractions import Fraction as F
from math import comb  # float64-ok: exact integer binomial coefficient

MU = {2: F("2.22457"), 3: F("1.42622"), 4: F("9.24338"),
      5: F("-55.77912"), 6: F("166.12507"), 7: F("-373.24295")}
KNOWN = {2: F("2.2246"), 3: F("8.1000"), 4: F("28.2957")}   # AME, mirror-averaged

CHECKS = []


def check(name, got, want, note=""):
    ok = got == want
    CHECKS.append(ok)
    print(f"  [{'ok ' if ok else 'FAIL'}] {name}: {got}" + (f"  ({note})" if note else ""))
    return ok


def mu_of(Bd, kmax=7):
    f = lambda j: F(0) if j < 2 else Bd[j]        # noqa: E731  -- corpus convention
    return {k: sum((-1) ** (k - j) * comb(k, j) * f(j) for j in range(k + 1))
            for k in range(2, kmax + 1)}


print("=" * 78)
print("The mu_k growth above k=3 is the He-4 spike and the A=5 gap — two points")
print("=" * 78)

B = {A: sum(MU[k] * comb(A, k) for k in MU if k <= A) for A in range(2, 8)}

print("\n1. Reconstruction of B(A) from the coefficients, checked against AME")
for A, v in KNOWN.items():
    check(f"B({A}) matches AME within 1e-3 MeV", abs(B[A] - v) < F(1, 1000), True,
          f"{float(B[A]):.4f} vs {float(v):.4f}")  # float64-ok: display-only f-string of exact Fraction
check("round-trip: mu_k recovered from B", mu_of(B), MU, "exact")

print("\n2. B/A is NOT monotonic — the alpha particle is a local maximum")
ba = {A: B[A] / A for A in B}
check("B/A rises to a maximum at A=4", max(ba, key=lambda a: ba[a]), 4,
      f"B/A(4) = {float(ba[4]):.4f}")  # float64-ok: display-only f-string of exact Fraction
check("B(5) < B(4) — binding DECREASES", B[5] < B[4], True,
      f"{float(B[5]):.4f} < {float(B[4]):.4f}")  # float64-ok: display-only f-string of exact Fraction

print("\n3. Delta^2 B picks out A=4 before any interpolation is chosen")
A = sorted(B)
d1 = {a: B[a + 1] - B[a] for a in A[:-1]}
d2 = {a: d1[a + 1] - d1[a] for a in A[:-2]}
for a in A:
    c1 = f"{float(d1[a]):>9.3f}" if a in d1 else " " * 9  # float64-ok: display-only f-string
    c2 = f"{float(d2[a]):>9.3f}" if a in d2 else " " * 9  # float64-ok: display-only f-string
    print(f"       A={a}  B={float(B[a]):>9.4f}  D1={c1}  D2={c2}")  # float64-ok: display-only f-string
# d2[a] = B(a+2) - 2B(a+1) + B(a), i.e. the second difference CENTERED on a+1.
# So the alpha/mass-5 feature -- B(3), B(4), B(5) -- is indexed at a = 3.
# (I first asserted index 4 here; the probe's own check caught the off-by-one.)
extremal = max(d2, key=lambda a: abs(d2[a]))
check("|Delta^2 B| is extremal at the triple centered on A=4", extremal, 3,
      f"d2[3] = {float(d2[3]):.3f}, spanning B(3),B(4),B(5)")  # float64-ok: display-only f-string
check("and it is the only |Delta^2 B| above 15",
      [a for a in d2 if abs(d2[a]) > 15], [3],
      f"others: {[round(float(d2[a]), 3) for a in sorted(d2) if a != 3]}")  # float64-ok: display-only f-string

print("\n4. Null model: interpolate A=4,5 between the untouched A=3 and A=6")
Bs = dict(B)
for a in (4, 5):
    Bs[a] = B[3] + F(a - 3, 3) * (B[6] - B[3])
M2 = mu_of(Bs)
check("mu_2 unchanged", M2[2], MU[2], "involves only A<=2")
check("mu_3 unchanged", M2[3], MU[3], "involves only A<=3 — b_3 is untouched")
print(f"       {'k':>2} {'measured':>13} {'null':>13}")
for k in range(2, 8):
    print(f"       {k:>2} {float(MU[k]):>13.4f} {float(M2[k]):>13.4f}")  # float64-ok: display-only f-string

rate = lambda m: (abs(float(m[7])) / abs(float(m[4]))) ** (1 / 3)   # noqa: E731  # float64-ok: descriptive growth rate display
print(f"\n       growth rate   measured {rate(MU):.3f}   null {rate(M2):.3f}")
check("null |mu_7| is >20x smaller", abs(MU[7]) > 20 * abs(M2[7]), True,
      f"{float(abs(MU[7]) / abs(M2[7])):.1f}x")  # float64-ok: display-only f-string
check("null growth rate falls inside the smooth-toy band",
      abs(M2[7]) / abs(M2[4]) < F(11), True,
      f"null |mu7/mu4| = {float(abs(M2[7]) / abs(M2[4])):.2f}, toy max 10.27")  # float64-ok: display-only f-string
check("measured growth rate does NOT", abs(MU[7]) / abs(MU[4]) > F(11), True,
      f"measured |mu7/mu4| = {float(abs(MU[7]) / abs(MU[4])):.2f}")  # float64-ok: display-only f-string

print("\n5. CORRECTION — mu_3 is NOT robust under the mirror conventions")
B2 = F("2.224566"); H3 = F("8.481798"); He3 = F("7.718043")
lo, hi = He3 - 3 * B2, H3 - 3 * B2
mid = (lo + hi) / 2
check("mirror average reproduces the quoted mu_3", abs(mid - MU[3]) < F(1, 1000), True,
      f"{float(mid):.5f} vs {float(MU[3]):.5f}")  # float64-ok: display-only f-string
check("mu_3 band exceeds 50%", (hi - lo) / mid > F(1, 2), True,
      f"{float(lo):.5f}..{float(hi):.5f} = {float((hi - lo) / mid) * 100:.1f}%")  # float64-ok: display-only f-string
print("       -> 0.271 significant digits; the LEAST determined magnitude in the")
print("          tower.  Reproduces binding_magnitude_is_not_validatable_probe.py,")
print("          which measured it first.  Invariance under A=4,5 interpolation and")
print("          invariance under the mirror conventions are DIFFERENT axes.")

ok = all(CHECKS)
print("\n" + "=" * 78)
print(f"{sum(CHECKS)}/{len(CHECKS)} checks pass")
print("=" * 78)
print("""
VERDICT (scope-(a) localisation; nothing refuted):

  The mu_k above k = 3 are dominated by TWO data points.  Removing only the
  He-4 spike and the A=5 gap -- by interpolating between the untouched A=3 and
  A=6 -- drops |mu_7| from 373.24 to 6.40, a factor of 58, and the growth rate
  from 3.431 to 1.289, inside the band of smooth models with no many-body
  content.

  Delta^2 B identifies A=4 as the outlier independently, before any
  interpolation is chosen, so the conclusion does not rest on the null model's
  crudeness.

  UNTOUCHED: mu_2 and mu_3 are exactly unchanged, so b_3 = +1.4262 != 0 and
  not_pairLocal_of_b3_ne_zero stand.

  CONSEQUENCE: a framework term aimed at "the growing body-order coefficients"
  would be aiming at the alpha-particle binding maximum and the mass-5 gap --
  textbook shell structure.

  BUT DO NOT READ mu_3 AS THE ROBUST RESIDUE.  It is invariant under THIS
  probe's A=4,5 interpolation and has a 53.6% band (0.271 digits) across the 27
  mirror conventions -- the least determined magnitude in the tower.  See
  binding_magnitude_is_not_validatable_probe.py, which measured that first and
  whose numbers are reproduced here.  The quantity with resolution is
  b_7/b_6 = 2.2468 +- 5.0%, at the OTHER end of the tower.
""")
sys.exit(0 if ok else 1)
