---
# qou-006b
title: 'GAP: BringZeroModeBlochClass quantifies over the opaque BlochWigner_unit_circle; the Bloch class [Z] on Bring''s surface is not identified'
status: todo
type: task
priority: normal
tags:
    - gap
    - reorg-2026-10-04
    - 8f-lean
    - 8f-open
    - lean
created_at: 2026-09-03T09:08:30Z
updated_at: 2026-10-10T07:56:52Z
parent: qou-8lxd
---

Advisory from the SM-surface Lean sweep (bean qou-08zf, 2026-09-03); not changed. lean/QOU/Archimedean/EmCouplingBringZeroMode.lean imports QOU.Archimedean.BlochWignerUnitCircle, where BlochWigner_unit_circle is declared "noncomputable opaque (_θ : ℝ) : ℝ" — an unconstrained function. The conjecture class BringZeroModeBlochClass has a single field, ∃ θ, BlochWigner_unit_circle θ = 2/(3π), which is therefore unfalsifiable as stated; against the Clausen definition in BlochWignerMathlibFiller it would be true by the intermediate value theorem (2/(3π) ≈ 0.212 lies in the range of Cl₂), which is not the open claim either. The open claim is the identification of the specific Bloch-group class [Z] from the Yekutieli triple on {T(2,9), T(3,5)} whose τ_arch-image is 2/(3π).

NEXT HONEST STEP: pin the field to the group-homology pairing the file's own docstring describes (pairing the Euler/volume class with the fundamental 2-cycle of Bring's surface), or carry the angle θ as an explicit parameter of the class with the identification as the field. No instance exists; none should be added. Recorded as an advisory entry in docs/audits/lean-vacuity-review-ledger.json.


## Triaged 2026-10-10 — OPEN Lean work, not mechanical; tagged `8f-open`

Read as part of working the `8f-lean` front. The bean's "NEXT HONEST STEP" is to
restructure a conjecture class — pin the field to the group-homology pairing its
own docstring describes, or carry the angle as an explicit class parameter. That
is formalisation, not a repair, and it needs a judgement about what the claim
asserts.

**The trap it documents is worth restating**, because it is the reason this
cannot be closed by making the Lean compile: the single field
`exists θ, BlochWigner_unit_circle θ = 2/(3π)` is **unfalsifiable as stated**,
since `BlochWigner_unit_circle` is `noncomputable opaque (_θ : ℝ) : ℝ` — an
unconstrained function. Against the real Clausen definition it would instead be
**true by the intermediate value theorem** (`2/(3π) ≈ 0.212` lies in the range of
`Cl₂`). Neither reading is the open claim, which is the identification of the
specific Bloch-group class from the Yekutieli triple on `{T(2,9), T(3,5)}`.

So a green Lean file here would mean nothing either way. The bean's instruction
stands: **no instance exists; none should be added.**
