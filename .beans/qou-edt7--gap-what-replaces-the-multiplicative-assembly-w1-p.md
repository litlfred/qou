---
# qou-edt7
title: 'GAP: what replaces the multiplicative assembly W=1-PROD f — both corpus assemblies miss the 3-body sign, in OPPOSITE directions'
status: todo
type: task
priority: normal
created_at: 2026-08-30T03:16:24Z
updated_at: 2026-08-30T09:00:03Z
parent: qou-mhj9
---

Opened 2026-08-30 after #6059 merged (207ee81f). The merged tranche 3 named the
ASSEMBLY as the defect locus; this bean is the successor question.

## The trilemma -- both corpus assemblies miss the 3-body sign, opposite ways

AME2020 Ursell cumulants (measured, he4_body_order_shortfall_location_probe):
    b2 = 2.224566   b3 = +1.426222   b4 = +9.243387  MeV

ASSEMBLY 1 -- multiplicative / Mayer, W(K) = 1 - PROD f_ij, normalised at the
deuteron. This is what the 08-29 probe and PROBE 2 use.
    b3 = 3*f_pn - 2 - P3,  P3 >= 0  =>  b3 <= 3*f_pn - 2
    b3 > 0 REQUIRES f_pn > 2/3; all four measured f_pn are below it (largest
    z_D = 0.61269). => b3 < 0 ALWAYS.
    PROVED: QOU.MassTheory.MayerThreeBodySign.lt_of_b3_pos (merged, sorry-free).

ASSEMBLY 2 -- pairwise-additive log form, B = -alpha * SUM_{i<j} ln f_ij. This is
the form the 2026-08-08 audit s10a DERIVES (tr_M multiplicative + energy
extensive => Cauchy functional equation => f = c*ln x, "the log form is forced").
    A pairwise-additive map has ALL connected cumulants above 2 identically zero:
      uniform g: B(2)=g, B(3)=3g, B(4)=6g
      b2 = g;  b3 = 3g - 3*g = 0;  b4 = 6g - 6g - 4*0 = 0
    => b3 = 0 EXACTLY, not merely small. (Arithmetic, not a fit.)

So: assembly 1 gives b3 < 0, assembly 2 gives b3 = 0, nature gives b3 > 0.
NEITHER corpus assembly can produce a positive connected 3-body cumulant.

