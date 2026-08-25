import QOU.Infra.BorelRank

/-!
# Borel partial resolution of the keystone sharpness target

Compiled formalisation of `prop:borel-partial-resolution`.
Sibling docstub at `appendix-surreals/borel-partial-resolution.lean`.
-/

namespace QOU.AppendixSurreals.BorelPartialResolution

open QOU.Infra.BorelRank

/-- **Definitional unfolding of `borelRankPredicted`** (`prop:borel-partial-resolution`,
    arithmetic core). `borelRankPredicted n r1 r2` evaluates to `r1 + r2` for even `n` and
    `r2` for odd `n` — a rewrite lemma exposing the definition, holding for every `n` (the
    earlier `2 ≤ n` hypothesis was unused decoration and is dropped). The *substantive*
    identification with `K_{2n-1}^{ind}(F) ⊗ ℚ` is the (unproved) `BorelRank F` class, NOT
    this equation. -/
theorem borel_partial (n r1 r2 : ℕ) :
    borelRankPredicted n r1 r2 =
        (if n % 2 = 0 then r1 + r2 else r2) := by
  rfl

end QOU.AppendixSurreals.BorelPartialResolution
