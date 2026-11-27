/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import MathlibExt.MatrixCoefficientBialgebra
import Mathlib.Algebra.RingQuot

/-!
# `U_q(sl₂)` as an algebra, its coproduct, and its matrix-coefficient form

The corpus had `U_q(sl₂)` only through its representations
(`BraidKnotOctonion/QuantumSl2Fundamental.lean`, `Rep.tensor`). This file presents the
algebra over a generic commutative ring `R`, with `q : Rˣ` and a scalar `c` standing for
`(q - q⁻¹)⁻¹`:

  `K K⁻¹ = K⁻¹ K = 1`,  `K E = q² E K`,  `K F = q⁻² F K`,  `E F = F E + c (K - K⁻¹)`.

No hypothesis on `c` is needed: the coproduct respects the relations for every `c`.

The coproduct is the corpus convention of `Rep.tensor`:
`Δ E = E ⊗ K + 1 ⊗ E`, `Δ F = F ⊗ 1 + K⁻¹ ⊗ F`, `Δ K^{±1} = K^{±1} ⊗ K^{±1}`, with
`ε E = ε F = 0`, `ε K^{±1} = 1`. `instBialgebra` proves the bialgebra axioms.

**Matrix-coefficient form.** Both Borel halves are matrix-coefficient coproducts:
`((1, E), (0, K))` and `((K⁻¹, F), (0, 1))`. Their block sum `uqMatrix` has entries
`1, E, K, K⁻¹, F`, which generate, so `Δ` is the only coproduct of matrix-coefficient type for
it (`comul_unique`). So `U_q(sl₂)`'s `Δ` is the same construction as the coproducts of
`O_q(SU(2))`, Sweedler's algebra and the additive and affine formal groups.
-/

set_option linter.unusedSectionVars false
set_option linter.unusedSimpArgs false

namespace QOU.UqSl2

open TensorProduct QOU.Coproduct

noncomputable section

variable {R : Type*} [CommRing R] (q : Rˣ) (c : R)

/-- Generators `E, F, K, K⁻¹`. -/
inductive Gen
  | E | F | K | Kinv
  deriving DecidableEq

local notation "ι" => FreeAlgebra.ι R

/-- `q²` and `q⁻²` as scalars. -/
abbrev q2 : R := ((q ^ 2 : Rˣ) : R)
abbrev q2i : R := (((q ^ 2)⁻¹ : Rˣ) : R)

/-- The defining relations. -/
inductive Rel : FreeAlgebra R Gen → FreeAlgebra R Gen → Prop
  | K_Kinv : Rel (ι .K * ι .Kinv) 1
  | Kinv_K : Rel (ι .Kinv * ι .K) 1
  | K_E : Rel (ι .K * ι .E) (q2 q • (ι .E * ι .K))
  | K_F : Rel (ι .K * ι .F) (q2i q • (ι .F * ι .K))
  | E_F : Rel (ι .E * ι .F) (ι .F * ι .E + c • (ι .K - ι .Kinv))

/-- **`U_q(sl₂)`** over `R`. -/
abbrev Uq : Type _ := RingQuot (Rel (R := R) q c)

/-- The quotient map. -/
def mk : FreeAlgebra R Gen →ₐ[R] Uq q c := RingQuot.mkAlgHom R (Rel q c)

def E : Uq q c := mk q c (ι .E)
def F : Uq q c := mk q c (ι .F)
def K : Uq q c := mk q c (ι .K)
def Kinv : Uq q c := mk q c (ι .Kinv)

theorem K_Kinv : K q c * Kinv q c = 1 := by
  simpa [K, Kinv, mk] using RingQuot.mkAlgHom_rel R (Rel.K_Kinv (q := q) (c := c))
theorem Kinv_K : Kinv q c * K q c = 1 := by
  simpa [K, Kinv, mk] using RingQuot.mkAlgHom_rel R (Rel.Kinv_K (q := q) (c := c))
theorem K_E : K q c * E q c = q2 q • (E q c * K q c) := by
  simpa [K, E, mk] using RingQuot.mkAlgHom_rel R (Rel.K_E (q := q) (c := c))
