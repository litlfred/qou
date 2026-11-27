/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.Topology.Order.IntermediateValue
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import QOU.MassTheory.BringSchwingerNormalizationDerivation
import QOU.MassTheory.EmFermionLoopFourTopology

/-!
# Two-Loop Bring–Schwinger Fixed-Point Equation, `(8π)²` Tiling Measure, and `§3b-cond` Bridge (`ℝ`)

This module formalizes the archimedean (`ℝ`) half of beans `qou-l4t2` and `qou-9y43`, consuming the
generic `[CommRing]` / `[Field]` 4-topology cancellation identities of
`QOU.Archimedean.EmFermionLoopFourTopology` via `(K := ℝ)` instantiation per `AGENTS.md` §7c:

1. **Section 1 — Two-Loop Bring–Schwinger Fixed-Point Equation, `(8π)²` Tiling Factorization, and
   Weak-Coupling Existence & Uniqueness (`ℝ`):**
   - Defines `IsTwoLoopBringFixedPoint T_tree G q c_loop c2_add α` and proves unconditional
     equivalence to `twoLoopBringCubic T_tree G q c_loop c2_add α = 0` (`twoLoopBringFixedPoint_iff_cubic`).
   - Instantiates `four_topology_bar_hermitian_moment_sum (K := ℝ)` to link the 4-topology
     bar-Hermitian `EmFermionLoop` dressing `1 + α * (m_pm + m_mp - m_pp - m_mm) = 1 - (hHecke q)² * α`
     directly to `IsTwoLoopBringFixedPoint` (`twoLoopBringFixedPoint_of_four_topology_sum`).
   - Proves that the `EmFermionLoop` weight-3 Bloch-`B₃` candidate
     `c2_add = habiroNorm q * (delta_B3 / (Real.pi * firstBetti 4))` factors over the squared
     tiling Betti period `(8π)² = (π · (2 - bringTilingEuler))²` (`twoLoop_blochB3_tiling_measure`).
   - Proves unconditional existence and uniqueness of a positive root `α > 0` for any cubic
     `a₃ * α³ + a₂ * α² + a₁ * α - 1 = 0` with `0 ≤ a₃`, `0 ≤ a₂`, `0 < a₁`
     (`exists_unique_pos_cubic_root`).

2. **Section 2 — Non-Vacuous `§3b-cond` Hypothesis Class & `trivialModel` Consistency Witness:**
   Packages the open physical two-loop Bloch-`B₃` coupling bridge in
   `AlphaEmTwoLoopBlochSchwingerClass` with **zero global instances** and a concrete
   `def trivialModel` consistency witness (`lean-generation` §5).
-/

set_option autoImplicit false

namespace QOU.Archimedean
namespace AlphaEmTwoLoopBlochSchwinger

open QOU.QInteger (qIntBal)
open QOU.Archimedean.BringSchwingerNormalizationDerivation (habiroNorm hHecke)
open QOU.Archimedean.EmFermionLoopFourTopology (four_topology_bar_hermitian_moment_sum)

/-! ## Section 1: Two-Loop Bring–Schwinger Fixed-Point Equation, `(8π)²` Tiling Measure, and Uniqueness -/

section TwoLoopBringFixedPointReal

/-- **Two-Loop Bring–Schwinger Self-Consistency Relation on `ℝ`**:
Extends `IsUnifiedBringFixedPoint` (`s = +1`) with an explicit additive two-loop `O(α²)`
remainder `c2_add * α ^ 2`:
`1 / α = (T_tree + 2 * G / bringSurfaceArea) + α * habiroNorm q * (1 - c_loop * α) + c2_add * α ^ 2`. -/
def IsTwoLoopBringFixedPoint (T_tree G q c_loop c2_add α : ℝ) : Prop :=
  1 / α =
    (T_tree + (2 * G) / bringSurfaceArea) +
      α * habiroNorm q * (1 - c_loop * α) +
      c2_add * α ^ 2

