import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
# QOU.AlgebraicSubstrate.QVonMangoldtFunction

**Canonical declaration** for content block at
[`quantum-observable-universe/q-geometric-langlands/q-von-mangoldt-function.ts`](quantum-observable-universe/q-geometric-langlands/q-von-mangoldt-function.ts).

Formalises the manuscript **definition** of the q-von Mangoldt function
`Λ_q` over the maximal ideals `𝔪` of the coordinate ring `𝒪_q(𝓑)`
(§7c: archimedean over `ℝ`, since the weight `N(𝔪)^{ℏ_q}` is a real power).
-/

namespace QOU.AlgebraicSubstrate

/-- Data for the q-von Mangoldt function `Λ_q`.

    A `definition` carrier: `Idx` indexes the maximal ideals `𝔪`, `N 𝔪` is
    the norm (residue-field cardinality), `isFundamentalDefect` marks the
    ideals lying over a prime of the centre, and `Lambda_q` is pinned by its
    defining piecewise value — the `q`-deformation `(N 𝔪 ^ ℏ_q − 1)/ℏ_q` of
    `log N(𝔪)` on defects, `0` otherwise. -/
structure QVonMangoldtFunction where
  /-- Index type for the maximal ideals `𝔪` of `𝒪_q(𝓑)`. -/
  Idx : Type
  /-- Norm `N(𝔪)` — the residue-field cardinality. -/
  N : Idx → ℝ
  /-- Substrate `q`-Planck constant `ℏ_q`. -/
  hbar_q : ℝ
  /-- Whether `𝔪` is a fundamental defect (lies over a prime of the centre). -/
  isFundamentalDefect : Idx → Prop
  /-- Decidability of the defect predicate (so the piecewise value is a term). -/
  [decidableDefect : DecidablePred isFundamentalDefect]
  /-- The q-von Mangoldt function. -/
  Lambda_q : Idx → ℝ
  /-- Defining identity: `Λ_q(𝔪) = (N 𝔪 ^ ℏ_q − 1)/ℏ_q` on defects, else `0`. -/
  lambda_def : ∀ m,
    Lambda_q m =
      if isFundamentalDefect m then (N m ^ hbar_q - 1) / hbar_q else 0

attribute [instance] QVonMangoldtFunction.decidableDefect

-- Ref: [leitner2026] quantum-observable-universe/q-geometric-langlands/q-von-mangoldt-function.ts

/-- The q-von Mangoldt weight vanishes off the fundamental defects. -/
theorem vanishes_off_defect
    (Λ : QVonMangoldtFunction) (m : Λ.Idx) (h : ¬ Λ.isFundamentalDefect m) :
    Λ.Lambda_q m = 0 := by
  rw [Λ.lambda_def m, if_neg h]

end QOU.AlgebraicSubstrate
