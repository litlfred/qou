import HeckeTemperleyLieb.TLGluedTensor

/-!
# Associativity of the tensor in the glued Temperley–Lieb category

Bean `hkmt`. The tensor `tensHom` of `TLGluedTensor` is strictly associative, up to reindexing
the strand count of the object. By the interchange law it suffices to tensor one morphism with
two identities. In the first two slots every glued morphism is a composite of single cups,
single caps and endomorphisms of a top object, so it suffices to check these, which is a short
computation with the slide words one level up.

Everything holds over any field, with `δ ε = 1`; only the Temperley–Lieb relations are used.

-- Ref: [kauffman1987] State models and the Jones polynomial, §3.
-- Ref: [leitner2026] the Temperley–Lieb chapter (bean `hkmt`).
-/

namespace QOU.HeckeTemperleyLieb.TLGluedAssoc

open CategoryTheory
open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebMarkov
open QOU.HeckeTemperleyLieb.TLCupCap QOU.HeckeTemperleyLieb.TLNegligible
open QOU.HeckeTemperleyLieb.TLCableBraiding QOU.HeckeTemperleyLieb.TLQuotientTensor
open QOU.HeckeTemperleyLieb.TLRectHom QOU.HeckeTemperleyLieb.TLQuotientModular
open QOU.HeckeTemperleyLieb.TLGlued QOU.HeckeTemperleyLieb.TLSlideIso
open QOU.HeckeTemperleyLieb.TLZigzag QOU.HeckeTemperleyLieb.TLGluedTensor

/-! ## Slide words one level up -/

section Words

variable {K : Type*} [Field K] {δ : K}

theorem slideU_base (a m : ℕ) (y : TLFin K δ m) : slideU δ a m y a = tens δ (1 : TLFin K δ a) y := by
  rw [slideU_self, pl_zero_self]

theorem slideV_base (a m : ℕ) (y : TLFin K δ m) : slideV δ a m y a = tens δ (1 : TLFin K δ a) y := by
  rw [slideV_self, pl_zero_self]

theorem P_two (a : ℕ) : P δ a (a + 1 + 1) = δ⁻¹ • gen δ (a + 1 + 1) (a + 1) := by
  rw [P_succ_succ δ (by omega), P_self, capEmb, map_one, map_one, one_mul, gen_of_lt (by omega)]
  rfl

theorem pl_zero_one_cap {N L : ℕ} (h : 0 + (L + 1 + 1) ≤ N) :
    pl δ 0 (L + 1 + 1) h (capEmb δ L 1) = δ⁻¹ • gen δ N (L + 1) := by
  rw [pl_capEmb, map_one, one_mul, Nat.zero_add]

theorem slideU_one (hδ : δ ≠ 0) (a b : ℕ) :
    slideU δ a b (1 : TLFin K δ b) (a + 2) = δ⁻¹ • zig δ (a + 2 + b + 1) (a + 1) (b + 2) := by
  rw [slideU_step _ le_rfl, slideU_base, tens_one, pl_zero_one_cap, mul_smul_comm, smul_smul,
    show a + b + 1 + 1 = (a + 1) + (b + 1) by omega, show b + 2 = (b + 1) + 1 from rfl,
    zig_mul_gen (by omega), smul_smul]
  congr 1
  field_simp

theorem slideV_one (hδ : δ ≠ 0) (a b : ℕ) :
    slideV δ a b (1 : TLFin K δ b) (a + 2) = δ⁻¹ • zag δ (a + 2 + b + 1) (a + 1) (b + 2) := by
  rw [slideV_step _ le_rfl, slideV_base, tens_one, pl_zero_one_cap, smul_mul_assoc, smul_smul,
    show a + b + 1 + 1 = (a + 1) + (b + 1) by omega, show b + 2 = (b + 1) + 1 from rfl,
    gen_mul_zag (by omega), smul_smul]
  congr 1
  field_simp

theorem tens_P_two_one (a m : ℕ) :
    tens δ (P δ a (a + 1 + 1)) (1 : TLFin K δ m) = δ⁻¹ • gen δ (a + 1 + 1 + m + 1) (a + 1) := by
  rw [TLQuotientBraiding.tens_eq_pl, map_one, mul_one, P_two, map_smul, pl_gen _ (by omega),
    Nat.zero_add]

theorem tens_one_P_two (a b : ℕ) :
    tens δ (1 : TLFin K δ a) (P δ b (b + 1 + 1)) =
      δ⁻¹ • gen δ (a + (b + 1 + 1) + 1) (a + 1 + (b + 1)) := by
  rw [TLQuotientBraiding.tens_eq_pl, map_one, one_mul, P_two, map_smul, pl_gen _ (by omega)]

