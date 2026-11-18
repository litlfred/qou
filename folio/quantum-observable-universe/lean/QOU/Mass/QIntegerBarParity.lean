/-
  Why the corpus's quantum integer is the BALANCED one: bar parity.

  The corpus carries two q-integer conventions (nine definitions across nine
  files at the time of writing, four geometric and five balanced):

      GEOMETRIC   `qIntPoly q n = ∑_{i<n} q^i`        (`QOU.Mass.QHookDimensionBalanced`)
      BALANCED    `qIntBal  q n = (q^n − q⁻¹^n)/(q − q⁻¹)`

  (Module reference corrected 2026-08-30: the geometric `qIntPoly` was in
  `QOU.Mass.QHookDimension` when this file was written and moved out in
  `1646b5d6d3`, which replaced it there with a *balanced* `qInt`. It survives
  verbatim — same `∑_{i<n} q^i`, over `CommRing` — in
  `QOU.Mass.QHookDimensionBalanced`, which this file already imports. The
  `open` was left pointing at the old home, so this file has not compiled
  since that commit.)
                                                      (`QOU.Mass.QHookDimensionBalanced`)

  `qIntBal_eq_twist` already relates them: `qIntBal q n = q⁻¹^(n−1) · qIntPoly (q^2) n`.
  So they are ONE object reparametrised, and a geometric site is *correct*
  precisely when its variable means `q^2`.

  THIS FILE PROVES THE SEPARATING PROPERTY — their behaviour under the bar
  involution `σ : q ↦ q⁻¹`, which is the involution the whole corpus runs on
  (the sinh/cosh split, bar-even vs bar-odd channels, the `c₃` parity
  bookkeeping, AGENTS.md §"Im(q) at fibre vs observable level"):

    * `qIntBal_bar_even`      — `[n]_{q⁻¹} = [n]_q`.  BAR-EVEN, an invariant.
    * `qIntPoly_bar_covariant` — `qIntPoly q⁻¹ n = q⁻¹^(n−1) · qIntPoly q n`.
      NOT invariant: it transforms with weight `−(n−1)`.

  WHY IT MATTERS, stated as the contrapositive that is actually usable:
  `qIntPoly_bar_even_forces_degenerate` shows the geometric form is bar-even
  *only* in degenerate cases (`n ≤ 1`, `q^(n−1) = 1`, or a vanishing sum).  So **any quantity required to be
  bar-even — every cosh-channel / mass-side object — must use the balanced
  form**; a geometric `[n]` inside one breaks the parity bookkeeping silently,
  because at a single anchor the two differ only by a monomial factor that no
  single-point check can see.

  This is the structural reason the balanced convention is FORCED rather than
  chosen.  It is independent of, and complementary to, the other two reasons
  recorded in the companion audit:
    * AGENTS.md §7a's Hecke relation `(σ−q)(σ+q⁻¹) = 0` has structure constant
      `q − q⁻¹`, the balanced denominator;
    * balanced `[n]_q` is the quantum dimension of the k-dimensional `U_q(sl₂)`
      irrep, i.e. the sum over a SYMMETRIC `sl₂` weight string.

  Base ring: generic `Field R` (§7c) — this is pure algebra, no ordering, no
  `Real.sqrt`, nothing archimedean.  `q ≠ 0` and `q^2 ≠ 1` are exactly the
  hypotheses under which the balanced form is defined at all (its denominator
  `q − q⁻¹` vanishes iff `q^2 = 1`).

  -- Ref: [leitner2026] docs/audits/2026-08-08-q-integer-convention-derived.md
  -- Ref: [leitner2026] AGENTS.md §7a (Hecke–Skein convention)
-/

import Mathlib.Tactic
import QOU.Mass.QHookDimension
import QOU.Mass.QHookDimensionBalanced

open QOU.Mass.QHookDimensionBalanced (qIntPoly)

namespace QOU.Mass.QIntegerBarParity

open QOU.Mass.QHookDimensionBalanced (qIntBal)

variable {R : Type*} [Field R]

/-- **The balanced quantum integer is BAR-EVEN.**

`[n]_{q⁻¹} = [n]_q` — the bar involution `σ : q ↦ q⁻¹` fixes it.

Both the numerator and the denominator change sign under `σ`, and the two signs
cancel.  This is the property that makes the balanced form the one compatible
with the corpus's bar-even / bar-odd channel decomposition.

