/-
  Surreal blow-up calculus.

  Named infinite/infinitesimal surreals replacing informal ∞
  in physics renormalisation arguments.

  ## References
  - [conway1976] Conway, *On Numbers and Games*, Academic Press.
  - [ehrlich2012] Ehrlich, *The absolute arithmetic continuum*,
    Bull. Symbolic Logic 18 (2012) 1-45.
    https://doi.org/10.2178/bsl/1327328438
-/

import Mathlib.SetTheory.Ordinal.Basic

namespace QOU.AppendixSurreals

universe u

variable (K : Type u) [SurrealField K]

/-- The first infinite surreal: `ω = 1 + 1 + ⋯`.  In the
    Conway construction, this is the simplest surreal larger
    than every natural number. -/
-- Ref: [conway1976] §0
noncomputable def omegaSurreal : K :=
  -- Existence: K extends ℝ ∪ Ord, so ω ∈ K.
  -- Ref: [ehrlich2012] Theorem 12.5 — every ordinal embeds in K.
  sorry

/-- The first positive infinitesimal: `ε = 1/ω`. -/
-- Ref: [conway1976] §0
noncomputable def epsilonSurreal : K :=
  (omegaSurreal K)⁻¹

/-- A **renormalisation cutoff** is a choice of named infinite
    surreal serving as the upper limit of integration / sum. -/
structure Cutoff where
  /-- The cutoff value (typically `omegaSurreal` or a power thereof). -/
  value : K
  /-- The cutoff is genuinely infinite. -/
  is_infinite : ∀ n : ℕ, (n : K) < value

/-- A **counterterm** is a function from cutoffs to surreals,
    designed so that subtracting it from the divergent expression
    yields a finite surreal. -/
abbrev Counterterm := Cutoff (K := K) → K

/-- The **renormalised value** of a divergent expression
    `X : Cutoff → K` with counterterm `C` at the canonical
    cutoff `ω` is `st(X(ω) - C(ω))`. -/
-- Ref: [conway1976], [ehrlich2012]
noncomputable def renormalisedValue
    (X : @Cutoff K _ → K) (C : @Counterterm K _) : ℝ :=
  let cutoff : @Cutoff K _ :=
    { value := omegaSurreal K
      is_infinite := by
        -- Ref: [conway1976] §0 — ω > every natural
        sorry }
  -- standardPart is from `standard-part-functor.lean`
  -- Ref: [robinson1966] §3.2
  sorry

end QOU.AppendixSurreals
