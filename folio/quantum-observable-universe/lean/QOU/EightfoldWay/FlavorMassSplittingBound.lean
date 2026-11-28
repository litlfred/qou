import QOU.Core.Basic
import QOU.EightfoldWay.FlavorDressingFunctor
import QOU.EightfoldWay.DressedMassFromSubstrateSplit

/-!
# QOU.FlavorDressing.flavor_mass_splitting_bound

Two-sided substrate bound on the down–up dressed-quark splitting:

```
0 < μ_d − μ_u ≤ M_N · ℏ_q² · h_q · [2]_q / 3 < M_N · ℏ_q² · h_q · [2]_q
```

with ℏ_q = (q − 1)/q, h_q = q − q⁻¹, [2]_q = q + q⁻¹.

The lower bound is positivity; the upper bound follows from the
algebraic identity

```
(q − 1)²(1 − q⁻⁴)/3 = (1/3) · ℏ_q² · h_q · [2]_q
```

at non-zero `q` (no spurious `q²` factor — see direct expansion
in the lemma `substrate_to_bound_ratio` below).

LaTeX: `\label{thm:flavor-mass-splitting-bound}`
-/

namespace QOU.FlavorDressing

open Flavor

/-- The substrate ratio `(q − 1)²(1 − q⁻⁴)/3` over the bound
    factor `ℏ_q² · h_q · [2]_q` equals exactly `1/3` for any
    non-zero `q`.  This algebraic identity is the engine of the
    upper bound; stated over a generic `Field R` per the
    repository's base-ring convention (AGENTS.md §7c) — the
    identity is a rational-function fact with no archimedean
    content.  The downstream inequality `flavor_mass_splitting_bound`
    keeps its `ℝ` specialisation because it uses ordering.

    The hypothesis `(3 : R) ≠ 0` rules out characteristic 3, where
    `1/3` itself is undefined; in `ℝ`, `ℚ`, or any char-0 field this
    is automatic. -/
-- Ref: [leitner2026] braids-and-knots/flavor-mass-splitting-bound
theorem substrate_to_bound_ratio {R : Type*} [Field R]
    (q : R) (hq : q ≠ 0) (hq4 : q^4 ≠ 1) (h3 : (3 : R) ≠ 0) :
    ((q - 1)^2 * (1 - q^(-4 : ℤ)) / 3)
    / (((q - 1)/q)^2 * (q - q⁻¹) * (q + q⁻¹))
      = 1 / 3 := by
  -- Derive the auxiliary nonzero facts.  In a field, `(q^4 - 1) ≠ 0`
  -- factors as `(q - 1)(q + 1)(q^2 + 1) ≠ 0`, so each factor is nonzero.
  have hq4_sub : q^4 - 1 ≠ 0 := sub_ne_zero.mpr hq4
  have hq2 : q^2 ≠ 0 := pow_ne_zero _ hq
  have hq4_pow : q^4 ≠ 0 := pow_ne_zero _ hq
  have hqsub1 : q - 1 ≠ 0 := by
    intro h
    apply hq4
    have hq1 : q = 1 := by linear_combination h
    rw [hq1]; norm_num
  have hq2_sub : q^2 - 1 ≠ 0 := by
    intro h
    apply hq4_sub
    have : q^4 - 1 = (q^2 - 1) * (q^2 + 1) := by ring
    rw [this, h, zero_mul]
  have hq2_add : q^2 + 1 ≠ 0 := by
    intro h
    apply hq4_sub
    have : q^4 - 1 = (q^2 - 1) * (q^2 + 1) := by ring
    rw [this, h, mul_zero]
  -- Replace the negative integer power by `(q^4)⁻¹` so `field_simp`
  -- can handle everything.
  have h_neg4 : (q : R)^(-4 : ℤ) = (q^4)⁻¹ := by
    rw [show (-4 : ℤ) = -((4 : ℕ) : ℤ) from rfl, zpow_neg, zpow_natCast]
  rw [h_neg4]
  -- (q - q⁻¹) = (q^2 - 1)/q  and  (q + q⁻¹) = (q^2 + 1)/q;  rewriting
  -- these makes the denominator a clean rational expression.
  have h_qm : q - q⁻¹ = (q^2 - 1) / q := by field_simp
  have h_qp : q + q⁻¹ = (q^2 + 1) / q := by field_simp
  rw [h_qm, h_qp]
  field_simp
  ring

/-! ### Positivity and inequality helpers (at `q > 1`) -/

