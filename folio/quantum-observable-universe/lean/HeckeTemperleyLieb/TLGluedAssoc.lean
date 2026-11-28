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

theorem one_mem_HomSp (c : ℕ) : (1 : Q T c) ∈ HomSp T c c c := by
  rw [mem_Hom, PQ_self, one_mul, one_mul]

/-- **Associativity on a base-level morphism in the first slot.** -/
theorem assoc_base_first {a : ℕ} (φ : Q T a) (b c : ℕ) :
    recastQ T (by omega) (tensLvl T (a + b + 1) c (a + b + 1) c
      (tensLvl T a b a b φ (1 : Q T b)) (1 : Q T c)) =
      tensLvl T a (b + c + 1) a (b + c + 1) φ (1 : Q T (b + c + 1)) := by
  rw [tensLvl_base T φ (one_mem_HomSp T b), tensLvl_base T _ (one_mem_HomSp T c),
    tensLvl_base T φ (one_mem_HomSp T _), tensQ_assoc, tensQ_one]

/-- **Associativity on a base-level morphism in the second slot.** -/
theorem assoc_base_second (a : ℕ) {b : ℕ} (ψ : Q T b) (c : ℕ) :
    recastQ T (by omega) (tensLvl T (a + b + 1) c (a + b + 1) c
      (tensQ T (1 : Q T a) ψ) (1 : Q T c)) =
      tensQ T (1 : Q T a) (tensLvl T b c b c ψ (1 : Q T c)) := by
  rw [tensLvl_base T _ (one_mem_HomSp T c), tensLvl_base T ψ (one_mem_HomSp T c), tensQ_assoc]

