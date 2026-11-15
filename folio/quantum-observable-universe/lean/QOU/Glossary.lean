import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Topology.Basic
import Mathlib.Geometry.Manifold.IsManifold.Basic
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.CategoryTheory.Category.Basic
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.Tactic.Ring

/-!
# QOU.Glossary — Formal Semantic Registry

Central glossary of all mathematical terms used in the QOU manuscript.
Each entry is defined as a `def`, `class`, `structure`, or `constant` with a
docstring containing the original narrative definition for LSP hover-support.

This file is the **Ontologist** output — the single source of truth for
type assignments.  The Formalizer reads this to generate theorem signatures.

Generated scaffold; entries are populated by:
  `python .github/scripts/ontologist.py generate-lean`
-/


open scoped Topology Manifold CategoryTheory

namespace QOU.Glossary

/-! ## Core Algebraic Structures -/

/-- **Frobenius-Hopf Object**: An object `A` in a rigid monoidal category
    equipped with a Hopf algebra structure `(μ, η, Δ, ε, S)` and a
    Frobenius form `λ : A → 𝟙` satisfying non-degeneracy.

    LaTeX: `\label{def:frobenius-hopf}`
    Mathlib: No direct equivalent — builds on `Mathlib.CategoryTheory.Monoidal.Category`
    Universes: objects in `u`, morphisms in `v` -/
-- Ref: [kock2004] Kock, "Frobenius Algebras and 2D Topological Quantum Field Theories," CUP LMS Student Texts 59, 2004
structure FrobeniusHopfObject where
  /-- The carrier type of the underlying object. -/
  carrier : Type*
  /-- Multiplication `μ : A ⊗ A → A`. -/
  mul : carrier → carrier → carrier
  /-- Unit element `η : 𝟙 → A`. -/
  unit : carrier
  /-- Comultiplication `Δ : A → A × A`. -/
  comul : carrier → carrier × carrier
  /-- Counit `ε : A → unit`. -/
  counit : carrier → Unit
  /-- Antipode `S : A → A`. -/
  antipode : carrier → carrier
  /-- Frobenius form `λ : A → ℝ` (non-degenerate). -/
  frobeniusForm : carrier → ℝ

/-- **Quantum Deformation Parameter**: The parameter `q ∈ k×` governing
    the Hopf algebra structure.  At `q = 1` we recover the classical
    cocommutative case.

    LaTeX: `\label{def:quantum-parameter}` -/
-- Ref: [lusztig1993] Lusztig, "Introduction to Quantum Groups," Birkhäuser 1993 (DOI: 10.1007/978-0-8176-4717-9)
noncomputable def quantumParameter : ℝ := 1.1097

/-- **Fibre Functor**: An exact faithful k-linear monoidal functor
    `ω : C → Vect_k` used in Tannaka-Krein reconstruction.

    LaTeX: `\label{def:fibre-functor}`
    Mathlib: `Mathlib.CategoryTheory.Functor.Basic` -/
-- Ref: [baez1995] Baez, "Knots and quantum gravity: progress and prospects," J. Math. Phys. 36 (1995)
structure FibreFunctor where
  /-- Source category (representation category). -/
  source : Type*
  /-- Target category (vector spaces). -/
  target : Type*
  /-- The functor map on objects. -/
  mapObj : source → target

/-- **Quantum Gauge Group**: The quantum group `G_q = Aut⊗(ω)` reconstructed
    via Tannaka-Krein duality from the fibre functor.

    LaTeX: `\label{def:quantum-gauge-group}` -/
-- Ref: [lusztig1993] Lusztig, "Introduction to Quantum Groups," Birkhäuser 1993 (DOI: 10.1007/978-0-8176-4717-9)
structure QuantumGaugeGroup where
  /-- The carrier type of the quantum group. -/
  carrier : Type*
  /-- The deformation parameter q. -/
  q : ℝ
  /-- q is positive. -/
  q_pos : 0 < q

/-! ## Geometric Structures -/

