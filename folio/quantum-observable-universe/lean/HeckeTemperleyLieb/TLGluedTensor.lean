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

/-! ## The level tensor bifunctor -/

section LevelFunctor

variable {K : Type*} [Field K] {δ ε : K} {T : MarkovTower δ ε} {hε : δ * ε = 1}

/-- The tensor of two level objects. -/
def lobjT {n m : ℕ} (A : LObj T hε n) (A' : LObj T hε m) : LObj T hε (n + m + 1) :=
  ⟨A.a + A'.a + 1, by have := A.le; have := A'.le; omega,
    by have := A.par; have := A'.par; omega⟩

/-- **The level tensor of morphisms.** -/
noncomputable def ltens {n m : ℕ} {A B : LObj T hε n} {A' B' : LObj T hε m} (f : A ⟶ B)
    (g : A' ⟶ B') : lobjT A A' ⟶ lobjT B B' :=
  lmk (tensLvl T A.a A'.a B.a B'.a (lval f) (lval g))
    (tensLvl_mem T hε A.le A.par.symm A'.le A'.par.symm B.le B.par.symm B'.le B'.par.symm
      (lval_mem f) (lval_mem g))

theorem lval_ltens {n m : ℕ} {A B : LObj T hε n} {A' B' : LObj T hε m} (f : A ⟶ B)
    (g : A' ⟶ B') : lval (ltens f g) = tensLvl T A.a A'.a B.a B'.a (lval f) (lval g) := rfl

theorem lval_comp {N : ℕ} {X Y Z : LObj T hε N} (f : X ⟶ Y) (g : Y ⟶ Z) :
    lval (f ≫ g) = lval g * lval f := rfl

theorem lval_id {N : ℕ} (X : LObj T hε N) : lval (𝟙 X) = PQ T X.a N := rfl

theorem ltens_comp {n m : ℕ} {A B C : LObj T hε n} {A' B' C' : LObj T hε m} (f : A ⟶ B)
    (h : B ⟶ C) (g : A' ⟶ B') (k : B' ⟶ C') :
    ltens (f ≫ h) (g ≫ k) = ltens f g ≫ ltens h k := by
  apply lhom_ext
  rw [lval_comp, lval_ltens, lval_ltens, lval_ltens, lval_comp, lval_comp,
    tensLvl_mul T hε B.le B.par.symm (lval_mem h) (lval_mem k)]

theorem ltens_id {n m : ℕ} (A : LObj T hε n) (A' : LObj T hε m) :
    ltens (𝟙 A) (𝟙 A') = 𝟙 (lobjT A A') := by
  apply lhom_ext
  rw [lval_ltens, lval_id, lval_id, lval_id, tensLvl_id T hε A.le A.par.symm A'.le A'.par.symm]
  rfl

theorem leg_recast {L L' : ℕ} (h : L = L') {c d : ℕ} {hc : c ≤ L} {pc : c % 2 = L % 2}
    {hd : d ≤ L} {pd : d % 2 = L % 2} {hc' : c ≤ L'} {pc' : c % 2 = L' % 2} {hd' : d ≤ L'}
    {pd' : d % 2 = L' % 2} (z : (⟨c, hc, pc⟩ : LObj T hε L) ⟶ ⟨d, hd, pd⟩)
    (hz : recastQ T h (lval z) ∈ HomSp T L' c d) :
    (leg T hε L').map (X := ⟨c, hc', pc'⟩) (Y := ⟨d, hd', pd'⟩) (lmk (recastQ T h (lval z)) hz) =
      (leg T hε L).map z := by
  subst h
  rfl

theorem leg_stabL (N : ℕ) {X Y : LObj T hε N} (f : X ⟶ Y) :
    (leg T hε (N + 1 + 1)).map ((stabL T hε N).map f) = (leg T hε N).map f := by
  have := Functor.congr_hom (stabL_comp_leg (T := T) (hε := hε) N) f
  simpa using this

/-- **Two more strands on the first factor**, seen in the glued category. -/
theorem leg_ltens_stabL_left {n m : ℕ} {A B : LObj T hε n} {A' B' : LObj T hε m} (f : A ⟶ B)
    (g : A' ⟶ B') :
    (leg T hε (n + 1 + 1 + m + 1)).map (ltens ((stabL T hε n).map f) g) =
      (leg T hε (n + m + 1)).map (ltens f g) := by
  rw [← leg_stabL (n + m + 1) (ltens f g)]
  have h : lval (ltens ((stabL T hε n).map f) g) =
      recastQ T (by omega) (lval ((stabL T hε (n + m + 1)).map (ltens f g))) :=
    tensLvl_capQ_left T hε A.le B.le (lval f) (lval g)
  have : ltens ((stabL T hε n).map f) g = lmk _ (h ▸ lval_mem _) := lhom_ext h
  rw [this]
  exact leg_recast _ _ _

/-- **Two more strands on the second factor**, seen in the glued category. -/
theorem leg_ltens_stabL_right {n m : ℕ} {A B : LObj T hε n} {A' B' : LObj T hε m} (f : A ⟶ B)
    (g : A' ⟶ B') :
    (leg T hε (n + (m + 1 + 1) + 1)).map (ltens f ((stabL T hε m).map g)) =
      (leg T hε (n + m + 1)).map (ltens f g) := by
  rw [← leg_stabL (n + m + 1) (ltens f g)]
  have h : lval (ltens f ((stabL T hε m).map g)) =
      lval ((stabL T hε (n + m + 1)).map (ltens f g)) :=
    tensLvl_capQ_right T hε A'.le B'.le (lval f) (lval g)
  exact congrArg _ (lhom_ext h)

end LevelFunctor

end QOU.HeckeTemperleyLieb.TLGluedTensor