/-- **Associativity in the third slot**, for every morphism there: the first two factors are
identities at base level, so no slide word appears. -/
theorem assoc_third (a b : ℕ) {m c c' : ℕ} {χ : Q T m} (hχ : χ ∈ HomSp T m c c') :
    recastQ T (by omega) (tensLvl T (a + b + 1) c (a + b + 1) c'
      (tensQ T (1 : Q T a) (1 : Q T b)) χ) =
      tensQ T (1 : Q T a) (tensLvl T b c b c' (1 : Q T b) χ) := by
  rw [tensLvl_base T _ hχ, tensLvl_base T _ hχ, tensQ_assoc]

end LevelGen



/-! ## The glued associativity square -/

section Glued

variable {K : Type*} [Field K] {δ ε : K} {T : MarkovTower δ ε} {hε : δ * ε = 1}

variable (T hε) in
/-- **The glued morphism of a level element.** -/
noncomputable def gl (N : ℕ) {a b : ℕ} (ha : a ≤ N) (pa : a % 2 = N % 2) (hb : b ≤ N)
    (pb : b % 2 = N % 2) (φ : Q T N) (hφ : φ ∈ HomSp T N a b) :
    (GObj.mk a : GObj T hε) ⟶ GObj.mk b :=
  (leg T hε N).map (X := ⟨a, ha, pa⟩) (Y := ⟨b, hb, pb⟩) (lmk φ hφ)

theorem pre_gl (N : ℕ) {a b : ℕ} (ha : a ≤ N) (pa : a % 2 = N % 2) (hb : b ≤ N)
    (pb : b % 2 = N % 2) (φ : Q T N) (hφ : φ ∈ HomSp T N a b) :
    pre (X := GObj.mk a) (Y := GObj.mk b) N ha pa hb pb (gl T hε N ha pa hb pb φ hφ) =
      lmk φ hφ := by
  apply (leg T hε N).map_injective
  rw [leg_pre]
  rfl

theorem gl_pre (N : ℕ) {X Y : GObj T hε} (hX : X.a ≤ N) (pX : X.a % 2 = N % 2) (hY : Y.a ≤ N)
    (pY : Y.a % 2 = N % 2) (f : X ⟶ Y) :
    gl T hε N hX pX hY pY (lval (pre N hX pX hY pY f)) (lval_mem _) = f :=
  leg_pre N hX pX hY pY f

/-- **The tensor of two level morphisms is the level tensor.** -/
theorem tensHom_gl (n m : ℕ) {a b a' b' : ℕ} (ha : a ≤ n) (pa : a % 2 = n % 2) (hb : b ≤ n)
    (pb : b % 2 = n % 2) (ha' : a' ≤ m) (pa' : a' % 2 = m % 2) (hb' : b' ≤ m)
    (pb' : b' % 2 = m % 2) (φ : Q T n) (hφ : φ ∈ HomSp T n a b) (ψ : Q T m)
    (hψ : ψ ∈ HomSp T m a' b') :
    tensHom (gl T hε n ha pa hb pb φ hφ) (gl T hε m ha' pa' hb' pb' ψ hψ) =
      gl T hε (n + m + 1) (a := a + a' + 1) (b := b + b' + 1) (by omega) (by omega) (by omega)
        (by omega) (tensLvl T a a' b b' φ ψ)
        (tensLvl_mem T hε ha pa.symm ha' pa'.symm hb pb.symm hb' pb'.symm hφ hψ) := by
  rw [tensHom_eq n m ha pa hb pb ha' pa' hb' pb']
  unfold tensVia
  rw [pre_gl, pre_gl]
  rfl

theorem gl_comp (N : ℕ) {a b c : ℕ} (ha : a ≤ N) (pa : a % 2 = N % 2) (hb : b ≤ N)
    (pb : b % 2 = N % 2) (hc : c ≤ N) (pc : c % 2 = N % 2) (φ : Q T N)
    (hφ : φ ∈ HomSp T N a b) (ψ : Q T N) (hψ : ψ ∈ HomSp T N b c) :
    gl T hε N ha pa hb pb φ hφ ≫ gl T hε N hb pb hc pc ψ hψ =
      gl T hε N ha pa hc pc (ψ * φ) (comp_mem T hε hφ hψ) := by
  unfold gl
  rw [← Functor.map_comp]
  rfl

/-- **Raising a level morphism two strands.** -/
theorem gl_lift (N : ℕ) {a b : ℕ} (ha : a ≤ N) (pa : a % 2 = N % 2) (hb : b ≤ N)
    (pb : b % 2 = N % 2) (φ : Q T N) (hφ : φ ∈ HomSp T N a b) :
    gl T hε N ha pa hb pb φ hφ =
      gl T hε (N + 1 + 1) (by omega) (by omega) (by omega) (by omega) (capQ T hε N φ)
        (capQ_mem T hε ha hb hφ) := by
  unfold gl
  rw [← leg_stabL]
  rfl

theorem gl_id (a : ℕ) :
    gl T hε a le_rfl rfl le_rfl rfl (1 : Q T a) (mem_top a 1) = 𝟙 (GObj.mk a) := by
  unfold gl
  rw [show lmk (X := (⟨a, le_rfl, rfl⟩ : LObj T hε a)) (Y := ⟨a, le_rfl, rfl⟩) (1 : Q T a)
      (mem_top a 1) = 𝟙 _ from lhom_ext (by rw [lval_id, PQ_self]; rfl),
    CategoryTheory.Functor.map_id]
  rfl

/-- **Transport of a level morphism along equal strand counts.** -/
theorem gl_eqToHom {N N' A A' B B' : ℕ} (hN : N = N') (hA : A = A') (hB : B = B')
    (h1 : A ≤ N) (p1 : A % 2 = N % 2) (h2 : B ≤ N) (p2 : B % 2 = N % 2)
    (h1' : A' ≤ N') (p1' : A' % 2 = N' % 2) (h2' : B' ≤ N') (p2' : B' % 2 = N' % 2)
    (φ : Q T N) (hφ : φ ∈ HomSp T N A B) (ψ : Q T N') (hψ : ψ ∈ HomSp T N' A' B')
    (h : recastQ T hN φ = ψ) :
    gl T hε N h1 p1 h2 p2 φ hφ ≫ eqToHom (congrArg GObj.mk hB) =
      eqToHom (congrArg GObj.mk hA) ≫ gl T hε N' h1' p1' h2' p2' ψ hψ := by
  subst hN hA hB h
  simp only [eqToHom_refl, Category.comp_id, Category.id_comp]
  rfl

theorem tensObj_assoc (X Y Z : GObj T hε) :
    tensObj (tensObj X Y) Z = tensObj X (tensObj Y Z) := by
  show GObj.mk (X.a + Y.a + 1 + Z.a + 1) = GObj.mk (X.a + (Y.a + Z.a + 1) + 1)
  congr 1
  omega

/-- **The associativity square** for three glued morphisms. -/
def AssocNat {X Y Z X' Y' Z' : GObj T hε} (f : X ⟶ X') (g : Y ⟶ Y') (h : Z ⟶ Z') : Prop :=
  tensHom (tensHom f g) h ≫ eqToHom (tensObj_assoc X' Y' Z') =
    eqToHom (tensObj_assoc X Y Z) ≫ tensHom f (tensHom g h)

theorem AssocNat.comp {X Y Z X' Y' Z' X'' Y'' Z'' : GObj T hε} {f : X ⟶ X'} {g : Y ⟶ Y'}
    {h : Z ⟶ Z'} {f' : X' ⟶ X''} {g' : Y' ⟶ Y''} {h' : Z' ⟶ Z''} (H : AssocNat f g h)
    (H' : AssocNat f' g' h') : AssocNat (f ≫ f') (g ≫ g') (h ≫ h') := by
  unfold AssocNat at *
  rw [tensHom_comp, tensHom_comp, Category.assoc, H', ← Category.assoc, H, Category.assoc,
    tensHom_comp, tensHom_comp]

theorem gl_congr (N : ℕ) {a b : ℕ} (ha : a ≤ N) (pa : a % 2 = N % 2) (hb : b ≤ N)
    (pb : b % 2 = N % 2) {φ ψ : Q T N} (hφ : φ ∈ HomSp T N a b) (hψ : ψ ∈ HomSp T N a b)
    (h : φ = ψ) : gl T hε N ha pa hb pb φ hφ = gl T hε N ha pa hb pb ψ hψ := by
  subst h
  rfl

/-- **The square for three level morphisms is the level identity.** -/
theorem assocNat_gl (n m p : ℕ) {a a' b b' c c' : ℕ} (ha : a ≤ n) (pa : a % 2 = n % 2)
    (ha' : a' ≤ n) (pa' : a' % 2 = n % 2) (hb : b ≤ m) (pb : b % 2 = m % 2) (hb' : b' ≤ m)
    (pb' : b' % 2 = m % 2) (hc : c ≤ p) (pc : c % 2 = p % 2) (hc' : c' ≤ p)
    (pc' : c' % 2 = p % 2) (φ : Q T n) (hφ : φ ∈ HomSp T n a a') (ψ : Q T m)
    (hψ : ψ ∈ HomSp T m b b') (χ : Q T p) (hχ : χ ∈ HomSp T p c c')
    (H : recastQ T (by omega) (tensLvl T (a + b + 1) c (a' + b' + 1) c' (tensLvl T a b a' b' φ ψ) χ)
      = tensLvl T a (b + c + 1) a' (b' + c' + 1) φ (tensLvl T b c b' c' ψ χ)) :
    AssocNat (gl T hε n ha pa ha' pa' φ hφ) (gl T hε m hb pb hb' pb' ψ hψ)
      (gl T hε p hc pc hc' pc' χ hχ) := by
  unfold AssocNat
  rw [tensHom_gl, tensHom_gl, tensHom_gl, tensHom_gl]
  exact gl_eqToHom (by omega) (by simp only [tensObj]; omega) (by simp only [tensObj]; omega)
    _ _ _ _ _ _ _ _ _ _ _ _ H

/-- **The third slot**: identities in the first two slots. -/
theorem assocNat_third (X Y : GObj T hε) {Z Z' : GObj T hε} (h : Z ⟶ Z') :
    AssocNat (𝟙 X) (𝟙 Y) h := by
  by_cases hp : Z.a % 2 = Z'.a % 2
  swap
  · unfold AssocNat
    rw [hom_eq_zero_of_parity hp h, tensHom_zero_right, tensHom_zero_right, tensHom_zero_right,
      Limits.zero_comp, Limits.comp_zero]
  obtain ⟨a⟩ := X
  obtain ⟨b⟩ := Y
  rw [← gl_id a, ← gl_id b, ← gl_pre (Z.a + 2 * Z'.a) (by omega) (by omega) (by omega)
    (by omega) h]
  refine assocNat_gl _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ?_
  have hχ : lval (pre (Z.a + 2 * Z'.a) (by omega) (by omega) (by omega) (by omega) h) ∈
      HomSp T (Z.a + 2 * Z'.a) Z.a Z'.a := lval_mem _
  rw [tensLvl_base T _ (one_mem_HomSp T b), tensLvl_base T _
    (tensLvl_mem T hε le_rfl rfl (by omega) (by omega) le_rfl rfl (by omega) (by omega)
      (mem_top b 1) hχ)]
  exact assoc_third T a b hχ

/-! ### Cups, caps and projectors at one level -/

include hε in
theorem PQ_mem_up (a N : ℕ) : PQ T a N ∈ HomSp T N a N := by
  rw [mem_Hom, PQ_self, one_mul, PQ_idem T hε]

include hε in
theorem PQ_mem_down (a N : ℕ) : PQ T a N ∈ HomSp T N N a := by
  rw [mem_Hom, PQ_self, mul_one, PQ_idem T hε]

include hε in
theorem PQ_cup_mul (a M : ℕ) (ha : a ≤ M) :
    PQ T M (M + 1 + 1) * PQ T a (M + 1 + 1) = PQ T a (M + 1 + 1) := by
  rw [← capQ_PQ T hε (a := M) (n := M) (by omega), ← capQ_PQ T hε (a := a) (n := M) (by omega),
    ← capQ_mul, PQ_self, one_mul]

include hε in
theorem PQ_mul_cap (a M : ℕ) (ha : a ≤ M) :
    PQ T a (M + 1 + 1) * PQ T M (M + 1 + 1) = PQ T a (M + 1 + 1) := by
  rw [← capQ_PQ T hε (a := M) (n := M) (by omega), ← capQ_PQ T hε (a := a) (n := M) (by omega),
    ← capQ_mul, PQ_self, mul_one]

/-! ### The first slot -/

/-- A morphism whose associativity square with two identities commutes. -/
def Good1 {X X' : GObj T hε} (f : X ⟶ X') : Prop := ∀ Y Z : GObj T hε, AssocNat f (𝟙 Y) (𝟙 Z)

/-- A morphism whose associativity square in the middle slot commutes. -/
def Good2 {Y Y' : GObj T hε} (g : Y ⟶ Y') : Prop := ∀ X Z : GObj T hε, AssocNat (𝟙 X) g (𝟙 Z)

theorem Good1.comp {X X' X'' : GObj T hε} {f : X ⟶ X'} {f' : X' ⟶ X''} (H : Good1 f)
    (H' : Good1 f') : Good1 (f ≫ f') := by
  intro Y Z
  have := (H Y Z).comp (H' Y Z)
  simp only [Category.comp_id] at this
  exact this

theorem Good2.comp {Y Y' Y'' : GObj T hε} {g : Y ⟶ Y'} {g' : Y' ⟶ Y''} (H : Good2 g)
    (H' : Good2 g') : Good2 (g ≫ g') := by
  intro X Z
  have := (H X Z).comp (H' X Z)
  simp only [Category.comp_id] at this
  exact this

theorem good1_id (X : GObj T hε) : Good1 (𝟙 X) := fun Y Z => assocNat_third X Y (𝟙 Z)

theorem good2_id (Y : GObj T hε) : Good2 (𝟙 Y) := fun X Z => assocNat_third X Y (𝟙 Z)

theorem good1_cup (M : ℕ) :
    Good1 (gl T hε (M + 1 + 1) (a := M) (b := M + 1 + 1) (by omega) (by omega) le_rfl rfl
      (PQ T M (M + 1 + 1)) (PQ_mem_up (hε := hε) M _)) := by
  intro Y Z
  obtain ⟨b⟩ := Y
  obtain ⟨c⟩ := Z
  rw [← gl_id b, ← gl_id c]
  refine assocNat_gl _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ?_
  rw [tensLvl_base T (1 : Q T b) (one_mem_HomSp T c), tensQ_one]
  exact assoc_cup_first T hε M b c

theorem good1_cap (M : ℕ) :
    Good1 (gl T hε (M + 1 + 1) (a := M + 1 + 1) (b := M) le_rfl rfl (by omega) (by omega)
      (PQ T M (M + 1 + 1)) (PQ_mem_down (hε := hε) M _)) := by
  intro Y Z
  obtain ⟨b⟩ := Y
  obtain ⟨c⟩ := Z
  rw [← gl_id b, ← gl_id c]
  refine assocNat_gl _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ?_
  rw [tensLvl_base T (1 : Q T b) (one_mem_HomSp T c), tensQ_one]
  exact assoc_cap_first T hε M b c

theorem good1_base (N : ℕ) (φ : Q T N) :
    Good1 (gl T hε N le_rfl rfl le_rfl rfl φ (mem_top N φ)) := by
  intro Y Z
  obtain ⟨b⟩ := Y
  obtain ⟨c⟩ := Z
  rw [← gl_id b, ← gl_id c]
  refine assocNat_gl _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ?_
  rw [tensLvl_base T (1 : Q T b) (one_mem_HomSp T c), tensQ_one]
  exact assoc_base_first T φ b c

theorem good1_zero {X X' : GObj T hε} : Good1 (0 : X ⟶ X') := by
  intro Y Z
  unfold AssocNat
  rw [tensHom_zero_left, tensHom_zero_left, tensHom_zero_left, Limits.zero_comp, Limits.comp_zero]

theorem good2_zero {Y Y' : GObj T hε} : Good2 (0 : Y ⟶ Y') := by
  intro X Z
  unfold AssocNat
  rw [tensHom_zero_right, tensHom_zero_left, tensHom_zero_left, tensHom_zero_right,
    Limits.zero_comp, Limits.comp_zero]

/-! ### The middle slot and generator induction -/

theorem good2_cup (M : ℕ) :
    Good2 (gl T hε (M + 1 + 1) (a := M) (b := M + 1 + 1) (by omega) (by omega) le_rfl rfl
      (PQ T M (M + 1 + 1)) (PQ_mem_up (hε := hε) M _)) := by
  intro X Z
  obtain ⟨a⟩ := X
  obtain ⟨c⟩ := Z
  rw [← gl_id a, ← gl_id c]
  refine assocNat_gl _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ?_
  rw [tensLvl_base T (1 : Q T a) (PQ_mem_up (hε := hε) M _),
    tensLvl_base T (1 : Q T a) (tensLvl_mem T hε (by omega) (by omega) le_rfl rfl
      le_rfl rfl le_rfl rfl (PQ_mem_up (hε := hε) M _) (one_mem_HomSp T c))]
  exact assoc_cup_second T hε a M c

theorem good2_cap (M : ℕ) :
    Good2 (gl T hε (M + 1 + 1) (a := M + 1 + 1) (b := M) le_rfl rfl (by omega) (by omega)
      (PQ T M (M + 1 + 1)) (PQ_mem_down (hε := hε) M _)) := by
  intro X Z
  obtain ⟨a⟩ := X
  obtain ⟨c⟩ := Z
  rw [← gl_id a, ← gl_id c]
  refine assocNat_gl _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ?_
  rw [tensLvl_base T (1 : Q T a) (PQ_mem_down (hε := hε) M _),
    tensLvl_base T (1 : Q T a) (tensLvl_mem T hε le_rfl rfl le_rfl rfl
      (by omega) (by omega) le_rfl rfl (PQ_mem_down (hε := hε) M _) (one_mem_HomSp T c))]
  exact assoc_cap_second T hε a M c

theorem good2_base (N : ℕ) (ψ : Q T N) :
    Good2 (gl T hε N le_rfl rfl le_rfl rfl ψ (mem_top N ψ)) := by
  intro X Z
  obtain ⟨a⟩ := X
  obtain ⟨c⟩ := Z
  rw [← gl_id a, ← gl_id c]
  refine assocNat_gl _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ?_
  rw [tensLvl_base T (1 : Q T a) (mem_top N ψ),
    tensLvl_base T (1 : Q T a) (tensLvl_mem T hε le_rfl rfl le_rfl rfl
      le_rfl rfl le_rfl rfl (mem_top N ψ) (one_mem_HomSp T c))]
  exact assoc_base_second T a ψ c

/-- **Generator induction on glued morphisms.** Any property of morphisms in `GObj T hε` that holds
on identities, zeros, single cups `[M] → [M+2]`, single caps `[M+2] → [M]` and top-level
endomorphisms `[N] → [N]`, and is closed under composition, holds on every morphism. -/
theorem glued_induction (P : ∀ {X Y : GObj T hε}, (X ⟶ Y) → Prop)
    (hid : ∀ X, P (𝟙 X))
    (hzero : ∀ {X Y}, P (0 : X ⟶ Y))
    (hcomp : ∀ {X Y Z} {f : X ⟶ Y} {g : Y ⟶ Z}, P f → P g → P (f ≫ g))
    (hcup : ∀ M, P (gl T hε (M + 1 + 1) (a := M) (b := M + 1 + 1) (by omega) (by omega)
      le_rfl rfl (PQ T M (M + 1 + 1)) (PQ_mem_up (hε := hε) M _)))
    (hcap : ∀ M, P (gl T hε (M + 1 + 1) (a := M + 1 + 1) (b := M) le_rfl rfl
      (by omega) (by omega) (PQ T M (M + 1 + 1)) (PQ_mem_down (hε := hε) M _)))
    (hbase : ∀ N (φ : Q T N), P (gl T hε N le_rfl rfl le_rfl rfl φ (mem_top N φ))) :
    ∀ {X Y : GObj T hε} (f : X ⟶ Y), P f := by
  have hup : ∀ (a k : ℕ), P (gl T hε (a + 2 * k) (a := a) (b := a + 2 * k)
      (by omega) (by omega) le_rfl rfl (PQ T a (a + 2 * k)) (PQ_mem_up (hε := hε) a _)) := by
    intro a k
    induction k with
    | zero =>
      have e : gl T hε (a + 2 * 0) (a := a) (b := a + 2 * 0) (by omega) (by omega) le_rfl rfl
          (PQ T a (a + 2 * 0)) (PQ_mem_up (hε := hε) a _) = 𝟙 (GObj.mk a) := by
        show gl T hε a (a := a) (b := a) _ _ _ _ (PQ T a a) _ = 𝟙 (GObj.mk a)
        rw [gl_congr a _ _ _ _ _ (mem_top a 1) (PQ_self T a)]
        exact gl_id a
      rw [e]
      exact hid _
    | succ k ih =>
      set M := a + 2 * k
      have h1 : gl T hε M (a := a) (b := M) (by omega) (by omega) le_rfl rfl
          (PQ T a M) (PQ_mem_up (hε := hε) a M) ≫
        gl T hε (M + 1 + 1) (a := M) (b := M + 1 + 1) (by omega) (by omega) le_rfl rfl
          (PQ T M (M + 1 + 1)) (PQ_mem_up (hε := hε) M _) =
        gl T hε (M + 1 + 1) (a := a) (b := M + 1 + 1) (by omega) (by omega) le_rfl rfl
          (PQ T a (M + 1 + 1)) (PQ_mem_up (hε := hε) a _) := by
        rw [gl_lift M (a := a) (b := M) (by omega) (by omega) le_rfl rfl (PQ T a M) _,
          gl_comp (M + 1 + 1)]
        refine gl_congr (M + 1 + 1) _ _ _ _ _ _ ?_
        rw [capQ_PQ T hε (by omega), PQ_cup_mul (hε := hε) a M (by omega)]
      change P (gl T hε (M + 1 + 1) (a := a) (b := M + 1 + 1) _ _ _ _ (PQ T a (M + 1 + 1)) _)
      rw [← h1]
      exact hcomp ih (hcup M)
  have hdown : ∀ (b k : ℕ), P (gl T hε (b + 2 * k) (a := b + 2 * k) (b := b)
      le_rfl rfl (by omega) (by omega) (PQ T b (b + 2 * k)) (PQ_mem_down (hε := hε) b _)) := by
    intro b k
    induction k with
    | zero =>
      have e : gl T hε (b + 2 * 0) (a := b + 2 * 0) (b := b) le_rfl rfl (by omega) (by omega)
          (PQ T b (b + 2 * 0)) (PQ_mem_down (hε := hε) b _) = 𝟙 (GObj.mk b) := by
        show gl T hε b (a := b) (b := b) _ _ _ _ (PQ T b b) _ = 𝟙 (GObj.mk b)
        rw [gl_congr b _ _ _ _ _ (mem_top b 1) (PQ_self T b)]
        exact gl_id b
      rw [e]
      exact hid _
    | succ k ih =>
      set M := b + 2 * k
      have h1 : gl T hε (M + 1 + 1) (a := M + 1 + 1) (b := M) le_rfl rfl (by omega) (by omega)
          (PQ T M (M + 1 + 1)) (PQ_mem_down (hε := hε) M _) ≫
        gl T hε M (a := M) (b := b) le_rfl rfl (by omega) (by omega)
          (PQ T b M) (PQ_mem_down (hε := hε) b M) =
        gl T hε (M + 1 + 1) (a := M + 1 + 1) (b := b) le_rfl rfl (by omega) (by omega)
          (PQ T b (M + 1 + 1)) (PQ_mem_down (hε := hε) b _) := by
        rw [gl_lift M (a := M) (b := b) le_rfl rfl (by omega) (by omega) (PQ T b M) _,
          gl_comp (M + 1 + 1)]
        refine gl_congr (M + 1 + 1) _ _ _ _ _ _ ?_
        rw [capQ_PQ T hε (by omega), PQ_mul_cap (hε := hε) b M (by omega)]
      change P (gl T hε (M + 1 + 1) (a := M + 1 + 1) (b := b) _ _ _ _ (PQ T b (M + 1 + 1)) _)
      rw [← h1]
      exact hcomp (hcap M) ih
  have hup' : ∀ {a N : ℕ} (ha : a ≤ N) (pa : a % 2 = N % 2),
      P (gl T hε N ha pa le_rfl rfl (PQ T a N) (PQ_mem_up (hε := hε) a N)) := by
    intro a N ha pa
    obtain ⟨k, rfl⟩ : ∃ k, N = a + 2 * k := ⟨(N - a) / 2, by omega⟩
    exact hup a k
  have hdown' : ∀ {b N : ℕ} (hb : b ≤ N) (pb : b % 2 = N % 2),
      P (gl T hε N le_rfl rfl hb pb (PQ T b N) (PQ_mem_down (hε := hε) b N)) := by
    intro b N hb pb
    obtain ⟨k, rfl⟩ : ∃ k, N = b + 2 * k := ⟨(N - b) / 2, by omega⟩
    exact hdown b k
  intro ⟨a⟩ ⟨b⟩ f
  by_cases hp : a % 2 = b % 2
  swap
  · rw [hom_eq_zero_of_parity hp f]
    exact hzero
  set N := a + 2 * b
  have ha : a ≤ N := by omega
  have pa : a % 2 = N % 2 := by omega
  have hb : b ≤ N := by omega
  have pb : b % 2 = N % 2 := by omega
  set φ := lval (pre (X := GObj.mk a) (Y := GObj.mk b) N ha pa hb pb f)
  have hφ : φ ∈ HomSp T N a b := lval_mem _
  have hf : f = gl T hε N ha pa le_rfl rfl (PQ T a N) (PQ_mem_up (hε := hε) a N) ≫
      gl T hε N le_rfl rfl le_rfl rfl φ (mem_top N φ) ≫
      gl T hε N le_rfl rfl hb pb (PQ T b N) (PQ_mem_down (hε := hε) b N) := by
    rw [gl_comp N, gl_comp N, ← gl_pre (X := GObj.mk a) (Y := GObj.mk b) N ha pa hb pb f]
    exact gl_congr N ha pa hb pb hφ _ ((mem_Hom T).mp hφ).symm
  rw [hf]
  exact hcomp (hup' ha pa) (hcomp (hbase N φ) (hdown' hb pb))

theorem good1_all {X X' : GObj T hε} (f : X ⟶ X') : Good1 f :=
  glued_induction (@Good1 _ _ _ _ T hε) good1_id (@good1_zero _ _ _ _ T hε)
    (@Good1.comp _ _ _ _ T hε) good1_cup good1_cap good1_base f

theorem good2_all {Y Y' : GObj T hε} (g : Y ⟶ Y') : Good2 g :=
  glued_induction (@Good2 _ _ _ _ T hε) good2_id (@good2_zero _ _ _ _ T hε)
    (@Good2.comp _ _ _ _ T hε) good2_cup good2_cap good2_base g

/-- **Naturality of the associator on the glued category**, for arbitrary morphisms in all three
slots. -/
theorem assoc_nat {X Y Z X' Y' Z' : GObj T hε} (f : X ⟶ X') (g : Y ⟶ Y') (h : Z ⟶ Z') :
    AssocNat f g h := by
  have h12 := (good1_all f Y Z).comp (good2_all g X' Z)
  simp only [Category.comp_id, Category.id_comp] at h12
  have h123 := h12.comp (assocNat_third X' Y' h)
  simpa only [Category.comp_id, Category.id_comp] using h123

theorem tensHom_eqToHom_left {X X' : GObj T hε} (h : X = X') (Y : GObj T hε) :
    tensHom (eqToHom h) (𝟙 Y) = eqToHom (congrArg (fun U => tensObj U Y) h) := by
  subst h
  simp [tensHom_id]

theorem tensHom_eqToHom_right (X : GObj T hε) {Y Y' : GObj T hε} (h : Y = Y') :
    tensHom (𝟙 X) (eqToHom h) = eqToHom (congrArg (tensObj X) h) := by
  subst h
  simp [tensHom_id]

/-- **The Mac Lane pentagon** for `tensHom` and `eqToHom (tensObj_assoc · · ·)` on `GObj`. -/
theorem tensHom_pentagon (W X Y Z : GObj T hε) :
    tensHom (eqToHom (tensObj_assoc W X Y)) (𝟙 Z) ≫
      eqToHom (tensObj_assoc W (tensObj X Y) Z) ≫
      tensHom (𝟙 W) (eqToHom (tensObj_assoc X Y Z)) =
    eqToHom (tensObj_assoc (tensObj W X) Y Z) ≫
      eqToHom (tensObj_assoc W X (tensObj Y Z)) := by
  rw [tensHom_eqToHom_left, tensHom_eqToHom_right]
  simp

end Glued

end QOU.HeckeTemperleyLieb.TLGluedAssoc
