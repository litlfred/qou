import Mathlib.Tactic
import QOU.MathlibExt.QIntegerCanonical
import QOU.Mass.QHookDimensionBalanced

/-!
# QOU.Eightfold.OcneanuTwoThreeNotProportional — the `N=2` and `N=3` weight ratios differ

Bean `qou-bhfg`. Companion to
`docs/audits/2026-08-25-n3-exclusion-provenance-audit.md` (route 3).

## What this closes

One of the seven `N = 3` exclusions is *"re-tune the Ocneanu parameter to
`N = 3`"*, excluded because **the `N=2` and `N=3` traces are not proportional**.
Its source
(`docs/audits/2026-08-07-two-row-projection-is-the-pairwise-cap.md`) supplies the
closed form

    y_{(2,1)} / y_{(3)}  =  q [2]_q [N−1]_q / [N+2]_q

and then concludes non-proportionality because the ratio *"differs at every `q`
tested"*. **The formula is symbolic; that last step was sampling.** A provenance
audit that reports the row as resting on exact algebra should not leave the
inference resting on a finite sample, so it is proved here instead.

## The identity

At `N = 2` the ratio is `q [2]_q [1]_q / [4]_q`; at `N = 3` it is
`q [2]_q [2]_q / [5]_q`. Cancelling the common nonzero `q [2]_q`, they agree iff
`[1]_q [5]_q = [2]_q [4]_q`. And there is an exact identity:

    [2]_q [4]_q  −  [1]_q [5]_q  =  [3]_q

(an instance of `[a][b] − [a−1][b+1] = [b−a+1]`). So the two ratios agree **iff
`[3]_q = 0`** — a single, checkable condition, rather than a sample.

`qb_three_eq` gives `[3]_q = q² + 1 + q⁻²`, so over an ordered field the
condition fails outright; that discharge is `QOU.Archimedean.OcneanuTwoThreeSubstrate`,
kept separate per §7c. Nothing in this file mentions `ℝ` or an ordering.

## Scope

This is an identity about `q`-brackets and the quoted ratio formula. It does
**not** re-derive the ratio formula itself from the Hecke weights — that is the
source audit's, consumed here as the definition of what is being compared. It
therefore strengthens the exclusion's *stated reason* from sampled to proved,
and claims nothing further about `N = 3`.

-- Ref: [kassel1995] Ch. VI (`q`-integers and their product identities).
-/

namespace QOU.Eightfold.OcneanuTwoThreeNotProportional

variable {R : Type*} [Field R]

/-- The balanced `q`-integer `[n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹)`, the convention in
which `[2]_q = q + q⁻¹` (AGENTS.md §7aa).

> **This duplicates the canonical `QOU.QInteger.qIntBal`** and is kept only so
> the proofs below can `simp [qb]` down to the literal body, exactly as
> `QOU.BraidKnot.AJTrefoil.qInt` is kept for the same reason. The consolidation
> is the equation `qb_eq_canonical` immediately below: same function, one
> canonical meaning, no proof touched. Flagged on PR #5746 by the agent working
> bean `qou-qint`, which is actively bridging duplicate `q`-integer definitions
> — this file was written without checking for one, and would otherwise have
> been another. -/
noncomputable def qb (q : R) (n : ℕ) : R := (q ^ n - (q ^ n)⁻¹) / (q - q⁻¹)

/-- **The consolidation.** `qb` is the canonical balanced `q`-integer. The two
bodies differ only by `q⁻¹ ^ n` versus `(q ^ n)⁻¹`, which `inv_pow` identifies. -/
theorem qb_eq_canonical (q : R) (n : ℕ) : qb q n = QOU.QInteger.qIntBal q n := by
  simp [qb, inv_pow]

/-- The `q`-bracket denominator is nonzero exactly when `q² ≠ 1` — which is, by
`QOU.Eightfold.HeckeBraidingNonSymmetric.double_braiding_eq_one_iff`, exactly
the condition that the braiding is **not** symmetric. The `q`-integers are
well-defined precisely on the non-symmetric locus. -/
theorem sub_inv_ne_zero (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) : q - q⁻¹ ≠ 0 :=
  QOU.Mass.QHookDimensionBalanced.sub_inv_ne_zero hq hq2

