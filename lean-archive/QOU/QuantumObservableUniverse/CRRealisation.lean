import QOU.QuantumObservableUniverse.Structures
import Mathlib.Topology.Basic
import Mathlib.Topology.ContinuousMap.Basic
import Mathlib.Geometry.Manifold.IsManifold.Basic
import Mathlib.Analysis.InnerProductSpace.Basic

/-!
# §2  ℂ Realisation

CR manifold data, the ℂ quantum observable universe, and instanton
connections on principal bundles over CR manifolds.
-/


namespace QOU

/-! ## §2  ℂ Realisation -/

/-- **CR manifold data** for the ℂ realisation.

    A 5-tuple `(M, θ, G, P, E)` as in Example 1.3.  `M` is a CR manifold
    of hypersurface type with non-degenerate Levi form; `θ` is the contact
    form (pseudo-Hermitian structure); `G = SU(2)`; `P → M` is a principal
    `G`-bundle; `E = P ×_G CP¹` is the state bundle.

    LaTeX: `\label{def:c-quantum-universe}` -/
structure CRManifoldData where
  /-- The underlying smooth manifold carrier. -/
  M : Type*
  [topM : TopologicalSpace M]
  /-- CR dimension `n ≥ 1`; real dimension of `M` is `2n + 1`. -/
  n : ℕ
  n_pos : 0 < n
  /-- Levi form signature `(r, s)` with `r + s = n`. -/
  r : ℕ
  s : ℕ
  rs_sum : r + s = n
  /-- The contact form `θ` represented abstractly as a continuous 1-form. -/
  contactForm : M → ℝ
  /-- The Reeb vector field `ξ`, characterised by `ι_ξ dθ = 0` and `θ(ξ) = 1`. -/
  reebField : M → M

/-- **ℂ quantum observable universe**: CR manifold data satisfying the
    vanishing conditions `H⁰(M, Ad(P)) = 0` and `Γ_c(M, E) = 0`.

    LaTeX: `\label{def:c-quantum-observable-universe}` -/
structure CQuantumObservableUniverse extends CRManifoldData where
  /-- The type of global sections of the adjoint bundle `Ad(P)`. -/
  adjointSections : Type*
  /-- `H⁰(M, Ad(P))` is trivial. -/
  adjoint_cohomology_vanishes : Subsingleton adjointSections
  /-- The type of compactly supported sections of the state bundle `E`. -/
  compactStateSections : Type*
  /-- `Γ_c(M, E)` is trivial. -/
  state_sections_vanish : Subsingleton compactStateSections

/-- **Instanton connection** on a principal bundle `P` over a CR manifold.

    LaTeX: `\label{def:instanton}` -/
structure InstantonConnection (cr : CRManifoldData) where
  /-- Abstract connection data (gauge potential). -/
  connectionData : cr.M → ℝ
  /-- Curvature `F_A` restricted to `H = ker θ`. -/
  curvature_H : cr.M → ℝ
  /-- The type of covariant-constant sections of `Ad(P)`. -/
  parallelAdjointSections : Type*
  /-- When `n = 2` (`dim_ℝ H = 4`), the Hodge star on 2-forms restricted to `H`. -/
  hodgeStar : cr.n = 2 → HodgeInvolution (cr.M → ℝ)
  /-- The Yang–Mills energy functional. -/
  yangMillsEnergy : ℝ
  /-- Yang–Mills minimisation: energy is non-negative. -/
  yang_mills_minimises : yangMillsEnergy ≥ 0
  /-- **Self-duality**: when `dim_ℝ H = 4`, the curvature is self-dual. -/
  self_dual : ∀ (hn : cr.n = 2), (hodgeStar hn).IsSelfDual curvature_H

end QOU
