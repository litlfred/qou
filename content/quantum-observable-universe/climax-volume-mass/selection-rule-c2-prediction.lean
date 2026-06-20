/-
# QOU.Mass.SelectionRuleC2Prediction
#
# PR #1765's per-component selection rule
#   lw(c)(q) := (1/(c+1)) · Σ_{λ⊢(c+1)} dim_q V_λ
# applied at c=2 (predicting the 2-component-link case, e.g. Hopf link).
#
# Closed form (proved here):
#   lw(2)(q) = (1 + (q + q⁻¹) + 1) / 3
#           = (2 + q + q⁻¹) / 3
#           = (q+1)² / (3q)
#
# q-dimensions at H_3 (q-hook-length formula):
#   dim_q V_{(3)}     = 1
#   dim_q V_{(2,1)}   = [2]_q = q + q⁻¹
#   dim_q V_{(1,1,1)} = 1
#
# Pure algebraic identity over a Field; closed by field_simp; ring.
#
# LaTeX label: `prop:selection-rule-c2-prediction`
# Cross-reference: `prop:selection-rule-anchors-c1-c3` (the proved anchors).
#
# AGENTS.md §7c compliant: stated over ℝ for the substrate-anchor regime;
# the identity is q-rational at fibre level.
-/

import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.Mass

/-- **Selection rule at c=2 — q-form** (sum of H_3 q-dimensions over 3).

`(1 + (q + q⁻¹) + 1) / 3 = (2 + q + q⁻¹) / 3`. -/
theorem selection_rule_c2_sum_form (q : ℝ) (hq : 0 < q) :
    (1 + (q + q⁻¹) + 1) / 3 = (2 + q + q⁻¹) / 3 := by
  -- `ring` over ℝ doesn't handle `q⁻¹` directly (per Copilot review
  -- on PR #1929); `field_simp` clears denominators first, then `ring`
  -- closes on the resulting polynomial identity. `hq` provides `q ≠ 0`.
  have hq_ne : q ≠ 0 := ne_of_gt hq
  field_simp
  ring

/-- **Selection rule at c=2 — closed form `(q+1)²/(3q)`**.

`(2 + q + q⁻¹) / 3 = (q+1)² / (3q)` for real `q > 0` (equivalently `q ≠ 0`).

This is the algebraic identity supporting the framework's 2-component-link
linking_weight closed form: `lw(c=2) = (q+1)²/(3q)`. -/
theorem selection_rule_c2_eq_closed_form (q : ℝ) (hq : 0 < q) :
    (2 + q + q⁻¹) / 3 = (q + 1)^2 / (3 * q) := by
  have hq_ne : q ≠ 0 := ne_of_gt hq
  field_simp
  ring

/-- **Composite c=2 prediction** — chains the sum-form and closed-form
identities into the full PR #1765 statement:

`(1/3) · Σ_{λ⊢3} dim_q V_λ
   = (dim_q V_(3) + dim_q V_(2,1) + dim_q V_(1,1,1)) / 3
   = (1 + (q + q⁻¹) + 1) / 3
   = (q+1)² / (3q)`. -/
theorem selection_rule_c2_prediction (q : ℝ) (hq : 0 < q) :
    (1 + (q + q⁻¹) + 1) / 3 = (q + 1)^2 / (3 * q) := by
  rw [selection_rule_c2_sum_form q hq]
  exact selection_rule_c2_eq_closed_form q hq

end QOU.Mass