/-- At `q > 1`, the substrate split factor is strictly positive. -/
-- Ref: [leitner2026] braids-and-knots/flavor-mass-splitting-bound
private lemma aether_split_factor_pos {q : ℝ} (hq : 1 < q) :
    0 < aether_split_factor q := by
  have hq0 : 0 < q := by linarith
  have hq_ne : q ≠ 0 := ne_of_gt hq0
  have hq_inv_pos : 0 < q⁻¹ := inv_pos.mpr hq0
  have hsub_q1 : 0 < q - 1 := by linarith
  have hq4_pos : 0 < q ^ 4 := pow_pos hq0 4
  have hq4_gt_1 : 1 < q ^ 4 := by nlinarith [sq_nonneg (q - 1), sq_nonneg (q + 1)]
  have h_one_sub_q4_inv : 0 < 1 - q ^ (-4 : ℤ) := by
    have h_pow : (q : ℝ) ^ (-4 : ℤ) = (q ^ 4)⁻¹ := by
      rw [show (-4 : ℤ) = -((4 : ℕ) : ℤ) from rfl, zpow_neg, zpow_natCast]
    rw [h_pow]
    have : (q ^ 4 : ℝ)⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq4_gt_1
    linarith
  unfold aether_split_factor
  apply mul_pos
  · apply div_pos (mul_pos (pow_pos hsub_q1 2) h_one_sub_q4_inv) (by norm_num)
  · positivity

@[deprecated (since := "2026-11-27")] alias substrate_split_factor_pos := aether_split_factor_pos

/-- The convention-D Skein factor `q(q² + 1)/(q⁴ + 1)` is at most `1` for
    `q > 0`, since `q⁴ + 1 − q(q² + 1) = (q − 1)(q³ − 1) ≥ 0`. -/
private lemma skeinD_factor_le_one {q : ℝ} (hq : 0 < q) :
    q * (q ^ 2 + 1) / (q ^ 4 + 1) ≤ 1 := by
  rw [div_le_one (by positivity)]
  nlinarith [mul_nonneg (sq_nonneg (q - 1)) (add_nonneg (add_nonneg (sq_nonneg q) hq.le) zero_le_one)]

/-- **Substrate bound on the dressed-quark splitting.**
    For substrate parameter `q > 1`, nucleon average mass `M_N > 0`,
    and any `FlavorDressingFunctor F` satisfying the derivation
    identity of `prop:flavor-dressed-mass-from-aether-split`,
    the down–up splitting satisfies the two-sided substrate bound

      0 < μ_d − μ_u < M_N · ℏ_q² · h_q · [2]_q

    where ℏ_q = (q − 1)/q, h_q = q − q⁻¹, [2]_q = q + q⁻¹.

    The strict lower bound expresses positivity of the substrate
    factor at q > 1; the strict upper bound uses the algebraic
    identity `substrate_to_bound_ratio` plus the convention-D Skein
    factor `q(q² + 1)/(q⁴ + 1) ≤ 1` (owner ruling 2026-11-27), which
    gives the sharper bound `≤ M_N · ℏ_q² · h_q · [2]_q / 3`.

    This form takes the splitting identity as a plain hypothesis
    `h_derive`; `flavor_mass_splitting_bound` below is the form
    conditional on `conj:flavor-split-aether-mass`. -/
