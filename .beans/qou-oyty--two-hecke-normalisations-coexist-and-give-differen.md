---
# qou-oyty
title: 'Two Hecke normalisations coexist and give different Ext^1: Z vs Z[i]'
status: todo
type: task
priority: normal
created_at: 2026-08-24T20:25:30Z
updated_at: 2026-08-24T20:25:30Z
---

Found while computing Ext^1 for bean qou-zut2 (2026-08-24). Not a defect in either block on its own — a discrepancy BETWEEN blocks that changes a stated answer, and it is invisible unless the two are read together.

## The two relations

* `QOU/BraidKnot/HeckeAnyonicSubstrate.lean` field `heckeQuadratic`:
  "(T_{s_i} - q)(T_{s_i} + 1) = 0"  -->  eigenvalues q and -1.
* `content/.../knots-particles-confinement/categorical-meson.md`, and the
  Groebner-Shirshov normal-form work generally:
  "sigma_i^2 = h sigma_i + 1" with h = q - q^-1  -->  roots q and -q^-1.

Both are standard Iwahori-Hecke normalisations. They are related by rescaling
the generator, so neither is wrong. But the Ext computation is not invariant
under that rescaling, because it depends on the DIFFERENCE of the eigenvalues.

## Why it changes the answer

QOU/Mathlib/HeckeExtOne.lean proves Ext^1(V_beta, V_alpha) = R / (alpha - beta),
for the rank-one-by-rank-one extension, over any CommRing.

* Convention A (alpha = q, beta = -1): ideal (q + 1), and
  R_q/(q+1) = Z[q,q^-1]/(q+1) = Z  via q |-> -1.
* Convention B (alpha = q, beta = -q^-1): ideal (q + q^-1). In R_q the factor
  q^-1 is a unit, so the ideal is (q^2 + 1), and the quotient is
  Z[q]/(q^2+1) = Z[i] — the GAUSSIAN INTEGERS, not Z.

So `phase-transition-boundary.md`s "Ext^1_{H_n(q)}(V_asym, V_sym) = Z" is
correct under A and false under B. The block does not say which relation it
assumes, and the corpus uses B in the chapter where the normal forms are
actually computed.

The degeneracy loci differ too, which is the physical reading: A degenerates at
q = -1, B at q^2 = -1. Those are different points, so "the non-semisimple locus"
is not a convention-free notion here either.

## What to do

Not mechanical — pick one and say so, or state both. Three options:

1. Declare a normalisation in the substrate (one block, cited by both chapters)
   and mark every Hecke relation elsewhere as a rescaling of it, with the
   rescaling written down. Most work, most durable.
2. Leave both but annotate `phase-transition-boundary.md` with the relation its
   "= Z" assumes. Cheapest honest fix.
3. Check whether the mixed-channel argument actually needs B, in which case the
   answer is Z[i] and the pi_3(S^2) generator claim needs re-examining, since
   Z[i] is not the Hopf invariant group.

Option 3 is the one that could change a physics claim, so it should be checked
before 2 is written.

## Where the evidence is

QOU/Mathlib/HeckeExtOne.lean module docstring states the caveat in full and
proves the general R/(alpha - beta) form deliberately, so neither convention is
baked in. Zero sorries, axiom-clean. This bean exists so the caveat is not lost
in a file docstring.
