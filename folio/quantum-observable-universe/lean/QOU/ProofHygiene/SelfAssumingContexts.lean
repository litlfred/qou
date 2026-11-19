/-
Copyright (c) 2026 litlfred. All rights reserved.

# The self-assuming context patterns are provably contentless

The Lean vacuity ledger (`docs/audits/lean-vacuity-review-ledger.json`) records four
patterns whose common defect is that the context class **carries its own conclusion** —
`proof-decoy-hypothesis` (13), `field-projection` (22), `exact-field-projection` (2) and
`tuple-projection` (11): **48 live `genuine` entries between them**. A fifth,
`prop-universe-field`, is worse still; it is covered by the criterion here and
*demonstrated* in `docs/audits/` rather than in this file (see the closing section for
why). The ledger records each as prose, per entry, with a heuristic
verdict. This file states the criterion once and proves that every one of those shapes
meets it, and that the genuine §3b-cond conditional shape does not.

Counts are of entries whose recorded `file_sha` still matches the file on disk, so stale
verdicts are excluded — 44 of the ledger's 149 `genuine` entries are stale and at least
four of those are demonstrably already fixed (bean `qou-wsx3`).

**The criterion** is `Contentless K C : Nonempty K ↔ C` — the class is inhabited exactly
when the conclusion holds, so instantiating it is logically identical to assuming `C`,
however the conclusion is extracted (projection, application, or a chain of either). Its
negation is the reviewer's test: **exhibit an instance without already having the
conclusion** (`not_contentless_of_witness`).

The subtlest of the four is the decoy-hypothesis shape, because it extracts by
*application*. A context class

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

-- Ref: [leitner2026] docs/audits/lean-vacuity-review-ledger.json (`proof-decoy-hypothesis`)
-/
import Mathlib.Tactic

namespace QOU.ProofHygiene

/-! ## The criterion

All four of the ledger's self-assuming patterns — `proof-decoy-hypothesis`,
`field-projection` (22), `exact-field-projection` (2), `tuple-projection` (11),
**48 live `genuine` entries between them** — are instances of one property, and it is worth naming because it
is checkable rather than aesthetic. -/

/-- **A context class is contentless for `C` when it is inhabited exactly when `C` holds.**

Instantiating such a class is then logically identical to assuming `C`, whatever the
class's fields are named and however the conclusion is extracted from them — by a
projection, by an application, or by a chain of either.

The negation is the practical test, and it is the one a reviewer can actually run:
**exhibit an instance without already having the conclusion** (`not_contentless_of_witness`). -/
def Contentless (K : Sort*) (C : Prop) : Prop := Nonempty K ↔ C

/-! **🛑 Contentless is not automatically a defect — read this before applying it.**

A **conjecture carrier** is *supposed* to be contentless for its conjecture. That is what
AGENTS.md §3b means by *"the class instance is the conjectural witness (sorry =
conjecture), not a missing proof"*: assuming the class is meant to be exactly assuming the
conjecture, and `Nonempty K ↔ C` is the correct semantics, not a finding.

The defect is a **theorem** that extracts `C` from such a carrier and is then presented,
named, or cited as though `C` had been *derived*. The ledger's own wording for the
`field-projection` entries makes the same distinction: *"a projection like this is the
legitimate Mathlib accessor idiom ONLY when something builds the bundle"* — i.e. when the
carrier is inhabited by real mathematics somewhere, rather than never inhabited at all.

So the criterion below answers *"does this class carry content?"*. It does **not** by
itself answer *"is this declaration wrong?"*. For that, ask the two questions the ledger
asks: **is anything ever going to inhabit the carrier**, and **is a downstream declaration
presenting the projection as a derivation?**

The one case that is unconditionally a defect regardless of intent is the bare-`Prop`-field
carrier (closing section) — there, the carrier asserts nothing *even as a conjecture*, so
it cannot serve as a conjectural witness either. -/

/-- **The reviewer's test.** If the class can be instantiated while the conclusion fails,
it is not contentless — it carries something. Contrapositively, a class you can only
instantiate by already having `C` proves nothing about `C`. -/
theorem not_contentless_of_witness {K : Sort*} {C : Prop}
    (hK : Nonempty K) (hC : ¬ C) : ¬ Contentless K C := by
  intro h
  exact hC (h.mp hK)

/-- **The bluntest shape: a field of the conclusion's own type**, with the "theorem"
`ctx.claim`. This is `proof-field-projection` / `exact-field-projection`, and it is what
AGENTS.md §3b-cond item 5 calls a *"vacuous self-assuming projection"* — stated there in
prose, machine-checked here. -/
structure SelfAssumingContext (C : Prop) where
  /-- The conclusion, carried as a hypothesis. -/
  claim : C