-- Ref: [leitner2026] braids-and-knots/flavor-mass-splitting-bound
theorem flavor_mass_splitting_bound_of_split
    (F : FlavorDressingFunctor) (M_N q : ℝ)
    (hM : 0 < M_N) (hq : 1 < q)
    (h_derive :
      F.μ Flavor.down - F.μ Flavor.up
        = M_N * aether_split_factor q) :
    0 < F.μ Flavor.down - F.μ Flavor.up ∧
    F.μ Flavor.down - F.μ Flavor.up
      ≤ M_N * (((q - 1)/q)^2 * (q - q⁻¹) * (q + q⁻¹)) / 3 ∧
    F.μ Flavor.down - F.μ Flavor.up
      < M_N * (((q - 1)/q)^2 * (q - q⁻¹) * (q + q⁻¹)) := by
  have hq0 : 0 < q := by linarith
  have hq_ne : q ≠ 0 := ne_of_gt hq0
  have hq_inv_pos : 0 < q⁻¹ := inv_pos.mpr hq0
  have h_qpqinv_pos : 0 < q + q⁻¹ := by linarith
  have h_qmqinv_pos : 0 < q - q⁻¹ := by
    have : q - q⁻¹ = (q ^ 2 - 1) / q := by field_simp
    rw [this]
    apply div_pos _ hq0
    nlinarith
  have h_sub_div_sq_pos : 0 < ((q - 1) / q) ^ 2 := pow_pos (div_pos (show (0:ℝ) < q - 1 by linarith) hq0) 2
  have hq4_pos : 0 < q ^ 4 := pow_pos hq0 4
  have hq4_gt_1 : 1 < q ^ 4 := by nlinarith [sq_nonneg (q - 1), sq_nonneg (q + 1)]
  have hq4_ne : q ^ 4 ≠ 1 := ne_of_gt hq4_gt_1
  -- Apply `substrate_to_bound_ratio` at `R := ℝ`.
  have h_ratio :
      ((q - 1) ^ 2 * (1 - q ^ (-4 : ℤ)) / 3)
        / (((q - 1) / q) ^ 2 * (q - q⁻¹) * (q + q⁻¹)) = (1 / 3 : ℝ) :=
    substrate_to_bound_ratio q hq_ne hq4_ne (by norm_num)
  have hdenom_ne :
      ((q - 1) / q) ^ 2 * (q - q⁻¹) * (q + q⁻¹) ≠ 0 :=
    ne_of_gt (mul_pos (mul_pos h_sub_div_sq_pos h_qmqinv_pos) h_qpqinv_pos)
  -- Cross-multiply to obtain the closed form of the (q-1)²(1-q⁻⁴)/3 piece.
  have h_numerator_form :
      (q - 1) ^ 2 * (1 - q ^ (-4 : ℤ)) / 3
        = ((q - 1) / q) ^ 2 * (q - q⁻¹) * (q + q⁻¹) / 3 := by
    have := h_ratio
    rw [div_eq_iff hdenom_ne] at this
    linarith
  -- aether_split_factor q = B/3 · r,  with  B = ((q-1)/q)² · (q-q⁻¹) · (q+q⁻¹)
  -- and the convention-D Skein factor  r = q(q²+1)/(q⁴+1) ∈ (0, 1].
  set B := ((q - 1) / q) ^ 2 * (q - q⁻¹) * (q + q⁻¹) with hBdef
  have hB_pos : 0 < B := mul_pos (mul_pos h_sub_div_sq_pos h_qmqinv_pos) h_qpqinv_pos
  have h_factor_form :
      aether_split_factor q = B / 3 * (q * (q ^ 2 + 1) / (q ^ 4 + 1)) := by
    unfold aether_split_factor
    rw [h_numerator_form]
  have h_r_le : q * (q ^ 2 + 1) / (q ^ 4 + 1) ≤ 1 := skeinD_factor_le_one hq0
  have h_factor_le : aether_split_factor q ≤ B / 3 := by
    rw [h_factor_form]
    have : 0 < B / 3 := by positivity
    nlinarith
  refine ⟨?_, ?_, ?_⟩
  · rw [h_derive]
    exact mul_pos hM (aether_split_factor_pos hq)
  · rw [h_derive, mul_div_assoc]
    exact mul_le_mul_of_nonneg_left h_factor_le hM.le
  · rw [h_derive]
    apply mul_lt_mul_of_pos_left _ hM
    linarith

/-- **Substrate bound on the dressed-quark splitting, conditional on
    `conj:flavor-split-aether-mass`** (§3b-cond). With
    `M_N = (m_p + m_n)/2`, the conjecture `[FlavorSplitSubstrateMass m_p m_n q]`
    and the nucleon form of the pair Skein mass formula give

      0 < μ_d − μ_u ≤ M_N · ℏ_q² · h_q · [2]_q / 3 < M_N · ℏ_q² · h_q · [2]_q.

    The splitting identity is derived by `dressed_mass_from_substrate_split`
    and then bounded by `flavor_mass_splitting_bound_of_split`. -/
-- Ref: [leitner2026] braids-and-knots/flavor-mass-splitting-bound
theorem flavor_mass_splitting_bound
    (F : FlavorDressingFunctor) (m_p m_n q : ℝ)
    [h : FlavorSplitSubstrateMass m_p m_n q]
    (h_skein : PairSkeinNucleonSplit F m_p m_n q) :
    0 < F.μ Flavor.down - F.μ Flavor.up ∧
    F.μ Flavor.down - F.μ Flavor.up
      ≤ (m_p + m_n) / 2 * (((q - 1)/q)^2 * (q - q⁻¹) * (q + q⁻¹)) / 3 ∧
    F.μ Flavor.down - F.μ Flavor.up
      < (m_p + m_n) / 2 * (((q - 1)/q)^2 * (q - q⁻¹) * (q + q⁻¹)) :=
  flavor_mass_splitting_bound_of_split F ((m_p + m_n) / 2) q h.M_N_pos h.q_gt_one
    (dressed_mass_from_substrate_split F m_p m_n q h_skein).1

end QOU.FlavorDressing
