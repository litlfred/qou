import QOU.BraidKnot.CasimirShared
import Mathlib.Algebra.RingQuot
import Mathlib.Algebra.FreeAlgebra
import Mathlib.LinearAlgebra.Span.Basic
import Mathlib.Tactic

/-!
# QOU.QCasimir.exists — existence, centrality, and spin-`j` eigenvalue of the `q`-Casimir element

Formalises `prop:q-casimir-exists` (`\label{prop:q-casimir-exists}`):
1. `QCasimir.not_exists_unconstrained`: refutes existence on unconstrained `QuantumSu2` at `q = 0`.
2. **Generic `CommRing R` normalized `q`-Casimir (`UqRing`):**
   Over *any* commutative ring `R` in which `q : Rˣ` and `(q - q⁻¹)` is invertible
   (`[Invertible ((q : R) - ↑q⁻¹)]`), defines the exact normalized shifted `q`-Casimir
   `qCasimirNormRing q E F K K' := F * E + ⅟(q - q⁻¹)^2 • (q • K + q⁻¹ • K' - (q + q⁻¹) • 1)`,
   proves it commutes with `K, K', E, F` in any `R`-algebra `A` satisfying `UqRelsRing`,
   and proves it acts as the exact scalar `[j]_q [j + 1]_q · id` on every vector in any
   highest-weight spin-`j` module `V_j` (`j : ℕ`, spanned by `{F^r • v₀ | r : ℕ}` with
   `E • v₀ = 0`, `K • v₀ = q^{2j} • v₀`, `K' • v₀ = (q⁻¹)^{2j} • v₀`).
3. **Presented `U_q(sl₂)` (`UqSl2.Uq k q`):**
   Proves centrality of both `qCasimir` and the shifted `qCasimirNorm` across the entire
   presented algebra `Uq k q`, constructs `Uq.fund` (`2 × 2` spin-`1/2` representation),
   proves `Nontrivial (Uq k q)`, and proves `Uq.fund(qCasimirNorm) = ((q^2 + q⁻² - q - q⁻¹)/(q - q⁻¹)^2) • I₂`.

## References

- [leitner2026] §4-braids-and-knots/q-casimir-exists
- [kassel1995] Quantum Groups (Springer GTM 155), §VI.4
- [lusztig1993] Introduction to Quantum Groups (Birkhäuser)
-/

namespace QOU

noncomputable section

instance charZero_R_q_casimirExists : CharZero R_q :=
  charZero_of_injective_algebraMap (algebraMap ℚ R_q).injective

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

-- Ref: [kassel1995] Quantum Groups, §VI.4 (needs q invertible)
theorem QCasimir.not_exists_unconstrained :
    ¬ ∀ qs : QuantumSu2.{0}, Nonempty (QCasimirData qs) := by
  intro h
  obtain ⟨d⟩ := h QCasimir.qsZero
  have := d.qInv_left
  simp only [QCasimir.qsZero, mul_zero] at this
  exact zero_ne_one this

end

/-! ## Generic `CommRing R` Normalized `q`-Casimir and Spin-`j` Eigenvalue `[j]_q [j + 1]_q` -/

namespace UqRing

section CommRingCasimir

variable {R : Type*} [CommRing R] (q : Rˣ) [Invertible ((q : R) - (↑q⁻¹ : R))]

/-- Balanced symmetric `q`-integer `[n]_q = (q^n - q^{-n}) / (q - q⁻¹)` over any `CommRing R`
    with `q : Rˣ` and `(q - q⁻¹)` invertible. -/
def qIntSymRing (n : ℕ) : R :=
  ((q : R) ^ n - (↑q⁻¹ : R) ^ n) * ⅟((q : R) - (↑q⁻¹ : R))

/-- Spin-`j` Casimir eigenvalue `[j]_q [j + 1]_q` over any `CommRing R`. -/
def casimirEigenvalueRing (j : ℕ) : R :=
  qIntSymRing q j * qIntSymRing q (j + 1)

omit [Invertible ((q : R) - (↑q⁻¹ : R))] in
/-- Exact Laurent factorization underlying the spin-`j` Casimir eigenvalue:
    `q · q^{2j} + q⁻¹ · q^{-2j} - (q + q⁻¹) = (q^j - q^{-j})(q^{j+1} - q^{-(j+1)})`. -/
