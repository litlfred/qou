#!/usr/bin/env python3
"""The binding tower's resolution problem is SELF-INFLICTED, not experimental —
5.81 digits are lost to the mirror convention, and the framework already holds
the information needed to recover them.

## The standing conclusion this qualifies

`binding_magnitude_is_not_validatable_probe.py` measures the body-order tower
under all 27 mirror conventions, finds `b_3` determined to 0.271 significant
digits, and concludes:

    "AME light-nucleus binding is the wrong observable to test one against, and
     effort should go to finding an observable with resolution rather than to a
     seventh ansatz."

Three further probes (`..._alternation_is_generic`, `..._growth_is_the_alpha_
anomaly`, `..._ratio_is_a_transient`) reached the same place from other
directions.  Nothing here disputes any of that measurement.

What none of them asked is WHERE the 0.271 digits go.  The implicit reading is
that the data are poor.  The data are excellent.

## The measurement

AME2020 gives the light bindings to 6.7-7.6 significant digits:

    2H    2224.566 keV  +- 0.00040   6.75 digits
    3H    8481.796 keV  +- 0.00090   6.97
    3He   7718.041 keV  +- 0.00045   7.23
    4He  28295.662 keV  +- 0.00080   7.55

Propagating those through `b_3 = B(3) - 3*B(2)`:

    variant            b_3 (keV)    sigma_exp    digits
    3H alone           1808.0976     0.001500      6.08
    3He alone          1044.3427     0.001282      5.91
    mirror average     1426.2202     0.001301      6.04

    CONVENTION band    1044.34 .. 1808.10  = 53.6%  ->  0.271 digits

**5.81 digits — a factor of 646,000 — are lost to the choice between 3H and
3He, and none of it to experiment.**

## Why that matters, and it is not a criticism of the earlier probe

"The observable has no resolution" and "our construction discards the
resolution the observable has" call for opposite responses.  The first says
abandon the observable.  The second says fix the construction.

The mirror ambiguity exists because the body-order construction takes `A` as its
only input, so `B(3)` must stand for both 3H and 3He.  But the framework is not
A-only: `canonical_braid_crossings.atom_canonical_crossings(Z, N)` returns
DIFFERENT words for tritium (1,2) and 3He (2,1) -- measured in
`per_atom_braid_closure_probe`, 4 of 35 positions differ, exponent sums 4 and 8.
The information needed to separate the mirror pair is already computed and then
averaged away.

## What is claimed and what is not

CLAIMED (measured): the experimental resolution of `b_3` is ~6 digits; the
convention band is 0.271; the difference is 5.81 digits.

CLAIMED (measured, prior work): the framework's per-atom word distinguishes the
mirror pair.

INFERRED, and flagged as inference: a Z-resolved body-order construction would
have ~6 digits to work with rather than 0.27, comparable to Q_beta (6.11) and
Delta_pn (6.36) in the L2 dashboard.

NOT CLAIMED: that such a construction exists, that anyone should build it, that
it would match anything, or that the many-body term is derivable.  The
resolution being recoverable in principle says nothing about whether there is
something to find.

## Scope

(a).  It refutes nothing and reverses no conclusion.  It relocates the cause of
a measured problem from the data to the construction, which changes what the
sensible response is.

Exact `Fraction` arithmetic on the tabulated values; uncertainties combined in
quadrature with `math.hypot`, which is the correct propagation for independent
errors and is the only floating-point step.  `float()` otherwise only in
f-strings.
"""
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

_R = Path(__file__).resolve().parents[2]
AME = _R / "qou-mass/src/qou_mass/data/ame2020.json"

CHECKS = []


def check(name, got, want, note=""):
    ok = got == want
    CHECKS.append(ok)
    print(f"  [{'ok ' if ok else 'FAIL'}] {name}: {got}" + (f"  ({note})" if note else ""))
    return ok


d = json.load(open(AME))
E = {(e["Z"], e["A"]): e for e in d["entries"]}
B = lambda Z, A: F(str(E[(Z, A)]["binding_energy_total_keV"]))          # noqa: E731
U = lambda Z, A: F(str(E[(Z, A)]["binding_energy_per_A_unc_keV"])) * A  # noqa: E731

print("=" * 78)
print("The binding tower's resolution loss is SELF-INFLICTED — 5.81 digits")
print("=" * 78)

