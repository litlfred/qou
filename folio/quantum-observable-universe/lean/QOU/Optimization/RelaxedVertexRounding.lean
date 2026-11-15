/-
  Rounding a one-constraint selection LP to its integer optimum, by slopes.

  Setting.  Finitely many candidate words `k`, each with a cost `c k` and a
  character value `x k`; a word is *feasible* when `x k ≥ 0`.  The integer
  program picks the cheapest feasible word.  Its LP relaxation mixes words;
  when the cheapest word overall is infeasible, an optimal mixture sits on an
  edge `[a, b]` with `x a < 0 < x b` at the point where the mixed character is
  `0`, and its value is

      crossVal a b = (c a · x b − c b · x a) / (x b − x a) = c a − x a · slope a b,
      slope a b    = (c b − c a) / (x b − x a).

  Such an edge has exactly ONE feasible endpoint, `b`, so "round the relaxed
  optimum to the feasible vertex of its face" is a canonical rule, not a
  choice.  This file proves the two facts that make the rule return the
  integer optimum:

  * `crossVal_le_iff_slope_le` — for a fixed infeasible `a`, the edge to `b`
    beats the edge to `j` exactly when its slope is smaller (`x a < 0`).
  * `slope_le_of_margin` — a margin condition under which the cheapest
    feasible word `b` has the smallest slope against EVERY feasible `j` that
    costs at least `δ` more and has character at most a common bound `X`.

  For the γγ family `V^k` in `H₃` the bound is `X = 2` (det V = 1, so
  χ_(2,1)(V^k) = 2 cos kθ), `δ = 2` crossings, and the probe
  `collision_gradient_lagrangian_probe.py` checks the margin at the pin.

  Generic over a linearly ordered field.
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.Optimization.RelaxedVertexRounding

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- Slope of the cost against the character along the edge `a → b`. -/
def slope (ca xa cb xb : K) : K := (cb - ca) / (xb - xa)

/-- Value of the mixture of `a` and `b` whose character is `0`. -/
def crossVal (ca xa cb xb : K) : K := (ca * xb - cb * xa) / (xb - xa)

omit [IsStrictOrderedRing K] in
theorem crossVal_eq (ca xa cb xb : K) (h : xa < xb) :
    crossVal ca xa cb xb = ca - xa * slope ca xa cb xb := by
  have hne : xb - xa ≠ 0 := sub_ne_zero.mpr (ne_of_gt h)
  unfold crossVal slope
  field_simp
  ring

/-- The mixture weights: `λ = x b / (x b − x a)` on `a` lies in `(0, 1)`,
kills the character, and has cost `crossVal`. -/
theorem mixture (ca xa cb xb : K) (ha : xa < 0) (hb : 0 < xb) :
    let l := xb / (xb - xa)
    0 < l ∧ l < 1 ∧ l * xa + (1 - l) * xb = 0
      ∧ l * ca + (1 - l) * cb = crossVal ca xa cb xb := by
  intro l
  have hd : 0 < xb - xa := by linarith
  have hne : xb - xa ≠ 0 := hd.ne'
  refine ⟨div_pos hb hd, (div_lt_one hd).mpr (by linarith), ?_, ?_⟩
  · simp only [l]; field_simp; ring
  · simp only [l, crossVal]; field_simp; ring

/-- **For a fixed infeasible `a`, a smaller slope means a cheaper mixture.** -/
theorem crossVal_le_iff_slope_le {ca xa cb xb cj xj : K}
    (ha : xa < 0) (hb : 0 < xb) (hj : 0 < xj) :
    crossVal ca xa cb xb ≤ crossVal ca xa cj xj
      ↔ slope ca xa cb xb ≤ slope ca xa cj xj := by
  rw [crossVal_eq ca xa cb xb (by linarith), crossVal_eq ca xa cj xj (by linarith)]
  constructor
  · intro h
    by_contra hc
    push_neg at hc
    have : -xa * slope ca xa cj xj < -xa * slope ca xa cb xb :=
      mul_lt_mul_of_pos_left hc (by linarith)
    linarith
  · intro h
    have : -xa * slope ca xa cb xb ≤ -xa * slope ca xa cj xj :=
      mul_le_mul_of_nonneg_left h (by linarith)
    linarith

/-- **The margin condition.**  Let `b` be feasible with `c a < c b`, and let `j`
be any feasible word with `c j ≥ c b + δ` and `x j ≤ X`.  If
`(c b − c a)(X − x b) ≤ δ (x b − x a)`, then `slope a b ≤ slope a j`. -/
theorem slope_le_of_margin {ca xa cb xb cj xj X δ : K}
    (ha : xa < 0) (hb : 0 < xb) (hj : 0 < xj) (hjX : xj ≤ X)
    (hcab : ca < cb) (hcj : cb + δ ≤ cj)
    (hmargin : (cb - ca) * (X - xb) ≤ δ * (xb - xa)) :
    slope ca xa cb xb ≤ slope ca xa cj xj := by
  unfold slope
  have hdb : 0 < xb - xa := by linarith
  have hdj : 0 < xj - xa := by linarith
  rw [div_le_div_iff₀ hdb hdj]
  -- (cb − ca)(xj − xa) ≤ (cb − ca)(X − xa) ≤ (cb − ca + δ)(xb − xa) ≤ (cj − ca)(xb − xa)
  have h1 : (cb - ca) * (xj - xa) ≤ (cb - ca) * (X - xa) :=
    mul_le_mul_of_nonneg_left (by linarith) (by linarith)
  have h2 : (cb - ca + δ) * (xb - xa) ≤ (cj - ca) * (xb - xa) :=
    mul_le_mul_of_nonneg_right (by linarith) hdb.le
  nlinarith

/-- **Rounding returns the integer optimum.**  Under the margin condition, the
edge from `a` to the cheapest feasible word `b` is no more expensive than the
edge to any other admissible feasible `j`. -/
theorem crossVal_le_of_margin {ca xa cb xb cj xj X δ : K}
    (ha : xa < 0) (hb : 0 < xb) (hj : 0 < xj) (hjX : xj ≤ X)
    (hcab : ca < cb) (hcj : cb + δ ≤ cj)
    (hmargin : (cb - ca) * (X - xb) ≤ δ * (xb - xa)) :
    crossVal ca xa cb xb ≤ crossVal ca xa cj xj :=
  (crossVal_le_iff_slope_le ha hb hj).mpr
    (slope_le_of_margin ha hb hj hjX hcab hcj hmargin)

end QOU.Optimization.RelaxedVertexRounding
