import QOU.MathlibExt.OctonionDerivations
import Mathlib.LinearAlgebra.FiniteDimensional.Defs

set_option maxHeartbeats 4000000

/-!
# QOU.MathlibExt.OctonionDerivationsBound — `dim Der(𝕆) = 14`

Finrank bounds on the octonion derivation space `Der𝕆` from
`QOU.MathlibExt.OctonionDerivations`.

* **Lower bound `octDer_finrank_ge : 14 ≤ dim Der𝕆`** — fully proved. The coordinate
  projection `proj𝕆` onto the 14 *free* matrix entries sends the 14 explicit derivations
  `octDer 0 .. 13` to the standard basis of `ℚ¹⁴` (`projDer_octDer`), so it is a left inverse
  of the linear-combination map `c ↦ Σ cᵢ · octDer i`, which is therefore injective;
  `LinearMap.finrank_le_finrank_of_injective` gives `14 ≤ dim`. (`octDer_linearIndependent` is
  the same fact stated as linear independence.)

* **Upper bound `octDer_finrank_le : dim Der𝕆 ≤ 14`** — the residual content. Equivalent to
  injectivity of `proj𝕆` on `Der𝕆`: a derivation is pinned by its 14 free entries, the other
  50 being forced by the Leibniz constraints. This is the classical `Der(𝕆) ≅ 𝔤₂` (dim 14);
  its explicit 50-constraint Lean certificate is left as a cited `sorry`. Everything upstream
  — the multiplication, the 14 derivations, the reduction `dim = 14 ⟺ rank = 50`, and the
  lower bound — is machine-verified.

* **`octonion_derivation_dim : dim Der𝕆 = 14`** — assembles the two bounds.

Base ring ℚ (char 0). Convention: [albuquerque-majid1999]; derivation-algebra dimension:
[baez2002] §4.1.
-/

namespace QOU.MathlibExt.OctonionDerivations

open Matrix

/-- Row indices of the 14 free matrix-entries (the kernel-pivot coordinates from Gaussian
elimination of the Leibniz-defect matrix). -/
def freeA : Fin 14 → Fin 8 := ![5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7]

/-- Column indices of the 14 free matrix-entries. -/
def freeB : Fin 14 → Fin 8 := ![1, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]

/-- Projection of an endomorphism onto its 14 *free* matrix entries
`f ↦ (t ↦ f(e_{freeB t})(freeA t))`. The 14 derivations map to the standard basis of `ℚ¹⁴`;
on `Der𝕆` it is injective (a derivation is determined by these 14 numbers). -/
def proj𝕆 : ((Fin 8 → ℚ) →ₗ[ℚ] (Fin 8 → ℚ)) →ₗ[ℚ] (Fin 14 → ℚ) where
  toFun f := fun t => f (Pi.single (freeB t) 1) (freeA t)
  map_add' f g := by funext t; simp
  map_smul' c f := by funext t; simp

@[simp] theorem proj𝕆_apply (f : (Fin 8 → ℚ) →ₗ[ℚ] (Fin 8 → ℚ)) (t : Fin 14) :
    proj𝕆 f t = f (Pi.single (freeB t) 1) (freeA t) := rfl

/-- `proj𝕆` restricted to the derivation space. -/
def projDer : Der𝕆 →ₗ[ℚ] (Fin 14 → ℚ) := proj𝕆.comp Der𝕆.subtype

/-- The 14 derivations are sent by `projDer` to the standard basis of `ℚ¹⁴`. -/
theorem projDer_octDer (i : Fin 14) : projDer (octDer i) = Pi.single i 1 := by
  funext t
  simp only [projDer, LinearMap.comp_apply, Submodule.subtype_apply, proj𝕆_apply, octDer,
    Matrix.mulVecLin_apply, Matrix.mulVec_single, MulOpposite.op_one, one_smul]
  fin_cases i <;> fin_cases t <;>
    simp only [octDerMat, freeA, freeB, Matrix.col_apply, Matrix.of_apply, Matrix.cons_val',
      Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons, Matrix.head_fin_const,
      Matrix.empty_val', Matrix.cons_val_fin_one, Matrix.cons_val, Fin.isValue,
      Pi.single_apply] <;> decide

