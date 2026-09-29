/-
# Block dominance exchange forces a sign crossing

Formalisation of the *structural* content of the ≥3-row signed-trace sign
crossing measured in PR #4829 / #4832 (bean `qou-prjo`).

## What is being formalised (and what is NOT)

The probe studies, for a nuclide braid `β_K` and the PROVED value-only weight
`Δ_λ = (−1)^{n(λ)}·dim V_λ` (`QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional`),

  `F_K(q) = Σ_{λ ⊢ 3A, ℓ(λ) ≥ 3} y_λ(q) · χ^λ(β_K;q) · Δ_λ`

and finds, for the deuteron (`n = 6`), that `F_D` is positive just above `q = 1`
and negative at the substrate `q₀`, with the change driven by a *two-block
overtake*: near `q = 1` the total is set by the `(4,1,1)` block (`Δ = −10`, term
positive), while by `q₀` the `(3,2,1)` block (`Δ = +16`, the largest `|Δ_λ|` in
the ≥3-row stratum of 6, term negative) has overtaken it.

**This file proves exactly that implication and nothing more.**  It takes the
per-block dominance data as *hypotheses* and derives the existence (and, under a
monotone-ratio hypothesis, the uniqueness) of the crossing.  It does **not**
assert the hypotheses: the numerical values of `y_λ` and `χ^λ` are f64
computations living in the probe, not in Lean.  Per AGENTS.md
§"Conditional-proved ≠ premise-established", a reader may cite these theorems as
*"a dominance exchange forces a zero"* and may **not** cite them as evidence
that the deuteron numbers are what the probe says they are.

Nothing here is a binding-energy statement: `F_K` is value-only, and the
extensive super-pairwise magnitude term remains open (bean `qou-prjo`).

## Base ring

`ℝ` throughout, and genuinely so (§7c): both results are archimedean — they use
the order structure and the intermediate value theorem, which have no
counterpart over a generic `CommRing`.
-/
import Mathlib.Topology.Instances.Real.Lemmas
import Mathlib.Topology.Order.IntermediateValue
import Mathlib.Algebra.Order.Field.Basic

namespace QOU.BraidsAndKnots

open Set

/-- **Block dominance exchange forces a zero.**

Let `F = T₁ + T₂ + R` be a continuous function split into two distinguished
blocks and a remainder.  Suppose that

* at the left endpoint `a` the first block is positive and **dominates**
  everything else: `|T₂ a + R a| < T₁ a`;
* at the right endpoint `b` the second block is negative and **dominates**
  everything else: `|T₁ b + R b| < -T₂ b`.

Then `F` vanishes somewhere strictly between `a` and `b`.

This is the exact shape of the measured deuteron data: `T₁` is the `(4,1,1)`
term, `T₂` the `(3,2,1)` term, and `R` the remaining ≥3-row blocks.  The
hypotheses are falsifiable statements about those numbers — dropping either
dominance hypothesis makes the conclusion fail (a positive `F` with a merely
*larger* negative block elsewhere need not vanish). -/
theorem sign_crossing_of_block_dominance_exchange
    {a b : ℝ} (hab : a ≤ b) {F T₁ T₂ R : ℝ → ℝ}
    (hsplit : ∀ q, F q = T₁ q + T₂ q + R q)
    (hcont : ContinuousOn F (Icc a b))
    (ha_dom : |T₂ a + R a| < T₁ a)
    (hb_dom : |T₁ b + R b| < -T₂ b) :
    ∃ c ∈ Ioo a b, F c = 0 := by
  -- `F a > 0`: the first block outweighs the rest at `a`.
  have hFa : 0 < F a := by
    have h := (abs_lt.mp ha_dom).1
    have : F a = T₁ a + (T₂ a + R a) := by rw [hsplit]; ring
    rw [this]; linarith
  -- `F b < 0`: the second block outweighs the rest at `b`.
  have hFb : F b < 0 := by
    have h := (abs_lt.mp hb_dom).2
    have : F b = T₂ b + (T₁ b + R b) := by rw [hsplit]; ring
    rw [this]; linarith
  -- Intermediate value theorem on the decreasing side.
  have hmem : (0 : ℝ) ∈ Ioo (F b) (F a) := ⟨hFb, hFa⟩
  obtain ⟨c, hc, hFc⟩ := intermediate_value_Ioo' hab hcont hmem
  exact ⟨c, hc, hFc⟩

/-- **The crossing is unique when the block ratio is strictly monotone.**

In the two-block regime (`F = T₁ + T₂` with `T₁ > 0` and `T₂ < 0` throughout),
write the *overtake ratio* `r = (-T₂)/T₁`.  Then `F q = 0` exactly when
`r q = 1`, so if `r` is strictly monotone on `[a, b]` the crossing is unique.

This is the formal content of the word "overtake": the second block does not
merely become large, it grows *relative to* the first, and it does so
monotonically, so it crosses the first exactly once. -/
theorem crossing_unique_of_strictMonoOn_ratio
    {a b : ℝ} {T₁ T₂ : ℝ → ℝ}
    (hT₁ : ∀ q ∈ Icc a b, 0 < T₁ q)
    (hmono : StrictMonoOn (fun q => (-T₂ q) / T₁ q) (Icc a b)) :
    ∀ c ∈ Icc a b, ∀ d ∈ Icc a b,
      T₁ c + T₂ c = 0 → T₁ d + T₂ d = 0 → c = d := by
  intro c hc d hd hzc hzd
  -- At a zero of `T₁ + T₂` the ratio equals `1`.
  have key : ∀ x ∈ Icc a b, T₁ x + T₂ x = 0 → (-T₂ x) / T₁ x = 1 := by
    intro x hx hzx
    have hpos := hT₁ x hx
    have : -T₂ x = T₁ x := by linarith
    rw [this, div_self (ne_of_gt hpos)]
  have hrc := key c hc hzc
  have hrd := key d hd hzd
  -- A strictly monotone function is injective on the set.
  exact hmono.injOn hc hd (by rw [hrc, hrd])

/-- **Sign of a two-block sum is the sign of `1 − r`.**

The companion readout used by the probe: with `T₁ > 0`, the sum `T₁ + T₂` is
negative precisely when the overtake ratio `r = (-T₂)/T₁` exceeds `1`.  This is
what makes "the `(3,2,1)` block has overtaken `(4,1,1)`" and "the total has gone
negative" the *same* statement rather than two correlated observations. -/
theorem two_block_neg_iff_ratio_gt_one
    {t₁ t₂ : ℝ} (ht₁ : 0 < t₁) :
    t₁ + t₂ < 0 ↔ 1 < (-t₂) / t₁ := by
  rw [lt_div_iff₀ ht₁, one_mul]
  constructor <;> intro h <;> linarith

end QOU.BraidsAndKnots
