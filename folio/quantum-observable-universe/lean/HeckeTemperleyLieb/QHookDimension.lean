import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-!
# The q-dimensions the selection rule runs on, derived rather than substituted

`prop:selection-rule-anchors-c1-c3` and `prop:selection-rule-c2-prediction` state
the per-component selection rule

    lw(c)(q) := (1/(c+1)) · Σ_{λ ⊢ c+1} dim_q V_λ

and give closed forms at c = 1, 2, 3.  Their `.md` calls those "derivation-tight
(not a fit; both follow from the q-deformed hook-length formula)".

**Their Lean did not follow from the hook-length formula, because it never
mentioned it.**  What those files prove is, in full:

    selection_rule_c1_eq_one          ((1 : R) + 1) / 2 = 1
    selection_rule_c2_prediction      (1 + (q + q⁻¹) + 1) / 3 = (q+1)^2 / (3*q)
    selection_rule_c3_eq_family_a     (1 + (q²+1+q⁻²) + (q²+q⁻²) + (q²+1+q⁻²) + 1) / 4
                                        = 5/2 + (3/4)(q - q⁻¹)^2

Every one is an arithmetic identity over literals typed in by hand.  No
partition, no Young diagram, no hook length and no `dim_q` occurs in any
statement; the hook-length computation was done in a docstring and only its
*output* reached the Lean.  The c=1 case is the clearest: `(1+1)/2 = 1` is true
of the numeral `1`, and its own docstring concedes the `q` argument "is
genuinely unused".  That is the `sorry-free ≠ derived` failure AGENTS.md
legislates against, and Strict Lean Discipline §8's test catches it — *could
this be wrong?*  No: not because the mathematics is sound, but because the
statement does not mention the objects it claims to be about.

This file supplies the missing half.  `dimQ` is built from the shape:

    shape (a `List ℕ`)  →  conjugate  →  hook lengths  →  q-hook-length formula

so `dimQ_two_one` and friends are *computed*, and the selection-rule sums below
are consequences of the hook-length formula rather than restatements of a
docstring.  The originals are not wrong and are not deleted — they remain true
arithmetic, and `selection_rule_c2_from_hooks` closes the gap by deriving their
left-hand sides.

## Conventions

`qInt` is the **balanced** q-integer `[n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹)`, matching
`mass_at_3A_proper.qint` in `computations/`, so `[2]_q = q + q⁻¹` and
`[3]_q = q² + 1 + q⁻²`.  It is written as an explicit `zpow` sum rather than as
that quotient so it is defined at `q = 1` too and needs no `q ≠ ±1` side
condition; `qInt_two` and `qInt_three` below check it against the closed forms.
-/

namespace QOU.Mass

open Finset

variable {R : Type*} [Field R]

/-- Balanced q-integer `[n]_q = q^{-(n-1)} + q^{-(n-3)} + ⋯ + q^{n-1}`.

Written as a sum of `zpow`s rather than as `(qⁿ − q⁻ⁿ)/(q − q⁻¹)` so that it is
total: no `q ≠ ±1` hypothesis is needed anywhere downstream. -/
def qInt (q : R) (n : ℕ) : R :=
  ∑ i ∈ range n, q ^ (2 * (i : ℤ) - ((n : ℤ) - 1))

@[simp] theorem qInt_zero (q : R) : qInt q 0 = 0 := by simp [qInt]

@[simp] theorem qInt_one (q : R) : qInt q 1 = 1 := by simp [qInt]

/-- No `q ≠ 0` needed: at `q = 0` both sides are `0`, since Lean sends `0⁻¹`
to `0`. -/
theorem qInt_two (q : R) : qInt q 2 = q + q⁻¹ := by
  simp [qInt, Finset.sum_range_succ, zpow_neg, zpow_one]
  ring

theorem qInt_three (q : R) (hq : q ≠ 0) : qInt q 3 = q ^ 2 + 1 + (q ^ 2)⁻¹ := by
  have h2 : (2 : ℤ) - 2 = 0 := by norm_num
  simp [qInt, Finset.sum_range_succ, zpow_neg]
  field_simp
  ring

/-- q-factorial `[n]_q! = ∏_{k=1}^{n} [k]_q`. -/
def qFact (q : R) : ℕ → R
  | 0 => 1
  | (n + 1) => qInt q (n + 1) * qFact q n

