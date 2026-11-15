import QOU.BraidKnot.CasimirShared
import Mathlib.Algebra.RingQuot
import Mathlib.Algebra.FreeAlgebra
import Mathlib.Tactic


/-!
# QOU.QCasimir.exists — existence of the q-Casimir element

C_q = FE + (qK + q⁻¹K⁻¹ - (q + q⁻¹))/(q - q⁻¹)² is central in
𝒰_q(𝔰𝔲(2)) and acts as [j]_q[j+1]_q on V_j.

LaTeX: `\label{prop:q-casimir-exists}`

## References

- [leitner2026] §4-braids-and-knots/q-casimir-exists
- [kassel1995] Quantum Groups (Springer GTM 155), §VI.4
- [lusztig1993] Introduction to Quantum Groups (Birkhäuser)
-/

namespace QOU

noncomputable section

/-- `R_q = ℚ(q)` has characteristic zero. -/
instance charZero_R_q_casimirExists : CharZero R_q :=
  charZero_of_injective_algebraMap (algebraMap ℚ R_q).injective

/-! **The former axiom `QCasimir.exists_axiom` was false** (removed
    2026-11-15). It claimed `Nonempty (QCasimirData qs)` for every
    `qs : QuantumSu2`. `QuantumSu2` only asks `q ≠ 1`, so `q = 0` is
    allowed, and then the field `qInv_left : qInv * q = 1` cannot hold.
    The data also needs a ring map `R_q → qs.Algebra`, which an arbitrary
    ring need not admit. The true statement is the construction of `C_q`
    in an actual `𝒰_q(𝔰𝔲(2))` with `q` generic; recorded as open in bean
    `qou-n2un`. -/

/-- A `QuantumSu2` with `q = 0`, which `QuantumSu2` allows. -/
def QCasimir.qsZero : QuantumSu2.{0} where
  q := 0
  q_ne_one := zero_ne_one
  Algebra := R_q
  E := 0
  F := 0
  K := 1
  K_inv := 1
  K_inv_left := mul_one 1
  K_inv_right := mul_one 1

/-- **The former axiom is false**: at `q = 0` there is no `QCasimirData`. -/
-- Ref: [kassel1995] Quantum Groups, §VI.4 (needs q invertible)
theorem QCasimir.not_exists_unconstrained :
    ¬ ∀ qs : QuantumSu2.{0}, Nonempty (QCasimirData qs) := by
  intro h
  obtain ⟨d⟩ := h QCasimir.qsZero
  have := d.qInv_left
  simp only [QCasimir.qsZero, mul_zero] at this
  exact zero_ne_one this

end

/-! ## Repaired form (option B, 2026-11-15): the q-Casimir in a constructed `U_q(sl₂)`

Over any field `k` with `q ≠ 0` and `q − q⁻¹ ≠ 0`:
* `UqSl2.Uq k q` is `U_q(sl₂)`, presented as a quotient of the free algebra
  on `E, F, K, K'` by `KK' = K'K = 1`, `KE = q²EK`, `KF = q⁻²FK`,
  `EF − FE = (K − K')/(q − q⁻¹)`;
* `Uq.casimir_central`: `C_q = FE + (qK + q⁻¹K')/(q − q⁻¹)²` is central;
* `Uq.nontrivial`: the algebra is not zero, since it maps to `M₂(k)` through
  the fundamental representation `Uq.fund`.

The constant shift `−(q + q⁻¹)/(q − q⁻¹)²` in the paper's `C_q` is a scalar,
so it does not affect centrality. The eigenvalue `[j]_q[j+1]_q` on `V_j` is
not proved here. -/

namespace UqSl2

variable {k : Type*} [Field k] {A : Type*} [Ring A] [Algebra k A]

