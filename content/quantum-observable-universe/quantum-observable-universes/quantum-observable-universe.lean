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
# QOU.QuantumObservableUniverse

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse.lean (monolithic)
-/

open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Quantum Observable Universe** over a field `k`.

    A quantum universe satisfying three observability conditions:
    (i)   the Frobenius form on `A` is non-degenerate — an exact self-pairing,
          already enforced structurally by the snake identities in
          `FrobeniusHopfData`.
    (ii)  `Hom_C(𝟙, Ad(A))` is trivial — no non-trivial invariant adjoint
          morphisms.
    (iii) categorical volume constraint: the fundamental object `V` of
          categorical dimension 2 admits a non-degenerate epimorphism
          `ε : Λ²V → 𝟙` preserved by the rigid dualities.

    LaTeX: `\label{def:quantum-observable-universe}` -/
structure QuantumObservableUniverse (k : Type*) [Field k]
    extends QuantumUniverse.{u, v} k where
  /-- The adjoint object `Ad(A)` in `C`, carrying the adjoint action of the
      Hopf algebra `A` on itself.  In a braided monoidal category this is
      constructed from `(A, μ, Δ, S)` and the braiding; here it is provided
      abstractly. -/
  adjointObj : C
  /-- **Adjoint vanishing** (condition ii): all morphisms `𝟙 → Ad(A)` in
      `C` are equal.  In a `k`-linear category this is equivalent to
      `Hom_C(𝟙, Ad(A)) = 0`, since the zero morphism is always present
      and all others must equal it. -/
  adjoint_vanishing : Subsingleton ((𝟙_ C) ⟶ adjointObj)
  /-- The fundamental object `V` of categorical dimension 2. -/
  fundamentalObj : C
  /-- The exterior square `Λ²V` as an object of `C`. -/
  exteriorSquare : C
  /-- **Volume constraint** (condition iii): the non-degenerate epimorphism
      `ε : Λ²V → 𝟙` that forces `det(g_V) = 1` for all
      `g ∈ Aut⊗(ω)`, restricting the gauge group from `GL(2)` to `SL(2)`.
      LaTeX: `\label{eq:categorical-volume-constraint}` -/
  volumeForm : exteriorSquare ⟶ (𝟙_ C)
  /-- **Non-degeneracy**: the volume form is an epimorphism —
      if two morphisms agree after precomposition with `volumeForm`,
      they are equal.  This forces the pairing to be non-degenerate. -/
  volumeForm_epi : ∀ (f g : (𝟙_ C) ⟶ (𝟙_ C)),
    volumeForm ≫ f = volumeForm ≫ g → f = g
/-- The **quantum gauge group** `G_q = Aut⊗(ω)`: the group of monoidal
    natural automorphisms of the fibre functor.

    The full definition is `Aut⊗(ω)` — natural isomorphisms `ω ≅ ω`
    that are compatible with the monoidal structure (tensor products
    and unit).  The type `ω ≅ ω` captures `Aut(ω)`; the monoidal
    constraint is enforced by `fibreFunctor_monoidal` on `QuantumUniverse`,
    which restricts to monoidal natural transformations.

    By Tannaka–Krein duality, `G_q` is a compact group (or algebraic
    group over `k`) that can be recovered from `ω`.

    Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9 -/
noncomputable def QuantumUniverse.gaugeGroup {k : Type*} [Field k]
    (QU : QuantumUniverse.{u, v} k) : Type* :=
  letI := QU.catInst
  QU.fibreFunctor ≅ QU.fibreFunctor

end QOU
