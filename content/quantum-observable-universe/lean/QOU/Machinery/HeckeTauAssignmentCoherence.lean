/-
# Coherent canonicity, first edge — diagram symmetries intertwine the τ-assignments

The canonicity refutation (`tauAssignment_pair_dependent`) shows the
τ-assignment is genuinely pair-dependent, so the right question is
**coherence**: is the family of assignments, indexed by marked pairs, a
functor on a marked-pair groupoid with specified transition maps?

This file proves the first — and structurally cleanest — edge of that
groupoid, in full generality: **any symmetry of the Coxeter matrix
induces a group endomorphism intertwining the assignments of the
corresponding marked pairs.** For a bijection `e : B ≃ B` with
`M (e a) (e b) = M a b`, the simple-selection `k ↦ σ (e k)` is liftable
(the Coxeter relations transport along `e`), giving `diagramHom : W →* W`
with `σ k ↦ σ (e k)`; the six-element cell of `(e i, e j)` is the
`diagramHom`-image of the cell of `(i, j)`, so

    τ-assignment at (e i, e j)  =  τ-assignment at (i, j) ∘ (pullback along diagramHom)

for both the `H^{1,0}` and conjugate `H^{0,1}` legs. The distinctness
hypothesis at the image pair is FREE — it is supplied by the Chebyshev
leg's `simple_ne_full`, the second consumer of that theorem.

At the A₃ rung the diagram flip `0 ↔ 2` instantiates this: the
`(2,1)`-assignment is the pullback of the `(0,1)`-assignment along the
flip automorphism.

Scope (honest): this is ONE edge class of the coherence groupoid.
Still open:

* **pair swap** `(i, j) ↦ (j, i)` — the cell words are not symmetric
  in the pair, and the base-rung `H₃` assignment reads the cell indices
  asymmetrically, so the swap edge needs its own (possibly nontrivial)
  transition map or fails;
* **W-conjugation edges** (conjugating one marked pair to another
  within the group rather than the diagram);
* the **assembled functor** on the full groupoid, which would be the
  affirmative resolution of coherent canonicity.

HONESTY (STRICT): sorry-free, no axioms; `decide` only on finite
`Fin 3` / matrix-entry facts. Nothing here claims full coherent
canonicity — only the diagram-symmetry edge. Nothing wired; `1/(8π)`
stays phase-4.

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Machinery.HeckeTauAssignmentCanonicity

namespace QOU.Machinery.CoxeterParabolic

open CoxeterSystem List CoxeterMatrix Complex
open QOU.Machinery.HeckeGeneral
open scoped Classical

variable {B W : Type*} [Group W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W)

local prefix:100 "πW" => cs.wordProd
local prefix:100 "σW" => cs.simple

/-! ## The induced endomorphism of a matrix symmetry -/

/-- A matrix symmetry makes the shifted simple-selection liftable: the
Coxeter relations transport along `e`. -/
lemma diagramLiftable (e : B ≃ B) (he : ∀ a b, M (e a) (e b) = M a b) :
    M.IsLiftable (fun k => σW (e k)) := by
  intro a b
  have h := cs.simple_mul_simple_pow (e a) (e b)
  rwa [he a b] at h

/-- The group endomorphism `σ k ↦ σ (e k)` induced by a matrix
symmetry. -/
noncomputable def diagramHom (e : B ≃ B)
    (he : ∀ a b, M (e a) (e b) = M a b) : W →* W :=
  cs.lift ⟨fun k => σW (e k), diagramLiftable cs e he⟩

@[simp] lemma diagramHom_simple (e : B ≃ B)
    (he : ∀ a b, M (e a) (e b) = M a b) (k : B) :
    diagramHom cs e he (σW k) = σW (e k) :=
  cs.lift_apply_simple (diagramLiftable cs e he) k

/-- Simple-distinctness transports along any bijection of the index
set — supplied unconditionally by the Chebyshev leg. -/
theorem simple_ne_map (e : B ≃ B) {i j : B} (hne : σW i ≠ σW j) :
    σW (e i) ≠ σW (e j) :=
  simple_ne_full cs fun h => hne (congrArg cs.simple (e.injective h))

/-! ## The cell transports along the symmetry -/

