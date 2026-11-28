import HeckeTemperleyLieb.TLGlued
import HeckeTemperleyLieb.TLSlideIso

/-!
# The tensor product of morphisms in the glued Temperley–Lieb category

Bean `hkmt`. For morphisms `φ : [a] → [a']` at level `n` and `ψ : [b] → [b']` at level `m`, the
level tensor is

  `V' · (φ ⊗ ψ) · U  :  [a + b + 1] → [a' + b' + 1]`   at level `n + m + 1`,

where `U`, `V'` are the slide words of `TLSlideIso`. They move the cups of the first factor past
the whole second block, so the tensor corner `P_a ⊗ P_b` becomes the standard corner
`P_{a+b+1}`.

* `tensLvl_mem`: the level tensor is a morphism `[a + b + 1] → [a' + b' + 1]`.
* `tensLvl_mul`, `tensLvl_id`: it is functorial.
* `tensLvl_capQ_left`, `tensLvl_capQ_right`: adding two strands to either factor is adding two
  strands to the tensor.

Everything holds over any field, with `δ ε = 1`; only the Temperley–Lieb relations are used.

-- Ref: [kauffman1987] State models and the Jones polynomial, §3.
-- Ref: [leitner2026] the Temperley–Lieb chapter (bean `hkmt`).
-/

namespace QOU.HeckeTemperleyLieb.TLGluedTensor

open CategoryTheory
open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebMarkov
open QOU.HeckeTemperleyLieb.TLCupCap QOU.HeckeTemperleyLieb.TLNegligible
open QOU.HeckeTemperleyLieb.TLCableBraiding QOU.HeckeTemperleyLieb.TLQuotientTensor
open QOU.HeckeTemperleyLieb.TLRectHom QOU.HeckeTemperleyLieb.TLQuotientModular
open QOU.HeckeTemperleyLieb.TLGlued QOU.HeckeTemperleyLieb.TLSlideIso

/-! ## Closed forms at any level of the right parity -/

section Closed

variable {K : Type*} [Field K] {δ : K}

theorem slideU_mul_slideV_P (hδ : δ ≠ 0) {a b n m : ℕ} (ha : a ≤ n) (hpa : n % 2 = a % 2) :
    slideU δ a m (P δ b m) n * slideV δ a m (P δ b m) n = tens δ (P δ a n) (P δ b m) := by
  obtain ⟨k, rfl⟩ : ∃ k, n = a + 2 * k := ⟨(n - a) / 2, by omega⟩
  exact slideU_mul_slideV hδ a m (P_idem δ hδ b m) k

theorem slideV_mul_slideU_P (hδ : δ ≠ 0) {a b n m : ℕ} (ha : a ≤ n) (hpa : n % 2 = a % 2)
    (hb : b ≤ m) (hpb : m % 2 = b % 2) :
    slideV δ a m (P δ b m) n * slideU δ a m (P δ b m) n = P δ (a + b + 1) (n + m + 1) := by
  obtain ⟨k, rfl⟩ : ∃ k, n = a + 2 * k := ⟨(n - a) / 2, by omega⟩
  obtain ⟨j, rfl⟩ : ∃ j, m = b + 2 * j := ⟨(m - b) / 2, by omega⟩
  exact slideV_mul_slideU hδ a (b + 2 * j) (a + b + 1) (P_idem δ hδ b _) (tens_one_P a b j)
    (by omega) k

