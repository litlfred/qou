import QOU.AppendixSurreals.QCollatz

/-!
# The `[2]_q`-adic valuation is not a descent measure (Front A, A1)

`reaches_cycle_of_descent` reduces q-Collatz convergence to the existence of a
measure `μ : Skein → ℕ` strictly decreasing off the attractor. The natural
candidate is the `[2]_q`-adic valuation `v_[2] = qTwoValuation` (multiplicity of
the root `q = -1`). It descends by exactly one on an **even** step
(`qTwoValuation_mul_qplus_one`) — but on an **odd** step it can *increase*.

This file machine-checks that failure with a concrete witness, turning the audit's
prose wall into a theorem: `P = -X - 2` is `q`-odd (`v_[2] = 0`), yet its odd
branch `([3]_q P + 1)/[2]_q = -(X+1)²` has `v_[2] = 2`. So **no unconditional
monotone descent measure can equal `v_[2]` alone.**

**Scope (a), not (b).** This rules out the *obvious* candidate `μ = v_[2]`; it does
**not** exclude the existence of *some* descent measure (the convergence wall
stays open). No fabricated `μ`.
-/

namespace QOU.AppendixSurreals

open Polynomial

/-- **The `[2]_q`-adic valuation increases on an odd step** — so it is not a
    descent measure. Witness `P = -X-2` (`q`-odd, `v_[2] = 0`); the odd-branch
    relation `[2]_q · Pnext = [3]_q · P + 1` gives `Pnext = -(X+1)²` with
    `v_[2] = 2`. Scope-(a): kills the natural `μ` candidate, not the conjecture. -/
theorem qcollatz_vTwo_increases_on_odd_branch :
    ∃ P Pnext : Polynomial ℤ,
      (X + 1) * Pnext = (X ^ 2 + X + 1) * P + 1 ∧
      qTwoValuation P = 0 ∧ 2 ≤ qTwoValuation Pnext := by
  refine ⟨-X - 2, -(X + 1) ^ 2, ?_, ?_, ?_⟩
  · ring
  · -- v_[2](-X-2) = 0 : (-X-2) is not zero at q = -1
    unfold qTwoValuation
    apply Polynomial.rootMultiplicity_eq_zero
    simp [Polynomial.IsRoot]
  · -- v_[2](-(X+1)²) ≥ 2 : (X+1)² divides it
    unfold qTwoValuation
    have hXC : (X - C (-1 : ℤ)) = X + 1 := by
      rw [C_neg, C_1, sub_neg_eq_add]
    have hne : (-(X + 1) ^ 2 : Polynomial ℤ) ≠ 0 := by
      have h1 : (X + 1 : Polynomial ℤ) ≠ 0 := by
        simpa using (monic_X_add_C (1 : ℤ)).ne_zero
      simpa using pow_ne_zero 2 h1
    rw [Polynomial.le_rootMultiplicity_iff hne, hXC]
    exact ⟨-1, by ring⟩

/-- **Odd-branch divisor evaluation (`qcz14` B4):** any polynomial `P : Polynomial ℤ`
    admitting an odd-branch successor `(X + 1) * Pnext = (X ^ 2 + X + 1) * P + 1`
    must evaluate to `-1` at `X = -1`. -/
theorem odd_branch_forces_eval_neg_one {P Pnext : Polynomial ℤ}
    (hodd : (X + 1) * Pnext = (X ^ 2 + X + 1) * P + 1) :
    P.eval (-1) = -1 := by
  have heval := congrArg (Polynomial.eval (-1 : ℤ)) hodd
  simp only [eval_mul, eval_add, eval_pow, eval_X, eval_one] at heval
  linarith

/-- **Odd-branch zero-valuation law (`qcz14` B4):** any polynomial `P : Polynomial ℤ`
    admitting an odd-branch successor `(X + 1) * Pnext = (X ^ 2 + X + 1) * P + 1`
    has `[2]_q`-adic valuation `qTwoValuation P = 0` (`P` is `q`-odd). -/
theorem odd_branch_forces_vTwo_zero {P Pnext : Polynomial ℤ}
    (hodd : (X + 1) * Pnext = (X ^ 2 + X + 1) * P + 1) :
    qTwoValuation P = 0 := by
  have hev : P.eval (-1) = -1 := odd_branch_forces_eval_neg_one hodd
  unfold qTwoValuation
  apply Polynomial.rootMultiplicity_eq_zero
  intro hroot
  rw [Polynomial.IsRoot.def, hev] at hroot
  omega

/-- **Higher `[2]_q`-adic valuation jump (`v_[2] ≥ 5`) on a single odd branch (`qcz14` B4):**
    For `P = -(X + 2) * (1 - (X + 1) ^ 3)`, `P` is `q`-odd (`qTwoValuation P = 0`), while its
    odd-branch successor `Pnext = (X + 1) ^ 5` satisfies `(X + 1) * Pnext = (X ^ 2 + X + 1) * P + 1`
    and `5 ≤ qTwoValuation Pnext`. -/
theorem qcollatz_vTwo_jump_five_on_odd_branch :
    ∃ P Pnext : Polynomial ℤ,
      (X + 1) * Pnext = (X ^ 2 + X + 1) * P + 1 ∧
      qTwoValuation P = 0 ∧ 5 ≤ qTwoValuation Pnext := by
  refine ⟨-(X + 2) * (1 - (X + 1) ^ 3), (X + 1) ^ 5, ?_, ?_, ?_⟩
  · ring
  · exact odd_branch_forces_vTwo_zero (Pnext := (X + 1) ^ 5) (by ring)
  · unfold qTwoValuation
    have hXC : (X - C (-1 : ℤ)) = X + 1 := by
      rw [C_neg, C_1, sub_neg_eq_add]
    have hne : ((X + 1) ^ 5 : Polynomial ℤ) ≠ 0 := by
      have h1 : (X + 1 : Polynomial ℤ) ≠ 0 := by
        simpa using (monic_X_add_C (1 : ℤ)).ne_zero
      exact pow_ne_zero 5 h1
    rw [Polynomial.le_rootMultiplicity_iff hne, hXC]

end QOU.AppendixSurreals
