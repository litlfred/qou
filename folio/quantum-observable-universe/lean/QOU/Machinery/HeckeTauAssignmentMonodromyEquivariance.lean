/-
# Monodromy equivariance along diagram edges — the length-preservation chip

The orbit-invariants file left one honest boundary: coherence was
proved for functionals factoring through the cell restriction, while
the ambient `q = i` monodromy operator `monodromyN (descentRight cs l)`
acts through the LENGTH RULE on the full group, and marking morphisms
need not preserve length. This file chips that boundary in half:

* **`diagramHom_length`** — diagram symmetries preserve Coxeter length
  (map a reduced word, bound both directions through the inverse
  symmetry). This is the structural reason the diagram half of the
  groupoid is compatible with everything built from the length rule.
* **`monodromyN_diagram_equivariant`** — the `q = i` Jordan nilpotent
  at the image generator pulls back along a diagram symmetry to the
  nilpotent at the source generator. So on the diagram half of the
  marked-pair groupoid, the ENTIRE monodromy-weight-filtration
  apparatus — not merely the cell-factoring functionals — transports.

Honest remainder: conjugation edges. Inner automorphisms do not
preserve length in general, so the same argument does not run; whether
some corrected form of monodromy equivariance holds along conjugation
edges is OPEN — stated here, not settled. (For the τ-assignment laws
themselves this does not matter: they factor through the cell, and
their coherence along ALL edges is already proved.)

HONESTY (STRICT): sorry-free, no axioms, no `decide`; general-rank.
Nothing wired; `1/(8π)` stays phase-4.

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Machinery.HeckeTauAssignmentOrbitInvariants

namespace QOU.Machinery.CoxeterParabolic

open CoxeterSystem List Complex
open QOU.Machinery.HeckeGeneral
open scoped Classical

variable {B W : Type*} [Group W] {M : CoxeterMatrix B}
  (cs : CoxeterSystem M W)

local prefix:100 "πW" => cs.wordProd
local prefix:100 "σW" => cs.simple

/-- A diagram symmetry maps word products to word products of the
mapped word. -/
lemma diagramHom_wordProd (e : B ≃ B)
    (he : ∀ a b, M (e a) (e b) = M a b) (ω : List B) :
    diagramHom cs e he (πW ω) = πW (ω.map e) := by
  induction ω with
  | nil => rw [wordProd_nil, map_one, List.map_nil, wordProd_nil]
  | cons a l ih =>
      rw [wordProd_cons, map_mul, diagramHom_simple, ih, List.map_cons,
        wordProd_cons]

/-- The inverse symmetry undoes `diagramHom`, pointwise. -/
lemma diagramHom_symm_apply (e : B ≃ B)
    (he : ∀ a b, M (e a) (e b) = M a b) (w : W) :
    diagramHom cs e.symm (matrixSymm_symm e he)
      (diagramHom cs e he w) = w := by
  have hcomp : (diagramHom cs e.symm (matrixSymm_symm e he)).comp
      (diagramHom cs e he) = MonoidHom.id W := by
    apply cs.ext_simple
    intro k
    show diagramHom cs e.symm (matrixSymm_symm e he)
      (diagramHom cs e he (σW k)) = σW k
    rw [diagramHom_simple, diagramHom_simple, e.symm_apply_apply]
  exact DFunLike.congr_fun hcomp w

/-- **Diagram symmetries preserve Coxeter length.** One direction maps
a reduced word; the other applies the inverse symmetry. -/
theorem diagramHom_length (e : B ≃ B)
    (he : ∀ a b, M (e a) (e b) = M a b) (w : W) :
    cs.length (diagramHom cs e he w) = cs.length w := by
  have hle : ∀ (e' : B ≃ B) (he' : ∀ a b, M (e' a) (e' b) = M a b)
      (x : W), cs.length (diagramHom cs e' he' x) ≤ cs.length x := by
    intro e' he' x
    rcases cs.exists_reduced_word x with ⟨ω, hlen, rfl⟩
    rw [diagramHom_wordProd cs e' he' ω]
    calc cs.length (πW (ω.map e')) ≤ (ω.map e').length :=
          cs.length_wordProd_le _
      _ = ω.length := by rw [List.length_map]
      _ = cs.length (πW ω) := hlen
  refine le_antisymm (hle e he w) ?_
  have h2 := hle e.symm (matrixSymm_symm e he) (diagramHom cs e he w)
  rwa [diagramHom_symm_apply cs e he w] at h2

/-- **Monodromy is diagram-equivariant**: the `q = i` Jordan nilpotent
at the image generator pulls back along a diagram symmetry to the
nilpotent at the source generator. Conjugation edges are NOT covered —
inner automorphisms need not preserve length; that case is open. -/
theorem monodromyN_diagram_equivariant (e : B ≃ B)
    (he : ∀ a b, M (e a) (e b) = M a b) (l : B) (v : W → ℂ) (u : W) :
    monodromyN (descentRight cs (e l)) v (diagramHom cs e he u)
      = monodromyN (descentRight cs l)
          (fun x => v (diagramHom cs e he x)) u := by
  unfold monodromyN mulStep descentRight
  simp only [Pi.sub_apply, Pi.smul_apply, smul_eq_mul]
  have ht : diagramHom cs e he u * σW (e l)
      = diagramHom cs e he (u * σW l) := by
    rw [map_mul, diagramHom_simple]
  simp only [ht, diagramHom_length cs e he]

end QOU.Machinery.CoxeterParabolic
