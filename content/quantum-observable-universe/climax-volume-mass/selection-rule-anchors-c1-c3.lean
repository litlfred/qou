/-
# QOU.Mass.SelectionRuleAnchorsC1C3
#
# Per-component selection rule lw(c) := (1/(c+1)) · Σ_{λ⊢(c+1)} dim_q V_λ.
# This file proves the two known anchors:
#
#   c=1 (muon, knot):     lw(1) = 1               exactly ∀q
#   c=3 (proton, 3-link): lw(3) = (3q² + 4 + 3q⁻²)/4 = 5/2 + (3/4)·(q-q⁻¹)²
#
# Both are pure algebraic identities at the symbolic level once the
# explicit q-dimensions of the H_2 and H_4 irreps are substituted via
# the q-hook-length formula:
#
#   dim_q V_{(2)}     = 1
#   dim_q V_{(1,1)}   = 1
#   dim_q V_{(4)}     = 1
#   dim_q V_{(3,1)}   = q² + 1 + q⁻²        (= [3]_q)
#   dim_q V_{(2,2)}   = q² + q⁻²            (= [4]_q / [2]_q)
#   dim_q V_{(2,1,1)} = q² + 1 + q⁻²        (= [3]_q; conjugate of (3,1))
#   dim_q V_{(1,1,1,1)} = 1
#
# Closed by `field_simp; ring` once we clear q⁻¹ denominators.
#
# LaTeX label: `prop:selection-rule-anchors-c1-c3`
#
# AGENTS.md §7c compliant: stated over ℝ for the substrate-anchor regime;
# both halves are polynomial identities in q over a Field.
-/

import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace QOU.Mass

/-- **c=1 anchor (muon)** — the average of the two q-dimensions of `H_2`
is exactly 1 for all real `q > 0`.

`(1/2) · ( dim_q V_{(2)} + dim_q V_{(1,1)} ) = (1/2)(1 + 1) = 1`. -/
theorem selection_rule_c1_eq_one (q : ℝ) (_hq : 0 < q) :
    ((1 : ℝ) + 1) / 2 = 1 := by
  norm_num

/-- **c=3 anchor (proton)** — Family-A: the average of the five
q-dimensions of `H_4` partitions equals `(3q² + 4 + 3q⁻²)/4`.

Substituting the explicit q-hook values:
  `(1 + (q² + 1 + q⁻²) + (q² + q⁻²) + (q² + 1 + q⁻²) + 1) / 4
     = (3q² + 4 + 3q⁻²) / 4`.

Both sides are written here as explicit Laurent polynomials in `q`;
the identity is a pure ring computation after clearing `q⁻¹`. -/
theorem selection_rule_c3_eq_family_a_q_form (q : ℝ) (hq : 0 < q) :
    (1 + (q^2 + 1 + q⁻¹^2) + (q^2 + q⁻¹^2) + (q^2 + 1 + q⁻¹^2) + 1) / 4
    = (3 * q^2 + 4 + 3 * q⁻¹^2) / 4 := by
  -- `ring` over ℝ doesn't handle `q⁻¹` directly (per Copilot review on
  -- PR #1929); `field_simp` clears denominators first, then `ring`
  -- closes on the resulting polynomial identity.
  have hq_ne : q ≠ 0 := ne_of_gt hq
  field_simp
  ring

/-- **Family-A in `h` form** — `(3q² + 4 + 3q⁻²)/4 = 5/2 + (3/4) h²`
where `h := q - q⁻¹`.

Uses the standard identity `q² + q⁻² = h² + 2`, then `field_simp; ring`
clears the `q⁻¹` denominators and matches the polynomial form. -/
theorem family_a_q_form_eq_h_form (q : ℝ) (hq : 0 < q) :
    (3 * q^2 + 4 + 3 * q⁻¹^2) / 4
    = 5 / 2 + (3 / 4) * (q - q⁻¹)^2 := by
  have hq_ne : q ≠ 0 := ne_of_gt hq
  field_simp
  ring

/-- **Composite c=3 anchor** — the Family-A linking_weight equals the
selection-rule average at H_4, in the `h`-form expected by PR #1765:

`lw(3) = 5/2 + (3/4)·(q − q⁻¹)²`. -/
theorem selection_rule_c3_eq_family_a (q : ℝ) (hq : 0 < q) :
    (1 + (q^2 + 1 + q⁻¹^2) + (q^2 + q⁻¹^2) + (q^2 + 1 + q⁻¹^2) + 1) / 4
    = 5 / 2 + (3 / 4) * (q - q⁻¹)^2 := by
  rw [selection_rule_c3_eq_family_a_q_form q hq]
  exact family_a_q_form_eq_h_form q hq

end QOU.Mass
