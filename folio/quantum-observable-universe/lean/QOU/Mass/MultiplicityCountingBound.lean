/-
# The counting bound behind the multiplicity channel — generic base ring

The substrate half of `QOU/Mass/MultiplicityNotExtensive.lean` (bean
`qou-brng`). Split out under AGENTS.md §7c: nothing in this file needs an
ordering beyond a linearly ordered ring, no `Real.log`, no `Real.sqrt`, no
`q`, no anchor. The archimedean consequences — the log-amplitude form, the
`√A` law and the AME comparison — live in the sibling, which consumes this,
exactly as `BondCutSymmetryLogBound.lean` consumes `BondCutSymmetry.lean`.

## What it says

A signed sum of `m` terms, each bounded in absolute value by `M`, is bounded
by `m·M`. That is the **entire** multiplicity channel of a trace-sum binding
law: having many summands instead of one can buy a factor of their number and
nothing more, whatever the signs are and whatever the braid word is.

The bound is deliberately one-sided. Cancellation only makes the left side
smaller, and the claim under test — that the partition sum's *multiplicity*
supplies the binding's extensive term — is a claim that many summands make the
sum **bigger**. So the direction proved here is the direction that decides it.

## Why a signed statement is the point

`QOU/Hecke/BondCutSymmetry.lean` (#7165) excludes positive pair-additive bond
counts, and its `bondSum_nonneg` needs `0 ≤ n_pp`, `0 ≤ n_pn`, `0 ≤ n_nn` —
the summands there are **counts**. The Frobenius pairing's summands are not:
`Δ_λ = (-1)^{n(λ)}·dim V_λ` carries a proved sign. Everything below is stated
for arbitrary signs precisely so that it reaches the object `BondCutSymmetry`
cannot.

-- Ref: [macdonald1995] https://doi.org/10.1093/oso/9780198534891.001.0001
-/

import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.AbsoluteValue.Basic
import Mathlib.Tactic

namespace QOU.Mass.MultiplicityCountingBound

variable {R : Type*} [Ring R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **Many summands buy at most a factor of their number.** A signed sum whose
summands are bounded by `M` is bounded by `card · M`. This is the entire
multiplicity channel: the triangle inequality, and no more is available. -/
theorem abs_sum_le_card_mul {ι : Type*} (s : Finset ι) (a : ι → R) (M : R)
    (hM : ∀ i ∈ s, |a i| ≤ M) :
    |∑ i ∈ s, a i| ≤ (s.card : R) * M := by
  calc |∑ i ∈ s, a i| ≤ ∑ i ∈ s, |a i| := Finset.abs_sum_le_sum_abs _ _
    _ ≤ s.card • M := Finset.sum_le_card_nsmul _ _ _ hM
    _ = (s.card : R) * M := nsmul_eq_mul _ _

/-- The same bound stated against the dominant summand: if `a i₀` attains the
maximum absolute value, the whole sum is at most `card` times it. -/
theorem abs_sum_le_card_mul_dominant {ι : Type*} (s : Finset ι) (a : ι → R)
    (i₀ : ι) (hdom : ∀ i ∈ s, |a i| ≤ |a i₀|) :
    |∑ i ∈ s, a i| ≤ (s.card : R) * |a i₀| :=
  abs_sum_le_card_mul s a _ hdom

/-- **The bound has content: it is not vacuous and it is not an equality.**
A two-element signed sum `1 + (-1) = 0` is strictly below `2 · 1`, so the
inequality is genuinely one-sided — cancellation is real, and the multiplicity
channel is an upper bound on what many summands can supply, never a value. -/
example : |((1 : ℤ) + (-1))| < ((2 : ℕ) : ℤ) * 1 := by norm_num

/-- **Non-negative difference form of `abs_sum_le_card_mul_dominant` (`qou-8fl1`).**
If `∀ i ∈ s, |a i| ≤ |a i₀|`, then `0 ≤ (s.card : R) * |a i₀| - |∑ i ∈ s, a i|`. -/
theorem sub_nonneg_of_dominant {ι : Type*} (s : Finset ι) (a : ι → R)
    (i₀ : ι) (hdom : ∀ i ∈ s, |a i| ≤ |a i₀|) :
    0 ≤ (s.card : R) * |a i₀| - |∑ i ∈ s, a i| :=
  sub_nonneg.mpr (abs_sum_le_card_mul_dominant s a i₀ hdom)

end QOU.Mass.MultiplicityCountingBound
