/-
  The H₂ covalent bond word under the one γγ rule (owner ruling 2026-11-15).

  Bond words are selected like every other canonical word: γγ construction plus
  reading-3 confinement.  The word the earlier knot-list selection chose, the
  inverse trefoil σ₀⁻¹σ₁⁻¹σ₀⁻¹, has three letters, and every γγ word has even
  length, so the inverse trefoil is not admissible as a bond word.  Which γγ
  word IS selected is a computation (witness `h2-gg-electron`), recorded in the
  narrative of prop:ilp-covalent-bond.

  Replaced here: `covalent_bond_is_ilp_optimal : inverse_trefoil.length = 3 := rfl`
  (it proved the length, not optimality) and `axiom h2_binding_energy`
  (`∃ E, 0 < E ∧ E < 5`, which holds for E = 1 and says nothing about H₂).

  Ref: [leitner2026] Ch 12 §1, prop:ilp-covalent-bond; bean qou-ales
-/

import QOU.QBeta.GammaGammaSelectedDeltaVanishes

namespace QOU.Molecular

open QOU.Mass.GammaGammaWordSelection QOU.QBeta.GammaGammaDelta

/-- The inverse trefoil braid word σ₀⁻¹σ₁⁻¹σ₀⁻¹. -/
def inverse_trefoil : Word := [⟨0, false⟩, ⟨1, false⟩, ⟨0, false⟩]

/-- **The inverse trefoil is not a γγ word**: it has odd length, and every γγ
word has even length (`gammaGamma_length_even`).  So under the one γγ rule it
cannot be the H₂ bond word. -/
theorem inverse_trefoil_not_gammaGamma : ¬ GammaGammaWord inverse_trefoil :=
  not_gammaGamma_of_odd_length (by decide)

/-- **The γγ bond letter V³ is a γγ word**: three pair-production vertices at
the junction site `s`. -/
theorem bond_V3_gammaGamma (s : ℕ) :
    GammaGammaWord (vertex s ++ (vertex s ++ (vertex s ++ []))) :=
  .cons s (.cons s (.cons s .nil))

end QOU.Molecular
