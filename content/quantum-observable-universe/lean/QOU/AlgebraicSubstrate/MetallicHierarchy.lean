import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic

/-!
# Metallic-ratio hierarchy of the Hecke scalar

The Iwahori–Hecke generator satisfies `σ² = (q − q⁻¹)·σ + 1`, so the
structural scalar of the braiding is `q − q⁻¹`.  This file proves the
owner's assertion (2026-06-08): the real values `q > 0` at which this
scalar is a non-negative integer `n` are exactly the **metallic ratios**
`δ_n = (n + √(n²+4))/2` — golden (`n = 1`), silver (`n = 2`),
bronze (`n = 3`), … (`n = 0` gives the trivial `δ_0 = 1`, i.e. `q = 1`) —
and the bar involution `q ↦ q⁻¹` sends `δ_n` to `δ_n − n = 1/δ_n`.

Ref: docs/audits/2026-06-08-q-regime-map-coordination.md §3b and
docs/audits/2026-06-08-metallic-q-hierarchy-proof.md (rigorous hand proof).

Machine-verified 2026-06-08 (lean v4.24.0): clean compile, and
`#print axioms` on every theorem here = `[propext, Classical.choice,
Quot.sound]` (the standard Mathlib axioms — no `sorryAx`).
-/

namespace QOU.AlgebraicSubstrate

open Real

/-- The `n`-th **metallic ratio**: the positive root of `x² − n·x − 1 = 0`.
`metallic 1 = φ` (golden), `metallic 2 = 1 + √2` (silver), … -/
noncomputable def metallic (n : ℕ) : ℝ := ((n : ℝ) + Real.sqrt ((n : ℝ) ^ 2 + 4)) / 2

lemma sqrt_sq_metallic (n : ℕ) :
    Real.sqrt ((n : ℝ) ^ 2 + 4) ^ 2 = (n : ℝ) ^ 2 + 4 :=
  Real.sq_sqrt (by positivity)

lemma sqrt_metallic_pos (n : ℕ) : 0 < Real.sqrt ((n : ℝ) ^ 2 + 4) :=
  Real.sqrt_pos.mpr (by positivity)

/-- `√(n²+4) ≥ n`. -/
lemma sqrt_metallic_ge (n : ℕ) : (n : ℝ) ≤ Real.sqrt ((n : ℝ) ^ 2 + 4) := by
  have hn : (0 : ℝ) ≤ (n : ℝ) := Nat.cast_nonneg n
  nlinarith [sqrt_sq_metallic n, sqrt_metallic_pos n, hn]

/-- **Metallic characterization.** For `q > 0`, the Hecke scalar `q − q⁻¹`
equals the integer `n` iff `q` is the `n`-th metallic ratio. -/
theorem metallic_iff_hecke_scalar (n : ℕ) (q : ℝ) (hq : 0 < q) :
    q - q⁻¹ = (n : ℝ) ↔ q = metallic n := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hs2 := sqrt_sq_metallic n
  have hspos := sqrt_metallic_pos n
  have hsge := sqrt_metallic_ge n
  constructor
  · intro h
    have hquad : q ^ 2 - (n : ℝ) * q - 1 = 0 := by
      field_simp at h; nlinarith [h]
    have hkey : (2 * q - (n : ℝ)) ^ 2 = Real.sqrt ((n : ℝ) ^ 2 + 4) ^ 2 := by
      rw [hs2]; nlinarith [hquad]
    have hfac : (2 * q - (n : ℝ) - Real.sqrt ((n : ℝ) ^ 2 + 4)) *
        (2 * q - (n : ℝ) + Real.sqrt ((n : ℝ) ^ 2 + 4)) = 0 := by
      linear_combination hkey
    rcases mul_eq_zero.mp hfac with h1 | h2
    · unfold metallic; linarith [h1]
    · exfalso; nlinarith [h2, hspos, hq, hsge]
  · intro h
    have hq2 : q ^ 2 = (n : ℝ) * q + 1 := by
      rw [h]; unfold metallic; nlinarith [hs2]
    field_simp; nlinarith [hq2]

/-- `metallic n > 0`. -/
lemma metallic_pos (n : ℕ) : 0 < metallic n := by
  unfold metallic; have := sqrt_metallic_pos n; positivity

/-- **Bar-involution pairing.** `(δ_n)⁻¹ = δ_n − n`, i.e. the involution
`q ↦ q⁻¹` sends the `n`-th metallic ratio to its sub-unit mirror. -/
theorem metallic_inv (n : ℕ) : (metallic n)⁻¹ = metallic n - (n : ℝ) := by
  have hq2 : (metallic n) ^ 2 = (n : ℝ) * metallic n + 1 := by
    unfold metallic; nlinarith [sqrt_sq_metallic n]
  have hpos := metallic_pos n
  field_simp
  nlinarith [hq2]

/-- **Golden is the first rung.** `metallic 1 = φ = (1 + √5)/2`. -/
theorem metallic_one_eq_golden : metallic 1 = (1 + Real.sqrt 5) / 2 := by
  unfold metallic; norm_num

/-- `δ_n` is a root of `x² − n·x − 1 = 0`. -/
lemma metallic_sq (n : ℕ) : (metallic n) ^ 2 = (n : ℝ) * metallic n + 1 := by
  unfold metallic; nlinarith [sqrt_sq_metallic n]

/-- **Quantum dimension at a metallic ratio.** The Temperley–Lieb loop /
quantum dimension `[2]_q = q + q⁻¹` evaluates to `√(n²+4)` at `q = δ_n`
(golden → `√5`, silver → `√8 = 2√2`). On the unit circle this scalar is
`2cos θ ∈ [−2,2]`; here on the real-metallic ladder it is `√(n²+4) ≥ 2`,
so only `n = 0` (`δ_0 = 1`, value `2`) meets the root-of-unity range — the
algebraic reason golden is the *unique* metallic ratio that is also a
root-of-unity quantum dimension (`φ = 2cos(π/5)`). -/
theorem metallic_two_q (n : ℕ) :
    metallic n + (metallic n)⁻¹ = Real.sqrt ((n : ℝ) ^ 2 + 4) := by
  rw [metallic_inv]; unfold metallic; ring

/-- **Golden self-similarity.** `φ² = φ + 1` — the defining golden identity,
here the `n = 1` case of `metallic_sq`. -/
theorem golden_self_similar : metallic 1 ^ 2 = metallic 1 + 1 := by
  rw [metallic_sq]; push_cast; ring

end QOU.AlgebraicSubstrate