import QOU.MathlibExt.WenzlSchurElement

/-!
# `SchurElementCriterion` carries no Geck–Pfeiffer content as stated

The class `SchurElementCriterion Q X semisimple` takes the semisimplicity
predicate `semisimple : ℕ → Prop` as a **free, opaque parameter**: nothing ties
it to any Hecke algebra. So the class is not the Geck–Pfeiffer theorem; it is a
hypothesis about whatever predicate is passed in.

**What is proved (sorry-free).**
* `schurElementCriterion_iff_forall` — in the substrate regime `Q > 1`,
  `X ≤ 0` (where every Schur element is nonzero, `schurElement_ne_zero`), the
  class holds **iff** `semisimple n` holds for every `n`. So there it is
  literally the hypothesis "the predicate is true at every rank".
* `not_schurElementCriterion_false` — with `semisimple := fun _ => False`,
  `Q = 2`, `X = 0` the class fails: it is **not** true for all parameters.
* `schurElementCriterion_true` — with `semisimple := fun _ => True` it holds
  for every `Q, X`: trivially inhabited, for a wrong reason.

**What is not proved.** Geck–Pfeiffer Thm 7.2.6 (Schur elements nonzero ⇒ the
symmetric algebra is semisimple) for the actual Iwahori–Hecke algebra. To make
the class a real debt item, `semisimple` would have to be replaced by
`IsSemisimpleRing (H_n(q))` for a concrete Hecke algebra; that is a refactor of
the source class and needs owner approval.

-- Ref: [leitner2026] QOU.MathlibExt.WenzlSchurElement; [geckpfeiffer2000]
-- Geck–Pfeiffer, Characters of finite Coxeter groups and Iwahori–Hecke
-- algebras, Thm 7.2.6.
-/

namespace QOU.MathlibExt.WenzlSchurElement.Instances

open QOU.MathlibExt.WenzlSchurElement

/-- In the substrate regime the class is equivalent to `∀ n, ss n`. -/
theorem schurElementCriterion_iff_forall {Q X : ℝ} (hQ : 1 < Q) (hX : X ≤ 0)
    (ss : ℕ → Prop) : SchurElementCriterion Q X ss ↔ ∀ n, ss n := by
  constructor
  · intro C n
    exact C.semisimple_of_schur_ne_zero n fun lam _ => schurElement_ne_zero hQ hX lam
  · intro h
    exact ⟨fun n _ => h n⟩

/-- The class is not universally true: it fails for the predicate `False`. -/
theorem not_schurElementCriterion_false :
    ¬ SchurElementCriterion 2 0 (fun _ => False) := by
  rw [schurElementCriterion_iff_forall (by norm_num) le_rfl]
  intro h
  exact h 0

/-- The class is trivially inhabited by the predicate `True`. -/
theorem schurElementCriterion_true (Q X : ℝ) :
    SchurElementCriterion Q X (fun _ => True) :=
  ⟨fun _ _ => trivial⟩

end QOU.MathlibExt.WenzlSchurElement.Instances