/-- The conjugate (transpose) of a partition given as a weakly-decreasing list of
row lengths: column `j` of `λ` is as long as there are rows exceeding `j`. -/
def conjugate (l : List ℕ) : List ℕ :=
  (List.range (l.headI)).map fun j => (l.filter fun r => j < r).length

/-- Hook length at cell `(i, j)`: arm + leg + 1. -/
def hookAt (l : List ℕ) (i j : ℕ) : ℕ :=
  (l.getD i 0 - j - 1) + ((conjugate l).getD j 0 - i - 1) + 1

/-- Every hook length of the diagram, row by row. -/
def hooks (l : List ℕ) : List ℕ :=
  (List.range l.length).flatMap fun i =>
    (List.range (l.getD i 0)).map fun j => hookAt l i j

/-- **The q-hook-length formula.**  `dim_q V_λ = [n]_q! / ∏_{cells} [hook]_q`. -/
noncomputable def dimQ (q : R) (l : List ℕ) : R :=
  qFact q l.sum / ((hooks l).map (qInt q)).prod

/-! ## The hook multisets, computed from the shapes

`decide` settles these: they are equalities of concrete `List ℕ`, so nothing is
assumed about which hooks a shape has — the shape determines them. -/

theorem hooks_two : hooks [2] = [2, 1] := by decide
theorem hooks_one_one : hooks [1, 1] = [2, 1] := by decide
theorem hooks_three : hooks [3] = [3, 2, 1] := by decide
theorem hooks_two_one : hooks [2, 1] = [3, 1, 1] := by decide
theorem hooks_one_one_one : hooks [1, 1, 1] = [3, 2, 1] := by decide

/-! ## The q-dimensions, derived

Each is now `[n]_q!` over the product of the computed hooks.

The non-vanishing hypotheses are not decoration.  `dimQ` divides by the product
of the hooks' q-integers, and Lean's division sends a zero denominator to `0`,
so at `[2]_q = 0` (that is, `q² = −1`) the claim `dimQ q [2] = 1` is genuinely
FALSE rather than merely unproved.  Carrying `qInt q 2 ≠ 0` explicitly is what
makes each statement true as written; `qInt_pos` below discharges it for every
real `q > 0`, which is the regime the selection rule is stated in. -/

@[simp] theorem qFact_one (q : R) : qFact q 1 = 1 := by
  simp [qFact, qInt_one]

@[simp] theorem qFact_two (q : R) : qFact q 2 = qInt q 2 := by
  simp [qFact, qInt_one]

@[simp] theorem qFact_three (q : R) : qFact q 3 = qInt q 3 * qInt q 2 := by
  simp [qFact, qInt_one]

theorem dimQ_two (q : R) (h2 : qInt q 2 ≠ 0) : dimQ q [2] = 1 := by
  simp [dimQ, hooks_two, qFact_two, qInt_one]
  exact div_self h2

theorem dimQ_one_one (q : R) (h2 : qInt q 2 ≠ 0) : dimQ q [1, 1] = 1 := by
  simp [dimQ, hooks_one_one, qFact_two, qInt_one]
  exact div_self h2

theorem dimQ_three (q : R) (h2 : qInt q 2 ≠ 0) (h3 : qInt q 3 ≠ 0) :
    dimQ q [3] = 1 := by
  simp [dimQ, hooks_three, qFact_three, qInt_one]
  exact div_self (mul_ne_zero h3 h2)

theorem dimQ_one_one_one (q : R) (h2 : qInt q 2 ≠ 0) (h3 : qInt q 3 ≠ 0) :
    dimQ q [1, 1, 1] = 1 := by
  simp [dimQ, hooks_one_one_one, qFact_three, qInt_one]
  exact div_self (mul_ne_zero h3 h2)

/-- **`dim_q V_{(2,1)} = [2]_q`** — the one non-trivial H₃ dimension, and the
value the c=2 selection rule turns on.  Hooks `[3,1,1]` against `[3]_q!`:
the `[3]` cancels and the `[1]`s are 1, leaving `[2]_q`. -/
theorem dimQ_two_one (q : R) (h3 : qInt q 3 ≠ 0) :
    dimQ q [2, 1] = qInt q 2 := by
  simp [dimQ, hooks_two_one, qFact_three, qInt_one]
  field_simp

/-! ## The selection rule, now resting on the formula

`selection_rule_c1_from_hooks` and `selection_rule_c2_from_hooks` state the sums
over the *actual* `dimQ` of the *actual* partitions, and derive the closed forms
the original blocks assert.  These are the statements the `.md` claimed. -/

