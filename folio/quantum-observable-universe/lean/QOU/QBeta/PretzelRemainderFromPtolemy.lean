import Mathlib.Topology.Order.IntermediateValue
import Mathlib.Tactic
import QOU.QBeta.AdjointIndexSetM3
import QOU.QBeta.FloorRemainderFromDerivedShapeFields

/-!
# QOU.QBeta.PretzelRemainderFromPtolemy — the third knot's `H_floor` inputs, from the solved Ptolemy varieties

## Where this sits (Route C, M3, bean `qou-m3ad` Part 6)

`AdjointIndexSetM3` carries the `(−2,3,7)` row of Garoufalidis–Zagier's table as a
transcription: `realEmbeddings pretzel237 = 4`, `complexPairs pretzel237 = 1`,
`|P_K| = 7`. Part 4 called the count `7` *a prediction, not a check*, because the
Ptolemy database is firewalled. The variety itself is small enough to solve here
(`aomega_m3_pretzel_remainder_from_ptolemy_probe.py`, 10/10): SnapPy's census
`m016` (= `K12n242` = `(−2,3,7)` = Culler's `K3_1`, 3 tetrahedra) has two `N = 2`
obstruction classes, and a lex Gröbner basis reduces each to one cubic in one
Ptolemy coordinate:

* class 1: `c³ − c − 1 = 0` — discriminant `−23`, the `5₂` shape cubic in `−c`
  (`c = −θ`, `θ³ − θ + 1 = 0`): **one** real root;
* class 0: `c³ + 4c² + 3c − 1 = 0` — discriminant `49`, splits over
  `ℚ(η)`, `η³ + η² − 2η − 1 = 0`: **three** real roots.

Boundary-unipotent representations are the nontrivial elements of `P_K`, one per
Ptolemy solution over all obstruction classes, so `|P_K| = 1 + 3 + 3 = 7`, the real
embeddings number `1 + 3 = 4`, and `H_floor`'s remainder is `4`. This file proves
the two real-root counts over `ℝ` and links them to the transcribed values, as
`FloorRemainderFromDerivedShapeFields` does for `4₁` and `5₂`.

**Scope.** The triangulation is SnapPy's census one (a held tool), not a Farey-word
derivation — the pretzel is not two-bridge. Nothing here separates `H_Ad` from
`H_floor` (core `3` under both), and the pretzel's `q → 0` Stokes matrix is still
not held (GGM record its level as `2`), so the one-sided `H_Ad` test stays open.

-- Ref: [leitner2026] computations/probes/aomega_m3_pretzel_remainder_from_ptolemy_probe.py
-- Ref: [garoufalidis-zagier-2024] library/arxiv-2111.06645v3 §2.1 (the table this checks)
-/

namespace QOU.QBeta.PretzelRemainderFromPtolemy

open QOU.QBeta.AdjointIndexSetM3
open QOU.QBeta.FloorRemainderFromDerivedShapeFields

/-- The class-1 cubic, `c³ − c − 1`. -/
def geoCubic (c : ℝ) : ℝ := c ^ 3 - c - 1

/-- `c³ − c − 1 = −((−c)³ − (−c) + 1)`: the `5₂` shape cubic in `−c`. -/
theorem geoCubic_eq_neg_fiveTwo (c : ℝ) : geoCubic c = -fiveTwoShapeCubic (-c) := by
  unfold geoCubic fiveTwoShapeCubic; ring

/-- **Exactly one real root**, inherited from `fiveTwoShapeCubic_existsUnique_root`. -/
theorem geoCubic_existsUnique_root : ∃! c : ℝ, geoCubic c = 0 := by
  obtain ⟨θ, hθ, huniq⟩ := fiveTwoShapeCubic_existsUnique_root
  refine ⟨-θ, ?_, ?_⟩
  · show geoCubic (-θ) = 0
    rw [geoCubic_eq_neg_fiveTwo, neg_neg, hθ, neg_zero]
  · intro c hc
    have hc' : geoCubic c = 0 := hc
    rw [geoCubic_eq_neg_fiveTwo, neg_eq_zero] at hc'
    have := huniq (-c) hc'
    linarith

/-- The class-0 cubic, `c³ + 4c² + 3c − 1`. -/
def realCubic (c : ℝ) : ℝ := c ^ 3 + 4 * c ^ 2 + 3 * c - 1

theorem realCubic_continuous : Continuous realCubic := by
  unfold realCubic; fun_prop

theorem realCubic_neg_three : realCubic (-3) = -1 := by unfold realCubic; norm_num
theorem realCubic_neg_two : realCubic (-2) = 1 := by unfold realCubic; norm_num
theorem realCubic_neg_one : realCubic (-1) = -1 := by unfold realCubic; norm_num
theorem realCubic_one : realCubic 1 = 7 := by unfold realCubic; norm_num

/-- **Three real roots**, one in each of `(−3,−2)`, `(−2,−1)`, `(−1,1)` — the
intermediate value theorem three times; the intervals are disjoint, so the roots
are distinct. A cubic has no more, so this is the full signature `(3, 0)`. -/
theorem realCubic_three_real_roots :
    (∃ c ∈ Set.Ioo (-3 : ℝ) (-2), realCubic c = 0) ∧
    (∃ c ∈ Set.Ioo (-2 : ℝ) (-1), realCubic c = 0) ∧
    (∃ c ∈ Set.Ioo (-1 : ℝ) 1, realCubic c = 0) := by
  refine ⟨?_, ?_, ?_⟩
  · have hmem : (0 : ℝ) ∈ Set.Ioo (realCubic (-3)) (realCubic (-2)) := by
      rw [realCubic_neg_three, realCubic_neg_two]; constructor <;> norm_num
    obtain ⟨c, hc, hz⟩ := intermediate_value_Ioo (by norm_num : (-3 : ℝ) ≤ -2)
      realCubic_continuous.continuousOn hmem
    exact ⟨c, hc, hz⟩
  · have hmem : (0 : ℝ) ∈ Set.Ioo (realCubic (-1)) (realCubic (-2)) := by
      rw [realCubic_neg_one, realCubic_neg_two]; constructor <;> norm_num
    obtain ⟨c, hc, hz⟩ := intermediate_value_Ioo' (by norm_num : (-2 : ℝ) ≤ -1)
      realCubic_continuous.continuousOn hmem
    exact ⟨c, hc, hz⟩
  · have hmem : (0 : ℝ) ∈ Set.Ioo (realCubic (-1)) (realCubic 1) := by
      rw [realCubic_neg_one, realCubic_one]; constructor <;> norm_num
    obtain ⟨c, hc, hz⟩ := intermediate_value_Ioo (by norm_num : (-1 : ℝ) ≤ 1)
      realCubic_continuous.continuousOn hmem
    exact ⟨c, hc, hz⟩

/-- **The transcribed pretzel row is the derived count**: `4 = 3 + 1` real
embeddings — three real roots of the class-0 cubic, one of the class-1 cubic. -/
theorem pretzel_realEmbeddings_derived :
    realEmbeddings PKnot.pretzel237 = 4 ∧
    ((∃ c ∈ Set.Ioo (-3 : ℝ) (-2), realCubic c = 0) ∧
     (∃ c ∈ Set.Ioo (-2 : ℝ) (-1), realCubic c = 0) ∧
     (∃ c ∈ Set.Ioo (-1 : ℝ) 1, realCubic c = 0)) ∧
    (∃! c : ℝ, geoCubic c = 0) :=
  ⟨by decide, realCubic_three_real_roots, geoCubic_existsUnique_root⟩

/-- `|P_K| = 7` and remainder `4`, now with a derived source on all three knots. -/
theorem pretzel_pk_and_remainder :
    pkSize PKnot.pretzel237 = 7 ∧ floorRemainder PKnot.pretzel237 = 4 := by decide

end QOU.QBeta.PretzelRemainderFromPtolemy
