import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Module.LinearMap.Basic
import Mathlib.Algebra.Module.End

/-!
# QOU.BraidKnot.WeakSpectralCompleteness

Plancherel completeness for the EW/Higgs {T(2,4), T(2,6), T(2,8)} idempotent decomposition.

LaTeX label: `conj:weak-spectral-completeness`

## Conjectural content

Conjectural Plancherel completeness: the three torus-knot idempotents T(2,4), T(2,6), T(2,8) span the EW/Higgs sector irrep decomposition.

## Status

Class-axiomatised per CLAUDE.md §3b-cond. The conjecture sits in
the residual §3b-violator cone identified in
[`AUDIT-DEEP-2026-05.md`](../../../../AUDIT-DEEP-2026-05.md) §1A
(P1.b sweep). Class declaration here lets downstream
provable-kind blocks (in the same `uses[]` cone) become
`conditional-on-class` rather than violators.

`sorry` in any concrete instance is understood as **conjecture**,
not missing proof. Downstream blocks may take `[WeakSpectralCompleteness]` as an
explicit `[Instance]` hypothesis to retain
`theorem` / `proposition` status under §3b-cond.

## References

- [manuscript] §Plancherel completeness for the EW/Higgs {T(2,4), T(2,6), T(2,8)} idempotent decomposition, `conj:weak-spectral-completeness`
-/

namespace QOU.BraidKnot

/-- **Conjecture class** for `conj:weak-spectral-completeness`,
    operator-level form.

    Parameterised by a base ring `R` (the Hecke-algebra coefficient
    ring) and an EW/Higgs sector `R`-module `EWModule`.  The
    conjecture asserts the three torus-knot Plancherel idempotents
    `e_T_2_4`, `e_T_2_6`, `e_T_2_8` are pairwise-orthogonal
    idempotents of `EWModule` whose sum is the identity (Plancherel
    completeness for the {T(2,4), T(2,6), T(2,8)} idempotent
    decomposition of the EW/Higgs sector). -/
class WeakSpectralCompleteness (R : Type*) [Ring R] (EWModule : Type*)
    [AddCommGroup EWModule] [Module R EWModule] where
  /-- Idempotent projector for the T(2,4) torus knot. -/
  e_T_2_4 : Module.End R EWModule
  /-- Idempotent projector for the T(2,6) torus knot. -/
  e_T_2_6 : Module.End R EWModule
  /-- Idempotent projector for the T(2,8) torus knot. -/
  e_T_2_8 : Module.End R EWModule
  /-- Each `e_T_{2,2k}` is idempotent. -/
  is_idempotent_24 : e_T_2_4 ∘ₗ e_T_2_4 = e_T_2_4
  is_idempotent_26 : e_T_2_6 ∘ₗ e_T_2_6 = e_T_2_6
  is_idempotent_28 : e_T_2_8 ∘ₗ e_T_2_8 = e_T_2_8
  /-- Pairwise orthogonality: `e_i ∘ e_j = 0` for distinct `i ≠ j`. -/
  orthogonal_24_26 : e_T_2_4 ∘ₗ e_T_2_6 = 0
  orthogonal_24_28 : e_T_2_4 ∘ₗ e_T_2_8 = 0
  orthogonal_26_28 : e_T_2_6 ∘ₗ e_T_2_8 = 0
  /-- Plancherel completeness: the three idempotents sum to the
      identity on the EW/Higgs sector. -/
  spans : e_T_2_4 + e_T_2_6 + e_T_2_8 = LinearMap.id

/-- **Structural skeleton** of `conj:weak-spectral-completeness`
    (kept for `uses` cone bookkeeping under §3b-cond — see CLAUDE.md).
    A `WeakSpectralCompleteness R EWModule` instance implies the
    skeleton via the writhe assignment `4, 6, 8`. -/
class WeakSpectralCompletenessSkeleton : Prop where
  three_torus_writhes : ∃ (w : Fin 3 → ℕ),
    w 0 = 4 ∧ w 1 = 6 ∧ w 2 = 8 ∧ Function.Injective w

instance instWeakSpectralCompletenessSkeleton
    {R : Type*} [Ring R] {EWModule : Type*}
    [AddCommGroup EWModule] [Module R EWModule]
    [WeakSpectralCompleteness R EWModule] :
    WeakSpectralCompletenessSkeleton where
  three_torus_writhes := by
    refine ⟨![4, 6, 8], rfl, rfl, rfl, ?_⟩
    intro i j hij
    fin_cases i <;> fin_cases j <;> simp_all

end QOU.BraidKnot
