import QOU.Archimedean.rj_canonical_inner_product
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Algebra.Algebra.Prod

/-!
# QOU.Archimedean.RossoJonesH4 — Rosso–Jones at `r = 4`, convention D

Scratch: under construction.
-/

set_option linter.unusedSimpArgs false
set_option linter.unreachableTactic false
set_option linter.unusedTactic false
set_option linter.unnecessarySeqFocus false

namespace QOU.Archimedean

open QOU.QInteger

variable {R : Type*} [Field R]

/-- Coordinates of an element of `H₄(q)` in the coset decomposition
`H₄ = H₃ ⊕ H₃·σ₃ ⊕ H₃·σ₃σ₂ ⊕ H₃·σ₃σ₂σ₁` (Jones normal form). -/
structure H4 (R : Type*) where
  h0 : H3 R
  h1 : H3 R
  h2 : H3 R
  h3 : H3 R

namespace H4

/-- Right multiplication by `σ₁`. -/
noncomputable def rs1 (q : R) (V : H4 R) : H4 R :=
  ⟨H3.rs1 q V.h0, H3.rs1 q V.h1, V.h3, H3.add V.h2 (H3.smul (q - q⁻¹) V.h3)⟩

/-- Right multiplication by `σ₂`. -/
noncomputable def rs2 (q : R) (V : H4 R) : H4 R :=
  ⟨H3.rs2 q V.h0, V.h2, H3.add V.h1 (H3.smul (q - q⁻¹) V.h2), H3.rs1 q V.h3⟩

/-- Right multiplication by `σ₃`. -/
noncomputable def rs3 (q : R) (V : H4 R) : H4 R :=
  ⟨V.h1, H3.add V.h0 (H3.smul (q - q⁻¹) V.h1), H3.rs2 q V.h2, H3.rs2 q V.h3⟩

/-- The unit. -/
def one : H4 R := ⟨H3.one, ⟨0, 0, 0, 0, 0, 0⟩, ⟨0, 0, 0, 0, 0, 0⟩, ⟨0, 0, 0, 0, 0, 0⟩⟩

/-- Coordinates of `γˢ`, `γ = σ₁σ₂σ₃`. -/
noncomputable def gammaPow (q : R) : ℕ → H4 R
  | 0 => one
  | s + 1 => rs3 q (rs2 q (rs1 q (gammaPow q s)))

/-- The Markov trace on coordinates, as forced by the Markov conditions. -/
noncomputable def markovTr (q z : R) (V : H4 R) : R :=
  H3.markovTr q z V.h0 + z * H3.markovTr q z V.h1 + z * H3.markovTr q z (H3.rs2 q V.h2)
    + z * H3.markovTr q z (H3.rs1 q (H3.rs2 q V.h3))

section Embed

variable {A : Type*} [Ring A] [Algebra R A]

/-- Evaluation in an `R`-algebra with chosen `s₁, s₂, s₃`. -/
def eval (s1 s2 s3 : A) (V : H4 R) : A :=
  H3.eval s1 s2 V.h0 + H3.eval s1 s2 V.h1 * s3 + H3.eval s1 s2 V.h2 * (s3 * s2)
    + H3.eval s1 s2 V.h3 * (s3 * s2 * s1)

variable (q : R) (s1 s2 s3 : A)

theorem eval_rs1 (hs1 : s1 * s1 = (q - q⁻¹) • s1 + 1) (hc : s1 * s3 = s3 * s1) (V : H4 R) :
    eval s1 s2 s3 (rs1 q V) = eval s1 s2 s3 V * s1 := by
  have k1 : s3 * s2 * s1 * s1 = (q - q⁻¹) • (s3 * s2 * s1) + s3 * s2 := by
    rw [mul_assoc, hs1, mul_add, mul_smul_comm, mul_one]
  simp only [eval, rs1, H3.eval_rs1 q s1 s2 hs1, H3.eval_add, H3.eval_smul]
  generalize H3.eval s1 s2 V.h0 = X0
  generalize H3.eval s1 s2 V.h1 = X1
  generalize H3.eval s1 s2 V.h2 = X2
  generalize H3.eval s1 s2 V.h3 = X3
  have e1 : X1 * s1 * s3 = X1 * s3 * s1 := by rw [mul_assoc, hc, ← mul_assoc]
  have e3 : X3 * (s3 * s2 * s1) * s1 = (q - q⁻¹) • (X3 * (s3 * s2 * s1)) + X3 * (s3 * s2) := by
    rw [mul_assoc, k1, mul_add, mul_smul_comm]
  simp only [add_mul, e1, e3, smul_mul_assoc]
  simp only [mul_assoc]
  abel