/-- **CR Manifold Structure**: A pseudo-Hermitian structure with Levi
    distribution, Reeb vector field, and Webster metric.

    LaTeX: `\label{def:cr-manifold}`
    Mathlib: `Mathlib.Geometry.Manifold.IsManifold.Basic` -/
-- Ref: [witten1988] Witten, "Topological quantum field theory," Comm. Math. Phys. 117 (1988)
structure CRManifold where
  /-- The underlying topological space. -/
  carrier : Type*
  [toTopSpace : TopologicalSpace carrier]
  /-- CR dimension `n ≥ 1` (real dimension is `2n + 1`). -/
  n : ℕ
  /-- Non-degeneracy: `n ≥ 1`. -/
  n_pos : 0 < n

/-- **Bring's Surface**: The maximally symmetric CR manifold of genus 4,
    with Euler characteristic χ = −6, defined by Σ x_j^k = 0 for k = 1,2,3
    in CP⁴.

    LaTeX: `\label{def:brings-surface}` -/
-- Ref: [atiyah1988] Atiyah, "Topological quantum field theories," Publ. IHES 68 (1988)
structure BringsSurface where
  /-- The carrier type. -/
  carrier : Type*
  /-- Genus of Bring's surface is 4. -/
  genus : ℕ := 4
  /-- Euler characteristic is −6. -/
  eulerChar : ℤ := -6

/-- **Substrate Parameter**: `q(p) = 1 + |⟨L_θ, F_A⁺⟩|(p)` — couples
    chiral curvature to contact geometry on Bring's surface.

    LaTeX: `\label{def:substrate-parameter}` -/
-- Ref: [witten1988] Witten, "Topological quantum field theory," Comm. Math. Phys. 117 (1988)
noncomputable def substrateParameter (p : ℝ) : ℝ := 1 + |p|

/-! ## Jet Prolongation -/

/-- **Jet Prolongation**: The first jet bundle `J¹E` represented
    categorically by `A ⊗ Ω¹(A)` where `Ω¹(A) = ker(m : A ⊗ A → A)`.

    LaTeX: `\label{def:jet-prolongation}` -/
-- Ref: [lurie2009] Lurie, "On the Classification of Topological Field Theories," arXiv:0905.0465
structure JetProlongation where
  /-- The base type (algebra `A`). -/
  base : Type*
  /-- The fibre type (first-order differentials). -/
  fibre : Type*
  /-- Jet projection to the base. -/
  proj : fibre → base

/- **Kähler Differentials** — moved (2026-11-15).  `Ω¹(A) = ker(m : A ⊗ A → A)`, the
    universal first-order differential calculus (`\label{def:kahler-differentials}`), is now
    a real construction in `QOU.MathlibExt.UniversalDifferentials` (file
    `QOU/MathlibExt/UniversalDifferentials.lean`): the bimodule `Ω1 R A`, the derivation `d`,
    the Leibniz rule, the universal property, and the identification with Mathlib's
    `KaehlerDifferential` when `A` is commutative.  The three-field stub that stood here
    carried no axioms and had no consumers, so it was removed rather than aliased. -/

/-! ## Braid and Knot Theory -/

/-- **Braid Group B₃**: The braid group on 3 strands, presented as
    `⟨σ₁, σ₂ | σ₁σ₂σ₁ = σ₂σ₁σ₂⟩`.

    LaTeX: `\label{def:braid-group}` -/
-- Ref: [turaev2010] Turaev, "Quantum Invariants of Knots and 3-Manifolds," de Gruyter 2010
structure BraidGroup (n : ℕ) where
  /-- Carrier type for braid group elements. -/
  carrier : Type*
  /-- The identity braid. -/
  one : carrier
  /-- Composition of braids. -/
  mul : carrier → carrier → carrier

/-- **Binary Dihedral Group**: `Dic₃ ⊂ SU(2)` of order 12, lifting S₃
    via the double cover `SU(2) → SO(3)`.

    LaTeX: `\label{def:binary-dihedral}` -/
