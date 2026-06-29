import QOU.BraidKnot.SpechtStandardBasis
import Mathlib.Data.Nat.Lattice

/-!
# QOU.BraidKnot.SpechtSpanningCore — reduction of brick-4's spanning stub

`QOU.BraidKnot.SpechtStandardBasis.standardPolytabloid_straightening` is the
spanning half of the standard-basis theorem for Specht modules (Sagan,
*The Symmetric Group*, §2.6): every polytabloid `e_t` (arbitrary tableau `t`)
lies in the span of the *standard* polytabloids `{e_{sytToTableau T} : T ∈ SYT(μ)}`.

This module is an **independent** reduction of *that same statement* (it imports
`SpechtStandardBasis` read-only and modifies nothing). It peels the entire
**well-founded-recursion** scaffolding off the straightening obligation —
sorry-free — and isolates the irreducible content as a single, recursion-free,
**one-step** core:

> `polytabloid_garnir_core` — there is a measure `wt : Tableau μ → ℕ` such that
> for every *non-standard* tableau `t` (one not of the form `sytToTableau T`),
> the polytabloid `e_t` is a `k`-combination of polytabloids `e_{t'}` of
> **strictly smaller measure**. This is exactly Sagan's §2.6 Garnir / straightening
> step: a single Garnir relation rewrites `e_t` into more-dominant polytabloids,
> and `wt` is an order-reversing rank in (a linear extension of) the dominance
> order, so the rewrite strictly decreases it.

From the one-step core, the full span statement follows by **strong induction on
the measure** — supplied here sorry-free by a general, self-contained lever
(`span_of_measure_step`) that the pinned Mathlib lacks (it has no
"measure-decreasing rewrites land in the terminal set" span lemma; a natural
upstream candidate). The lever works over any module.

## sorry-free ↔ stubbed map

| Declaration | Status |
|---|---|
| `span_of_measure_step` (the strong-induction span lever) | **sorry-free** |
| `polytabloid_garnir_core` (Sagan §2.6 — the single combinatorial core) | **STUB** `sorry` — `-- Ref: [sagan2001]` §2.6 |
| `standardPolytabloid_straightening'` (verbatim brick-4 target) | **sorry-free MODULO the single core** |

`#print axioms standardPolytabloid_straightening'` confirms `sorryAx` enters only
through `polytabloid_garnir_core`; the lever + the range/image bridge are
`[propext, Classical.choice, Quot.sound]`.

This module carries 1 honest `sorry` target, so — like brick 4's `SpechtStandardBasis`
itself — it is intentionally **not** imported by the `QOU.BraidKnot` umbrella. It
reproduces the `standardPolytabloid_straightening` statement as a separate,
reduction-bearing theorem (the standard one-way dependency: `SpechtStandardBasis`
cannot import this file).

## References
- [sagan2001] Sagan, *The Symmetric Group*, §2.6 (the straightening algorithm:
  Garnir relations rewrite any polytabloid as a ℤ-combination of standard
  polytabloids, terminating in the dominance order).
- [james1984representation] James, *The Representation Theory of the Symmetric
  Groups*, §8 (the standard basis / Garnir relations).
-/

open scoped BigOperators

namespace QOU.BraidKnot.SpechtSpanningCore

open QOU.BraidKnot
open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtStandardBasis

/-! ## 1. The strong-induction span lever (sorry-free, general)

A general module fact absent from the pinned Mathlib: if a family `v : ι → M`
admits a `ℕ`-measure `wt` under which every non-terminal index `i` (those with
`¬ P i`) has `v i` in the span of *strictly-smaller-measure* members, then **every**
`v i` lies in the span of the **terminal** members `v '' {j | P j}`. Proof: strong
induction on `wt i`. -/

