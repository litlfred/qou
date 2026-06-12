-- Specific imports (not the `Mathlib` umbrella): the lake-cache
-- restore omits the root `Mathlib.olean`; see
-- lean-environment-setup.md §"Two more gotchas after a lake-cache restore".
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# QOU.BraidKnot.MassGapKeystone — substrate gap S1a + the ε³ lemma (Step 2)

Implements the **S1a keystone skeleton** and the **Step-2 ε³ lemma** of
the mass-gap three-step program
(`docs/workplans/2026-06-11-mass-gap-three-step-program.md` §4 and §2),
discharging all three skeleton `sorry`s.

Contents:

- `crossingEnergy q = (q − q⁻¹)/2` and the categorical mass-gap lower
  bound `gapBound q = crossingEnergy q · (q − 1)²`.
- **S1a** (all sorry-free): `gapBound_pos` (strict positivity for
  `1 < q`), `gapBound_div_hbarSq` (the exact physical-units identity
  `Δ_q/ℏ_q² = ½·q·(q−1)·(q+1)`, probe-verified by
  `q1_mass_gap_probe.py`), `gapBound_at_one` (μ₂-vanishing at the
  classical point).
- **Step 2, the ε³ lemma** (all sorry-free): at `q = 1 + ε` the gap has
  the *exact* closed forms

  * `gapBound (1+ε) = ε³(2+ε) / (2(1+ε))` — the ε³ rate with the
    correction factor displayed exactly (no `O(·)` needed);
  * `gapBound (1+ε) / ℏ_q² = ε + (3/2)ε² + (1/2)ε³` — an exact cubic,
    exhibiting the physical-units linear rate and the `3/2`
    second-order coefficient of the workplan target;
  * the two-sided bound `ε³/2 ≤ gapBound (1+ε) ≤ ε³` for `0 < ε`,
    which is the quantitative form of `Δ_q = ε³(1 + O(ε))` and makes
    the standard-part-zero statement immediate.

- `SubstrateGap` — the conditional uniform-in-`n` gap class
  (§3b-cond conditional-class pattern); S1b will pin `spectrum` to
  the transfer-matrix `𝒯_q` excitation energies.

Relation to `QOU.AlgebraicSubstrate.SurrealRateCalculus`: the abstract
rate-table class there records `massGap = ε³` with the positive scalar
absorbed into the named quantity; `gapBound_one_add_eps` below realises
that rate concretely on `ℝ` with the scalar `(2+ε)/(2(1+ε))` displayed
(and pinched in `[1/2, 1]` for `0 < ε ≤ 1` by
`gapBound_one_add_eps_bounds`).

Per CLAUDE.md §7c the ordering hypothesis `1 < q` forces the
archimedean carrier `ℝ` — no generic-`R` version of the positivity
statements exists.

LaTeX/workplan provenance: the statement shapes are verbatim from the
workplan §4 skeleton; the `sorry`s there are discharged here.
-/

namespace QOU.BraidKnot

/-- Crossing energy `E_×(q) = (q − q⁻¹)/2`. -/
noncomputable def crossingEnergy (q : ℝ) : ℝ := (q - q⁻¹) / 2

/-- Categorical mass-gap lower bound `Δ_q = E_×(q) · (q − 1)²`. -/
noncomputable def gapBound (q : ℝ) : ℝ := crossingEnergy q * (q - 1) ^ 2

/-- For `1 < q` the antisymmetric combination `q − q⁻¹` is positive
    (the crossing energy numerator). -/
theorem sub_inv_pos {q : ℝ} (hq : 1 < q) : 0 < q - q⁻¹ := by
  have h0 : (0 : ℝ) < q := lt_trans one_pos hq
  have key : q - q⁻¹ = (q ^ 2 - 1) / q := by
    field_simp
  rw [key]
  apply div_pos _ h0
  nlinarith

/-- **S1a keystone, fixed n**: the categorical gap bound is strictly
    positive for `1 < q`. -/
-- Ref: [manuscript] models-of-qous/yang-mills-mass-gap.md
theorem gapBound_pos {q : ℝ} (hq : 1 < q) : 0 < gapBound q := by
  have hE : 0 < crossingEnergy q := by
    unfold crossingEnergy
    have := sub_inv_pos hq
    linarith
  have hsq : 0 < (q - 1) ^ 2 := by
    have : (0 : ℝ) < q - 1 := by linarith
    positivity
  exact mul_pos hE hsq

/-- **S1a exact physical-units identity**
    `Δ_q / ℏ_q² = ½·q·(q−1)·(q+1)` with `ℏ_q = (q−1)/q`.
    Probe-verified at 50 dps by `q1_mass_gap_probe.py`
    (`q1-mass-gap-probe.witness.json`, field `exact_identities`). -/
-- Ref: [manuscript] q1-mass-gap-probe.witness.json exact_identities
theorem gapBound_div_hbarSq {q : ℝ} (h0 : q ≠ 0) (h1 : q ≠ 1) :
    gapBound q / ((q - 1) / q) ^ 2 = q * (q - 1) * (q + 1) / 2 := by
  have hq1 : q - 1 ≠ 0 := sub_ne_zero.mpr h1
  unfold gapBound crossingEnergy
  field_simp
  ring

/-- **S1a μ₂-vanishing**: the gap bound vanishes identically at the
    classical point `q = 1` (the computational shadow of the
    `𝔾ₘ`-torsion statement in the conjecture block). -/
