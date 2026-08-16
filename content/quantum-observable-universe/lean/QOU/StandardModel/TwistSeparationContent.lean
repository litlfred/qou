/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Tactic

/-!
# What the twist "independence" theorem actually says

Bean `qou-7dzg` (V6, follow-up). Companion to
[`ChiralityGradingConstruction.lean`](ChiralityGradingConstruction.lean).

## The claim under test

`appendix-standard-model/strand-twist-datum.lean` carries

```
theorem exists_same_writhe_ne_totalTwist (n : ℕ) (hn : 0 < n) :
    ∃ t₁ t₂ : TwistDatum n, totalTwist t₁ ≠ totalTwist t₂
```

whose docstring reads *"over any fixed word (hence fixed writhe) there exist
framings with distinct total twist"*, and which
`conj:sm-hypercharge-invariant` leans on: the separation it advertises is what
"qualifies the datum as a candidate" for hypercharge.

But no braid word occurs in that type. Every mention of braid, writhe, or word
in that file is in a comment; its imports are `Perm.Basic`, `Fintype.Perm`,
`Tactic` — no braid group, no knot theory, no category theory. So the statement
proved is *"two `ℤ`-valued functions can have different sums"*, and whether it
supports a claim **about braids** is exactly what was never checked.

This file runs that check, by stating the claim **with the braid word in the
type** — the step the original skips.

## Result: the claim is true, and it is braid-free

`separation_at_fixed_word` is the docstring's sentence, formalised: at a *fixed*
word, two framings of that word have different total twist. It is proved for an
**arbitrary** `Word` type and an **arbitrary** `writhe : Word → ℤ`. Nothing
about braids, crossings, or the writhe is used or available — the hypotheses are
not there to be used.

`separation_holds_with_one_word` makes that concrete: instantiate `Word := Unit`,
where there is exactly **one** word and the writhe is constant. The separation
still holds. A statement that survives collapsing the braid group to a point is
not evidence about braid groups.

The reason is structural, not incidental: in this model the framing is
`Fin n → ℤ`, an arbitrary function, so it is *by construction* unconstrained by
whatever the word does. Independence is an artifact of the encoding, not a
discovered property of ribbon framings.

## The other horn

`factoring_twist_cannot_separate`: if instead the twist *is* determined by the
crossing content — as a genuine ribbon-category twist is, being canonical rather
than freely assignable — then it takes equal values on writhe-degenerate states
and separates nothing. This is the argument of
`chirality_not_a_function_of_crossing` (V9) applied to the twist.

Together the two horns are a dilemma for the hypercharge candidacy, and the
corpus needs one of them: either the twist is free — and its separating power is
put in by hand, proving nothing about the ribbon structure — or it is canonical,
and it cannot separate at all.

## Scope

Scope-(a), and narrow. This says what the existing theorem does and does not
establish; it does **not** refute `conj:sm-hypercharge-invariant`, and it does
not touch `tr_M`, whose framing is unambiguous (the writhe prefactor sits
outside the trace). A twist datum *derived* from the braid word — the open
`qou-kebu` item — is untouched by both horns, because it would be neither free
nor a function of the writhe alone.
-/

namespace QOU.StandardModel.TwistContent

variable {n : ℕ}

/-- Per-strand integer framing datum (the model used by `def:strand-twist-datum`:
an arbitrary function, unconstrained by any braid). -/
def TwistDatum (n : ℕ) : Type := Fin n → ℤ

/-- Total twist. -/
def totalTwist (t : TwistDatum n) : ℤ := ∑ i, t i

/-- **The docstring's claim, with the word in the type.**

At a *fixed* word `β`, two framings of `β` have different total twist — so the
pair is writhe-degenerate by construction (same word, hence same writhe).

Note the binders: `Word` is an arbitrary type and `writhe` an arbitrary
function, both entirely unused in the proof. That is the finding — the sentence
is provable without knowing what a braid is. -/
theorem separation_at_fixed_word {Word : Type*} (writhe : Word → ℤ) (β : Word)
    (hn : 0 < n) :
    ∃ s₁ s₂ : Word × TwistDatum n,
      s₁.1 = β ∧ s₂.1 = β ∧
      writhe s₁.1 = writhe s₂.1 ∧
      totalTwist s₁.2 ≠ totalTwist s₂.2 := by
  refine ⟨(β, fun _ => 0), (β, fun i => if i = ⟨0, hn⟩ then 1 else 0),
    rfl, rfl, rfl, ?_⟩
  have h1 : totalTwist (n := n) (fun _ => 0) = 0 := by
    simp [totalTwist]
  have h2 : totalTwist (n := n) (fun i => if i = ⟨0, hn⟩ then 1 else 0) = 1 := by
    simp [totalTwist]
  simp only [h1, h2]
  omega

/-- **The claim survives collapsing the braid group to a point.**

`Word := Unit` has one element, so there is a single word and the writhe is
constant. Separation still holds. Whatever this establishes, it is not about
braids. -/
theorem separation_holds_with_one_word (hn : 0 < n) :
    ∃ s₁ s₂ : Unit × TwistDatum n,
      (fun _ : Unit => (0 : ℤ)) s₁.1 = (fun _ : Unit => (0 : ℤ)) s₂.1 ∧
      totalTwist s₁.2 ≠ totalTwist s₂.2 := by
  obtain ⟨s₁, s₂, _, _, hw, hne⟩ :=
    separation_at_fixed_word (n := n) (fun _ : Unit => (0 : ℤ)) () hn
  exact ⟨s₁, s₂, hw, hne⟩

/-- **The other horn.**  A twist determined by the crossing content — i.e.
factoring through the writhe, as a canonical ribbon twist does — takes equal
values on writhe-degenerate states, so it separates nothing.

This is `chirality_not_a_function_of_crossing` (V9) applied to the twist: a
datum that factors through a coordinate cannot separate states sharing it. -/
theorem factoring_twist_cannot_separate
    {Word : Type*} (writhe : Word → ℤ) (T : Word → ℤ)
    (hfac : ∃ f : ℤ → ℤ, ∀ β, T β = f (writhe β))
    (β₁ β₂ : Word) (hw : writhe β₁ = writhe β₂) :
    T β₁ = T β₂ := by
  obtain ⟨f, hf⟩ := hfac
  rw [hf, hf, hw]

/-- The dilemma, as a single statement: for any candidate twist on words,
*either* it factors through the writhe — and then it is constant on
writhe-degenerate pairs, separating nothing — *or* it does not, in which case it
carries information the crossing content does not determine, and that
information was supplied by hand rather than derived. -/
theorem twist_dilemma {Word : Type*} (writhe : Word → ℤ) (T : Word → ℤ) :
    (∀ β₁ β₂, writhe β₁ = writhe β₂ → T β₁ = T β₂) ∨
    (∃ β₁ β₂, writhe β₁ = writhe β₂ ∧ T β₁ ≠ T β₂) := by
  by_cases h : ∀ β₁ β₂, writhe β₁ = writhe β₂ → T β₁ = T β₂
  · exact Or.inl h
  · push_neg at h
    obtain ⟨β₁, β₂, hw, hne⟩ := h
    exact Or.inr ⟨β₁, β₂, hw, hne⟩

end QOU.StandardModel.TwistContent
