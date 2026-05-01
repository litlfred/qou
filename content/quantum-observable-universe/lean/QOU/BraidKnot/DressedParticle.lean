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

/-- **Dressing composition — typeclass (Pattern 4).**

    Witnesses level preservation under dressing concatenation, *for
    a specific compatible pair*. The cleaner long-term fix adds a
    `level_preserved` field to `DressedParticle`; until then the
    obligation is per-instance, not universal. -/
-- Ref: [manuscript] braids-and-knots/dressed-particle
class DressingComposes (D₁ D₂ : DressedParticle)
    (_h_chain : D₁.composite = D₂.bare) : Prop where
  /-- Level is preserved through the composition. -/
  level_eq : D₂.composite.level = D₁.bare.level

/-- **Dressing composition** (per-instance form).
    Use this lemma — backed by `DressingComposes` — instead of the
    deprecated universal axiom. -/
-- Ref: [manuscript] braids-and-knots/dressed-particle
theorem dressing_composes
    (D₁ D₂ : DressedParticle)
    (h_chain : D₁.composite = D₂.bare)
    [h : DressingComposes D₁ D₂ h_chain] :
    D₂.composite.level = D₁.bare.level :=
  h.level_eq

end QOU.BraidKnot
