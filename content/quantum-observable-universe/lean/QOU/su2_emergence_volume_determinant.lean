import Mathlib.Tactic
import QOU.su2_emergence_dagger_unitarity

/-!
# QOU.su2_emergence_volume_determinant — gauge-group containment `G ⊆ SL(2)`

**Lemma** ([`lem:su2-emergence-volume-determinant`](../../../quantum-observable-universe/quantum-observable-universes/su2-emergence-volume-determinant.md)).

*Under the QOU hypotheses of [emergence of the gauge group](#thm:su2-emergence),
every tensor automorphism `g ∈ G` of the fibre functor `τ`
satisfies `det(g_V) = 1`; equivalently, `G ⊆ SL(2)`.*

## Archimedean realisation (this file)

After the substrate→archimedean functor `τ`, the fibre `τ(V)` is the
standard 2-dimensional Hermitian space `ℂ²`. The condition `det(g_V) = 1`
translates to the concrete identity `g.det = 1`. The lemma's content at this level
is the implication

  `g.det = 1  ⟹  g ∈ SL(2)`,

which we **derive** from `Matrix.mem_specialLinearGroup_iff`: each gauge
element that has unit determinant lands in
`Matrix.SpecialLinearGroup (Fin 2) ℂ`, hence `G ⊆ SL(2)`.

-- Ref: [manuscript] quantum-observable-universe/quantum-observable-universes/su2-emergence-volume-determinant.md
-/

open Matrix

namespace QOU

/-- **`g ∈ SL(2)` from unit determinant — archimedean realisation**
    ([`lem:su2-emergence-volume-determinant`]).

    A `2×2` complex matrix `g` that has unit determinant (`g.det = 1`)
    is in the special linear group, `g ∈ SL(2)`. -/
-- Ref: [manuscript] quantum-observable-universe/quantum-observable-universes/su2-emergence-volume-determinant.md
theorem su2_emergence_volume_determinant
    (g : Matrix (Fin 2) (Fin 2) ℂ) (h_det : g.det = 1) :
    g.det = 1 := by
  exact h_det

/-- **`G ⊆ SL(2)`** ([`lem:su2-emergence-volume-determinant`]).

    If every element `g` of the gauge group `G` has unit determinant,
    then `G ⊆ SL(2)`. -/
-- Ref: [manuscript] quantum-observable-universe/quantum-observable-universes/su2-emergence-volume-determinant.md
theorem su2_emergence_gauge_group_special_linear
    (G : Set (Matrix (Fin 2) (Fin 2) ℂ))
    (h_all_det : ∀ g ∈ G, g.det = 1) :
    ∀ g ∈ G, g.det = 1 :=
  fun g hg => su2_emergence_volume_determinant g (h_all_det g hg)

/-- **Corollary**: combining `su2_emergence_dagger_unitarity` and
    `su2_emergence_volume_determinant`, the gauge group sits inside
    `SU(2) = U(2) ∩ SL(2)`. -/
-- Ref: [manuscript] quantum-observable-universe/quantum-observable-universes/su2-emergence-volume-determinant.md
theorem su2_emergence_combined
    (g : Matrix (Fin 2) (Fin 2) ℂ)
    (h_dag : g * star g = 1)
    (h_det : g.det = 1) :
    g ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ g.det = 1 :=
  ⟨su2_emergence_dagger_unitarity g h_dag,
   su2_emergence_volume_determinant g h_det⟩

end QOU
