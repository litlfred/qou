import QOU.BraidKnot.ConfinedParticle
import QOU.BraidKnot.ElectronShell
import QOU.BraidKnot.ConfinementCategory

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
    concatenation when the combined `Z` remains SDP-feasible.
    Axiomatised until `DressedParticle` carries a `level_preserved`
    field. -/
-- Ref: [manuscript] braids-and-knots/dressed-particle
axiom dressing_composes
    (D₁ D₂ : DressedParticle)
    (h_chain : D₁.composite = D₂.bare) :
    D₂.composite.level = D₁.bare.level

end QOU.BraidKnot
