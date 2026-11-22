import QOU.Basic
import QOU.BraidKnot.DressedParticle

/-!
# QOU.BraidKnot.DressedParticle

A dressed particle is the codomain of a dressing morphism
`P_bare → P_dressed` in the confinement category. Dressings compose
via shell concatenation; stripping is not in general invertible.

The canonical structure lives in `QOU.BraidKnot.DressedParticle` (imported
above), which the `.ts` manifest's `lean.ref` resolves to. This content-extract
file confirms the canonical declarations are in scope rather than shadowing
them with re-declarations (AGENTS.md §0a no-shadowing-stubs).

**This file previously shadowed that library module with a weaker copy.** It
declared its own `BareTy`, `ShellTy` and a plain `DressedParticle` whose
`level` was a **free field**, plus
`axiom DressedParticle.level_canonical_under_bare` asserting that two records
sharing a `bare` core share a `level`. That axiom was **false** — the fields
were independent — and its own docstring said so: *"Pending a structure
refactor carrying canonicity as a proof field."*

The library had already done that refactor. Its `DressedParticle` carries
`shell_on_bare` and `level_preserved` as **proof fields**, and proves
`dressing_composes` from them with no axiom. So nothing is lost by deleting the
shadow: the composition result the axiom was propping up is stronger in the
library, and reaches this block by resolution. Bean `qou-i6u4`.

LaTeX: `\label{def:dressed-particle}`
-/

namespace QOU.BraidKnot

-- Witness that the canonical declarations are in scope (no re-declaration).
-- canonical decls: QOU.BraidKnot.DressedParticle, QOU.BraidKnot.dressing_composes
-- Ref: [leitner2026] braids-and-knots/dressed-particle
example (D : DressedParticle) : D.composite.level = D.bare.level :=
  D.level_preserved

example (D₁ D₂ : DressedParticle) (h_chain : D₁.composite = D₂.bare) :
    D₂.composite.level = D₁.bare.level :=
  dressing_composes D₁ D₂ h_chain

end QOU.BraidKnot