-- Ref: [turaev2010] Turaev, "Quantum Invariants of Knots and 3-Manifolds," de Gruyter 2010
structure BinaryDihedralGroup where
  /-- Carrier type for group elements. -/
  carrier : Type*
  /-- The group order is 12. -/
  order : ℕ := 12

/-! ## Chapter 1 — Geometric and Analytic Terms -/

/-- **Levi Form**: The Hermitian form `L_θ : H × H → ℂ` on the horizontal
    distribution `H = ker θ`, defined by `L_θ(V, W) = −i dθ(V, W̄)`.
    Non-degeneracy of the Levi form is the defining property of a CR manifold
    of hypersurface type.

    LaTeX: used in `\label{def:c-quantum-universe}`, item (i).
    Mathlib: `Mathlib.Analysis.InnerProductSpace.Basic` (sesquilinear forms) -/
structure LeviForm where
  /-- The horizontal distribution `H` as a type. -/
  horizontal : Type*
  /-- The Hermitian pairing `L_θ : H × H → ℝ` (real part). -/
  pairing : horizontal → horizontal → ℝ

/-- **Webster Metric**: The pseudo-Riemannian metric `g_θ` of signature
    `(2r, 2s)` on the horizontal distribution `H`, induced by the contact
    form `θ` and the Levi form `L_θ`.

    LaTeX: used in `\label{def:c-quantum-universe}`, item (ii).
    Mathlib: `Mathlib.Geometry.Manifold.IsManifold.Basic` -/
structure WebsterMetric where
  /-- The horizontal distribution `H` as a type. -/
  horizontal : Type*
  /-- The metric tensor `g_θ : H × H → ℝ`. -/
  metric : horizontal → horizontal → ℝ
  /-- Signature parameter `r`. -/
  r : ℕ
  /-- Signature parameter `s`. -/
  s : ℕ

/-- **Reeb Vector Field**: The unique vector field `ξ` on a contact manifold
    `(M, θ)` characterised by `ι_ξ dθ = 0` and `θ(ξ) = 1`.

    LaTeX: `\label{def:reeb-decomposition}` (defined within)
    Mathlib: No direct equivalent; builds on vector field infrastructure. -/
structure ReebVectorField where
  /-- The manifold carrier. -/
  manifold : Type*
  /-- The Reeb field as a map `M → TM` (simplified to `M → M`). -/
  field : manifold → manifold

/-- **Lusztig Integral Form**: The `ℤ[q, q⁻¹]`-subalgebra
    `U^ℤ_q(𝔰𝔲(2))` of `U_q(𝔰𝔲(2))` generated by `K^{±1}` and the
    divided powers `E^{(n)} = Eⁿ/[n]_q!`, `F^{(n)} = Fⁿ/[n]_q!`.

    LaTeX: `\label{def:substrate-parameter}` (referenced within).
    Ref: [lusztig1993] -/
-- Ref: [lusztig1993] Lusztig, "Introduction to Quantum Groups," Birkhäuser 1993 (DOI: 10.1007/978-0-8176-4717-9)
structure LusztigIntegralForm where
  /-- Carrier type of the integral form. -/
  carrier : Type*
  /-- The deformation parameter `q`. -/
  q : ℝ
  /-- Generator `E`. -/
  genE : carrier
  /-- Generator `F`. -/
  genF : carrier
  /-- Generator `K`. -/
  genK : carrier

/-- **Yang–Mills Functional**: The gauge-theoretic energy functional
    `∫_M ‖F_A|_H‖² θ ∧ (dθ)ⁿ` whose critical points are Yang–Mills
    connections.  Instantons are absolute minimisers.

    LaTeX: `\label{def:instanton}` (referenced within). -/
structure YangMillsFunctional where
  /-- The manifold carrier. -/
  manifold : Type*
  /-- The functional evaluated on a connection (abstract). -/
  energy : (manifold → ℝ) → ℝ
  /-- The energy is non-negative. -/
  energy_nonneg : ∀ conn, 0 ≤ energy conn

