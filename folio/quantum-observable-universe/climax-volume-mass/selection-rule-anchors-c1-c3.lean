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
# AGENTS.md §7c: both halves are polynomial identities in q over a Field,
# as this docstring already observed — so the file is now stated over a
# generic `{R : Type*} [Field R] [CharZero R]`, not over ℝ.
#
# `[CharZero R]` is required, not decorative: every anchor divides by 4
# (and by 2), so `field_simp` needs `(4 : R) ≠ 0`. A port to plain
# `[Field R]` leaves those goals unsolved.
#
# The old hypothesis `0 < q` was never used as an ordering — each proof
# consumed it only through `ne_of_gt` to obtain `q ≠ 0` for `field_simp`.
# It is therefore replaced by the weaker, order-free `q ≠ 0`, which
# strengthens all three anchors. The archimedean substrate evaluation is
# the instantiation `R := ℝ` at `q := q₀`.
-/

import Mathlib.Algebra.Field.Basic
import QOU.Mass.QHookDimension
import Mathlib.Algebra.Order.Ring.Cast
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace QOU.Mass

variable {R : Type*} [Field R] [CharZero R]

/-- **c=1 anchor (muon)** — the average of the two q-dimensions of `H_2`
is exactly 1, at every `q` and over any base field.

`(1/2) · ( dim_q V_{(2)} + dim_q V_{(1,1)} ) = (1/2)(1 + 1) = 1`.

The `q` argument is retained for uniformity with the c=3 anchors but is
genuinely unused: both `H_2` q-dimensions are the constant 1, so the
statement carries no `q` at all. -/
theorem selection_rule_c1_eq_one (_q : R) :
    ((1 : R) + 1) / 2 = 1 := by
  norm_num

/-- **c=3 anchor (proton)** — Family-A: the average of the five
q-dimensions of `H_4` partitions equals `(3q² + 4 + 3q⁻²)/4`.

Substituting the explicit q-hook values:
  `(1 + (q² + 1 + q⁻²) + (q² + q⁻²) + (q² + 1 + q⁻²) + 1) / 4
     = (3q² + 4 + 3q⁻²) / 4`.

Both sides are written here as explicit Laurent polynomials in `q`;
the identity is a pure ring computation after clearing `q⁻¹`. -/
theorem selection_rule_c3_eq_family_a_q_form (q : R) (hq : q ≠ 0) :
    (1 + (q^2 + 1 + q⁻¹^2) + (q^2 + q⁻¹^2) + (q^2 + 1 + q⁻¹^2) + 1) / 4
    = (3 * q^2 + 4 + 3 * q⁻¹^2) / 4 := by
  -- `ring` over ℝ doesn't handle `q⁻¹` directly (per Copilot review on
  -- PR #1929); `field_simp` clears denominators first, then `ring`
  -- closes on the resulting polynomial identity.
  have hq_ne : q ≠ 0 := hq
  field_simp
  ring

/-- **Family-A in `h` form** — `(3q² + 4 + 3q⁻²)/4 = 5/2 + (3/4) h²`
where `h := q - q⁻¹`.

Uses the standard identity `q² + q⁻² = h² + 2`, then `field_simp; ring`
clears the `q⁻¹` denominators and matches the polynomial form. -/
theorem family_a_q_form_eq_h_form (q : R) (hq : q ≠ 0) :
    (3 * q^2 + 4 + 3 * q⁻¹^2) / 4
    = 5 / 2 + (3 / 4) * (q - q⁻¹)^2 := by
  have hq_ne : q ≠ 0 := hq
  field_simp
  ring

/-- **Composite c=3 anchor** — the Family-A linking_weight equals the
selection-rule average at H_4, in the `h`-form expected by PR #1765:

`lw(3) = 5/2 + (3/4)·(q − q⁻¹)²`. -/
theorem selection_rule_c3_eq_family_a (q : R) (hq : q ≠ 0) :
    (1 + (q^2 + 1 + q⁻¹^2) + (q^2 + q⁻¹^2) + (q^2 + 1 + q⁻¹^2) + 1) / 4
    = 5 / 2 + (3 / 4) * (q - q⁻¹)^2 := by
  rw [selection_rule_c3_eq_family_a_q_form q hq]
  exact family_a_q_form_eq_h_form q hq

/-! ## Derived from the hook-length formula (bean `qou-lx7k`, 2026-08-29)

Everything above is an arithmetic identity over q-dimension values substituted by
hand: no partition, hook length or `dim_q` occurs in any of those *statements*,
and the hook-length step lived in the docstrings.  The theorems are true and are
kept; what was missing was the derivation of their left-hand sides.

`QOU.Mass.QHookDimension` supplies it — shape → conjugate → hook lengths →
`[n]_q!` over the hooks' q-integers, with each shape's hook multiset settled by
`decide`.  The two anchors below are the statements this block's `.md` describes,
now resting on that formula rather than on a substitution. -/

theorem selection_rule_c1_anchor_derived {K : Type*} [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] {q : K} (hq : 0 < q) :
    (dimQ q [2] + dimQ q [1, 1]) / 2 = 1 :=
  selection_rule_c1_real hq

theorem selection_rule_c3_anchor_derived {K : Type*} [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] {q : K} (hq : 0 < q) :
    (dimQ q [4] + dimQ q [3, 1] + dimQ q [2, 2] + dimQ q [2, 1, 1]
       + dimQ q [1, 1, 1, 1]) / 4
      = 5 / 2 + (3 / 4) * (q - q⁻¹) ^ 2 :=
  selection_rule_c3_real hq

end QOU.Mass