print("\n1. AME2020 knows these bindings to 6.7-7.6 digits")
for lbl, (Z, A) in (("2H", (1, 2)), ("3H", (1, 3)), ("3He", (2, 3)), ("4He", (2, 4))):
    b, u = B(Z, A), U(Z, A)
    dig = math.log10(float(b / u))
    print(f"       {lbl:<5} {float(b):>12.3f} keV  +- {float(u):.5f}   {dig:>5.2f} digits")
    check(f"{lbl} known to >6 digits", dig > 6, True, f"{dig:.2f}")

print("\n2. Propagated to b_3 = B(3) - 3*B(2)")
B2, U2 = B(1, 2), U(1, 2)
variants = {"3H alone": (B(1, 3), U(1, 3)), "3He alone": (B(2, 3), U(2, 3))}
digs = {}
for lbl, (B3, U3) in variants.items():
    b3 = B3 - 3 * B2
    s = math.hypot(float(U3), 3 * float(U2))          # independent errors
    digs[lbl] = math.log10(abs(float(b3)) / s)
    print(f"       {lbl:<12} b_3 = {float(b3):>10.4f}   sigma = {s:.6f}   {digs[lbl]:>5.2f} digits")
check("both variants give >5.9 experimental digits",
      all(v > 5.9 for v in digs.values()), True,
      f"{min(digs.values()):.2f} .. {max(digs.values()):.2f}")

print("\n3. The convention band — the number the corpus reports")
lo, hi = B(2, 3) - 3 * B2, B(1, 3) - 3 * B2
mid = (lo + hi) / 2
band = (hi - lo) / mid
conv_dig = math.log10(1 / float(band))
print(f"       {float(lo):.4f} .. {float(hi):.4f}   width/mid = {float(band) * 100:.1f}%"
      f"   -> {conv_dig:.3f} digits")
check("reproduces the recorded 53.6% band", abs(float(band) - 0.536) < 0.001, True,
      f"{float(band) * 100:.1f}%")
check("reproduces the recorded 0.271 digits", abs(conv_dig - 0.271) < 0.002, True,
      f"{conv_dig:.3f}")

print("\n4. The split")
lost = digs["3H alone"] - conv_dig
print(f"       experimental      {digs['3H alone']:>6.2f} digits")
print(f"       convention band   {conv_dig:>6.2f} digits")
print(f"       LOST              {lost:>6.2f} digits   = a factor of {10 ** lost:.3g}")
check("more than 5 digits lost to the convention", lost > 5, True, f"{lost:.2f}")
check("and essentially none to experiment", digs["3H alone"] > 6, True,
      f"{digs['3H alone']:.2f} available")

print("\n5. The framework already separates the mirror pair")
print("       per_atom_braid_closure_probe (merged, #6942): tritium (1,2) and")
print("       3He (2,1) have DIFFERENT canonical words -- 4 of 35 positions")
print("       differ, exponent sums 4 vs 8.  The body-order construction takes")
print("       A as its only input and averages that distinction away.")
print("\n       For comparison, the L2 dashboard's own observables:")
print("         m_p 9.51   m_e 9.50   m_n 9.29   m_mu 7.66")
print("         Delta_pn 6.36   Q_beta 6.11   m_K/m_pi 4.58")
print(f"       A Z-resolved b_3 would sit at ~{digs['3H alone']:.1f} — in that company.")
print("       INFERENCE, not a result: nobody has built such a construction.")

ok = all(CHECKS)
print("\n" + "=" * 78)
print(f"{sum(CHECKS)}/{len(CHECKS)} checks pass")
print("=" * 78)
print("""
VERDICT (scope-(a); nothing refuted, one cause relocated):

  AME light-nucleus binding is NOT a low-resolution observable.  It carries
  ~6 significant digits on b_3.  The 0.271 digits the corpus reports is what
  survives averaging 3H against 3He, and 5.81 digits -- a factor of 646,000 --
  are lost there rather than in the measurement.

  This does not reverse the standing conclusion; it changes what follows from
  it.  "The observable has no resolution" implies abandoning the observable.
  "Our construction discards the resolution it has" implies fixing the
  construction -- and the framework already computes the Z-dependence it
  averages away.

  Whether a Z-resolved construction would find anything is a separate question
  and is NOT addressed here.
""")
sys.exit(0 if ok else 1)