theorem highest_weight_laurent_factor (j : ℕ) :
    (q : R) * (q : R) ^ (2 * j) + (↑q⁻¹ : R) * (↑q⁻¹ : R) ^ (2 * j) - ((q : R) + (↑q⁻¹ : R)) =
      ((q : R) ^ j - (↑q⁻¹ : R) ^ j) * ((q : R) ^ (j + 1) - (↑q⁻¹ : R) ^ (j + 1)) := by
  have hq : (q : R) * (↑q⁻¹ : R) = 1 := q.mul_inv
  have hqp : (q : R) ^ j * (↑q⁻¹ : R) ^ j = 1 := by
    rw [← mul_pow, hq, one_pow]
  calc (q : R) * (q : R) ^ (2 * j) + (↑q⁻¹ : R) * (↑q⁻¹ : R) ^ (2 * j) - ((q : R) + (↑q⁻¹ : R))
      = (q : R) ^ j * (q : R) ^ (j + 1) + (↑q⁻¹ : R) ^ j * (↑q⁻¹ : R) ^ (j + 1) -
          (q : R) * ((q : R) ^ j * (↑q⁻¹ : R) ^ j) -
          (↑q⁻¹ : R) * ((q : R) ^ j * (↑q⁻¹ : R) ^ j) := by
        rw [hqp, two_mul, pow_add, pow_add]
        ring
    _ = ((q : R) ^ j - (↑q⁻¹ : R) ^ j) * ((q : R) ^ (j + 1) - (↑q⁻¹ : R) ^ (j + 1)) := by
        ring

theorem highest_weight_casimir_scalar_eq (j : ℕ) :
    (⅟((q : R) - (↑q⁻¹ : R)) ^ 2) *
        ((q : R) * (q : R) ^ (2 * j) + (↑q⁻¹ : R) * (↑q⁻¹ : R) ^ (2 * j) -
          ((q : R) + (↑q⁻¹ : R))) =
      casimirEigenvalueRing q j := by
  unfold casimirEigenvalueRing qIntSymRing
  rw [highest_weight_laurent_factor q j]
  ring

variable {A : Type*} [Ring A] [Algebra R A]

/-- Defining relations of `𝒰_q(𝔰𝔲(2))` over any commutative ring `R` in which `q` and `q - q⁻¹`
    are invertible. -/
