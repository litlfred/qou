/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import MathlibExt.MatrixCoefficientBialgebra
import CompactQuantumMetrics.OqSU2Coproduct
import TwistedFrobeniusHopf.SweedlerJet
import QOU.LiftingDescent.TangentNoIntegral

/-!
# Three corpus coproducts are one matrix-coefficient coproduct

`MathlibExt/MatrixCoefficientBialgebra.lean` proves that `Δ (u i j) = ∑ k, u i k ⊗ u k j`
is a bialgebra on the free algebra over any commutative ring. This file shows that three
coproducts the corpus built by hand are that coproduct, pushed through a matrix of
generators, and that the matrix determines each of them.

| algebra | matrix `M` | coproduct |
|---|---|---|
| `O_q(SU(2))` | `((α, β), (γ, δ))` | `OqSU2.coprod` |
| Sweedler `H₄` | `((G, X), (0, 1))` | `Sweedler.comul`, `Sweedler.counit` |
| `k[X]` | `((1, X), (0, 1))` | `addComul` |

For each, `IsMatrixCoproduct M Δ` says `Δ ∘ π = (π ⊗ π) ∘ Δ_free` with `π (u i j) = M i j`,
and the entries of `M` generate the algebra, so `IsMatrixCoproduct.unique` says no other
coproduct has that property. In the Sweedler case the bialgebra structure already on
`H₄` makes `π` a coalgebra map.

Everything here is over a generic commutative ring, with no analysis and no axiom.
-/

namespace QOU.Coproduct

open TensorProduct

noncomputable section

/-! ## `O_q(SU(2))` -/

section OqSU2

open QOU.AlgebraicSubstrate QOU.AlgebraicSubstrate.OqSU2

variable {R : Type*} [CommRing R] (q : Rˣ)

/-- The fundamental matrix `((α, β), (γ, δ))` of `O_q(SU(2))`. -/
def oqMatrix : Matrix (Fin 2) (Fin 2) (OqSU2 R q) :=
  Matrix.of ![![α q, β q], ![γ q, δ q]]

theorem oqSU2_isMatrixCoproduct : IsMatrixCoproduct (R := R) (oqMatrix q) (coprod q) := by
  rw [isMatrixCoproduct_iff]
  intro i j
  fin_cases i <;> fin_cases j <;> simp [oqMatrix, Fin.sum_univ_two]

theorem oqSU2_present_surjective :
    Function.Surjective (present (R := R) (oqMatrix q)) := by
  have h : (present (R := R) (oqMatrix q)).comp
      (FreeAlgebra.lift R fun i : Fin 4 => ![u R 0 0, u R 0 1, u R 1 0, u R 1 1] i) =
      RingQuot.mkAlgHom R (OqSU2Rel (R := R) q) := by
    apply FreeAlgebra.hom_ext
    funext i
    fin_cases i <;> simp [oqMatrix, α, β, γ, δ, gen, oqFreeGen]
  intro a
  obtain ⟨x, rfl⟩ := RingQuot.mkAlgHom_surjective R (OqSU2Rel (R := R) q) a
  exact ⟨_, congrArg (fun f => f x) h⟩

/-- `OqSU2.coprod` is the only coproduct on `O_q(SU(2))` that is the matrix-coefficient
coproduct for `((α, β), (γ, δ))`. -/
theorem oqSU2_coprod_unique {Δ : OqSU2 R q →ₐ[R] OqSU2 R q ⊗[R] OqSU2 R q}
    (h : IsMatrixCoproduct (oqMatrix q) Δ) : Δ = coprod q :=
  IsMatrixCoproduct.unique (oqSU2_present_surjective q) h (oqSU2_isMatrixCoproduct q)

end OqSU2

/-! ## Sweedler's four-dimensional Hopf algebra -/

section Sweedler

open QOU.LiftingDescent QOU.LiftingDescent.Sweedler

variable (k : Type*) [CommRing k]

/-- The matrix `((G, X), (0, 1))`: `G` group-like, `X` skew-primitive. -/
def sweedlerMatrix : Matrix (Fin 2) (Fin 2) (Sweedler k) :=
  Matrix.of ![![G k, X k], ![0, 1]]