/-- Characteristic cubic polynomial corresponding to `IsTwoLoopBringFixedPoint`:
`P₂(α) = (c2_add - c_loop * habiroNorm q) * α³ + habiroNorm q * α² + (T_tree + 2G / bringSurfaceArea) * α - 1`. -/
noncomputable def twoLoopBringCubic (T_tree G q c_loop c2_add α : ℝ) : ℝ :=
  (c2_add - c_loop * habiroNorm q) * α ^ 3 +
    habiroNorm q * α ^ 2 +
    (T_tree + (2 * G) / bringSurfaceArea) * α - 1

/-- **Unconditional Algebraic Equivalence (`twoLoopBringFixedPoint_iff_cubic`)**:
For every nonzero `α : ℝ`, `IsTwoLoopBringFixedPoint T_tree G q c_loop c2_add α` holds if and
only if `twoLoopBringCubic T_tree G q c_loop c2_add α = 0`. -/
theorem twoLoopBringFixedPoint_iff_cubic (T_tree G q c_loop c2_add α : ℝ) (hα : α ≠ 0) :
    IsTwoLoopBringFixedPoint T_tree G q c_loop c2_add α ↔
      twoLoopBringCubic T_tree G q c_loop c2_add α = 0 := by
  unfold IsTwoLoopBringFixedPoint twoLoopBringCubic
  rw [div_eq_iff hα]
  constructor
  · intro h; linear_combination -h
  · intro h; linear_combination -h

/-- **`§7c` Bridge from Generic Four-Topology Moment Sum (`(K := ℝ)`)**:
Instantiates `EmFermionLoopFourTopology.four_topology_bar_hermitian_moment_sum (K := ℝ)` to show
that replacing `1 - (hHecke q)² * α` by the 4-topology dressed factor
`1 + α * (1 + 1 - (hHecke q * m_sig + 1) - (1 - hHecke q * m_sig + (hHecke q)²))` yields an
identical `IsTwoLoopBringFixedPoint` equation for **every** first-moment tadpole `m_sig : ℝ`. -/
theorem twoLoopBringFixedPoint_of_four_topology_sum
    (T_tree G q m_sig c2_add α : ℝ) :
    (1 / α =
      (T_tree + (2 * G) / bringSurfaceArea) +
        α * habiroNorm q *
          (1 + α * ((1 : ℝ) + 1 - (hHecke q * m_sig + 1) -
            (1 - hHecke q * m_sig + (hHecke q) ^ 2))) +
        c2_add * α ^ 2) ↔
    IsTwoLoopBringFixedPoint T_tree G q ((hHecke q) ^ 2) c2_add α := by
  have h4 :=
    (four_topology_bar_hermitian_moment_sum (K := ℝ) (hHecke q) m_sig α).2.2.2
  unfold IsTwoLoopBringFixedPoint
  rw [h4]

/-- **Two-Loop `(8π)² = (π b₁(Σ₄))²` Tiling Measure Factorization**:
The `EmFermionLoop` weight-3 Bloch-`B₃` candidate
`habiroNorm q * (delta_B3 / (Real.pi * firstBetti 4))` equals both
`((q + q⁻¹) * delta_B3) / (64 * Real.pi ^ 2)` and
`((q + q⁻¹) * delta_B3) / (Real.pi * ((2 - bringTilingEuler : ℤ) : ℝ)) ^ 2`. -/
theorem twoLoop_blochB3_tiling_measure (q delta_B3 : ℝ) :
    habiroNorm q * (delta_B3 / (Real.pi * firstBetti 4)) =
      ((q + q⁻¹) * delta_B3) / (64 * Real.pi ^ 2) ∧
    habiroNorm q * (delta_B3 / (Real.pi * firstBetti 4)) =
      ((q + q⁻¹) * delta_B3) / (Real.pi * ((2 - bringTilingEuler : ℤ) : ℝ)) ^ 2 := by
  have hπ : Real.pi ≠ 0 := Real.pi_ne_zero
  have h1 :
      habiroNorm q * (delta_B3 / (Real.pi * firstBetti 4)) =
        ((q + q⁻¹) * delta_B3) / (64 * Real.pi ^ 2) := by
    unfold habiroNorm firstBetti
    field_simp
    ring
  refine ⟨h1, ?_⟩
  rw [h1, bringTiling_b1]
  push_cast
  ring