structure UqRelsRing (E F K K' : A) : Prop where
  kk' : K * K' = 1
  k'k : K' * K = 1
  ke : K * E = ((q : R) ^ 2) • (E * K)
  kf : K * F = ((↑q⁻¹ : R) ^ 2) • (F * K)
  ef : E * F = F * E + ⅟((q : R) - (↑q⁻¹ : R)) • (K - K')

/-- Normalized shifted `q`-Casimir element over `R`:
    `C_q = F E + (q K + q⁻¹ K⁻¹ - (q + q⁻¹) · 1) / (q - q⁻¹)^2`. -/
def qCasimirNormRing (E F K K' : A) : A :=
  F * E + (⅟((q : R) - (↑q⁻¹ : R)) ^ 2) •
    ((q : R) • K + (↑q⁻¹ : R) • K' - ((q : R) + (↑q⁻¹ : R)) • (1 : A))

theorem UqRelsRing.k'e {q : Rˣ} [Invertible ((q : R) - (↑q⁻¹ : R))]
    {E F K K' : A} (h : UqRelsRing q E F K K') :
    K' * E = ((↑q⁻¹ : R) ^ 2) • (E * K') := by
  have hq : (↑q⁻¹ : R) * (q : R) = 1 := q.inv_mul
  have ek : E * K = ((↑q⁻¹ : R) ^ 2) • (K * E) := by
    rw [h.ke, smul_smul, ← mul_pow, hq, one_pow, one_smul]
  calc K' * E = K' * (E * K) * K' := by rw [mul_assoc, mul_assoc, h.kk', mul_one]
    _ = ((↑q⁻¹ : R) ^ 2) • (E * K') := by
      rw [ek, mul_smul_comm, smul_mul_assoc, ← mul_assoc, h.k'k, one_mul]

theorem UqRelsRing.k'f {q : Rˣ} [Invertible ((q : R) - (↑q⁻¹ : R))]
    {E F K K' : A} (h : UqRelsRing q E F K K') :
    K' * F = ((q : R) ^ 2) • (F * K') := by
  have hq : (q : R) * (↑q⁻¹ : R) = 1 := q.mul_inv
  have fk : F * K = ((q : R) ^ 2) • (K * F) := by
    rw [h.kf, smul_smul, ← mul_pow, hq, one_pow, one_smul]
  calc K' * F = K' * (F * K) * K' := by rw [mul_assoc, mul_assoc, h.kk', mul_one]
    _ = ((q : R) ^ 2) • (F * K') := by
      rw [fk, mul_smul_comm, smul_mul_assoc, ← mul_assoc, h.k'k, one_mul]

theorem qCasimirNormRing_comm_K {q : Rˣ} [Invertible ((q : R) - (↑q⁻¹ : R))]
    {E F K K' : A} (h : UqRelsRing q E F K K') :
    qCasimirNormRing q E F K K' * K = K * qCasimirNormRing q E F K K' := by
  have hq : (↑q⁻¹ : R) * (q : R) = 1 := q.inv_mul
  unfold qCasimirNormRing
  simp only [add_mul, mul_add, sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm,
    one_mul, mul_one, h.kk', h.k'k]
  rw [mul_assoc F E K, ← mul_assoc K F E, h.kf, smul_mul_assoc, mul_assoc, h.ke,
    mul_smul_comm, smul_smul, ← mul_assoc, ← mul_pow, hq, one_pow, one_smul]

theorem qCasimirNormRing_comm_K' {q : Rˣ} [Invertible ((q : R) - (↑q⁻¹ : R))]
    {E F K K' : A} (h : UqRelsRing q E F K K') :
    qCasimirNormRing q E F K K' * K' = K' * qCasimirNormRing q E F K K' := by
  have hq : (q : R) * (↑q⁻¹ : R) = 1 := q.mul_inv
  have hk'f := h.k'f
  have hk'e := h.k'e
  unfold qCasimirNormRing
  simp only [add_mul, mul_add, sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm,
    one_mul, mul_one, h.kk', h.k'k]
  rw [mul_assoc F E K', ← mul_assoc K' F E, hk'f, smul_mul_assoc, mul_assoc, hk'e,
    mul_smul_comm, smul_smul, ← mul_assoc, ← mul_pow, hq, one_pow, one_smul]

theorem qCasimirNormRing_comm_E {q : Rˣ} [Invertible ((q : R) - (↑q⁻¹ : R))]
    {E F K K' : A} (h : UqRelsRing q E F K K') :
    qCasimirNormRing q E F K K' * E = E * qCasimirNormRing q E F K K' := by
  have hq : (q : R) * (↑q⁻¹ : R) = 1 := q.mul_inv
  have hd : ((q : R) - (↑q⁻¹ : R)) * ⅟((q : R) - (↑q⁻¹ : R)) = 1 := mul_invOf_self _
  have hk'e := h.k'e
  unfold qCasimirNormRing
  simp only [add_mul, mul_add, sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm,
    smul_add, smul_sub, smul_smul, one_mul, mul_one, mul_assoc]
  rw [← mul_assoc E F E, h.ef]
  simp only [add_mul, sub_mul, smul_mul_assoc, smul_sub, smul_smul, mul_assoc, h.ke, hk'e]
  have hsK :
      ⅟((q : R) - (↑q⁻¹ : R)) ^ 2 * ((q : R) * (q : R) ^ 2) =
        ⅟((q : R) - (↑q⁻¹ : R)) * (q : R) ^ 2 + ⅟((q : R) - (↑q⁻¹ : R)) ^ 2 * (q : R) := by
    linear_combination
      (⅟((q : R) - (↑q⁻¹ : R)) * (q : R) ^ 2) * hd +
      (⅟((q : R) - (↑q⁻¹ : R)) ^ 2 * (q : R)) * hq
  have hsK' :
      ⅟((q : R) - (↑q⁻¹ : R)) ^ 2 * ((↑q⁻¹ : R) * (↑q⁻¹ : R) ^ 2) =
        -(⅟((q : R) - (↑q⁻¹ : R)) * (↑q⁻¹ : R) ^ 2) +
          ⅟((q : R) - (↑q⁻¹ : R)) ^ 2 * (↑q⁻¹ : R) := by
    linear_combination
      -(⅟((q : R) - (↑q⁻¹ : R)) * (↑q⁻¹ : R) ^ 2) * hd +
      (⅟((q : R) - (↑q⁻¹ : R)) ^ 2 * (↑q⁻¹ : R)) * hq
  rw [hsK, hsK', add_smul, add_smul, neg_smul]
  abel

theorem qCasimirNormRing_comm_F {q : Rˣ} [Invertible ((q : R) - (↑q⁻¹ : R))]
    {E F K K' : A} (h : UqRelsRing q E F K K') :
    qCasimirNormRing q E F K K' * F = F * qCasimirNormRing q E F K K' := by
  have hq : (q : R) * (↑q⁻¹ : R) = 1 := q.mul_inv
  have hd : ((q : R) - (↑q⁻¹ : R)) * ⅟((q : R) - (↑q⁻¹ : R)) = 1 := mul_invOf_self _
  have hk'f := h.k'f
  unfold qCasimirNormRing
  simp only [add_mul, mul_add, sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm,
    smul_add, smul_sub, smul_smul, one_mul, mul_one, mul_assoc]
  rw [h.ef]
  simp only [mul_add, mul_sub, mul_smul_comm, smul_sub, smul_smul, mul_assoc, h.kf, hk'f]
  have htK :
      ⅟((q : R) - (↑q⁻¹ : R)) ^ 2 * ((q : R) * (↑q⁻¹ : R) ^ 2) =
        -⅟((q : R) - (↑q⁻¹ : R)) + ⅟((q : R) - (↑q⁻¹ : R)) ^ 2 * (q : R) := by
    linear_combination
      -⅟((q : R) - (↑q⁻¹ : R)) * hd +
      (⅟((q : R) - (↑q⁻¹ : R)) ^ 2 * (↑q⁻¹ : R)) * hq
  have htK' :
      ⅟((q : R) - (↑q⁻¹ : R)) ^ 2 * ((↑q⁻¹ : R) * (q : R) ^ 2) =
        ⅟((q : R) - (↑q⁻¹ : R)) + ⅟((q : R) - (↑q⁻¹ : R)) ^ 2 * (↑q⁻¹ : R) := by
    linear_combination
      ⅟((q : R) - (↑q⁻¹ : R)) * hd +
      (⅟((q : R) - (↑q⁻¹ : R)) ^ 2 * (q : R)) * hq
  rw [htK, htK', add_smul, add_smul, neg_smul]
  abel

theorem qCasimirNormRing_comm_F_pow {q : Rˣ} [Invertible ((q : R) - (↑q⁻¹ : R))]
    {E F K K' : A} (h : UqRelsRing q E F K K') (r : ℕ) :
    qCasimirNormRing q E F K K' * (F ^ r) = (F ^ r) * qCasimirNormRing q E F K K' :=
  (Commute.pow_right (qCasimirNormRing_comm_F h) r).eq

/-- **Action of `C_q` on any spin-`j` highest-weight vector `v₀`:**
    Whenever `E • v₀ = 0`, `K • v₀ = q^{2j} • v₀`, and `K' • v₀ = (q⁻¹)^{2j} • v₀`,
    `qCasimirNormRing` acts on `v₀` as `[j]_q [j + 1]_q • v₀`. -/
theorem qCasimirNormRing_smul_highestWeight
    {V : Type*} [AddCommGroup V] [Module R V] [Module A V] [IsScalarTower R A V]
    {E F K K' : A} (j : ℕ) {v₀ : V}
    (hE : E • v₀ = 0)
    (hK : K • v₀ = ((q : R) ^ (2 * j)) • v₀)
    (hK' : K' • v₀ = ((↑q⁻¹ : R) ^ (2 * j)) • v₀) :
    qCasimirNormRing q E F K K' • v₀ = (casimirEigenvalueRing q j) • v₀ := by
  unfold qCasimirNormRing
  rw [add_smul, mul_smul, hE, smul_zero, zero_add, smul_assoc]
  rw [sub_smul, add_smul, smul_assoc, smul_assoc, smul_assoc, one_smul, hK, hK']
  rw [smul_smul, smul_smul, ← add_smul, ← sub_smul, smul_smul]
  rw [highest_weight_casimir_scalar_eq q j]

/-- **Action of `C_q` as `[j]_q [j + 1]_q · id` across the entire spin-`j` module `V_j`:**
    On every vector `v` in the `R`-submodule spanned by `{F^r • v₀ | r : ℕ}` (in particular,
    on every simple highest-weight module `V_j` generated by `v₀` over `R`),
    `qCasimirNormRing • v = [j]_q [j + 1]_q • v`. -/
theorem qCasimirNormRing_acts_as_eigenvalue_on_Vj
    {V : Type*} [AddCommGroup V] [Module R V] [Module A V] [IsScalarTower R A V]
    {E F K K' : A} (h : UqRelsRing q E F K K') (j : ℕ) {v₀ : V}
    (hE : E • v₀ = 0)
    (hK : K • v₀ = ((q : R) ^ (2 * j)) • v₀)
    (hK' : K' • v₀ = ((↑q⁻¹ : R) ^ (2 * j)) • v₀)
    {v : V} (hv : v ∈ Submodule.span R (Set.range (fun r : ℕ => (F ^ r) • v₀))) :
    qCasimirNormRing q E F K K' • v = (casimirEigenvalueRing q j) • v := by
  refine Submodule.span_induction ?_ ?_ ?_ ?_ hv
  · rintro _ ⟨r, rfl⟩
    rw [← mul_smul, qCasimirNormRing_comm_F_pow h r, mul_smul,
      qCasimirNormRing_smul_highestWeight q j hE hK hK']
    rw [← algebraMap_smul A (casimirEigenvalueRing q j) v₀, ← mul_smul,
      ← Algebra.commutes (casimirEigenvalueRing q j) (F ^ r), mul_smul,
      algebraMap_smul]
  · simp
  · intro x y _ _ hx hy
    rw [smul_add, hx, hy, smul_add]
  · intro c x _ hx
    rw [← algebraMap_smul A c x, ← mul_smul,
      ← Algebra.commutes c (qCasimirNormRing q E F K K'),
      mul_smul, algebraMap_smul, hx, smul_comm, algebraMap_smul]

end CommRingCasimir

end UqRing

/-! ## Field Presentation `UqSl2.Uq k q` and Spin-`1/2` Matrix Action -/

namespace UqSl2

variable {k : Type*} [Field k] {A : Type*} [Ring A] [Algebra k A]

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

/-- Unshifted quantum Casimir `C = F E + (q K + q⁻¹ K') / (q − q⁻¹)²`. -/
def qCasimir (q : k) (E F K K' : A) : A :=
  F * E + ((q - q⁻¹)⁻¹ ^ 2) • (q • K + q⁻¹ • K')

/-- Normalized shifted quantum Casimir `C_q = F E + (q K + q⁻¹ K' - (q + q⁻¹)) / (q - q⁻¹)²`. -/
def qCasimirNorm (q : k) (E F K K' : A) : A :=
  qCasimir q E F K K' - (((q + q⁻¹) * ((q - q⁻¹)⁻¹ ^ 2))) • (1 : A)

namespace UqRels
variable {q : k} {E F K K' : A}

theorem casimir_comm_K (h : UqRels q E F K K') (hq : q ≠ 0) :
    qCasimir q E F K K' * K = K * qCasimir q E F K K' := by
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
  simp only [add_mul, sub_mul, smul_mul_assoc, smul_sub, smul_smul, mul_assoc, h.ke, hk'e]
  have hq2 : q ^ 2 - 1 ≠ 0 := by
    intro h0; apply hc; field_simp; linear_combination h0
  match_scalars <;> field_simp <;> ring

theorem casimir_comm_F (h : UqRels q E F K K') (hq : q ≠ 0) (hc : q - q⁻¹ ≠ 0) :
    qCasimir q E F K K' * F = F * qCasimir q E F K K' := by
  have hk'f := h.k'f hq
  unfold qCasimir
  simp only [add_mul, mul_add, smul_mul_assoc, mul_smul_comm, smul_add, mul_assoc]
  rw [h.ef]
  simp only [mul_add, mul_sub, mul_smul_comm, smul_sub, smul_smul, h.kf, hk'f]
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

section Presented
variable (k)

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

abbrev Uq (q : k) := RingQuot (UqRel k q)

variable {k}

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

/-- **Centrality of the normalized shifted Casimir `C_q` in `U_q(sl₂)`.** -/
theorem Uq.casimirNorm_central (q : k) (hq : q ≠ 0) (hc : q - q⁻¹ ≠ 0) (a : Uq k q) :
    qCasimirNorm q (Uq.gen q 0) (Uq.gen q 1) (Uq.gen q 2) (Uq.gen q 3) * a
      = a * qCasimirNorm q (Uq.gen q 0) (Uq.gen q 1) (Uq.gen q 2) (Uq.gen q 3) := by
  unfold qCasimirNorm
  rw [sub_mul, mul_sub, Uq.casimir_central q hq hc a, smul_mul_assoc, mul_smul_comm,
    one_mul, mul_one]

def Uq.fundGen (q : k) : Fin 4 → Matrix (Fin 2) (Fin 2) k
  | 0 => !![0, 1; 0, 0]
  | 1 => !![0, 0; 1, 0]
  | 2 => !![q, 0; 0, q⁻¹]
  | 3 => !![q⁻¹, 0; 0, q]

noncomputable def Uq.fund (q : k) (hq : q ≠ 0) (hc : q - q⁻¹ ≠ 0) :
    Uq k q →ₐ[k] Matrix (Fin 2) (Fin 2) k :=
  RingQuot.liftAlgHom k ⟨FreeAlgebra.lift k (Uq.fundGen q), fun x y hxy => by
    have hq2 : -1 + q ^ 2 ≠ 0 := by
      intro h0; apply hc; field_simp; linear_combination h0
    cases hxy <;> simp only [map_mul, map_one, map_add, map_smul, map_sub,
      FreeAlgebra.lift_ι_apply, Uq.fundGen] <;> ext i j <;> fin_cases i <;> fin_cases j <;>
      simp [Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring_nf <;> field_simp <;> ring⟩

/-- Explicit action of `qCasimirNorm` on the 2D spin-`1/2` fundamental module `V_{1/2}`:
    `Uq.fund(C_q) = ((q^2 + q⁻² - (q + q⁻¹)) / (q - q⁻¹)^2) • I₂ = [1/2]_q [3/2]_q • I₂`. -/
theorem Uq.fund_casimirNorm (q : k) (hq : q ≠ 0) (hc : q - q⁻¹ ≠ 0) :
    Uq.fund q hq hc (qCasimirNorm q (Uq.gen q 0) (Uq.gen q 1) (Uq.gen q 2) (Uq.gen q 3)) =
      ((q ^ 2 + q⁻¹ ^ 2 - (q + q⁻¹)) / (q - q⁻¹) ^ 2) • (1 : Matrix (Fin 2) (Fin 2) k) := by
  have hgen : ∀ i : Fin 4, Uq.fund q hq hc (Uq.gen q i) = Uq.fundGen q i := fun i => by
    simp [Uq.fund, Uq.gen]
  have hq4 : 1 - q ^ 2 * 2 + q ^ 4 ≠ 0 := by
    intro h0
    have hsq : (q ^ 2 - 1) ^ 2 = 0 := by linear_combination h0
    have hq2 : q ^ 2 - 1 = 0 := sq_eq_zero_iff.mp hsq
    apply hc; field_simp; linear_combination hq2
  unfold qCasimirNorm qCasimir
  simp only [map_sub, map_add, map_mul, map_smul, map_one, hgen, Uq.fundGen]
  ext i j
  fin_cases i <;> fin_cases j
  · simp; field_simp
  · simp
  · simp
  · simp; field_simp
    have hinv := mul_inv_cancel₀ hq4
    linear_combination -hinv

theorem Uq.nontrivial (q : k) (hq : q ≠ 0) (hc : q - q⁻¹ ≠ 0) : Nontrivial (Uq k q) := by
  refine ⟨⟨0, 1, fun h01 => ?_⟩⟩
  have := congrArg (Uq.fund q hq hc) h01
  rw [map_zero, map_one] at this
  have := congrFun (congrFun this 0) 0
  simp at this

end Presented

end UqSl2

end QOU