theorem pl_zero_recast {L L' : ℕ} (hL : L = L') (h : 0 + L ≤ L') (z : TLFin K δ L) :
    pl δ 0 L h z = recast δ hL z := by
  subst hL; exact pl_zero_self _ _

end Closed

/-! ## The level tensor on the quotient -/

section Level

variable {K : Type*} [Field K] {δ ε : K} (T : MarkovTower δ ε) (hε : δ * ε = 1)

/-- The source slide word in the quotient. -/
noncomputable def sUQ (a b m n : ℕ) : Q T (n + m + 1) := (slideU δ a m (P δ b m) n : Q T _)

/-- The target slide word in the quotient. -/
noncomputable def sVQ (a b m n : ℕ) : Q T (n + m + 1) := (slideV δ a m (P δ b m) n : Q T _)

/-- **The level tensor** of `φ : [a] → [a']` at level `n` and `ψ : [b] → [b']` at level `m`. -/
noncomputable def tensLvl (a b a' b' : ℕ) {n m : ℕ} (φ : Q T n) (ψ : Q T m) : Q T (n + m + 1) :=
  sVQ T a' b' m n * tensQ T φ ψ * sUQ T a b m n

include hε in
theorem sUQ_mul_sVQ {a b n m : ℕ} (ha : a ≤ n) (hpa : n % 2 = a % 2) :
    sUQ T a b m n * sVQ T a b m n = tensQ T (PQ T a n) (PQ T b m) := by
  rw [sUQ, sVQ, ← RingCon.coe_mul, slideU_mul_slideV_P (left_ne_zero_of_mul_eq_one hε) ha hpa,
    PQ, PQ, tensQ_coe]

include hε in
theorem sVQ_mul_sUQ {a b n m : ℕ} (ha : a ≤ n) (hpa : n % 2 = a % 2) (hb : b ≤ m)
    (hpb : m % 2 = b % 2) :
    sVQ T a b m n * sUQ T a b m n = PQ T (a + b + 1) (n + m + 1) := by
  rw [sUQ, sVQ, ← RingCon.coe_mul,
    slideV_mul_slideU_P (left_ne_zero_of_mul_eq_one hε) ha hpa hb hpb, PQ]

include hε in
/-- **The level tensor is a morphism** `[a + b + 1] → [a' + b' + 1]`. -/
theorem tensLvl_mem {a b a' b' n m : ℕ} (ha : a ≤ n) (hpa : n % 2 = a % 2) (hb : b ≤ m)
    (hpb : m % 2 = b % 2) (ha' : a' ≤ n) (hpa' : n % 2 = a' % 2) (hb' : b' ≤ m)
    (hpb' : m % 2 = b' % 2) {φ : Q T n} {ψ : Q T m} (hφ : φ ∈ HomSp T n a a')
    (hψ : ψ ∈ HomSp T m b b') :
    tensLvl T a b a' b' φ ψ ∈ HomSp T (n + m + 1) (a + b + 1) (a' + b' + 1) := by
  rw [mem_Hom, ← sVQ_mul_sUQ T hε ha' hpa' hb' hpb', ← sVQ_mul_sUQ T hε ha hpa hb hpb, tensLvl]
  have hT : tensQ T (PQ T a' n) (PQ T b' m) * tensQ T φ ψ * tensQ T (PQ T a n) (PQ T b m) =
      tensQ T φ ψ := by
    rw [tensQ_mul, tensQ_mul, (mem_Hom T).mp hφ, (mem_Hom T).mp hψ]
  calc sVQ T a' b' m n * sUQ T a' b' m n * (sVQ T a' b' m n * tensQ T φ ψ * sUQ T a b m n) *
        (sVQ T a b m n * sUQ T a b m n)
      = sVQ T a' b' m n * ((sUQ T a' b' m n * sVQ T a' b' m n) * tensQ T φ ψ *
          (sUQ T a b m n * sVQ T a b m n)) * sUQ T a b m n := by simp only [mul_assoc]
    _ = _ := by rw [sUQ_mul_sVQ T hε ha' hpa', sUQ_mul_sVQ T hε ha hpa, hT]

include hε in
/-- **The level tensor is functorial.** -/
theorem tensLvl_mul {a b a' b' a'' b'' n m : ℕ} (ha' : a' ≤ n) (hpa' : n % 2 = a' % 2)
    {φ φ' : Q T n} {ψ ψ' : Q T m} (hφ' : φ' ∈ HomSp T n a' a'') (hψ' : ψ' ∈ HomSp T m b' b'') :
    tensLvl T a' b' a'' b'' φ' ψ' * tensLvl T a b a' b' φ ψ =
      tensLvl T a b a'' b'' (φ' * φ) (ψ' * ψ) := by
  unfold tensLvl
  calc sVQ T a'' b'' m n * tensQ T φ' ψ' * sUQ T a' b' m n *
        (sVQ T a' b' m n * tensQ T φ ψ * sUQ T a b m n)
      = sVQ T a'' b'' m n * (tensQ T φ' ψ' * (sUQ T a' b' m n * sVQ T a' b' m n) *
          tensQ T φ ψ) * sUQ T a b m n := by simp only [mul_assoc]
    _ = _ := by
      rw [sUQ_mul_sVQ T hε ha' hpa', tensQ_mul, tensQ_mul, right_mul_of_mem T hε hφ',
        right_mul_of_mem T hε hψ']

include hε in
/-- **The level tensor preserves identities.** -/
theorem tensLvl_id {a b n m : ℕ} (ha : a ≤ n) (hpa : n % 2 = a % 2) (hb : b ≤ m)
    (hpb : m % 2 = b % 2) :
    tensLvl T a b a b (PQ T a n) (PQ T b m) = PQ T (a + b + 1) (n + m + 1) := by
  rw [tensLvl, ← sUQ_mul_sVQ T hε ha hpa]
  calc sVQ T a b m n * (sUQ T a b m n * sVQ T a b m n) * sUQ T a b m n
      = (sVQ T a b m n * sUQ T a b m n) * (sVQ T a b m n * sUQ T a b m n) := by
        simp only [mul_assoc]
    _ = _ := by rw [sVQ_mul_sUQ T hε ha hpa hb hpb, PQ_idem T hε]

include hε in
/-- **Two more strands on the second factor** are two more strands on the tensor. -/
theorem tensLvl_capQ_right {a b a' b' n m : ℕ} (hb : b ≤ m) (hb' : b' ≤ m) (φ : Q T n)
    (ψ : Q T m) :
    tensLvl T a b a' b' φ (capQ T hε m ψ) = capQ T hε (n + m + 1) (tensLvl T a b a' b' φ ψ) := by
  obtain ⟨x, rfl⟩ := coe_surj T φ
  obtain ⟨y, rfl⟩ := coe_surj T ψ
  unfold tensLvl sUQ sVQ
  rw [capQ_coe, tensQ_coe, tensQ_coe, ← RingCon.coe_mul, ← RingCon.coe_mul, ← RingCon.coe_mul,
    ← RingCon.coe_mul, capQ_coe, P_succ_succ δ (by omega : b ≠ m + 1 + 1),
    P_succ_succ δ (by omega : b' ≠ m + 1 + 1),
    slide_conj_capEmb_right (left_ne_zero_of_mul_eq_one hε)]

include hε in
/-- **Two more strands on the first factor** are two more strands on the tensor. -/
theorem tensLvl_capQ_left {a b a' b' n m : ℕ} (ha : a ≤ n) (ha' : a' ≤ n) (φ : Q T n)
    (ψ : Q T m) :
    tensLvl T a b a' b' (capQ T hε n φ) ψ =
      recastQ T (by omega) (capQ T hε (n + m + 1) (tensLvl T a b a' b' φ ψ)) := by
  obtain ⟨x, rfl⟩ := coe_surj T φ
  obtain ⟨y, rfl⟩ := coe_surj T ψ
  unfold tensLvl sUQ sVQ
  rw [capQ_coe, tensQ_coe, tensQ_coe, ← RingCon.coe_mul, ← RingCon.coe_mul, ← RingCon.coe_mul,
    ← RingCon.coe_mul, capQ_coe, recastQ_coe,
    slide_conj_succ (left_ne_zero_of_mul_eq_one hε) ha ha' (P δ b m) (P δ b' m) x y,
    pl_zero_recast (by omega)]

end Level

end QOU.HeckeTemperleyLieb.TLGluedTensor