theorem slideU_one' (hδ : δ ≠ 0) {a b n : ℕ} (hn : n = a + 2) :
    slideU δ a b (1 : TLFin K δ b) n = δ⁻¹ • zig δ (n + b + 1) (a + 1) (b + 2) := by
  subst hn; exact slideU_one hδ a b

theorem slideV_one' (hδ : δ ≠ 0) {a b n : ℕ} (hn : n = a + 2) :
    slideV δ a b (1 : TLFin K δ b) n = δ⁻¹ • zag δ (n + b + 1) (a + 1) (b + 2) := by
  subst hn; exact slideV_one hδ a b

theorem recast_zig {N N' : ℕ} (h : N = N') (p k : ℕ) : recast δ h (zig δ N p k) = zig δ N' p k := by
  subst h; rfl

theorem recast_zag {N N' : ℕ} (h : N = N') (p k : ℕ) : recast δ h (zag δ N p k) = zag δ N' p k := by
  subst h; rfl

theorem tens_one_right {n m : ℕ} (x : TLFin K δ n) :
    tens δ x (1 : TLFin K δ m) = pl δ 0 n (by omega) x := by
  rw [TLQuotientBraiding.tens_eq_pl, map_one, mul_one]

theorem tens_one_left {n m : ℕ} (y : TLFin K δ m) :
    tens δ (1 : TLFin K δ n) y = pl δ (n + 1) m (by omega) y := by
  rw [TLQuotientBraiding.tens_eq_pl, map_one, one_mul]

/-- A cup followed by its slide past `m + 1` strands. -/
theorem cup_mul_zig (a m : ℕ) :
    tens δ (P δ a (a + 1 + 1)) (1 : TLFin K δ m) * (δ⁻¹ • zig δ (a + 1 + 1 + m + 1) (a + 1) (m + 2)) =
      δ⁻¹ • zig δ (a + 1 + 1 + m + 1) (a + 1) (m + 2) := by
  rw [tens_P_two_one, smul_mul_smul_comm, gen_mul_zig (by omega), smul_smul]
  congr 1
  field_simp

theorem zig_congr {n p p' k k' : ℕ} (hp : p = p') (hk : k = k') : zig δ n p k = zig δ n p' k' := by
  subst hp hk; rfl

theorem zag_congr {n p p' k k' : ℕ} (hp : p = p') (hk : k = k') : zag δ n p k = zag δ n p' k' := by
  subst hp hk; rfl

/-- A cap after its slide past `m + 1` strands. -/
theorem zag_mul_cap (a m : ℕ) :
    (δ⁻¹ • zag δ (a + 1 + 1 + m + 1) (a + 1) (m + 2)) * tens δ (P δ a (a + 1 + 1)) (1 : TLFin K δ m) =
      δ⁻¹ • zag δ (a + 1 + 1 + m + 1) (a + 1) (m + 2) := by
  rw [tens_P_two_one, smul_mul_smul_comm, zag_mul_gen (by omega), smul_smul]
  congr 1
  field_simp

/-- **Two cup slides in a row are one slide**, past both blocks. -/
theorem zig_zig_slide {N : ℕ} (p b c : ℕ) (hN : p + b + c + 3 < N + 1) :
    (δ⁻¹ • zig δ N p (b + 2)) * (δ⁻¹ • zig δ N (p + b + 1) (c + 2)) =
      δ⁻¹ • zig δ N p (b + c + 1 + 2) := by
  rw [show zig δ N (p + b + 1) (c + 2) = gen δ N (p + (b + 1)) * zig δ N (p + (b + 2)) (c + 1) by
      rw [show c + 2 = 1 + (c + 1) by omega, zig_add, zig_one]
      exact congrArg₂ _ (congrArg _ (by omega)) (zig_congr (by omega) rfl),
    smul_mul_smul_comm, ← mul_assoc, show b + 2 = (b + 1) + 1 from rfl,
    zig_mul_gen (by omega), smul_mul_assoc, smul_smul, ← zig_add,
    show b + 1 + 1 + (c + 1) = b + c + 1 + 2 by omega]
  congr 1
  field_simp

