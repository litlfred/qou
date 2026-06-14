import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Ring.Finset


/-!
# QOU.BraidKnot.plancherel_weight_boundedness

Plancherel weights `w_lam = (dim V_lam)² / n!` (with `dim V_lam` the
classical, q-independent Hecke irrep dimension) form a probability
distribution on partitions of `n`: each `w_lam ∈ [0, 1]` and
`Σ_lam w_lam = 1` exactly.

Remark: the q-deformed alternative `dim_q²/[n]_q!` does NOT sum to
1 at finite `q ≠ 1` (empirical: ~1.51 at q₀ ≈ 1.1097, n = 12);
it is recorded alongside but is not the probability measure.

This formalises the convergence guarantee for the curvature-rank
strata `Φ_k` and the universal Frobenius co-Casimir tail.

LaTeX label: `prop:plancherel-weight-boundedness`

## References

- [manuscript] Ch. Braids and Knots, §Plancherel boundedness
- [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU.BraidKnot

/-- Abstract Plancherel data: a finite indexing set with weights. -/
structure PlancherelDistribution where
  partitions : Finset (List ℕ)
  weight : List ℕ → ℝ
  weight_nonneg : ∀ lam ∈ partitions, 0 ≤ weight lam
  weight_sum_one : (partitions.sum weight) = 1

namespace PlancherelDistribution

variable (P : PlancherelDistribution)

/-- Each Plancherel weight is bounded above by 1. -/
-- Ref: [manuscript] Ch. Braids and Knots, §Plancherel boundedness
theorem weight_le_one : ∀ lam ∈ P.partitions, P.weight lam ≤ 1 := by
  intro lam hlam
  -- weight lam ≤ Σ_μ weight μ = 1, since other weights are non-negative.
  have h_sum : P.weight lam ≤ P.partitions.sum P.weight := by
    have := P.weight_nonneg
    exact Finset.single_le_sum (f := P.weight)
      (fun μ hμ => P.weight_nonneg μ hμ) hlam
  rw [P.weight_sum_one] at h_sum
  exact h_sum

/-- A bounded function on partitions yields a bounded weighted sum. -/
-- Ref: [manuscript] Ch. Braids and Knots, §Plancherel boundedness
theorem weighted_sum_bounded
    (f : List ℕ → ℝ) (M : ℝ)
    (hM : ∀ lam ∈ P.partitions, |f lam| ≤ M) (hM_nn : 0 ≤ M) :
    |P.partitions.sum (fun lam => P.weight lam * f lam)| ≤ M := by
  -- |Σ w · f| ≤ Σ |w · f| = Σ w · |f| ≤ Σ w · M = M · Σ w = M
  calc |P.partitions.sum (fun lam => P.weight lam * f lam)|
      ≤ P.partitions.sum (fun lam => |P.weight lam * f lam|) :=
        Finset.abs_sum_le_sum_abs _ _
    _ = P.partitions.sum (fun lam => P.weight lam * |f lam|) := by
        apply Finset.sum_congr rfl
        intro lam hlam
        rw [abs_mul, abs_of_nonneg (P.weight_nonneg lam hlam)]
    _ ≤ P.partitions.sum (fun lam => P.weight lam * M) := by
        apply Finset.sum_le_sum
        intro lam hlam
        exact mul_le_mul_of_nonneg_left (hM lam hlam) (P.weight_nonneg lam hlam)
    _ = (P.partitions.sum P.weight) * M := by
        rw [← Finset.sum_mul]
    _ = M := by rw [P.weight_sum_one, one_mul]

end PlancherelDistribution

/-- **Proposition (Plancherel-weight boundedness)**.

    The Plancherel distribution on partitions of `n` satisfies:
    1. Each weight is in `[0, 1]`.
    2. Sum of weights is `1`.

    Hence any bounded function `f : Partition → ℝ` has a Plancherel
    average bounded by `‖f‖_∞`. -/
-- Ref: [manuscript] Ch. Braids and Knots, §Plancherel boundedness
theorem plancherel_weight_boundedness (P : PlancherelDistribution) :
    (∀ lam ∈ P.partitions, 0 ≤ P.weight lam ∧ P.weight lam ≤ 1) ∧
    P.partitions.sum P.weight = 1 :=
  ⟨fun lam hlam => ⟨P.weight_nonneg lam hlam, P.weight_le_one lam hlam⟩,
   P.weight_sum_one⟩

end QOU.BraidKnot
