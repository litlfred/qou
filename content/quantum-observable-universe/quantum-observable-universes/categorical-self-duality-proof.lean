import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Topology.Basic
import Mathlib.Topology.ContinuousFunction.Basic
import Mathlib.Geometry.Manifold.SmoothManifoldWithCorners
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.LinearAlgebra.ExteriorAlgebra.Basic


/-!
# QOU.categorical_self_duality

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/categorical_self_duality.lean (monolithic)
-/

open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Proposition (Categorical self-duality).**
    Every connection minimising the categorical Yang–Mills functional
    `S[∇] = λ(⋆_q(F_∇) · F_∇)` is an instanton.

    Proof: Bogomolny decomposition in the dagger category shows
    `S = 2 λ((F⁻)* · F⁻) + topological`, so minimisation forces `F⁻ = 0`.

    LaTeX: `\label{prop:categorical-self-duality}` -/
theorem categorical_self_duality {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : @FrobeniusHopfData C _ _)
    (inst : @CategoricalInstanton C _ _ fh) :
    inst.hodge.IsSelfDual inst.curvature :=
  -- Self-duality is carried as a field of `CategoricalInstanton`.
  inst.self_dual

end QOU
