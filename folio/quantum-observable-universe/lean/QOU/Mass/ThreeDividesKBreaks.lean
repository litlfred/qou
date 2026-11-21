/-
  The `3 ∣ k` pattern does NOT persist for all `k` — the mechanism, in closed
  form.

  THE OPEN ITEM, quoted from `GammaGammaSelectionTen.lean` §"What is NOT proved":

    "whether the `3 ∣ k` pattern persists for all `k` — it is a statement about
     `cos(k·θ)` with `2 cos θ = −1 − h²`, i.e. about `θ/π`, which step 4 left
     open."

  This file settles the mechanism and the answer is **no**.

  THE IDENTIFICATION. `χ_k = 2 cos(k·θ)`, which `GammaGammaSelectionTen` points
  at in prose but does not use — it grinds a fresh Chebyshev polynomial per `k`,
  which is why it stopped at ten. §1 proves the recursion that backs the
  identification; the numerical agreement with all five published closed forms
  `χ₆ … χ₁₀` is checked to `1e-60` in the companion probe, not asserted here.

  THE MECHANISM. Write `θ = 2π/3 + δ`. At `δ = 0` the three residue classes give
  `χ_k = +2, −1, −1` — the `3 ∣ k` pattern exactly. For `δ > 0` the phase `k·δ`
  **accumulates**, and §2 computes what each class becomes:

      k = 3m      χ_k = 2 cos(k·δ)
      k = 3m+1    χ_k = 2 cos(2π/3 + k·δ)
      k = 3m+2    χ_k = 2 cos(4π/3 + k·δ)

  §3 is the refutation: a `k ≡ 2 (mod 3)` whose accumulated phase has reached the
  window `[π/6, 5π/6]` is **feasible while not divisible by 3**, so the pattern
  fails there. At the proton pin `δ = 0.025423100322699…` and `k = 23` is in the
  window — the probe supplies that witness and checks it.

  WHAT THIS DOES NOT BREAK, and the distinction is the whole point. The
  **selection** of `k = 3` is untouched: `FrobeniusSelected` minimises the word
  length over the feasible set, and every feasible `k ≠ 3` costs more than 3
  whether it is 6, 9, or the newly-feasible 23. What is false past `k = 22` is
  only the summary claim that the survivors *are* the powers of `V³`.
  `frobeniusSelected_borromean_ten` stands.

  🛑 NOT PROVED HERE:

  * The EXISTENCE of such a `k` from `δ > 0` alone. §3 takes the witness as a
    hypothesis (`k ≡ 2 mod 3` and the phase in window) and proves the failure
    from it; producing the `k` needs an archimedean/minimal-element argument
    this file does not carry. The probe exhibits `k = 23` and verifies the
    hypothesis numerically, so the refutation is complete as a pair — but the
    Lean half alone does not assert "for every `δ > 0` there is such a `k`".
  * That `θ/π > 2/3` at the pin. That is a numerical fact about `arccos`, and it
    is measured in the probe.
  * Anything about the `H₆` interface or the `InterfaceBranching` hypothesis.

  Sorry-free. No `axiom`, no conditional class, no `native_decide`.

  -- Ref: [leitner2026] QOU/Mass/GammaGammaSelectionTen.lean
  -- Ref: [leitner2026] computations/probes/gamma_gamma_three_divides_k_breaks_at_23_probe.py
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace QOU.Mass.ThreeDividesKBreaks

open Real

/-! ### 1. The recursion behind `χ_k = 2 cos(k·θ)` -/

/-- **The Chebyshev recursion for `2 cos(k·θ)`.**