/-- `[2]_q = q + q⁻¹` — the convention-fixing case (AGENTS.md §7aa). -/
theorem qb_two_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    qb q 2 = q + q⁻¹ := by
  rw [qb, div_eq_iff (sub_inv_ne_zero q hq hq2)]; field_simp; ring

/-- `[3]_q = q² + 1 + q⁻²`. This is the quantity the whole comparison reduces
to, so it is worth having in expanded form. -/
theorem qb_three_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    qb q 3 = q ^ 2 + 1 + (q ^ 2)⁻¹ := by
  rw [qb, div_eq_iff (sub_inv_ne_zero q hq hq2)]; field_simp; ring

/-- `[4]_q = q³ + q + q⁻¹ + q⁻³`. -/
theorem qb_four_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    qb q 4 = q ^ 3 + q + q⁻¹ + (q ^ 3)⁻¹ := by
  rw [qb, div_eq_iff (sub_inv_ne_zero q hq hq2)]; field_simp; ring

/-- `[5]_q = q⁴ + q² + 1 + q⁻² + q⁻⁴`. -/
theorem qb_five_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    qb q 5 = q ^ 4 + q ^ 2 + 1 + (q ^ 2)⁻¹ + (q ^ 4)⁻¹ := by
  rw [qb, div_eq_iff (sub_inv_ne_zero q hq hq2)]; field_simp; ring

/-- **The general shift identity.** `[n+1]_q [n+3]_q − [n]_q [n+4]_q = [3]_q`
for **every** `n` — the right-hand side does not depend on `n`.

This is the statement the exclusion actually wants. Comparing the Ocneanu weight
ratio at `N` and at `N+1` reduces to this cross-product difference, and it is
`[3]_q` at every `N`. So re-tuning does not fail to reproduce the `N = 2`
weighting *only* at `N = 3`: **every** adjacent pair of `N` re-weights, and
always by the same amount. -/
theorem qb_shift_identity (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ) :
    qb q (n + 1) * qb q (n + 3) - qb q n * qb q (n + 4) = qb q 3 := by
  have hd : q - q⁻¹ ≠ 0 := sub_inv_ne_zero q hq hq2
  have hpn : q ^ n ≠ 0 := pow_ne_zero _ hq
  have e1 : q ^ (n + 1) = q ^ n * q ^ 1 := pow_add q n 1
  have e3 : q ^ (n + 3) = q ^ n * q ^ 3 := pow_add q n 3
  have e4 : q ^ (n + 4) = q ^ n * q ^ 4 := pow_add q n 4
  simp only [qb, e1, e3, e4, div_mul_div_comm, div_sub_div_same]
  rw [div_eq_div_iff (mul_ne_zero hd hd) hd]
  field_simp
  ring

/-- **The identity.** `[2]_q [4]_q − [1]_q [5]_q = [3]_q`.

This is what replaces *"differs at every `q` tested"*: the discrepancy between
the two weight ratios is not merely nonzero on a sample, it is exactly `[3]_q`. -/
theorem qb_two_four_sub_one_five (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    qb q 2 * qb q 4 - qb q 1 * qb q 5 = qb q 3 :=
  qb_shift_identity q hq hq2 1

/-- **The gate.** The `N=2` and `N=3` Ocneanu weight ratios are equal **iff**
`[3]_q = 0`.

Stated as an `iff` deliberately: it says exactly what would have to happen for
the two traces to be proportional, rather than asserting they are not. The
archimedean file rules the right-hand side out. -/
theorem ratio_eq_iff_qb_three_eq_zero (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (h2 : qb q 2 ≠ 0) (h4 : qb q 4 ≠ 0) (h5 : qb q 5 ≠ 0) :
    q * qb q 2 * qb q 1 / qb q 4 = q * qb q 2 * qb q 2 / qb q 5 ↔ qb q 3 = 0 := by
  have hid := qb_two_four_sub_one_five q hq hq2
  have hne : q * qb q 2 ≠ 0 := mul_ne_zero hq h2
  rw [div_eq_div_iff h4 h5]
  constructor
  · intro h
    have hc : qb q 2 * qb q 4 - qb q 1 * qb q 5 = 0 := by
      apply mul_left_cancel₀ hne
      linear_combination -h
    linear_combination hc - hid
  · intro h3
    linear_combination (-(q * qb q 2)) * hid - (q * qb q 2) * h3

end QOU.Eightfold.OcneanuTwoThreeNotProportional