theorem eval_rs2 (hs1 : s1 * s1 = (q - q⁻¹) • s1 + 1) (hs2 : s2 * s2 = (q - q⁻¹) • s2 + 1)
    (hbr : s1 * s2 * s1 = s2 * s1 * s2) (hc : s1 * s3 = s3 * s1) (V : H4 R) :
    eval s1 s2 s3 (rs2 q V) = eval s1 s2 s3 V * s2 := by
  have k1 : s3 * s2 * s2 = (q - q⁻¹) • (s3 * s2) + s3 := by
    rw [mul_assoc, hs2, mul_add, mul_smul_comm, mul_one]
  have k2 : s3 * s2 * s1 * s2 = s1 * (s3 * s2 * s1) := by
    calc s3 * s2 * s1 * s2 = s3 * (s2 * s1 * s2) := by simp only [mul_assoc]
      _ = s3 * (s1 * s2 * s1) := by rw [hbr]
      _ = (s3 * s1) * (s2 * s1) := by simp only [mul_assoc]
      _ = s1 * (s3 * s2 * s1) := by rw [← hc]; simp only [mul_assoc]
  simp only [eval, rs2, H3.eval_rs2 q s1 s2 hs2 hbr, H3.eval_rs1 q s1 s2 hs1, H3.eval_add,
    H3.eval_smul]
  generalize H3.eval s1 s2 V.h0 = X0
  generalize H3.eval s1 s2 V.h1 = X1
  generalize H3.eval s1 s2 V.h2 = X2
  generalize H3.eval s1 s2 V.h3 = X3
  have e2 : X2 * (s3 * s2) * s2 = (q - q⁻¹) • (X2 * (s3 * s2)) + X2 * s3 := by
    rw [mul_assoc, k1, mul_add, mul_smul_comm]
  have e3 : X3 * (s3 * s2 * s1) * s2 = X3 * s1 * (s3 * s2 * s1) := by
    rw [mul_assoc, k2, ← mul_assoc]
  simp only [add_mul, e2, e3, smul_mul_assoc]
  simp only [mul_assoc]
  abel

