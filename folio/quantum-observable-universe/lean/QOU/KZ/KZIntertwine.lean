import QOU.KZ.KZFunctorial
import QOU.KZ.KZHexagonCentral
import QOU.KZ.KZShiftPhi
import Mathlib.Analysis.Matrix

/-!
# The KZ associator intertwines

Stage S2 prerequisite of bean `qou-zoyv`. This is naturality of the associator for morphisms
between *different* tensor powers. Let `T : U → U'` intertwine the residues: `T A = A' T`,
`T B = B' T`. Then `T Φ(A, B) = Φ(A', B') T` (`Φ_intertwine`).

The proof places `A ⊕ A'`, `B ⊕ B'` in the block algebra `End(U ⊕ U')`. There the
off-diagonal `T` commutes with both residues, hence with `Φ(A ⊕ A', B ⊕ B')`
(`KZHexagonCentral.commute_Φ`). Functoriality (`KZFunctorial.map_Φ`) for the block-diagonal
embedding and the two projections of the product algebra shows that this associator is
`Φ(A, B) ⊕ Φ(A', B')`. Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S2)
-/

noncomputable section

namespace QOU.KZ.KZIntertwine

open QOU.KZ.FuchsianFormal QOU.KZ.KZPentagon

section Product

variable {R R' : Type*} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R]
  [NormedRing R'] [NormedAlgebra ℂ R'] [CompleteSpace R']

omit [NormedAlgebra ℂ R] [CompleteSpace R] [NormedAlgebra ℂ R'] [CompleteSpace R'] in
theorem nonResonant_prod {A : R} {A' : R'} (hA : NonResonant A) (hA' : NonResonant A') :
    NonResonant ((A, A') : R × R') := by
  intro k hk
  have e : indicial ((A, A') : R × R') k = Prod.map (indicial A k) (indicial A' k) := by
    funext X; ext <;> simp [indicial, ad]
  rw [e]
  exact (hA k hk).prodMap (hA' k hk)

theorem Φ_prod (A B : R) (A' B' : R') (hA : NonResonant A) (hB : NonResonant B)
    (hA' : NonResonant A') (hB' : NonResonant B') :
    Φ ((A, A') : R × R') (B, B') (nonResonant_prod hA hA') (nonResonant_prod hB hB') =
      (Φ A B hA hB, Φ A' B' hA' hB') := by
  ext
  · exact KZFunctorial.map_Φ (AlgHom.fst ℂ R R') continuous_fst ((A, A') : R × R') (B, B')
      (nonResonant_prod hA hA') (nonResonant_prod hB hB') hA hB
  · exact KZFunctorial.map_Φ (AlgHom.snd ℂ R R') continuous_snd ((A, A') : R × R') (B, B')
      (nonResonant_prod hA hA') (nonResonant_prod hB hB') hA' hB'

end Product

section Blocks

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

variable {ι ι' : Type*} [Fintype ι] [DecidableEq ι] [Fintype ι'] [DecidableEq ι']

/-- The product algebra `End U × End U'`. -/
abbrev PR (ι ι' : Type*) [Fintype ι] [DecidableEq ι] [Fintype ι'] [DecidableEq ι'] :=
  Matrix ι ι ℂ × Matrix ι' ι' ℂ

/-- The block-diagonal embedding `End U × End U' → End(U ⊕ U')` (stated with the normed-ring
instances, so that `KZFunctorial.map_Φ` applies without an expensive instance unification). -/
def blockDiag : @AlgHom ℂ (PR ι ι') (Matrix (ι ⊕ ι') (ι ⊕ ι') ℂ) _
    (NormedRing.toRing (α := PR ι ι')).toSemiring
    (NormedRing.toRing (α := Matrix (ι ⊕ ι') (ι ⊕ ι') ℂ)).toSemiring
    (NormedAlgebra.toAlgebra (𝕜 := ℂ) (𝕜' := PR ι ι'))
    (NormedAlgebra.toAlgebra (𝕜 := ℂ) (𝕜' := Matrix (ι ⊕ ι') (ι ⊕ ι') ℂ)) where
  toFun p := Matrix.fromBlocks p.1 0 0 p.2
  map_one' := Matrix.fromBlocks_one
  map_mul' p q := by simp [Matrix.fromBlocks_multiply]
  map_zero' := by simp
  map_add' p q := by simp [Matrix.fromBlocks_add]
  commutes' r := by
    simp only [Algebra.algebraMap_eq_smul_one]
    ext (i | i) (j | j) <;> simp [Matrix.one_apply]

theorem blockDiag_apply (p : PR ι ι') :
    blockDiag p = Matrix.fromBlocks p.1 0 0 p.2 := rfl

/-- **The associator intertwines.** If `T A = A' T` and `T B = B' T`, then
`T Φ(A, B) = Φ(A', B') T`. Non-resonance is needed for the residues and for their block sums. -/
theorem Φ_intertwine (A B : Matrix ι ι ℂ) (A' B' : Matrix ι' ι' ℂ) (T : Matrix ι' ι ℂ)
    (hTA : T * A = A' * T) (hTB : T * B = B' * T)
    (hA : NonResonant A) (hB : NonResonant B) (hA' : NonResonant A') (hB' : NonResonant B')
    (hDA : NonResonant (Matrix.fromBlocks A 0 0 A'))
    (hDB : NonResonant (Matrix.fromBlocks B 0 0 B')) :
    T * Φ A B hA hB = Φ A' B' hA' hB' * T := by
  have hDA' : NonResonant (blockDiag ((A, A') : PR ι ι')) := by
    rw [blockDiag_apply]; exact hDA
  have hDB' : NonResonant (blockDiag ((B, B') : PR ι ι')) := by
    rw [blockDiag_apply]; exact hDB
  have hmap := KZFunctorial.map_Φ blockDiag
    (LinearMap.continuous_of_finiteDimensional blockDiag.toLinearMap) ((A, A') : PR ι ι') (B, B')
    (nonResonant_prod hA hA') (nonResonant_prod hB hB') hDA' hDB'
  rw [Φ_prod A B A' B' hA hB hA' hB', blockDiag_apply,
    KZShiftPhi.Φ_congr (blockDiag_apply _) (blockDiag_apply _) hDA' hDB' hDA hDB] at hmap
  set Toff : Matrix (ι ⊕ ι') (ι ⊕ ι') ℂ := Matrix.fromBlocks 0 0 T 0
  have cA : Commute Toff (Matrix.fromBlocks A 0 0 A') := by
    show Toff * _ = _ * Toff
    simp [Toff, Matrix.fromBlocks_multiply, hTA]
  have cB : Commute Toff (Matrix.fromBlocks B 0 0 B') := by
    show Toff * _ = _ * Toff
    simp [Toff, Matrix.fromBlocks_multiply, hTB]
  have hc := (KZHexagonCentral.commute_Φ hDA hDB cA cB).eq
  have e : Φ (Matrix.fromBlocks A 0 0 A') (Matrix.fromBlocks B 0 0 B') hDA hDB =
      Matrix.fromBlocks (Φ A B hA hB) 0 0 (Φ A' B' hA' hB') := hmap.symm
  rw [e] at hc
  simp only [Toff, Matrix.fromBlocks_multiply, Matrix.zero_mul, Matrix.mul_zero, add_zero,
    zero_add] at hc
  exact (Matrix.fromBlocks_inj.1 hc).2.2.1

/-- **`exp` intertwines.** If `T A = A' T` then `T e^{A} = e^{A'} T`. -/
theorem exp_intertwine (A : Matrix ι ι ℂ) (A' : Matrix ι' ι' ℂ) (T : Matrix ι' ι ℂ)
    (hT : T * A = A' * T) :
    T * NormedSpace.exp ℂ A = NormedSpace.exp ℂ A' * T := by
  have hpow : ∀ n : ℕ, T * A ^ n = A' ^ n * T := by
    intro n
    induction n with
    | zero => simp
    | succ n ih => rw [pow_succ, ← Matrix.mul_assoc, ih, Matrix.mul_assoc, hT, ← Matrix.mul_assoc,
        pow_succ]
  let Lm : Matrix ι ι ℂ →ₗ[ℂ] Matrix ι' ι ℂ :=
    { toFun := fun M => T * M, map_add' := Matrix.mul_add T, map_smul' := fun r M =>
        Matrix.mul_smul T r M }
  let Rm : Matrix ι' ι' ℂ →ₗ[ℂ] Matrix ι' ι ℂ :=
    { toFun := fun M => M * T, map_add' := fun M N => Matrix.add_mul M N T,
      map_smul' := fun r M => Matrix.smul_mul r M T }
  have hL : Continuous Lm := LinearMap.continuous_of_finiteDimensional Lm
  have hR : Continuous Rm := LinearMap.continuous_of_finiteDimensional Rm
  rw [NormedSpace.exp_eq_tsum, NormedSpace.exp_eq_tsum]
  have e1 : T * (∑' n : ℕ, ((n.factorial : ℂ))⁻¹ • A ^ n) =
      ∑' n : ℕ, T * (((n.factorial : ℂ))⁻¹ • A ^ n) :=
    (NormedSpace.expSeries_summable' (𝕂 := ℂ) A).map_tsum Lm hL
  have e2 : (∑' n : ℕ, ((n.factorial : ℂ))⁻¹ • A' ^ n) * T =
      ∑' n : ℕ, (((n.factorial : ℂ))⁻¹ • A' ^ n) * T :=
    (NormedSpace.expSeries_summable' (𝕂 := ℂ) A').map_tsum Rm hR
  rw [e1, e2]
  exact tsum_congr fun n => by rw [Matrix.mul_smul, hpow, Matrix.smul_mul]

end Blocks

end QOU.KZ.KZIntertwine
