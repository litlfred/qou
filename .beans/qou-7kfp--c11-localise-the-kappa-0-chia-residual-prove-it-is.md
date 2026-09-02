---
# qou-7kfp
title: 'C11: localise the kappa_0 = chi(A) residual — prove it is exactly one equation and independent of the structural inputs'
status: completed
type: task
priority: normal
created_at: 2026-08-29T18:05:20Z
updated_at: 2026-08-29T18:09:39Z
parent: qou-ifot
---

LANDED 2026-08-29, PR #6042, commits d7a5da7355 + 369528b64d. File: content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/obstruction_residual_gap.lean. Purely ADDITIVE -- the context class is untouched, so none of its five consumers (SkeinResolutionObstruction, collatz_obstruction_link, collatz_contact_boundary, MassGapObstruction, MassGapFrontier) move. A refactor was considered and rejected: five consumers, and the wider QOU cone has no oleans here so it could not have been verified.

FINDING 1 -- the residual is EXACTLY one integer equation. The context spreads the gap over three fields. trace_pairing_cast says the pairing IS the canonical cast, which collapses hattori_stallings to the bare equation. residual_gap_iff proves the equivalence over free data (so it characterises the SHAPE, not just what an instance grants). Consequence for anyone auditing: audit hattori_stallings alone; the other two fields carry nothing.

FINDING 2 -- the structural inputs provably cannot close it. The context docstring ASSERTED this; it is now proved. gapWitness satisfies Van den Bergh CY-3 duality and Drinfeld rigidity with chi_A = 0, kappa_0 = 1. Meanwhile structuralCore_hhCohDim_two shows those same inputs DO force conclusion (a) dim HH^2 = 1 -- and needs NO axioms at all. So the block's conclusions separate sharply: (a) is derived from literature; (b),(c) rest solely on the trace computation.

core_with_gap_gives_conclusions gives the converse: supply the one equation and everything conditional follows.

ASSESSMENT RECORDED (not glossed): finding 1 puts the context close to the 3b-cond rule-5 shape -- a class carrying its own conclusion with a theorem that projects it. It is NOT a violation: conclusion (c) is the vanishing iff, while the assumed equation is a named literature input (Hattori-Stallings) which, composed with the DEFINITIONAL kappa_vanishes_def, yields it. Assuming a cited theorem and deriving from it is the intended pattern. But the margin is thin and a future reader should know.

Verified: lean-direct exit 0, clean first pass. Axioms: residual_gap_iff / context_residual_is_kappa_eq_chi [propext, Classical.choice, Quot.sound]; structuralCore_not_force_gap and core_with_gap_gives_conclusions [propext] only; structuralCore_hhCohDim_two NO axioms. No sorryAx.

WHAT REMAINS ON C11: the equation itself. Closing it needs a genuine Hochschild computation (the Connes / Hattori-Stallings pairing on the HH^2 generator), which is not in the corpus and not in Mathlib. That is now a precisely-bounded target rather than 'the remaining substrate primitives'.
