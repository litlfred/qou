---
# qou-lo1t
title: 'VACUITY drain batch 1: self-assuming-projection bulk (118 genuine remaining)'
status: todo
type: task
priority: normal
created_at: 2026-08-22T21:28:27Z
updated_at: 2026-08-23T08:06:35Z
---

## Batch 2 (2026-08-23) — Instanton.lean cluster, 4 defects

Two dispositions, and a **detector limitation** worth recording.

**2 re-adjudicated genuine -> legit.** `kernelIncl_exact` and
`categorical_jet_prolongation` project fields of `CategoricalJet` /
`CategoricalJetProlongation` — but those are STRUCTURES DEFINING AN OBJECT,
whose fields are the definition's own axioms (exactness; the prolongation
commuting square). The theorems are universally quantified over the structure,
i.e. the standard Lean field-accessor idiom — exactly Mathlib's
`mul_assoc := Group.mul_assoc`.

**The detector cannot tell these apart from real defects.** A definition's
accessor and a conjecture-carrier's conclusion projection are *syntactically
identical* — both are `:= x.field` where the field type is the conclusion.
The discriminator is semantic: does the structure DEFINE an object (fields =
axioms of the definition) or ASSERT a result (field = the claim)? Likely a
meaningful fraction of the remaining genuine queue is this false-positive
class; worth a triage pass before treating the count as a work-list.

**2 fixed — circular instances removed.** `categorical_irreducible` and
`categorical_dq_squared_nonvanishing` had inhabitation routes that started
from their own conclusions:
- `hasCategoricalIrreducibility_of_subsingleton` took
  `[Subsingleton ((𝟙_C) ⟶ adjointObj)]` — the conclusion verbatim — and
  returned `⟨hsub⟩`.
- `hasDqSquaredNonvanishing_of_fact` produced the class from
  `[Fact (dq ≫ dq ≠ 0)]`, ignoring all three of the class's hypotheses
  (`hq`, `hd_sq`, `hcross`) that the theorem binds — so the statement read
  as a substantive conditional while none of them was load-bearing.
Both removed (0 external refs each); the classes are now honest open carriers.

**A ledger evidence correction.** `categorical_irreducible`'s recorded
evidence said 'UNINHABITED carrier … no instance exists'. That was **wrong** —
the instance existed at line 120. The defect was circularity, not absence.