/-- **Strict Monotonicity, Existence, and Uniqueness on `(0, ∞)` (`exists_unique_pos_cubic_root`)**:
For any real polynomial `P(α) = a₃ * α³ + a₂ * α² + a₁ * α - 1` with `0 ≤ a₃`, `0 ≤ a₂`,
and `0 < a₁`, there exists a **unique** positive real number `α > 0` satisfying `P(α) = 0`. -/
theorem exists_unique_pos_cubic_root (a₃ a₂ a₁ : ℝ)
    (ha3 : 0 ≤ a₃) (ha2 : 0 ≤ a₂) (ha1 : 0 < a₁) :
    ∃! α : ℝ, 0 < α ∧ a₃ * α ^ 3 + a₂ * α ^ 2 + a₁ * α - 1 = 0 := by
  let f : ℝ → ℝ := fun x => a₃ * x ^ 3 + a₂ * x ^ 2 + a₁ * x - 1
  have hcont : Continuous f := by continuity
  have hf0 : f 0 = -1 := by simp [f]
  have htop_pos : 0 < 1 / a₁ := div_pos zero_lt_one ha1
  have hftop : 0 ≤ f (1 / a₁) := by
    dsimp only [f]
    have hmul : a₁ * (1 / a₁) = 1 := mul_one_div_cancel (ne_of_gt ha1)
    have hpow2 : 0 ≤ a₂ * (1 / a₁) ^ 2 := mul_nonneg ha2 (sq_nonneg _)
    have hpow3 : 0 ≤ a₃ * (1 / a₁) ^ 3 := mul_nonneg ha3 (pow_nonneg (le_of_lt htop_pos) 3)
    linarith
  have hivt : (0 : ℝ) ∈ Set.Icc (f 0) (f (1 / a₁)) := by
    rw [hf0]
    exact ⟨by norm_num, hftop⟩
  obtain ⟨r, hr_mem, hr_eq⟩ := intermediate_value_Icc (le_of_lt htop_pos) hcont.continuousOn hivt
  have hr_pos : 0 < r := by
    rcases lt_or_eq_of_le hr_mem.1 with hlt | rfl
    · exact hlt
    · linarith [hf0, hr_eq]
  refine ⟨r, ⟨hr_pos, hr_eq⟩, ?_⟩
  intro y ⟨hy_pos, hy_eq⟩
  by_contra hne
  rcases lt_trichotomy y r with hlt | heq | hgt
  · have hdiff : f r - f y > 0 := by
      dsimp only [f]
      have h1 : a₁ * (r - y) > 0 := mul_pos ha1 (sub_pos.mpr hlt)
      have h2 : a₂ * (r ^ 2 - y ^ 2) ≥ 0 := by
        have : r ^ 2 - y ^ 2 = (r - y) * (r + y) := by ring
        rw [this]
        exact mul_nonneg ha2 (mul_nonneg (le_of_lt (sub_pos.mpr hlt)) (by linarith))
      have h3 : a₃ * (r ^ 3 - y ^ 3) ≥ 0 := by
        have : r ^ 3 - y ^ 3 = (r - y) * (r ^ 2 + r * y + y ^ 2) := by ring
        rw [this]
        have hquad : 0 ≤ r ^ 2 + r * y + y ^ 2 := by nlinarith
        exact mul_nonneg ha3 (mul_nonneg (le_of_lt (sub_pos.mpr hlt)) hquad)
      linarith
    linarith [hr_eq, hy_eq]
  · exact hne heq
  · have hdiff : f y - f r > 0 := by
      dsimp only [f]
      have h1 : a₁ * (y - r) > 0 := mul_pos ha1 (sub_pos.mpr hgt)
      have h2 : a₂ * (y ^ 2 - r ^ 2) ≥ 0 := by
        have : y ^ 2 - r ^ 2 = (y - r) * (y + r) := by ring
        rw [this]
        exact mul_nonneg ha2 (mul_nonneg (le_of_lt (sub_pos.mpr hgt)) (by linarith))
      have h3 : a₃ * (y ^ 3 - r ^ 3) ≥ 0 := by
        have : y ^ 3 - r ^ 3 = (y - r) * (y ^ 2 + y * r + r ^ 2) := by ring
        rw [this]
        have hquad : 0 ≤ y ^ 2 + y * r + r ^ 2 := by nlinarith
        exact mul_nonneg ha3 (mul_nonneg (le_of_lt (sub_pos.mpr hgt)) hquad)
      linarith
    linarith [hr_eq, hy_eq]

