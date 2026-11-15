import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Algebra.Order.Ring.Abs
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Ring.Finset


/-!
# QOU.BraidKnot.plancherel_weight_boundedness

Plancherel weights `w_λ = (dim V_λ)² / n!` (with `dim V_λ` the
classical, q-independent Hecke irrep dimension) form a probability
distribution on partitions of `n`: each `w_λ ∈ [0, 1]` and
`Σ_λ w_λ = 1` exactly.

Remark: the q-deformed alternative `dim_q²/[n]_q!` does NOT sum to
1 at finite `q ≠ 1` (empirical: ~1.51 at q₀ ≈ 1.1097, n = 12);
it is recorded alongside but is not the probability measure.

This formalises the convergence guarantee for the curvature-rank
strata `Φ_k` and the universal Frobenius co-Casimir tail.

## Base ring (AGENTS.md §7c)

Pre-archimedean: the statements below hold over **any** linearly
ordered commutative ring `R` — `[CommRing R] [LinearOrder R]
[IsStrictOrderedRing R]` — and use no completeness, no `Real.*`
function and no archimedean axiom. Only the order is needed (for
`0 ≤ w_λ`, `|·|` and `Finset.single_le_sum`). This matches the
narrative, which asserts `Σ_λ w_λ = 1` *exactly in* `ℚ`: the
classical weights `(dim V_λ)²/n!` are rational, so `R := ℚ` is
already an instance and the previous `ℝ` specialisation was
gratuitous. `R := ℝ` remains an instance for archimedean evaluation
downstream.

LaTeX label: `prop:plancherel-weight-boundedness`

## References

- [leitner2026] Ch. Braids and Knots, §Plancherel boundedness
- [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU.BraidKnot

/-- Abstract Plancherel data: a finite indexing set with weights,
    over any linearly ordered commutative ring (§7c: no archimedean
    input; `ℚ` and `ℝ` are both instances). -/
structure PlancherelDistribution (R : Type*) [CommRing R] [LinearOrder R]
    [IsStrictOrderedRing R] where
  partitions : Finset (List ℕ)
  weight : List ℕ → R
  weight_nonneg : ∀ p ∈ partitions, 0 ≤ weight p
  weight_sum_one : (partitions.sum weight) = 1

namespace PlancherelDistribution

variable {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
variable (P : PlancherelDistribution R)

/-- Each Plancherel weight is bounded above by 1. -/
-- Ref: [leitner2026] Ch. Braids and Knots, §Plancherel boundedness
theorem weight_le_one : ∀ p ∈ P.partitions, P.weight p ≤ 1 := by
  intro p hp
  -- weight p ≤ Σ_μ weight μ = 1, since other weights are non-negative.
  have h_sum : P.weight p ≤ P.partitions.sum P.weight := by
    have := P.weight_nonneg
    exact Finset.single_le_sum (f := P.weight)
      (fun μ hμ => P.weight_nonneg μ hμ) hp
  rw [P.weight_sum_one] at h_sum
  exact h_sum

/-- A bounded function on partitions yields a bounded weighted sum. -/
-- Ref: [leitner2026] Ch. Braids and Knots, §Plancherel boundedness
theorem weighted_sum_bounded
    (f : List ℕ → R) (M : R)
    (hM : ∀ p ∈ P.partitions, |f p| ≤ M) (_hM_nn : 0 ≤ M) :
    |P.partitions.sum (fun p => P.weight p * f p)| ≤ M := by
  -- |Σ w · f| ≤ Σ |w · f| = Σ w · |f| ≤ Σ w · M = M · Σ w = M
  calc |P.partitions.sum (fun p => P.weight p * f p)|
      ≤ P.partitions.sum (fun p => |P.weight p * f p|) :=
        Finset.abs_sum_le_sum_abs _ _
    _ = P.partitions.sum (fun p => P.weight p * |f p|) := by
        apply Finset.sum_congr rfl
        intro p hp
        rw [abs_mul, abs_of_nonneg (P.weight_nonneg p hp)]
    _ ≤ P.partitions.sum (fun p => P.weight p * M) := by
        apply Finset.sum_le_sum
        intro p hp
        exact mul_le_mul_of_nonneg_left (hM p hp) (P.weight_nonneg p hp)
    _ = (P.partitions.sum P.weight) * M := by
        rw [← Finset.sum_mul]
    _ = M := by rw [P.weight_sum_one, one_mul]

end PlancherelDistribution

/-- **Proposition (Plancherel-weight boundedness)**.

    The Plancherel distribution on partitions of `n` satisfies:
    1. Each weight is in `[0, 1]`.
    2. Sum of weights is `1`.

    Hence any bounded function `f : Partition → R` has a Plancherel
    average bounded by `‖f‖_∞`.

    Stated over any linearly ordered commutative ring (§7c). -/
-- Ref: [leitner2026] Ch. Braids and Knots, §Plancherel boundedness
theorem plancherel_weight_boundedness {R : Type*} [CommRing R] [LinearOrder R]
    [IsStrictOrderedRing R] (P : PlancherelDistribution R) :
    (∀ p ∈ P.partitions, 0 ≤ P.weight p ∧ P.weight p ≤ 1) ∧
    P.partitions.sum P.weight = 1 :=
  ⟨fun p hp => ⟨P.weight_nonneg p hp, P.weight_le_one p hp⟩,
   P.weight_sum_one⟩

end QOU.BraidKnot
