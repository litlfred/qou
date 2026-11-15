import Mathlib.Topology.Order.IntermediateValue
import Mathlib.Tactic
import QOU.QBeta.AdjointIndexSetM3

/-!
# QOU.QBeta.FloorRemainderFromDerivedShapeFields — H_floor's remainder for `4₁` and `5₂`, from the corpus's own shape fields

## Where this sits (Route C, milestone M3, bean `qou-m3ad` Part 4)

`AdjointIndexSetM3` records the rival hypothesis `H_floor`: the knot-independent
core of the DT index set is the triple `{trivial, geometric, conjugate-geometric}`
and the knot-**dependent** remainder is the number of **real** embeddings of the
trace field. Its inputs — `realEmbeddings` and `complexPairs` — were transcribed
from Garoufalidis–Zagier §2.1 (`library/arxiv-2111.06645v3`), i.e. from a table.

This file derives both numbers for `4₁` and `5₂` from the shape fields the
corpus's own two-bridge triangulations produce (`two_bridge_layered_nz_probe.py`,
#6985; Farey word `R` for `4₁`, `RL` for `5₂`):

* `4₁`: both shapes are `e^{iπ/3}`, minimal polynomial `x² − x + 1`
  (discriminant `−3`) — **no real root**, so the signature is `(0, 1)` and the
  remainder is `0`;
* `5₂`: shapes `θ, θ, θ² − 1, θ² − 1` with `θ³ − θ + 1 = 0` (discriminant `−23`,
  `FiveTwoGluingFromFareyWord.shape_cubic_discriminant`) — **exactly one real
  root**, so the signature is `(1, 1)` and the remainder is `1`.

The real-root statements are proved outright over `ℝ` (this is archimedean
content, §7c: the ordering is the whole point). The link theorems at the end say
the transcribed `realEmbeddings` values are the derived real-root counts, so
`forced_remainder_is_the_real_embedding_count` now rests on a derivation rather
than on a table for the two knots the corpus derives.

The companion probe
`computations/probes/aomega_m3_floor_remainder_from_derived_shape_fields_probe.py`
(13/13) computes the same signatures by an exact Sturm count and, in addition,
pushes every tetrahedron shape through every embedding of the field and sums the
Bloch–Wigner dilogarithm: the real embedding of `5₂` gives real shapes and volume
exactly `0`, the complex pair gives `±Vol`, i.e. the Chern–Simons value sets
`{+V, −V}` and `{0, +V, −V}` that `H_floor` grades by. That part is measured, not
formalised here (`BlochWignerLobachevsky.BlochWigner_lob_real_eq_zero` covers
real shapes in `(0,1)` only; the `5₂` real embedding has a shape `θ ≈ −1.3247`).

**Scope.** This does **not** separate `H_Ad` from `H_floor` (the core is `3` under
both, `core_is_three_on_all_three`), and it does not reach `(−2,3,7)`, whose field
the corpus does not derive. It upgrades the *provenance* of Part 4's rule on two
knots; it derives nothing about `A_ω`.

