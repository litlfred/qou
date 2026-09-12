/-
Copyright (c) 2026 litlfred. All rights reserved.

# The decoy-hypothesis pattern is provably contentless

The Lean vacuity ledger (`docs/audits/lean-vacuity-review-ledger.json`) carries a
`proof-decoy-hypothesis` finding, currently **13 live `genuine` entries** across the
fluid-dynamics and appendix-surreals trees, all of one shape. A context class

```
structure FooContext where
  foo_holds_abstractly : Prop          -- a named premise
  foo_active           : foo_holds_abstractly
  impl_bar             : foo_holds_abstractly → Bar
```

with the block's "theorem" discharged as `ctx.impl_bar ctx.foo_active`.

The ledger records the finding as **prose**, per entry, with a heuristic verdict. This
file turns it into a theorem, once, for the shape rather than for any instance.

## Why the existing detectors miss it

`proof-no-self-assuming-projection` looks for a class field *of the conclusion's type*
being projected out. `DecoyContext` has **no field of type `C`** — it has a field of type
`P → C`, and the proof term `ctx.impl ctx.premise_holds` is an **application**, not a
projection. So a field-projection scan is structurally blind to it; that is recorded in
the ledger evidence for all 13 entries in nearly identical words.

## What is proved

* **`decoy_nonempty_iff`** — `Nonempty (DecoyContext C) ↔ C`. The class is inhabited
  **exactly when the conclusion holds**, so instantiating it is logically identical to
  assuming `C` outright. Everything downstream of such an instance is conditional on the
  very thing it appears to establish.
* **`decoy_premise_irrelevant`** — given `C`, the premise can be taken to be `True`. The
  named premise (`bloch_suslin`, `acoustic_horizon_formed`, `peter_weyl_holds`, …)
  carries **no** logical weight: it is decor, and the name is where the apparent content
  lives.
* **`decoy_of_false_not_inhabited`** — `¬ Nonempty (DecoyContext False)`. The pattern is
  not *universally* inhabited, which is what makes it look like it says something.

## The contrast that makes this a criterion rather than a complaint

A genuine §3b-cond conditional class is **not** of this shape, and the difference is
machine-checkable, not stylistic:

* `ConditionalContext H C` carries only `impl : H → C` — the implication, *not* the
  antecedent. `conditional_nonempty_iff`: it is inhabited iff `H → C`, which is weaker
  than `C` and is exactly what "conditional on `H`" should mean.
* **`separation`** exhibits the gap concretely at `H = C = False`:
  `Nonempty (ConditionalContext False False)` holds while `Nonempty (DecoyContext False)`
  does not. Two classes, same conclusion, opposite inhabitedness — so the shapes are
  genuinely different objects and not two spellings of one.

The operative difference is whether the class **supplies its own antecedent**. A
conditional class leaves `H` to the consumer; a decoy class asserts it (`premise_holds`)
and thereby collapses to `C`.

## What this does NOT say

* **It does not say the 13 conclusions are false, or even doubtful.** They may all be
  true, and several are plainly intended as honest §3b axiomatisations of open inputs.
  What is established is narrower and entirely about the Lean: *as structured, those
  declarations prove nothing beyond assuming their conclusions*, so they may not be cited
  as evidence for them.
* **It does not restructure any of them.** Each fix is a per-file mathematical judgement
  about what the genuine sub-hypotheses are — `Bar` derived by *composing* fields rather
  than by applying one — and that is the author's call, not a sweep to be run. The 13
  entries stay in the ledger as `genuine`; this file gives them something to cite.
* Nothing here is a fit, nothing is wired, and no existing file is modified.

Mathlib-only; no QOU imports, so this is citable from anywhere in the tree. §7c: no ring,
no archimedean construct — pure propositional logic. Sorry-free.

-- Ref: [manuscript] docs/audits/lean-vacuity-review-ledger.json (`proof-decoy-hypothesis`)
-/
import Mathlib.Tactic

namespace QOU.ProofHygiene

/-- **The decoy-hypothesis shape.** A named premise, an assertion that it holds, and an
implication into the conclusion. This is the shape of `B1TorusKnotRowsContext`,
`AcousticHorizonConditionsContext`, `DiscreteVortexSpectrumContext`,
`KelvinDispersionDerivationContext`, `QOUFluidUniverse`, `QuantumPeterWeylContext` and
the rest of the `proof-decoy-hypothesis` cluster, with the names abstracted away. -/
structure DecoyContext (C : Prop) where
  /-- The named premise — `bloch_suslin`, `acoustic_horizon_formed`, … -/
  premise : Prop
  /-- …asserted to hold, which is the step that makes the class equivalent to `C`. -/
  premise_holds : premise
  /-- …and an implication into the conclusion. -/
  impl : premise → C

/-- The pattern's "theorem": an **application**, not a projection, which is why a
field-projection scan cannot see it. -/
theorem decoy_conclusion {C : Prop} (ctx : DecoyContext C) : C :=
  ctx.impl ctx.premise_holds

/-- **The decoy class is inhabited exactly when its conclusion holds.**

So writing the class and instantiating it is logically identical to assuming `C`. The
forward direction is the pattern's own theorem; the backward direction takes the premise
to be `True`. -/
theorem decoy_nonempty_iff (C : Prop) : Nonempty (DecoyContext C) ↔ C := by
  constructor
  · rintro ⟨ctx⟩
    exact decoy_conclusion ctx
  · intro hC
    exact ⟨⟨True, trivial, fun _ => hC⟩⟩

/-- **The named premise carries no logical weight.** Given the conclusion, a decoy context
exists with premise `True` — so `bloch_suslin`, `peter_weyl_holds` and the rest are decor.
The apparent content of these declarations lives in the *name*, not in the Lean. -/
theorem decoy_premise_irrelevant {C : Prop} (hC : C) :
    ∃ ctx : DecoyContext C, ctx.premise = True :=
  ⟨⟨True, trivial, fun _ => hC⟩, rfl⟩

/-- **The pattern is not universally inhabited** — which is exactly why it looks like it
says something. At `C = False` no decoy context exists. -/
theorem decoy_of_false_not_inhabited : ¬ Nonempty (DecoyContext False) := by
  rw [decoy_nonempty_iff]
  exact id

/-- **A genuine conditional class** (§3b-cond): it carries the implication and leaves the
antecedent to the consumer. Note what is absent — there is no `H` field. -/
structure ConditionalContext (H C : Prop) where
  /-- The implication only. The antecedent `H` is the consumer's to supply. -/
  impl : H → C

/-- A conditional class is inhabited iff the implication holds — **weaker** than `C`, and
exactly what "conditional on `H`" ought to mean. -/
theorem conditional_nonempty_iff (H C : Prop) :
    Nonempty (ConditionalContext H C) ↔ (H → C) := by
  constructor
  · rintro ⟨ctx⟩; exact ctx.impl
  · intro h; exact ⟨⟨h⟩⟩

/-- **The separation.** At `H = C = False` the conditional class is inhabited and the
decoy class is not. Same conclusion, opposite inhabitedness — so the two shapes are
genuinely different objects, and "carries the implication" versus "carries the
implication *and asserts its antecedent*" is a real distinction rather than a stylistic
preference.

This is what makes `proof-decoy-hypothesis` a criterion: a reviewer can ask whether the
class supplies its own antecedent, and that question has a definite answer. -/
theorem separation :
    Nonempty (ConditionalContext False False) ∧ ¬ Nonempty (DecoyContext False) := by
  refine ⟨?_, decoy_of_false_not_inhabited⟩
  rw [conditional_nonempty_iff]
  exact id

end QOU.ProofHygiene
