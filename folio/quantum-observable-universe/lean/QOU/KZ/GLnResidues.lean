import QOU.KZ.FuchsianFormal
import Mathlib.RingTheory.Adjoin.Basic
import Mathlib.Algebra.Algebra.Bilinear

/-!
# The `𝔤𝔩_n` residues of the KZ system: infinitesimal braid relations and non-resonance

Stage S1 of bean `qou-zoyv` (the Drinfeld category `D_ℏ`).

## Annihilating polynomial of `ad_A`

If `A` is annihilated by a split polynomial `p = ∏_i (X − a_i)`, then `ad_A = L_A − R_A` is
annihilated by `∏_{i,j} (X − (a_i − a_j))` (`aeval_adL_eq_zero`). The proof is the ideal
membership in two commuting variables: `p(x − y + a_j) − p(x)` is divisible by `a_j − y`, so
`∏_j p(x − y + a_j) ≡ ±∏_j (y − a_j) · (…) = ±q(y)(…)` modulo `p(x)`.

Consequently, if the roots are integer multiples of `c` and `c ∉ ℚ`, then `A` is non-resonant
(`nonResonant_of_int_roots`).

Base ring (§7c): generic field `K`, ring `R`. Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S1)
-/

namespace QOU.KZ.GLnResidues

open Polynomial QOU.KZ.FuchsianFormal

section Annihilator

variable {K E : Type*} [Field K] [Ring E] [Algebra K E]

