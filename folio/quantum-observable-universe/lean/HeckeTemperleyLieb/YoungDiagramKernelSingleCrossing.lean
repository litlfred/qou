import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# QOU.BraidsAndKnots.YoungDiagramKernelSingleCrossing — single crossing ⇒ positive first moment

The covariance-kernel moment `M₁(n) = Cov_Planch(Σ_□ h, ω₃)` (bean `qou-k5r5`) can be written,
via the Jucys–Murphy elements and Young's orthogonal form (audit
`docs/audits/2026-11-27-covariance-kernel-M1-jucys-murphy-form.md`), as

  `M₁(n) = (n(n−1)(n−2)/3) · Σ_s s · ρₙ(s)`,

where `ρₙ(s)` is a signed measure on the antidiagonal index `s = i + j` of the `n`-th box of
Plancherel growth, and `Σ_s ρₙ(s) = 0`. That identity is computer-verified, not formalized here.

This file proves the elementary step that turns a **sign pattern** of `ρₙ` into positivity. Suppose
a mass-zero signed measure on `{0, …, N−1}` is `≤ 0` below a threshold `t` and `≥ 0` from `t` on
(one crossing). Then its first moment is `≥ 0`. It is `> 0` unless the measure is zero.

Proof: `Σ s·ρ(s) = Σ (s − t)·ρ(s) + t·Σ ρ(s)`. The second term vanishes, and every summand of the
first is `≥ 0`.

The hypothesis (one crossing for every `n`) is **not** proved. Exact computation confirms it for
`n ≤ 34`. So this is a reduction of `M₁ > 0` to a sign-pattern statement, not a proof of `M₁ > 0`.

Base ring: a generic ordered commutative ring (§7c), with no `ℝ`.
-/

namespace QOU.BraidsAndKnots.YoungDiagramKernelSingleCrossing

open Finset

variable {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **Single crossing ⇒ nonnegative first moment.** -/
theorem firstMoment_nonneg_of_single_crossing (ρ : ℕ → R) (N t : ℕ)
    (hmass : ∑ s ∈ range N, ρ s = 0)
    (hneg : ∀ s, s < t → ρ s ≤ 0)
    (hpos : ∀ s, t ≤ s → 0 ≤ ρ s) :
    0 ≤ ∑ s ∈ range N, (s : R) * ρ s := by
  have hsplit : ∑ s ∈ range N, (s : R) * ρ s
      = ∑ s ∈ range N, ((s : R) - t) * ρ s + (t : R) * ∑ s ∈ range N, ρ s := by
    rw [mul_sum, ← sum_add_distrib]
    refine sum_congr rfl (fun s _ => ?_)
    ring
  rw [hsplit, hmass, mul_zero, add_zero]
  refine sum_nonneg (fun s _ => ?_)
  rcases lt_or_ge s t with h | h
  · have h1 : (s : R) - t ≤ 0 := by
      have : (s : R) < t := by exact_mod_cast h
      linarith
    exact mul_nonneg_of_nonpos_of_nonpos h1 (hneg s h)
  · have h1 : 0 ≤ (s : R) - t := by
      have : (t : R) ≤ s := by exact_mod_cast h
      linarith
    exact mul_nonneg h1 (hpos s h)

/-- **Single crossing ⇒ strictly positive first moment**, unless the measure vanishes. -/
theorem firstMoment_pos_of_single_crossing (ρ : ℕ → R) (N t : ℕ)
    (hmass : ∑ s ∈ range N, ρ s = 0)
    (hneg : ∀ s, s < t → ρ s ≤ 0)
    (hpos : ∀ s, t ≤ s → 0 ≤ ρ s)
    (hne : ∃ s ∈ range N, ρ s ≠ 0) :
    0 < ∑ s ∈ range N, (s : R) * ρ s := by
  have hsplit : ∑ s ∈ range N, (s : R) * ρ s
      = ∑ s ∈ range N, ((s : R) - t) * ρ s + (t : R) * ∑ s ∈ range N, ρ s := by
    rw [mul_sum, ← sum_add_distrib]
    refine sum_congr rfl (fun s _ => ?_)
    ring
  have hterm : ∀ s ∈ range N, 0 ≤ ((s : R) - t) * ρ s := by
    intro s _
    rcases lt_or_ge s t with h | h
    · have h1 : (s : R) - t ≤ 0 := by
        have : (s : R) < t := by exact_mod_cast h
        linarith
      exact mul_nonneg_of_nonpos_of_nonpos h1 (hneg s h)
    · have h1 : 0 ≤ (s : R) - t := by
        have : (t : R) ≤ s := by exact_mod_cast h
        linarith
      exact mul_nonneg h1 (hpos s h)
  rw [hsplit, hmass, mul_zero, add_zero]
  -- Some s ≠ t carries nonzero mass: if only t did, the total mass would be ρ t ≠ 0.
  by_contra hle
  have hzero : ∑ s ∈ range N, ((s : R) - t) * ρ s = 0 :=
    le_antisymm (not_lt.mp hle) (sum_nonneg hterm)
  have hall : ∀ s ∈ range N, ((s : R) - t) * ρ s = 0 :=
    (sum_eq_zero_iff_of_nonneg hterm).mp hzero
  obtain ⟨s₀, hs₀, hρ₀⟩ := hne
  have hst : s₀ = t := by
    by_contra hne'
    have hsub : (s₀ : R) - t ≠ 0 := by
      intro h
      apply hne'
      exact_mod_cast (sub_eq_zero.mp h)
    exact hρ₀ ((mul_eq_zero.mp (hall s₀ hs₀)).resolve_left hsub)
  -- Every s ≠ t has ρ s = 0, so the total mass is ρ t = ρ s₀ ≠ 0: contradiction.
  have hrest : ∀ s ∈ range N, s ≠ s₀ → ρ s = 0 := by
    intro s hs hne'
    have hsub : (s : R) - t ≠ 0 := by
      intro h
      apply hne'
      rw [hst]
      exact_mod_cast (sub_eq_zero.mp h)
    exact (mul_eq_zero.mp (hall s hs)).resolve_left hsub
  have hsum : ∑ s ∈ range N, ρ s = ρ s₀ := sum_eq_single_of_mem s₀ hs₀ hrest
  exact hρ₀ (hsum.symm.trans hmass)

end QOU.BraidsAndKnots.YoungDiagramKernelSingleCrossing
