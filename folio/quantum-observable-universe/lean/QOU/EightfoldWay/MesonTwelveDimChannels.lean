/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/

import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.IntervalCases
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import QOU.EightfoldWay.MesonThreeByFourCharacterization

/-!
# Every coloured channel of classical dimension 12 has `dim_q = [3]_q [4]_q` (`§7c` generic)

Bean `qou-mk34` (compute accuracy C5, option 2). Mathematics only: no measured number.

`MesonRatioSelectionStatus` left one reading of `m_K² / m_π²` unexcluded: choosing the channel
`V₂ ⊗ Sym²_q W₃*`, whose quantum dimension is `[3]_q [4]_q`. This file shows that, once the
classical integer `12` is given, **the choice of channel among `U_q(sl₂) × U_q(sl₃)` isotypes does
not matter**:

1. `classical_dim_twelve_channels`: an isotype `V_n ⊗ W_(a,b)` (`n`-dimensional `sl₂` irrep,
   `sl₃` irrep of highest weight `(a,b)`, classical dimension `(a+1)(b+1)(a+b+2)/2`) has classical
   dimension `12` iff it is one of `V₂ ⊗ W_(2,0)`, `V₂ ⊗ W_(0,2)`, `V₄ ⊗ W_(1,0)`, `V₄ ⊗ W_(0,1)`,
   `V₁₂ ⊗ W_(0,0)`. (No `sl₃` irrep has dimension `2`, `4` or `12`.)
2. `twelve_channel_qdim`: each of the four with a nontrivial `sl₃` factor has quantum dimension
   exactly `[3]_q [4]_q`, as an identity over any field.
3. `qInt12_ne_qInt34_at_two`: the colourless one, `V₁₂`, has `[12]_q`, which is not `[3]_q[4]_q`.

**What this moves.** The premise behind `[3]_q [4]_q` is no longer "which channel"; it is
(i) the classical multiplicity `12` and (ii) a nontrivial colour factor. Neither is derived here.
Probe: `computations/meson/twelve_dim_channel_qdim_probe.py` (exact `sympy`, also records the first
tensor degree of each isotype in `(V₂ ⊕ W₃*)^{⊗k}`: `3, 5, 4, 5, 11`).
-/

set_option autoImplicit false

namespace QOU.EightfoldWay
namespace MesonTwelveDimChannels

open QOU.QInteger (qIntBal qIntBal_def)
open MesonThreeByFourCharacterization (qIntBal_small_laurent)

/-- Twice the classical dimension of the `sl₃` irrep of highest weight `(a, b)`. -/
def sl3DimTwice (a b : ℕ) : ℕ := (a + 1) * (b + 1) * (a + b + 2)

/-- Quantum dimension of the `U_q(sl₃)` irrep of highest weight `(a, b)`. -/
noncomputable def qDimSl3 {K : Type*} [Field K] (q : K) (a b : ℕ) : K :=
  qIntBal q (a + 1) * qIntBal q (b + 1) * qIntBal q (a + b + 2) / qIntBal q 2

