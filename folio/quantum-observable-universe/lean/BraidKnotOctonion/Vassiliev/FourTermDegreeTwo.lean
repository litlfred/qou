/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under CC BY 4.0 as described in the repository LICENSE.
-/
import BraidKnotOctonion.Vassiliev.WeightSystem

/-!
# Degree-2 check of the four-term relation: the crossed diagram survives

Bean `qou-bgq9`.  `FourTermEncodingCollapse.lean` shows that the former 4T encoding made every
weight system of positive degree zero.  This file checks the replacement (Bar-Natan's 4T, in
`FourTermRelation.lean`) in the first degree where 4T has content.

On four marked points there are three chord diagrams: `(0 1)(2 3)` and `(0 3)(1 2)`, which
carry an isolated chord, and the crossed diagram `(0 2)(1 3)`.  The known answer is
`𝒜₂ ≅ R`, spanned by the crossed diagram.  Proved here:

* `crossedEval_fourTerm` — evaluation at the crossed diagram kills every 4T relator of degree 2.
  This is a finite check over the three diagrams, four chord endpoints and four rotations.
* `crossedEval_oneTerm` — it kills every 1T relator (the crossed diagram has no isolated chord).
* `relationsSubmodule_two_ne_top` — so over any non-trivial commutative ring the degree-2
  relations are a proper submodule, and `exists_weightSystem_two_ne_zero` gives a non-zero
  weight system.  Under the former encoding both statements were false whenever `2` is a unit.

No measured values.
-/

namespace QOU.KnotTheory.Vassiliev

open scoped Classical
open Equiv

/-- The crossed degree-2 pairing `(0 2)(1 3)`. -/
def crossedPairing : Perm (Fin (2 * 2)) := swap 0 2 * swap 1 3

/-- The crossed degree-2 chord diagram. -/
def crossed : ChordDiagram 2 where
  pairing := crossedPairing
  involutive := by intro x; fin_cases x <;> decide
  fixedPointFree := by intro x; fin_cases x <;> decide

/-- The three fixed-point-free involutions of `Fin 4`. -/
theorem pairing_two_cases (σ : Perm (Fin (2 * 2))) (hi : Function.Involutive σ)
    (hf : ∀ i, σ i ≠ i) :
    σ = swap 0 1 * swap 2 3 ∨ σ = swap 0 3 * swap 1 2 ∨ σ = crossedPairing := by
  have key : ∀ f : Fin 4 → Fin 4, (∀ i, f (f i) = i) → (∀ i, f i ≠ i) →
      f = ⇑((swap (0 : Fin 4) 1 * swap (2 : Fin 4) 3 : Perm (Fin 4))) ∨
        f = ⇑((swap (0 : Fin 4) 3 * swap (1 : Fin 4) 2 : Perm (Fin 4))) ∨
        f = ⇑((swap (0 : Fin 4) 2 * swap (1 : Fin 4) 3 : Perm (Fin 4))) := by
    decide +kernel
  rcases key σ hi hf with h | h | h
  · exact Or.inl (Equiv.ext (congrFun h))
  · exact Or.inr (Or.inl (Equiv.ext (congrFun h)))
  · exact Or.inr (Or.inr (Equiv.ext (congrFun h)))

variable (R : Type*) [CommRing R]

/-- Evaluation at the crossed diagram. -/
noncomputable def crossedEval : CDModule R 2 →ₗ[R] R := Finsupp.lapply crossed

theorem crossedEval_of (D : ChordDiagram 2) :
    crossedEval R (CDModule.of D) = if D.pairing = crossedPairing then 1 else 0 := by
  unfold crossedEval CDModule.of
  rw [Finsupp.lapply_apply, Finsupp.single_apply]
  congr 1
  apply propext
  constructor
  · rintro rfl; rfl
  · intro h; exact ChordDiagram.ext h

