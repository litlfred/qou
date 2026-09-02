/-
  Bean `qou-z9ws` — why `DoubleMagicConjecture.magic_iff_double_magic` was FALSE,
  and a guard that the repair actually excludes the counterexample.

  WHAT THIS FILE WAS, AND WHY IT CHANGED

  Until 2026-08-31 this file proved `DoubleMagicConjecture → False` by
  instantiating the class's `magic_iff_double_magic` field at the all-empty
  composite.  That field has since been **removed** from the class and
  `IsDoubleMagic` has been **corrected**, so the original theorem can no longer
  be stated — its subject is gone.

  Deleting the file would delete the evidence, so it is converted instead: every
  fact the refutation rested on is re-proved below in a form that survives the
  repair, and one new theorem checks that the repair does what it was supposed
  to.  A refutation whose target has been fixed should leave behind a
  regression guard, not a gap.

  THE ORIGINAL DEFECT

  `IsDoubleMagic` read

      def IsDoubleMagic (C : Composite) : Prop :=
        isSelfConjugate C.ydZ ∧ isSelfConjugate C.ydN

  while its own docstring said *"both constituents are **saturated** and
  self-conjugate"*.  The saturation was never in the definition, so
  "double magic" meant "both constituents self-conjugate" with no magic number
  anywhere — and the **empty** composite `⟨∅, ∅, ∅⟩` qualified, the empty
  diagram being trivially self-conjugate.  The class's second field then forced
  `C.ydA.n ∈ magicLadder`, i.e. `0 ∈ {2, 8, 20, 28, 50, 82, 126}`.

  `emptyComposite_old_isDoubleMagic` and `zero_not_in_magicLadder` below are
  those two halves, still proved.

  THE REPAIR, AND WHY IT IS NOT JUST A NON-DEGENERACY GUARD

  Two things changed, for two independent reasons:

  1. `IsDoubleMagic` gained the saturation its docstring already claimed
     (`Z, N ∈ 𝔐` is the `.md`'s opening hypothesis).
     `emptyComposite_not_isDoubleMagic` checks this closes the hole.

  2. `magic_iff_double_magic` was **removed**, not guarded.  Its
     `A ∈ magicLadder` conjunct is absent from the `.md`, and is false at every
     physically intended instance: `magic_sum_is_almost_never_magic` below
     enumerates all 49 magic pairs and finds `8 + 20 = 28` as the *only* pair
     whose sum is magic, so ⁴He (A=4), ¹⁶O (16), ⁴⁰Ca (40), ⁴⁸Ca (48),
     ⁵⁶Ni (56), ¹³²Sn (132) and ²⁰⁸Pb (208) all fail it.  And the `↔` cannot be
     rescued by a guard in any case: adding the saturation makes the `←`
     direction safe and breaks `→` at the same empty composite.

  SCOPE.  None of this says double-magic nuclei are not special, or that
  LR-fusion rigidity is wrong.  `lr_rigidity` — the `.md`'s actual claim —
  survives untouched as the open conjecture.  What was excluded is one
  conjunct the Lean added and one converse the `.md` does not assert.

  VERIFY (lean-direct, Mathlib oleans restored, no `lake build` — a build
  against a restored cache with `traces=0` evicts it):

      LEAN_PATH=<mathlib libs>:<QOU build lib> \
        lean docs/audits/2026-08-31-double-magic-conjecture-is-false.lean

  Measured 2026-08-31: exit 0, 0 errors.
-/
import QOU.Interactions.LRFusion

namespace DoubleMagicRefutation
open QOU.Interactions.LRFusion QOU.BraidKnot.ShellNeutrality
  QOU.LiftingDescent.HomologicalCondensation

/-- The all-empty composite: `|λ_A| = |λ_Z| + |λ_N|` reads `0 = 0 + 0`. -/
def emptyComposite : Composite where
  ydZ := emptyDiagram
  ydN := emptyDiagram
  ydA := emptyDiagram
  mass_eq := by simp [emptyDiagram]

/-- **Half one of the original refutation.** Under the OLD definition —
`isSelfConjugate ydZ ∧ isSelfConjugate ydN`, with no saturation — the empty
composite is double-magic. -/
theorem emptyComposite_old_isDoubleMagic :
    isSelfConjugate emptyComposite.ydZ ∧ isSelfConjugate emptyComposite.ydN :=
  ⟨emptyDiagram_isSelfConjugate, emptyDiagram_isSelfConjugate⟩

/-- **Half two.** `0` is not on the magic ladder, so the removed field's
`A ∈ magicLadder` conjunct failed there. -/
theorem zero_not_in_magicLadder : (0 : ℕ) ∉ magicLadder := by
  unfold magicLadder QOU.Common.magicSet
  simp

/-- **The repair closes the hole.** With saturation in the definition, the empty
composite is no longer double-magic. -/
theorem emptyComposite_not_isDoubleMagic : ¬ IsDoubleMagic emptyComposite := by
  simp [IsDoubleMagic, emptyComposite, emptyDiagram, magicLadder,
    QOU.Common.magicSet]

/-- **The removed conjunct was false at every intended instance.** Over all
`7 × 7` magic pairs, the only one whose sum is again magic is `8 + 20 = 28`; in
particular no `(Z, N)` with `Z = N` qualifies, so ⁴He, ¹⁶O, ⁴⁰Ca and ⁵⁶Ni are
all counterexamples to `A ∈ magicLadder`. -/
theorem magic_sum_is_almost_never_magic :
    (QOU.Common.magicSet ×ˢ QOU.Common.magicSet).filter
        (fun p => p.1 + p.2 ∈ QOU.Common.magicSet)
      = {(8, 20), (20, 8)} := by
  decide

end DoubleMagicRefutation
