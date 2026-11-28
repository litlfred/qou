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

/-! ## The tensor of morphisms in the glued category -/

section Glued

variable {K : Type*} [Field K] {δ ε : K} {T : MarkovTower δ ε} {hε : δ * ε = 1}

/-- **The tensor of two objects**: `[a] ⊗ [b] = [a + b + 1]` (`a + 1` and `b + 1` strands). -/
def tensObj (X Y : GObj T hε) : GObj T hε := ⟨X.a + Y.a + 1⟩

/-- A glued object seen at a level `n` above it, of its parity. -/
def lo (X : GObj T hε) (n : ℕ) (h : X.a ≤ n) (p : X.a % 2 = n % 2) : LObj T hε n := ⟨X.a, h, p⟩

/-- The level-zero morphism. -/
noncomputable def lzero {N : ℕ} (X Y : LObj T hε N) : X ⟶ Y := lmk 0 (HomSp T N X.a Y.a).zero_mem

theorem leg_lzero {N : ℕ} (X Y : LObj T hε N) : (leg T hε N).map (lzero X Y) = 0 := by
  rw [leg_map, ← Submodule.Quotient.mk_zero, mk_eq_iff]
  refine ⟨N, fun M hM => ?_⟩
  have h := ext_smul_ev T hε (0 : K) (0 : Q T N) M hM
  rw [zero_smul, zero_smul] at h
  exact h

/-- **A glued morphism at level `n`**: its preimage under the leg. -/
noncomputable def pre (n : ℕ) {X Y : GObj T hε} (hX : X.a ≤ n) (pX : X.a % 2 = n % 2)
    (hY : Y.a ≤ n) (pY : Y.a % 2 = n % 2) (f : X ⟶ Y) : lo X n hX pX ⟶ lo Y n hY pY :=
  (leg T hε n).preimage f

theorem leg_pre (n : ℕ) {X Y : GObj T hε} (hX : X.a ≤ n) (pX : X.a % 2 = n % 2)
    (hY : Y.a ≤ n) (pY : Y.a % 2 = n % 2) (f : X ⟶ Y) :
    (leg T hε n).map (pre n hX pX hY pY f) = f :=
  Functor.map_preimage (leg T hε n) (X := lo X n hX pX) (Y := lo Y n hY pY) f

theorem pre_succ (n : ℕ) {X Y : GObj T hε} (hX : X.a ≤ n) (pX : X.a % 2 = n % 2)
    (hY : Y.a ≤ n) (pY : Y.a % 2 = n % 2) (f : X ⟶ Y) :
    pre (n + 1 + 1) (by omega) (by omega) (by omega) (by omega) f =
      (stabL T hε n).map (pre n hX pX hY pY f) := by
  apply (leg T hε (n + 1 + 1)).map_injective
  rw [leg_pre, leg_stabL, leg_pre]

theorem pre_comp (n : ℕ) {X Y Z : GObj T hε} (hX : X.a ≤ n) (pX : X.a % 2 = n % 2)
    (hY : Y.a ≤ n) (pY : Y.a % 2 = n % 2) (hZ : Z.a ≤ n) (pZ : Z.a % 2 = n % 2)
    (f : X ⟶ Y) (g : Y ⟶ Z) :
    pre n hX pX hZ pZ (f ≫ g) = pre n hX pX hY pY f ≫ pre n hY pY hZ pZ g := by
  apply (leg T hε n).map_injective
  rw [Functor.map_comp, leg_pre, leg_pre, leg_pre]

theorem pre_id (n : ℕ) {X : GObj T hε} (hX : X.a ≤ n) (pX : X.a % 2 = n % 2) :
    pre n hX pX hX pX (𝟙 X) = 𝟙 _ := by
  apply (leg T hε n).map_injective
  rw [leg_pre, CategoryTheory.Functor.map_id]
  rfl

theorem pre_zero (n : ℕ) {X Y : GObj T hε} (hX : X.a ≤ n) (pX : X.a % 2 = n % 2)
    (hY : Y.a ≤ n) (pY : Y.a % 2 = n % 2) :
    pre n hX pX hY pY (0 : X ⟶ Y) = lzero _ _ := by
  apply (leg T hε n).map_injective
  rw [leg_pre, leg_lzero]

