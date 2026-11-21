import Mathlib.Data.Real.Basic
import Mathlib.Topology.Instances.Real.Lemmas
import Mathlib.Topology.Order.IntermediateValue

/-!
# QOU.BraidKnot.UnstableAtom.decay_channel — uniquely-determined decay channel

The violated constraint γ*(K, q) is well-defined off the boundary
variety (where two shadow prices agree), and an atom that is stable at `q₁`
and unstable at `q₂` crosses the boundary variety in between.

LaTeX: `\label{prop:unstable-atom-decay-channel}`

## 2026-08-31 — the ref pointed past this file, and the file it pointed at was empty

This sibling used to say:

> *"The **substantive** Lean encoding (the `DecayChannelContext` class plus
> the `decay_channel` conditional result) lives at the **canonical library
> path** `QOU/BraidKnot/UnstableAtom/decay_channel.lean`."*

Two things were wrong with that.

**It cannot be reached.**  Per AGENTS.md §0a, a block's `lean.ref` resolves to
the **sibling first**, and this sibling exists — so `lean.ref =
qou:QOU.BraidKnot.UnstableAtom.decay_channel` resolved here, to a file that
declared `decay_channel_unique` and no `decay_channel` at all.  The prose
declared the library canonical while resolution sent every reader here.

**It was not substantive.**  The library `DecayChannelContext` carried `Z`,
`N`, `q`, `PartitionIdx`, `lam_star`, `E_lambda`, `on_boundary`, `lam_alt`,
`q_1`, `q_2` **and** all three manuscript sub-claims as its own fields, and
`decay_channel` returned the three claim fields as a triple.  `on_boundary :=
fun _ => True` makes sub-claim (ii) vacuous, `q_1 := 1, q_2 := 0` makes (iii)
vacuous, `E_lambda := 1` discharges (i) — so a `[DecayChannelContext]` binder
assumed nothing (AGENTS.md §3b-cond item 5; bean `qou-z9ws`).  The library
file is gutted and this one carries the encoding, under the name the ref
actually names.

**And sub-claim (iii) is derivable, not axiomatic.**  *"Stable at `q₁`,
unstable at `q₂` implies `∃ q* ∈ [q₁, q₂]` with `E(λ*, q*) = 0`"* is the
intermediate value theorem for a continuous energy: the manuscript's own
Connection-to-phase-boundary paragraph is an IVT argument.  It is proved
below from `ContinuousOn` and a sign change, rather than assumed.

## What is NOT encoded, stated rather than implied

- **Sub-claim (i), well-definedness of `λ*`.**  The manuscript derives it by
  running the LP relaxation, taking the optimal vertex and rounding.  The
  library encoded it as the bare field `E_lambda ≠ 0`, which is neither that
  argument nor a consequence of it.  Nothing here constructs the LP, its
  vertex, or the `arg min`; existence of the violated constraint is assumed
  wherever it is needed.
- **The LP-duality selection input.**  That off the boundary variety any
  energy-minimising partition equals `lam_star` is
  `prop:mass-coefficient-shadow-price`, taken as a hypothesis.
- **The boundary variety itself.**  `OnBoundary` is an opaque predicate; that
  it is `{q : ∃ λ₁ ≠ λ₂, |y_{λ₁}(q)| = |y_{λ₂}(q)|}` and has measure zero is
  not encoded, so "generically" is not formalised.
- **Continuity of `E(λ*, ·)`** is a hypothesis of the crossing result, not a
  theorem.  The manuscript does not establish it either.
-/

namespace QOU.BraidKnot.UnstableAtom

/-- **Uniqueness of the decay channel off the boundary variety** (manuscript
sub-claim (ii)).

Given the LP-duality selection input — off the boundary variety, every
partition minimising the constraint-violation energy equals `lamStar` — any
two energy-minimising partitions coincide.

