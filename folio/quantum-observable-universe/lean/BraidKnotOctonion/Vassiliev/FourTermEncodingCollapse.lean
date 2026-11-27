/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under CC BY 4.0 as described in the repository LICENSE.
-/
import BraidKnotOctonion.Vassiliev.WeightSystem
import Mathlib.GroupTheory.Perm.Fin
import Mathlib.Logic.Equiv.Fin.Rotate

/-!
# The current 4T encoding collapses the reduced chord-diagram space

Bean `qou-bgq9` (4T relations and the braid-to-chord-diagram jet), sub-item "link the
infinitesimal pure-braid relation to `FourTermRelation`".

`FourTermRelation.lean` encodes the four-term relation as the commutator-shaped relator

`fourTermRelator D i j = ⟨D⟩ − ⟨D·sᵢ⟩ − ⟨D·sⱼ⟩ + ⟨D·sᵢsⱼ⟩`

for **every** pair of cyclically adjacent transpositions `sᵢ, sⱼ` of the `2n` marked points,
with no condition tying `i, j` to the chords of `D`.  Its docstring already flags that the
faithfulness of this encoding to Bar-Natan's 4T relation is unchecked.  This file checks it,
and the answer is negative:

* `two_smul_slide_mem` — the relator with `i = j` is `2(⟨D⟩ − ⟨D·sᵢ⟩)`, because `sᵢ² = 1`.
* `slide_mem` — so when `2` is a unit in `R`, every single endpoint slide is a relation.
* `closure_adjTransp` — the cyclic adjacent transpositions generate `Perm (Fin N)` as a monoid.
* `conj_sub_mem` — hence `⟨D·g⟩ − ⟨D⟩` is a relation for **every** relabelling `g`.
* `relationsSubmodule_eq_top` — for `n ≥ 1` every diagram is relabelling-equivalent to one with
  an isolated chord, which 1T kills, so `1T ⊔ 4T` is the whole module.
* `weightSystem_eq_zero` — consequently every weight system of degree `n ≥ 1` is zero, over any
  commutative ring in which `2` is a unit (for example `ℚ`, `ℝ`, `ℂ`).

So the encoded `𝒜_n` is `0` for `n ≥ 1` whenever `2` is invertible.  The true `𝒜_n` is not:
`𝒜₂` over `ℚ` is one-dimensional, spanned by the crossed two-chord diagram (Chmutov–Duzhin–
Mostovoy, Table 4.1), and the `𝔰𝔩₂` weight system is non-zero on it.  The structural results of
`WeightSystem.lean` are proved for an arbitrary relations submodule and stay true; it is the
specific `fourTermSubmodule` that has to be replaced by Bar-Natan's relation, in which the two
slid endpoints are the ends of chords of `D` meeting a fixed third chord.

No measured values; this is combinatorics of fixed-point-free involutions.
-/

namespace QOU.KnotTheory.Vassiliev

open Equiv

variable (R : Type*) [CommRing R] {n : ℕ}

/-- The cyclic adjacent transposition is an involution. -/
theorem adjTransp_mul_self (i : Fin (2 * n)) : adjTransp i * adjTransp i = 1 := by
  unfold adjTransp
  exact swap_mul_self _ _

/-- The 4T relator with equal indices is twice a single endpoint slide. -/
theorem two_smul_slide_mem (D : ChordDiagram n) (i : Fin (2 * n)) :
    (2 : R) • (CDModule.of D - CDModule.of (D.conj (adjTransp i))) ∈ fourTermSubmodule R := by
  have h : fourTermRelator R D i i =
      (2 : R) • (CDModule.of D - CDModule.of (D.conj (adjTransp i))) := by
    unfold fourTermRelator
    rw [adjTransp_mul_self, ChordDiagram.conj_one, two_smul]
    abel
  rw [← h]
  exact Submodule.subset_span ⟨D, i, i, rfl⟩

/-- When `2` is a unit, every single endpoint slide is a 4T relation. -/
theorem slide_mem (h2 : IsUnit (2 : R)) (D : ChordDiagram n) (i : Fin (2 * n)) :
    CDModule.of (D.conj (adjTransp i)) - CDModule.of D ∈ fourTermSubmodule R := by
  obtain ⟨u, hu⟩ := h2
  have hmem := (fourTermSubmodule R).smul_mem (↑u⁻¹ : R) (two_smul_slide_mem R D i)
  rw [smul_smul, ← hu, Units.inv_mul, one_smul] at hmem
  have := (fourTermSubmodule R).neg_mem hmem
  rwa [neg_sub] at this

/-- The cyclic adjacent transpositions `(i, i+1 mod N)` generate `Perm (Fin N)` as a monoid. -/
theorem closure_adjTransp (N : ℕ) :
    Submonoid.closure (Set.range fun i : Fin N => swap i (finRotate N i)) = ⊤ := by
  cases N with
  | zero =>
    apply Subsingleton.elim
  | succ m =>
    rw [eq_top_iff, ← Equiv.Perm.mclosure_swap_castSucc_succ m, Submonoid.closure_le]
    rintro _ ⟨j, rfl⟩
    apply Submonoid.subset_closure
    refine ⟨j.castSucc, ?_⟩
    simp only [finRotate_succ_apply, Fin.coeSucc_eq_succ]