/-- **The tensor of two glued morphisms, computed at levels `n` and `m`.** -/
noncomputable def tensVia (n m : ℕ) {X Y X' Y' : GObj T hε} (hX : X.a ≤ n)
    (pX : X.a % 2 = n % 2) (hY : Y.a ≤ n) (pY : Y.a % 2 = n % 2) (hX' : X'.a ≤ m)
    (pX' : X'.a % 2 = m % 2) (hY' : Y'.a ≤ m) (pY' : Y'.a % 2 = m % 2) (f : X ⟶ Y)
    (g : X' ⟶ Y') : tensObj X X' ⟶ tensObj Y Y' :=
  (leg T hε (n + m + 1)).map (X := lobjT (lo X n hX pX) (lo X' m hX' pX'))
    (Y := lobjT (lo Y n hY pY) (lo Y' m hY' pY'))
    (ltens (pre n hX pX hY pY f) (pre m hX' pX' hY' pY' g))

theorem tensVia_succ_left (n m : ℕ) {X Y X' Y' : GObj T hε} (hX : X.a ≤ n)
    (pX : X.a % 2 = n % 2) (hY : Y.a ≤ n) (pY : Y.a % 2 = n % 2) (hX' : X'.a ≤ m)
    (pX' : X'.a % 2 = m % 2) (hY' : Y'.a ≤ m) (pY' : Y'.a % 2 = m % 2) (f : X ⟶ Y)
    (g : X' ⟶ Y') :
    tensVia (n + 1 + 1) m (by omega) (by omega) (by omega) (by omega) hX' pX' hY' pY' f g =
      tensVia n m hX pX hY pY hX' pX' hY' pY' f g := by
  unfold tensVia
  rw [pre_succ n hX pX hY pY f]
  exact leg_ltens_stabL_left _ _

theorem tensVia_succ_right (n m : ℕ) {X Y X' Y' : GObj T hε} (hX : X.a ≤ n)
    (pX : X.a % 2 = n % 2) (hY : Y.a ≤ n) (pY : Y.a % 2 = n % 2) (hX' : X'.a ≤ m)
    (pX' : X'.a % 2 = m % 2) (hY' : Y'.a ≤ m) (pY' : Y'.a % 2 = m % 2) (f : X ⟶ Y)
    (g : X' ⟶ Y') :
    tensVia n (m + 1 + 1) hX pX hY pY (by omega) (by omega) (by omega) (by omega) f g =
      tensVia n m hX pX hY pY hX' pX' hY' pY' f g := by
  unfold tensVia
  rw [pre_succ m hX' pX' hY' pY' g]
  exact leg_ltens_stabL_right _ _

theorem tensVia_level_left (k : ℕ) : ∀ (n n' m : ℕ) (_ : n' = n + 2 * k) {X Y X' Y' : GObj T hε}
    (hX : X.a ≤ n) (pX : X.a % 2 = n % 2) (hY : Y.a ≤ n) (pY : Y.a % 2 = n % 2)
    (hX2 : X.a ≤ n') (pX2 : X.a % 2 = n' % 2) (hY2 : Y.a ≤ n') (pY2 : Y.a % 2 = n' % 2)
    (hX' : X'.a ≤ m) (pX' : X'.a % 2 = m % 2) (hY' : Y'.a ≤ m) (pY' : Y'.a % 2 = m % 2)
    (f : X ⟶ Y) (g : X' ⟶ Y'),
    tensVia n' m hX2 pX2 hY2 pY2 hX' pX' hY' pY' f g =
      tensVia n m hX pX hY pY hX' pX' hY' pY' f g := by
  induction k with
  | zero =>
    intro n n' m hk X Y X' Y' _ _ _ _ _ _ _ _ _ _ _ _ f g
    obtain rfl : n' = n := by omega
    rfl
  | succ k ih =>
    intro n n' m hk X Y X' Y' hX pX hY pY _ _ _ _ hX' pX' hY' pY' f g
    obtain rfl : n' = n + 2 * k + 1 + 1 := by omega
    rw [tensVia_succ_left (n + 2 * k) m (by omega) (by omega) (by omega) (by omega)]
    exact ih n (n + 2 * k) m rfl _ _ _ _ _ _ _ _ _ _ _ _ f g

theorem tensVia_level_right (k : ℕ) : ∀ (n m m' : ℕ) (_ : m' = m + 2 * k) {X Y X' Y' : GObj T hε}
    (hX : X.a ≤ n) (pX : X.a % 2 = n % 2) (hY : Y.a ≤ n) (pY : Y.a % 2 = n % 2)
    (hX' : X'.a ≤ m) (pX' : X'.a % 2 = m % 2) (hY' : Y'.a ≤ m) (pY' : Y'.a % 2 = m % 2)
    (hX2 : X'.a ≤ m') (pX2 : X'.a % 2 = m' % 2) (hY2 : Y'.a ≤ m') (pY2 : Y'.a % 2 = m' % 2)
    (f : X ⟶ Y) (g : X' ⟶ Y'),
    tensVia n m' hX pX hY pY hX2 pX2 hY2 pY2 f g =
      tensVia n m hX pX hY pY hX' pX' hY' pY' f g := by
  induction k with
  | zero =>
    intro n m m' hk X Y X' Y' _ _ _ _ _ _ _ _ _ _ _ _ f g
    obtain rfl : m' = m := by omega
    rfl
  | succ k ih =>
    intro n m m' hk X Y X' Y' hX pX hY pY hX' pX' hY' pY' _ _ _ _ f g
    obtain rfl : m' = m + 2 * k + 1 + 1 := by omega
    rw [tensVia_succ_right n (m + 2 * k) hX pX hY pY (by omega) (by omega) (by omega) (by omega)]
    exact ih n m (m + 2 * k) rfl _ _ _ _ _ _ _ _ _ _ _ _ f g

/-- **The tensor of glued morphisms does not depend on the levels.** -/
theorem tensVia_indep (n n' m m' : ℕ) {X Y X' Y' : GObj T hε}
    (hX : X.a ≤ n) (pX : X.a % 2 = n % 2) (hY : Y.a ≤ n) (pY : Y.a % 2 = n % 2)
    (hX' : X'.a ≤ m) (pX' : X'.a % 2 = m % 2) (hY' : Y'.a ≤ m) (pY' : Y'.a % 2 = m % 2)
    (hX2 : X.a ≤ n') (pX2 : X.a % 2 = n' % 2) (hY2 : Y.a ≤ n') (pY2 : Y.a % 2 = n' % 2)
    (hX2' : X'.a ≤ m') (pX2' : X'.a % 2 = m' % 2) (hY2' : Y'.a ≤ m') (pY2' : Y'.a % 2 = m' % 2)
    (f : X ⟶ Y) (g : X' ⟶ Y') :
    tensVia n' m' hX2 pX2 hY2 pY2 hX2' pX2' hY2' pY2' f g =
      tensVia n m hX pX hY pY hX' pX' hY' pY' f g := by
  rw [← tensVia_level_left n n' (n' + 2 * n) m' rfl hX2 pX2 hY2 pY2 (by omega) (by omega)
      (by omega) (by omega),
    tensVia_level_left ((n' + n) / 2) n (n' + 2 * n) m' (by omega) hX pX hY pY,
    ← tensVia_level_right m n m' (m' + 2 * m) rfl hX pX hY pY hX2' pX2' hY2' pY2' (by omega)
      (by omega) (by omega) (by omega),
    tensVia_level_right ((m' + m) / 2) n m (m' + 2 * m) (by omega) hX pX hY pY hX' pX' hY' pY']

/-- **The tensor of two glued morphisms**, `0` between labels of different parity. -/
noncomputable def tensHom {X Y X' Y' : GObj T hε} (f : X ⟶ Y) (g : X' ⟶ Y') :
    tensObj X X' ⟶ tensObj Y Y' :=
  if h : X.a % 2 = Y.a % 2 ∧ X'.a % 2 = Y'.a % 2 then
    tensVia (X.a + 2 * Y.a) (X'.a + 2 * Y'.a) (by omega) (by omega) (by omega) (by omega)
      (by omega) (by omega) (by omega) (by omega) f g
  else 0

/-- The tensor is computed at any level of the right parity. -/
theorem tensHom_eq (n m : ℕ) {X Y X' Y' : GObj T hε}
    (hX : X.a ≤ n) (pX : X.a % 2 = n % 2) (hY : Y.a ≤ n) (pY : Y.a % 2 = n % 2)
    (hX' : X'.a ≤ m) (pX' : X'.a % 2 = m % 2) (hY' : Y'.a ≤ m) (pY' : Y'.a % 2 = m % 2)
    (f : X ⟶ Y) (g : X' ⟶ Y') :
    tensHom f g = tensVia n m hX pX hY pY hX' pX' hY' pY' f g := by
  rw [tensHom, dif_pos ⟨by omega, by omega⟩]
  exact tensVia_indep _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ f g

theorem ltens_lzero_left {n m : ℕ} (A B : LObj T hε n) {A' B' : LObj T hε m} (g : A' ⟶ B') :
    ltens (lzero A B) g = lzero _ _ := by
  apply lhom_ext
  rw [lval_ltens]
  show tensLvl T _ _ _ _ 0 (lval g) = 0
  have h := tensQ_smul_left T (0 : K) (0 : Q T n) (lval g)
  rw [zero_smul, zero_smul] at h
  rw [tensLvl, h, mul_zero, zero_mul]

theorem ltens_lzero_right {n m : ℕ} {A B : LObj T hε n} (f : A ⟶ B) (A' B' : LObj T hε m) :
    ltens f (lzero A' B') = lzero _ _ := by
  apply lhom_ext
  rw [lval_ltens]
  show tensLvl T _ _ _ _ (lval f) 0 = 0
  have h := tensQ_smul_right T (0 : K) (lval f) (0 : Q T m)
  rw [zero_smul, zero_smul] at h
  rw [tensLvl, h, mul_zero, zero_mul]

theorem tensHom_zero_left {X Y X' Y' : GObj T hε} (g : X' ⟶ Y') :
    tensHom (0 : X ⟶ Y) g = 0 := by
  by_cases h : X.a % 2 = Y.a % 2 ∧ X'.a % 2 = Y'.a % 2
  · rw [tensHom, dif_pos h]
    unfold tensVia
    rw [pre_zero, ltens_lzero_left]
    exact leg_lzero _ _
  · rw [tensHom, dif_neg h]

theorem tensHom_zero_right {X Y X' Y' : GObj T hε} (f : X ⟶ Y) :
    tensHom f (0 : X' ⟶ Y') = 0 := by
  by_cases h : X.a % 2 = Y.a % 2 ∧ X'.a % 2 = Y'.a % 2
  · rw [tensHom, dif_pos h]
    unfold tensVia
    rw [pre_zero, ltens_lzero_right]
    exact leg_lzero _ _
  · rw [tensHom, dif_neg h]

/-- **The tensor of glued morphisms preserves identities.** -/
theorem tensHom_id (X X' : GObj T hε) : tensHom (𝟙 X) (𝟙 X') = 𝟙 (tensObj X X') := by
  rw [tensHom_eq X.a X'.a le_rfl rfl le_rfl rfl le_rfl rfl le_rfl rfl]
  unfold tensVia
  rw [pre_id, pre_id, ltens_id, CategoryTheory.Functor.map_id]
  rfl

/-- **The tensor of glued morphisms is functorial.** -/
theorem tensHom_comp {X Y Z X' Y' Z' : GObj T hε} (f : X ⟶ Y) (h : Y ⟶ Z) (g : X' ⟶ Y')
    (k : Y' ⟶ Z') : tensHom (f ≫ h) (g ≫ k) = tensHom f g ≫ tensHom h k := by
  by_cases h1 : X.a % 2 = Y.a % 2
  swap
  · rw [hom_eq_zero_of_parity h1 f, Limits.zero_comp, tensHom_zero_left, tensHom_zero_left,
      Limits.zero_comp]
  by_cases h2 : Y.a % 2 = Z.a % 2
  swap
  · rw [hom_eq_zero_of_parity h2 h, Limits.comp_zero, tensHom_zero_left, tensHom_zero_left,
      Limits.comp_zero]
  by_cases h3 : X'.a % 2 = Y'.a % 2
  swap
  · rw [hom_eq_zero_of_parity h3 g, Limits.zero_comp, tensHom_zero_right, tensHom_zero_right,
      Limits.zero_comp]
  by_cases h4 : Y'.a % 2 = Z'.a % 2
  swap
  · rw [hom_eq_zero_of_parity h4 k, Limits.comp_zero, tensHom_zero_right, tensHom_zero_right,
      Limits.comp_zero]
  have e := fun {A B : GObj T hε} {A' B' : GObj T hε} (u : A ⟶ B) (v : A' ⟶ B')
      (hA : A.a ≤ X.a + Y.a + Z.a) (pA : A.a % 2 = (X.a + Y.a + Z.a) % 2)
      (hB : B.a ≤ X.a + Y.a + Z.a) (pB : B.a % 2 = (X.a + Y.a + Z.a) % 2)
      (hA' : A'.a ≤ X'.a + Y'.a + Z'.a) (pA' : A'.a % 2 = (X'.a + Y'.a + Z'.a) % 2)
      (hB' : B'.a ≤ X'.a + Y'.a + Z'.a) (pB' : B'.a % 2 = (X'.a + Y'.a + Z'.a) % 2) =>
    tensHom_eq (X.a + Y.a + Z.a) (X'.a + Y'.a + Z'.a) hA pA hB pB hA' pA' hB' pB' u v
  rw [e (f ≫ h) (g ≫ k) (by omega) (by omega) (by omega) (by omega) (by omega) (by omega)
      (by omega) (by omega),
    e f g (by omega) (by omega) (by omega) (by omega) (by omega) (by omega) (by omega) (by omega),
    e h k (by omega) (by omega) (by omega) (by omega) (by omega) (by omega) (by omega) (by omega)]
  unfold tensVia
  rw [pre_comp _ _ _ (by omega) (by omega), pre_comp _ _ _ (by omega) (by omega), ltens_comp,
    CategoryTheory.Functor.map_comp]

end Glued

end QOU.HeckeTemperleyLieb.TLGluedTensor
