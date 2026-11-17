---
# qou-zut2
title: Ext^1 = Z for the mixed-channel extension contradicts H_n(q0) semisimplicity
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T20:05:49Z
updated_at: 2026-11-17T13:00:03Z
parent: qou-59vq
---

Raised while building route 2 to the topological charge (QOU/Mathlib/ExtensionClass.lean, 2026-08-24).

## The claim

`phase-transition-boundary.md` states that at the mixed-channel temperature the Hecke representation forms a NON-SPLIT extension

    0 -> V_sym -> V_mixed -> V_asym -> 0

"classified by Ext^1_{H_n(q)}(V_asym, V_sym) ~ Z. The Hopf invariant of pi_3(S^2) = Z generates it." This is one of only three routes the corpus has to a topological integer, and the only homological one.

## The contradiction

A SEMISIMPLE algebra has Ext^1 = 0: every module is projective, every short exact sequence splits, and there is no non-split extension to classify. The corpus asserts semisimplicity twice, at the physical point:

* `knot-eigenbasis-complete.md:3` — "Semisimplicity. The Iwahori-Hecke algebra H_n(R,q) = End_{B_n}(V^{tensor n}) is semisimple."
* `skein-resolution-obstruction.md:19` — "Over R at non-torsion q_0 ~ 1.1099, the algebra H_n(q_0) is semisimple (Rad = 0)."

So at q_0 the Ext group is 0, not Z, and the non-split extension cannot exist. Both claims cannot hold at the same q.

## NOT a missing-machinery problem — note the inversion

The instinct is that Ext over a non-division ring needs machinery we lack. The opposite is true. Ext exists precisely to work over rings where complements are not automatic; over a division ring it is identically zero and there is nothing to measure. `Submodule.exists_isCompl` requiring a DivisionRing is not an obstacle to recovering the invariant — it is why the invariant can exist at all.

What kills it here is that the algebra is TOO GOOD. Semisimplicity, not the ground ring, forces Ext^1 = 0.

## Where the resolution must lie

`skein-resolution-obstruction.md:19` names the non-semisimple locus in the same sentence: "At root-of-unity torsion ... the Iwahori-Hecke algebra has a radical that prunes the resolution tree." So Rad != 0 exactly at root-of-unity torsion.

Three candidate resolutions, and they are different papers:

1. The mixed-channel temperature is NOT q_0 but a root-of-unity point where Rad != 0. The claim survives but its q is not the physical one, and the phase transition becomes a statement about the degenerate locus. Requires saying which root of unity.
2. Ext is taken over R_q = Z[q,q^-1] (global dimension 2) rather than over H_n(q). Over R_q, Ext^1 is generally nonzero — but then it does not classify H_n(q)-module extensions and the Hecke content is decorative.
3. The claim is wrong and the corpus has only two routes to the integer.

## Already built

QOU/Mathlib/ExtensionClass.lean proves the part that does not depend on this: the charge IS the failure to split (hasRetraction_of_hasSection, isCompl_of_isSplit), and the ⋆_q eigenspace sequence splits when 2 is invertible (selfDual_isSplit), so the charge does not live in the self-duality decomposition. Zero sorries, axiom-clean.

## Mathlib status

CategoryTheory.Abelian.Ext exists (needs HasExt). CategoryTheory.ProjectiveResolution is NOT in this tree — probed, unknown identifier. Even the affirmative route needs infrastructure work.


---

## Verified 2026-08-24 — the contradiction is real, and it is worse than stated

Read all three blocks in full, plus `knot-eigenbasis-complete-proof.md`,
`hecke-algebra-from-braiding.md`, `phase-transition-interpretation.md`,
`composite-crossing-sublimation-criteria.md`, `substrate-parameter.{md,ts}`,
and the block's own Lean sibling. Five findings, each independently fatal
to `Ext^1_{H_n(q)}(V_asym, V_sym) = Z`.