/-- **Classification.** `n · dim W_(a,b) = 12` has exactly five solutions. -/
theorem classical_dim_twelve_channels (n a b : ℕ) (h : n * sl3DimTwice a b = 24) :
    (n = 2 ∧ (a = 2 ∧ b = 0 ∨ a = 0 ∧ b = 2)) ∨
    (n = 4 ∧ (a = 1 ∧ b = 0 ∨ a = 0 ∧ b = 1)) ∨
    (n = 12 ∧ a = 0 ∧ b = 0) := by
  unfold sl3DimTwice at h
  have hn : 1 ≤ n := by
    rcases Nat.eq_zero_or_pos n with h0 | h0
    · simp [h0] at h
    · exact h0
  have hX : (a + 1) * (b + 1) * (a + b + 2) ≤ 24 := by
    calc (a + 1) * (b + 1) * (a + b + 2) ≤ n * ((a + 1) * (b + 1) * (a + b + 2)) :=
          Nat.le_mul_of_pos_left _ hn
      _ = 24 := h
  have ha : a ≤ 3 := by
    by_contra hc
    push_neg at hc
    have : (a + 1) * (a + 2) ≤ (a + 1) * (b + 1) * (a + b + 2) := by
      have h1 : a + 1 ≤ (a + 1) * (b + 1) := Nat.le_mul_of_pos_right _ (Nat.succ_pos b)
      exact Nat.mul_le_mul h1 (by omega)
    nlinarith
  have hb : b ≤ 3 := by
    by_contra hc
    push_neg at hc
    have : (b + 1) * (b + 2) ≤ (a + 1) * (b + 1) * (a + b + 2) := by
      have h1 : b + 1 ≤ (a + 1) * (b + 1) := Nat.le_mul_of_pos_left _ (Nat.succ_pos a)
      exact Nat.mul_le_mul h1 (by omega)
    nlinarith
  interval_cases a <;> interval_cases b <;> omega

/-- **Every coloured classical-dimension-12 channel has `dim_q = [3]_q [4]_q`.** -/
theorem twelve_channel_qdim {K : Type*} [Field K] (q : K)
    (hq : q ≠ 0) (hqdiff : q - q⁻¹ ≠ 0) (hqsum : q + q⁻¹ ≠ 0)
    (n a b : ℕ) (h : n * sl3DimTwice a b = 24) (hcol : ¬ (a = 0 ∧ b = 0)) :
    qIntBal q n * qDimSl3 q a b = qIntBal q 3 * qIntBal q 4 := by
  obtain ⟨hb1, hb2, hb3, hb4, -⟩ := qIntBal_small_laurent q hq hqdiff
  have hq2 : qIntBal q 2 ≠ 0 := by rw [hb2]; exact hqsum
  rcases classical_dim_twelve_channels n a b h with
    ⟨rfl, ⟨rfl, rfl⟩ | ⟨rfl, rfl⟩⟩ | ⟨rfl, ⟨rfl, rfl⟩ | ⟨rfl, rfl⟩⟩ | ⟨-, rfl, rfl⟩
  · simp only [qDimSl3, Nat.reduceAdd, hb1]; field_simp [hq2]; try ring
  · simp only [qDimSl3, Nat.reduceAdd, hb1]; field_simp [hq2]; try ring
  · simp only [qDimSl3, Nat.reduceAdd, hb1]; field_simp [hq2]; try ring
  · simp only [qDimSl3, Nat.reduceAdd, hb1]; field_simp [hq2]; try ring
  · exact absurd ⟨rfl, rfl⟩ hcol

/-- The colourless channel `V₁₂` has `dim_q = [12]_q`. -/
theorem colourless_channel_qdim {K : Type*} [Field K] (q : K)
    (hq : q ≠ 0) (hqdiff : q - q⁻¹ ≠ 0) (hqsum : q + q⁻¹ ≠ 0) :
    qIntBal q 12 * qDimSl3 q 0 0 = qIntBal q 12 := by
  obtain ⟨hb1, hb2, -, -, -⟩ := qIntBal_small_laurent q hq hqdiff
  have hq2 : qIntBal q 2 ≠ 0 := by rw [hb2]; exact hqsum
  simp only [qDimSl3, Nat.reduceAdd, hb1]; field_simp [hq2]; try ring

/-- `[12]_q ≠ [3]_q [4]_q` as Laurent polynomials: they differ at `q = 2` over `ℚ`. -/
theorem qInt12_ne_qInt34_at_two :
    qIntBal (2 : ℚ) 12 ≠ qIntBal (2 : ℚ) 3 * qIntBal (2 : ℚ) 4 := by
  norm_num [qIntBal_def]

end MesonTwelveDimChannels
end QOU.EightfoldWay
