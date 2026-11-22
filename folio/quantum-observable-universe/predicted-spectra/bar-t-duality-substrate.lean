import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith


/-!
# QOU.Archimedean.bar_t_duality_substrate — Substrate-level bar T-duality

The bar involution q ↦ q⁻¹ on the substrate parameter induces an
involution on the Descartes-family elliptic curves: 𝓔_q ↔ 𝓔_{q⁻¹}.
This is distinct from the X ↔ z target-space T-duality of a single
curve; it acts on the moduli parameter q.

This file abstracts the bar T-duality at the level of (q, x, y)-tuples:
the involution is just q ↦ q⁻¹ on the parameter axis. We prove the
involution is its own inverse and that its fixed locus on ℝ_{>0} is
{1}.

LaTeX label: `prop:bar-t-duality-substrate`

## References

- [leitner2026] §6/bar-t-duality-substrate
- [leitner2026] §6/golden-skew-dual-node
- [leitner2026] §6/bar-self-dual-confinement-band
-/

namespace QOU.Archimedean.BarTDualitySubstrate

/-- The bar involution on the multiplicative group ℝˣ. -/
noncomputable def bar (q : ℝ) : ℝ := q⁻¹

/-- The bar involution is an involution on nonzero reals. -/
-- Ref: [leitner2026] §6/bar-t-duality-substrate
theorem bar_involutive (q : ℝ) (_ : q ≠ 0) : bar (bar q) = q := by
  unfold bar
  exact inv_inv q

/-- Bar fixes 1: bar 1 = 1. -/
-- Ref: [leitner2026] §6/bar-t-duality-substrate
theorem bar_one : bar (1 : ℝ) = 1 := by
  unfold bar
  exact inv_one

/-- Bar maps positives to positives. -/
-- Ref: [leitner2026] §6/bar-t-duality-substrate
theorem bar_pos {q : ℝ} (hq : 0 < q) : 0 < bar q := by
  unfold bar
  exact inv_pos.mpr hq

/-- The unique positive fixed point of bar is 1. -/
-- Ref: [leitner2026] §6/bar-t-duality-substrate
theorem bar_fixed_point_pos {q : ℝ} (hq : 0 < q) :
    bar q = q ↔ q = 1 := by
  unfold bar
  constructor
  · intro h
    have h1 : q * q = 1 := by
      have hne : q ≠ 0 := ne_of_gt hq
      -- From h : q⁻¹ = q, multiply both sides by q: q * q⁻¹ = q * q, then q*q⁻¹ = 1.
      have : q * q⁻¹ = q * q := by rw [h]
      rw [mul_inv_cancel₀ hne] at this
      linarith
    nlinarith [sq_nonneg (q - 1), sq_nonneg (q + 1)]
  · intro h
    rw [h]
    exact inv_one

/-- Bar is order-reversing on positives. -/
-- Ref: [leitner2026] §6/bar-t-duality-substrate
theorem bar_lt_iff {a b : ℝ} (ha : 0 < a) (hb : 0 < b) :
    bar a < bar b ↔ b < a := by
  unfold bar
  exact inv_lt_inv₀ ha hb

/-- A discriminant function f : ℝ → ℝ has a "bar-paired zero locus":
    if f(a) = 0 then (f ∘ bar)(a⁻¹) = 0. This is the abstract content
    of the bar T-duality on discriminants. -/
-- Ref: [leitner2026] §6/bar-t-duality-substrate
theorem bar_paired_zero_locus
    {f : ℝ → ℝ} {a : ℝ} (ha : 0 < a) (hf : f a = 0) :
    (f ∘ bar) (a⁻¹) = 0 := by
  simp only [Function.comp_apply, bar, inv_inv]
  exact hf

/-- **Substrate-level bar T-duality** (Proposition):

    The bar involution bar : ℝ → ℝ on the substrate parameter is
    self-inverse, fixes 1, and is order-reversing on positives.
    Any zero of a "discriminant" function f at q = a is bar-paired
    to a zero of f ∘ bar at q = a⁻¹. -/
-- Ref: [leitner2026] §6/bar-t-duality-substrate
theorem bar_t_duality_substrate :
    (∀ q : ℝ, q ≠ 0 → bar (bar q) = q) ∧
    bar 1 = 1 ∧
    (∀ a b : ℝ, 0 < a → 0 < b → (bar a < bar b ↔ b < a)) ∧
    (∀ {f : ℝ → ℝ} {a : ℝ}, 0 < a → f a = 0 → (f ∘ bar) (a⁻¹) = 0) :=
  ⟨bar_involutive, bar_one,
    fun _ _ ha hb => bar_lt_iff ha hb,
    fun ha hf => bar_paired_zero_locus ha hf⟩

end QOU.Archimedean.BarTDualitySubstrate