/-- When `2` is a unit, `⟨D·g⟩ − ⟨D⟩` is a 4T relation for every relabelling `g`. -/
theorem conj_sub_mem (h2 : IsUnit (2 : R)) (g : Perm (Fin (2 * n))) (D : ChordDiagram n) :
    CDModule.of (D.conj g) - CDModule.of D ∈ fourTermSubmodule R := by
  let S : Submonoid (Perm (Fin (2 * n))) :=
    { carrier := {g | ∀ D : ChordDiagram n,
        CDModule.of (D.conj g) - CDModule.of D ∈ fourTermSubmodule R}
      one_mem' := by
        intro D
        simp only [ChordDiagram.conj_one, sub_self]
        exact (fourTermSubmodule R).zero_mem
      mul_mem' := by
        intro h g hh hg D
        rw [ChordDiagram.conj_mul]
        have := (fourTermSubmodule R).add_mem (hh (D.conj g)) (hg D)
        rwa [sub_add_sub_cancel] at this }
  have hle : Submonoid.closure (Set.range fun i : Fin (2 * n) => swap i (finRotate (2 * n) i))
      ≤ S := by
    rw [Submonoid.closure_le]
    rintro _ ⟨i, rfl⟩
    exact fun D => slide_mem R h2 D i
  have hg : g ∈ S := hle (by rw [closure_adjTransp]; trivial)
  exact hg D

/-- For `n ≥ 1` every chord diagram is a relabelling of one with an isolated chord. -/
theorem exists_conj_hasAdjacentChord (k : ℕ) (D : ChordDiagram (k + 1)) :
    ∃ g : Perm (Fin (2 * (k + 1))), HasAdjacentChord (D.conj g) := by
  let z : Fin (2 * (k + 1)) := ⟨0, by omega⟩
  let o : Fin (2 * (k + 1)) := ⟨1, by omega⟩
  have hzo : z ≠ o := by simp [z, o]
  have hzD : z ≠ D.pairing z := (D.fixedPointFree z).symm
  refine ⟨swap o (D.pairing z), z, ?_⟩
  have key : ∀ (N : ℕ) (i : Fin N), i.val + 1 < N → (finRotate N i).val = i.val + 1 := by
    intro N i hi
    cases N with
    | zero => exact i.elim0
    | succ m =>
      have hm : 1 < m + 1 := by omega
      rw [finRotate_succ_apply, Fin.val_add, Fin.val_one', Nat.mod_eq_of_lt hm,
        Nat.mod_eq_of_lt hi]
  have hrot : finRotate (2 * (k + 1)) z = o := by
    ext
    rw [key _ z (by simp [z]; omega)]
  rw [ChordDiagram.conj_pairing, hrot, swap_inv, Perm.mul_apply, Perm.mul_apply,
    swap_apply_of_ne_of_ne hzo hzD, swap_apply_right]

/-- **The encoded `1T ⊔ 4T` is the whole module** in every degree `n ≥ 1`, over any commutative
ring in which `2` is a unit. -/
theorem relationsSubmodule_eq_top (h2 : IsUnit (2 : R)) (k : ℕ) :
    relationsSubmodule R (n := k + 1) = ⊤ := by
  rw [eq_top_iff, ← Finsupp.supported_univ, Finsupp.supported_eq_span_single, Submodule.span_le]
  rintro _ ⟨D, -, rfl⟩
  obtain ⟨g, hg⟩ := exists_conj_hasAdjacentChord k D
  have h1 : CDModule.of (D.conj g) ∈ relationsSubmodule R :=
    of_mem_relations_of_hasAdjacentChord (R := R) hg
  have h4 : CDModule.of (D.conj g) - CDModule.of D ∈ relationsSubmodule R :=
    fourTermSubmodule_le_relations R (conj_sub_mem R h2 g D)
  have := (relationsSubmodule R).sub_mem h1 h4
  rw [sub_sub_cancel] at this
  exact this

/-- **Every weight system of degree `n ≥ 1` is zero** under the current encoding, whenever `2`
is a unit in `R`. -/
theorem weightSystem_eq_zero (h2 : IsUnit (2 : R)) (k : ℕ) (w : WeightSystem R (k + 1)) :
    w = 0 := by
  have hsub : Subsingleton (AReduced R (k + 1)) := by
    rw [Submodule.Quotient.subsingleton_iff]
    intro x
    rw [relationsSubmodule_eq_top R h2 k]
    trivial
  refine LinearMap.ext fun x => ?_
  rw [Subsingleton.elim x 0, map_zero, LinearMap.zero_apply]

end QOU.KnotTheory.Vassiliev