/-- The integer count behind a 4T relator, as a function of the pairing alone. -/
def crossedCount (σ : Perm (Fin (2 * 2))) (p m : Fin (2 * 2)) : ℤ :=
  let ind : ℕ → ℤ := fun k =>
    if (finRotate (2 * 2) ^ (m : ℕ) * gapPerm (2 * 2) k) * σ *
        (finRotate (2 * 2) ^ (m : ℕ) * gapPerm (2 * 2) k)⁻¹ = crossedPairing then 1 else 0
  ind (p.val + 1) - ind p.val + ind ((σ p).val + 1) - ind (σ p).val

/-- The finite check: every admissible 4T count vanishes on the three degree-2 pairings. -/
theorem crossedCount_eq_zero :
    ∀ σ ∈ [swap (0 : Fin 4) 1 * swap 2 3, swap (0 : Fin 4) 3 * swap 1 2, crossedPairing],
      ∀ p m : Fin 4, p.val + 1 < 4 → (σ p).val + 1 < 4 → crossedCount σ p m = 0 := by
  decide +kernel

theorem crossedEval_fourTerm (D : ChordDiagram 2) (p m : Fin (2 * 2))
    (h : FourTermAdmissible D p) : crossedEval R (fourTermRelator R D p m) = 0 := by
  have hc : crossedCount D.pairing p m = 0 := by
    rcases pairing_two_cases D.pairing D.involutive D.fixedPointFree with hσ | hσ | hσ <;>
      exact crossedCount_eq_zero _ (by rw [hσ]; simp) p m h.1 h.2
  unfold fourTermRelator
  simp only [map_add, map_sub, crossedEval_of, ChordDiagram.conj_pairing]
  have := congrArg (fun z : ℤ => (z : R)) hc
  simp only [crossedCount, Int.cast_sub, Int.cast_add, Int.cast_ite, Int.cast_one,
    Int.cast_zero] at this
  exact this

theorem crossed_not_hasAdjacentChord : ¬ HasAdjacentChord crossed := by
  unfold HasAdjacentChord
  decide

theorem crossedEval_oneTerm (D : ChordDiagram 2) (h : HasAdjacentChord D) :
    crossedEval R (CDModule.of D) = 0 := by
  rw [crossedEval_of, if_neg]
  intro hp
  have : D = crossed := ChordDiagram.ext hp
  exact crossed_not_hasAdjacentChord (this ▸ h)

/-- Every degree-2 relation is killed by evaluation at the crossed diagram. -/
theorem relations_le_ker_crossedEval :
    relationsSubmodule R (n := 2) ≤ LinearMap.ker (crossedEval R) := by
  apply sup_le
  · rw [oneTermSubmodule, Submodule.span_le]
    rintro _ ⟨D, h, rfl⟩
    exact crossedEval_oneTerm R D h
  · rw [fourTermSubmodule, Submodule.span_le]
    rintro _ ⟨D, p, m, h, rfl⟩
    exact crossedEval_fourTerm R D p m h

/-- **The degree-2 relations are a proper submodule** over any non-trivial commutative ring. -/
theorem relationsSubmodule_two_ne_top [Nontrivial R] :
    relationsSubmodule R (n := 2) ≠ ⊤ := by
  intro htop
  have hmem : CDModule.of crossed ∈ relationsSubmodule R (n := 2) := by rw [htop]; trivial
  have h0 := relations_le_ker_crossedEval R hmem
  rw [LinearMap.mem_ker, crossedEval_of, if_pos (show crossed.pairing = crossedPairing from rfl)] at h0
  exact one_ne_zero h0

/-- **A non-zero weight system of degree 2.** -/
theorem exists_weightSystem_two_ne_zero [Nontrivial R] : ∃ w : WeightSystem R 2, w ≠ 0 := by
  refine ⟨(relationsSubmodule R).liftQ (crossedEval R) (relations_le_ker_crossedEval R), ?_⟩
  intro hw
  have h := LinearMap.congr_fun hw (AReduced.mk crossed)
  unfold AReduced.mk AReduced.proj at h
  rw [Submodule.mkQ_apply, Submodule.liftQ_apply, crossedEval_of,
    if_pos (show crossed.pairing = crossedPairing from rfl), LinearMap.zero_apply] at h
  exact one_ne_zero h

end QOU.KnotTheory.Vassiliev
