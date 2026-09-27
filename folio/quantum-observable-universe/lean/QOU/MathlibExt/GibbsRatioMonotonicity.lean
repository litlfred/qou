import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.Field.Basic

/-!
# Damped-sum ratios: an exact criterion bounding the A-growth of a Gibbs family

**Analytic infrastructure for per-block-weight exclusions.**

A recurring shape in the Δ_λ binding programme is a ratio of two exponentially
damped finite sums,

  `Z a C τ = ∑ i, a i * exp (-(C i) * τ)` ,   `R τ = Z b D τ / Z a C τ` ,

with `a i ≥ 0` per-partition amplitudes and `C i` content-Casimir "energies".
The physical question — *can any damping time `τ` reproduce an observed A-growth
ratio?* — is a question about the **range** of `R` on `[0, ∞)`, so answering it
excludes a whole one-parameter family rather than a single point.

The main result is an exact, calculus-free criterion (`ratio_le_initial_iff`):

  `R τ ≤ R 0`  ↔  `∑ᵢ ∑ⱼ aᵢ bⱼ e^{-Dⱼτ} ≤ ∑ᵢ ∑ⱼ aᵢ bⱼ e^{-Cᵢτ}` ,

i.e. damping shrinks the growth ratio exactly when the *cross-weighted*
denominator energies beat the numerator ones. `ratio_le_initial_of_energies_le`
gives the clean sufficient condition `∀ i j, C i ≤ D j`, and
`target_unreachable_of_gt_initial` packages the exclusion: a target strictly
above the undamped value `R 0` is then unreachable for **every** `τ ≥ 0`.

This is the general form of the GAP-6 (bean `qou-bcig`) numerical finding, where
the undamped supremum `3.658` fell short of the `12.72` A-growth target, so no
damping time — canonical or fitted — could work.

**Two sufficient conditions, and which one applies.** The termwise test
`∀ i j, C i ≤ D j` (`crossSum_le_of_energies_le`) is **false for the Δ_λ data**
(`C_max(D) = 75.4 > C_min(⁴He) = 20.3` — the energy ranges overlap), and so is
the Jensen relaxation `min D ≥ E_r[C]` (`20.28 < 23.11`). The usable hypothesis
is a **coupling** (`crossSum_le_of_coupling`): a non-negative matrix with the
prescribed marginals, supported on pairs with `C i ≤ D j`. Such a coupling
exists exactly when the numerator's energy distribution first-order
stochastically dominates the denominator's — a finite CDF check, which for the
Δ_λ data **holds** (0 violations across all 43 thresholds).

So the GAP-6 family exclusion is proved here *modulo exhibiting that coupling*:
`target_unreachable_of_coupling` is the closed chain, and the remaining input is
a finite combinatorial certificate rather than an analytic gap.

Base ring: archimedean (`Real.exp`, ordering) ⇒ `ℝ`, the correct §7c placement.
-/

namespace QOU.MathlibExt.GibbsRatioMonotonicity

open Finset Real

variable {ι κ : Type*} [Fintype ι] [Fintype κ]

/-- The damped (Gibbs / partition-function) sum `Z(τ) = ∑ aᵢ e^{-Cᵢ τ}`. -/
noncomputable def Z (a C : ι → ℝ) (τ : ℝ) : ℝ :=
  ∑ i, a i * Real.exp (-(C i) * τ)

/-- At `τ = 0` the damping is trivial and `Z` is the plain amplitude sum. -/
theorem Z_zero (a C : ι → ℝ) : Z a C 0 = ∑ i, a i := by
  simp [Z]

/-- A Gibbs sum with non-negative amplitudes, at least one positive, is
positive — the standing non-degeneracy hypothesis. -/
theorem Z_pos {a C : ι → ℝ} (ha : ∀ i, 0 ≤ a i) {j : ι} (hj : 0 < a j) (τ : ℝ) :
    0 < Z a C τ := by
  refine Finset.sum_pos' (fun i _ => ?_) ⟨j, Finset.mem_univ j, ?_⟩
  · exact mul_nonneg (ha i) (Real.exp_pos _).le
  · exact mul_pos hj (Real.exp_pos _)

