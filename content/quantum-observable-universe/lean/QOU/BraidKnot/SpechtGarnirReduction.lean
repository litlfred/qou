import QOU.BraidKnot.SpechtGarnirSplit
import QOU.BraidKnot.SpechtGarnirWt

/-!
# QOU.BraidKnot.SpechtGarnirReduction — the straightening core, reduced to dominance

This is the capstone of the Garnir-machinery chain. It assembles
`SpechtGarnirSplit.polytabloid_mem_span_shuffled` (over a char-0 field,
`e_t ∈ span{e_{σ·t} : σ ∈ S_X ∖ C_t}`, modulo the two-column row bound) with the
column-dominance measure `SpechtGarnirWt.colWt`, reducing the brick-4 straightening
core to a **single combinatorial statement**:

> `polytabloid_mem_span_colWt_of_decrease` — if, for a Garnir set `X` of `t`
> (with the row bound), **every** shuffle `σ ∈ S_X ∖ C_t` strictly increases column
> dominance (`colWt (σ·t) < colWt t`), then `e_t ∈ span{e_s : colWt s < colWt t}`.

No explicit transversal is needed: the full-group split already isolates exactly
the non-trivial cosets `σ ∈ S_X ∖ C_t`, and `colPattern (σ·t) = colPattern t ∘ σ⁻¹`
is constant on cosets of `S_X ∩ C_t`. Combined with the strong-induction span lever
`SpechtSpanningCore.span_of_measure_step` (using `colWt` as the measure), the **only**
remaining input to close `polytabloid_garnir_core` is the existence, for every
non-standard `t`, of such a Garnir set `X` whose shuffles are all column-dominance
strict — i.e. the `A∪B`-from-violation construction plus the column-dominance Garnir
lemma. Everything algebraic and order-theoretic is now in place, sorry-free.
-/

open scoped BigOperators

namespace QOU.BraidKnot.SpechtGarnirReduction

open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtGarnirCore
open QOU.BraidKnot.SpechtGarnirSplit
open QOU.BraidKnot.SpechtGarnirWt
open Equiv (Perm)

variable {k : Type} [Field k] [CharZero k]
variable {μ : YoungDiagram}

/-- **The straightening core, reduced to column dominance.** Given a Garnir set
`X` of `t` satisfying the two-column row bound, if every shuffle `σ ∈ S_X ∖ C_t`
strictly increases column dominance (`colWt (σ·t) < colWt t`), then `e_t` lies in
the span of strictly-smaller-`colWt` polytabloids — exactly the one-step
hypothesis of `SpechtSpanningCore.polytabloid_garnir_core` (with `wt = colWt`). -/
theorem polytabloid_mem_span_colWt_of_decrease {X : Finset (Fin (nOf μ))}
    {t : Tableau μ} {m : ℕ} (hcard : m < X.card)
    (hbound : ∀ π : colStab t, ∀ l ∈ X,
      rowPattern ((π : Perm (Fin (nOf μ))) • t) l < m)
    (hdom : ∀ σ : suppSubgroup (μ := μ) X,
      (σ : Perm (Fin (nOf μ))) ∉ colStab t →
        colWt ((σ : Perm (Fin (nOf μ))) • t) < colWt t) :
    polytabloid (k := k) t ∈ Submodule.span k
      {x | ∃ s : Tableau μ, colWt s < colWt t ∧ x = polytabloid (k := k) s} := by
  have hsub :
      {x | ∃ σ : suppSubgroup (μ := μ) X,
          (σ : Perm (Fin (nOf μ))) ∉ colStab t ∧
            x = polytabloid (k := k) ((σ : Perm (Fin (nOf μ))) • t)}
        ⊆ {x | ∃ s : Tableau μ, colWt s < colWt t ∧ x = polytabloid (k := k) s} := by
    rintro _ ⟨σ, hσ, rfl⟩
    exact ⟨(σ : Perm (Fin (nOf μ))) • t, hdom σ hσ, rfl⟩
  exact Submodule.span_mono hsub (polytabloid_mem_span_shuffled (k := k) hcard hbound)

end QOU.BraidKnot.SpechtGarnirReduction
