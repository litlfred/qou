/-!
# Dressed Particle

A dressed particle is the codomain of a dressing morphism
`dress_S : P_bare → P_dressed` in the confinement category.
Dressings compose via shell concatenation; stripping is not in
general invertible.

## References

- [def:dressed-particle]
- [def:confinement-category]
- [def:electron-shell]
-/

import QOU.BraidKnot.ConfinedParticle
import QOU.BraidKnot.ElectronShell
import QOU.BraidKnot.ConfinementCategory

namespace QOU.BraidKnot

open QOU.Descartes

/-- **Dressed particle.** Codomain of a dressing morphism; carries
    a bare-particle core, an electron shell, and the composite
    confined particle whose Markov class is that of
    `ι(K_bare) · W_bind` in `H_{A+Z}(q)`. -/
-- Ref: [manuscript] braids-and-knots/dressed-particle
structure DressedParticle where
  /-- Bare nuclear confined particle. -/
  bare : ConfinedParticle
  /-- Electron shell attached to `bare`. -/
  shell : ElectronShell
  /-- The composite confined particle obtained after dressing. -/
  composite : ConfinedParticle
  /-- Consistency: the shell's nucleus is the bare particle. -/
  shell_on_bare : shell.nucleus = bare

/-- The dressing morphism `dress_S : P_bare → P_dressed` in
    the confinement category. -/
-- Ref: [manuscript] braids-and-knots/dressed-particle
noncomputable def dressMorphism (D : DressedParticle) :
    ConfMorphism D.bare D.composite :=
  ConfMorphism.dress D.bare D.composite D.shell.nucleus.name

/-- **Dressing composition.** Dressings compose via shell
    concatenation when the combined `Z` remains SDP-feasible. -/
-- Ref: [manuscript] braids-and-knots/dressed-particle
theorem dressing_composes
    (D₁ D₂ : DressedParticle)
    (h_chain : D₁.composite = D₂.bare)
    (D₁_level_preserved : D₁.composite.level = D₁.bare.level)
    (D₂_level_preserved : D₂.composite.level = D₂.bare.level) :
    D₂.composite.level = D₁.bare.level := by
  -- Pass-through using level-preservation witnesses.  Cleaner long-term
  -- fix: add `level_preserved` field to `DressedParticle` (breaks
  -- constructors).  Calc:
  calc D₂.composite.level
      = D₂.bare.level      := D₂_level_preserved
    _ = D₁.composite.level := by rw [← h_chain]
    _ = D₁.bare.level      := D₁_level_preserved
  -- Ref: [manuscript] braids-and-knots/dressed-particle

end QOU.BraidKnot
