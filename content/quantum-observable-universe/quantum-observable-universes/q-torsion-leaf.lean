import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.LinearAlgebra.ExteriorAlgebra.Basic


/-!
# QOU.QTorsionLeaf

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/QTorsionLeaf.lean (monolithic)

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

universe u v

/-- **Reeb decomposition** `α = α_H + α_V` of a differential form on a CR
    manifold (local prerequisite for the leaf integrality condition; the
    library counterpart is `QOU.ReebDecomposition`). -/
structure ReebDecomposition (M : Type*) where
  /-- The total form (abstract representative). -/
  total : M → ℝ
  /-- Horizontal component `α_H` satisfying `ι_ξ α_H = 0`. -/
  horizontal : M → ℝ
  /-- Vertical component `α_V = θ ∧ ι_ξ α`. -/
  vertical : M → ℝ
  /-- Decomposition identity: `total = horizontal + vertical`. -/
  decomp : ∀ (p : M), total p = horizontal p + vertical p

/-- **q-deformed Reeb flow** (local prerequisite, mirroring `QOU.QReebFlow`).

    Flow time is `ℝ`. This docstring used to say "over the ground ring `R_q`"
    and to note, without resolving it, that *"the library counterpart
    `QOU.QReebFlow` evaluates time over `ℝ`"* — a divergence recorded in prose
    and enforced by nothing (bean `qou-u87j`). `q-reeb-flow.md` settles it in
    favour of `ℝ`: the flow is defined "in the archimedean realisation" by the
    ODE `d/dt φ_t^q = ξ_q ∘ φ_t^q`. The `q` deforms the vector field, not the
    time parameter. -/
structure QReebFlow (M : Type*) where
  /-- The flow map at time `t : ℝ`. -/
  flow : ℝ → M → M
  /-- Initial condition: `φ^q_0 = id`. -/
  flow_zero : ∀ (p : M), flow 0 p = p

/-- **q-Torsion leaf**: a maximal integral submanifold `L ↪ M` of `H`
    that is invariant under the q-deformed Reeb flow.

    LaTeX: `\label{def:q-torsion-leaf}` -/
structure QTorsionLeaf (M : Type*) where
  /-- The leaf as a subset of `M`. -/
  leaf : Set M
  /-- The leaf is non-empty. -/
  nonempty : leaf.Nonempty
  /-- Tangent inclusion `T_p L ⊂ H_p` for all `p ∈ L` (integrality of the
      horizontal distribution).  Formalised as: for any Reeb decomposition
      with the leaf as support, the vertical component vanishes on the leaf. -/
  tangent_in_horizontal : ∀ (rd : ReebDecomposition M),
    (∀ p, p ∈ leaf → rd.vertical p = 0)
  /-- Flow invariance: `φ^q_t(L) = L` for all `t ∈ ℝ`.

      The binder said `t : R_q` while this docstring said `t ∈ ℝ` — the prose
      was right and the type was not. -/
  flow_invariant : ∀ (qrf : QReebFlow M) (t : ℝ),
    ∀ (p : M), p ∈ leaf → qrf.flow t p ∈ leaf

end

end QOU
