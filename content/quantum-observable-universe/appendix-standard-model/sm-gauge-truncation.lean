import Mathlib.LinearAlgebra.UnitaryGroup
import Mathlib.Data.Complex.Basic

/-!
# Conjecture: Standard-Model truncation of the gauge symmetry

The archimedean (observable-scale) truncation of the categorical
gauge symmetry is conjectured to contain the Standard Model gauge
group `SU(3) × SU(2) × U(1)`. This file states that containment as
a content-bearing conjecture class over an abstract group `G`
(intended: the archimedean image of the gauge symmetry under the
fibre functor `τ`).

This is a **primary conjecture** (AGENTS.md §3b-tax): its signature
binds no other conjecture class. No instance is provided — the open
state is a content-bearing class with no instance.

The archimedean base `ℂ` is genuinely required (AGENTS.md §7c):
`SU(3)`, `SU(2)`, `U(1)` are archimedean Lie groups, and this class
lives on the observable side of the substrate→archimedean wall. The
statement is deliberately *containment*, not isomorphism: the
truncation may carry additional symmetry (and the physical SM group
is the quotient `(SU(3) × SU(2) × U(1))/ℤ₆` in some conventions);
an isomorphism claim would overstate what the framework currently
supports.

## References

- [manuscript] Appendix: Toward the Standard Model
- [baez2004] Baez–Lauda, Higher-dimensional algebra V: 2-groups
-/

namespace QOU.StandardModel

/-- **Conjecture (Standard-Model truncation).** The group `G`
(intended: the archimedean truncation of the QOU gauge symmetry)
contains an embedded copy of `SU(3) × SU(2) × U(1)`: there is an
injective group homomorphism from the product into `G`.

Falsifiable content: the field fails for any `G` too small or too
commutative to host the product (e.g. any abelian `G`, since
`SU(3)` is non-abelian and homomorphic images of non-abelian simple
compact groups in abelian groups kill them, breaking injectivity). -/
class StandardModelTruncation (G : Type*) [Group G] : Prop where
  /-- `SU(3) × SU(2) × U(1)` embeds in `G`. -/
  sm_embeds :
    ∃ φ : (Matrix.specialUnitaryGroup (Fin 3) ℂ ×
           Matrix.specialUnitaryGroup (Fin 2) ℂ ×
           unitary ℂ) →* G,
      Function.Injective φ

end QOU.StandardModel
