/-
# The assembled functor — τ-assignments as a natural transformation on the marked-pair category

The terminus of the coherence program. The three edge results —
diagram symmetries coherent (`tauAssignment_diagram_coherent`),
W-conjugations coherent (`tauAssignment_conj_coherent`), pair swap
obstructed target-side (`tauAssignment_swap_no_target_transition`) —
are here assembled into a single categorical object:

* **`MarkedPair`** — the category whose objects are marked pairs
  (a generator pair with bond 3 and distinct simples) and whose
  morphisms are group homomorphisms of `W` carrying one marking to the
  other. The single coherence engine is
  **`tauAssignment_hom_coherent`**: EVERY marking-preserving
  homomorphism intertwines the assignments by pullback — this subsumes
  both merged edge theorems, whose homomorphisms embed as
  **`diagramEdge`** and **`conjEdge`**, each proved invertible
  (`IsIso`), so both edge classes live in the core groupoid.
* **`markedStateFunctor`** — the contravariant state functor
  (every pair sees the full state space; morphisms act by pullback);
  **`markedIsotypicFunctor`** — the constant functor at the isotypic
  slot.
* **`tauAssignmentNat` / `tauAssignmentBarNat`** — THE ASSEMBLED
  FUNCTOR PACKAGE: the τ-assignment family is a natural transformation
  from the state functor to the constant isotypic functor, for both the
  `H^{1,0}` and conjugate `H^{0,1}` legs. Naturality at every morphism
  IS the coherence square.
* **`tauAssignmentGroupoidNat`** — the same transformation restricted
  along the core inclusion: a natural transformation on the
  **marked-pair groupoid** (`Core (MarkedPair cs)`), where the proved
  edges live.

Reconciliation with the swap obstruction: a swap `(i,j) ↦ (j,i)` is a
morphism of this category only when some marking-carrying homomorphism
exists — e.g. at rank 2, where exchanging the two generators IS a
matrix symmetry — and then its coherence is *source-side* (pullback on
states), which is exactly what `tauAssignment_hom_coherent` provides.
The merged obstruction excluded *target-side* factorizations
`τ' = T ∘ τ`; the two results are complementary, not in tension.

HONESTY (STRICT): sorry-free, no axioms, no `decide`. The category has
all marking-preserving homomorphisms as morphisms; the groupoid
statement is obtained by restriction to the core, in which the two
proved edge classes are shown to lie. Nothing here manufactures new
assignments — the natural transformation packages the already-proved
squares. Nothing wired; `1/(8π)` stays phase-4.

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import Mathlib.CategoryTheory.Core
import Mathlib.CategoryTheory.Whiskering
import Mathlib.CategoryTheory.Functor.Const
import QOU.Machinery.HeckeTauAssignmentSwapConjugation

namespace QOU.Machinery.CoxeterParabolic

open CoxeterSystem List Complex CategoryTheory
open QOU.Machinery.HeckeGeneral
open scoped Classical

universe uB uW

variable {B : Type uB} {W : Type uW} [Group W] {M : CoxeterMatrix B}
  (cs : CoxeterSystem M W)

local prefix:100 "πW" => cs.wordProd
local prefix:100 "σW" => cs.simple

/-! ## The coherence engine: marking-preserving homomorphisms -/