end TwoLoopBringFixedPointReal

/-! ## Section 2: `§3b-cond` Hypothesis Class & `trivialModel` Consistency Witness -/

section ConditionalTwoLoopBridge

/-- **Conjecture Carrier (`§3b-cond`, Content-Bearing, Zero Global Instances)**:
Packages the working-assumption hypothesis that an electromagnetic coupling `α > 0` at substrate
parameter `q > 1` with non-negative weight-3 Bloch-`B₃` defect `delta_B3 ≥ 0` satisfies the
two-loop Bring–Schwinger fixed-point equation with fibre skein coefficient `(hHecke q)²` and
archimedean two-loop coefficient `habiroNorm q * (delta_B3 / (Real.pi * firstBetti 4))`. -/
class AlphaEmTwoLoopBlochSchwingerClass (q delta_B3 α : ℝ) : Prop where
  /-- Substrate parameter lies in the hyperbolic / real-`q` regime `q > 1`. -/
  one_lt_q : 1 < q
  /-- Weight-3 Bloch-`B₃` trilogarithm defect `Δ_{B₃}(q) = ζ(3) - Li₃(q⁻²)` is non-negative. -/
  delta_B3_nonneg : 0 ≤ delta_B3
  /-- Coupling `α` is strictly positive. -/
  alpha_pos : 0 < α
  /-- Two-loop Bring–Schwinger self-consistency relation holds. -/
  two_loop_self_consistent :
    IsTwoLoopBringFixedPoint
      (q * qIntBal q 9 * qIntBal q 10)
      4
      q
      ((hHecke q) ^ 2)
      (habiroNorm q * (delta_B3 / (Real.pi * firstBetti 4)))
      α

/-- **Conditional Two-Loop Cubic & Tiling-Measure Theorem (`§3b-cond`)**:
Under `[AlphaEmTwoLoopBlochSchwingerClass q delta_B3 α]`, `α` satisfies `twoLoopBringCubic = 0`
and the archimedean two-loop coefficient equals `((q + q⁻¹) * delta_B3) / (64 * Real.pi ^ 2)`. -/
theorem alpha_em_two_loop_cubic_and_tiling_measure (q delta_B3 α : ℝ)
    [inst : AlphaEmTwoLoopBlochSchwingerClass q delta_B3 α] :
    twoLoopBringCubic
      (q * qIntBal q 9 * qIntBal q 10)
      4
      q
      ((hHecke q) ^ 2)
      (habiroNorm q * (delta_B3 / (Real.pi * firstBetti 4)))
      α = 0 ∧
    habiroNorm q * (delta_B3 / (Real.pi * firstBetti 4)) =
      ((q + q⁻¹) * delta_B3) / (64 * Real.pi ^ 2) := by
  refine ⟨?_, (twoLoop_blochB3_tiling_measure q delta_B3).1⟩
  have hα : α ≠ 0 := ne_of_gt inst.alpha_pos
  exact (twoLoopBringFixedPoint_iff_cubic _ _ _ _ _ α hα).mp inst.two_loop_self_consistent

