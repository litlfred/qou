/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Algebra.FreeAlgebra
import Mathlib.Data.Matrix.Basic
import Mathlib.RingTheory.Bialgebra.Basic
import Mathlib.RingTheory.TensorProduct.Basic

/-!
# The matrix-coefficient bialgebra: one construction behind the corpus coproducts

For a finite index type `n` and a commutative ring `R`, the free algebra on the
symbols `u i j` carries the **matrix-coefficient coproduct**

  `Δ (u i j) = ∑ k, u i k ⊗ u k j`,  `ε (u i j) = if i = j then 1 else 0`.

This file proves it is a bialgebra (`instBialgebra`), with no hypothesis beyond
`[CommRing R]`: no field, no order, no analysis, no axiom.

It is the Tannaka coend of one object `V` with `τ V = Rⁿ` together with its tensor
powers: the matrix coalgebra `End(Rⁿ)^*` spans the degree-one part, and the free
algebra is what the tensor product of `V`-powers adds. Dividing by a bi-ideal (for
instance the RTT relations of a braiding `c_{V,V}`) keeps the bialgebra; that is
the FRT construction.

## Matrix-type coproducts on presented algebras

An algebra `A` with a matrix `M : Matrix n n A` receives `π = lift M` from the free
algebra. A coproduct `Δ` on `A` **is the matrix-coefficient coproduct for `M`**
(`IsMatrixCoproduct`) when `Δ ∘ π = (π ⊗ π) ∘ Δ_free`. This is checked on
generators (`isMatrixCoproduct_iff`), and when the entries of `M` generate `A`,
it determines `Δ` (`IsMatrixCoproduct.unique`). The corpus instances are in
`QOU/LiftingDescent/MatrixCoefficientCoproducts.lean`.

-- Ref: [kassel1995] Kassel, *Quantum Groups*, GTM 155, §VIII.6 (FRT construction)
   and Ch. XI (reconstruction). https://doi.org/10.1007/978-1-4612-0783-2
-/

namespace QOU.Coproduct

open TensorProduct

noncomputable section

variable (R : Type*) [CommRing R] (n : Type*) [Fintype n] [DecidableEq n]

/-- The free algebra on the matrix-coefficient symbols `u i j`. -/
abbrev MatCoeff : Type _ := FreeAlgebra R (n × n)

variable {n}

/-- The generator `u i j`. -/
abbrev u (i j : n) : MatCoeff R n := FreeAlgebra.ι R (i, j)

variable (n)

/-- The matrix-coefficient coproduct `Δ (u i j) = ∑ k, u i k ⊗ u k j`. -/
def matComul : MatCoeff R n →ₐ[R] MatCoeff R n ⊗[R] MatCoeff R n :=
  FreeAlgebra.lift R fun p => ∑ k, u R p.1 k ⊗ₜ[R] u R k p.2

/-- The counit `ε (u i j) = δ i j`. -/
def matCounit : MatCoeff R n →ₐ[R] R :=
  FreeAlgebra.lift R fun p => if p.1 = p.2 then 1 else 0

variable {R n}

omit [DecidableEq n] in
@[simp] theorem matComul_u (i j : n) :
    matComul R n (u R i j) = ∑ k, u R i k ⊗ₜ[R] u R k j := by
  simp [matComul]

omit [Fintype n] in
@[simp] theorem matCounit_u (i j : n) :
    matCounit R n (u R i j) = if i = j then 1 else 0 := by
  simp [matCounit]

omit [DecidableEq n] in
theorem matComul_coassoc :
    (Algebra.TensorProduct.assoc R R (MatCoeff R n) (MatCoeff R n) (MatCoeff R n)).toAlgHom.comp
      ((Algebra.TensorProduct.map (matComul R n) (.id R _)).comp (matComul R n))
      = (Algebra.TensorProduct.map (.id R _) (matComul R n)).comp (matComul R n) := by
  apply FreeAlgebra.hom_ext
  funext ⟨i, j⟩
  simp only [Function.comp_apply, AlgHom.coe_comp, matComul_u, map_sum,
    Algebra.TensorProduct.map_tmul, AlgHom.id_apply, AlgEquiv.toAlgHom_eq_coe,
    AlgHom.coe_coe, sum_tmul, tmul_sum, Algebra.TensorProduct.assoc_tmul]
  exact Finset.sum_comm

theorem matCounit_rTensor :
    (Algebra.TensorProduct.map (matCounit R n) (.id R _)).comp (matComul R n)
      = (Algebra.TensorProduct.lid R (MatCoeff R n)).symm := by
  apply FreeAlgebra.hom_ext
  funext ⟨i, j⟩
  simp [ite_tmul]