theorem K_F : K q c * F q c = q2i q • (F q c * K q c) := by
  simpa [K, F, mk] using RingQuot.mkAlgHom_rel R (Rel.K_F (q := q) (c := c))
theorem E_F : E q c * F q c = F q c * E q c + c • (K q c - Kinv q c) := by
  simpa [K, E, F, Kinv, mk] using RingQuot.mkAlgHom_rel R (Rel.E_F (q := q) (c := c))

/-! ## Maps out of `U_q(sl₂)` -/

variable {B : Type*} [Ring B] [Algebra R B]

/-- The algebra map sending `E, F, K, K⁻¹` to elements satisfying the relations. -/
def lift (e f k ki : B) (h1 : k * ki = 1) (h2 : ki * k = 1) (h3 : k * e = q2 q • (e * k))
    (h4 : k * f = q2i q • (f * k)) (h5 : e * f = f * e + c • (k - ki)) : Uq q c →ₐ[R] B :=
  RingQuot.liftAlgHom R ⟨FreeAlgebra.lift R fun g => match g with
      | .E => e | .F => f | .K => k | .Kinv => ki, by
    rintro _ _ h
    cases h <;> simp [h1, h2, h3, h4, h5]⟩

section LiftApply
variable (e f k ki : B) (h1 : k * ki = 1) (h2 : ki * k = 1) (h3 : k * e = q2 q • (e * k))
    (h4 : k * f = q2i q • (f * k)) (h5 : e * f = f * e + c • (k - ki))
@[simp] theorem lift_E : lift q c e f k ki h1 h2 h3 h4 h5 (E q c) = e := by simp [lift, E, mk]
@[simp] theorem lift_F : lift q c e f k ki h1 h2 h3 h4 h5 (F q c) = f := by simp [lift, F, mk]
@[simp] theorem lift_K : lift q c e f k ki h1 h2 h3 h4 h5 (K q c) = k := by simp [lift, K, mk]
@[simp] theorem lift_Kinv : lift q c e f k ki h1 h2 h3 h4 h5 (Kinv q c) = ki := by
  simp [lift, Kinv, mk]
end LiftApply

/-- Maps out of `U_q(sl₂)` are determined on `E, F, K, K⁻¹`. -/
theorem hom_ext {B : Type*} [Semiring B] [Algebra R B] {φ ψ : Uq q c →ₐ[R] B} (hE : φ (E q c) = ψ (E q c)) (hF : φ (F q c) = ψ (F q c))
    (hK : φ (K q c) = ψ (K q c)) (hKi : φ (Kinv q c) = ψ (Kinv q c)) : φ = ψ := by
  apply RingQuot.ringQuot_ext'
  apply FreeAlgebra.hom_ext
  funext g
  cases g
  · exact hE
  · exact hF
  · exact hK
  · exact hKi

/-! ## The coproduct and counit -/

theorem q2_mul_q2i : q2 q * q2i q = 1 := Units.mul_inv _
theorem q2i_mul_q2 : q2i q * q2 q = 1 := Units.inv_mul _

theorem E_Kinv : E q c * Kinv q c = q2 q • (Kinv q c * E q c) := by
  calc E q c * Kinv q c = Kinv q c * (K q c * E q c) * Kinv q c := by
        rw [← mul_assoc (Kinv q c), Kinv_K, one_mul]
    _ = q2 q • (Kinv q c * E q c) := by
        rw [K_E]
        simp only [mul_smul_comm, smul_mul_assoc, mul_assoc, K_Kinv, mul_one]

local notation "UU" => Uq q c ⊗[R] Uq q c

