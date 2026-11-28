import HeckeTemperleyLieb.TLZigzag
import HeckeTemperleyLieb.TLTensorCorner

/-!
# The slide isomorphisms between a tensor corner and the standard corner

Bean `hkmt`. The tensor product `x ⊗ y` of two Temperley–Lieb elements (`tens`) puts the cups
of the first factor *between* the two blocks. The standard corner of the tensor product has all
its cups at the end. This file builds, level by level, explicit words that slide the cups of the
first factor past the whole second block, and proves how they behave when two strands are added.

* `slide_step`: conjugating `capEmb x ⊗ ψ` by one full slide is `capEmb` of the conjugate of
  `x ⊗ ψ`. This is the first-factor half of the compatibility with adding two strands.

Everything holds over any field with `δ ≠ 0`; only the Temperley–Lieb relations are used.

-- Ref: [kauffman1987] State models and the Jones polynomial, §3 (zigzag isotopy).
-- Ref: [leitner2026] the Temperley–Lieb chapter (bean `hkmt`).
-/

namespace QOU.HeckeTemperleyLieb.TLSlideIso

open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebMarkov
open QOU.HeckeTemperleyLieb.TLCupCap QOU.HeckeTemperleyLieb.TLCableBraiding
open QOU.HeckeTemperleyLieb.TLQuotientTensor QOU.HeckeTemperleyLieb.TLZigzag

variable {K : Type*} [Field K] {δ : K}

/-- `capEmb` multiplies out: three factors. -/
theorem capEmb_mul3 (hδ : δ ≠ 0) (n : ℕ) (u v w : TLFin K δ n) :
    capEmb δ n (u * v * w) = capEmb δ n u * capEmb δ n v * capEmb δ n w := by
  rw [capEmb_mul δ hδ, capEmb_mul δ hδ]

/-- **One step of the slide.** With `V` and `U` on the tensor level of `x ⊗ ψ`, the words
`δ⁻¹ capEmb V · zag` and `δ⁻¹ zig · capEmb U` conjugate `capEmb x ⊗ ψ` to `capEmb` of
`V (x ⊗ ψ) U`. -/
theorem slide_step (hδ : δ ≠ 0) {n m : ℕ} (x : TLFin K δ n) (ψ : TLFin K δ m)
    (U V : TLFin K δ (n + m + 1)) :
    (δ⁻¹ • (pl δ 0 (n + m + 1 + 1 + 1) (N := n + 1 + 1 + m + 1) (by omega) (capEmb δ _ V) *
        zag δ (n + 1 + 1 + m + 1) (n + 1) (m + 2))) * tens δ (capEmb δ n x) ψ *
      (δ⁻¹ • (zig δ (n + 1 + 1 + m + 1) (n + 1) (m + 2) *
        pl δ 0 (n + m + 1 + 1 + 1) (N := n + 1 + 1 + m + 1) (by omega) (capEmb δ _ U))) =
      pl δ 0 (n + m + 1 + 1 + 1) (N := n + 1 + 1 + m + 1) (by omega)
        (capEmb δ _ (V * tens δ x ψ * U)) := by
  have hc := slide_conj_capEmb (δ := δ) hδ (N := n + 1 + 1 + m + 1) (n := n) (m := m) (by omega)
    x ψ
  rw [TLQuotientBraiding.tens_eq_pl (capEmb δ n x) ψ] at *
  rw [capEmb_mul3 hδ, map_mul, map_mul, smul_mul_assoc, smul_mul_assoc, mul_smul_comm,
    smul_smul]
  have hr : ∀ (A B C Z W D : TLFin K δ (n + 1 + 1 + m + 1)),
      A * Z * (B * C) * (W * D) = A * (Z * (B * C) * W) * D := fun _ _ _ _ _ _ => by
    simp only [mul_assoc]
  rw [hr]
  erw [hc]
  rw [mul_smul_comm, smul_mul_assoc, smul_smul,
    show δ⁻¹ * δ⁻¹ * δ ^ 2 = 1 by field_simp, one_smul]

/-! ## The slide words, level by level -/