/-- The 14 octonion derivations are linearly independent. -/
theorem octDer_linearIndependent : LinearIndependent ℚ octDer := by
  have hcomp : ⇑projDer ∘ octDer = ⇑(Pi.basisFun ℚ (Fin 14)) := by
    funext i
    rw [Function.comp_apply, projDer_octDer, Pi.basisFun_apply]
  have hli : LinearIndependent ℚ (⇑projDer ∘ octDer) := by
    rw [hcomp]; exact (Pi.basisFun ℚ (Fin 14)).linearIndependent
  exact hli.of_comp projDer

/-- **Lower bound (fully proved):** `14 ≤ dim Der(𝕆)`.

`projDer` is a left inverse of the injective linear-combination map `c ↦ Σ cᵢ · octDer i`
(`projDer_octDer` sends the derivations to the standard basis), so `ℚ¹⁴` embeds in `Der𝕆`. -/
theorem octDer_finrank_ge : 14 ≤ Module.finrank ℚ Der𝕆 := by
  haveI : FiniteDimensional ℚ (↥Der𝕆) := Submodule.finiteDimensional_of_le le_top
  -- The linear-combination map `L14 : ℚ¹⁴ → Der𝕆`, `c ↦ Σ cᵢ · octDer i`.
  let L14 : (Fin 14 → ℚ) →ₗ[ℚ] Der𝕆 := ∑ i, (LinearMap.proj i).smulRight (octDer i)
  -- `projDer` is a left inverse of `L14`, hence `L14` is injective.
  have hsec : ∀ c, projDer (L14 c) = c := by
    intro c
    have hLc : L14 c = ∑ i, c i • octDer i := by
      simp [L14, LinearMap.sum_apply, LinearMap.smulRight_apply, LinearMap.proj_apply]
    rw [hLc, map_sum]
    funext t
    rw [Finset.sum_apply]
    simp only [map_smul, projDer_octDer, Pi.smul_apply, Pi.single_apply, smul_eq_mul, mul_ite,
      mul_one, mul_zero]
    rw [Finset.sum_ite_eq]
    simp
  have hinj : Function.Injective L14 := by
    intro a b hab
    have ha := hsec a; rw [hab, hsec b] at ha; exact ha.symm
  have hle := L14.finrank_le_finrank_of_injective hinj
  simpa using hle

/-- **Upper bound:** `dim Der(𝕆) ≤ 14`. Equivalent to injectivity of `proj𝕆` on `Der𝕆` — a
derivation is determined by its 14 free entries, the other 50 being forced by the Leibniz
constraints (the classical `Der(𝕆) ≅ 𝔤₂`). The reduction and lower bound above are proved;
this direction's explicit 50-constraint certificate is the remaining formalization step. -/
theorem octDer_finrank_le : Module.finrank ℚ Der𝕆 ≤ 14 := by
  -- Reduces to `Function.Injective projDer` via `LinearMap.finrank_le_finrank_of_injective`
  -- (the 50 pivot entries of a derivation are the row-space certificate of the rank-50
  -- Leibniz-defect matrix; injectivity of `projDer` is the classical `Der(𝕆) ≅ 𝔤₂`).
  -- Ref: [baez2002] "The Octonions" §4.1 (Der(𝕆) ≅ 𝔤₂, dim 14).
  sorry

/-- **`dim Der(𝕆) = 14`** — the octonion derivation algebra is the 14-dimensional compact
`𝔤₂`. The lower bound and the rank–nullity reduction are machine-verified; the upper bound is
conditional on the classical `Der(𝕆) ≅ 𝔤₂` (`octDer_finrank_le`). -/
theorem octonion_derivation_dim : Module.finrank ℚ Der𝕆 = 14 :=
  le_antisymm octDer_finrank_le octDer_finrank_ge

end QOU.MathlibExt.OctonionDerivations
