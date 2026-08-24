---
# qou-09mr
title: 'Vacuous: CrystalRMatrixSubLemma.canonical picks poleIndicator to BE the function it is compared against'
status: todo
type: bug
priority: normal
created_at: 2026-08-24T19:37:08Z
updated_at: 2026-08-24T19:37:08Z
---

`QOU/BraidKnot/CrystalRMatrixSubLemma.lean:188`, verified present 2026-08-24.

```
instance canonical (R : Type u) [CommRing R] (q : R) :
    let C := CrystalGraphRealization.canonical R q
    @CrystalRMatrixSubLemma R _ q C := by
  intro C
  exact {
    poleIndicator := fun rho => decide (rho <= -1)
    pole_indicator_correct := fun _ => rfl
  }
```

The class's data field `poleIndicator` is set to the very function the
propositional field compares it against, so `pole_indicator_correct` closes by
`rfl`. Its own docstring says so out loud — *"the indicator IS the witness
function"* — and offers that as reassurance ("this instance introduces no
`sorry`"). No `sorry` is exactly the problem: there is no visible record of what
was not established, and `#print axioms` cannot contradict prose.

## Why this is not the shape qou-fngs / qou-4els already drained

Those were **constant-data** vacuity: `PUnit`, `0`, `True`. This is
**definitional laundering** — the data is a real, non-degenerate function, and it
is still chosen to make the claim reflexive. Same defect, different tell.

`qou-4els` (completed) touched this file only as a *consumer*: it demoted
`CrystalGraphRealization.canonical` and noted that `CrystalRMatrixSubLemma.canonical`
names the demoted term explicitly. It never adjudicated this instance itself.

## Also worth knowing before you pick it up

- It is still an `instance`, so `[CrystalRMatrixSubLemma R q C]` is resolved
  everywhere and any conditional theorem taking it is unconditional.
- The upstream `let C := CrystalGraphRealization.canonical R q` binds it to the
  one-point crystal that `qou-4els` demoted to a `def` — so the instance is
  pinned to the trivial realisation as well.
- **The automated vacuity detector does not see this.**
  `checkNoVacuousInstanceData` requires a degenerate *value* (`0|1|True|PUnit.unit|...`),
  and `fun rho => decide (rho <= -1)` is none of those; the fields are also inside
  a tactic-block `exact { ... }` rather than a `where`. Filed as folio-assistant
  bean **folio-assistant-ilbh**. Do not expect the detector to regress-guard this fix.

## Disposition

Same as `ConfinementGradingCorrespondence.canonical`: demote `instance` -> `def`,
keep it as a named consistency witness, and say in the docstring that the
indicator was *chosen* to satisfy the comparison, so `[CrystalRMatrixSubLemma]`
becomes a hypothesis a real R-matrix has to discharge.
