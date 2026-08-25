/-
# The figure-eight cyclotomic term is bar-invariant — so `1/q₀` is no better than `q₀`

Front (a) of the c₃-carrier programme asked for a fibre carrier built at
`1/q₀ ≈ 0.90092`, on the strength of a claim in PR #5084 that this is *"the only
member of the bar-pair inside the unit disc, which is exactly where a state
integral / q-series converges."*

**That claim is correct for a generic q-series and wrong for the object actually
wanted.** The figure-eight knot's cyclotomic (Habiro / Kashaev) expansion is

    J(4₁; q)  =  Σ_{n ≥ 0} (q;q)_n · (q⁻¹;q⁻¹)_n

and each term involves **both** `q` and `q⁻¹`. This file proves the term is
*exactly* invariant under the bar involution — not merely equal in modulus —
so the divergence is symmetric and neither side of the pair is privileged.

* `fig8Factor_bar_invariant` — the single factor `(1 − qʲ)(1 − q⁻ʲ)` is fixed by
  `q ↦ q⁻¹`. One line: the involution swaps the two brackets.

* `fig8Term_bar_invariant` — hence so is the whole product `T_n(q)`.
  `T_n(q) = T_n(q⁻¹)` for every `n` and every `q`, over any field. Generic
  per §7c: no ordering, no `ℝ`, no archimedean input.

* `fig8Factor_eq_neg_sq_div` — the closed form `(1 − qʲ)(1 − q⁻ʲ) =
  −(qʲ − 1)²/qʲ`, stated without square roots so it stays over a generic field.

* `fig8Factor_nonpos` / `abs_fig8Factor` — over `ℝ` with `0 < q`, every factor is
  `≤ 0` with `|factor| = (qʲ − 1)²/qʲ`. Away from
  `q = 1` that product grows without bound in `n` — and by bar-invariance it
  grows *at the same rate* on both sides of the pair.

**Consequence for front (a), and it is a correction to my own earlier framing.**
Moving the evaluation to `1/q₀` does not rescue the carrier. `HabiroEvaluationTrichotomy`
showed `(q;q)ₙ` behaves differently on the two sides (diverges above 1, tends to
a nonzero limit below); `BarInvolutionDomainObstruction` showed the unit ball is
not bar-stable. Both are true, and both are about the *building block*. The
figure-eight **invariant** contracts those two behaviours into a bar-symmetric
product, and the asymmetry cancels exactly.

So the substrate bar-pair is not "one good side and one bad side" for `J(4₁)`.
It is two equally bad sides, and a state integral — an integral, convergent on
`ℂ ∖ ℝ`, not a series in `q` — is not one route among several but the **only**
route. That is a narrowing of front (a), not a refutation of it.

**Scope-(b), invariant named**: the bar involution fixes each cyclotomic factor,
hence each term, hence `|T_n|`. This excludes *any* choice of evaluation point
within a bar-pair as a way to make the `J(4₁)` series converge. It says nothing
about (H1) `c₃^even = −Vol(4₁)`, and nothing against the state-integral route.

Companion probe: `computations/qbeta/qbeta_fig8_cyclotomic_bar_invariance.py`
(exact invariance to 5.9e-49 at the substrate pair; growth rate → q₀).
-/

import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace QOU.QBeta.Fig8CyclotomicBarInvariance

/-- One factor of the figure-eight cyclotomic term: `(1 − qʲ)(1 − q⁻ʲ)`. -/
def fig8Factor {K : Type*} [Field K] (q : K) (j : ℕ) : K :=
  (1 - q ^ j) * (1 - q⁻¹ ^ j)

/-- The figure-eight cyclotomic term `T_n(q) = ∏_{j=1}^{n} (1 − qʲ)(1 − q⁻ʲ)`,
the `n`-th summand of `J(4₁; q) = Σ_n (q;q)_n (q⁻¹;q⁻¹)_n`. -/
def fig8Term {K : Type*} [Field K] (q : K) : ℕ → K
  | 0 => 1
  | n + 1 => fig8Term q n * fig8Factor q (n + 1)

