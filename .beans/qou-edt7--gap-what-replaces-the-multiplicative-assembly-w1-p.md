---
# qou-edt7
title: 'GAP: what replaces the multiplicative assembly W=1-PROD f — both corpus assemblies miss the 3-body sign, in OPPOSITE directions'
status: todo
type: task
priority: normal
created_at: 2026-08-30T03:16:24Z
updated_at: 2026-08-30T03:34:50Z
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
