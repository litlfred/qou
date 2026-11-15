/-
# The Milnor deficit sign and the weight bar-parity agree in VALUE but not in MECHANISM

The Milnor-parity sign law (#4389) gives the A-body Brunnian cluster deficit sign
`sign(1 − τ_A) = (−1)^{A−1}` (A=3 `+` proved, A=4 `−` measured, general open). My weight bar-sign
(#4399) is `(−1)^{n-1}` at `n = 3A`, and `(−1)^{3A−1} = (−1)^{A−1}` — the same value.

**This file records why the agreement is a CONVERGENCE, not a derivation.** Three pure
arithmetic/parity facts capture the structural obstruction:

1. the deficit order `2(A−1)` is **even** — the deficit is bar-even, so its sign is a leading-
   *coefficient* (Milnor / `(A−1)`-fold-commutator) effect, never a bar-parity flip;
2. the weight-prefactor order `n−1 = 3A−1` **strictly exceeds** the deficit order `2(A−1)` — and
   because `τ_A` is a *normalized* (link/unlink) trace, the `(q−q⁻¹)^{n-1}` Ocneanu weight prefactor
   **cancels** (it is absent from the `h^{2(A−1)}` deficit, verified on the proved Borromean closed
   form `h⁴(3+h²)/(h²+4)`); so it cannot set the deficit's leading sign;
3. yet `(−1)^{3A−1} = (−1)^{A−1}` — the two signs coincide in value.

Together: same value (fact 3), distinct-order sources (facts 1–2, the weight is a cancelled,
subleading prefactor). The `(−1)^{A−1}` match is a convergence via distinct mechanisms. This is an
anti-laundering safeguard: it forbids passing the coincidence off as a derivation of the sign law that
#4389 leaves open. Sign claims only; no magnitude, no fit, nothing wired.
-/
import Mathlib.Tactic

namespace QOU.MassTheory.MilnorWeightParity

/-- **Deficit order is even.** `2(A−1)` is even, so the A-body deficit `1 − τ_A` (leading order
`h^{2(A−1)}`) is bar-even; its sign is a leading-*coefficient* effect, not a bar-parity flip. -/
theorem deficit_order_even (A : ℕ) : Even (2 * (A - 1)) :=
  ⟨A - 1, by ring⟩

/-- **The weight prefactor is subleading.** For `A ≥ 1` the Ocneanu-weight order `n−1 = 3A−1` strictly
exceeds the deficit order `2(A−1)`. Since `τ_A` is a normalized (link/unlink) ratio the weight
prefactor cancels; being higher-order it cannot set the deficit's leading sign. -/
theorem weight_order_gt_deficit (A : ℕ) (hA : 1 ≤ A) : 2 * (A - 1) < 3 * A - 1 := by
  omega

/-- **The parity coincidence.** The weight bar-sign `(−1)^{n-1} = (−1)^{3A−1}` equals the cluster sign
`(−1)^{A−1}` (phrased with `A = k+1` so `ℕ`-subtraction is well-defined). Same VALUE — the source
orders differ (facts above), so this is a convergence, not a derivation. -/
theorem weight_parity_eq_cluster_sign (k : ℕ) :
    ((-1 : ℤ)) ^ (3 * (k + 1) - 1) = (-1) ^ ((k + 1) - 1) := by
  have e1 : 3 * (k + 1) - 1 = 3 * k + 2 := by omega
  have e2 : (k + 1) - 1 = k := by omega
  rw [e1, e2, pow_add, pow_mul]
  norm_num

/-- **Convergence, not derivation (the packaged statement).** For `A = k+1 ≥ 1`: the signs agree in
value (`weight_parity_eq_cluster_sign`) while the weight order strictly exceeds the (even) deficit
order — so the shared `(−1)^{A−1}` comes from distinct-order objects. -/
theorem convergence_not_derivation (k : ℕ) :
    ((-1 : ℤ)) ^ (3 * (k + 1) - 1) = (-1) ^ ((k + 1) - 1)
      ∧ 2 * ((k + 1) - 1) < 3 * (k + 1) - 1
      ∧ Even (2 * ((k + 1) - 1)) :=
  ⟨weight_parity_eq_cluster_sign k, weight_order_gt_deficit (k + 1) (by omega),
   deficit_order_even (k + 1)⟩

end QOU.MassTheory.MilnorWeightParity