/-- The cell transports along ANY homomorphism carrying the marking —
the common generalization of the diagram and conjugation transport
lemmas. -/
lemma cellElem3_hom (φ : W →* W) {i j i' j' : B}
    (hi : φ (σW i) = σW i') (hj : φ (σW j) = σW j') (k : Fin 6) :
    cellElem3 cs i' j' k = φ (cellElem3 cs i j k) := by
  fin_cases k
  · show πW [] = φ (πW [])
    rw [wordProd_nil, map_one]
  · show πW [i'] = φ (πW [i])
    rw [wordProd_singleton, wordProd_singleton, hi]
  · show πW [j'] = φ (πW [j])
    rw [wordProd_singleton, wordProd_singleton, hj]
  · show πW [j', i'] = φ (πW [j, i])
    rw [wordProd_ij cs j' i', wordProd_ij cs j i, map_mul, hi, hj]
  · show πW [i', j'] = φ (πW [i, j])
    rw [wordProd_ij cs i' j', wordProd_ij cs i j, map_mul, hi, hj]
  · show πW [i', j', i'] = φ (πW [i, j, i])
    rw [wordProd_iji cs i' j', wordProd_iji cs i j, map_mul, map_mul,
      hi, hj]

/-- **The single coherence theorem**: every marking-preserving
homomorphism intertwines the assignments by pullback. Subsumes the
diagram-symmetry and W-conjugation edge theorems. -/
theorem tauAssignment_hom_coherent (φ : W →* W) {i j i' j' : B}
    (hi : φ (σW i) = σW i') (hj : φ (σW j) = σW j')
    (hm : M i j = 3) (hne : σW i ≠ σW j)
    (hm' : M i' j' = 3) (hne' : σW i' ≠ σW j') (v : W → ℂ) :
    (tauAssignmentAtRank cs i' j' hm' hne').toFun v
      = (tauAssignmentAtRank cs i j hm hne).toFun (fun x => v (φ x)) := by
  show tauAssignmentH3.toFun (cellRestrict cs i' j' v)
    = tauAssignmentH3.toFun (cellRestrict cs i j (fun x => v (φ x)))
  congr 1
  funext k
  show v (cellElem3 cs i' j' k) = v (φ (cellElem3 cs i j k))
  rw [cellElem3_hom cs φ hi hj k]

/-- The conjugate-leg twin. -/
theorem tauAssignment_hom_coherent_bar (φ : W →* W) {i j i' j' : B}
    (hi : φ (σW i) = σW i') (hj : φ (σW j) = σW j')
    (hm : M i j = 3) (hne : σW i ≠ σW j)
    (hm' : M i' j' = 3) (hne' : σW i' ≠ σW j') (w : W → ℂ) :
    (tauAssignmentAtRank cs i' j' hm' hne').toFunBar w
      = (tauAssignmentAtRank cs i j hm hne).toFunBar
          (fun x => w (φ x)) := by
  show tauAssignmentH3.toFunBar (cellRestrict cs i' j' w)
    = tauAssignmentH3.toFunBar (cellRestrict cs i j (fun x => w (φ x)))
  congr 1
  funext k
  show w (cellElem3 cs i' j' k) = w (φ (cellElem3 cs i j k))
  rw [cellElem3_hom cs φ hi hj k]

/-! ## The marked-pair category -/

/-- A marked pair: a generator pair with bond order 3 and distinct
simple reflections. -/
structure MarkedPair where
  i : B
  j : B
  bond : M i j = 3
  ne : cs.simple i ≠ cs.simple j

/-- A morphism of marked pairs: a group homomorphism of `W` carrying
one marking to the other. -/
structure MarkedPairHom (p p' : MarkedPair cs) where
  hom : W →* W
  map_i : hom (cs.simple p.i) = cs.simple p'.i
  map_j : hom (cs.simple p.j) = cs.simple p'.j

lemma MarkedPairHom.ext' {p p' : MarkedPair cs}
    {f g : MarkedPairHom cs p p'} (h : f.hom = g.hom) : f = g := by
  cases f
  cases g
  cases h
  rfl

instance : Category (MarkedPair cs) where
  Hom p p' := MarkedPairHom cs p p'
  id _ := ⟨MonoidHom.id W, rfl, rfl⟩
  comp f g := ⟨g.hom.comp f.hom,
    by rw [MonoidHom.comp_apply, f.map_i, g.map_i],
    by rw [MonoidHom.comp_apply, f.map_j, g.map_j]⟩
  id_comp f := MarkedPairHom.ext' cs (MonoidHom.comp_id f.hom)
  comp_id f := MarkedPairHom.ext' cs (MonoidHom.id_comp f.hom)
  assoc _ _ _ := MarkedPairHom.ext' cs rfl

/-! ## The two proved edge classes live in the category — invertibly -/

/-- The image of a marked pair under a matrix symmetry. -/
def markedMapDiagram (e : B ≃ B) (he : ∀ a b, M (e a) (e b) = M a b)
    (p : MarkedPair cs) : MarkedPair cs :=
  ⟨e p.i, e p.j, by rw [he]; exact p.bond, simple_ne_map cs e p.ne⟩

/-- Diagram symmetries as marked-pair morphisms. -/
noncomputable def diagramEdge (e : B ≃ B) (he : ∀ a b, M (e a) (e b) = M a b)
    (p : MarkedPair cs) : p ⟶ markedMapDiagram cs e he p :=
  ⟨diagramHom cs e he, diagramHom_simple cs e he p.i,
    diagramHom_simple cs e he p.j⟩

/-- A matrix symmetry's inverse is again a matrix symmetry. -/
lemma matrixSymm_symm (e : B ≃ B) (he : ∀ a b, M (e a) (e b) = M a b)
    (a b : B) : M (e.symm a) (e.symm b) = M a b := by
  have h := he (e.symm a) (e.symm b)
  rw [e.apply_symm_apply, e.apply_symm_apply] at h
  exact h.symm

/-- The inverse edge of a diagram symmetry. -/
noncomputable def diagramEdgeInv (e : B ≃ B) (he : ∀ a b, M (e a) (e b) = M a b)
    (p : MarkedPair cs) : markedMapDiagram cs e he p ⟶ p :=
  ⟨diagramHom cs e.symm (matrixSymm_symm e he),
    by show diagramHom cs e.symm _ (σW (e p.i)) = σW p.i
       rw [diagramHom_simple, e.symm_apply_apply],
    by show diagramHom cs e.symm _ (σW (e p.j)) = σW p.j
       rw [diagramHom_simple, e.symm_apply_apply]⟩

/-- Diagram edges are isomorphisms — they lie in the core groupoid. -/
instance (e : B ≃ B) (he : ∀ a b, M (e a) (e b) = M a b)
    (p : MarkedPair cs) : IsIso (diagramEdge cs e he p) :=
  ⟨diagramEdgeInv cs e he p,
    by
      apply MarkedPairHom.ext' cs
      apply cs.ext_simple
      intro k
      show diagramHom cs e.symm (matrixSymm_symm e he) (diagramHom cs e he (σW k)) = σW k
      rw [diagramHom_simple, diagramHom_simple, e.symm_apply_apply],
    by
      apply MarkedPairHom.ext' cs
      apply cs.ext_simple
      intro k
      show diagramHom cs e he (diagramHom cs e.symm (matrixSymm_symm e he) (σW k)) = σW k
      rw [diagramHom_simple, diagramHom_simple, e.apply_symm_apply]⟩

/-- W-conjugations as marked-pair morphisms. -/
def conjEdge (u : W) (p p' : MarkedPair cs)
    (hi : u * σW p.i * u⁻¹ = σW p'.i)
    (hj : u * σW p.j * u⁻¹ = σW p'.j) : p ⟶ p' where
  hom :=
    { toFun := fun x => u * x * u⁻¹
      map_one' := by group
      map_mul' := fun a b => by group }
  map_i := hi
  map_j := hj

/-- Conjugation edges are isomorphisms — they lie in the core
groupoid. -/
instance (u : W) (p p' : MarkedPair cs)
    (hi : u * σW p.i * u⁻¹ = σW p'.i)
    (hj : u * σW p.j * u⁻¹ = σW p'.j) :
    IsIso (conjEdge cs u p p' hi hj) :=
  ⟨conjEdge cs u⁻¹ p' p
      (by rw [← hi]; group) (by rw [← hj]; group),
    by
      apply MarkedPairHom.ext' cs
      apply MonoidHom.ext
      intro x
      show u⁻¹ * (u * x * u⁻¹) * u⁻¹⁻¹ = x
      group,
    by
      apply MarkedPairHom.ext' cs
      apply MonoidHom.ext
      intro x
      show u * (u⁻¹ * x * u⁻¹⁻¹) * u⁻¹ = x
      group⟩

/-! ## The assembled functor package -/

/-- The contravariant state functor: every marked pair sees the full
state space, and marking morphisms act by pullback. -/
def markedStateFunctor : (MarkedPair cs)ᵒᵖ ⥤ Type uW where
  obj _ := W → ℂ
  map f v := fun x => v (f.unop.hom x)

/-- The constant functor at the isotypic slot. -/
def markedIsotypicFunctor : (MarkedPair cs)ᵒᵖ ⥤ Type uW :=
  (Functor.const _).obj (ULift.{uW} (Fin 4 → ℂ))

/-- **THE ASSEMBLED FUNCTOR PACKAGE**: the τ-assignment family is a
natural transformation from the state functor to the constant isotypic
functor on the marked-pair category. Naturality at each morphism is
precisely the coherence square. -/
noncomputable def tauAssignmentNat : markedStateFunctor cs ⟶ markedIsotypicFunctor cs where
  app p v := ULift.up
    ((tauAssignmentAtRank cs p.unop.i p.unop.j p.unop.bond p.unop.ne).toFun v)
  naturality p p' f := by
    funext v
    exact congrArg ULift.up
      ((tauAssignment_hom_coherent cs f.unop.hom f.unop.map_i f.unop.map_j
        p'.unop.bond p'.unop.ne p.unop.bond p.unop.ne v).symm)

/-- The conjugate-leg twin of the assembled package. -/
noncomputable def tauAssignmentBarNat :
    markedStateFunctor cs ⟶ markedIsotypicFunctor cs where
  app p w := ULift.up
    ((tauAssignmentAtRank cs p.unop.i p.unop.j p.unop.bond
      p.unop.ne).toFunBar w)
  naturality p p' f := by
    funext w
    exact congrArg ULift.up
      ((tauAssignment_hom_coherent_bar cs f.unop.hom f.unop.map_i
        f.unop.map_j p'.unop.bond p'.unop.ne p.unop.bond p.unop.ne w).symm)

/-! ## Restriction to the marked-pair groupoid -/

/-- **The τ-assignment as a natural transformation on the marked-pair
GROUPOID**: the assembled package restricted along the core inclusion.
The proved edge classes (diagram symmetries, W-conjugations) are
isomorphisms, hence morphisms of this groupoid. -/
noncomputable def tauAssignmentGroupoidNat :
    (Core.inclusion (MarkedPair cs)).op ⋙ markedStateFunctor cs ⟶
      (Core.inclusion (MarkedPair cs)).op ⋙ markedIsotypicFunctor cs :=
  Functor.whiskerLeft (Core.inclusion (MarkedPair cs)).op (tauAssignmentNat cs)

/-- The conjugate-leg groupoid restriction. -/
noncomputable def tauAssignmentBarGroupoidNat :
    (Core.inclusion (MarkedPair cs)).op ⋙ markedStateFunctor cs ⟶
      (Core.inclusion (MarkedPair cs)).op ⋙ markedIsotypicFunctor cs :=
  Functor.whiskerLeft (Core.inclusion (MarkedPair cs)).op (tauAssignmentBarNat cs)

end QOU.Machinery.CoxeterParabolic