/-- Defining relations of `U_q(sl₂)` on elements `E F K K'` of a `k`-algebra. -/
structure UqRels (q : k) (E F K K' : A) : Prop where
  kk' : K * K' = 1
  k'k : K' * K = 1
  ke : K * E = (q ^ 2) • (E * K)
  kf : K * F = (q⁻¹ ^ 2) • (F * K)
  ef : E * F = F * E + (q - q⁻¹)⁻¹ • (K - K')

namespace UqRels
variable {q : k} {E F K K' : A}

theorem k'e (h : UqRels q E F K K') (hq : q ≠ 0) : K' * E = (q⁻¹ ^ 2) • (E * K') := by
  have ek : E * K = (q⁻¹ ^ 2) • (K * E) := by
    rw [h.ke, smul_smul, ← mul_pow, inv_mul_cancel₀ hq, one_pow, one_smul]
  calc K' * E = K' * (E * K) * K' := by rw [mul_assoc, mul_assoc, h.kk', mul_one]
    _ = (q⁻¹ ^ 2) • (E * K') := by
      rw [ek, mul_smul_comm, smul_mul_assoc, ← mul_assoc, h.k'k, one_mul]

theorem k'f (h : UqRels q E F K K') (hq : q ≠ 0) : K' * F = (q ^ 2) • (F * K') := by
  have fk : F * K = (q ^ 2) • (K * F) := by
    rw [h.kf, smul_smul, ← mul_pow, mul_inv_cancel₀ hq, one_pow, one_smul]
  calc K' * F = K' * (F * K) * K' := by rw [mul_assoc, mul_assoc, h.kk', mul_one]
    _ = (q ^ 2) • (F * K') := by
      rw [fk, mul_smul_comm, smul_mul_assoc, ← mul_assoc, h.k'k, one_mul]

end UqRels

/-- The quantum Casimir `C = F E + (q K + q⁻¹ K') / (q − q⁻¹)²`. -/
def qCasimir (q : k) (E F K K' : A) : A :=
  F * E + ((q - q⁻¹)⁻¹ ^ 2) • (q • K + q⁻¹ • K')

namespace UqRels
variable {q : k} {E F K K' : A}

theorem casimir_comm_K (h : UqRels q E F K K') (hq : q ≠ 0) :
    qCasimir q E F K K' * K = K * qCasimir q E F K K' := by
  have fk : F * K = (q ^ 2) • (K * F) := by
    rw [h.kf, smul_smul, ← mul_pow, mul_inv_cancel₀ hq, one_pow, one_smul]
  unfold qCasimir
  simp only [add_mul, mul_add, smul_mul_assoc, mul_smul_comm, h.kk', h.k'k]
  rw [mul_assoc F E K, ← mul_assoc K F E, h.kf, smul_mul_assoc, mul_assoc, h.ke,
    mul_smul_comm, smul_smul, ← mul_assoc, ← mul_pow, inv_mul_cancel₀ hq, one_pow, one_smul]

theorem casimir_comm_E (h : UqRels q E F K K') (hq : q ≠ 0) (hc : q - q⁻¹ ≠ 0) :
    qCasimir q E F K K' * E = E * qCasimir q E F K K' := by
  have hk'e := h.k'e hq
  unfold qCasimir
  simp only [add_mul, mul_add, smul_mul_assoc, mul_smul_comm, smul_add, mul_assoc]
  rw [← mul_assoc E F E, h.ef]
  simp only [add_mul, sub_mul, smul_mul_assoc, smul_add, smul_sub, smul_smul, mul_assoc,
    h.ke, hk'e, mul_smul_comm]
  have hq2 : q ^ 2 - 1 ≠ 0 := by
    intro h0; apply hc; field_simp; linear_combination h0
  match_scalars <;> field_simp <;> ring

theorem casimir_comm_F (h : UqRels q E F K K') (hq : q ≠ 0) (hc : q - q⁻¹ ≠ 0) :
    qCasimir q E F K K' * F = F * qCasimir q E F K K' := by
  have hk'f := h.k'f hq
  unfold qCasimir
  simp only [add_mul, mul_add, smul_mul_assoc, mul_smul_comm, smul_add, mul_assoc]
  rw [h.ef]
  simp only [mul_add, mul_sub, mul_smul_comm, smul_add, smul_sub, smul_smul, mul_assoc,
    h.kf, hk'f, smul_mul_assoc]
  have hq2 : q ^ 2 - 1 ≠ 0 := by
    intro h0; apply hc; field_simp; linear_combination h0
  match_scalars <;> field_simp <;> ring

theorem casimir_comm_K' (h : UqRels q E F K K') (hq : q ≠ 0) :
    qCasimir q E F K K' * K' = K' * qCasimir q E F K K' := by
  have hk'f := h.k'f hq
  have hk'e := h.k'e hq
  unfold qCasimir
  simp only [add_mul, mul_add, smul_mul_assoc, mul_smul_comm, h.kk', h.k'k, mul_assoc]
  rw [← mul_assoc K' F E, hk'f, smul_mul_assoc, mul_assoc, hk'e, mul_smul_comm, smul_smul,
    ← mul_pow, mul_inv_cancel₀ hq, one_pow, one_smul]

end UqRels

/-! ## The presented algebra `U_q(sl₂)` -/

section Presented
variable (k)

/-- Defining relations on the free algebra with generators `0 = E, 1 = F, 2 = K, 3 = K'`. -/
inductive UqRel (q : k) : FreeAlgebra k (Fin 4) → FreeAlgebra k (Fin 4) → Prop
  | kk' : UqRel q (FreeAlgebra.ι k 2 * FreeAlgebra.ι k 3) 1
  | k'k : UqRel q (FreeAlgebra.ι k 3 * FreeAlgebra.ι k 2) 1
  | ke : UqRel q (FreeAlgebra.ι k 2 * FreeAlgebra.ι k 0)
      ((q ^ 2) • (FreeAlgebra.ι k 0 * FreeAlgebra.ι k 2))
  | kf : UqRel q (FreeAlgebra.ι k 2 * FreeAlgebra.ι k 1)
      ((q⁻¹ ^ 2) • (FreeAlgebra.ι k 1 * FreeAlgebra.ι k 2))
  | ef : UqRel q (FreeAlgebra.ι k 0 * FreeAlgebra.ι k 1)
      (FreeAlgebra.ι k 1 * FreeAlgebra.ι k 0
        + (q - q⁻¹)⁻¹ • (FreeAlgebra.ι k 2 - FreeAlgebra.ι k 3))

/-- **The quantum group `U_q(sl₂)`**, as the quotient of the free algebra. -/
abbrev Uq (q : k) := RingQuot (UqRel k q)

variable {k}

/-- The generator images. -/
noncomputable def Uq.gen (q : k) (i : Fin 4) : Uq k q :=
  RingQuot.mkAlgHom k (UqRel k q) (FreeAlgebra.ι k i)

theorem Uq.rels (q : k) :
    UqRels q (Uq.gen q 0) (Uq.gen q 1) (Uq.gen q 2) (Uq.gen q 3) := by
  have hr := fun {x y} (h : UqRel k q x y) => RingQuot.mkAlgHom_rel k h
  refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;> simp only [Uq.gen, ← map_mul]
  · rw [hr UqRel.kk', map_one]
  · rw [hr UqRel.k'k, map_one]
  · rw [hr UqRel.ke, map_smul, map_mul]
  · rw [hr UqRel.kf, map_smul, map_mul]
  · rw [hr UqRel.ef, map_add, map_smul, map_sub, map_mul]

/-- **The quantum Casimir is central in `U_q(sl₂)`.** -/
theorem Uq.casimir_central (q : k) (hq : q ≠ 0) (hc : q - q⁻¹ ≠ 0) (a : Uq k q) :
    qCasimir q (Uq.gen q 0) (Uq.gen q 1) (Uq.gen q 2) (Uq.gen q 3) * a
      = a * qCasimir q (Uq.gen q 0) (Uq.gen q 1) (Uq.gen q 2) (Uq.gen q 3) := by
  have h := Uq.rels q
  set C := qCasimir q (Uq.gen q 0) (Uq.gen q 1) (Uq.gen q 2) (Uq.gen q 3)
  obtain ⟨x, rfl⟩ := RingQuot.mkAlgHom_surjective k (UqRel k q) a
  show Commute C _
  induction x using FreeAlgebra.induction with
  | grade0 r => rw [AlgHom.commutes]; exact Algebra.commute_algebraMap_right r C
  | grade1 i =>
    fin_cases i
    · exact h.casimir_comm_E hq hc
    · exact h.casimir_comm_F hq hc
    · exact h.casimir_comm_K hq
    · exact h.casimir_comm_K' hq
  | mul a b ha hb => rw [map_mul]; exact ha.mul_right hb
  | add a b ha hb => rw [map_add]; exact ha.add_right hb

/-- Generators of the two-dimensional representation `V₁`. -/
def Uq.fundGen (q : k) : Fin 4 → Matrix (Fin 2) (Fin 2) k
  | 0 => !![0, 1; 0, 0]
  | 1 => !![0, 0; 1, 0]
  | 2 => !![q, 0; 0, q⁻¹]
  | 3 => !![q⁻¹, 0; 0, q]

/-- **The fundamental representation** `U_q(sl₂) → M₂(k)`. -/
noncomputable def Uq.fund (q : k) (hq : q ≠ 0) (hc : q - q⁻¹ ≠ 0) :
    Uq k q →ₐ[k] Matrix (Fin 2) (Fin 2) k :=
  RingQuot.liftAlgHom k ⟨FreeAlgebra.lift k (Uq.fundGen q), fun x y hxy => by
    have hq2 : -1 + q ^ 2 ≠ 0 := by
      intro h0; apply hc; field_simp; linear_combination h0
    cases hxy <;> simp only [map_mul, map_one, map_add, map_smul, map_sub,
      FreeAlgebra.lift_ι_apply, Uq.fundGen] <;> ext i j <;> fin_cases i <;> fin_cases j <;>
      simp [Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring_nf <;> field_simp <;> ring⟩

/-- `U_q(sl₂)` is not the zero ring: it maps onto a nonzero matrix algebra. -/
theorem Uq.nontrivial (q : k) (hq : q ≠ 0) (hc : q - q⁻¹ ≠ 0) : Nontrivial (Uq k q) := by
  refine ⟨⟨0, 1, fun h01 => ?_⟩⟩
  have := congrArg (Uq.fund q hq hc) h01
  rw [map_zero, map_one] at this
  have := congrFun (congrFun this 0) 0
  simp at this

end Presented

end UqSl2

end QOU