1. **The modules do not exist.** `V_sym`, `V_mixed`, `V_asym` are defined
   NOWHERE — grep over `content/**` (md, ts, lean) returns only
   `phase-transition-boundary.md`, `composite-crossing-sublimation-criteria.md`
   (same claim with `S_sym`/`S_asym`), and `ExtensionClass.lean`'s docstring
   quoting the claim. There is no object for the Ext group to be taken of.

2. **Semisimplicity is the corpus's own theorem, with its own proof.**
   `knot-eigenbasis-complete-proof.md` part (1): "When q is not a root of
   unity, H_n(R,q) is isomorphic to C[S_n] as an abstract algebra (Jimbo's
   theorem), hence semisimple." So Ext^1 = 0 at q_0 follows from a proof the
   corpus already carries, not merely from an assertion.

3. **Resolution 1 (root of unity) is forbidden by axiom, twice over.**
   `fluid-dynamics/root-of-unity-truncation.md:24`: "The governing QOU axiom
   rigorously demands that q remains **not** a root of unity."
   `def:substrate-parameter`'s authorNote carries "not a root of unity" as an
   archimedean predicate on `ArchimedeanSubstrateField`. And there is no q to
   move anyway: the mixed channel is a **temperature** at fixed q, not a value
   of q — the block's own formulas are T_q = S_q / [2]_q, functions OF q.

4. **Z is not in the range of Ext over this algebra at ANY q.** Ext^1_A(M,N)
   for a k-algebra A is a k-module. The block's `.ts` authorNote and its
   `.lean` sibling both fix the ground ring: "archimedean specialisation over
   R", `abbrev R_q := R`. Over R (or C, per `jones-markov-trace.md`) Ext^1 is
   a vector space — divisible, torsion-free — hence never isomorphic to Z
   unless zero. Root-of-unity relocation would give a C-vector space, so
   resolution 1 could not deliver Z even if the axiom permitted it.

5. **The corpus already states the sequence as a direct sum.**
   `rem:hecke-algebra-from-braiding`: "The per-crossing weights q and -q^-1
   are exactly the eigenvalues of sigma on S^2 V (+) Lambda^2 V." The two
   channels the SES tries to connect ARE those two eigenspaces (per
   `phase-transition-interpretation.md`: gas = symmetric, eigenvalue q; solid
   = antisymmetric, eigenvalue -q^-1). They split by the orthogonal
   idempotents e_+ = (sigma + q^-1)/[2]_q, e_- = (q - sigma)/[2]_q, which need
   only [2]_q invertible — the very quantity `phase-transition-boundary.md`
   divides by two equations earlier. The block presupposes the splitting it
   then denies.

   Corollary: `V_mixed` cannot be a middle term either. The corpus identifies
   the mixed channel with lambda = (2,1) (`baryon-octet-decomposition.md`) and
   `knot-eigenbasis-complete.md` calls S_lambda **irreducible**. An
   irreducible module has no proper nonzero submodule.

## Resolution: 3 (the claim is wrong)

Not 1 — forbidden by the substrate axiom, and would not produce Z regardless.
Not 2 — the block's ground ring is pinned to R by its own `.ts` note and its
own Lean sibling, so no R_q-module reading is on offer here. (For the record,
2 is not mathematically empty: Ext^1_{Z[q,q^-1]}(Z, Z) = Z for Z = R_q/(q-1),
via 0 -> R_q -(q-1)-> R_q -> Z -> 0. But those are R_q-modules with no Hecke
content, and no block asks for them.)

**Falsifier.** Either (i) a corpus definition of V_sym/V_mixed/V_asym as
H_n(q_0)-modules in which V_mixed is not the direct sum of the other two, or
(ii) an explicit statement that the mixed-channel Hecke algebra is taken over
Z[q,q^-1] rather than over R. Either would overturn this.

**Consequence: the corpus has TWO routes to the topological integer, not
three.** The residue route (`thm:topological-charge-quantization`, lean.ref a
stub) and the winding route (`winding-parity-sign-transport`) survive. The
homological route does not exist.

## Mathlib status — this bean's note was wrong on the first point

Probed fresh today with `lean` directly:

* `CategoryTheory.ProjectiveResolution` **IS** in this tree. It needs
  `import Mathlib.CategoryTheory.Abelian.Projective.Resolution`; the earlier
  probe presumably imported the wrong module. Type-checks.