/-- **The exact criterion.** The damped ratio drops below its undamped value
exactly when the cross-weighted denominator energies dominate:
`R τ ≤ R 0 ↔ ∑ᵢⱼ aᵢbⱼ e^{-Dⱼτ} ≤ ∑ᵢⱼ aᵢbⱼ e^{-Cᵢτ}`. Calculus-free. -/
theorem ratio_le_initial_iff {a C : ι → ℝ} {b D : κ → ℝ}
    (ha : ∀ i, 0 ≤ a i) {i₀ : ι} (hi₀ : 0 < a i₀) (τ : ℝ) :
    Z b D τ / Z a C τ ≤ Z b D 0 / Z a C 0 ↔
      (∑ i, ∑ j, a i * b j * Real.exp (-(D j) * τ))
        ≤ ∑ i, ∑ j, a i * b j * Real.exp (-(C i) * τ) := by
  have hτ := Z_pos ha hi₀ (C := C) τ
  have h0 := Z_pos ha hi₀ (C := C) 0
  rw [div_le_div_iff₀ hτ h0]
  have hL : Z b D τ * Z a C 0 = ∑ i, ∑ j, a i * b j * Real.exp (-(D j) * τ) := by
    simp only [Z, mul_zero, Real.exp_zero, mul_one]
    rw [Finset.sum_mul_sum, Finset.sum_comm]
    exact Finset.sum_congr rfl (fun i _ => Finset.sum_congr rfl (fun j _ => by ring))
  have hR : Z b D 0 * Z a C τ = ∑ i, ∑ j, a i * b j * Real.exp (-(C i) * τ) := by
    simp only [Z, mul_zero, Real.exp_zero, mul_one]
    rw [Finset.sum_mul_sum, Finset.sum_comm]
    exact Finset.sum_congr rfl (fun i _ => Finset.sum_congr rfl (fun j _ => by ring))
  rw [hL, hR]

/-- **Sufficient condition, termwise.** If every denominator energy is at most
every numerator energy, then for `τ ≥ 0` the criterion holds termwise. -/
theorem crossSum_le_of_energies_le {a C : ι → ℝ} {b D : κ → ℝ}
    (ha : ∀ i, 0 ≤ a i) (hb : ∀ j, 0 ≤ b j)
    (hCD : ∀ i j, C i ≤ D j) {τ : ℝ} (hτ : 0 ≤ τ) :
    (∑ i, ∑ j, a i * b j * Real.exp (-(D j) * τ))
      ≤ ∑ i, ∑ j, a i * b j * Real.exp (-(C i) * τ) := by
  refine Finset.sum_le_sum (fun i _ => Finset.sum_le_sum (fun j _ => ?_))
  refine mul_le_mul_of_nonneg_left ?_ (mul_nonneg (ha i) (hb j))
  refine Real.exp_le_exp.mpr ?_
  have : (-(D j)) * τ ≤ (-(C i)) * τ :=
    mul_le_mul_of_nonneg_right (neg_le_neg (hCD i j)) hτ
  exact this

/-- **Sufficient condition via a coupling (the usable one).** The termwise test
`∀ i j, C i ≤ D j` is far too strong — it fails whenever the two energy ranges
overlap, as they do for the Δ_λ data. The right hypothesis is a **coupling**:
a non-negative matrix `M` with the prescribed row/column marginals, supported
only on pairs where `C i ≤ D j`. Then the comparison holds termwise *along the
coupling* rather than for all pairs.

By the standard characterisation, such a coupling exists exactly when the
numerator's energy distribution **first-order stochastically dominates** the
denominator's — a finite, checkable condition on the two CDFs. For the Δ_λ data
it **holds** (0 violations across all 43 thresholds), which is what makes this
the applicable route where `crossSum_le_of_energies_le` is not. -/
theorem crossSum_le_of_coupling {a C : ι → ℝ} {b D : κ → ℝ} (M : ι → κ → ℝ)
    (hM : ∀ i j, 0 ≤ M i j)
    (hrow : ∀ i, ∑ j, M i j = a i * (∑ j, b j))
    (hcol : ∀ j, ∑ i, M i j = b j * (∑ i, a i))
    (hdom : ∀ i j, 0 < M i j → C i ≤ D j) {τ : ℝ} (hτ : 0 ≤ τ) :
    (∑ i, ∑ j, a i * b j * Real.exp (-(D j) * τ))
      ≤ ∑ i, ∑ j, a i * b j * Real.exp (-(C i) * τ) := by
  -- along the coupling the comparison is termwise
  have key : (∑ i, ∑ j, M i j * Real.exp (-(D j) * τ))
      ≤ ∑ i, ∑ j, M i j * Real.exp (-(C i) * τ) := by
    refine Finset.sum_le_sum (fun i _ => Finset.sum_le_sum (fun j _ => ?_))
    rcases eq_or_lt_of_le (hM i j) with h | h
    · simp [← h]
    · refine mul_le_mul_of_nonneg_left (Real.exp_le_exp.mpr ?_) h.le
      exact mul_le_mul_of_nonneg_right (neg_le_neg (hdom i j h)) hτ
  -- both sides of `key` and of the goal collapse to the same product form
  have hML : (∑ i, ∑ j, M i j * Real.exp (-(D j) * τ))
      = (∑ i, a i) * ∑ j, b j * Real.exp (-(D j) * τ) := by
    rw [Finset.sum_comm, Finset.mul_sum]
    refine Finset.sum_congr rfl (fun j _ => ?_)
    rw [← Finset.sum_mul, hcol j]
    ring
  have hMR : (∑ i, ∑ j, M i j * Real.exp (-(C i) * τ))
      = (∑ j, b j) * ∑ i, a i * Real.exp (-(C i) * τ) := by
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl (fun i _ => ?_)
    rw [← Finset.sum_mul, hrow i]
    ring
  have hGL : (∑ i, ∑ j, a i * b j * Real.exp (-(D j) * τ))
      = (∑ i, a i) * ∑ j, b j * Real.exp (-(D j) * τ) := by
    rw [Finset.sum_mul_sum]
    exact Finset.sum_congr rfl (fun i _ => Finset.sum_congr rfl (fun j _ => by ring))
  have hGR : (∑ i, ∑ j, a i * b j * Real.exp (-(C i) * τ))
      = (∑ j, b j) * ∑ i, a i * Real.exp (-(C i) * τ) := by
    rw [Finset.sum_mul_sum, Finset.sum_comm]
    exact Finset.sum_congr rfl (fun i _ => Finset.sum_congr rfl (fun j _ => by ring))
  rw [hML, hMR] at key
  rw [hGL, hGR]
  exact key

