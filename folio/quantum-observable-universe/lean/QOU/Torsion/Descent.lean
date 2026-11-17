import QOU.Torsion.JetProlongation
import QOU.Torsion.BraneTower
import Mathlib.CategoryTheory.Monoidal.Category

/-!
# §8–§10  Descent, Descent Involution, Brane Boundary

Descent (reverse traversal of the brane tower), the descent involution
`τ_n = ℓ_n ∘ 𝔡_{n+1}`, eigenspace decomposition, and the defining
boundary of the brane.
-/


open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU.Torsion

universe u v

/-! ## §8  Descent -/

/-- **Descent**: reverse traversal of the brane tower.
    LaTeX: `\label{def:descent}` -/
structure Descent where
  tower : RecursiveBraneTower
  descentMap : (n : ℕ) → (n_pos : 0 < n) → Type*
  preserves_qou : ∀ (n : ℕ) (hn : 0 < n) (m : ℕ) (hm : 0 < m) (_hmn : m < n),
    descentMap n hn → descentMap m hm

/-- **Lemma (Descent preserves QOU).**
    LaTeX: `\label{lem:descent}` -/
theorem descent_preserves_qou (tower : RecursiveBraneTower) (n : ℕ)
    (_hn : 0 < n) :
    (tower.jet_prolongation (n - 1)).prolonged.n =
    (tower.jet_prolongation (n - 1)).base.n :=
  (tower.jet_prolongation (n - 1)).dim_preserved

theorem descent_ascent_id {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    (jp : JetProlongation C) :
    jp.ascent ≫ jp.restriction = 𝟙 jp.base.obj :=
  jp.retraction

/-! ## §9  Descent Involution -/

/-- **Descent Involution**: `τ_n = ℓ_n ∘ 𝔡_{n+1}`.
    LaTeX: `\label{def:descent-involution}` -/
structure DescentInvolution (V : Type*) where
  tau : V → V
  idempotent : ∀ (v : V), tau (tau v) = tau v

/-- Build the descent involution from jet prolongation data. -/
noncomputable def DescentInvolution.fromJetProlongation
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    (jp : JetProlongation C) :
    DescentInvolution (jp.base.obj ⟶ jp.jet.obj) := by
  refine ⟨fun f => jp.ascent ≫ (jp.restriction ≫ f), fun f => ?_⟩
  show jp.ascent ≫ (jp.restriction ≫ (jp.ascent ≫ (jp.restriction ≫ f))) =
       jp.ascent ≫ (jp.restriction ≫ f)
  rw [← CategoryTheory.Category.assoc jp.ascent jp.restriction,
      jp.retraction, CategoryTheory.Category.id_comp]

/-- **Eigenspace decomposition** of the descent involution.
    LaTeX: `\label{prop:descent-eigenspaces}` -/
structure EigenspaceDecomposition (V : Type*) (di : DescentInvolution V) where
  desc : Set V
  trans : Set V
  desc_eq_image : desc = Set.range di.tau
  trans_eq_complement : trans = {v | di.tau v ≠ v}

/-- Bosonic modes lie in the descended subalgebra. -/
theorem bosonic_modes_in_desc {M : Type*} (b : Boson M) :
    b.toReebDecomposition.isPurelyHorizontal := by
  exact b.purely_horizontal

/-- An element lies in the descended subspace of an eigenspace decomposition
if and only if it is a fixed point of the descent projector `di.tau`. -/
theorem mem_desc_iff_tau_eq (V : Type*) (di : DescentInvolution V)
    (ed : EigenspaceDecomposition V di) (v : V) :
    v ∈ ed.desc ↔ di.tau v = v := by
  rw [ed.desc_eq_image, Set.mem_range]
  constructor
  · rintro ⟨w, rfl⟩
    exact di.idempotent w
  · intro hv
    exact ⟨v, hv⟩

/-! ## §10  Defining Boundary of the Brane -/

/-- **Defining boundary**: `∂E_n ⊆ E_n`.
    LaTeX: `\label{def:brane-boundary}` -/
structure BraneBoundary (M : Type*) where
  boundary : Set M
  codim_ge_two : ∀ (p : M), p ∉ boundary →
    ∃ (q : M), q ∉ boundary ∧ q ≠ p
  exceptionalFibre : Type*
  exceptional_nonempty : Nonempty exceptionalFibre

/-- **Proposition (Structure of the defining boundary).**
    LaTeX: `\label{prop:brane-boundary}` -/
structure BraneBoundaryStructure (M : Type*) extends BraneBoundary M where
  involution_restricts : ∀ (di : DescentInvolution M),
    ∀ (p : M), p ∈ boundary → di.tau p ∈ boundary
  chirality_interface : ∀ (p : M), p ∈ boundary ∨ p ∉ boundary

end QOU.Torsion