* `CategoryTheory.Abelian.Ext` and `CategoryTheory.Abelian.HasExt` are
  unknown constants even after importing `Mathlib.CategoryTheory.Abelian.Ext`;
  the Ext API's actual declaration name is still unlocated. Not chased —
  Ext is not needed for the surviving statement.
* What IS available and is all the surviving statement needs:
  `IsSemisimpleRing.isSemisimpleModule`, `exists_isCompl` (on
  `IsSemisimpleModule`), `Module.projective_lifting_property`.

RESOLVED — the contradiction dissolves; see QOU/Mathlib/HeckeExtOne.lean (2026-08-24).

Ext^1(V_beta, V_alpha) = R / (alpha - beta), computed directly for the
rank-one-by-rank-one extension. `extAction_quadratic` shows the Hecke relation
constrains the extension parameter c not at all, so the classification is a full
quotient of R.

With alpha = q, beta = -1: R_q/(q+1) = Z. **The corpus"s "= Z" is right.**

And it never contradicted semisimplicity. The Ext group is a TORSION module
supported exactly where the eigenvalues collide — which is exactly where the
algebra degenerates. `splits_of_isUnit_sub`: alpha - beta a unit implies
everything splits, so at q_0 ~ 1.1099 (q_0 + 1 ~ 2.11 invertible) Ext^1 = 0,
which is what Rad = 0 demands. The non-split extensions live at q = -1, the
double root of (T - q)(T + 1). Two statements about different fibres, not a
contradiction. Resolution (a) of the three listed above, confirmed by
computation rather than chosen.

No CategoryTheory.Abelian.Ext needed — the direct computation also sidesteps
ProjectiveResolution being absent from this Mathlib.

CAVEAT SPLIT OUT to bean qou-oyty: the answer is normalisation-dependent. The
corpus carries two Hecke relations and the other one gives Z[i], not Z. Do not
quote "= Z" without saying which relation is meant. qou-oyty option 3 is the one
that could change a physics claim.


---

## CORRECTION 2026-08-24 — the "dissolves" verdict above does not hold for this block

The RESOLVED note above is right about the algebra and wrong about the verdict.
`HeckeExtOne.lean`'s computation `Ext^1(V_beta, V_alpha) = R/(alpha - beta)` is
correct and is kept. What does not follow is "the corpus's = Z is right".

**1. Normalisation.** The note's Z comes from alpha = q, beta = -1, i.e.
convention A, `(T - q)(T + 1) = 0`, which lives in
`QOU/BraidKnot/HeckeAnyonicSubstrate.lean`. `phase-transition-boundary` is not
under A. The block that *defines* H_n(R,q) for this corpus,
`rem:hecke-algebra-from-braiding`, writes `(sigma - q)(sigma + q^-1) = 0`, and
`rem:phase-transition-interpretation` — the remark interpreting this very
proposition — names the channels "symmetric, eigenvalue q" and "antisymmetric,
eigenvalue -q^-1". That is convention B. Under B the ideal is
(q + q^-1) = (q^2 + 1) and the answer is Z[i], not Z. This is exactly
`qou-oyty` option 3, and the answer to it is: yes, the mixed-channel argument
needs B, so the value is Z[i] and the pi_3(S^2) = Z generator claim fails —
Z[i] is Z^2 as a group with no distinguished generator.

**2. Ring.** Even granting A, the "different fibres" defence relocates the
group off the block's own ring. The block's `.ts` note and its Lean sibling
both pin it to R (`abbrev R_q := ℝ`), and the note itself concedes Ext^1 = 0
there. So the sentence "the Hecke representation at the mixed-channel
temperature forms a non-split extension" remains false at the temperature and
ring the block is about.

**3. No real degenerate q exists under B.** Newly proved in
`QOU/Mathlib/ExtensionClass.lean`, sorry-free and axiom-clean:
`twoQ_eq_zero_iff` (the gap q + q^-1 vanishes iff q^2 + 1 = 0) and
`twoQ_ne_zero_of_ordered` / `heckeSES_isSplit_of_ordered` (over an ordered
field it never vanishes, so the sequence splits at EVERY nonzero q). The
collision point of A is q = -1; of B it is q = ±i. Neither is admissible —
`def:substrate-parameter` forbids roots of unity — and ±i is not even real.