theorem span_of_measure_step {ι : Type*} {M : Type*} {R : Type*}
    [Semiring R] [AddCommMonoid M] [Module R M]
    (v : ι → M) (wt : ι → ℕ) (P : ι → Prop)
    (step : ∀ i, ¬ P i →
      v i ∈ Submodule.span R {x | ∃ j, wt j < wt i ∧ x = v j}) :
    ∀ i, v i ∈ Submodule.span R (v '' {j | P j}) := by
  have key : ∀ n, ∀ i, wt i = n → v i ∈ Submodule.span R (v '' {j | P j}) := by
    intro n
    induction n using Nat.strong_induction_on with
    | _ n IH =>
      intro i hi
      by_cases hP : P i
      · exact Submodule.subset_span ⟨i, hP, rfl⟩
      · have hsub : {x | ∃ j, wt j < wt i ∧ x = v j} ⊆
            (Submodule.span R (v '' {j | P j}) : Set M) := by
          rintro x ⟨j, hj, rfl⟩
          exact IH (wt j) (hi ▸ hj) j rfl
        exact (Submodule.span_le.mpr hsub) (step i hP)
  exact fun i => key (wt i) i rfl

/-! ## 2. The single combinatorial core (one cited `sorry`) -/

variable {k : Type} [Field k] [CharZero k]
variable {μ : YoungDiagram}

omit [CharZero k] in
/-- **STUB — the irreducible Garnir / straightening core (Sagan §2.6).** There is
a measure `wt : Tableau μ → ℕ` under which every *non-standard* tableau `t` (one
*not* equal to any `sytToTableau T`) has its polytabloid `e_t` expressed as a
`k`-combination of polytabloids `e_{t'}` of **strictly smaller** measure.

This bundles exactly the straightening content: a single Garnir relation rewrites
`e_t` into a combination of more-dominant polytabloids, and `wt` is an
order-reversing rank in a linear extension of the dominance order (so "more
dominant" ⟹ strictly smaller `wt`). From it, the full spanning statement follows
sorry-free via `span_of_measure_step`. -/
theorem polytabloid_garnir_core :
    ∃ wt : Specht.Tableau μ → ℕ,
      ∀ t : Specht.Tableau μ,
        (∀ T : StandardYoungTableau μ, sytToTableau T ≠ t) →
        Specht.polytabloid (k := k) t ∈
          Submodule.span k
            {x | ∃ t', wt t' < wt t ∧ x = Specht.polytabloid (k := k) t'} := by
  -- Ref: [sagan2001] §2.6 (Garnir relations / straightening algorithm: every
  -- polytabloid is a ℤ-combination of standard polytabloids, terminating in the
  -- dominance order). See also [james1984representation] §8. The irreducible
  -- spanning core of brick 4, with the well-founded recursion peeled off.
  sorry

/-! ## 3. The spanning statement (sorry-free modulo the single core) -/

omit [CharZero k] in
/-- **Brick-4 spanning half, reduced.** Verbatim restatement of
`SpechtStandardBasis.standardPolytabloid_straightening`, proved **sorry-free
modulo** the single core `polytabloid_garnir_core` (the well-founded recursion is
discharged by `span_of_measure_step`, and the terminal-set ↔ standard-range
identification is the image/range bridge). -/
theorem standardPolytabloid_straightening' :
    ∀ t : Specht.Tableau μ,
      Specht.polytabloid (k := k) t ∈
        Submodule.span k (Set.range (standardPolytabloid (k := k) (μ := μ))) := by
  obtain ⟨wt, hcore⟩ := polytabloid_garnir_core (k := k) (μ := μ)
  intro t
  have hlever :
      Specht.polytabloid (k := k) t ∈
        Submodule.span k
          (Specht.polytabloid (k := k) ''
            {s : Specht.Tableau μ | ∃ T : StandardYoungTableau μ, sytToTableau T = s}) :=
    span_of_measure_step (R := k) (M := Specht.Mtab (k := k) μ)
      (v := Specht.polytabloid (k := k)) (wt := wt)
      (P := fun s => ∃ T : StandardYoungTableau μ, sytToTableau T = s)
      (fun s hs => hcore s (fun T hT => hs ⟨T, hT⟩)) t
  refine Submodule.span_mono ?_ hlever
  rintro _ ⟨s, ⟨T, rfl⟩, rfl⟩
  exact ⟨T, rfl⟩

end QOU.BraidKnot.SpechtSpanningCore