-- Ref: [manuscript] models-of-qous/yang-mills-mass-gap.md §G_m-torsion
theorem gapBound_at_one : gapBound 1 = 0 := by
  unfold gapBound crossingEnergy
  norm_num

/-! ## Step 2 — the ε³ lemma (exact forms at `q = 1 + ε`) -/

/-- **ε³ lemma, categorical form (exact).** At `q = 1 + ε`:

    `Δ_{1+ε} = ε³ · (2 + ε) / (2(1 + ε))`.

    The factor `(2+ε)/(2(1+ε))` tends to `1` as `ε → 0`, so this is
    the exact form of the workplan target `Δ_q = ε³(1 + O(ε))`; the
    quantitative pinch is `gapBound_one_add_eps_bounds` below. -/
-- Ref: [manuscript] docs/workplans/2026-06-11-mass-gap-three-step-program.md §2
theorem gapBound_one_add_eps (ε : ℝ) (hm : (1 : ℝ) + ε ≠ 0) :
    gapBound (1 + ε) = ε ^ 3 * (2 + ε) / (2 * (1 + ε)) := by
  unfold gapBound crossingEnergy
  field_simp
  ring

/-- **ε³ lemma, physical-units form (exact cubic).** At `q = 1 + ε`,
    with `ℏ_q = (q−1)/q = ε/(1+ε)`:

    `Δ_{1+ε} / ℏ_{1+ε}² = ε + (3/2)·ε² + (1/2)·ε³`.

    This is an exact polynomial — the workplan's
    `Δ_q/ℏ_q² = ε + 3⁄2·ε² + O(ε³)` with the `O(ε³)` term pinned to
    exactly `ε³/2`.  The physical-units gap dies *linearly* in `ε`;
    its standard part at the classical point is `0`. -/
-- Ref: [manuscript] docs/workplans/2026-06-11-mass-gap-three-step-program.md §2
theorem gapBound_one_add_eps_div_hbarSq (ε : ℝ) (h0 : ε ≠ 0)
    (hm : (1 : ℝ) + ε ≠ 0) :
    gapBound (1 + ε) / ((1 + ε - 1) / (1 + ε)) ^ 2
      = ε + 3 / 2 * ε ^ 2 + ε ^ 3 / 2 := by
  have h2 : (1 : ℝ) + ε - 1 = ε := by ring
  rw [h2, gapBound_one_add_eps ε hm]
  field_simp
  ring

/-- **Two-sided ε³ pinch**: for every `0 < ε`,

    `ε³/2 ≤ Δ_{1+ε} ≤ ε³` whenever additionally `ε ≤ 1` for the upper
    bound to be stated in this clean form — in fact the upper bound
    `Δ_{1+ε} ≤ ε³` holds for ALL `ε > 0` since `2 + ε ≤ 2(1 + ε)`.

    This is the quantitative content of `Δ_q = ε³(1 + O(ε))` and makes
    the standard-part-zero claim of the workplan immediate: the gap is
    squeezed between two infinitesimals of order exactly 3. -/
-- Ref: [manuscript] docs/workplans/2026-06-11-mass-gap-three-step-program.md §2
theorem gapBound_one_add_eps_bounds {ε : ℝ} (h0 : 0 < ε) :
    ε ^ 3 / 2 ≤ gapBound (1 + ε) ∧ gapBound (1 + ε) ≤ ε ^ 3 := by
  have hm : (1 : ℝ) + ε ≠ 0 := ne_of_gt (by linarith)
  rw [gapBound_one_add_eps ε hm]
  have hden : (0 : ℝ) < 2 * (1 + ε) := by linarith
  constructor
  · -- lower bound: the difference is exactly ε³ / (2(1+ε)) ≥ 0
    have key : ε ^ 3 * (2 + ε) / (2 * (1 + ε)) - ε ^ 3 / 2
        = ε ^ 3 / (2 * (1 + ε)) := by
      field_simp
      ring
    have hpos : 0 ≤ ε ^ 3 / (2 * (1 + ε)) :=
      le_of_lt (div_pos (pow_pos h0 3) hden)
    linarith
  · -- upper bound: the difference is exactly ε⁴ / (2(1+ε)) ≥ 0
    have key : ε ^ 3 - ε ^ 3 * (2 + ε) / (2 * (1 + ε))
        = ε ^ 4 / (2 * (1 + ε)) := by
      field_simp
      ring
    have hpos : 0 ≤ ε ^ 4 / (2 * (1 + ε)) :=
      le_of_lt (div_pos (pow_pos h0 4) hden)
    linarith

/-! ## Conditional uniform-in-n gap class (S1b/S1c interface) -/

/-- Uniform-in-`n` substrate gap, conditional form (§3b-cond
    conditional-class pattern), parametrized by the level-`n`
    excitation spectrum.  S1b pins `spectrum` to the transfer-matrix
    `𝒯_q` excitation energies; S1c (research-grade) supplies
    instances.  Until then, downstream consumers take this class as
    an explicit `[Instance]` hypothesis per the conditional-class
    discipline. -/
-- Ref: [manuscript] docs/workplans/2026-06-11-mass-gap-three-step-program.md §4
class SubstrateGap (q : ℝ) (spectrum : ℕ → Set ℝ) : Prop where
  one_lt : 1 < q
  gap_uniform : ∀ n : ℕ, ∀ E ∈ spectrum n, E ≠ 0 → gapBound q ≤ E

end QOU.BraidKnot