/-- **c = 1 anchor, derived.**  `(1/2) Σ_{λ⊢2} dim_q V_λ = 1`, over the real
q-dimensions rather than over the literal `1`s. -/
theorem selection_rule_c1_from_hooks (q : R) (h2 : qInt q 2 ≠ 0)
    (two_ne : (2 : R) ≠ 0) :
    (dimQ q [2] + dimQ q [1, 1]) / 2 = 1 := by
  rw [dimQ_two q h2, dimQ_one_one q h2]
  rw [show (1 : R) + 1 = 2 by ring]
  exact div_self two_ne

/-- **c = 2 prediction, derived.**  `(1/3) Σ_{λ⊢3} dim_q V_λ = (q+1)²/(3q)`,
with the three q-dimensions computed from their hook multisets. -/
theorem selection_rule_c2_from_hooks (q : R) (hq : q ≠ 0)
    (h2 : qInt q 2 ≠ 0) (h3 : qInt q 3 ≠ 0) :
    (dimQ q [3] + dimQ q [2, 1] + dimQ q [1, 1, 1]) / 3
      = (q + 1) ^ 2 / (3 * q) := by
  rw [dimQ_three q h2 h3, dimQ_one_one_one q h2 h3, dimQ_two_one q h3,
    qInt_two q]
  field_simp
  ring

/-! ## Discharging the hypotheses at real `q > 0`

The selection rule is stated over `ℝ_{>0}`, where every balanced q-integer is a
sum of positive powers and so is positive.  That is what makes the hypotheses
above cost nothing in the regime the blocks use, while keeping the statements
true over a general field. -/

theorem qInt_pos {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] {q : K} (hq : 0 < q)
    {n : ℕ} (hn : 0 < n) : 0 < qInt q n := by
  refine Finset.sum_pos (fun i _ => zpow_pos hq _) ⟨0, Finset.mem_range.mpr hn⟩

theorem qInt_ne_zero {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] {q : K} (hq : 0 < q)
    {n : ℕ} (hn : 0 < n) : qInt q n ≠ 0 :=
  ne_of_gt (qInt_pos hq hn)

/-- **The c=2 prediction over `ℝ_{>0}`, with nothing assumed.**  This is the
statement `prop:selection-rule-c2-prediction` describes: the q-dimensions are
those of the partitions of 3, computed from their hook lengths, and the closed
form follows. -/
theorem selection_rule_c2_real {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] {q : K}
    (hq : 0 < q) :
    (dimQ q [3] + dimQ q [2, 1] + dimQ q [1, 1, 1]) / 3
      = (q + 1) ^ 2 / (3 * q) :=
  selection_rule_c2_from_hooks q (ne_of_gt hq)
    (qInt_ne_zero hq (by norm_num)) (qInt_ne_zero hq (by norm_num))

/-- **The c=1 anchor over `ℝ_{>0}`, with nothing assumed.** -/
theorem selection_rule_c1_real {K : Type*} [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] {q : K} (hq : 0 < q) :
    (dimQ q [2] + dimQ q [1, 1]) / 2 = 1 :=
  selection_rule_c1_from_hooks q (qInt_ne_zero hq (by norm_num)) (by norm_num)

/-! ## c = 3: the partitions of 4

The proton anchor.  Five shapes, five hook multisets, and the one non-trivial
ratio `[4]_q/[2]_q`.  Added so `prop:selection-rule-anchors-c1-c3` rests on the
hook-length formula for BOTH its anchors rather than only for c=1 — half a
derivation would have left its "derivation-tight" claim still half-asserted. -/

theorem hooks_four : hooks [4] = [4, 3, 2, 1] := by decide
theorem hooks_three_one : hooks [3, 1] = [4, 2, 1, 1] := by decide
theorem hooks_two_two : hooks [2, 2] = [3, 2, 2, 1] := by decide
theorem hooks_two_one_one : hooks [2, 1, 1] = [4, 1, 2, 1] := by decide
theorem hooks_one_four : hooks [1, 1, 1, 1] = [4, 3, 2, 1] := by decide

@[simp] theorem qFact_four (q : R) : qFact q 4 = qInt q 4 * (qInt q 3 * qInt q 2) := by
  simp [qFact, qInt_one]