**4. The middle term is still wrong.** `HeckeExtOne`'s M_c is free of rank two.
The corpus's V_mixed is the irreducible S_(2,1) (`baryon-octet-decomposition`,
`knot-eigenbasis-complete`). Nothing connects the two, and an irreducible
module admits no such sequence.

## What was done

* Content: `phase-transition-boundary.md` no longer asserts the non-split
  extension; it states the eigenprojection splitting, the semisimplicity
  vanishing, and the Z[i] classification with its non-real support. Status
  authorNote on the `.ts` with the evidence and the two rejected relocations.
  `rem:phase-transition-interpretation` and
  `rem:composite-crossing-sublimation-criteria` carried the same claim and are
  corrected with their own status notes; the valence-shell classification and
  the crossing-parity arithmetic are retained as empirical, without a
  derivation. `phase-transitions-intro.md` still promises the withdrawn
  derivation — SEE BELOW, not yet fixed at time of writing this note.
* Lean, all sorry-free and `#print axioms`-clean (propext / Classical.choice /
  Quot.sound only): `ExtensionClass.isSplit_of_isCompl`,
  `isSplit_of_isSemisimpleModule`, `isSplit_of_isSemisimpleRing`,
  `isCompl_ker_quadratic`, `heckeSES`, `heckeSES_isSplit`, `twoQ_eq_zero_iff`,
  `twoQ_ne_zero_of_ordered`, `heckeSES_isSplit_of_ordered`.
* `HeckeExtOne.lean` keeps every theorem; only its narrative was corrected —
  the title, the "they are not [inconsistent]" verdict, and the two
  normalisation-A docstrings that called A "the corpus's" relation.

**Bottom line: the corpus has two routes to the topological integer, not
three.** Residue (`thm:topological-charge-quantization`, lean.ref a stub) and
winding (`rem:winding-parity-sign-transport`). The homological route does not
exist at any q a QOU admits.

**Falsifier, restated after the reconciliation.** Show that
`phase-transition-boundary` is under convention A rather than B — i.e. that its
mixed channel is built from a generator with eigenvalues q and -1 rather than q
and -q^-1 — AND that its ground ring is R_q rather than R. Both are needed; A
alone still leaves the group zero over R.


**Addendum (same session):** `phase-transitions-intro.md` is now fixed too — the
chapter intro promised "we then derive sublimation using a non-split extension
classified by Ext^1"; it now says the channels are complementary summands and
that Ext^1 supplies no obstruction. Four content files in total:
`phase-transitions-intro.md`, `phase-transition-boundary.{md,ts,lean}`,
`phase-transition-interpretation.{md,ts}`,
`composite-crossing-sublimation-criteria.{md,ts}`.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-24 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

### Progress Update (Round 68 — PR litlfred/qou#8356)
- **PR:** https://github.com/litlfred/qou/pull/8356 (`2c058b5e380e076d0aec9233aad57fa6af43d018`)
- **Lean 4 Module:** `QOU.Foundations.BringCurveHochschildStaleWeightCyclicityThreeCellComparabilityQuadraticRescaling` (`LEAN_EXIT=0`, `0` warnings, `0` `sorry`, `0` `axiom`, `0 CRITICAL, 0 major, 0 advisory` across all directory-mode static vacuity & borrowed-name audits)
- **Numerical Probe & Witness:** `computations/probes/bring_curve_hochschild_stale_weight_cyclicity_three_cell_comparability_quadratic_rescaling_probe.py` & `computations/probes/bring-curve-hochschild-stale-weight-cyclicity-three-cell-comparability-quadratic-rescaling.witness.json` (`COMMIT1 = 8ee314938e6a9bac9ee46faedf9aebdee8b895fb`, `scriptHash = 326bd13833f0`, `allPassed = True`, `dps = 80`)