theorem comul_rel_K_E :
    (K q c ⊗ₜ[R] K q c) * (E q c ⊗ₜ[R] K q c + 1 ⊗ₜ E q c) =
      q2 q • ((E q c ⊗ₜ[R] K q c + 1 ⊗ₜ E q c) * (K q c ⊗ₜ[R] K q c)) := by
  simp only [mul_add, add_mul, Algebra.TensorProduct.tmul_mul_tmul, mul_one, one_mul, K_E,
    smul_add, ← smul_tmul', tmul_smul]

theorem comul_rel_K_F :
    (K q c ⊗ₜ[R] K q c) * (F q c ⊗ₜ[R] 1 + Kinv q c ⊗ₜ F q c) =
      q2i q • ((F q c ⊗ₜ[R] 1 + Kinv q c ⊗ₜ F q c) * (K q c ⊗ₜ[R] K q c)) := by
  simp only [mul_add, add_mul, Algebra.TensorProduct.tmul_mul_tmul, mul_one, one_mul, K_F,
    K_Kinv, Kinv_K, smul_add, ← smul_tmul', tmul_smul]

theorem comul_rel_E_F :
    (E q c ⊗ₜ[R] K q c + 1 ⊗ₜ E q c) * (F q c ⊗ₜ[R] 1 + Kinv q c ⊗ₜ F q c) =
      (F q c ⊗ₜ[R] 1 + Kinv q c ⊗ₜ F q c) * (E q c ⊗ₜ[R] K q c + 1 ⊗ₜ E q c) +
        c • (K q c ⊗ₜ[R] K q c - Kinv q c ⊗ₜ Kinv q c) := by
  have cross : (E q c * Kinv q c) ⊗ₜ[R] (K q c * F q c) =
      (Kinv q c * E q c) ⊗ₜ[R] (F q c * K q c) := by
    rw [E_Kinv, K_F, ← smul_tmul', tmul_smul, smul_smul, q2_mul_q2i, one_smul]
  simp only [mul_add, add_mul, Algebra.TensorProduct.tmul_mul_tmul, mul_one, one_mul, cross,
    E_F, add_tmul, tmul_add, smul_tmul', tmul_smul, sub_tmul, tmul_sub, smul_sub]
  rw [smul_tmul]
  abel

/-- **The coproduct** `Δ E = E ⊗ K + 1 ⊗ E`, `Δ F = F ⊗ 1 + K⁻¹ ⊗ F`, `Δ K^{±1} = K^{±1} ⊗ K^{±1}`. -/
def comul : Uq q c →ₐ[R] Uq q c ⊗[R] Uq q c :=
  lift q c (E q c ⊗ₜ[R] K q c + 1 ⊗ₜ[R] E q c) (F q c ⊗ₜ[R] 1 + Kinv q c ⊗ₜ[R] F q c)
    (K q c ⊗ₜ[R] K q c) (Kinv q c ⊗ₜ[R] Kinv q c)
    (by rw [Algebra.TensorProduct.tmul_mul_tmul, K_Kinv, Algebra.TensorProduct.one_def])
    (by rw [Algebra.TensorProduct.tmul_mul_tmul, Kinv_K, Algebra.TensorProduct.one_def])
    (comul_rel_K_E q c) (comul_rel_K_F q c) (comul_rel_E_F q c)

/-- The counit `ε E = ε F = 0`, `ε K^{±1} = 1`. -/
def counit : Uq q c →ₐ[R] R :=
  lift q c 0 0 1 1 (by simp) (by simp) (by simp) (by simp) (by simp)

@[simp] theorem comul_E : comul q c (E q c) = E q c ⊗ₜ K q c + 1 ⊗ₜ E q c := by simp [comul]
@[simp] theorem comul_F : comul q c (F q c) = F q c ⊗ₜ 1 + Kinv q c ⊗ₜ F q c := by simp [comul]
@[simp] theorem comul_K : comul q c (K q c) = K q c ⊗ₜ K q c := by simp [comul]
@[simp] theorem comul_Kinv : comul q c (Kinv q c) = Kinv q c ⊗ₜ Kinv q c := by simp [comul]
@[simp] theorem counit_E : counit q c (E q c) = 0 := by simp [counit]
@[simp] theorem counit_F : counit q c (F q c) = 0 := by simp [counit]
@[simp] theorem counit_K : counit q c (K q c) = 1 := by simp [counit]
@[simp] theorem counit_Kinv : counit q c (Kinv q c) = 1 := by simp [counit]

theorem comul_coassoc :
    (Algebra.TensorProduct.assoc R R (Uq q c) (Uq q c) (Uq q c)).toAlgHom.comp
      ((Algebra.TensorProduct.map (comul q c) (.id R _)).comp (comul q c))
      = (Algebra.TensorProduct.map (.id R _) (comul q c)).comp (comul q c) := by
  apply hom_ext <;>
    simp [tmul_add, add_tmul, add_assoc, Algebra.TensorProduct.one_def]

theorem counit_rTensor :
    (Algebra.TensorProduct.map (counit q c) (.id R _)).comp (comul q c)
      = (Algebra.TensorProduct.lid R (Uq q c)).symm := by
  apply hom_ext <;> simp

theorem counit_lTensor :
    (Algebra.TensorProduct.map (.id R _) (counit q c)).comp (comul q c)
      = (Algebra.TensorProduct.rid R R (Uq q c)).symm := by
  apply hom_ext <;> simp

/-- **`U_q(sl₂)` is a bialgebra** over any commutative ring. -/
instance instBialgebra : Bialgebra R (Uq q c) :=
  Bialgebra.ofAlgHom (comul q c) (counit q c)
    (comul_coassoc q c) (counit_rTensor q c) (counit_lTensor q c)

/-! ## Matrix-coefficient form -/

/-- The block sum of the Borel matrices `((1, E), (0, K))` and `((K⁻¹, F), (0, 1))`. -/
def uqMatrix : Matrix (Fin 4) (Fin 4) (Uq q c) :=
  Matrix.of ![![1, E q c, 0, 0], ![0, K q c, 0, 0], ![0, 0, Kinv q c, F q c], ![0, 0, 0, 1]]

theorem comul_isMatrixCoproduct : IsMatrixCoproduct (R := R) (uqMatrix q c) (comul q c) := by
  rw [isMatrixCoproduct_iff]
  intro i j
  fin_cases i <;> fin_cases j <;>
    simp only [uqMatrix, Matrix.of_apply, Fin.sum_univ_four, Fin.isValue, Matrix.cons_val_zero,
      Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Fin.zero_eta, Fin.mk_one,
      Fin.reduceFinMk] <;>
    simp [Algebra.TensorProduct.one_def, add_comm]

theorem counit_isMatrixCounit : IsMatrixCounit (R := R) (uqMatrix q c) (counit q c) := by
  rw [isMatrixCounit_iff]
  intro i j
  fin_cases i <;> fin_cases j <;>
    simp only [uqMatrix, Matrix.of_apply, Fin.isValue, Matrix.cons_val_zero,
      Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Fin.zero_eta, Fin.mk_one,
      Fin.reduceFinMk] <;>
    simp

theorem present_surjective : Function.Surjective (present (R := R) (uqMatrix q c)) := by
  have h : (present (R := R) (uqMatrix q c)).comp
      (FreeAlgebra.lift R fun g : Gen => match g with
        | .E => u R 0 1 | .F => u R 2 3 | .K => u R 1 1 | .Kinv => u R 2 2) = mk q c := by
    apply FreeAlgebra.hom_ext
    funext g
    cases g <;>
      simp only [Function.comp_apply, AlgHom.coe_comp, FreeAlgebra.lift_ι_apply, present_u,
        uqMatrix, Matrix.of_apply, Matrix.cons_val_zero, Matrix.cons_val_one,
        Matrix.cons_val_two, Matrix.cons_val_three, Fin.isValue, Fin.reduceFinMk] <;> rfl
  intro a
  obtain ⟨x, rfl⟩ := RingQuot.mkAlgHom_surjective R (Rel (R := R) q c) a
  exact ⟨_, congrArg (fun f => f x) h⟩

/-- `Δ` is the only coproduct of matrix-coefficient type for the Borel block matrix. -/
theorem comul_unique {Δ : Uq q c →ₐ[R] Uq q c ⊗[R] Uq q c}
    (h : IsMatrixCoproduct (uqMatrix q c) Δ) : Δ = comul q c :=
  IsMatrixCoproduct.unique (present_surjective q c) h (comul_isMatrixCoproduct q c)

end

end QOU.UqSl2