/-- **Two cap slides in a row are one slide.** -/
theorem zag_zag_slide {N : ℕ} (p b c : ℕ) (hN : p + b + c + 3 < N + 1) :
    (δ⁻¹ • zag δ N (p + b + 1) (c + 2)) * (δ⁻¹ • zag δ N p (b + 2)) =
      δ⁻¹ • zag δ N p (b + c + 1 + 2) := by
  rw [show zag δ N (p + b + 1) (c + 2) = zag δ N (p + (b + 2)) (c + 1) * gen δ N (p + (b + 1)) by
      rw [show c + 2 = 1 + (c + 1) by omega, zag_add, zag_one]
      exact congrArg₂ _ (zag_congr (by omega) rfl) (congrArg _ (by omega)),
    smul_mul_smul_comm, mul_assoc, show b + 2 = (b + 1) + 1 from rfl,
    gen_mul_zag (by omega), mul_smul_comm, smul_smul, ← zag_add,
    show b + 1 + 1 + (c + 1) = b + c + 1 + 2 by omega]
  congr 1
  field_simp

end Words

/-! ## The level tensor on the generators -/

section LevelGen

variable {K : Type*} [Field K] {δ ε : K} (T : MarkovTower δ ε) (hε : δ * ε = 1)

theorem PQ_self (a : ℕ) : PQ T a a = 1 := by
  rw [PQ, P_self, RingCon.coe_one]

/-- **At the base level of the first factor no slide is needed.** -/
theorem tensLvl_base {a b b' m : ℕ} (φ : Q T a) {ψ : Q T m} (hψ : ψ ∈ HomSp T m b b') :
    tensLvl T a b a b' φ ψ = tensQ T φ ψ := by
  unfold tensLvl sUQ sVQ
  rw [slideU_base, slideV_base, ← tensQ_coe, ← tensQ_coe, RingCon.coe_one, tensQ_mul, tensQ_mul,
    one_mul, mul_one, ← PQ, ← PQ, (mem_Hom T).mp hψ]

include hε in
/-- The level tensor of a morphism one level above its source with an identity. -/
theorem tensLvl_cup {A c n : ℕ} (hn : n = A + 2) (x : TLFin K δ n) :
    tensLvl T A c n c (x : Q T n) (1 : Q T c) =
      ((tens δ x (1 : TLFin K δ c) * (δ⁻¹ • zig δ (n + c + 1) (A + 1) (c + 2)) : TLFin K δ _) :
        Q T (n + c + 1)) := by
  unfold tensLvl sUQ sVQ
  rw [P_self, slideV_base, tens_one, slideU_one' (left_ne_zero_of_mul_eq_one hε) hn,
    ← RingCon.coe_one, tensQ_coe, ← RingCon.coe_mul, ← RingCon.coe_mul, one_mul]

include hε in
/-- The level tensor of a morphism one level above its target with an identity. -/
theorem tensLvl_cap {A c n : ℕ} (hn : n = A + 2) (x : TLFin K δ n) :
    tensLvl T n c A c (x : Q T n) (1 : Q T c) =
      (((δ⁻¹ • zag δ (n + c + 1) (A + 1) (c + 2)) * tens δ x (1 : TLFin K δ c) : TLFin K δ _) :
        Q T (n + c + 1)) := by
  unfold tensLvl sUQ sVQ
  rw [P_self, slideU_base, tens_one, slideV_one' (left_ne_zero_of_mul_eq_one hε) hn,
    ← RingCon.coe_one, tensQ_coe, ← RingCon.coe_mul, ← RingCon.coe_mul, mul_one]

include hε in
/-- **Associativity on a single cup in the first slot.** -/
theorem assoc_cup_first (a b c : ℕ) :
    recastQ T (by omega) (tensLvl T (a + b + 1) c (a + 1 + 1 + b + 1) c
      (tensLvl T a b (a + 1 + 1) b (PQ T a (a + 1 + 1)) (1 : Q T b)) (1 : Q T c)) =
      tensLvl T a (b + c + 1) (a + 1 + 1) (b + c + 1) (PQ T a (a + 1 + 1)) (1 : Q T (b + c + 1)) := by
  rw [PQ, tensLvl_cup T hε rfl, tensLvl_cup T hε rfl, cup_mul_zig, cup_mul_zig,
    tensLvl_cup T hε (A := a + b + 1) (by omega), tens_one_right, map_smul,
    pl_zig _ (b + 2) (by omega), Nat.zero_add, show a + b + 1 + 1 = a + 1 + b + 1 by omega,
    zig_zig_slide (a + 1) b c (by omega), recastQ_coe, map_smul, recast_zig]