theorem selfAssuming_contentless (C : Prop) : Contentless (SelfAssumingContext C) C := by
  constructor
  · rintro ⟨ctx⟩; exact ctx.claim
  · intro hC; exact ⟨⟨hC⟩⟩

/-- **The tuple shape**: several conclusions bundled, the "theorem" projecting one out.
This is `proof-tuple-projection`. Bundling does not dilute the defect — the class is
inhabited iff *both* hold, so it is contentless for the conjunction, and projecting either
component is still assuming it. -/
structure TupleContext (C D : Prop) where
  /-- First conclusion, carried as a hypothesis. -/
  fst : C
  /-- Second conclusion, likewise. -/
  snd : D

theorem tuple_contentless (C D : Prop) : Contentless (TupleContext C D) (C ∧ D) := by
  constructor
  · rintro ⟨ctx⟩; exact ⟨ctx.fst, ctx.snd⟩
  · rintro ⟨hC, hD⟩; exact ⟨⟨hC, hD⟩⟩

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

/-- The decoy shape in the criterion's vocabulary: contentless, like the projection and
tuple shapes, despite extracting its conclusion by application rather than projection. -/
theorem decoy_contentless (C : Prop) : Contentless (DecoyContext C) C :=
  decoy_nonempty_iff C

/-- **The named premise carries no logical weight.** Given the conclusion, a decoy context
exists with any inhabited premise `P` — so `bloch_suslin`, `peter_weyl_holds` and the rest are decor.
The apparent content of these declarations lives in the *name*, not in the Lean. -/
theorem decoy_premise_irrelevant {C : Prop} (hC : C) (P : Prop) (hP : P) :
    ∃ ctx : DecoyContext C, ctx.premise = P :=
  ⟨⟨P, hP, fun _ => hC⟩, rfl⟩

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

/-- **A genuine conditional class is NOT contentless for the conclusion**, witnessed at
`H = C = False` — it is inhabited there while the conclusion fails. This is the reviewer's
test (`not_contentless_of_witness`) run on the shape that should pass it. -/
theorem conditional_not_contentless :
    ¬ Contentless (ConditionalContext False False) False :=
  not_contentless_of_witness ⟨⟨fun h => h⟩⟩ (fun h => h)

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

/-! ## The bare-`Prop`-field carrier — worse than self-assuming, and demonstrated elsewhere

`proof-claims-unencoded` / `prop-universe-field`. The ledger states the defect the same
way in every instance:

> *"Every field of this carrier is typed bare `: Prop` — the UNIVERSE of propositions, not
> a proposition. An instance therefore supplies a proposition rather than a proof of one,
> so `instance := ⟨True⟩` type-checks and discharges the class, and every `[C]`-conditional
> theorem downstream is conditional on nothing."*

It is a **type-level** error rather than a judgement about intent, and it is strictly worse
than the self-assuming shapes above — those at least assert their conclusion; this one
asserts nothing *even as a conjecture*, so it cannot serve as a §3b conjectural witness
either.

**It is demonstrated in `docs/audits/`, deliberately, and not here.**

* [`2026-08-23-free-prop-field-triviality-probe.lean`](../../../../../docs/audits/2026-08-23-free-prop-field-triviality-probe.lean)
  — the original, which has priority: three real carriers reproduced verbatim, each
  discharged with `⟨True, …⟩`, and a conditional theorem shown unconditional.
* [`2026-09-12-prop-universe-carrier-shape.lean`](../../../../../docs/audits/2026-09-12-prop-universe-carrier-shape.lean)
  — the same for the abstract *shape*, plus the conjunction case (a field conjoining
  `Prop`-typed fields changes nothing, since `True ∧ True` discharges it) and the
  discriminator: `claim : Prop` is always inhabited, `claim : C` at `C = False` never is.

**Why not in this file.** `scripts/free-prop-field-audit.py` globs `content/**/*.lean`, so
a demonstration carrier placed here is by construction an instance of the very defect that
audit counts — a permanent false positive in an active drain queue (bean `qou-tsnp`). It
was here briefly and did exactly that, reported as `PropUniverseWithConjunction`,
2 fields. The `docs/audits/` convention exists for this reason and the 2026-08-23 probe
already followed it.

The criterion above still covers the pattern: such a carrier is `Contentless` for `True`,
which is the degenerate case of `Contentless K C`. -/

end QOU.ProofHygiene
