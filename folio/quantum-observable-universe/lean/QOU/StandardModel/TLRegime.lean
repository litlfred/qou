/-
  The Temperley–Lieb loop weight at real `q` (audit §14, item 4).

  The TL loop weight is `δ = q + q⁻¹`. For real `q > 0`, `δ − 2 = (q − 1)²/q`, so `δ > 2` for
  every real `q ≠ 1`, including the substrate `q₀ ≈ 1.11`. The lattice-to-Virasoro limit of the
  Temperley–Lieb / XXZ chain (Koo–Saleur; Grans-Samuelsson–Jacobsen–Saleur, arXiv 2010.12819)
  is taken with `q` on the unit circle, `|δ| ≤ 2`. At real `q₀` the chain is in the gapped
  `δ > 2` regime, so that construction does not apply there. This is scope (a): a statement about
  that limit, not about the Temperley–Lieb quotient itself, which convention D does select.
  Archimedean (ordered field), so `ℝ`-type hypotheses are needed (§7c).

  -- Ref: [leitner2026] predicted-spectra
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace QOU.TLRegime

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- `q + q⁻¹ − 2 = (q − 1)²/q`. -/
theorem loop_weight_sub_two {q : K} (hq : q ≠ 0) : q + q⁻¹ - 2 = (q - 1) ^ 2 / q := by
  field_simp
  ring

/-- **The loop weight exceeds 2 at every real `q > 0`, `q ≠ 1`.** -/
theorem loop_weight_gt_two {q : K} (hq : 0 < q) (h1 : q ≠ 1) : 2 < q + q⁻¹ := by
  have h := loop_weight_sub_two hq.ne'
  have : 0 < (q - 1) ^ 2 / q := div_pos (by have := sub_ne_zero.mpr h1; positivity) hq
  linarith

end QOU.TLRegime