variable (δ) in
/-- The starting word at level `n = a`: the tensor corner `1_a ⊗ y` itself (and `0` elsewhere). -/
noncomputable def slideBase (a m : ℕ) (y : TLFin K δ m) (n : ℕ) : TLFin K δ (n + m + 1) :=
  if h : a = n then pl δ 0 (a + m + 1) (by omega) (tens δ (1 : TLFin K δ a) y) else 0

variable (δ) in
/-- **The slide word, source side.** `slideU a m y n` is the partial isometry from the standard
corner at level `n + m + 1` to the tensor corner `P_a^n ⊗ y`: start at `n = a` with the tensor
corner, and each time two strands are added to the first factor, slide the new cup past the
whole second block with `zig`. -/
noncomputable def slideU (a m : ℕ) (y : TLFin K δ m) : ∀ n, TLFin K δ (n + m + 1)
  | 0 => slideBase δ a m y 0
  | 1 => slideBase δ a m y 1
  | n + 2 => if a ≤ n then
      δ⁻¹ • (zig δ _ (n + 1) (m + 2) *
        pl δ 0 (n + m + 1 + 1 + 1) (by omega) (capEmb δ _ (slideU a m y n)))
    else slideBase δ a m y (n + 2)

variable (δ) in
/-- **The slide word, target side**: the same slides read backwards, with `zag`. -/
noncomputable def slideV (a m : ℕ) (y : TLFin K δ m) : ∀ n, TLFin K δ (n + m + 1)
  | 0 => slideBase δ a m y 0
  | 1 => slideBase δ a m y 1
  | n + 2 => if a ≤ n then
      δ⁻¹ • (pl δ 0 (n + m + 1 + 1 + 1) (by omega) (capEmb δ _ (slideV a m y n)) *
        zag δ _ (n + 1) (m + 2))
    else slideBase δ a m y (n + 2)

theorem slideBase_self (a m : ℕ) (y : TLFin K δ m) :
    slideBase δ a m y a = pl δ 0 (a + m + 1) (N := a + m + 1) (by omega) (tens δ (1 : TLFin K δ a) y) := by
  simp [slideBase]

theorem slideU_self (a m : ℕ) (y : TLFin K δ m) :
    slideU δ a m y a = pl δ 0 (a + m + 1) (N := a + m + 1) (by omega) (tens δ (1 : TLFin K δ a) y) := by
  rcases a with _ | _ | a
  · exact slideBase_self 0 m y
  · exact slideBase_self 1 m y
  · rw [slideU.eq_3, if_neg (by omega)]; exact slideBase_self _ m y

theorem slideV_self (a m : ℕ) (y : TLFin K δ m) :
    slideV δ a m y a = pl δ 0 (a + m + 1) (N := a + m + 1) (by omega) (tens δ (1 : TLFin K δ a) y) := by
  rcases a with _ | _ | a
  · exact slideBase_self 0 m y
  · exact slideBase_self 1 m y
  · rw [slideV.eq_3, if_neg (by omega)]; exact slideBase_self _ m y

theorem slideU_step {a m n : ℕ} (y : TLFin K δ m) (h : a ≤ n) :
    slideU δ a m y (n + 2) = δ⁻¹ • (zig δ _ (n + 1) (m + 2) *
      pl δ 0 (n + m + 1 + 1 + 1) (by omega) (capEmb δ _ (slideU δ a m y n))) := by
  rw [slideU.eq_3, if_pos h]

theorem slideV_step {a m n : ℕ} (y : TLFin K δ m) (h : a ≤ n) :
    slideV δ a m y (n + 2) = δ⁻¹ • (pl δ 0 (n + m + 1 + 1 + 1) (by omega)
      (capEmb δ _ (slideV δ a m y n)) * zag δ _ (n + 1) (m + 2)) := by
  rw [slideV.eq_3, if_pos h]

