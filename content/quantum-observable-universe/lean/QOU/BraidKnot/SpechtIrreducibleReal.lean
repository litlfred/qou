import QOU.BraidKnot.SpechtIrreducibleCore

/-!
# QOU.BraidKnot.SpechtIrreducibleReal — Specht irreducibility over an ordered field

Over a a linearly ordered field (in particular `ℝ` and `ℚ`) the `M^μ` form
`⟨f, g⟩ = Σ_d f_d g_d` is **positive-definite** (the tabloid basis is orthonormal),
so its restriction to `S^μ` is automatically non-degenerate — *no hook-length Gram
determinant needed*. Combined with the (now sorry-free) James submodule theorem
`SpechtIrreducibleCore.specht_submodule_dichotomy'`, this gives a **fully
sorry-free** proof that `S^μ` is irreducible over any ordered field.

This closes the second B1 core (`specht_form_nondegenerate`) over ordered fields;
the general characteristic-zero case (e.g. `ℂ`) still needs the integral Gram
determinant (positive over `ℝ`, hence a nonzero integer, hence invertible in any
char-0 field) — that base-change is out of scope here.

| Declaration | Status |
|---|---|
| `bilinM_self_eq_zero` (positive-definiteness) | **sorry-free** |
| `specht_form_nondegenerate_ordered` (`S^μ ⊓ (S^μ)ᗮ = ⊥`) | **sorry-free** |
| `specht_isSimple_ordered` (irreducibility over an ordered field) | **sorry-free** |
-/

open scoped BigOperators

namespace QOU.BraidKnot.SpechtIrreducibleReal

open QOU.BraidKnot
open QOU.BraidKnot.Specht
open QOU.BraidKnot.SpechtIrreducible
open Equiv (Perm)

variable {k : Type} [Field k] [LinearOrder k] [IsStrictOrderedRing k]
variable {μ : YoungDiagram}

/-- **Positive-definiteness.** `⟨f, f⟩ = Σ_d f_d² = 0 ⟹ f = 0`. -/
theorem bilinM_self_eq_zero {f : Mtab (k := k) μ} (h : bilinM (k := k) μ f f = 0) :
    f = 0 := by
  rw [bilinM_apply, Finsupp.sum] at h
  have hnn : ∀ d ∈ f.support, (0 : k) ≤ f d * f d := fun d _ => mul_self_nonneg _
  rw [Finset.sum_eq_zero_iff_of_nonneg hnn] at h
  ext d
  simp only [Finsupp.coe_zero, Pi.zero_apply]
  by_cases hd : d ∈ f.support
  · rcases mul_eq_zero.1 (h d hd) with h' | h' <;> exact h'
  · exact Finsupp.not_mem_support_iff.1 hd

/-- **Non-degeneracy of the form on `S^μ`** over an ordered field. -/
theorem specht_form_nondegenerate_ordered (μ : YoungDiagram) :
    SpechtSubmodule (k := k) μ ⊓ spechtPerp (k := k) μ = ⊥ := by
  rw [eq_bot_iff]
  intro x hx
  rw [Submodule.mem_inf] at hx
  obtain ⟨hxS, hxP⟩ := hx
  rw [Submodule.mem_bot]
  apply bilinM_self_eq_zero
  exact (mem_spechtPerp_iff (k := k) μ x).1 hxP x hxS

/-- **Irreducibility of `S^μ` over an ordered field** — fully sorry-free.
Reproduces the brick-2 statement `QOU.BraidKnot.Specht.specht_isSimple` over any
`LinearOrderedField`, with no remaining `sorry`: the dichotomy is
`SpechtIrreducibleCore.specht_submodule_dichotomy'` (proved) and non-degeneracy is
positive-definiteness. -/
theorem specht_isSimple_ordered (μ : YoungDiagram) :
    ∀ N : Submodule k (Mtab (k := k) μ),
      N ≤ SpechtSubmodule (k := k) μ →
      (∀ σ : Perm (Fin (nOf μ)), ∀ x ∈ N, Mtab.rep μ σ x ∈ N) →
      N = ⊥ ∨ N = SpechtSubmodule (k := k) μ := by
  intro N hN_le hN_stable
  rcases SpechtIrreducibleCore.specht_submodule_dichotomy' (k := k) μ N hN_stable with hsub | hperp
  · exact Or.inr (le_antisymm hN_le hsub)
  · left
    rw [eq_bot_iff, ← specht_form_nondegenerate_ordered (k := k) μ]
    exact le_inf hN_le hperp

end QOU.BraidKnot.SpechtIrreducibleReal