/-- The six-element cell of the image pair is the `diagramHom`-image of
the cell of the source pair. -/
lemma cellElem3_diagramHom (e : B ≃ B)
    (he : ∀ a b, M (e a) (e b) = M a b) (i j : B) (k : Fin 6) :
    cellElem3 cs (e i) (e j) k
      = diagramHom cs e he (cellElem3 cs i j k) := by
  fin_cases k
  · show πW [] = diagramHom cs e he (πW [])
    rw [wordProd_nil, map_one]
  · show πW [e i] = diagramHom cs e he (πW [i])
    rw [wordProd_singleton, wordProd_singleton]
    simp only [diagramHom_simple]
  · show πW [e j] = diagramHom cs e he (πW [j])
    rw [wordProd_singleton, wordProd_singleton]
    simp only [diagramHom_simple]
  · show πW [e j, e i] = diagramHom cs e he (πW [j, i])
    rw [wordProd_ij cs (e j) (e i), wordProd_ij cs j i]
    simp only [map_mul, diagramHom_simple]
  · show πW [e i, e j] = diagramHom cs e he (πW [i, j])
    rw [wordProd_ij cs (e i) (e j), wordProd_ij cs i j]
    simp only [map_mul, diagramHom_simple]
  · show πW [e i, e j, e i] = diagramHom cs e he (πW [i, j, i])
    rw [wordProd_iji cs (e i) (e j), wordProd_iji cs i j]
    simp only [map_mul, diagramHom_simple]

/-! ## The coherence square -/

/-- **Diagram symmetries intertwine the τ-assignments**: the assignment
at the image pair is the pullback of the assignment at the source pair
along the induced endomorphism. The first proved edge of the coherence
groupoid. -/
theorem tauAssignment_diagram_coherent (e : B ≃ B)
    (he : ∀ a b, M (e a) (e b) = M a b) {i j : B}
    (hm : M i j = 3) (hne : σW i ≠ σW j)
    (hm' : M (e i) (e j) = 3) (hne' : σW (e i) ≠ σW (e j))
    (v : W → ℂ) :
    (tauAssignmentAtRank cs (e i) (e j) hm' hne').toFun v
      = (tauAssignmentAtRank cs i j hm hne).toFun
          (v ∘ diagramHom cs e he) := by
  show tauAssignmentH3.toFun (cellRestrict cs (e i) (e j) v)
    = tauAssignmentH3.toFun (cellRestrict cs i j (v ∘ diagramHom cs e he))
  congr 1
  funext k
  show v (cellElem3 cs (e i) (e j) k)
    = v (diagramHom cs e he (cellElem3 cs i j k))
  rw [cellElem3_diagramHom cs e he i j k]

/-- The conjugate `H^{0,1}` partner square. -/
theorem tauAssignment_diagram_coherent_bar (e : B ≃ B)
    (he : ∀ a b, M (e a) (e b) = M a b) {i j : B}
    (hm : M i j = 3) (hne : σW i ≠ σW j)
    (hm' : M (e i) (e j) = 3) (hne' : σW (e i) ≠ σW (e j))
    (w : W → ℂ) :
    (tauAssignmentAtRank cs (e i) (e j) hm' hne').toFunBar w
      = (tauAssignmentAtRank cs i j hm hne).toFunBar
          (w ∘ diagramHom cs e he) := by
  show tauAssignmentH3.toFunBar (cellRestrict cs (e i) (e j) w)
    = tauAssignmentH3.toFunBar (cellRestrict cs i j (w ∘ diagramHom cs e he))
  congr 1
  funext k
  show w (cellElem3 cs (e i) (e j) k)
    = w (diagramHom cs e he (cellElem3 cs i j k))
  rw [cellElem3_diagramHom cs e he i j k]

/-! ## The A₃ diagram flip -/

/-- The A₃ diagram automorphism `0 ↔ 2`. -/
def flipA3 : Fin 3 ≃ Fin 3 where
  toFun := ![2, 1, 0]
  invFun := ![2, 1, 0]
  left_inv := by decide
  right_inv := by decide

/-- The A₃ matrix is flip-symmetric. -/
lemma flipA3_symm : ∀ a b, (Aₙ 3) (flipA3 a) (flipA3 b) = (Aₙ 3) a b := by
  decide

/-- **The flip edge at A₃**: the `(2,1)`-assignment is the pullback of
the `(0,1)`-assignment along the flip automorphism — the two braid
pairs of the A₃ diagram carry coherently-identified assignments, even
though (by `tauAssignment_pair_dependent`) the assignments themselves
are distinct functions. -/
theorem tauAssignment_flip_coherent (v : (Aₙ 3).Group → ℂ) :
    (tauAssignmentAtRank csA3 (flipA3 0) (flipA3 1) (by decide)
        (simple_ne_map csA3 flipA3 simple_ne_A3_01)).toFun v
      = (tauAssignmentAtRank csA3 0 1 (by decide) simple_ne_A3_01).toFun
          (v ∘ diagramHom csA3 flipA3 flipA3_symm) :=
  tauAssignment_diagram_coherent csA3 flipA3 flipA3_symm (by decide)
    simple_ne_A3_01 (by decide)
    (simple_ne_map csA3 flipA3 simple_ne_A3_01) v

end QOU.Machinery.CoxeterParabolic