theorem matCounit_lTensor :
    (Algebra.TensorProduct.map (.id R _) (matCounit R n)).comp (matComul R n)
      = (Algebra.TensorProduct.rid R R (MatCoeff R n)).symm := by
  apply FreeAlgebra.hom_ext
  funext ⟨i, j⟩
  simp [tmul_ite]

/-- **The matrix-coefficient bialgebra**, over any commutative ring. -/
instance instBialgebra : Bialgebra R (MatCoeff R n) :=
  Bialgebra.ofAlgHom (matComul R n) (matCounit R n)
    matComul_coassoc matCounit_rTensor matCounit_lTensor

/-! ## Matrix-type coproducts on a presented algebra -/

variable {A : Type*} [Ring A] [Algebra R A]

/-- The algebra map `MatCoeff R n → A` sending `u i j` to `M i j`. -/
def present (M : Matrix n n A) : MatCoeff R n →ₐ[R] A :=
  FreeAlgebra.lift R fun p => M p.1 p.2

omit [Fintype n] [DecidableEq n] in
@[simp] theorem present_u (M : Matrix n n A) (i j : n) :
    present (R := R) M (u R i j) = M i j := by
  simp [present]

/-- `Δ` is **the matrix-coefficient coproduct for `M`**: `Δ ∘ π = (π ⊗ π) ∘ Δ_free`
with `π = present M`. -/
def IsMatrixCoproduct (M : Matrix n n A) (Δ : A →ₐ[R] A ⊗[R] A) : Prop :=
  Δ.comp (present M) =
    (Algebra.TensorProduct.map (present M) (present M)).comp (matComul R n)

/-- `ε` is the matrix-coefficient counit for `M`: `ε ∘ π = ε_free`. -/
def IsMatrixCounit (M : Matrix n n A) (ε : A →ₐ[R] R) : Prop :=
  ε.comp (present M) = matCounit R n

omit [DecidableEq n] in
/-- The matrix condition is checked on generators: `Δ (M i j) = ∑ k, M i k ⊗ M k j`. -/
theorem isMatrixCoproduct_iff (M : Matrix n n A) (Δ : A →ₐ[R] A ⊗[R] A) :
    IsMatrixCoproduct M Δ ↔ ∀ i j, Δ (M i j) = ∑ k, M i k ⊗ₜ[R] M k j := by
  constructor
  · intro h i j
    have := congrArg (fun f => f (u R i j)) h
    simpa [map_sum] using this
  · intro h
    apply FreeAlgebra.hom_ext
    funext ⟨i, j⟩
    simpa [map_sum] using h i j

omit [Fintype n] in
theorem isMatrixCounit_iff (M : Matrix n n A) (ε : A →ₐ[R] R) :
    IsMatrixCounit M ε ↔ ∀ i j, ε (M i j) = if i = j then 1 else 0 := by
  constructor
  · intro h i j
    simpa using congrArg (fun f => f (u R i j)) h
  · intro h
    apply FreeAlgebra.hom_ext
    funext ⟨i, j⟩
    simpa using h i j

omit [DecidableEq n] in
/-- **Uniqueness.** When the entries of `M` generate `A`, at most one coproduct on `A`
is the matrix-coefficient coproduct for `M`. -/
theorem IsMatrixCoproduct.unique {M : Matrix n n A}
    (hM : Function.Surjective (present (R := R) M)) {Δ₁ Δ₂ : A →ₐ[R] A ⊗[R] A}
    (h₁ : IsMatrixCoproduct M Δ₁) (h₂ : IsMatrixCoproduct M Δ₂) : Δ₁ = Δ₂ := by
  ext a
  obtain ⟨x, rfl⟩ := hM a
  exact (congrArg (fun f => f x) h₁).trans (congrArg (fun f => f x) h₂).symm

omit [Fintype n] in
theorem IsMatrixCounit.unique {M : Matrix n n A}
    (hM : Function.Surjective (present (R := R) M)) {ε₁ ε₂ : A →ₐ[R] R}
    (h₁ : IsMatrixCounit M ε₁) (h₂ : IsMatrixCounit M ε₂) : ε₁ = ε₂ := by
  ext a
  obtain ⟨x, rfl⟩ := hM a
  exact (congrArg (fun f => f x) h₁).trans (congrArg (fun f => f x) h₂).symm

end

end QOU.Coproduct
