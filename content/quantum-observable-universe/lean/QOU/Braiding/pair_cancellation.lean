/-
  Pair cancellation: the symmetric channels cancel, the antisymmetric add.

  RELOCATED (no mathematical change).  `pair_cancellation` was declared in
  `content/quantum-observable-universe/observations/crossing-energy-decomposition.lean`, a
  chapter-directory `.lean` belonging to a different content block, so the content-block
  resolver found it via neither candidate 1 (the citing block's own sibling) nor candidate 2
  (`<lakeRoot>/<Decl/Path>.lean`).  Moving it to the path matching its namespace makes candidate
  2 resolve.

  The declaration below is verbatim as it stood in the source file — same statement, same proof,
  same `-- Ref:` citations.
-/

import QOU.Braiding.crossing_energy_channels

namespace QOU.Braiding

/-- **Pair cancellation.** For a composite and its mirror, the symmetric
(strong) channels cancel and the antisymmetric (Coulomb) channels add:

  `𝔈(𝔥) + 𝔈(𝔥^σ) = 2·E_asym(𝔥)`.

This is the formal content of the QOU analogue of Einstein's hope for
`g_[μν]`: the sign-blind antisymmetric sector is what survives when the
symmetric sector is cancelled by pairing. -/
-- Ref: [manuscript] Ch. 7, §crossing-energy-decomposition
theorem pair_cancellation (p m : ℕ) (q : ℝ) :
    crossingEnergy p m q + crossingEnergy m p q = 2 * asymChannel p m q := by
  unfold crossingEnergy asymChannel antisymmetricWeight
  ring

end QOU.Braiding
