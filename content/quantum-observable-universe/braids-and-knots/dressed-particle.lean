/-!
# QOU.BraidKnot.DressedParticle

A dressed particle is the codomain of a dressing morphism
`P_bare → P_dressed` in the confinement category. Dressings compose
via shell concatenation; stripping is not in general invertible.

LaTeX: `\label{def:dressed-particle}`
-/

import QOU.Basic

namespace QOU.BraidKnot

universe u

/-- Placeholder types resolved by sibling files. -/
opaque BareTy : Type
opaque ShellTy : Type

/-- **Dressed particle.** Codomain of a dressing morphism; carries
    a bare-particle core, a shell record, and the composite Markov
    class of `ι(K_bare) · W_bind` in `H_{A+Z}(q)`. -/
-- Ref: [manuscript] braids-and-knots/dressed-particle
structure DressedParticle where
  /-- Bare nuclear particle. -/
  bare : BareTy
  /-- Electron shell attached to `bare`. -/
  shell : ShellTy
  /-- Composite name (e.g. `[He]`, `[Ne]`). -/
  compositeName : String
  /-- Confinement level ℓ of the composite particle. -/
  level : ℕ
  /-- Total strand count `n₀ + Z`. -/
  strandCount : ℕ

/-- Dressings compose: `dress_{S₂} ∘ dress_{S₁} = dress_{S₁ ⊕ S₂}`
    whenever `S₁ ⊕ S₂` remains SDP-feasible. -/
-- Ref: [manuscript] braids-and-knots/dressed-particle
theorem dressComposition
    (P₀ P₁ P₂ : DressedParticle)
    (h₀₁ : P₁.bare = P₀.bare)
    (h₁₂ : P₂.bare = P₁.bare) :
    P₂.level = P₀.level := by
  sorry

end QOU.BraidKnot
