import QOU.Eightfold.HeckeBraidingNonSymmetric
import QOU.MassTheory.TraceSignFlipRegime

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

/-- **The trace tower is not sign-flip invariant at the substrate.**

`rem:isospin-mass-split-em-localisation` lists the trace tower among the
functionals that *"respect these structural involutions"*, and uses that to
localise the mirror-isobar mass split entirely into the Coulomb sector. At any
real `q > 1` — the substrate included — this says the premise is false for that
sector: flipping a generator's sign changes the trace.

The remark's cited support, `prop:crystal-isospin-degeneracy`, is a **crystal
limit `q → 0`** statement, and remains true there. Both facts hold; what does not
hold is carrying the `q → 0` invariance across to the functional at `q₀`. The
size of the failure is `(q − q⁻¹) · tr 1`, about `0.209 · tr 1` at
`q₀ ≈ 1.10998`, so it is not a negligible-correction argument either.

Scope-(a), and narrow: this refutes one premise for one sector at one regime. It
does not touch the co-Casimir or chirality sectors, and it does not refute the
remark's conclusion — the split may still be entirely Coulomb-sourced. -/
theorem trace_not_sign_flip_invariant_of_q_gt_one {B : Type*} [Ring B] [Algebra ℝ B]
    (q : ℝ) (σ τ : B) (tr : B →ₗ[ℝ] ℝ) (hq : 1 < q) (htr : tr 1 ≠ 0)
    (hHecke : σ ^ 2 = algebraMap ℝ B (q - q⁻¹) * σ + 1) (hinv : σ * τ = 1) :
    tr τ ≠ tr σ := by
  have hq0 : q ≠ 0 := by positivity
  intro h
  have h2 : q ^ 2 = 1 :=
    (QOU.MassTheory.TraceSignFlipRegime.trace_sign_flip_iff_symmetric
      q σ τ tr hq0 htr hHecke hinv).mp h
  nlinarith [h2]

end QOU.Archimedean.HeckeBraidingSubstrateNonSymmetric