theorem eval_rs3 (hs2 : s2 * s2 = (q - q⁻¹) • s2 + 1) (hs3 : s3 * s3 = (q - q⁻¹) • s3 + 1)
    (hbr : s1 * s2 * s1 = s2 * s1 * s2) (hbr' : s2 * s3 * s2 = s3 * s2 * s3)
    (hc : s1 * s3 = s3 * s1) (V : H4 R) :
    eval s1 s2 s3 (rs3 q V) = eval s1 s2 s3 V * s3 := by
  have k2 : s3 * s2 * s3 = s2 * (s3 * s2) := by rw [← hbr', mul_assoc]
  have k3 : s3 * s2 * s1 * s3 = s2 * (s3 * s2 * s1) := by
    calc s3 * s2 * s1 * s3 = s3 * s2 * s3 * s1 := by rw [mul_assoc _ s1, hc, ← mul_assoc]
      _ = s2 * (s3 * s2 * s1) := by rw [k2]; simp only [mul_assoc]
  simp only [eval, rs3, H3.eval_rs2 q s1 s2 hs2 hbr, H3.eval_add, H3.eval_smul]
  generalize H3.eval s1 s2 V.h0 = X0
  generalize H3.eval s1 s2 V.h1 = X1
  generalize H3.eval s1 s2 V.h2 = X2
  generalize H3.eval s1 s2 V.h3 = X3
  have e1 : X1 * s3 * s3 = (q - q⁻¹) • (X1 * s3) + X1 := by
    rw [mul_assoc, hs3, mul_add, mul_smul_comm, mul_one]
  have e2 : X2 * (s3 * s2) * s3 = X2 * s2 * (s3 * s2) := by
    rw [mul_assoc, k2, ← mul_assoc]
  have e3 : X3 * (s3 * s2 * s1) * s3 = X3 * s2 * (s3 * s2 * s1) := by
    rw [mul_assoc, k3, ← mul_assoc]
  simp only [add_mul, e1, e2, e3, smul_mul_assoc]
  simp only [mul_assoc]
  abel


theorem eval_gammaPow (hs1 : s1 * s1 = (q - q⁻¹) • s1 + 1) (hs2 : s2 * s2 = (q - q⁻¹) • s2 + 1)
    (hs3 : s3 * s3 = (q - q⁻¹) • s3 + 1) (hbr : s1 * s2 * s1 = s2 * s1 * s2)
    (hbr' : s2 * s3 * s2 = s3 * s2 * s3) (hc : s1 * s3 = s3 * s1) (s : ℕ) :
    eval s1 s2 s3 (gammaPow q s) = (s1 * s2 * s3) ^ s := by
  induction s with
  | zero => simp [gammaPow, one, eval, H3.one, H3.eval]
  | succ n ih =>
    rw [gammaPow, eval_rs3 q s1 s2 s3 hs2 hs3 hbr hbr' hc, eval_rs2 q s1 s2 s3 hs1 hs2 hbr hc,
      eval_rs1 q s1 s2 s3 hs1 hc, ih, pow_succ]
    simp only [mul_assoc]

omit s3 in
theorem _root_.QOU.Archimedean.H3.eval_mem_adjoin (v : H3 R) :
    H3.eval s1 s2 v ∈ Algebra.adjoin R ({s1, s2} : Set A) := by
  have m1 : s1 ∈ Algebra.adjoin R ({s1, s2} : Set A) := Algebra.subset_adjoin (by simp)
  have m2 : s2 ∈ Algebra.adjoin R ({s1, s2} : Set A) := Algebra.subset_adjoin (by simp)
  unfold H3.eval
  refine Subalgebra.add_mem _ (Subalgebra.add_mem _ (Subalgebra.add_mem _ (Subalgebra.add_mem _
    (Subalgebra.add_mem _ ?_ ?_) ?_) ?_) ?_) ?_ <;>
  refine Subalgebra.smul_mem _ ?_ _
  · exact Subalgebra.one_mem _
  · exact m1
  · exact m2
  · exact Subalgebra.mul_mem _ m1 m2
  · exact Subalgebra.mul_mem _ m2 m1
  · exact Subalgebra.mul_mem _ (Subalgebra.mul_mem _ m1 m2) m1

/-- **Markov uniqueness on `H₄`.** Any `R`-linear functional with `t 1 = 1`,
`t s₁ = z`, `t(xy) = t(yx)`, and the Markov property at levels 2 and 3
(`t(x s₂) = z t(x)` for `x ∈ span{1, s₁}`, `t(x s₃) = z t(x)` for `x` in the
subalgebra generated by `s₁, s₂`) takes the value `markovTr q z V` on `eval V`. -/
theorem markov4_unique (hs1 : s1 * s1 = (q - q⁻¹) • s1 + 1)
    (hs2 : s2 * s2 = (q - q⁻¹) • s2 + 1) (hbr : s1 * s2 * s1 = s2 * s1 * s2)
    (z : R) (t : A →ₗ[R] R) (ht1 : t 1 = 1) (hts1 : t s1 = z)
    (hcyc : ∀ x y : A, t (x * y) = t (y * x))
    (hmark2 : ∀ c d : R, t ((c • (1 : A) + d • s1) * s2) = z * t (c • (1 : A) + d • s1))
    (hmark3 : ∀ x ∈ Algebra.adjoin R ({s1, s2} : Set A), t (x * s3) = z * t x)
    (V : H4 R) : t (eval s1 s2 s3 V) = markovTr q z V := by
  have mt := fun v => H3.markov3_unique q s1 s2 hs1 z t ht1 hts1 hcyc hmark2 v
  have m1 : s1 ∈ Algebra.adjoin R ({s1, s2} : Set A) := Algebra.subset_adjoin (by simp)
  have m2 : s2 ∈ Algebra.adjoin R ({s1, s2} : Set A) := Algebra.subset_adjoin (by simp)
  have T1 : t (H3.eval s1 s2 V.h1 * s3) = z * H3.markovTr q z V.h1 := by
    rw [hmark3 _ (H3.eval_mem_adjoin s1 s2 _), mt]
  have T2 : t (H3.eval s1 s2 V.h2 * (s3 * s2)) = z * H3.markovTr q z (H3.rs2 q V.h2) := by
    rw [← mul_assoc, hcyc, ← mul_assoc,
      hmark3 _ (Subalgebra.mul_mem _ m2 (H3.eval_mem_adjoin s1 s2 _)), hcyc,
      ← H3.eval_rs2 q s1 s2 hs2 hbr, mt]
  have T3 : t (H3.eval s1 s2 V.h3 * (s3 * s2 * s1))
      = z * H3.markovTr q z (H3.rs1 q (H3.rs2 q V.h3)) := by
    rw [mul_assoc s3, ← mul_assoc, hcyc, ← mul_assoc,
      hmark3 _ (Subalgebra.mul_mem _ (Subalgebra.mul_mem _ m2 m1) (H3.eval_mem_adjoin s1 s2 _)),
      hcyc, ← mul_assoc, ← H3.eval_rs2 q s1 s2 hs2 hbr, ← H3.eval_rs1 q s1 s2 hs1, mt]
  simp only [eval, map_add, T1, T2, T3, mt, markovTr]

end Embed

end H4

/-! ### A concrete Markov trace: the three two-row Temperley–Lieb standard modules -/

theorem qIntBal_five (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    qIntBal q 5 = q ^ 4 + q ^ 2 + 1 + q⁻¹ ^ 2 + q⁻¹ ^ 4 := by
  have h : q - q⁻¹ ≠ 0 := by
    intro h; apply hq2; field_simp at h; linear_combination h
  rw [qIntBal_def, div_eq_iff h]; field_simp; ring

namespace RJ4

/-- `σᵢ = q − eᵢ` on the 3-dimensional standard module `W_{4,2}` (shape `(3,1)`),
basis = position of the single cup, `eᵢ` acting by the Temperley–Lieb rules
`eᵢ bᵢ = [2] bᵢ`, `eᵢ b_{i±1} = bᵢ`. -/
noncomputable def B1 (q : R) : Matrix (Fin 3) (Fin 3) R := !![-q⁻¹, -1, 0; 0, q, 0; 0, 0, q]
noncomputable def B2 (q : R) : Matrix (Fin 3) (Fin 3) R := !![q, 0, 0; -1, -q⁻¹, -1; 0, 0, q]
noncomputable def B3 (q : R) : Matrix (Fin 3) (Fin 3) R := !![q, 0, 0; 0, q, 0; 0, -1, -q⁻¹]
/-- `σᵢ = q − eᵢ` on the 2-dimensional standard module `W_{4,0}` (shape `(2,2)`),
basis `{(12)(34), (14)(23)}`. -/
noncomputable def C1 (q : R) : Matrix (Fin 2) (Fin 2) R := !![-q⁻¹, -1; 0, q]
noncomputable def C2 (q : R) : Matrix (Fin 2) (Fin 2) R := !![q, 0; -1, -q⁻¹]

/-- The model algebra `R × M₃(R) × M₂(R)` (trivial ⊕ `W_{4,2}` ⊕ `W_{4,0}`). -/
abbrev M (R : Type*) [Field R] := R × Matrix (Fin 3) (Fin 3) R × Matrix (Fin 2) (Fin 2) R

noncomputable def S1 (q : R) : M R := (q, B1 q, C1 q)
noncomputable def S2 (q : R) : M R := (q, B2 q, C2 q)
noncomputable def S3 (q : R) : M R := (q, B3 q, C1 q)

/-- The quantum-dimension weighted trace `([5]·χ₍₄₎ + [3]·χ₍₃,₁₎ + [1]·χ₍₂,₂₎)/[2]⁴`. -/
noncomputable def tau (q : R) : M R →ₗ[R] R where
  toFun x := (qIntBal q 5 * x.1 + qIntBal q 3 * x.2.1.trace + x.2.2.trace) / qIntBal q 2 ^ 4
  map_add' x y := by simp only [Prod.fst_add, Prod.snd_add, Matrix.trace_add]; ring
  map_smul' c x := by
    simp only [Prod.smul_fst, Prod.smul_snd, Matrix.trace_smul, smul_eq_mul, RingHom.id_apply]
    ring

section Rel
variable (q : R) (hq : q ≠ 0)
include hq

theorem S1_sq : S1 q * S1 q = (q - q⁻¹) • S1 q + 1 := by
  refine Prod.ext ?_ (Prod.ext ?_ ?_)
  · simp [S1]; field_simp; ring
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [S1, B1, Matrix.mul_apply, Fin.sum_univ_three] <;> (try field_simp) <;> (try ring_nf) <;> (try simp)
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [S1, C1, Matrix.mul_apply, Fin.sum_univ_two] <;> (try field_simp) <;> (try ring_nf) <;> (try simp)

theorem S2_sq : S2 q * S2 q = (q - q⁻¹) • S2 q + 1 := by
  refine Prod.ext ?_ (Prod.ext ?_ ?_)
  · simp [S2]; field_simp; ring
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [S2, B2, Matrix.mul_apply, Fin.sum_univ_three] <;> (try field_simp) <;> (try ring_nf) <;> (try simp)
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [S2, C2, Matrix.mul_apply, Fin.sum_univ_two] <;> (try field_simp) <;> (try ring_nf) <;> (try simp)

theorem S3_sq : S3 q * S3 q = (q - q⁻¹) • S3 q + 1 := by
  refine Prod.ext ?_ (Prod.ext ?_ ?_)
  · simp [S3]; field_simp; ring
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [S3, B3, Matrix.mul_apply, Fin.sum_univ_three] <;> (try field_simp) <;> (try ring_nf) <;> (try simp)
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [S3, C1, Matrix.mul_apply, Fin.sum_univ_two] <;> (try field_simp) <;> (try ring_nf) <;> (try simp)

theorem S12_braid : S1 q * S2 q * S1 q = S2 q * S1 q * S2 q := by
  refine Prod.ext ?_ (Prod.ext ?_ ?_)
  · simp [S1, S2]; try ring
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [S1, S2, B1, B2, Matrix.mul_apply, Fin.sum_univ_three] <;> (try field_simp) <;> (try ring_nf) <;> (try simp)
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [S1, S2, C1, C2, Matrix.mul_apply, Fin.sum_univ_two] <;> (try field_simp) <;> (try ring_nf) <;> (try simp)

theorem S23_braid : S2 q * S3 q * S2 q = S3 q * S2 q * S3 q := by
  refine Prod.ext ?_ (Prod.ext ?_ ?_)
  · simp [S2, S3]; try ring
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [S2, S3, B2, B3, Matrix.mul_apply, Fin.sum_univ_three] <;> (try field_simp) <;> (try ring_nf) <;> (try simp)
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [S2, S3, C1, C2, Matrix.mul_apply, Fin.sum_univ_two] <;> (try field_simp) <;> (try ring_nf) <;> (try simp)

theorem S13_comm : S1 q * S3 q = S3 q * S1 q := by
  refine Prod.ext ?_ (Prod.ext ?_ ?_)
  · simp [S1, S3]; try ring
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [S1, S3, B1, B3, Matrix.mul_apply, Fin.sum_univ_three] <;> (try field_simp) <;> (try ring_nf) <;> (try simp)
  · simp [S1, S3]

end Rel

section TauMarkov
variable (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (hq1 : q ^ 2 + 1 ≠ 0)
include hq hq2 hq1

theorem tau_one : tau q 1 = 1 := by
  simp only [tau, LinearMap.coe_mk, AddHom.coe_mk, Prod.fst_one, Prod.snd_one, Matrix.trace_one,
    Fintype.card_fin]
  rw [qIntBal_five q hq hq2, qIntBal_three q hq hq2, qIntBal_two q hq hq2]
  have : q + q⁻¹ ≠ 0 := by
    intro h; apply hq1; field_simp at h; linear_combination h
  field_simp
  push_cast
  ring

theorem tau_S1 : tau q (S1 q) = markovZD q := by
  simp only [tau, LinearMap.coe_mk, AddHom.coe_mk, S1, B1, C1, Matrix.trace_fin_three,
    Matrix.trace_fin_two, Matrix.of_apply, Matrix.cons_val', Matrix.cons_val_zero,
    Matrix.cons_val_one, Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons,
    Matrix.empty_val', Matrix.cons_val_fin_one, Matrix.head_fin_const]
  rw [qIntBal_five q hq hq2, qIntBal_three q hq hq2, qIntBal_two q hq hq2, markovZD]
  have : q + q⁻¹ ≠ 0 := by
    intro h; apply hq1; field_simp at h; linear_combination h
  field_simp
  ring

omit hq hq2 hq1 in
theorem tau_cyc (x y : M R) : tau q (x * y) = tau q (y * x) := by
  simp only [tau, LinearMap.coe_mk, AddHom.coe_mk, Prod.fst_mul, Prod.snd_mul,
    Matrix.trace_mul_comm x.2.1, Matrix.trace_mul_comm x.2.2, mul_comm x.1]

theorem tau_mark2 (c d : R) :
    tau q ((c • (1 : M R) + d • S1 q) * S2 q) = markovZD q * tau q (c • (1 : M R) + d • S1 q) := by
  simp only [add_mul, smul_mul_assoc, one_mul, map_add, map_smul, smul_eq_mul]
  simp only [tau, LinearMap.coe_mk, AddHom.coe_mk, S1, S2, B1, B2, C1, C2,
    Prod.mk_mul_mk, Prod.fst_one, Prod.snd_one, Matrix.one_fin_three, Matrix.one_fin_two,
    Matrix.mul_fin_three, Matrix.mul_fin_two, Matrix.trace_fin_three, Matrix.trace_fin_two,
    Matrix.of_apply, Matrix.cons_val', Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons, Matrix.empty_val',
    Matrix.cons_val_fin_one, Matrix.head_fin_const]
  rw [qIntBal_five q hq hq2, qIntBal_three q hq hq2, qIntBal_two q hq hq2, markovZD]
  have : q + q⁻¹ ≠ 0 := by
    intro h; apply hq1; field_simp at h; linear_combination h
  field_simp
  ring

theorem tau_mark3 (v : H3 R) :
    tau q (H3.eval (S1 q) (S2 q) v * S3 q) = markovZD q * tau q (H3.eval (S1 q) (S2 q) v) := by
  simp only [H3.eval, add_mul, smul_mul_assoc, one_mul, map_add, map_smul, smul_eq_mul]
  simp only [tau, LinearMap.coe_mk, AddHom.coe_mk, S1, S2, S3, B1, B2, B3, C1, C2,
    Prod.mk_mul_mk, Prod.fst_one, Prod.snd_one, Matrix.one_fin_three, Matrix.one_fin_two,
    Matrix.mul_fin_three, Matrix.mul_fin_two, Matrix.trace_fin_three, Matrix.trace_fin_two,
    Matrix.of_apply, Matrix.cons_val', Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons, Matrix.empty_val',
    Matrix.cons_val_fin_one, Matrix.head_fin_const]
  rw [qIntBal_five q hq hq2, qIntBal_three q hq hq2, qIntBal_two q hq hq2, markovZD]
  have : q + q⁻¹ ≠ 0 := by
    intro h; apply hq1; field_simp at h; linear_combination h
  field_simp
  ring

theorem tau_mark3_adjoin (x : M R) (hx : x ∈ Algebra.adjoin R ({S1 q, S2 q} : Set (M R))) :
    tau q (x * S3 q) = markovZD q * tau q x := by
  obtain ⟨v, rfl⟩ := H3.exists_eval_of_mem_adjoin (S1 q) (S2 q) q (S1_sq q hq) (S2_sq q hq)
    (S12_braid q hq) hx
  exact tau_mark3 q hq hq2 hq1 v

end TauMarkov

/-- `γ = σ₁σ₂σ₃` on `W_{4,2}`. -/
noncomputable def G (q : R) : Matrix (Fin 3) (Fin 3) R := !![0, 0, -q⁻¹; -q ^ 2, 0, 1; 0, -q ^ 2, -q]
/-- `γ = σ₁σ₂σ₃` on `W_{4,0}`: the swap of the two cup diagrams. -/
def H (R : Type*) [Field R] : Matrix (Fin 2) (Fin 2) R := !![0, 1; 1, 0]

theorem B123 (q : R) (hq : q ≠ 0) : B1 q * B2 q * B3 q = G q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [B1, B2, B3, G, Matrix.mul_apply, Fin.sum_univ_three] <;> (try field_simp) <;>
    (try ring_nf) <;> (try simp)

theorem C121 (q : R) (hq : q ≠ 0) : C1 q * C2 q * C1 q = H R := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [C1, C2, H, Matrix.mul_apply, Fin.sum_univ_two] <;> (try field_simp) <;>
    (try ring_nf) <;> (try simp)

/-- The full twist `Δ² = γ⁴` acts on `W_{4,2}` by the scalar `q⁴`. -/
theorem G_pow_four (q : R) (hq : q ≠ 0) : G q ^ 4 = (q ^ 4) • (1 : Matrix (Fin 3) (Fin 3) R) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [G, pow_succ, Matrix.mul_apply, Fin.sum_univ_three] <;> (try field_simp) <;>
    (try ring_nf) <;> (try simp)

/-- The full twist acts on `W_{4,0}` by `1`. -/
theorem H_sq : H R ^ 2 = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [H, pow_succ, Matrix.mul_apply, Fin.sum_univ_two]

theorem trace_G_pow (q : R) (hq : q ≠ 0) (s : ℕ) :
    (G q ^ s).trace = q ^ s * (if s % 4 = 0 then 3 else -1) := by
  induction s using Nat.strong_induction_on with
  | _ s ih =>
    match s, ih with
    | 0, _ => simp
    | 1, _ =>
      simp [G, Matrix.trace_fin_three]
    | 2, _ =>
      simp [G, pow_succ, Matrix.trace_fin_three, Matrix.mul_apply, Fin.sum_univ_three] <;>
        (try field_simp) <;> (try ring)
    | 3, _ =>
      simp [G, pow_succ, Matrix.trace_fin_three, Matrix.mul_apply, Fin.sum_univ_three] <;>
        (try field_simp) <;> (try ring)
    | n + 4, ih =>
      rw [pow_add, G_pow_four q hq, Matrix.mul_smul, mul_one, Matrix.trace_smul, ih n (by omega),
        show (n + 4) % 4 = n % 4 by omega, smul_eq_mul, pow_add]
      ring

theorem trace_H_pow (s : ℕ) : (H R ^ s).trace = if s % 2 = 0 then 2 else 0 := by
  induction s using Nat.strong_induction_on with
  | _ s ih =>
    match s, ih with
    | 0, _ => simp
    | 1, _ => simp [H, Matrix.trace_fin_two]
    | n + 2, ih =>
      rw [pow_add, H_sq, mul_one, ih n (by omega), show (n + 2) % 2 = n % 2 by omega]

end RJ4



namespace H4

open RJ4

theorem qIntBal_two_ne_zero (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (hq1 : q ^ 2 + 1 ≠ 0) :
    qIntBal q 2 ≠ 0 := by
  rw [qIntBal_two q hq hq2]
  intro h; apply hq1; field_simp at h; linear_combination h

/-- **Rosso–Jones at `r = 4`, every `s`**, on the coordinate Markov trace of `H₄(q)`:
`[2]⁴ · tr_M((σ₁σ₂σ₃)ˢ) = [5] q^{3s} + [3] · qˢ · χ₄(s) + χ₂(s)`, where
`χ₄(s) = 3` if `4 ∣ s` else `−1` (the `(3,1)` block, on which `Δ² = γ⁴` acts by `q⁴`),
and `χ₂(s) = 2` if `2 ∣ s` else `0` (the `(2,2)` block, on which `Δ²` acts by `1`).
The value is obtained by evaluating the forced coordinate trace through the concrete
Markov trace `RJ4.tau` (uniqueness, `markov4_unique`). -/
theorem h4Trace_rossoJones (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (hq1 : q ^ 2 + 1 ≠ 0)
    (s : ℕ) :
    qIntBal q 2 ^ 4 * markovTr q (markovZD q) (gammaPow q s)
      = qIntBal q 5 * q ^ (3 * s) + qIntBal q 3 * (q ^ s * (if s % 4 = 0 then 3 else -1))
        + (if s % 2 = 0 then 2 else 0) := by
  have hS := eval_gammaPow q (S1 q) (S2 q) (S3 q) (S1_sq q hq) (S2_sq q hq) (S3_sq q hq)
    (S12_braid q hq) (S23_braid q hq) (S13_comm q hq) s
  have hU := markov4_unique q (S1 q) (S2 q) (S3 q) (S1_sq q hq) (S2_sq q hq) (S12_braid q hq)
    (markovZD q) (tau q) (tau_one q hq hq2 hq1) (tau_S1 q hq hq2 hq1) (tau_cyc q)
    (tau_mark2 q hq hq2 hq1) (tau_mark3_adjoin q hq hq2 hq1) (gammaPow q s)
  rw [← hU, hS]
  have hprod : S1 q * S2 q * S3 q = (q ^ 3, G q, H R) := by
    simp only [S1, S2, S3, Prod.mk_mul_mk, B123 q hq, C121 q hq]
    congr 1; ring
  rw [hprod]
  simp only [tau, LinearMap.coe_mk, AddHom.coe_mk, Prod.pow_mk, trace_G_pow q hq,
    trace_H_pow]
  have h2 := qIntBal_two_ne_zero q hq hq2 hq1
  rw [← pow_mul]
  field_simp

/-- **Torus knots `τ(4, s)`, `s` odd**: the block's formula
`[r+1] q^{s(r−1)} − [r−1] q^{s(r−3)}` at `r = 4`. -/
theorem h4Trace_rossoJones_coprime (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (hq1 : q ^ 2 + 1 ≠ 0) (s : ℕ) (hs : Odd s) :
    qIntBal q 2 ^ 4 * markovTr q (markovZD q) (gammaPow q s)
      = qIntBal q 5 * q ^ (s * 3) - qIntBal q 3 * q ^ (s * 1) := by
  obtain ⟨k, rfl⟩ := hs
  rw [h4Trace_rossoJones q hq hq2 hq1, if_neg (by omega), if_neg (by omega)]
  ring

end H4

open H4 in
/-- **Part (iii) at `r = 4` for every Markov trace.** In any `R`-algebra `A` with
`s₁, s₂, s₃` satisfying the Hecke, braid and far-commutation relations, any linear
functional satisfying the convention-D Markov conditions has
`[2]⁴ · t((s₁s₂s₃)ˢ) = [5] q^{3s} + [3]·qˢ·χ₄(s) + χ₂(s)`. -/
theorem h4_markov_rossoJones {A : Type*} [Ring A] [Algebra R A] (q : R)
    (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (hq1 : q ^ 2 + 1 ≠ 0) (s1 s2 s3 : A)
    (hs1 : s1 * s1 = (q - q⁻¹) • s1 + 1) (hs2 : s2 * s2 = (q - q⁻¹) • s2 + 1)
    (hs3 : s3 * s3 = (q - q⁻¹) • s3 + 1) (hbr : s1 * s2 * s1 = s2 * s1 * s2)
    (hbr' : s2 * s3 * s2 = s3 * s2 * s3) (hc : s1 * s3 = s3 * s1)
    (t : A →ₗ[R] R) (ht1 : t 1 = 1) (hts1 : t s1 = markovZD q)
    (hcyc : ∀ x y : A, t (x * y) = t (y * x))
    (hmark2 : ∀ c d : R,
      t ((c • (1 : A) + d • s1) * s2) = markovZD q * t (c • (1 : A) + d • s1))
    (hmark3 : ∀ x ∈ Algebra.adjoin R ({s1, s2} : Set A), t (x * s3) = markovZD q * t x)
    (s : ℕ) :
    qIntBal q 2 ^ 4 * t ((s1 * s2 * s3) ^ s)
      = qIntBal q 5 * q ^ (3 * s) + qIntBal q 3 * (q ^ s * (if s % 4 = 0 then 3 else -1))
        + (if s % 2 = 0 then 2 else 0) := by
  rw [← eval_gammaPow q s1 s2 s3 hs1 hs2 hs3 hbr hbr' hc,
    markov4_unique q s1 s2 s3 hs1 hs2 hbr (markovZD q) t ht1 hts1 hcyc hmark2 hmark3]
  exact h4Trace_rossoJones q hq hq2 hq1 s

end QOU.Archimedean
