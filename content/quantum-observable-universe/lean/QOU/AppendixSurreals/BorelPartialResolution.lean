import QOU.Infra.BorelRank

/-!
# Borel partial resolution of the keystone sharpness target

Compiled formalisation of `prop:borel-partial-resolution`.
Sibling docstub at `appendix-surreals/borel-partial-resolution.lean`.
-/

namespace QOU.AppendixSurreals.BorelPartialResolution

open QOU.Infra.BorelRank

/-- **Proposition (`prop:borel-partial-resolution`,
    arithmetic core).**
    The Borel rank `borelRankPredicted n r1 r2` is well-defined
    at every `n ≥ 2`; substantive identification with
    `K_{2n-1}^{ind}(F) ⊗ ℚ` is the `BorelRank F` class. -/
theorem borel_partial (n r1 r2 : ℕ) (_ : 2 ≤ n) :
    borelRankPredicted n r1 r2 =
        (if n % 2 = 0 then r1 + r2 else r2) := by
  rfl

end QOU.AppendixSurreals.BorelPartialResolution