/-- **q-Laplacian**: The operator `Δ_q = d_q δ_q + δ_q d_q` whose kernel
    defines q-harmonic forms (particles).

    LaTeX: `\label{def:q-harmonic-form}` (referenced within). -/
structure QLaplacian where
  /-- The type of forms on which the Laplacian acts. -/
  forms : Type*
  /-- The Laplacian operator `Δ_q : forms → forms`. -/
  op : forms → forms

/-- **Hodge Star** on the horizontal distribution `H`: the operator
    `*_H : Λ² H* → Λ² H*` determined by the Webster metric, satisfying
    `*_H² = id` when `dim_ℝ H = 4`.

    LaTeX: `\label{def:instanton}` (referenced within).
    Mathlib: `Mathlib.LinearAlgebra.ExteriorAlgebra.Basic` -/
structure HodgeStarH where
  /-- The type of 2-forms on `H`. -/
  forms : Type*
  /-- The Hodge star operator `*_H`. -/
  star : forms → forms
  /-- Involutivity: `*_H² = id` (when `dim_ℝ H = 4`). -/
  star_sq : ∀ f, star (star f) = f

/-- **State Bundle**: The associated bundle `E = P ×_G ℂP¹ → M` where
    `SU(2)` acts on `ℂP¹` by Möbius transformations.

    LaTeX: `\label{def:c-quantum-universe}`, item (v). -/
structure StateBundle where
  /-- The base manifold. -/
  base : Type*
  /-- The total space. -/
  total : Type*
  /-- Bundle projection `π : E → M`. -/
  proj : total → base

/-- **Principal Bundle**: A principal `G`-bundle `P → M` whose holonomy
    reduces to `SO(3) ⊂ SU(2)/{±I}`.

    LaTeX: `\label{def:c-quantum-universe}`, item (iv).
    Mathlib: `Mathlib.Topology.FiberBundle.Basic` -/
structure PrincipalBundle where
  /-- The base manifold. -/
  base : Type*
  /-- The structure group carrier. -/
  group : Type*
  /-- The total space. -/
  total : Type*
  /-- Bundle projection `π : P → M`. -/
  proj : total → base

/-- **Adjoint Object** `Ad(A)`: the object `A` with the conjugation coaction
    `a ↦ Σ a₍₁₎ b S(a₍₂₎)`.  In the ℂ realisation this is the adjoint
    bundle `Ad(P)`.

    LaTeX: `\label{def:quantum-observable-universe}`, item (ii). -/
structure AdjointObject where
  /-- The carrier type. -/
  carrier : Type*
  /-- The adjoint action map. -/
  adjointAction : carrier → carrier → carrier

/-- **Self-Dual Curvature**: The projection `F_A⁺ ∈ Γ(Λ⁺ H* ⊗ Ad(P))`
    of the curvature onto the self-dual subbundle of `Λ² H*`.

    LaTeX: `\label{prop:self-dual-curvature}` (defined within). -/
structure SelfDualCurvature where
  /-- The manifold carrier. -/
  manifold : Type*
  /-- The self-dual curvature as a section `M → ℝ` (simplified). -/
  section_ : manifold → ℝ

/-! ## p-Adic Structures -/

/-- **F-Isocrystal**: A module over the Dieudonné ring
    `ℚ_p⟨F, V⟩ / (FV − p)`, where the Frobenius endomorphism plays the
    role of Levi-form contraction.

    LaTeX: `\label{def:f-isocrystal}` -/
-- Ref: [freed2010] § Topological quantum field theories from compact Lie groups
structure FIsocrystal where
  /-- The carrier module. -/
  carrier : Type*
  /-- Frobenius endomorphism `F`. -/
  frobenius : carrier → carrier
  /-- Verschiebung endomorphism `V`. -/
  verschiebung : carrier → carrier

end QOU.Glossary