theorem sweedler_isMatrixCoproduct :
    IsMatrixCoproduct (R := k) (sweedlerMatrix k) (Sweedler.comul (k := k)) := by
  rw [isMatrixCoproduct_iff]
  intro i j
  fin_cases i <;> fin_cases j <;>
    simp [sweedlerMatrix, Fin.sum_univ_two, Algebra.TensorProduct.one_def, add_comm]

theorem sweedler_isMatrixCounit :
    IsMatrixCounit (R := k) (sweedlerMatrix k) (Sweedler.counit (k := k)) := by
  rw [isMatrixCounit_iff]
  intro i j
  fin_cases i <;> fin_cases j <;> simp [sweedlerMatrix]

theorem sweedler_present_surjective :
    Function.Surjective (present (R := k) (sweedlerMatrix k)) := by
  have h : (present (R := k) (sweedlerMatrix k)).comp
      (FreeAlgebra.lift k fun s : SweedlerGen => match s with
        | .g => u k 0 0
        | .x => u k 0 1) = Sweedler.mk k := by
    apply FreeAlgebra.hom_ext
    funext s
    cases s <;> simp [sweedlerMatrix, G, X]
  intro a
  obtain ⟨x, rfl⟩ := Sweedler.mk_surjective k a
  exact ⟨_, congrArg (fun f => f x) h⟩

/-- Sweedler's `Δ` is the only matrix-coefficient coproduct for `((G, X), (0, 1))`. -/
theorem sweedler_comul_unique {Δ : Sweedler k →ₐ[k] Sweedler k ⊗[k] Sweedler k}
    (h : IsMatrixCoproduct (sweedlerMatrix k) Δ) : Δ = Sweedler.comul :=
  IsMatrixCoproduct.unique (sweedler_present_surjective k) h (sweedler_isMatrixCoproduct k)

/-- `π : MatCoeff → H₄` is a coalgebra map for the bialgebra structure already on `H₄`. -/
theorem sweedler_present_comul (x : MatCoeff k (Fin 2)) :
    Coalgebra.comul (R := k) (present (R := k) (sweedlerMatrix k) x) =
      Algebra.TensorProduct.map (present (sweedlerMatrix k)) (present (sweedlerMatrix k))
        (Coalgebra.comul (R := k) x) :=
  congrArg (fun f => f x) (sweedler_isMatrixCoproduct k)

end Sweedler

/-! ## The additive coproduct on `k[X]` -/

section Additive

open Polynomial QOU.LiftingDescent

variable (k : Type*) [CommRing k]

/-- The unipotent matrix `((1, X), (0, 1))`. -/
def addMatrix : Matrix (Fin 2) (Fin 2) k[X] :=
  Matrix.of ![![1, X], ![0, 1]]

theorem addComul_isMatrixCoproduct :
    IsMatrixCoproduct (R := k) (addMatrix k) (addComul (k := k)) := by
  rw [isMatrixCoproduct_iff]
  intro i j
  fin_cases i <;> fin_cases j <;>
    simp [addMatrix, addComul, Fin.sum_univ_two, Algebra.TensorProduct.one_def, add_comm]

theorem add_present_surjective :
    Function.Surjective (present (R := k) (addMatrix k)) := by
  have h : (present (R := k) (addMatrix k)).comp (aeval (u k 0 1)) = AlgHom.id k k[X] := by
    apply Polynomial.algHom_ext
    simp [addMatrix]
  intro a
  exact ⟨aeval (u k 0 1) a, by simpa using congrArg (fun f => f a) h⟩

/-- `addComul` is the only matrix-coefficient coproduct for `((1, X), (0, 1))`. -/
theorem addComul_unique {Δ : k[X] →ₐ[k] k[X] ⊗[k] k[X]}
    (h : IsMatrixCoproduct (addMatrix k) Δ) : Δ = addComul :=
  IsMatrixCoproduct.unique (add_present_surjective k) h (addComul_isMatrixCoproduct k)

end Additive

end

end QOU.Coproduct
