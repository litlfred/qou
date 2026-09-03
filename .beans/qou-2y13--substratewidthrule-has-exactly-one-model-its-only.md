---
# qou-2y13
title: SubstrateWidthRule has exactly one model — its only Prop field pins its data to a constant
status: completed
type: bug
priority: normal
created_at: 2026-08-24T19:38:42Z
updated_at: 2026-08-24T21:04:07Z
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


## Resolved 2026-08-24 — parameterised and given an `iff`, rather than deleted

**Consumers before the change: 3 mentions of `SubstrateWidthRule`, all inside
`QOU/MassTheory/CableWidthBraneTowerLift.lean`** — the class, the `colorRule`
instance, and the single binder on `level_is_H9_of_rule`. Nothing imports this
module (`grep -rln '^import QOU.MassTheory.CableWidthBraneTowerLift'` → empty),
so the blast radius is one file.

**Departure from the bean's disposition, deliberately.** The bean's cheapest fix
was "delete the class and the conditional theorem, keep `derived_level_A3`". I
kept the seam and parameterised instead, because the seam is the part worth
having and the deletion throws away the one genuinely content-bearing statement
in the neighbourhood:

- `class SubstrateWidthRule (w : ℕ → ℕ) : Prop` now takes the width as a
  **parameter**, with `is_color` as its only field. The bean's condition ("if the
  class is wanted as a seam, `is_color` must go") is met differently and, I think,
  better: `is_color` can stay because it no longer pins a field the class owns —
  it constrains a width somebody else names. `[SubstrateWidthRule w]` is now
  falsifiable, which it was not.
- Proved pair: `colorRule` (satisfiable, at `fun _ => cableWidthColor`) beside
  `not_widthRule_of_ne` and `not_widthRule_width_four` (`¬ SubstrateWidthRule
  (fun _ => 4)`). A width-4 cable is exactly the family the file's own
  `lift_is_coefficient_ratio` argument rules out, so the non-model is meaningful
  in context rather than arbitrary.
- **`level_A3_eq_nine_iff (w) : jointTraceStrands 3 (w 3) = 9 ↔ w 3 =
  cableWidthColor`** — new, no class involved. This is the honest form of "the
  level is derived from the width": falsifiable in both directions, and it says
  strictly more than either `derived_level_A3` or `level_is_H9_of_rule`.
- `level_is_H9_of_rule` kept but retargeted to `(w : ℕ → ℕ)
  [SubstrateWidthRule w]`, and the parenthetical *"Non-vacuous conditional: the
  level is computed from the class field, not assumed"* — the sentence the bean
  told me to disbelieve — is **deleted**, with the reason written in its place.

**Not disputed, per the bean.** Whether `cableWidthColor = 3` is derived from
SU(3) colour content rather than fitted is a claim about the physics, argued in
the file header, and this change does not touch it. The docstring now says so
explicitly, so the next sweep does not re-open it as a Lean defect.

**Verification.** Fresh `lean` on `CableWidthBraneTowerLift` — exit 0, no
warnings (the file had none before either). `#print axioms` on all five
new/retargeted decls: four depend on nothing, `level_A3_eq_nine_iff` on
`[propext, Classical.choice, Quot.sound]` (from `omega`). No `sorryAx`. No
`sorry` in committed work.
