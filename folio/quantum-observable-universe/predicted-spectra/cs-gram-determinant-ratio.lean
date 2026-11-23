import QOU.Archimedean.GramDetRatioCongruence

/-!
# QOU.Archimedean.csGramDetRatio

`def:cs-gram-determinant-ratio`: the Gram-determinant ratio
`κ := det G_cl / det G_q` of two bilinear forms written in one basis.
The Chern–Simons instance takes the classical and `q`-deformed CS
pairings on the force-carrier sublattice.

Base ring: any field (§7c); nothing archimedean is used.

-- Ref: [leitner2026] §5/cs-gram-determinant-ratio
-/

namespace QOU.Archimedean

open Matrix

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- The Gram-determinant ratio `κ = det Gcl / det Gq`. -/
def csGramDetRatio {K : Type*} [Field K] (Gcl Gq : Matrix n n K) : K :=
  Gcl.det / Gq.det

/-- `κ` is unchanged when both forms are transported by the same
invertible change of basis. -/
theorem csGramDetRatio_congr {K : Type*} [Field K]
    (B Gcl Gq : Matrix n n K) (hB : B.det ≠ 0) :
    csGramDetRatio (Bᵀ * Gcl * B) (Bᵀ * Gq * B) = csGramDetRatio Gcl Gq :=
  gramDetRatio_congr_invariant B Gcl Gq hB

end QOU.Archimedean
