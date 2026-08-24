---
# qou-2y13
title: SubstrateWidthRule has exactly one model — its only Prop field pins its data to a constant
status: todo
type: bug
priority: normal
created_at: 2026-08-24T19:38:42Z
updated_at: 2026-08-24T19:38:42Z
---

`QOU/MassTheory/CableWidthBraneTowerLift.lean:66-73`, verified present 2026-08-24.

```
class SubstrateWidthRule where
  w : N -> N
  is_color : forall A, w A = cableWidthColor      -- cableWidthColor := 3

instance colorRule : SubstrateWidthRule where
  w := fun _ => cableWidthColor
  is_color := fun _ => rfl
```

The class's only propositional field pins its only data field to a constant. So
`SubstrateWidthRule` has **exactly one model** (up to `funext`), `colorRule`
supplies it globally, and `[SubstrateWidthRule]` carries no information: it is
`w = fun _ => 3` spelled as a hypothesis.

## The claim this defeats

```
/-- **From the derived width rule, the A=3 level is forced to be H9** -- the
    level is *derived* from the width input, not chosen.  (Non-vacuous
    conditional: the level is computed from the class field, not assumed.) -/
theorem level_is_H9_of_rule [rule : SubstrateWidthRule] :
    jointTraceStrands 3 (rule.w 3) = 9 := by
  rw [rule.is_color]; rfl
```

The parenthetical is the part to disbelieve. Yes, the level is *computed* from
`rule.w 3` rather than assumed — but `is_color` makes `rule.w 3` equal `3` in
every model, so the computation has one possible input and `H9` was never at
risk. The theorem is `level_is_H9`, unconditionally, with a binder that
constrains nothing. Compare the honest version two lines above it:

```
theorem derived_level_A3 : jointTraceStrands 3 cableWidthColor = 9 := rfl
```

which says the same thing and does not claim to be conditional.

## Not the same finding as the surrounding prose

The file argues at length that `cableWidthColor = 3` is *derived* from SU(3)
colour content and "not chosen to hit any target". Take that at face value —
it is a claim about the physics and this bean does not dispute it. The defect is
structural: **if** the width is derived, then it is a definition, and wrapping a
definition in a one-model class and calling the result a non-vacuous conditional
is what makes the Lean read as more than it is.

## Disposition (small, and safe)

Cheapest honest fix: delete the class and the conditional theorem, keep
`derived_level_A3`. If the class is wanted as a seam for a *future* width rule
that is not constant, then `is_color` must go — a class cannot both admit
alternatives and pin its field.

**Regression note:** `checkNoVacuousInstanceData` does not flag this.
`w := fun _ => cableWidthColor` is a constant behind a lambda *and* behind a
name, and the detector matches literal tokens only — folio-assistant bean
`folio-assistant-ilbh`.