/-- **Two commuting operators annihilated by the same split polynomial.** If `x, y` commute and
`p = ∏_i (X − a_i)` kills both, then `∏_j ∏_i (X − (a_i − a_j))` kills `x − y`. -/
theorem aeval_sub_eq_zero_of_commute {ι : Type*} [Fintype ι] (a : ι → K) (x y : E)
    (hxy : Commute x y) (hx : aeval x (∏ i, (X - C (a i))) = 0)
    (hy : aeval y (∏ i, (X - C (a i))) = 0) :
    aeval (x - y) (∏ j, ∏ i, (X - C (a i - a j))) = 0 := by
  classical
  let s : Set E := {x, y}
  have hs : ∀ u ∈ s, ∀ v ∈ s, u * v = v * u := by
    intro u hu v hv
    rcases hu with rfl | hu <;> rcases hv with rfl | hv
    · rfl
    · rw [Set.mem_singleton_iff.1 hv]; exact hxy.eq
    · rw [Set.mem_singleton_iff.1 hu]; exact hxy.eq.symm
    · rw [Set.mem_singleton_iff.1 hu, Set.mem_singleton_iff.1 hv]
  letI : CommRing (Algebra.adjoin K s) := Algebra.adjoinCommRingOfComm K hs
  let X' : Algebra.adjoin K s := ⟨x, Algebra.subset_adjoin (by simp [s])⟩
  let Y' : Algebra.adjoin K s := ⟨y, Algebra.subset_adjoin (by simp [s])⟩
  set p : K[X] := ∏ i, (X - C (a i))
  -- evaluation in the commutative subalgebra
  have ev : ∀ (f : K[X]) (z : Algebra.adjoin K s),
      aeval z f = (f.map (algebraMap K (Algebra.adjoin K s))).eval z := fun f z => by
    rw [aeval_def, eval_map]
  have hX' : aeval X' p = 0 := Subtype.ext (by rw [aeval_subalgebra_coe]; exact hx)
  have hY' : aeval Y' p = 0 := Subtype.ext (by rw [aeval_subalgebra_coe]; exact hy)
  set P := p.map (algebraMap K (Algebra.adjoin K s))
  have hPX : P.eval X' = 0 := by rw [← ev]; exact hX'
  -- for each `j`, `P(X' − Y' + a_j) = (Y' − a_j) * g_j`
  have key : ∀ j, ∃ g : Algebra.adjoin K s,
      P.eval (X' - Y' + algebraMap K _ (a j)) = (Y' - algebraMap K _ (a j)) * g := by
    intro j
    obtain ⟨g, hg⟩ := sub_dvd_eval_sub X' (X' - Y' + algebraMap K _ (a j)) P
    refine ⟨-g, ?_⟩
    have : P.eval X' - P.eval (X' - Y' + algebraMap K _ (a j)) =
        (Y' - algebraMap K _ (a j)) * g := by
      rw [hg]; congr 1; abel
    rw [hPX, zero_sub] at this
    rw [mul_neg, ← this, neg_neg]
  choose g hg using key
  have hprod : eval (X' - Y') ((∏ j, ∏ i, (X - C (a i - a j)) : K[X]).map
      (algebraMap K (Algebra.adjoin K s))) = ∏ j, P.eval (X' - Y' + algebraMap K _ (a j)) := by
    simp only [P, p, Polynomial.map_prod, eval_prod, Polynomial.map_sub, map_X, map_C, eval_sub,
      eval_X, eval_C, map_sub]
    refine Finset.prod_congr rfl fun j _ => Finset.prod_congr rfl fun i _ => by ring
  have hY'' : ∏ j, (Y' - algebraMap K _ (a j)) = 0 := by
    rw [← hY', ev]
    simp [p, Polynomial.map_prod, eval_prod]
  have : aeval (X' - Y') (∏ j, ∏ i, (X - C (a i - a j))) = 0 := by
    rw [ev, hprod, Finset.prod_congr rfl fun j _ => hg j, Finset.prod_mul_distrib, hY'', zero_mul]
  have h2 := congrArg Subtype.val this
  rw [aeval_subalgebra_coe] at h2
  exact h2

/-- `L_A` and `R_A` are annihilated by every polynomial annihilating `A`. -/
theorem aeval_mulLeft (A : E) (f : K[X]) :
    aeval (LinearMap.mulLeft K A) f = LinearMap.mulLeft K (aeval A f) :=
  aeval_algHom_apply (Algebra.lmul K E) A f

theorem aeval_mulRight (A : E) (f : K[X]) :
    aeval (LinearMap.mulRight K A) f = LinearMap.mulRight K (aeval A f) := by
  induction f using Polynomial.induction_on' with
  | add f g hf hg => rw [map_add, map_add, hf, hg]; ext Z; simp [mul_add]
  | monomial n c =>
    ext Z
    simp [aeval_monomial, LinearMap.pow_mulRight, Algebra.smul_def, mul_assoc,
      Algebra.commutes]

/-- **Annihilator of `ad_A`.** If `∏_i (A − a_i) = 0`, then
`∏_j ∏_i (ad_A − (a_i − a_j)) = 0`. -/
theorem aeval_adL_eq_zero {ι : Type*} [Fintype ι] (a : ι → K) (A : E)
    (hA : aeval A (∏ i, (X - C (a i))) = 0) :
    aeval (adL (K := K) A) (∏ j, ∏ i, (X - C (a i - a j))) = 0 :=
  aeval_sub_eq_zero_of_commute a _ _ (LinearMap.commute_mulLeft_right A A)
    (by rw [aeval_mulLeft, hA, LinearMap.mulLeft_zero_eq_zero])
    (by rw [aeval_mulRight, hA, LinearMap.mulRight_zero_eq_zero])

/-- **Non-resonance from integer roots and an irrational coupling.** If `A` is killed by
`∏_i (X − m_i c)` with `m_i ∈ ℤ` and `c ∉ ℚ`, then `A` is non-resonant. -/
theorem nonResonant_of_int_roots [CharZero K] {ι : Type*} [Fintype ι] (m : ι → ℤ) (c : K)
    (hc : ∀ r : ℚ, (r : K) ≠ c) (A : E)
    (hA : aeval A (∏ i, (X - C ((m i : K) * c))) = 0) : NonResonant A := by
  refine nonResonant_of_aeval (K := K) A _ (aeval_adL_eq_zero _ A hA) fun k hk => ?_
  simp only [eval_prod, eval_sub, eval_X, eval_C]
  refine Finset.prod_ne_zero_iff.2 fun j _ => Finset.prod_ne_zero_iff.2 fun i _ => ?_
  intro h
  by_cases hm : m i - m j = 0
  · have : (k : K) = 0 := by
      have hm' : ((m i : K) - m j) = 0 := by exact_mod_cast hm
      linear_combination h + c * hm'
    exact (Nat.cast_ne_zero.2 hk.ne') this
  · apply hc ((k : ℚ) / ((m i - m j : ℤ) : ℚ))
    have hm' : ((m i - m j : ℤ) : K) ≠ 0 := by exact_mod_cast hm
    push_cast at hm' ⊢
    field_simp
    linear_combination h

/-- **Scaling the roots.** If `∏_i (S − m_i) = 0` then `∏_i (c S − m_i c) = 0`. -/
theorem aeval_smul_of_roots {ι : Type*} [Fintype ι] (m : ι → K) (c : K) (S : E)
    (hS : aeval S (∏ i, (X - C (m i))) = 0) :
    aeval (c • S) (∏ i, (X - C (m i * c))) = 0 := by
  have hcomp : (∏ i, (X - C (m i * c))).comp (C c * X) = C (c ^ Fintype.card ι) *
      ∏ i, (X - C (m i)) := by
    rw [prod_comp, Finset.card_univ.symm, map_pow, ← Finset.prod_const, ← Finset.prod_mul_distrib]
    refine Finset.prod_congr rfl fun i _ => ?_
    simp only [sub_comp, X_comp, C_comp, mul_sub, ← C_mul]
    ring_nf
  have hcS : aeval S (C c * X) = c • S := by
    rw [map_mul, aeval_C, aeval_X, Algebra.smul_def]
  rw [← hcS, ← aeval_comp, hcomp, map_mul, hS, mul_zero]

end Annihilator

/-! ### Sums of transpositions -/

section Transpositions

variable {R : Type*} [Ring R]

/-- Three involutions permuted by conjugation like the transpositions of `S₃`
(`ab = bc = ca`, `ac = cb = ba`): their sum `S` satisfies `S³ = 9 S`. -/
theorem sum_three_cube (a b c : R) (ha : a * a = 1) (hb : b * b = 1) (hc : c * c = 1)
    (h1 : a * b = b * c) (h2 : b * c = c * a) (h3 : a * c = c * b) (h4 : c * b = b * a) :
    (a + b + c) * (a + b + c) * (a + b + c) = 9 • (a + b + c) := by
  have hSq : (a + b + c) * (a + b + c) = 3 • 1 + 3 • (a * b) + 3 • (b * a) := by
    have e1 : b * c = a * b := h1.symm
    have e2 : c * a = a * b := h2.symm.trans h1.symm
    have e3 : a * c = b * a := h3.trans h4
    have e4 : c * b = b * a := h4
    simp only [add_mul, mul_add, ha, hb, hc, e1, e2, e3, e4]
    abel
  have hu : (a + b + c) * (a * b) = a + b + c := by
    have t1 : a * (a * b) = b := by rw [← mul_assoc, ha, one_mul]
    have t2 : b * (a * b) = c := by rw [h1, ← mul_assoc, hb, one_mul]
    have t3 : c * (a * b) = a := by rw [h1, h2, ← mul_assoc, hc, one_mul]
    rw [add_mul, add_mul, t1, t2, t3]; abel
  have hv : (a + b + c) * (b * a) = a + b + c := by
    have t1 : a * (b * a) = c := by rw [← h4, ← h3, ← mul_assoc, ha, one_mul]
    have t2 : b * (b * a) = a := by rw [← mul_assoc, hb, one_mul]
    have t3 : c * (b * a) = b := by rw [← h4, ← mul_assoc, hc, one_mul]
    rw [add_mul, add_mul, t1, t2, t3]; abel
  rw [mul_assoc, hSq, mul_add, mul_add, mul_smul_comm, mul_smul_comm, mul_smul_comm, hu, hv,
    mul_one]
  abel

/-- Two involutions satisfying the braid relation `aba = bab` (the transpositions `(12), (23)` of
`S₃`): their sum `Q` satisfies `Q⁴ + 4 = 5 Q²`, i.e. `(Q² − 1)(Q² − 4) = 0`. -/
theorem sum_two_quartic (a b : R) (ha : a * a = 1) (hb : b * b = 1)
    (hab : a * b * a = b * a * b) :
    (a + b) * (a + b) * ((a + b) * (a + b)) + 4 • 1 = 5 • ((a + b) * (a + b)) := by
  have hSq : (a + b) * (a + b) = 2 • 1 + a * b + b * a := by
    simp only [add_mul, mul_add, ha, hb]; abel
  have huu : a * b * (a * b) = b * a := by
    rw [← mul_assoc, hab, mul_assoc, hb, mul_one]
  have hvv : b * a * (b * a) = a * b := by
    rw [← mul_assoc, ← hab, mul_assoc, ha, mul_one]
  have huv : a * b * (b * a) = 1 := by rw [mul_assoc, ← mul_assoc b, hb, one_mul, ha]
  have hvu : b * a * (a * b) = 1 := by rw [mul_assoc, ← mul_assoc a, ha, one_mul, hb]
  rw [hSq]
  simp only [add_mul, mul_add, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, huu, hvv, huv,
    hvu, smul_add, smul_smul]
  abel

end Transpositions

/-! ### Permutations of tensor factors -/

section Perm

variable (K : Type*) [Field K] (n : ℕ) {m : ℕ}

/-- The action of `σ ∈ S_m` on `V^{⊗m}`, `V = K^n`, as a matrix indexed by `Fin m → Fin n`
(column `x` is the basis vector `e_{x ∘ σ}`). -/
def permP (σ : Equiv.Perm (Fin m)) : Matrix (Fin m → Fin n) (Fin m → Fin n) K :=
  permMat K (fun x => x ∘ σ)

theorem permP_mul (σ τ : Equiv.Perm (Fin m)) :
    permP K n σ * permP K n τ = permP K n (τ * σ) :=
  permMat_mul K _ _

theorem permP_one : permP K n (1 : Equiv.Perm (Fin m)) = 1 := by
  ext i j
  simp [permP, permMat, Matrix.one_apply, eq_comm]

theorem permP_mul_self_of_mul_self {σ : Equiv.Perm (Fin m)} (h : σ * σ = 1) :
    permP K n σ * permP K n σ = 1 := by
  rw [permP_mul, h, permP_one]

/-- The flip `P_{ij}` of the tensor legs `i` and `j`. -/
abbrev flipP (i j : Fin m) : Matrix (Fin m → Fin n) (Fin m → Fin n) K :=
  permP K n (Equiv.swap i j)

theorem flipP_mul_self (i j : Fin m) : flipP K n i j * flipP K n i j = 1 :=
  permP_mul_self_of_mul_self K n (Equiv.swap_mul_self i j)

/-- The elementary matrix `E_{ab}` acting on tensor leg `i` of `V^{⊗m}`. -/
def legE (i : Fin m) (a b : Fin n) : Matrix (Fin m → Fin n) (Fin m → Fin n) K :=
  Matrix.of fun x y => if y i = b ∧ x = Function.update y i a then 1 else 0

/-- The split `𝔤𝔩_n` Casimir (trace form) on legs `i, j`: `t_{ij} = ∑_{a,b} E^{(i)}_{ab} E^{(j)}_{ba}`. -/
def casimirLeg (i j : Fin m) : Matrix (Fin m → Fin n) (Fin m → Fin n) K :=
  ∑ a : Fin n, ∑ b : Fin n, legE K n i a b * legE K n j b a

/-- **The split Casimir on legs `i ≠ j` is the flip `P_{ij}`.** -/
theorem casimirLeg_eq_flipP {i j : Fin m} (hij : i ≠ j) :
    casimirLeg K n i j = flipP K n i j := by
  ext x z
  simp only [casimirLeg, legE, Matrix.sum_apply, Matrix.mul_apply, Matrix.of_apply, permP,
    permMat, flipP]
  simp only [mul_ite, mul_one, mul_zero, ite_and]
  simp only [Finset.sum_ite_irrel, Finset.sum_const_zero, Finset.sum_ite_eq, Finset.sum_ite_eq',
    Finset.mem_univ, if_true, Function.update_of_ne hij]
  have : Function.update (Function.update z j (z i)) i (z j) = z ∘ Equiv.swap i j := by
    funext k
    by_cases hki : k = i
    · subst hki; simp [Equiv.swap_apply_left]
    · by_cases hkj : k = j
      · subst hkj; simp [Function.update_of_ne hki, Equiv.swap_apply_right]
      · simp [Function.update_of_ne hki, Function.update_of_ne hkj,
          Equiv.swap_apply_of_ne_of_ne hki hkj]
  simp only [this, eq_comm]

end Perm

end QOU.KZ.GLnResidues
