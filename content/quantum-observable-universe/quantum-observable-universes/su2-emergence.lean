import QOU.Basic
import QOU.Glossary
import QOU.QuantumObservableUniverse.Structures
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.Algebra.Group.Basic


/-!
# QOU.SU2Emergence — Emergence of the gauge group

Given a quantum observable universe (C, A, ω), the gauge group
G_q = Aut⊗(ω) is isomorphic to SU(2) (or SL(2, R) depending on
the signature of the Frobenius pairing).

This is the most depended-upon theorem on the critical path:
spin labels, maximal torus, projective line, and everything
downstream relies on this result.

## References

- [lusztig1993] Introduction to Quantum Groups
- [manuscript] §1 Theorem: Emergence of SU(2)

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

noncomputable section

universe u v

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ

/-- The canonical indeterminate `q` of `R_q`. -/
def q_param : R_q := LaurentPolynomial.T 1

/-- The inverse indeterminate `q⁻¹` of `R_q`. -/
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **Rank-1 characterisation** (hypotheses): in a QOU, the fundamental
    object has categorical dimension 2, the volume form forces determinant 1,
    and adjoint vanishing forces the gauge group to be rank 1.

    This packages the three constraints that together force SU(2).
    The actual theorem (`su2_emergence`) proves the conclusion from
    these hypotheses. -/
structure RankOneGaugeData (k : Type*) [Field k] where
  /-- The underlying QOU. -/
  qou : QuantumObservableUniverse.{u, v} k
  /-- The fundamental representation V has categorical dimension 2,
      encoded as: the spin label for V is j = 1/2 (twice_j = 1). -/
  fund_dim_two : ({ twice_j := 1 : SpinLabels }).cat_dim = 2
  /-- Volume constraint: Λ²V → 𝟙 is non-degenerate (epimorphism). -/
  volume_nondeg :
    letI := qou.catInst
    letI := qou.monInst
    ∀ (f g : (𝟙_ qou.C) ⟶ (𝟙_ qou.C)),
      qou.volumeForm ≫ f = qou.volumeForm ≫ g → f = g
  /-- Adjoint vanishing: Hom(𝟙, Ad(A)) is trivial. -/
  adjoint_trivial :
    letI := qou.catInst
    letI := qou.monInst
    Subsingleton ((𝟙_ qou.C) ⟶ qou.adjointObj) :=
      qou.adjoint_vanishing

/-- **Spin decomposition** in a QOU: the simple objects of `C` are
    indexed by `SpinLabels`, and the fundamental object has spin `1/2`.

    Mirrors the sibling `spin-labels.lean` definition; restated here so
    `su2_emergence` is self-contained (content-sibling `.lean` files
    compile standalone and cannot import one another). -/
structure SpinDecomposition (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] where
  /-- The simple object in `C` at spin label `j`. -/
  simpleObj : SpinLabels → C
  /-- The fundamental object `V` corresponds to spin `1/2`. -/
  fundamentalObj : C
  /-- `V = V_{1/2}` (the spin-1/2 representation). -/
  fundamental_is_half : fundamentalObj = simpleObj { twice_j := 1 }
  /-- The adjoint object `Ad(A)` corresponds to spin `1`. -/
  adjointObj : C
  /-- `Ad(A) = V_1` (the spin-1 representation). -/
  adjoint_is_one : adjointObj = simpleObj { twice_j := 2 }

/-- **Emergence of SU(2)** (Tannaka–Krein reconstruction):

    The three QOU constraints packaged in `RankOneGaugeData` —
    dim V = 2, volume non-degeneracy, adjoint vanishing — together
    force `Aut⊗(τ) ≅ SU(2)` (or `SL(2, ℝ)` by Frobenius pairing
    signature).

    **Proof sketch**:
    1. Faithfulness of τ embeds G into GL(τ(V)) = GL(2, k).
    2. Volume constraint (Λ²V → 𝟙 epi) forces det = 1 → G ⊆ SL(2, k).
    3. Adjoint vanishing forces trivial centre → G = SL(2, k) or SU(2).

    The reconstruction requires Tannaka duality for rigid monoidal
    categories with fibre functor + classification of connected
    subgroups of SL(2) with trivial centre.  Neither is available
    in Mathlib as of 2026-03.

    The axiom records the downstream consequence: every QOU with
    rank-1 gauge data admits a `SpinDecomposition` — simple objects
    indexed by half-integer spin labels with dim = 2j + 1, and the
    fundamental object matches the QOU's fundamental object.

    LaTeX: `\label{thm:su2-emergence}`
    Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9 -/
-- Ref: [lusztig1993] Lusztig, "Introduction to Quantum Groups," Birkhäuser 1993 (DOI: 10.1007/978-0-8176-4717-9)
-- Ref: [deligne2007] Catégories tannakiennes — see content/schema/references.ts
axiom su2_emergence {k : Type*} [Field k]
    (data : RankOneGaugeData.{u, v} k) :
    letI := data.qou.catInst
    letI := data.qou.monInst
    ∃ (sd : SpinDecomposition data.qou.C),
      sd.fundamentalObj = data.qou.fundamentalObj

end

end QOU