`V` is `2×2` with `det V = 1` and `tr V = −1 − x`, so Cayley–Hamilton gives
`χ_{k+2} = (tr V)·χ_{k+1} − χ_k`. The trace sequence `2 cos(k·θ)` satisfies the
same recursion with `2 cos θ = tr V`, which is what identifies the two — and it
is why one cosine can replace the ten separate polynomial identities that
`GammaGammaSelectionTen` carries. -/
theorem two_cos_recursion (θ : ℝ) (k : ℕ) :
    2 * cos ((k + 2) * θ)
      = (2 * cos θ) * (2 * cos ((k + 1) * θ)) - 2 * cos (k * θ) := by
  have h : ((k : ℝ) + 2) * θ = ((k + 1) * θ) + θ := by ring
  have h' : (k : ℝ) * θ = ((k + 1) * θ) - θ := by ring
  rw [h, h', Real.cos_add, Real.cos_sub]
  ring

/-! ### 2. The residue split — where the `3 ∣ k` pattern comes from, and what
becomes of it once `δ > 0` -/

/-- **`k = 3m`: the `2π/3` part is whole turns, so only the accumulated phase
survives.**

This is why the multiples of 3 are the feasible ones at `δ = 0` (`cos 0 = 1`),
and equally why they STOP being feasible once `k·δ` passes `π/2`. -/
theorem cos_of_three_mul (m : ℕ) (δ : ℝ) :
    cos ((3 * m : ℕ) * (2 * π / 3 + δ)) = cos ((3 * m : ℕ) * δ) := by
  have h : ((3 * m : ℕ) : ℝ) * (2 * π / 3 + δ)
      = ((3 * m : ℕ) : ℝ) * δ + (m : ℤ) * (2 * π) := by
    push_cast; ring
  rw [h, Real.cos_add_int_mul_two_pi]

/-- **`k = 3m+2`: a fixed `4π/3` offset plus the accumulated phase.**

At `δ = 0` this is `cos (4π/3) = −1/2 < 0`, which is the infeasibility of the
non-multiples. The offset is fixed; the phase is not — and §3 is what happens
when the phase catches up. -/
theorem cos_of_three_mul_add_two (m : ℕ) (δ : ℝ) :
    cos ((3 * m + 2 : ℕ) * (2 * π / 3 + δ))
      = cos (4 * π / 3 + (3 * m + 2 : ℕ) * δ) := by
  have h : ((3 * m + 2 : ℕ) : ℝ) * (2 * π / 3 + δ)
      = (4 * π / 3 + ((3 * m + 2 : ℕ) : ℝ) * δ) + (m : ℤ) * (2 * π) := by
    push_cast; ring
  rw [h, Real.cos_add_int_mul_two_pi]

/-- **`k = 3m+1`: offset `2π/3`.** Included so the three classes are visibly a
partition and a reader is not left wondering whether this one behaves
differently. It does not — it has the largest threshold, `5π/6`, which is why
the probe finds its first feasible member at `k = 103` rather than 23. -/
theorem cos_of_three_mul_add_one (m : ℕ) (δ : ℝ) :
    cos ((3 * m + 1 : ℕ) * (2 * π / 3 + δ))
      = cos (2 * π / 3 + (3 * m + 1 : ℕ) * δ) := by
  have h : ((3 * m + 1 : ℕ) : ℝ) * (2 * π / 3 + δ)
      = (2 * π / 3 + ((3 * m + 1 : ℕ) : ℝ) * δ) + (m : ℤ) * (2 * π) := by
    push_cast; ring
  rw [h, Real.cos_add_int_mul_two_pi]

/-! ### 3. The refutation -/

/-- **The feasibility window for the `2 mod 3` class.**

`cos (4π/3 + φ) ≥ 0` exactly when the total angle has come round to the fourth
quadrant, i.e. `φ ∈ [π/6, 5π/6]`: at `φ = π/6` the angle is `3π/2` and the
cosine is `0`, at `φ = 5π/6` it is `2π + π/6`. So a `2 mod 3` candidate becomes
FEASIBLE once its accumulated phase reaches `π/6` — it does not need to reach a
half turn. That small threshold is why the pattern breaks in this class first. -/
theorem cos_four_pi_thirds_add_nonneg {φ : ℝ} (h1 : π / 6 ≤ φ) (h2 : φ ≤ 5 * π / 6) :
    0 ≤ cos (4 * π / 3 + φ) := by
  have hrw : 4 * π / 3 + φ = (φ - 2 * π / 3) + (1 : ℤ) * (2 * π) := by
    push_cast; ring
  rw [hrw, Real.cos_add_int_mul_two_pi]
  apply Real.cos_nonneg_of_mem_Icc
  constructor <;> linarith

/-- **The pattern fails: a `k ≡ 2 (mod 3)` whose phase has reached the window is
feasible.**

`3 ∤ k` and `χ_k ≥ 0` together contradict `χ_k ≥ 0 ↔ 3 ∣ k`. So this exhibits
the failure from the hypothesis that such a `k` exists; the companion probe
supplies `k = 23` at the proton pin, where `δ = 0.0254231…` puts `k·δ = 0.5847`
inside `[π/6, 5π/6] = [0.5236, 2.6180]`.

Note what the hypothesis costs: only that the accumulated phase has entered a
window of width `2π/3`. Since consecutive members of this residue class step the
phase by `3δ`, any `δ ≤ 2π/9` cannot step over the window — so such a `k` exists
for every small positive `δ`. That existence argument is NOT formalised here
(see the file header); this theorem is the implication it feeds. -/
theorem pattern_fails_at_residue_two (m : ℕ) (δ : ℝ)
    (h1 : π / 6 ≤ (3 * m + 2 : ℕ) * δ) (h2 : ((3 * m + 2 : ℕ) : ℝ) * δ ≤ 5 * π / 6) :
    ¬ (3 ∣ (3 * m + 2)) ∧ 0 ≤ 2 * cos ((3 * m + 2 : ℕ) * (2 * π / 3 + δ)) := by
  refine ⟨?_, ?_⟩
  · omega
  · rw [cos_of_three_mul_add_two]
    have := cos_four_pi_thirds_add_nonneg h1 h2
    linarith

/-- **So no `θ` with `δ > 0` can satisfy `χ_k ≥ 0 ↔ 3 ∣ k` for all `k`**, once
one such `k` is in the window. Stated as the refutation of the universal claim,
which is the form the open item was posed in. -/
theorem not_forall_feasible_iff_three_dvd (m : ℕ) (δ : ℝ)
    (h1 : π / 6 ≤ (3 * m + 2 : ℕ) * δ) (h2 : ((3 * m + 2 : ℕ) : ℝ) * δ ≤ 5 * π / 6) :
    ¬ (∀ k : ℕ, 0 ≤ 2 * cos (k * (2 * π / 3 + δ)) ↔ 3 ∣ k) := by
  intro hall
  obtain ⟨hndvd, hfeas⟩ := pattern_fails_at_residue_two m δ h1 h2
  exact hndvd ((hall (3 * m + 2)).mp hfeas)

/-- **The multiples of 3 fail too, just later.** `cos (k·δ) < 0` once the phase
passes `π/2`, so the `3 ∣ k` class is not permanently feasible either — at the
pin the first casualty is `k = 63`. Kept so a reader does not conclude that only
one direction of the equivalence breaks. -/
theorem three_dvd_becomes_infeasible (m : ℕ) (δ : ℝ)
    (h1 : π / 2 < (3 * m : ℕ) * δ) (h2 : ((3 * m : ℕ) : ℝ) * δ < 3 * π / 2) :
    2 * cos ((3 * m : ℕ) * (2 * π / 3 + δ)) < 0 := by
  rw [cos_of_three_mul]
  have : cos ((3 * m : ℕ) * δ) < 0 := by
    apply Real.cos_neg_of_pi_div_two_lt_of_lt h1
    linarith [Real.pi_pos]
  linarith

end QOU.Mass.ThreeDividesKBreaks