/-- **Damping cannot raise the growth ratio** when a dominating coupling exists.
The applicable form of the exclusion for overlapping energy ranges. -/
theorem ratio_le_initial_of_coupling {a C : ι → ℝ} {b D : κ → ℝ}
    (ha : ∀ i, 0 ≤ a i) {i₀ : ι} (hi₀ : 0 < a i₀) (M : ι → κ → ℝ)
    (hM : ∀ i j, 0 ≤ M i j)
    (hrow : ∀ i, ∑ j, M i j = a i * (∑ j, b j))
    (hcol : ∀ j, ∑ i, M i j = b j * (∑ i, a i))
    (hdom : ∀ i j, 0 < M i j → C i ≤ D j) {τ : ℝ} (hτ : 0 ≤ τ) :
    Z b D τ / Z a C τ ≤ Z b D 0 / Z a C 0 :=
  (ratio_le_initial_iff ha hi₀ τ).mpr
    (crossSum_le_of_coupling M hM hrow hcol hdom hτ)

/-- **The exclusion, in its applicable form.** Given a dominating coupling, a
growth target strictly above the undamped value `R 0` is unreachable by every
`τ ≥ 0`. This is the statement that closes the GAP-6 family exclusion modulo the
finite CDF check that produces the coupling. -/
theorem target_unreachable_of_coupling {a C : ι → ℝ} {b D : κ → ℝ}
    (ha : ∀ i, 0 ≤ a i) {i₀ : ι} (hi₀ : 0 < a i₀) (M : ι → κ → ℝ)
    (hM : ∀ i j, 0 ≤ M i j)
    (hrow : ∀ i, ∑ j, M i j = a i * (∑ j, b j))
    (hcol : ∀ j, ∑ i, M i j = b j * (∑ i, a i))
    (hdom : ∀ i j, 0 < M i j → C i ≤ D j) {target : ℝ}
    (htarget : Z b D 0 / Z a C 0 < target) :
    ∀ τ : ℝ, 0 ≤ τ → Z b D τ / Z a C τ < target :=
  fun _ hτ =>
    lt_of_le_of_lt (ratio_le_initial_of_coupling ha hi₀ M hM hrow hcol hdom hτ) htarget

/-- **Damping cannot raise the growth ratio** when the energy ranges separate:
`R τ ≤ R 0` for every `τ ≥ 0`. -/
theorem ratio_le_initial_of_energies_le {a C : ι → ℝ} {b D : κ → ℝ}
    (ha : ∀ i, 0 ≤ a i) (hb : ∀ j, 0 ≤ b j) {i₀ : ι} (hi₀ : 0 < a i₀)
    (hCD : ∀ i j, C i ≤ D j) {τ : ℝ} (hτ : 0 ≤ τ) :
    Z b D τ / Z a C τ ≤ Z b D 0 / Z a C 0 :=
  (ratio_le_initial_iff ha hi₀ τ).mpr (crossSum_le_of_energies_le ha hb hCD hτ)

/-- **The exclusion.** A growth target strictly above the undamped value `R 0`
is unreachable by *every* damping time `τ ≥ 0` — canonical or fitted. This is
the shape of a one-parameter-family exclusion: it forecloses tuning `τ` as a
fit escape, rather than merely reporting that one particular `τ` missed. -/
theorem target_unreachable_of_gt_initial {a C : ι → ℝ} {b D : κ → ℝ}
    (ha : ∀ i, 0 ≤ a i) (hb : ∀ j, 0 ≤ b j) {i₀ : ι} (hi₀ : 0 < a i₀)
    (hCD : ∀ i j, C i ≤ D j) {target : ℝ}
    (htarget : Z b D 0 / Z a C 0 < target) :
    ∀ τ : ℝ, 0 ≤ τ → Z b D τ / Z a C τ < target :=
  fun _ hτ =>
    lt_of_le_of_lt (ratio_le_initial_of_energies_le ha hb hi₀ hCD hτ) htarget

end QOU.MathlibExt.GibbsRatioMonotonicity