/-- **Adding two strands to the first factor.** Above both base levels, conjugating
`capEmb x ⊗ ψ` by the slide words is `capEmb` of conjugating `x ⊗ ψ`. -/
theorem slide_conj_succ (hδ : δ ≠ 0) {a a' m n : ℕ} (ha : a ≤ n) (ha' : a' ≤ n)
    (y y' : TLFin K δ m) (x : TLFin K δ n) (ψ : TLFin K δ m) :
    slideV δ a' m y' (n + 2) * tens δ (capEmb δ n x) ψ * slideU δ a m y (n + 2) =
      pl δ 0 (n + m + 1 + 1 + 1) (by omega)
        (capEmb δ _ (slideV δ a' m y' n * tens δ x ψ * slideU δ a m y n)) := by
  rw [slideU_step y ha, slideV_step y' ha']
  exact slide_step hδ x ψ _ _

/-! ## The slide words compose to the corners -/

theorem pl_zero_self {L : ℕ} (h : 0 + L ≤ L) (z : TLFin K δ L) : pl δ 0 L h z = z := by
  simpa using algHom_eq_of_gen (pl δ 0 L h) (AlgHom.id K _) (fun j => by
    rw [pl_e, AlgHom.id_apply, E_of_lt (by omega)]; congr 1; ext; simp) z

/-- The cup after `x ⊗ ψ`, conjugated back by the slide, is `δ²` times `capEmb x ⊗ ψ`. -/
theorem zig_capEmb_zag (hδ : δ ≠ 0) {n m : ℕ} (x : TLFin K δ n) (ψ : TLFin K δ m) :
    zig δ (n + 1 + 1 + m + 1) (n + 1) (m + 2) *
        pl δ 0 (n + m + 1 + 1 + 1) (N := n + 1 + 1 + m + 1) (by omega)
          (capEmb δ _ (tens δ x ψ)) * zag δ (n + 1 + 1 + m + 1) (n + 1) (m + 2) =
      δ ^ 2 • tens δ (capEmb δ n x) ψ := by
  have hb := cup_slide_block (δ := δ) hδ (N := n + 1 + 1 + m + 1) (n := n) (m := m) (by omega)
    x ψ
  have hg : pl δ 0 (n + m + 1 + 1 + 1) (N := n + 1 + 1 + m + 1) (by omega)
      (e K δ adjFin (Fin.last (n + m + 1 + 1))) = gen δ _ ((n + 1) + (m + 1)) := by
    rw [pl_e, gen_eq_E]; congr 1; simp; omega
  have hY := commute_pl_zig (δ := δ) (N := n + 1 + 1 + m + 1) (t := n + 1 + 1 + 1) (M := m)
    (p := n + 1) (k := 1) (by omega) (Or.inr (by omega)) ψ
  rw [zig_one] at hY
  have hcx : pl δ 0 (n + 1 + 1) (N := n + 1 + 1 + m + 1) (by omega) (capEmb δ n x) =
      δ⁻¹ • (pl δ 0 n (by omega) x * gen δ _ (n + 1)) := by
    rw [capEmb, map_smul, map_mul, pl_incl, pl_incl, pl_e, gen_eq_E]; congr 3; simp
  have hT : tens δ (capEmb δ n x) ψ * gen δ _ (n + 1) = δ • tens δ (capEmb δ n x) ψ := by
    rw [TLQuotientBraiding.tens_eq_pl, hcx]
    simp only [smul_mul_assoc, mul_assoc]
    rw [hY.eq, ← mul_assoc (gen δ _ _), gen_sq (by omega)]
    simp only [smul_mul_assoc, mul_smul_comm, smul_smul]
    rw [mul_comm]
  rw [capEmb, map_smul, map_mul, pl_incl, pl_incl, TLQuotientBraiding.tens_eq_pl x ψ, map_mul,
    pl_pl, pl_pl, hg]
  simp only [Nat.zero_add]
  rw [mul_smul_comm, smul_mul_assoc, ← mul_assoc, ← hb, mul_assoc _ (zig δ _ _ _),
    show m + 2 = (m + 1) + 1 from rfl, zig_mul_gen (by omega), mul_smul_comm, smul_mul_assoc,
    mul_assoc _ (zig δ _ _ _), zig_mul_zag_succ (by omega), mul_smul_comm]
  have e1 : pl δ 0 (n + 1 + 1) (N := n + 1 + 1 + m + 1) (by omega) (capEmb δ n x) *
      pl δ (n + 3) m (N := n + 1 + 1 + m + 1) (by omega) ψ = tens δ (capEmb δ n x) ψ :=
    (TLQuotientBraiding.tens_eq_pl _ _).symm
  rw [e1, hT, smul_smul, smul_smul, smul_smul]
  congr 1
  field_simp

theorem capEmb_mul_last (n : ℕ) (V : TLFin K δ n) :
    capEmb δ n V * e K δ adjFin (Fin.last (n + 1)) = δ • capEmb δ n V := by
  rw [capEmb, smul_mul_assoc, mul_assoc, e_sq' δ, mul_smul_comm, smul_comm]

/-- `V · U` one level up is `capEmb` of `V · U`: the slides cancel against each other. -/
theorem slideV_mul_slideU_step (hδ : δ ≠ 0) {a a' m n : ℕ} (ha : a ≤ n) (ha' : a' ≤ n)
    (y y' : TLFin K δ m) :
    slideV δ a' m y' (n + 2) * slideU δ a m y (n + 2) =
      pl δ 0 (n + m + 1 + 1 + 1) (by omega)
        (capEmb δ _ (slideV δ a' m y' n * slideU δ a m y n)) := by
  rw [slideU_step y ha, slideV_step y' ha', smul_mul_assoc, mul_smul_comm, smul_smul,
    mul_assoc, ← mul_assoc (zag δ _ _ _), show m + 2 = (m + 1) + 1 from rfl,
    zag_mul_zig (m + 1) (by omega), smul_mul_assoc, mul_smul_comm, ← mul_assoc]
  have hg : gen δ (n + 2 + m + 1) (n + 1 + (m + 1)) =
      pl δ 0 (n + m + 1 + 1 + 1) (N := n + 2 + m + 1) (by omega)
        (e K δ adjFin (Fin.last (n + m + 1 + 1))) := by
    rw [pl_e, gen_eq_E]; congr 1; simp; omega
  rw [hg, ← map_mul, capEmb_mul_last, map_smul, smul_mul_assoc, smul_smul, ← map_mul,
    ← capEmb_mul δ hδ, smul_smul, show δ⁻¹ * δ⁻¹ * δ * δ = 1 by field_simp, one_smul]

/-- If `U · V = x ⊗ ψ` then one level up `U · V = capEmb x ⊗ ψ`. -/
theorem slideU_mul_slideV_step (hδ : δ ≠ 0) {a a' m n : ℕ} (ha : a ≤ n) (ha' : a' ≤ n)
    (y y' : TLFin K δ m) (x : TLFin K δ n) (ψ : TLFin K δ m)
    (h : slideU δ a m y n * slideV δ a' m y' n = tens δ x ψ) :
    slideU δ a m y (n + 2) * slideV δ a' m y' (n + 2) = tens δ (capEmb δ n x) ψ := by
  rw [slideU_step y ha, slideV_step y' ha', smul_mul_assoc, mul_smul_comm, smul_smul,
    mul_assoc, ← mul_assoc (pl δ 0 _ _ _), ← map_mul, ← capEmb_mul δ hδ, h, ← mul_assoc]
  erw [zig_capEmb_zag hδ x ψ]
  rw [smul_smul, show δ⁻¹ * δ⁻¹ * δ ^ 2 = 1 by field_simp, one_smul]

/-! ## Closed forms on the corners -/

theorem pl_zero_P {L L' : ℕ} (hL : L = L') (h : 0 + L ≤ L') (c : ℕ) :
    pl δ 0 L h (TLRectHom.P δ c L) = TLRectHom.P δ c L' := by
  subst hL; exact pl_zero_self _ _

theorem recast_P {L L' : ℕ} (hL : L = L') (c : ℕ) :
    recast δ hL (TLRectHom.P δ c L) = TLRectHom.P δ c L' := by
  subst hL; rfl

/-- `1_a ⊗ P_b^{b+2j}` is the standard corner `P_{a+b+1}`: the second factor's cups are already
at the end. -/
theorem tens_one_P (a b j : ℕ) :
    tens δ (1 : TLFin K δ a) (TLRectHom.P δ b (b + 2 * j)) =
      TLRectHom.P δ (a + b + 1) (a + (b + 2 * j) + 1) := by
  rw [TLTensorCorner.P_cupIter, TLTensorCorner.tens_cupIter_right, tens_one,
    ← TLTensorCorner.P_cupIter, recast_P]

/-- **`U · V` is the tensor corner.** For an idempotent second corner `y`, at every level
`a + 2k` the slide words compose to `P_a ⊗ y`. -/
theorem slideU_mul_slideV (hδ : δ ≠ 0) (a m : ℕ) {y : TLFin K δ m} (hy : y * y = y) :
    ∀ k, slideU δ a m y (a + 2 * k) * slideV δ a m y (a + 2 * k) =
      tens δ (TLRectHom.P δ a (a + 2 * k)) y
  | 0 => by
    show slideU δ a m y a * slideV δ a m y a = tens δ (TLRectHom.P δ a a) y
    rw [slideU_self, slideV_self, pl_zero_self, tens_mul, one_mul, hy, TLRectHom.P_self]
  | k + 1 => by
    show slideU δ a m y (a + 2 * k + 2) * slideV δ a m y (a + 2 * k + 2) =
      tens δ (TLRectHom.P δ a (a + 2 * k + 1 + 1)) y
    rw [TLRectHom.P_succ_succ δ (n := a + 2 * k) (by omega)]
    exact slideU_mul_slideV_step hδ (by omega) (by omega) y y _ y (slideU_mul_slideV hδ a m hy k)

/-- **`V · U` is the standard corner.** If `1_a ⊗ y` is the standard corner `P_c` of its level
(as for `y = P_b`, `c = a + b + 1`), then at every level `a + 2k` the slide words compose the
other way to `P_c`. -/
theorem slideV_mul_slideU (hδ : δ ≠ 0) (a m c : ℕ) {y : TLFin K δ m} (hy : y * y = y)
    (hc : tens δ (1 : TLFin K δ a) y = TLRectHom.P δ c (a + m + 1)) (hca : c ≤ a + m + 1) :
    ∀ k, slideV δ a m y (a + 2 * k) * slideU δ a m y (a + 2 * k) =
      TLRectHom.P δ c (a + 2 * k + m + 1)
  | 0 => by
    show slideV δ a m y a * slideU δ a m y a = TLRectHom.P δ c (a + m + 1)
    rw [slideU_self, slideV_self, pl_zero_self, tens_mul, one_mul, hy, hc]
  | k + 1 => by
    show slideV δ a m y (a + 2 * k + 2) * slideU δ a m y (a + 2 * k + 2) =
      TLRectHom.P δ c (a + 2 * k + 2 + m + 1)
    rw [slideV_mul_slideU_step hδ (by omega) (by omega) y y, slideV_mul_slideU hδ a m c hy hc hca k,
      ← TLRectHom.P_succ_succ δ (by omega), pl_zero_P (by omega)]

/-! ## Adding two strands to the second factor

The second factor gets its new cup at the right end, so no slide is needed: the slide words
of `capEmb y` are `capEmb` of the slide words of `y`. -/

theorem pl_gen {N t M i : ℕ} (h : t + M ≤ N) (hi : i < M) :
    pl δ t M h (gen δ M i) = gen δ N (t + i) := by
  rw [gen_eq_E, gen_eq_E, pl_E t M h hi]

theorem pl_zig {N t M p : ℕ} (h : t + M ≤ N) :
    ∀ k, p + k ≤ M → pl δ t M h (zig δ M p k) = zig δ N (t + p) k
  | 0, _ => by simp [zig]
  | k + 1, hk => by
    rw [zig_succ, zig_succ, map_mul, pl_zig h k (by omega), pl_gen h (by omega), add_assoc]

theorem pl_capEmb {N t L : ℕ} (h : t + (L + 1 + 1) ≤ N) (z : TLFin K δ L) :
    pl δ t (L + 1 + 1) h (capEmb δ L z) =
      δ⁻¹ • (pl δ t L (by omega) z * gen δ N (t + L + 1)) := by
  rw [capEmb, map_smul, map_mul, pl_incl, pl_incl, pl_e, gen_eq_E]
  simp [add_assoc]

theorem pl_zag {N t M p : ℕ} (h : t + M ≤ N) :
    ∀ k, p + k ≤ M → pl δ t M h (zag δ M p k) = zag δ N (t + p) k
  | 0, _ => by simp [zag]
  | k + 1, hk => by
    rw [zag_succ, zag_succ, map_mul, pl_zag h k (by omega), pl_gen h (by omega), add_assoc]

theorem slideBase_capEmb_right (a m : ℕ) (y : TLFin K δ m) (n : ℕ) :
    slideBase δ a (m + 1 + 1) (capEmb δ m y) n = capEmb δ (n + m + 1) (slideBase δ a m y n) := by
  unfold slideBase
  split_ifs with h
  · subst h
    rw [pl_zero_self, pl_zero_self, TLTensorCorner.tens_capEmb_right]
  · rw [capEmb_zero]

/-- **The core word identity.** A block `Y` on the first `L + 1` strands, then the cups at
`L + 1` and `L + 3`: pushing it through the long zigzag is the same as pushing it through the
short one and adding the cup at `L + 3` afterwards. -/
theorem zig_capEmb_two {N L p j : ℕ} (hp : p + j = L + 1) (hN : L + 3 < N) (Y : TLFin K δ N)
    (hY : ∀ i, L + 1 ≤ i → Commute Y (gen δ N i)) :
    zig δ N p (j + 1 + 1 + 1) * (Y * gen δ N (L + 1) * gen δ N (L + 3)) =
      zig δ N p (j + 1) * (Y * gen δ N (L + 1)) * gen δ N (L + 3) := by
  set g1 := gen δ N (L + 1)
  set g2 := gen δ N (L + 2)
  set g3 := gen δ N (L + 3)
  set z := zig δ N p (j + 1)
  have hz : zig δ N p (j + 1 + 1 + 1) = z * g2 * g3 := by
    simp only [z, zig_succ, g2, g3]
    rw [show p + (j + 1) = L + 2 by omega, show p + (j + 1 + 1) = L + 3 by omega]
  have hz1 : z * g1 = δ • z := by
    have := zig_mul_gen (δ := δ) (n := N) (p := p) (k := j) (by omega)
    rwa [hp] at this
  have hz121 : z * g2 * g1 = z := by
    simp only [z, zig_succ]
    rw [hp, mul_assoc, mul_assoc, ← mul_assoc g1, gen_adj_up (by omega)]
  have h13 : g3 * g1 = g1 * g3 := (commute_gen (Or.inl (by omega))).eq.symm
  have h33 : g3 * g3 = δ • g3 := gen_sq (by omega)
  have hY1 := (hY (L + 1) le_rfl).eq
  have hY23 : Commute Y (g2 * g3) := (hY (L + 2) (by omega)).mul_right (hY (L + 3) (by omega))
  have hY21 : Commute Y (g2 * g1) := (hY (L + 2) (by omega)).mul_right (hY (L + 1) le_rfl)
  rw [hz]
  calc z * g2 * g3 * (Y * g1 * g3)
      = z * ((g2 * g3) * Y) * (g1 * g3) := by simp only [mul_assoc]
    _ = z * Y * (g2 * (g3 * g1) * g3) := by rw [← hY23.eq]; simp only [mul_assoc]
    _ = δ • (z * (Y * (g2 * g1)) * g3) := by
        rw [h13, mul_assoc g2, mul_assoc g1, h33]
        simp only [mul_smul_comm, mul_assoc]
    _ = δ • (z * Y * g3) := by
        rw [hY21.eq, ← mul_assoc, ← mul_assoc, hz121]
    _ = z * (Y * g1) * g3 := by
        rw [hY1, ← mul_assoc, hz1, smul_mul_assoc, smul_mul_assoc]

theorem slideU_capEmb_right (hδ : δ ≠ 0) (a m : ℕ) (y : TLFin K δ m) :
    ∀ n, slideU δ a (m + 1 + 1) (capEmb δ m y) n = capEmb δ (n + m + 1) (slideU δ a m y n)
  | 0 => slideBase_capEmb_right a m y 0
  | 1 => slideBase_capEmb_right a m y 1
  | n + 2 => by
    by_cases h : a ≤ n
    · rw [slideU_step _ h, slideU_step _ h, slideU_capEmb_right hδ a m y n]
      refine (pl_zero_self (L := n + 1 + 1 + m + 1 + 1 + 1) (by omega) _).symm.trans
        (Eq.trans ?_ (pl_zero_self (L := n + 1 + 1 + m + 1 + 1 + 1) (by omega) _))
      rw [map_smul, map_mul]
      erw [pl_zig (M := n + 1 + 1 + m + 1 + 1 + 1) (p := n + 1) _ (m + 1 + 1 + 2) (by omega)]
      rw [pl_pl, pl_capEmb (L := n + (m + 1 + 1) + 1), pl_capEmb (L := n + m + 1)]
      rw [pl_capEmb (L := n + 1 + 1 + m + 1), map_smul, map_mul,
        pl_zig (M := n + 1 + 1 + m + 1) (p := n + 1) _ (m + 2) (by omega)]
      erw [pl_capEmb (L := n + m + 1)]
      rw [map_smul, map_mul, pl_pl, pl_gen _ (by omega)]
      simp only [Nat.zero_add, smul_mul_assoc, mul_smul_comm, smul_smul]
      congr 1
      rw [show gen δ (n + 1 + 1 + m + 1 + 1 + 1) (n + (m + 1 + 1) + 1 + 1) =
          gen δ (n + 1 + 1 + m + 1 + 1 + 1) (n + m + 1 + 3) from congrArg _ (by omega),
        show gen δ (n + 1 + 1 + m + 1 + 1 + 1) (n + 1 + 1 + m + 1 + 1) =
          gen δ (n + 1 + 1 + m + 1 + 1 + 1) (n + m + 1 + 3) from congrArg _ (by omega)]
      exact zig_capEmb_two (N := n + 1 + 1 + m + 1 + 1 + 1) (p := n + 1) (L := n + m + 1) (j := m + 1) (by omega) (by omega) (pl δ 0 (n + m + 1) (by omega) (slideU δ a m y n)) (fun i hi => by
        have := commute_pl_zig (δ := δ) (t := 0) (M := n + m + 1) (p := i) (k := 1)
          (N := n + 1 + 1 + m + 1 + 1 + 1) (by omega) (Or.inl (by omega)) (slideU δ a m y n)
        rwa [zig_one] at this)
    · rw [slideU.eq_3, slideU.eq_3, if_neg h, if_neg h]
      exact slideBase_capEmb_right a m y (n + 2)

/-- The mirror of `zig_capEmb_two`, through `zag`. -/
theorem zag_capEmb_two {N L p j : ℕ} (hp : p + j = L + 1) (hN : L + 3 < N) (Y : TLFin K δ N) :
    Y * gen δ N (L + 1) * gen δ N (L + 3) * zag δ N p (j + 1 + 1 + 1) =
      Y * gen δ N (L + 1) * zag δ N p (j + 1) * gen δ N (L + 3) := by
  set g1 := gen δ N (L + 1)
  set g2 := gen δ N (L + 2)
  set g3 := gen δ N (L + 3)
  set z := zag δ N p (j + 1)
  have hz : zag δ N p (j + 1 + 1 + 1) = g3 * (g2 * z) := by
    simp only [z, zag_succ, g2, g3]
    rw [show p + (j + 1) = L + 2 by omega, show p + (j + 1 + 1) = L + 3 by omega]
  have hzj : z = g1 * zag δ N p j := by simp only [z, zag_succ, g1]; rw [hp]
  have h121 : g1 * g2 * g1 = g1 := gen_adj_up (by omega)
  have h11 : g1 * g1 = δ • g1 := gen_sq (by omega)
  have h13 : g1 * g3 = g3 * g1 := (commute_gen (Or.inl (by omega))).eq
  have h33 : g3 * g3 = δ • g3 := gen_sq (by omega)
  have hz3 : z * g3 = g3 * z := (commute_zag (j + 1) (Or.inr (by omega))).eq.symm
  rw [hz]
  calc Y * g1 * g3 * (g3 * (g2 * z))
      = δ • (Y * (g1 * g3) * g2 * z) := by
        rw [mul_assoc (Y * g1) g3, ← mul_assoc g3 g3, h33]
        simp only [smul_mul_assoc, mul_smul_comm, mul_assoc]
    _ = δ • (Y * g3 * z) := by
        rw [h13, hzj]; simp only [mul_assoc]; rw [← mul_assoc g1 g2, ← mul_assoc (g1 * g2), h121]
    _ = Y * g1 * z * g3 := by
        rw [mul_assoc (Y * g1) z, hz3, ← mul_assoc, mul_assoc Y g1 g3, h13, hzj]
        simp only [mul_assoc]
        rw [← mul_assoc g1 g1, h11]
        simp only [smul_mul_assoc, mul_smul_comm]

theorem slideV_capEmb_right (hδ : δ ≠ 0) (a m : ℕ) (y : TLFin K δ m) :
    ∀ n, slideV δ a (m + 1 + 1) (capEmb δ m y) n = capEmb δ (n + m + 1) (slideV δ a m y n)
  | 0 => slideBase_capEmb_right a m y 0
  | 1 => slideBase_capEmb_right a m y 1
  | n + 2 => by
    by_cases h : a ≤ n
    · rw [slideV_step _ h, slideV_step _ h, slideV_capEmb_right hδ a m y n]
      refine (pl_zero_self (L := n + 1 + 1 + m + 1 + 1 + 1) (by omega) _).symm.trans
        (Eq.trans ?_ (pl_zero_self (L := n + 1 + 1 + m + 1 + 1 + 1) (by omega) _))
      rw [map_smul, map_mul]
      erw [pl_zag (M := n + 1 + 1 + m + 1 + 1 + 1) (p := n + 1) _ (m + 1 + 1 + 2) (by omega)]
      rw [pl_pl, pl_capEmb (L := n + (m + 1 + 1) + 1)]
      erw [pl_capEmb (L := n + m + 1)]
      rw [pl_capEmb (L := n + 1 + 1 + m + 1), map_smul, map_mul,
        pl_zag (M := n + 1 + 1 + m + 1) (p := n + 1) _ (m + 2) (by omega)]
      erw [pl_capEmb (L := n + m + 1)]
      rw [map_smul, map_mul, pl_pl, pl_gen _ (by omega)]
      simp only [Nat.zero_add, smul_mul_assoc, smul_smul]
      congr 1
      rw [show gen δ (n + 1 + 1 + m + 1 + 1 + 1) (n + (m + 1 + 1) + 1 + 1) =
          gen δ (n + 1 + 1 + m + 1 + 1 + 1) (n + m + 1 + 3) from congrArg _ (by omega),
        show gen δ (n + 1 + 1 + m + 1 + 1 + 1) (n + 1 + 1 + m + 1 + 1) =
          gen δ (n + 1 + 1 + m + 1 + 1 + 1) (n + m + 1 + 3) from congrArg _ (by omega)]
      exact zag_capEmb_two (N := n + 1 + 1 + m + 1 + 1 + 1) (p := n + 1) (L := n + m + 1)
        (j := m + 1) (by omega) (by omega) (pl δ 0 (n + m + 1) (by omega) (slideV δ a m y n))
    · rw [slideV.eq_3, slideV.eq_3, if_neg h, if_neg h]
      exact slideBase_capEmb_right a m y (n + 2)

/-- **Adding two strands to the second factor.** Conjugating `x ⊗ capEmb ψ` by the slide words
of `capEmb y`, `capEmb y'` is `capEmb` of conjugating `x ⊗ ψ`. -/
theorem slide_conj_capEmb_right (hδ : δ ≠ 0) {a a' m n : ℕ} (y y' : TLFin K δ m)
    (x : TLFin K δ n) (ψ : TLFin K δ m) :
    slideV δ a' (m + 1 + 1) (capEmb δ m y') n * tens δ x (capEmb δ m ψ) *
        slideU δ a (m + 1 + 1) (capEmb δ m y) n =
      capEmb δ (n + m + 1) (slideV δ a' m y' n * tens δ x ψ * slideU δ a m y n) := by
  rw [slideV_capEmb_right hδ, slideU_capEmb_right hδ, TLTensorCorner.tens_capEmb_right,
    capEmb_mul3 hδ]

end QOU.HeckeTemperleyLieb.TLSlideIso
