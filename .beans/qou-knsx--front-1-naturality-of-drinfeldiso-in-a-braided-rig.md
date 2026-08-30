---
# qou-knsx
title: 'Front 1: naturality of drinfeldIso in a braided right-rigid category'
status: completed
type: task
priority: normal
created_at: 2026-08-26T16:22:41Z
updated_at: 2026-08-26T16:38:07Z
---

CLOSED 2026-08-26, sorry-free, and my own difficulty estimate was wrong.

I recorded this as needing a Whitney-move coherence proof "of the same shape as
coevaluation_evaluation_braided'". It does not. That assessment came from a probe
in which I ran simp [drinfeldIso, rightDualIso, rightAdjointMate] and read the
resulting ~20-term goal as the difficulty. The error was attacking the DEFINITION
of the mate instead of its ALGEBRA.

The proof is two lemmas Mathlib lacks, each following from lemmas it has:

  rightAdjointMate_congr_dual -- the mate does not depend on the choice of dual,
  up to rightDualIso. Both sides rewrite, via comp_rightAdjointMate with explicit
  instance arguments, to the mixed mate (one object's first dual, the other's
  second). Composing f with an identity on either side is the whole trick; it is
  the same move rightDualIso's own proof uses. Five lines, first attempt.

  swap_mate_mate -- taking the mate twice, the second time against the swapped
  pairings, is the identity. The braided form of Mathlib's Future-work entry
  "the left adjoint mate of the right adjoint mate of a morphism is the morphism
  itself". Both (f-mate)-mate and f satisfy the same identity against epsilon --
  for f by braiding naturality on each side plus rightAdjointMate_comp_evaluation
  -- and pairing against epsilon is injective, because tensorRightHomEquiv
  carries g |-> (g whiskered) >> epsilon to g >> lambda-inv.

drinfeldIso_naturality is their composite. pivotalOfBraided follows: EVERY braided
right-rigid category is pivotal, unconditional, no instance hypothesis.

Lesson worth keeping: a large goal after `simp [<definition>]` measures how big
the definition unfolds to, not how hard the theorem is.
