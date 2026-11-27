import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Positivity

/-!
# Metallic-ratio hierarchy of the Hecke scalar (algebraic form)

The Iwahori–Hecke generator satisfies `σ² = (q − q⁻¹)·σ + 1`, so the
structural scalar of the braiding is `q − q⁻¹`.  The real values `q > 0` at
which this scalar is a non-negative integer `n` are exactly the **metallic
ratios** `δ_n`, the positive roots of `x² − n·x − 1 = 0` — golden (`n = 1`),
silver (`n = 2`), bronze (`n = 3`), … — and the bar involution `q ↦ q⁻¹`
sends `δ_n` to `δ_n − n = 1/δ_n`.

**Transcendental boundary (owner ruling 2026-11-27, bean `qou-dk7p`).** This
file carries `δ` as a parameter with its defining relation `δ² = n·δ + 1`,
`0 < δ`, over any ordered field, and uses no `Real.sqrt`. The explicit real
root `metallic n = (n + √(n²+4))/2` and its named instances live behind the
boundary in `QOU.Transcendental.BringsSurface.MetallicHierarchyReal`.

Ref: docs/audits/2026-06-08-q-regime-map-coordination.md §3b and
docs/audits/2026-06-08-metallic-q-hierarchy-proof.md (rigorous hand proof).
-/

namespace QOU.AlgebraicSubstrate

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- **Metallic characterization.** For `q > 0` and a positive root `δ` of
`x² − n·x − 1`, the Hecke scalar `q − q⁻¹` equals `n` iff `q = δ`. -/
theorem metallicRoot_iff_hecke_scalar {n q δ : K} (hq : 0 < q)
    (hδ : δ ^ 2 = n * δ + 1) (hδpos : 0 < δ) :
    q - q⁻¹ = n ↔ q = δ := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  constructor
  · intro h
    have hquad : q ^ 2 - n * q - 1 = 0 := by
      field_simp at h; linear_combination h
    -- (q − δ)(q + δ − n) = 0, and q + δ − n > 0 because δ(δ − n) = 1 > 0
    have hfac : (q - δ) * (q + δ - n) = 0 := by linear_combination hquad - hδ
    have hδn : n < δ := by nlinarith
    rcases mul_eq_zero.mp hfac with h1 | h2
    · linarith
    · exfalso; linarith
  · intro h
    subst h
    field_simp
    linear_combination hδ

omit [IsStrictOrderedRing K] in
/-- **Bar-involution pairing.** `δ⁻¹ = δ − n`. -/
theorem metallicRoot_inv {n δ : K} (hδ : δ ^ 2 = n * δ + 1) (hδpos : 0 < δ) :
    δ⁻¹ = δ - n := by
  have h0 : δ ≠ 0 := ne_of_gt hδpos
  field_simp
  linear_combination -hδ

omit [IsStrictOrderedRing K] in
/-- **Quantum dimension at a metallic ratio.** `[2]_δ = δ + δ⁻¹ = 2δ − n`, and its
square is `n² + 4`. On the unit circle this scalar is `2cos θ ∈ [−2,2]`; on the
real-metallic ladder its square is `n² + 4 ≥ 4`, so only `n = 0` meets the
root-of-unity range. -/
theorem metallicRoot_two_q {n δ : K} (hδ : δ ^ 2 = n * δ + 1) (hδpos : 0 < δ) :
    δ + δ⁻¹ = 2 * δ - n ∧ (δ + δ⁻¹) ^ 2 = n ^ 2 + 4 := by
  rw [metallicRoot_inv hδ hδpos]
  refine ⟨by ring, ?_⟩
  linear_combination 4 * hδ

omit [LinearOrder K] [IsStrictOrderedRing K] in
/-- **Golden self-similarity.** A golden root `φ² = φ + 1` is the `n = 1` case. -/
theorem goldenRoot_self_similar {φ : K} (hφ : φ ^ 2 = 1 * φ + 1) : φ ^ 2 = φ + 1 := by
  linear_combination hφ

end QOU.AlgebraicSubstrate
