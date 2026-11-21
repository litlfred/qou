import Mathlib.Data.Set.Basic
import Mathlib.Data.Nat.Basic


/-!
# QOU.PvsNPBoundary.polynomialObservableSubcategory

The **polynomial observable subcategory** R°(L, q) of a Skein
resolution tree: the full sub-poset of nodes whose degree-0 sections
are Markov-trace-computable in at most p(c) Planck steps.  This is the
computational analog of the observable subcategory Bun°(ℙ(V)).

LaTeX label: `def:polynomial-observable-subcategory`

## References
- [leitner2026] §9/p-vs-np-boundary
-/

namespace QOU.PvsNPBoundary

/-- A node of the resolution tree, abstracted as its index. -/
abbrev TreeNode := ℕ

/-- **Polynomial observable subcategory** R°(L, q).

    The set of resolution-tree nodes `x` whose polynomial-time
    degree-0 section space `Γ_poly(x)` is non-trivial — i.e. the
    nodes from which the degree-0 answer is computable in at most
    `polyBound` Planck steps.  Modelled as the subset of nodes for
    which a non-vanishing predicate `gammaPolyNonzero` holds. -/
-- Ref: [leitner2026] §9/p-vs-np-boundary
def polynomialObservableSubcategory
    (gammaPolyNonzero : TreeNode → Prop) : Set TreeNode :=
  {x : TreeNode | gammaPolyNonzero x}

/-- Membership in R° is exactly the non-vanishing of the
    polynomial-time degree-0 section space. -/
-- Ref: [leitner2026] §9/p-vs-np-boundary
theorem mem_polynomialObservableSubcategory
    (gammaPolyNonzero : TreeNode → Prop) (x : TreeNode) :
    x ∈ polynomialObservableSubcategory gammaPolyNonzero ↔
      gammaPolyNonzero x :=
  Iff.rfl

end QOU.PvsNPBoundary
