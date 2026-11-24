import Mathlib.Data.Nat.Notation

/-!
# QOU.Torsion.brane_boundary_structure — four properties of `∂A_n`

**Proposition** ([`prop:brane-boundary-structure`](../../../quantum-observable-universe/lifting-and-descent/brane-boundary-structure.md)).

*The defining boundary `∂A_n` has the following properties:*

*(1) **Codimension**: `∂A_n` is a closed subset of real codimension
≥ 2 in `𝓢_n`.*

*(2) **Exceptional object**: at each degeneration locus of `r_n`,
`ker(r_n|_S) ≅` a simple object of `𝐂` (archimedean: `ℙ¹(ℂ) ≅ S²`).*

*(3) **Involution symmetry**: the descent involution `τ̂_n` restricts
to an endomorphism of `∂A_n`, whose fixed subobjects coincide with
the monodromy fixed points of the quantum characteristic classes.*

*(4) **Chirality interface** (archimedean, `n = 1`): `∂𝓢_1`
separates macroscopic spacetime coordinates from internal chiral
modes; the Reeb involution `ξ ↦ −ξ` reverses orientation across it.*

The Lean encoding records the four properties as fields of an
abstract `BraneBoundaryContext`.

-- Ref: [leitner2026] quantum-observable-universe/lifting-and-descent/brane-boundary-structure.md
-/

namespace QOU.Torsion

/-- Abstract context for the brane-boundary structural lemma. -/
class BraneBoundaryContext where
  /-- The level `n`. -/
  n : ℕ
  /-- The boundary object `∂A_n`. -/
  boundary : Type
  /-- The "codimension at least 2" predicate. -/
  Codim_at_least_2 : Prop
  /-- The "exceptional kernel" predicate. -/
  ExceptionalKernel : Prop
  /-- The "involution symmetry" predicate. -/
  InvolutionSymmetric : Prop
  /-- The "chirality interface" predicate (only meaningful at `n = 1`). -/
  ChiralityInterface : Prop
  /-- Proposition: the brane boundary structure is regular. -/
  brane_boundary_regular : Prop
  /-- Hypothesis that the boundary is regular. -/
  boundary_active : brane_boundary_regular
  /-- Manuscript four-property structural lemma for `∂A_n`. -/
  impl_brane_boundary_structure :
    brane_boundary_regular →
    Codim_at_least_2 ∧ ExceptionalKernel ∧
    InvolutionSymmetric ∧ ChiralityInterface

/-- **Brane-boundary structure** ([`prop:brane-boundary-structure`]).

    All four structural properties hold for the boundary `∂A_n`. -/
-- Ref: [leitner2026] quantum-observable-universe/lifting-and-descent/brane-boundary-structure.md
theorem brane_boundary_structure [ctx : BraneBoundaryContext] :
    ctx.Codim_at_least_2 ∧
    ctx.ExceptionalKernel ∧
    ctx.InvolutionSymmetric ∧
    ctx.ChiralityInterface := by
  have h := ctx.boundary_active
  exact ctx.impl_brane_boundary_structure h

end QOU.Torsion