/-- **Non-Vacuity / Consistency Witness (`def`, NEVER `instance` — `lean-generation` §5)**:
Constructs an explicit mathematical model `(q = 2, delta_B3 = 8 * Real.pi * (hHecke 2) ^ 2)`
satisfying `AlphaEmTwoLoopBlochSchwingerClass`, proving the hypothesis bundle is consistent
without registering any global typeclass instance. -/
noncomputable def trivialModel :
    ∃ (q delta_B3 α : ℝ), AlphaEmTwoLoopBlochSchwingerClass q delta_B3 α := by
  let q : ℝ := 2
  let delta_B3 : ℝ := (Real.pi * firstBetti 4) * (hHecke q) ^ 2
  let t_tree : ℝ := q * qIntBal q 9 * qIntBal q 10
  let c2 : ℝ := habiroNorm q * (delta_B3 / (Real.pi * firstBetti 4))
  have hπ_pos : 0 < Real.pi := Real.pi_pos
  have hb1_pos : 0 < firstBetti 4 := by unfold firstBetti; norm_num
  have hdelta_nonneg : 0 ≤ delta_B3 := by
    dsimp only [delta_B3]
    exact mul_nonneg (le_of_lt (mul_pos hπ_pos hb1_pos)) (sq_nonneg _)
  have hc3_zero : c2 - (hHecke q) ^ 2 * habiroNorm q = 0 := by
    dsimp only [c2, delta_B3]
    have hden : Real.pi * firstBetti 4 ≠ 0 := ne_of_gt (mul_pos hπ_pos hb1_pos)
    field_simp
    ring
  have hhab_nonneg : 0 ≤ habiroNorm q := by
    unfold habiroNorm
    apply div_nonneg
    · dsimp only [q]; norm_num
    · linarith
  have hqbal_pos : ∀ n : ℕ, 1 ≤ n → 0 < qIntBal q n := by
    intro n hn
    rw [QOU.QInteger.qIntBal_def]
    dsimp only [q]
    apply div_pos
    · have hpow : (1 : ℝ) < (2 : ℝ) ^ n := one_lt_pow₀ (by norm_num) (by omega)
      have hinv : ((2 : ℝ)⁻¹) ^ n < 1 := pow_lt_one₀ (by norm_num) (by norm_num) (by omega)
      linarith
    · norm_num
  have ha1_pos : 0 < t_tree + (2 * (4 : ℝ)) / bringSurfaceArea := by
    apply add_pos
    · dsimp only [t_tree, q]
      exact mul_pos (mul_pos (by norm_num) (hqbal_pos 9 (by omega))) (hqbal_pos 10 (by omega))
    · unfold bringSurfaceArea bringFundamentalTriangleArea
      apply div_pos (by norm_num)
      linarith
  obtain ⟨α, ⟨hα_pos, hα_root⟩, _⟩ :=
    exists_unique_pos_cubic_root 0 (habiroNorm q) (t_tree + (2 * (4 : ℝ)) / bringSurfaceArea)
      (le_refl 0) hhab_nonneg ha1_pos
  refine ⟨q, delta_B3, α, ?_⟩
  refine
    { one_lt_q := by dsimp only [q]; norm_num
      delta_B3_nonneg := hdelta_nonneg
      alpha_pos := hα_pos
      two_loop_self_consistent := ?_ }
  rw [twoLoopBringFixedPoint_iff_cubic _ _ _ _ _ α (ne_of_gt hα_pos)]
  unfold twoLoopBringCubic
  rw [hc3_zero]
  exact hα_root

end ConditionalTwoLoopBridge

end AlphaEmTwoLoopBlochSchwinger
end QOU.Archimedean
