/-!
# QOU.Braiding.knot_particle_correspondence — Knot--particle correspondence via q-Schur--Weyl duality

The Markov trace on the Hecke algebra H_n(q) assigns to each irreducible
summand of V^{⊗n} a knot type, establishing a bijection between irreducible
representations and knot/link types arising as braid closures.

## References

- [manuscript] Ch. 4, §10
- [jones1987] https://doi.org/10.2307/1971403
-/

import Mathlib.Data.Real.Basic

namespace QOU.Braiding

-- Ref: [manuscript] Ch. 4, §10
-- Ref: [jones1987] https://doi.org/10.2307/1971403
/-- Irreducible summands of V^{⊗n} under q-Schur-Weyl duality,
    labelled by partitions λ ⊢ n. -/
axiom IrrepSummand (n : ℕ) : Type
/-- Knot/link types arising as closures of n-strand braids. -/
axiom KnotType (n : ℕ) : Type
/-- The Markov trace map from irreducible summands to knot types. -/
axiom markovTraceMap (n : ℕ) : IrrepSummand n → KnotType n

theorem knot_particle_correspondence (n : ℕ) :
    -- The Markov trace on H_n(q) induces a bijection between irreducible
    -- summands of V^{⊗n} and knot types arising as closures of n-strand braids.
    Function.Bijective (markovTraceMap n) := by
  -- Ref: [manuscript] Ch. 4, §10
  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  sorry

end QOU.Braiding
