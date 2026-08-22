---
# qou-oy4r
title: 'main is RED: def:qou-motivic-galois-instance lost its .lean sibling in 73a21ac34a'
status: completed
type: task
priority: normal
created_at: 2026-08-21T22:06:16Z
updated_at: 2026-08-22T20:26:26Z
---

MEASURED 2026-08-21, on a CLEAN checkout of main (ffd5c5e819) with no local
changes:

    bun run scripts/run-validate.ts content/quantum-observable-universe
    -> ✗ Invalid — 28 issue(s)      (1 error, 27 warnings)

The single error:

    ✗ [qou-motivic-galois-instance]: Definition
      "def:qou-motivic-galois-instance" requires Lean formalization.
      Expected sibling file: .../mass-endomorphism/qou-motivic-galois-instance.lean
      (or Lake-tree resolution from lean.ref
       "qou:QOU.LiftingDescent.QOUInstance.qouMotivicGaloisChar")

CAUSE — commit 73a21ac34a (Carl Leitner, 2026-08-21):
'refactor(motivic): demote almost_everywhere_nontrivial from class field to
standalone theorem, delete broken instance'. It deleted
content/quantum-observable-universe/mass-endomorphism/qou-motivic-galois-instance.lean
and left the block's .ts and .md in place. Exactly one .lean under a content
directory was deleted in that window, and it is this one.
`qouMotivicGaloisChar` now exists nowhere in the Lean tree.

The refactor's own reasoning is right and is not in question — encoding the
obstruction as a class field 'forced every instance to either prove it or
launder an axiom', which is the §Axiomatization-is-NOT-a-Proof rule. What is
left over is the CONTENT block describing an instance that deliberately no
longer exists.

NOT FIXED HERE because the disposition is an authoring call, not a mechanical
one, and it is the same author's refactor. Three options:
  a) delete the block, if the instance was its whole subject;
  b) demote it from `definition` (which REQUIRES a Lean sibling per the
     type system) to `remark`/`prose` interpreting the new standalone
     theorem;
  c) retarget `lean.ref` at the standalone theorem the same commit created,
     if the block's claim survives the demotion.

Timeline note: this is NOT from PR #5384. The sibling .lean was present at
that branch's tip 13bd56a35e, where run-validate was green at
'✓ Valid — 27 issue(s)'; 73a21ac34a landed among the 162 commits main gained
before the rebase-merge.

CLOSED 2026-08-22. main validates green again: '✓ Valid — 27 issue(s)', 0
errors, on a clean checkout.

Disposition chosen by the owner: option A, demote def: -> rem:. The block
asserted a formalized instance the corpus no longer carries — its .lean was
the axiom-laundering instance 73a21ac34a deleted — so the claim was withdrawn
rather than re-backed.

NOT retargeted at MotivicPerpetualObstructionFromTrace.lean, which the
block's own .md names as where the formalization went. Those theorems
conclude 'not IsUnit (4 : Z)' and 'not IsUnit (-32 : Z)', whose types mention
neither p nor S; pointing a definition at them would have recorded it as
formalized by something saying nothing about it. Separate bean qou-lrnd,
where p-dependent replacements have since landed.

Cascade handled: 6 references across 4 files repointed, QA sidecar label and
kind updated, foreshadows.json regenerated (514 blocks, 878 derived). All
three blocks' interprets targets resolve; find-dangling-remarks flags none.
