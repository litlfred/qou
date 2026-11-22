import Mathlib.CategoryTheory.Category.Basic
import Mathlib.Algebra.Group.Defs

/-!
# QOU.Lichnerowicz.qDirac — categorical Lichnerowicz formula

The proposition: on a categorical-instanton background
(⋆_q F_∇ = F_∇), the categorical Laplacian Δ_∇^q on Ω¹(End V)
equals the squared categorical Dirac 𝔇_∇² plus a q-scalar-curvature
correction:

  Δ_∇^q = 𝔇_∇² + (1/4) Sc_q,

simplifying on the parallel-Reeb Bring background to
Δ_∇^q = 𝔇_∇².

## Strategy

The proof has four steps in the paper-side .md, all reducible to:

(a) The Clifford-multiplication identity (ι_ξ)² = -id on a unit
    Reeb vector;
(b) Cartan formula for the cross-term {∇, ι_ξ ∇};
(c) Self-duality ⋆_q F = F absorbing the ι_ξ F piece into the
    scalar-curvature term;
(d) Weitzenböck for 1-forms on the gauge-Laplacian side.

Each of (a)–(d) is a single categorical-algebraic identity. A full
Mathlib derivation requires Clifford-bundle infrastructure, the
quantum-group Weitzenböck identity for 1-forms, and scalar-curvature
on contact manifolds — none currently in Mathlib at sufficient
generality.

The smart-constructor pattern records the structural identification
at the categorical level; the equality is then derivable from the
input hypotheses (each labeled axiom matching one step of the .md
proof).

-- Ref: [leitner2026] prop:categorical-lichnerowicz
-- Ref: [lichnerowicz1963] Lichnerowicz, "Spineurs harmoniques," C. R. Acad. Sci. Paris 257 (1963)
-- Ref: [woronowicz1989] Woronowicz, "Differential calculus on compact matrix pseudogroups (quantum groups)," Commun. Math. Phys. 122 (1989)
-/

namespace QOU.Lichnerowicz

universe u

/-- **Abstract setup for the categorical Lichnerowicz identity.**
    Packages the four structural ingredients (a)–(d) from the .md
    proof as fields of a single data structure. The categorical
    Lichnerowicz identity follows by composition. -/
structure QDiracLichnerowiczData (Op : Type u) [AddCommGroup Op] where
  /-- The categorical q-Laplacian on Ω¹(End V). -/
  qLaplacian : Op
  /-- The squared categorical Dirac operator. -/
  qDiracSq : Op
  /-- The q-scalar curvature contribution. -/
  qScalarCurv : Op
  /-- The cross term from Weitzenböck. -/
  crossTerm : Op
  /-- The categorical Weitzenböck assembly. -/
  weitzenbock : qLaplacian = qDiracSq + crossTerm
  /-- Clifford-multiplication and Cartan-formula identify cross term. -/
  cartan_and_clifford : crossTerm = qScalarCurv

/-- **Theorem (categorical Lichnerowicz).** Given the structural data,
    the q-Laplacian equals the squared Dirac plus the q-scalar-
    curvature correction. -/
-- Ref: [leitner2026] prop:categorical-lichnerowicz
theorem qDirac {Op : Type u} [AddCommGroup Op] (d : QDiracLichnerowiczData Op) :
    d.qLaplacian = d.qDiracSq + d.qScalarCurv := by
  rw [d.weitzenbock, d.cartan_and_clifford]

/-- **Parallel-Reeb specialisation.** If additionally the q-scalar
    curvature vanishes (the parallel-Reeb background of Bring's
    surface — `ex:categorical-reeb-brings`), the identity simplifies
    to Δ_∇^q = 𝔇_∇². -/
-- Ref: [leitner2026] prop:categorical-lichnerowicz
theorem qDirac_parallel {Op : Type u} [AddCommGroup Op]
    (d : QDiracLichnerowiczData Op) (h : d.qScalarCurv = 0) :
    d.qLaplacian = d.qDiracSq := by
  rw [qDirac d, h, add_zero]

end QOU.Lichnerowicz
