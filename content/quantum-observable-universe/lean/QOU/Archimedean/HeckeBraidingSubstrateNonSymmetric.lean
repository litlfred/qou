import QOU.Eightfold.HeckeBraidingNonSymmetric

/-!
# QOU.Archimedean.HeckeBraidingSubstrateNonSymmetric — the substrate braiding is not symmetric

Bean `qou-tzfm`. The **archimedean** half of
`QOU.Eightfold.HeckeBraidingNonSymmetric`, split off per AGENTS.md §7c: the
generic gate is stated over an arbitrary field and an arbitrary algebra over it
and mentions no ordering; this file is where `ℝ` and `1 < q` enter, and it does
nothing but instantiate.

## Why the framework needs it

`docs/audits/2026-08-25-4a-question-imports-symmetric-theory.md` observes that
the eightfold surface's surviving question — *"can the gerbe's band be
`SU(3)`?"* — is stated in **symmetric**-category machinery, while QOU's category
is not symmetric. The corpus previously carried that non-symmetry as prose
(`qou-definition-intro.md`). Here it is a consequence: the Hecke relation makes
the double braiding trivial **only** at `q² = 1`, and the substrate sits at
`q₀ ≈ 1.10998 > 1`.

What is *not* claimed: that this excludes `SU(3)` from the framework. It
establishes the hypothesis under which the symmetric machinery does not apply,
and nothing further. See the audit's §4.
-/

namespace QOU.Archimedean.HeckeBraidingSubstrateNonSymmetric

open QOU.Eightfold.HeckeBraidingNonSymmetric

/-- **Archimedean corollary** (the wall is crossed here, and only here: `ℝ`
appears because the substrate value is a real number, per §7c).

At any real `q > 1` the double braiding is not the identity. The substrate sits
at `q₀ ≈ 1.10998`, so the QOU braiding is non-symmetric — which is what the
audit needs, and it is a consequence of the Hecke relation rather than a
stipulation. -/
theorem q_gt_one_double_braiding_ne_one {B : Type*} [Ring B] [Algebra ℝ B]
    (q : ℝ) (σ : B) (hq : 1 < q)
    (hfree : ∀ r : ℝ, algebraMap ℝ B r * σ = 0 → r = 0)
    (hHecke : σ ^ 2 = algebraMap ℝ B (q - q⁻¹) * σ + 1) :
    σ ^ 2 ≠ 1 := by
  have hq0 : q ≠ 0 := by positivity
  intro hs
  have h2 : q ^ 2 = 1 := (double_braiding_eq_one_iff q σ hq0 hfree hHecke).mp hs
  nlinarith [h2]

end QOU.Archimedean.HeckeBraidingSubstrateNonSymmetric
