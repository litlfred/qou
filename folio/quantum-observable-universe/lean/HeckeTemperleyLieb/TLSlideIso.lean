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

end QOU.HeckeTemperleyLieb.TLSlideIso