/-- `[4]_q = (q² + q⁻²)·[2]_q`.  Stated as a product rather than the quotient
`[4]/[2]` so it needs no non-vanishing hypothesis of its own. -/
theorem qInt_four_eq (q : R) (hq : q ≠ 0) :
    qInt q 4 = (q ^ 2 + (q ^ 2)⁻¹) * qInt q 2 := by
  simp [qInt, Finset.sum_range_succ, zpow_neg]
  field_simp
  ring

theorem dimQ_four (q : R) (h2 : qInt q 2 ≠ 0) (h3 : qInt q 3 ≠ 0)
    (h4 : qInt q 4 ≠ 0) : dimQ q [4] = 1 := by
  simp [dimQ, hooks_four, qFact_four, qInt_one]
  exact div_self (mul_ne_zero h4 (mul_ne_zero h3 h2))

theorem dimQ_one_four (q : R) (h2 : qInt q 2 ≠ 0) (h3 : qInt q 3 ≠ 0)
    (h4 : qInt q 4 ≠ 0) : dimQ q [1, 1, 1, 1] = 1 := by
  simp [dimQ, hooks_one_four, qFact_four, qInt_one]
  exact div_self (mul_ne_zero h4 (mul_ne_zero h3 h2))

theorem dimQ_three_one (q : R) (h2 : qInt q 2 ≠ 0) (h4 : qInt q 4 ≠ 0) :
    dimQ q [3, 1] = qInt q 3 := by
  simp [dimQ, hooks_three_one, qFact_four, qInt_one]
  field_simp

theorem dimQ_two_one_one (q : R) (h2 : qInt q 2 ≠ 0) (h4 : qInt q 4 ≠ 0) :
    dimQ q [2, 1, 1] = qInt q 3 := by
  simp [dimQ, hooks_two_one_one, qFact_four, qInt_one]
  field_simp

/-- **`dim_q V_{(2,2)} = [4]_q/[2]_q = q² + q⁻²`** — the one H₄ dimension that is
not `1` or `[3]_q`, and the reason the c=3 anchor has a `3/4 h²` in it. -/
theorem dimQ_two_two (q : R) (hq : q ≠ 0) (h2 : qInt q 2 ≠ 0) (h3 : qInt q 3 ≠ 0) :
    dimQ q [2, 2] = q ^ 2 + (q ^ 2)⁻¹ := by
  simp [dimQ, hooks_two_two, qFact_four, qInt_one, qInt_four_eq q hq]
  field_simp

/-- **c = 3 anchor, derived.**  `(1/4) Σ_{λ⊢4} dim_q V_λ = 5/2 + (3/4)h²`, over
the real q-dimensions of the five partitions of 4. -/
theorem selection_rule_c3_from_hooks (q : R) (hq : q ≠ 0) (h2 : qInt q 2 ≠ 0)
    (h3 : qInt q 3 ≠ 0) (h4 : qInt q 4 ≠ 0) (four_ne : (4 : R) ≠ 0) :
    (dimQ q [4] + dimQ q [3, 1] + dimQ q [2, 2] + dimQ q [2, 1, 1]
       + dimQ q [1, 1, 1, 1]) / 4
      = 5 / 2 + (3 / 4) * (q - q⁻¹) ^ 2 := by
  rw [dimQ_four q h2 h3 h4, dimQ_one_four q h2 h3 h4, dimQ_three_one q h2 h4,
    dimQ_two_one_one q h2 h4, dimQ_two_two q hq h2 h3, qInt_three q hq]
  -- `(2 : R) ≠ 0` is not free in a general field: without it `field_simp`
  -- leaves a `2⁻¹` that `ring` cannot clear.  It follows from `four_ne`
  -- because `4 = 2 * 2`.
  have two_ne : (2 : R) ≠ 0 := fun hc =>
    four_ne (by rw [show (4 : R) = 2 * 2 by norm_num, hc]; ring)
  field_simp
  ring

/-- **The c=3 anchor over `ℝ_{>0}`, with nothing assumed.** -/
theorem selection_rule_c3_real {K : Type*} [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] {q : K} (hq : 0 < q) :
    (dimQ q [4] + dimQ q [3, 1] + dimQ q [2, 2] + dimQ q [2, 1, 1]
       + dimQ q [1, 1, 1, 1]) / 4
      = 5 / 2 + (3 / 4) * (q - q⁻¹) ^ 2 :=
  selection_rule_c3_from_hooks q (ne_of_gt hq)
    (qInt_ne_zero hq (by norm_num)) (qInt_ne_zero hq (by norm_num))
    (qInt_ne_zero hq (by norm_num)) (by norm_num)

end QOU.Mass
