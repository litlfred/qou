import QOU.BraidKnot.SpechtGarnirCore

/-!
# QOU.BraidKnot.SpechtGarnirSplit — `e_t` in the span of shuffled polytabloids

Over a **characteristic-zero field** the integer `N = |{σ ∈ S_X : σ ∈ C_t}| ≥ 1`
of the straightening split (`SpechtGarnirCore.polytabloid_nsmul_eq_garnir_tail`)
is invertible, so the relation `N · e_t = − Σ_{σ ∈ S_X, σ ∉ C_t} sgn(σ)·e_{σ·t}`
solves for `e_t`:

> `polytabloid_mem_span_shuffled` — `e_t ∈ span_k {e_{σ·t} : σ ∈ S_X, σ ∉ C_t}`
> whenever the two-column row-index bound holds.

This is the **final algebraic reduction** of the brick-4 straightening core
`SpechtSpanningCore.polytabloid_garnir_core`: combined with a *dominance* claim
(every `σ·t` with `σ ∈ S_X ∖ C_t` is strictly more dominant than `t`, hence has
strictly smaller measure `wt`), it produces exactly the
`{x | ∃ t', wt t' < wt t ∧ x = e_{t'}}`-span membership the core asserts. The
two remaining geometric inputs — the `A ∪ B` construction supplying the bound,
and the dominance order — are all that separate this from the closed core.
-/

open scoped BigOperators

namespace QOU.BraidKnot.SpechtGarnirSplit

open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtGarnirCore
open Equiv (Perm)

variable {k : Type} [Field k] [CharZero k]
variable {μ : YoungDiagram}

/-- **`e_t` in the span of the shuffled polytabloids.** Over a characteristic-zero
field, the straightening split solves for `e_t`: it lies in the span of
`{e_{σ·t} : σ ∈ S_X, σ ∉ C_t}` whenever the two-column row-index bound holds. -/
theorem polytabloid_mem_span_shuffled {X : Finset (Fin (nOf μ))} {t : Tableau μ}
    {m : ℕ} (hcard : m < X.card)
    (hbound : ∀ π : colStab t, ∀ l ∈ X,
      rowPattern ((π : Perm (Fin (nOf μ))) • t) l < m) :
    polytabloid (k := k) t ∈ Submodule.span k
      {x | ∃ σ : suppSubgroup (μ := μ) X,
        (σ : Perm (Fin (nOf μ))) ∉ colStab t ∧ x = polytabloid (k := k) ((σ : Perm (Fin (nOf μ))) • t)} := by
  classical
  set N := (Finset.univ.filter
      (fun σ : suppSubgroup (μ := μ) X => (σ : Perm (Fin (nOf μ))) ∈ colStab t)).card with hNdef
  have hsplit := polytabloid_nsmul_eq_garnir_tail (k := k) (X := X) (t := t) hcard hbound
  -- The tail is a span member.
  have htail : (- ∑ σ ∈ Finset.univ.filter
          (fun σ : suppSubgroup (μ := μ) X => (σ : Perm (Fin (nOf μ))) ∉ colStab t),
        (Equiv.Perm.sign (σ : Perm (Fin (nOf μ))) : ℤ) •
          polytabloid (k := k) ((σ : Perm (Fin (nOf μ))) • t)) ∈
      Submodule.span k
        {x | ∃ σ : suppSubgroup (μ := μ) X,
          (σ : Perm (Fin (nOf μ))) ∉ colStab t ∧
            x = polytabloid (k := k) ((σ : Perm (Fin (nOf μ))) • t)} := by
    refine Submodule.neg_mem _ (Submodule.sum_mem _ (fun σ hσ => ?_))
    refine zsmul_mem (Submodule.subset_span ?_) _
    exact ⟨σ, (Finset.mem_filter.mp hσ).2, rfl⟩
  -- `N ≥ 1` (the identity is column-preserving), so `(N : k) ≠ 0`.
  have hNpos : 0 < N := by
    apply Finset.card_pos.mpr
    refine ⟨1, Finset.mem_filter.mpr ⟨Finset.mem_univ _, ?_⟩⟩
    show ((1 : suppSubgroup (μ := μ) X) : Perm (Fin (nOf μ))) ∈ colStab t
    rw [Subgroup.coe_one]
    exact Subgroup.one_mem _
  have hNk : (N : k) ≠ 0 := Nat.cast_ne_zero.mpr hNpos.ne'
  -- `(N : k) • e_t = N • e_t = tail ∈ span`.
  have hNe : (N : k) • polytabloid (k := k) t ∈ Submodule.span k
      {x | ∃ σ : suppSubgroup (μ := μ) X,
        (σ : Perm (Fin (nOf μ))) ∉ colStab t ∧
          x = polytabloid (k := k) ((σ : Perm (Fin (nOf μ))) • t)} := by
    rw [Nat.cast_smul_eq_nsmul, hsplit]
    exact htail
  -- Divide by `N`.
  have hsm : (N : k)⁻¹ • ((N : k) • polytabloid (k := k) t) = polytabloid (k := k) t := by
    rw [smul_smul, inv_mul_cancel₀ hNk, one_smul]
  rw [← hsm]
  exact Submodule.smul_mem _ _ hNe

end QOU.BraidKnot.SpechtGarnirSplit