@[simp] theorem fig8Term_zero {K : Type*} [Field K] (q : K) : fig8Term q 0 = 1 := rfl

@[simp] theorem fig8Term_succ {K : Type*} [Field K] (q : K) (n : ℕ) :
    fig8Term q (n + 1) = fig8Term q n * fig8Factor q (n + 1) := rfl

/-! ## Bar invariance -/

/-- **Each factor is fixed by the bar involution.** The involution `q ↦ q⁻¹`
swaps the two brackets of `(1 − qʲ)(1 − q⁻ʲ)`, and multiplication commutes.

Generic per §7c — any field, and **no** `q ≠ 0` hypothesis is needed: Lean's
`0⁻¹ = 0` makes it hold at `q = 0` too. -/
theorem fig8Factor_bar_invariant {K : Type*} [Field K] (q : K) (j : ℕ) :
    fig8Factor q⁻¹ j = fig8Factor q j := by
  unfold fig8Factor
  rw [inv_inv]
  ring

/-- **The whole term is fixed by the bar involution**, exactly — not merely in
modulus. `T_n(q⁻¹) = T_n(q)` for every `n`.

This is the front-(a) result: for `J(4₁)` the two members of a bar-pair are
interchangeable, so moving the evaluation from `q₀` to `q₀⁻¹` changes nothing. -/
theorem fig8Term_bar_invariant {K : Type*} [Field K] (q : K) :
    ∀ n, fig8Term q⁻¹ n = fig8Term q n := by
  intro n
  induction n with
  | zero => simp
  | succ m ih => rw [fig8Term_succ, fig8Term_succ, ih, fig8Factor_bar_invariant q]

/-! ## The closed form, and the sign -/

/-- `(1 − qʲ)(1 − q⁻ʲ) = −(qʲ − 1)² / qʲ`.

Stated with a division rather than a square root so it remains over a generic
field; the `ℝ`-specific sign consequence is separated out below. -/
theorem fig8Factor_eq_neg_sq_div {K : Type*} [Field K] (q : K) (hq : q ≠ 0) (j : ℕ) :
    fig8Factor q j = -((q ^ j - 1) ^ 2 / q ^ j) := by
  have hqj : q ^ j ≠ 0 := pow_ne_zero _ hq
  unfold fig8Factor
  rw [inv_pow]
  field_simp
  ring

/-- Over `ℝ` with `0 < q`, every factor is `≤ 0`. Archimedean: needs the
ordering, so it takes `ℝ` and sits on that side of the wall. -/
theorem fig8Factor_nonpos {q : ℝ} (hq : 0 < q) (j : ℕ) : fig8Factor q j ≤ 0 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hqj : 0 < q ^ j := pow_pos hq j
  rw [fig8Factor_eq_neg_sq_div q hq0 j]
  have : 0 ≤ (q ^ j - 1) ^ 2 / q ^ j := div_nonneg (sq_nonneg _) (le_of_lt hqj)
  linarith

/-- The modulus of a factor, over `ℝ` with `0 < q`: `|(1 − qʲ)(1 − q⁻ʲ)| =
(qʲ − 1)²/qʲ`, manifestly bar-symmetric via `fig8Factor_bar_invariant`. -/
theorem abs_fig8Factor {q : ℝ} (hq : 0 < q) (j : ℕ) :
    |fig8Factor q j| = (q ^ j - 1) ^ 2 / q ^ j := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hqj : 0 < q ^ j := pow_pos hq j
  rw [abs_of_nonpos (fig8Factor_nonpos hq j), fig8Factor_eq_neg_sq_div q hq0 j]
  ring

/-- **Bar invariance of the modulus**, the form the probe measures (ratio `1.0`
to `5.9e-49` at the substrate pair). Immediate from the exact invariance. -/
theorem abs_fig8Term_bar_invariant (q : ℝ) (n : ℕ) :
    |fig8Term q⁻¹ n| = |fig8Term q n| := by
  rw [fig8Term_bar_invariant q n]

end QOU.QBeta.Fig8CyclotomicBarInvariance
