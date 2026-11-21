/-
Copyright (c) 2026. All rights reserved.

# A framed component inside a γγ word is balanced by its crossings with the others

Owner, 2026-11-21: *"GammaGamma should be able to make it (it just might not be standalone/unstable
if isolated)"*, about a gluon that is a framed (q-shifted) unknot.

Label each crossing of a word `true` when both strands belong to the same closure component
(a self-crossing) and `false` otherwise. The writhe splits into the self part and the part
between components. A γγ word has writhe `0` (`writhe_eq_zero`), so

* `selfWrithe_eq_neg_betweenWrithe` : in a γγ word the self part is minus the between part,
  for every labelling.
* `self_ne_zero_needs_between` : a γγ word whose self-crossings do not cancel must have
  crossings between components that do not cancel either. A framed unknot cannot be
  γγ-produced alone (that would need a single component, so no between crossings); it exists
  only linked into a larger word.

Pure combinatorics; no ring, no q, no empirical input.
-/
import QOU.Mass.GammaGammaWordSelection

namespace QOU.QBeta.FramedGluonWrithe

open QOU.Mass.GammaGammaWordSelection

/-- Signed sum over the crossings labelled `b`. -/
def labelledWrithe (b : Bool) : List (Crossing × Bool) → ℤ
  | [] => 0
  | (c, l) :: t => (if l = b then sign c else 0) + labelledWrithe b t

/-- Writhe of the self-crossings. -/
def selfWrithe (l : List (Crossing × Bool)) : ℤ := labelledWrithe true l

/-- Writhe of the crossings between different components. -/
def betweenWrithe (l : List (Crossing × Bool)) : ℤ := labelledWrithe false l

theorem self_add_between (w : Word) (ls : List Bool) (h : ls.length = w.length) :
    selfWrithe (w.zip ls) + betweenWrithe (w.zip ls) = writhe w := by
  induction w generalizing ls with
  | nil => simp [selfWrithe, betweenWrithe, labelledWrithe, writhe]
  | cons c t ih =>
    cases ls with
    | nil => simp at h
    | cons l lt =>
      simp only [List.length_cons, add_left_inj] at h
      have := ih lt h
      simp only [selfWrithe, betweenWrithe, List.zip_cons_cons, labelledWrithe] at this ⊢
      simp only [writhe, List.map_cons, List.sum_cons] at this ⊢
      cases l <;> simp <;> linarith

theorem selfWrithe_eq_neg_betweenWrithe {w : Word} (hw : GammaGammaWord w) (ls : List Bool)
    (h : ls.length = w.length) : selfWrithe (w.zip ls) = -betweenWrithe (w.zip ls) := by
  have := self_add_between w ls h
  rw [writhe_eq_zero hw] at this
  linarith

theorem self_ne_zero_needs_between {w : Word} (hw : GammaGammaWord w) (ls : List Bool)
    (h : ls.length = w.length) (hs : selfWrithe (w.zip ls) ≠ 0) :
    betweenWrithe (w.zip ls) ≠ 0 := by
  intro hb
  exact hs (by rw [selfWrithe_eq_neg_betweenWrithe hw ls h, hb, neg_zero])

/-- If every crossing is a self-crossing (one closure component), a γγ word has no framing. -/
theorem single_component_unframed {w : Word} (hw : GammaGammaWord w) :
    selfWrithe (w.zip (List.replicate w.length true)) = 0 := by
  have h1 := selfWrithe_eq_neg_betweenWrithe hw (List.replicate w.length true) (by simp)
  have h2 : ∀ (v : Word), betweenWrithe (v.zip (List.replicate v.length true)) = 0 := by
    intro v
    induction v with
    | nil => simp [betweenWrithe, labelledWrithe]
    | cons c t ih =>
      simp only [List.length_cons, List.replicate_succ, List.zip_cons_cons, betweenWrithe,
        labelledWrithe] at ih ⊢
      simpa using ih
  rw [h1, h2, neg_zero]

end QOU.QBeta.FramedGluonWrithe