-- Ref: [leitner2026] computations/probes/two_bridge_layered_nz_probe.py (#6985)
-- Ref: [leitner2026] docs/audits/2026-09-06-two-bridge-layering-from-farey-word.md
-- Ref: [garoufalidis-zagier-2024] library/arxiv-2111.06645v3 §2.1 (the transcribed table this replaces for 4₁, 5₂)
-/

namespace QOU.QBeta.FloorRemainderFromDerivedShapeFields

open QOU.QBeta.AdjointIndexSetM3

/-! ## `4₁`: the derived shape polynomial `x² − x + 1` has no real root -/

/-- The minimal polynomial of the `4₁` shape `e^{iπ/3}`. -/
def fourOneShapePoly (x : ℝ) : ℝ := x ^ 2 - x + 1

/-- **No real root**: `x² − x + 1 = (x − ½)² + ¾ > 0`. -/
theorem fourOneShapePoly_pos (x : ℝ) : 0 < fourOneShapePoly x := by
  unfold fourOneShapePoly; nlinarith [sq_nonneg (x - 1 / 2)]

theorem fourOneShapePoly_ne_zero (x : ℝ) : fourOneShapePoly x ≠ 0 :=
  (fourOneShapePoly_pos x).ne'

/-! ## `5₂`: the derived shape cubic `θ³ − θ + 1` has exactly one real root -/

/-- The derived shape cubic of `5₂`. -/
def fiveTwoShapeCubic (θ : ℝ) : ℝ := θ ^ 3 - θ + 1

theorem fiveTwoShapeCubic_continuous : Continuous fiveTwoShapeCubic := by
  unfold fiveTwoShapeCubic; fun_prop

theorem fiveTwoShapeCubic_neg_two : fiveTwoShapeCubic (-2) = -5 := by
  unfold fiveTwoShapeCubic; norm_num

theorem fiveTwoShapeCubic_neg_one : fiveTwoShapeCubic (-1) = 1 := by
  unfold fiveTwoShapeCubic; norm_num

/-- **Existence**: a real root in `(−2, −1)`, by the intermediate value theorem. -/
theorem fiveTwoShapeCubic_exists_root :
    ∃ θ : ℝ, θ ∈ Set.Ioo (-2 : ℝ) (-1) ∧ fiveTwoShapeCubic θ = 0 := by
  have hmem : (0 : ℝ) ∈ Set.Ioo (fiveTwoShapeCubic (-2)) (fiveTwoShapeCubic (-1)) := by
    rw [fiveTwoShapeCubic_neg_two, fiveTwoShapeCubic_neg_one]; constructor <;> norm_num
  obtain ⟨θ, hθ, hz⟩ :=
    intermediate_value_Ioo (by norm_num : (-2 : ℝ) ≤ -1)
      fiveTwoShapeCubic_continuous.continuousOn hmem
  exact ⟨θ, hθ, hz⟩

/-- **Every real root lies below `−1`.** On `[−1, ∞)` the cubic is positive: for
`θ ≥ 1` and for `θ ∈ [−1, 0]` the term `θ(θ² − 1)` is `≥ 0`; on `(0, 1)` it is
bounded below by `−2/(3√3) > −1`. -/
theorem fiveTwoShapeCubic_pos_of_neg_one_le {θ : ℝ} (h : -1 ≤ θ) :
    0 < fiveTwoShapeCubic θ := by
  unfold fiveTwoShapeCubic
  rcases le_or_gt θ 0 with h0 | h0
  · nlinarith [mul_nonneg (neg_nonneg.mpr h0) (by nlinarith : (0:ℝ) ≤ 1 - θ ^ 2)]
  · rcases le_or_gt 1 θ with h1 | h1
    · nlinarith [mul_nonneg h0.le (by nlinarith : (0:ℝ) ≤ θ ^ 2 - 1)]
    · nlinarith [sq_nonneg (θ - 1 / 2), sq_nonneg θ, mul_pos h0 (sub_pos.mpr h1),
        sq_nonneg (θ ^ 2 - 1 / 3), mul_pos h0 h0]

theorem fiveTwoShapeCubic_root_lt_neg_one {θ : ℝ} (hz : fiveTwoShapeCubic θ = 0) :
    θ < -1 := by
  by_contra h
  push_neg at h
  exact absurd hz (fiveTwoShapeCubic_pos_of_neg_one_le h).ne'

/-- **Uniqueness**: two real roots coincide. Both lie below `−1`, where the
cubic is strictly increasing: `f(a) − f(b) = (a − b)(a² + ab + b² − 1)` and
`a² + ab + b² − 1 > 0` there. -/
theorem fiveTwoShapeCubic_root_unique {a b : ℝ}
    (ha : fiveTwoShapeCubic a = 0) (hb : fiveTwoShapeCubic b = 0) : a = b := by
  have ha' := fiveTwoShapeCubic_root_lt_neg_one ha
  have hb' := fiveTwoShapeCubic_root_lt_neg_one hb
  unfold fiveTwoShapeCubic at ha hb
  have hfac : (a - b) * (a ^ 2 + a * b + b ^ 2 - 1) = 0 := by linear_combination ha - hb
  have hpos : 0 < a ^ 2 + a * b + b ^ 2 - 1 := by
    nlinarith [mul_pos (neg_pos.mpr (show a < 0 by linarith)) (neg_pos.mpr (show b < 0 by linarith))]
  rcases mul_eq_zero.mp hfac with h | h
  · linarith
  · linarith

/-- **Exactly one real root.** -/
theorem fiveTwoShapeCubic_existsUnique_root : ∃! θ : ℝ, fiveTwoShapeCubic θ = 0 := by
  obtain ⟨θ, -, hz⟩ := fiveTwoShapeCubic_exists_root
  exact ⟨θ, hz, fun b hb => fiveTwoShapeCubic_root_unique hb hz⟩

/-! ## The link to `H_floor`'s transcribed inputs

`realEmbeddings` in `AdjointIndexSetM3` is a table. The two theorems below say
its `4₁` and `5₂` entries are the real-root counts of the **derived** shape
polynomials: `0` because `x² − x + 1` has none, `1` because `θ³ − θ + 1` has
exactly one. (The complex-pair count `1` is then forced by the degrees `2` and
`3`.) So on these two knots `forced_remainder_is_the_real_embedding_count` rests
on the corpus's own triangulations, not on Garoufalidis–Zagier's table. -/

theorem fourOne_realEmbeddings_derived :
    realEmbeddings PKnot.fourOne = 0 ∧ ∀ x : ℝ, fourOneShapePoly x ≠ 0 :=
  ⟨by decide, fourOneShapePoly_ne_zero⟩

theorem fiveTwo_realEmbeddings_derived :
    realEmbeddings PKnot.fiveTwo = 1 ∧ ∃! θ : ℝ, fiveTwoShapeCubic θ = 0 :=
  ⟨by decide, fiveTwoShapeCubic_existsUnique_root⟩

/-- The remainders `0` and `1`, and their unit difference (Part 1's forced value),
now with the derived real-root counts as their source. -/
theorem floor_remainders_from_derived_fields :
    floorRemainder PKnot.fourOne = 0 ∧ floorRemainder PKnot.fiveTwo = 1 ∧
    floorRemainder PKnot.fiveTwo - floorRemainder PKnot.fourOne = 1 := by
  decide

end QOU.QBeta.FloorRemainderFromDerivedShapeFields