## What this constrains about a replacement

  * It must be NEITHER pairwise-additive (b3 = 0 identically) NOR
    multiplicative-with-f_pn<=2/3 (b3 < 0).
  * It cannot be reached by changing the EDGE SET (b3 bound is edge-set
    independent), the LIKE-PAIR TYPING (inside P3), or the ENERGY SCALE
    (b3's sign is scale-free) -- all three proved in the merged file.
  * It cannot be a per-lambda reweighting (PROBE 4 / #5234 scaling wall).
  * Tranche 2 adds: it must be ARRANGEMENT-INDEPENDENT, which the linear chain
    provably is not at q != 1 (ChainBondOrderDependence.orderIndependent_iff).

## The tension worth noticing

s10a's derivation of the log form is a real argument (multiplicativity +
extensivity => Cauchy => log). If it is right, assembly 2 is FORCED -- and
assembly 2 has b3 = 0, so the corpus would be committed to a functional that
provably cannot reproduce a nonzero 3-body cumulant. Either the s10a derivation
has an unstated hypothesis (most likely: it assumes the atom trace factorises
over INDEPENDENT subsystems, which is exactly what a bound state is not), or the
body-order series is not the right decomposition of B.

That is the honest next question, and it is a DERIVATION question, not a fit.

## Do NOT

  * propose a functional chosen because it lands b3 > 0 -- that is the forbidden
    anchor inversion in new clothes;
  * re-run an edge-set / typing / scale variant expecting the sign to move.


## HALF LANDED 2026-08-30 — the trilemma is now machine-checked

Lean: QOU/MassTheory/PairwiseAdditiveCumulants.lean, sorry-free, lean-direct
exit 0, #print axioms clean on all 9 decls.

  pairwise_b3_eq_zero / pairwise_b4_eq_zero -- a pairwise-additive assembly
      B(A) = C(A,2)*g has b3 = 0 and b4 = 0 EXACTLY, for every g. Not small.
  ame_b3_pos            -- AME's b3 > 0, from the 08-29 probe's own literals.
  no_pairwise_matches_ame / trilemma -- so no pairwise-additive assembly
      reproduces the measured 3-body cumulant.

With the merged MayerThreeBodySign.b3_neg_of_le (multiplicative assembly below
the 2/3 threshold => b3 < 0), both corpus assemblies are now machine-checked to
miss the measured sign, in opposite directions. The trilemma is no longer an
argument in a bean; it is two sorry-free files.

### STILL OPEN — and it is the whole question

What replaces the assembly. Nothing here proposes one, and the constraint list in
the body above stands unchanged. The 08-08 s10a Cauchy derivation of the log form
is untouched by this: if it is right, the corpus is committed to a functional
with zero 3-body content while the body-order programme needs some. My reading
of where the escape is -- judgement, marked as such in the Lean docstring too --
is that s10a assumes the trace factorises over INDEPENDENT subsystems, which a
bound state is not.


## SUPERSEDED IN PART ON MAIN 2026-08-30, and ONE SEAM CLOSED

#6101 (merged 06:42) landed QOU/Mass/PairwiseCumulantVanishing.lean with
b3_eq_zero_of_isPairwise / b4_eq_zero_of_isPairwise / b3_eq_zero_ofBondFunctional
-- general over EVERY bond functional. My PairwiseAdditiveCumulants.lean assumed
a COMMON BOND VALUE and is a special case, so it was DELETED rather than merged.

WHAT WAS GENUINELY MISSING, and is now added
(QOU/MassTheory/AmeBindingNotPairwise.lean, sorry-free, axioms clean):
their not_isPairwise_of_b3_ne_zero is the falsifiable form, and its docstring
instantiates it against measurement -- "Since AME2020 gives b3 = +1.426222 != 0,
the physical binding is not of this shape" -- IN PROSE. No BindingMap is built
from AME numbers anywhere on main. So the step from the general theorem to the
physical conclusion was asserted, not checked. Now:
  ameMap        -- pairs at B(D)=2.224566, triples at the 3H/3He isospin average
  ame_b3_eq     -- b3 = 2852445/2000000 = 1.4262225 exactly
  ame_not_isPairwise

DISCREPANCY NOTED, NOT RESOLVED: the 4He AME literal is 28.295673 in
he4_body_order_shortfall_location_probe.py and 28.2956624 in #6101's writeup --
1.1e-5 MeV apart. b3 does not depend on it, so the b4 leg was deliberately NOT
instantiated. Someone should reconcile the two literals against the AME2020
table before any b4 statement is machine-checked.

THE GATE IS STILL OPEN. Both assemblies are now excluded on main; nothing
proposes a replacement.


## RESOLVED (2026-08-30): the ⁴He AME literal discrepancy is a KNOWN, already-fixed defect

#6088 flagged `28.295673` (in `he4_body_order_shortfall_location_probe.py:90`) against
`28.2956624` (used in the #6101 writeup) — 1.06e-5 MeV apart — and deliberately left it
unresolved. It is settled, and the corpus settled it before either of us:

**28.2956624 is correct. 28.295673 is a hand-typed legacy literal.**

The producer `computations/ame_2020_binding_energies.py` names this exact pair in its own
docstring (lines 14-24), as one of six entries where a hand-typed witness disagreed with the
vendored AME2020 publication table:

    B_he4   28.295673   vs  28.2956624   (+10.6 eV)

and records that AME's own uncertainty on B(⁴He) is 0.8 eV, so "a 10.6 eV gap is ~13 sigma —
not a rounding artifact".

Independent confirmation, three ways:
1. Mass-excess route by hand: 2*7288.971064 + 2*8071.31806 - 2424.91587 = 28295.662378 keV.
2. `computations/ame-2020-binding-energies.witness.json` carries
   `B_he4_MeV = 28.2956624` and `B_he4_MeV_mass_excess_route = 28.295662378`, and the
   producer asserts the per-A and mass-excess columns agree for every nuclide.
3. `codata_constants.ame_binding_mev(2, 4)` returns `28.2956624` (run at 50 dps).

**The fix already exists as a function call** — `AME_B_HE4_MEV_VALIDATION = _ame_binding_mev(2, 4)`
in `computations/substrate/codata_constants.py:315`. What never happened is the consumer
migration: **82 live (non-`_deprecated/`) files still hardcode `28.295673` or `28.295674`**,
including 11 under `computations/deltalambda/` and 20 under `computations/probes/`.

Magnitude: 3.7e-7 relative. It cannot move any conclusion in this arc — the assembly defect
is 30 %+ — so the trilemma above stands unchanged with either literal. Recording it as a
separate stale-literal class rather than sweeping it here; a sweep touches long-compute
producers and would need its own scope. Tracked separately.
