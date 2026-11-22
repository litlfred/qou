/-
The pn interface letter is a strict convex combination of the pp and nn letters,
and the two-strand interface law is affine.  Therefore the pn bond factor is
strictly between the like-pair bond factors, for every parameter value — so it
can never be the strict maximum of the three.

Why that matters.  Bean `qou-q8vl` (PR #7226) establishes that a positive
three-body Ursell coefficient on the production `A = 3` chain needs EXACTLY ONE
bond factor above `1`, and that the sign-mixed assignment which also gives the
correct two-nucleon spectrum — unlike pairs bind, like pairs do not — is the one
with the pn bond opposite to both like-pair bonds.  In bond-factor terms that
pattern is

    mu_pn > 1 > mu_pp,  mu_pn > 1 > mu_nn,

i.e. `mu_pn` is the STRICT MAXIMUM of the three.  The theorems below say that is
unreachable whenever `mu_pn` is a strict convex combination of `mu_pp` and
`mu_nn`, independently of `q`, of the colour weight, and of the numerical values.

This is strictly stronger than the value-level exclusion recorded on `qou-q8vl`
("production letters excluded by `d <= 0`", which pins the current definitions):
it constrains what a THIRD bond family would have to do.  Such a family cannot
merely move the letters above `1`; it must break the averaging structure itself,
or break affineness of the interface law.

Scope (b) structural exclusion.  The invariant is the strict convexity of the
averaged letter together with affineness of the two-strand trace, both of which
are identities rather than measurements.

-- Ref: [leitner2026] bean qou-q8vl; probe
--      `the_pn_bond_is_an_average_and_cannot_be_extremal_probe`
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace QOU.MassTheory.PnBetweennessBlocksSignMixed

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- A strict convex combination of two values, with both weights strictly
positive and summing to one. -/
def combo (w : R) (a b : R) : R := w * a + (1 - w) * b

omit [LinearOrder R] [IsStrictOrderedRing R] in
lemma combo_self (w a : R) : combo w a a = a := by
  unfold combo; ring

/-- A strict convex combination never strictly exceeds both of its endpoints. -/
theorem combo_not_gt_both {w a b : R} (hw0 : 0 < w) (hw1 : w < 1) :
    ¬ (a < combo w a b ∧ b < combo w a b) := by
  rintro ⟨ha, hb⟩
  have h1w : (0 : R) < 1 - w := by linarith
  -- w*a + (1-w)*b > w*a + (1-w)*b is the contradiction we assemble
  have hA : w * a < w * (combo w a b) := by
    exact mul_lt_mul_of_pos_left ha hw0
  have hB : (1 - w) * b < (1 - w) * (combo w a b) := by
    exact mul_lt_mul_of_pos_left hb h1w
  have hsum : combo w a b < combo w a b := by
    calc combo w a b = w * a + (1 - w) * b := rfl
      _ < w * (combo w a b) + (1 - w) * (combo w a b) := by linarith
      _ = combo w a b := by ring
  exact lt_irrefl _ hsum

/-- Symmetrically, it never falls strictly below both endpoints. -/
theorem combo_not_lt_both {w a b : R} (hw0 : 0 < w) (hw1 : w < 1) :
    ¬ (combo w a b < a ∧ combo w a b < b) := by
  rintro ⟨ha, hb⟩
  have h1w : (0 : R) < 1 - w := by linarith
  have hA : w * (combo w a b) < w * a := mul_lt_mul_of_pos_left ha hw0
  have hB : (1 - w) * (combo w a b) < (1 - w) * b := mul_lt_mul_of_pos_left hb h1w
  have hsum : combo w a b < combo w a b := by
    calc combo w a b = w * (combo w a b) + (1 - w) * (combo w a b) := by ring
      _ < w * a + (1 - w) * b := by linarith
      _ = combo w a b := rfl
  exact lt_irrefl _ hsum

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- The affine interface law `mu = z + d` carries a convex combination of
offsets to the same convex combination of bond factors. -/
theorem affine_preserves_combo (z w dpp dnn : R) :
    z + combo w dpp dnn = combo w (z + dpp) (z + dnn) := by
  unfold combo; ring

/-- **The exclusion.**  If the pn offset is a strict convex combination of the
like-pair offsets and the interface law is affine, then the pn bond factor
cannot be the strict maximum of the three — so the sign-mixed pattern that
`qou-q8vl` shows is required (pn above one, both like pairs below) is
unreachable, for every `z`, every weight, and every offset pair. -/
theorem pn_not_strict_max
    {z w dpp dnn : R} (hw0 : 0 < w) (hw1 : w < 1) :
    ¬ ((z + dpp) < (z + combo w dpp dnn) ∧ (z + dnn) < (z + combo w dpp dnn)) := by
  rw [affine_preserves_combo]
  exact combo_not_gt_both hw0 hw1

/-- The required sign-mixed pattern, stated as `qou-q8vl` states it: the pn bond
factor exceeds one while both like-pair factors fall below it. -/
def signMixedPattern (mupp mupn munn : R) : Prop :=
  1 < mupn ∧ mupp < 1 ∧ munn < 1

/-- **Corollary.**  No averaged pn letter can realise the sign-mixed pattern.
The hypothesis is exactly "pn is a strict convex combination under an affine
interface law"; the conclusion needs no numerical input. -/
theorem signMixed_impossible_of_combo
    {z w dpp dnn : R} (hw0 : 0 < w) (hw1 : w < 1) :
    ¬ signMixedPattern (z + dpp) (z + combo w dpp dnn) (z + dnn) := by
  rintro ⟨h1, hpp, hnn⟩
  exact pn_not_strict_max hw0 hw1 ⟨by linarith, by linarith⟩

/-- The corpus weight.  With colour parameter `delta` the pn offset is
`d_pn = (1/2 + delta/4) * d_pp + (1/2 - delta/4) * d_nn`, so the weight is
`w = 1/2 + delta/4`, strictly inside `(0,1)` exactly when `|delta| < 2`. -/
def corpusWeight (delta : R) : R := 1/2 + delta/4

lemma corpusWeight_pos {delta : R} (h : -2 < delta) : 0 < corpusWeight delta := by
  unfold corpusWeight; linarith

lemma corpusWeight_lt_one {delta : R} (h : delta < 2) : corpusWeight delta < 1 := by
  unfold corpusWeight; linarith

/-- **The corpus instance.**  For every colour parameter strictly inside
`(-2, 2)` — the range in which the averaged interface is defined — the sign-mixed
pattern is unreachable. -/
theorem signMixed_impossible_corpus
    {z delta dpp dnn : R} (hlo : -2 < delta) (hhi : delta < 2) :
    ¬ signMixedPattern (z + dpp) (z + combo (corpusWeight delta) dpp dnn) (z + dnn) :=
  signMixed_impossible_of_combo (corpusWeight_pos hlo) (corpusWeight_lt_one hhi)

#print axioms combo_not_gt_both
#print axioms combo_not_lt_both
#print axioms affine_preserves_combo
#print axioms pn_not_strict_max
#print axioms signMixed_impossible_of_combo
#print axioms signMixed_impossible_corpus

end QOU.MassTheory.PnBetweennessBlocksSignMixed