Every object is a **parameter**: the partition index type, the minimiser
predicate, the boundary predicate and the selected channel are the caller's,
so the hypothesis constrains the caller's data rather than data an instance
chose.  The conclusion is not the hypothesis: it is the two-sided
consequence, reached by composing the selection input with itself through
`lamStar`. -/
-- Ref: [leitner2026] prop:mass-coefficient-shadow-price (the LP-duality input)
-- Ref: [leitner2026] braids-and-knots/local-shadow-ordering
theorem decay_channel_unique {ι : Type*}
    (lamStar : ι) (IsMinimiser : ι → Prop) (OnBoundary : ℝ → Prop) (q : ℝ)
    (hsel : ¬ OnBoundary q → ∀ lam : ι, IsMinimiser lam → lam = lamStar)
    (hoff : ¬ OnBoundary q)
    (lam₁ lam₂ : ι) (h₁ : IsMinimiser lam₁) (h₂ : IsMinimiser lam₂) :
    lam₁ = lam₂ :=
  (hsel hoff lam₁ h₁).trans (hsel hoff lam₂ h₂).symm

/-- **Phase-boundary crossing** (manuscript sub-claim (iii)).

An atom stable at `q₁` and unstable at `q₂` crosses a `q*` where the
constraint-violation energy of the violated channel vanishes.

**Derived, by the intermediate value theorem.**  The manuscript's
Connection-to-phase-boundary paragraph *is* an IVT argument — "necessarily
crosses a `q* ∈ [q₁, q₂]` where `E(λ*, q*) = 0`" — and it is proved here
rather than carried as an axiom, which is what the previous encoding did.

Continuity of `E` on `[q₁, q₂]` is a hypothesis; neither this file nor the
manuscript establishes it. -/
-- Ref: [leitner2026] prop:unstable-atom-decay-channel §Connection to phase boundary
theorem phase_boundary_crossing (E : ℝ → ℝ) (q₁ q₂ : ℝ) (hq : q₁ ≤ q₂)
    (hcont : ContinuousOn E (Set.Icc q₁ q₂))
    (hstable : E q₁ ≤ 0) (hunstable : 0 ≤ E q₂) :
    ∃ qStar ∈ Set.Icc q₁ q₂, E qStar = 0 := by
  have hmem : (0 : ℝ) ∈ Set.Icc (E q₁) (E q₂) := ⟨hstable, hunstable⟩
  obtain ⟨qStar, hqStar, hE⟩ := intermediate_value_Icc hq hcont hmem
  exact ⟨qStar, hqStar, hE⟩

/-- **Decay channel of an unstable atom**
([`prop:unstable-atom-decay-channel`]).

Off the boundary variety the violated constraint `λ*` is unique, and an atom
whose constraint-violation energy changes sign across `[q₁, q₂]` crosses the
boundary variety inside it.

Both conjuncts are derived.  This is the declaration the block's `lean.ref`
names; until 2026-08-31 the ref resolved to this file and this file did not
declare it. -/
-- Ref: [leitner2026] prop:unstable-atom-decay-channel
theorem decay_channel {ι : Type*}
    (lamStar : ι) (IsMinimiser : ι → Prop) (OnBoundary : ℝ → Prop)
    (E : ℝ → ℝ) (q q₁ q₂ : ℝ)
    (hsel : ¬ OnBoundary q → ∀ lam : ι, IsMinimiser lam → lam = lamStar)
    (hoff : ¬ OnBoundary q)
    (hq : q₁ ≤ q₂) (hcont : ContinuousOn E (Set.Icc q₁ q₂))
    (hstable : E q₁ ≤ 0) (hunstable : 0 ≤ E q₂) :
    (∀ lam₁ lam₂ : ι, IsMinimiser lam₁ → IsMinimiser lam₂ → lam₁ = lam₂) ∧
      (∃ qStar ∈ Set.Icc q₁ q₂, E qStar = 0) :=
  ⟨fun lam₁ lam₂ h₁ h₂ =>
      decay_channel_unique lamStar IsMinimiser OnBoundary q hsel hoff
        lam₁ lam₂ h₁ h₂,
   phase_boundary_crossing E q₁ q₂ hq hcont hstable hunstable⟩

end QOU.BraidKnot.UnstableAtom