No hypothesis at all: `inv_inv` holds unconditionally in a field, so this is an
identity of the *definition*, not a statement about a regular `q`. -/
theorem qIntBal_bar_even (q : R) (n : ℕ) :
    qIntBal q⁻¹ n = qIntBal q n := by
  unfold qIntBal
  rw [inv_inv]
  -- `(q⁻¹^n − q^n)/(q⁻¹ − q) = (q^n − q⁻¹^n)/(q − q⁻¹)`: negate top and bottom.
  rw [show q⁻¹ ^ n - q ^ n = -(q ^ n - q⁻¹ ^ n) by ring,
      show q⁻¹ - q = -(q - q⁻¹) by ring]
  exact neg_div_neg_eq _ _

/-- **The geometric quantum integer is NOT bar-even — it is bar-COVARIANT**,
transforming with weight `−(n−1)`:

`qIntPoly q⁻¹ n = q⁻¹^(n−1) · qIntPoly q n`.

Proof: `∑_{i<n} q^{−i}` is the same sum read backwards (`Finset.sum_range_reflect`),
and backwards it is `∑_{i<n} q^{i−(n−1)}`, i.e. the forward sum scaled by
`q^{−(n−1)}`.  Only `q ≠ 0` is needed — no `q ≠ 1`, and nothing archimedean. -/
theorem qIntPoly_bar_covariant (q : R) (n : ℕ) (hq : q ≠ 0) :
    qIntPoly q⁻¹ n = q⁻¹ ^ (n - 1) * qIntPoly q n := by
  unfold qIntPoly
  rw [Finset.mul_sum]
  conv_lhs => rw [← Finset.sum_range_reflect]
  refine Finset.sum_congr rfl fun j hj => ?_
  simp only [Finset.mem_range] at hj
  have hsplit : q ^ (n - 1) = q ^ (n - 1 - j) * q ^ j := by
    rw [← pow_add]; congr 1; omega
  rw [inv_pow, inv_pow, eq_comm, inv_mul_eq_div, div_eq_iff (pow_ne_zero _ hq),
      hsplit, ← mul_assoc, inv_mul_cancel₀ (pow_ne_zero _ hq), one_mul]

/-- **The separating statement, in usable contrapositive form.**

If the geometric form were bar-even at `n` — i.e. `qIntPoly q⁻¹ n = qIntPoly q n`
— then the covariance factor `q⁻¹^(n−1)` must act trivially on it.  Combined with
`qIntPoly_bar_covariant`, bar-evenness of the geometric form forces

    `(q⁻¹^(n−1) − 1) · qIntPoly q n = 0`,

so it holds only in the degenerate cases: `n ≤ 1` (where the sum is `0` or `1`),
`q^(n−1) = 1`, or `qIntPoly q n = 0`.  Away from those, the geometric form is
genuinely not bar-even, so it cannot carry a bar-even quantity. -/
theorem qIntPoly_bar_even_forces_degenerate (q : R) (n : ℕ) (hq : q ≠ 0)
    (hbar : qIntPoly q⁻¹ n = qIntPoly q n) :
    (q⁻¹ ^ (n - 1) - 1) * qIntPoly q n = 0 := by
  have h := qIntPoly_bar_covariant q n hq
  rw [hbar] at h
  -- `qIntPoly q n = q⁻¹^(n-1) * qIntPoly q n`, so the bracket annihilates it.
  rw [sub_mul, one_mul, ← h, sub_self]

/-- **The two forms are not interchangeable under bar.**  Concretely at `n = 2`:
balanced is fixed by `σ`, geometric is scaled by `q⁻¹`.  Recorded as the smallest
witness that the distinction is real rather than formal. -/
theorem bar_distinguishes_at_two (q : R) (hq : q ≠ 0) :
    qIntBal q⁻¹ 2 = qIntBal q 2 ∧ qIntPoly q⁻¹ 2 = q⁻¹ * qIntPoly q 2 := by
  refine ⟨qIntBal_bar_even q 2, ?_⟩
  have h := qIntPoly_bar_covariant q 2 hq
  simpa using h

/-! ### Axiom audit — these must depend on nothing but Lean's own axioms. -/

-- #print axioms qIntBal_bar_even
-- #print axioms qIntPoly_bar_covariant
-- #print axioms qIntPoly_bar_even_forces_degenerate
-- #print axioms bar_distinguishes_at_two

/-- Vanishing difference form of bar invariance for balanced quantum integers. -/
theorem qIntBal_bar_sub_eq_zero (q : R) (n : ℕ) :
    qIntBal q⁻¹ n - qIntBal q n = 0 := by
  rw [qIntBal_bar_even q n, sub_self]

end QOU.Mass.QIntegerBarParity