include hε in
/-- **Associativity on a single cap in the first slot.** -/
theorem assoc_cap_first (a b c : ℕ) :
    recastQ T (by omega) (tensLvl T (a + 1 + 1 + b + 1) c (a + b + 1) c
      (tensLvl T (a + 1 + 1) b a b (PQ T a (a + 1 + 1)) (1 : Q T b)) (1 : Q T c)) =
      tensLvl T (a + 1 + 1) (b + c + 1) a (b + c + 1) (PQ T a (a + 1 + 1)) (1 : Q T (b + c + 1)) := by
  rw [PQ, tensLvl_cap T hε rfl, tensLvl_cap T hε rfl, zag_mul_cap, zag_mul_cap,
    tensLvl_cap T hε (A := a + b + 1) (by omega), tens_one_right, map_smul,
    pl_zag _ (b + 2) (by omega), Nat.zero_add, show a + b + 1 + 1 = a + 1 + b + 1 by omega,
    zag_zag_slide (a + 1) b c (by omega), recastQ_coe, map_smul, recast_zag]

theorem tensQ_one_coe {a m : ℕ} (y : TLFin K δ m) :
    tensQ T (1 : Q T a) (y : Q T m) = (tens δ (1 : TLFin K δ a) y : Q T _) := by
  rw [← RingCon.coe_one, tensQ_coe]

include hε in
/-- **Associativity on a single cup in the second slot.** -/
theorem assoc_cup_second (a b c : ℕ) :
    recastQ T (by omega) (tensLvl T (a + b + 1) c (a + (b + 1 + 1) + 1) c
      (tensQ T (1 : Q T a) (PQ T b (b + 1 + 1))) (1 : Q T c)) =
      tensQ T (1 : Q T a) (tensLvl T b c (b + 1 + 1) c (PQ T b (b + 1 + 1)) (1 : Q T c)) := by
  have hx : tens δ (tens δ (1 : TLFin K δ a) (P δ b (b + 1 + 1))) (1 : TLFin K δ c) =
      δ⁻¹ • gen δ (a + (b + 1 + 1) + 1 + c + 1) (a + 1 + (b + 1)) := by
    rw [tens_one_P_two, tens_one_right, map_smul, pl_gen _ (by omega), Nat.zero_add]
  rw [PQ, tensQ_one_coe, tensLvl_cup T hε (A := a + b + 1) (by omega), hx,
    zig_congr (show a + b + 1 + 1 = a + 1 + (b + 1) by omega) (show c + 2 = (c + 1) + 1 from rfl),
    smul_mul_smul_comm, gen_mul_zig (by omega), smul_smul, tensLvl_cup T hε rfl, cup_mul_zig,
    tensQ_one_coe, tens_one_left, map_smul, pl_zig _ (c + 2) (by omega), recastQ_coe, map_smul,
    recast_zig]
  have hδ : δ ≠ 0 := left_ne_zero_of_mul_eq_one hε
  rw [show δ⁻¹ * δ⁻¹ * δ = δ⁻¹ by field_simp]

include hε in
/-- **Associativity on a single cap in the second slot.** -/
theorem assoc_cap_second (a b c : ℕ) :
    recastQ T (by omega) (tensLvl T (a + (b + 1 + 1) + 1) c (a + b + 1) c
      (tensQ T (1 : Q T a) (PQ T b (b + 1 + 1))) (1 : Q T c)) =
      tensQ T (1 : Q T a) (tensLvl T (b + 1 + 1) c b c (PQ T b (b + 1 + 1)) (1 : Q T c)) := by
  have hx : tens δ (tens δ (1 : TLFin K δ a) (P δ b (b + 1 + 1))) (1 : TLFin K δ c) =
      δ⁻¹ • gen δ (a + (b + 1 + 1) + 1 + c + 1) (a + 1 + (b + 1)) := by
    rw [tens_one_P_two, tens_one_right, map_smul, pl_gen _ (by omega), Nat.zero_add]
  rw [PQ, tensQ_one_coe, tensLvl_cap T hε (A := a + b + 1) (by omega), hx,
    zag_congr (show a + b + 1 + 1 = a + 1 + (b + 1) by omega) (show c + 2 = (c + 1) + 1 from rfl),
    smul_mul_smul_comm, zag_mul_gen (by omega), smul_smul, tensLvl_cap T hε rfl, zag_mul_cap,
    tensQ_one_coe, tens_one_left, map_smul, pl_zag _ (c + 2) (by omega), recastQ_coe, map_smul,
    recast_zag]
  have hδ : δ ≠ 0 := left_ne_zero_of_mul_eq_one hε
  rw [show δ⁻¹ * δ⁻¹ * δ = δ⁻¹ by field_simp]

end LevelGen

end QOU.HeckeTemperleyLieb.TLGluedAssoc
