import Mathlib.Tactic
import Mathlib.Analysis.SpecificLimits.Normed
import QOU.Mass.ConstantKernelGrowthBound

/-!
# Factorial growth is super-exponential — the bridge #6101 withdrew

`QOU.Mass.ConstantKernelGrowthBound` (landed in #6101) proves
`not_isConstKernelRec_of_superExponential`: no constant-kernel recurrence has a
`SuperExponential` solution, where

    SuperExponential a  :=  ∀ M K : ℝ, ∃ n, M * K ^ n < |a n|.

That is the right generality. But the corpus's actual growth statement is not
phrased that way: `SWPeriodSuperExponential.factorial_le_involution_two_mul`
(PR #6052) gives `n ! ≤ I (2n)` — a **factorial** lower bound on the *even*
subsequence. Without a bridge, the general theorem cannot be applied to the one
result that would trigger it.

#6101's author attempted that bridge and **withdrew it rather than half-prove
it**, recording in their docstring that they could not locate the Mathlib limit
lemma in this toolchain and that their first attempt mis-indexed `M·Kⁿ` at `2n`.
Their theorems are unaffected — nothing in their file needs it — and they noted
it "reads best" next to a factorial statement. This file supplies it.

## What is proved

* `superExponential_of_factorial_le` — if `n ! ≤ a (2n)` for every `n`, then `a`
  is `SuperExponential`. The index `2n` is what makes it work for *every real*
  `K`, negative included: `K ^ (2n) = (K²)ⁿ ≥ 0`, so the sign case on `M` is
  clean and no positivity hypothesis on `K` is needed.
* `not_isConstKernelRec_of_factorial_le` — hence no constant-kernel recurrence
  admits such an `a`, by composition with #6101's theorem.

The limit input is `Real.summable_pow_div_factorial`: `(K²)ⁿ / n !` is summable,
so its terms tend to zero, so the factorial outruns every geometric.
`tendsto_pow_div_factorial_atTop` does not exist under that name in this
toolchain, which is what stalled the original attempt.

## Scope

This is plumbing between two landed results, not a new finding. It decides
nothing about which premise of `prop:prolonged-periods-fixed-depth` is false —
the identification `a_D^(n) = I(n)/n`, the fixed-finite-rank operator, or the
`n`-independence of the kernel. See beans `qou-9yqb` and #6052.

Base ring `ℝ`: the content is an order/limit statement, so the archimedean
setting is genuinely required (AGENTS.md §7c).
-/

namespace QOU.MassTheory.FactorialSuperExponential

open QOU.Mass.ConstantKernelGrowthBound

/-- **Factorial growth on the even subsequence implies super-exponential
growth.** Stated against #6101's `SuperExponential`, so it composes directly
with `not_isConstKernelRec_of_superExponential`. -/
theorem superExponential_of_factorial_le {a : ℕ → ℝ}
    (h : ∀ n : ℕ, (Nat.factorial n : ℝ) ≤ a (2 * n)) : SuperExponential a := by
  intro M K
  have key : ∀ n : ℕ, M * K ^ (2 * n) = M * (K ^ 2) ^ n := by
    intro n; rw [← pow_mul, mul_comm 2 n]
  rcases le_or_lt M 0 with hM | hM
  · refine ⟨2 * 1, ?_⟩
    have hsq : (0:ℝ) ≤ (K ^ 2) ^ 1 := by positivity
    have hle : M * K ^ (2 * 1) ≤ 0 := by
      rw [key 1]; nlinarith [hsq, hM]
    have h1 : (Nat.factorial 1 : ℝ) ≤ a (2 * 1) := h 1
    have hf1 : (Nat.factorial 1 : ℝ) = 1 := by norm_num
    calc M * K ^ (2 * 1) ≤ 0 := hle
      _ < 1 := one_pos
      _ = (Nat.factorial 1 : ℝ) := hf1.symm
      _ ≤ a (2 * 1) := h1
      _ ≤ |a (2 * 1)| := le_abs_self _
  · have hlim := (Real.summable_pow_div_factorial (K ^ 2)).tendsto_atTop_zero
    have hev : ∀ᶠ n : ℕ in Filter.atTop,
        (K ^ 2) ^ n / (Nat.factorial n : ℝ) < 1 / M := by
      refine hlim.eventually (gt_mem_nhds ?_)
      positivity
    obtain ⟨n, hn⟩ := hev.exists
    refine ⟨2 * n, ?_⟩
    have hfacpos : (0:ℝ) < (Nat.factorial n : ℝ) := by positivity
    rw [div_lt_div_iff₀ hfacpos hM] at hn
    calc M * K ^ (2 * n) = M * (K ^ 2) ^ n := key n
      _ < (Nat.factorial n : ℝ) := by nlinarith [hn]
      _ ≤ a (2 * n) := h n
      _ ≤ |a (2 * n)| := le_abs_self _

/-- **Composition with #6101's theorem.** No depth-`d` constant-kernel recurrence
admits a solution growing at least factorially on its even subsequence. -/
theorem not_isConstKernelRec_of_factorial_le {d : ℕ} {c : Fin d → ℝ} {a : ℕ → ℝ}
    (hd : 0 < d) (h : ∀ n : ℕ, (Nat.factorial n : ℝ) ≤ a (2 * n)) :
    ¬ IsConstKernelRec d c a :=
  not_isConstKernelRec_of_superExponential hd (superExponential_of_factorial_le h)

end QOU.MassTheory.FactorialSuperExponential
