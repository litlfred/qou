---
# qou-zut2
title: Ext^1 = Z for the mixed-channel extension contradicts H_n(q0) semisimplicity
status: in-progress
type: task
priority: normal
created_at: 2026-08-24T20:05:49Z
updated_at: 2026-08-24T20:06:18Z
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
