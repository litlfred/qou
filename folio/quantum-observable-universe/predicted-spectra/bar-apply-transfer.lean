import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp


/-!
# QOU.Archimedean.bar_apply_transfer — Bar-transfer principle

Generic transfer lemma: a property P bar-invariant on ℝ_{>0}
(P(q) ↔ P(q⁻¹)) satisfies the equivalence
  (∀ q > a, P(q)) ↔ (∀ q ∈ (0, a⁻¹), P(q)).
This halves the proof obligation for every bar-invariant predicate.

LaTeX label: `prop:bar-apply-transfer`

## References

- [leitner2026] §6/bar-apply-transfer
- [leitner2026] §6/bar-self-dual-confinement-band
-/

namespace QOU.Archimedean.BarApplyTransfer

/-- A property is **bar-invariant** if P(q) ↔ P(q⁻¹) for every q > 0. -/
def BarInvariant (P : ℝ → Prop) : Prop :=
  ∀ q : ℝ, 0 < q → (P q ↔ P q⁻¹)

/-- **Lower-bound transfer**: for a bar-invariant property,
    "P holds for all q > a" is equivalent to
    "P holds for all q ∈ (0, a⁻¹)". -/
-- Ref: [leitner2026] §6/bar-apply-transfer
theorem lower_bound_transfer
    {P : ℝ → Prop} (hP : BarInvariant P) {a : ℝ} (ha : 0 < a) :
    (∀ q : ℝ, a < q → P q) ↔ (∀ q : ℝ, 0 < q → q < a⁻¹ → P q) := by
  constructor
  · intro h q hq hqa
    have hqi : 0 < q⁻¹ := inv_pos.mpr hq
    have h1 : a < q⁻¹ := by
      rw [lt_inv_comm₀ ha hq]; exact hqa
    have hPi : P q⁻¹ := h q⁻¹ h1
    exact (hP q hq).mpr hPi
  · intro h q hqa
    have hq : 0 < q := lt_trans ha hqa
    have hqi : 0 < q⁻¹ := inv_pos.mpr hq
    have h1 : q⁻¹ < a⁻¹ := by
      have := (inv_lt_inv₀ hq ha).mpr hqa
      simpa using this
    have hPi : P q⁻¹ := h q⁻¹ hqi h1
    exact (hP q hq).mpr hPi

/-- A simpler form of the transfer lemma that avoids the iff:
    if P holds on (a, ∞) and P is bar-invariant, then P holds on
    (0, a⁻¹) (positive part). -/
-- Ref: [leitner2026] §6/bar-apply-transfer
theorem bar_apply_lower
    {P : ℝ → Prop} (hP : BarInvariant P) {a : ℝ} (ha : 0 < a)
    (h : ∀ q : ℝ, a < q → P q) :
    ∀ q : ℝ, 0 < q → q < a⁻¹ → P q := by
  intro q hq hqa
  have hqi : 0 < q⁻¹ := inv_pos.mpr hq
  have h1 : a < q⁻¹ := by
    rw [lt_inv_comm₀ ha hq]; exact hqa
  have hPi : P q⁻¹ := h q⁻¹ h1
  exact (hP q hq).mpr hPi

/-- **Negation transfer**: a counterexample to P at q < a (with q > 0)
    transports along bar to a counterexample at q⁻¹ > a⁻¹. -/
-- Ref: [leitner2026] §6/bar-apply-transfer
theorem neg_transfer
    {P : ℝ → Prop} (hP : BarInvariant P) {a q : ℝ}
    (ha : 0 < a) (hq : 0 < q) (hqa : q < a) (hnotP : ¬ P q) :
    ¬ P q⁻¹ ∧ a⁻¹ < q⁻¹ := by
  refine ⟨fun h => hnotP ?_, ?_⟩
  · exact (hP q hq).mpr h
  · exact (inv_lt_inv₀ ha hq).mpr hqa

/-- **Bar-transfer principle** (Proposition):

    Combines the lower-bound transfer and the negation transfer
    into the headline statement. -/
-- Ref: [leitner2026] §6/bar-apply-transfer
theorem bar_apply_transfer
    {P : ℝ → Prop} (hP : BarInvariant P) {a : ℝ} (ha : 0 < a) :
    (∀ q : ℝ, a < q → P q) ↔ (∀ q : ℝ, 0 < q → q < a⁻¹ → P q) :=
  lower_bound_transfer hP ha

end QOU.Archimedean.BarApplyTransfer
