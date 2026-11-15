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

open QOU.Archimedean

/-- **Dressed particle.** Codomain of a dressing morphism; carries
    a bare-particle core, an electron shell, and the composite
    confined particle whose Markov class is that of
    `ι(K_bare) · W_bind` in `H_{A+Z}(q)`. -/
-- Ref: [leitner2026] braids-and-knots/dressed-particle
structure DressedParticle where
  /-- Bare nuclear confined particle. -/
  bare : ConfinedParticle
  /-- Electron shell attached to `bare`. -/
  shell : ElectronShell
  /-- The composite confined particle obtained after dressing. -/
  composite : ConfinedParticle
  /-- Consistency: the shell's nucleus is the bare particle. -/
  shell_on_bare : shell.nucleus = bare
  /-- Level preservation: dressing does not change the level. -/
  level_preserved : composite.level = bare.level

/-- The dressing morphism `dress_S : P_bare → P_dressed` in
    the confinement category. -/
-- Ref: [leitner2026] braids-and-knots/dressed-particle
noncomputable def dressMorphism (D : DressedParticle) :
    ConfMorphism D.bare D.composite :=
  ConfMorphism.dress D.bare D.composite D.shell.nucleus.name

/-- **Dressing composition** — proved from the structure fields.
    Each `DressedParticle` carries `level_preserved`; chaining via
    `D₁.composite = D₂.bare` then gives the equality by `rfl`/`rw`.
    The earlier `DressingComposes` typeclass has been removed. -/
-- Ref: [leitner2026] braids-and-knots/dressed-particle
theorem dressing_composes
    (D₁ D₂ : DressedParticle)
    (h_chain : D₁.composite = D₂.bare) :
    D₂.composite.level = D₁.bare.level := by
  rw [D₂.level_preserved, ← h_chain, D₁.level_preserved]

end QOU.BraidKnot
