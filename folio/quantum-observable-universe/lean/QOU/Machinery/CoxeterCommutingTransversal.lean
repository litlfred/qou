/-
# The commuting transversal — CommutingCosetStructure derived from any Coxeter system

The `m = 2` twin of `CoxeterParabolicTransversal`: for ANY Coxeter system
and any generator pair with `M i j = 2`, the coset datum of the merged
far-commutation reduction (`CommutingCosetStructure`, #4081) is
CONSTRUCTED. Far commutation on the length-rule module at general rank
therefore holds modulo exactly one residual fact per pair:

    `cs.IsReduced [i, j]`

— the faithfulness of the 4-element `ℤ₂×ℤ₂` cell (the Tits residue,
decidable in any concrete system). The chain mirrors the dihedral case:
`commute2` (from `(σᵢσⱼ)² = 1`), `mem_parabolic2` (the parabolic is the
four cell elements `e, sᵢ, sⱼ, sᵢsⱼ`), unique minimal representatives via
the unconditional lifting lemma, the factorization bijection, the
`CommutingCosetStructure`, and the payoff `far_commute_at_pair`.

HONESTY (STRICT): sorry-free; the ONLY hypothesis beyond Mathlib's
`CoxeterSystem` is the reducedness of `[i, j]`, stated explicitly, never
an instance. Nothing wired; `1/(8π)` stays phase-4. Base ring: generic
`[CommRing R]` at the module payoff (§7c).

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Machinery.CoxeterParabolicTransversal
import QOU.Machinery.HeckeCommutingCellReduction

namespace QOU.Machinery.CoxeterParabolic

open CoxeterSystem List
open QOU.Machinery.HeckeGeneral

variable {B W : Type*} [Group W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W)

local prefix:100 "ℓ" => cs.length
local prefix:100 "π" => cs.wordProd
local prefix:100 "σ" => cs.simple

variable (i j : B)

/-! ## The four-element cell -/

/-- The four cell words of the `{i, j}` parabolic (`M i j = 2`), ordered
to match the merged `descentC2σi` tables: `e, sᵢ, sⱼ, sᵢsⱼ`. -/
def cellWord2 : Fin 4 → List B := ![[], [i], [j], [i, j]]

/-- The four cell elements. -/
noncomputable def cellElem2 (k : Fin 4) : W := π (cellWord2 i j k)

lemma cellWord2_length (k : Fin 4) :
    (cellWord2 i j k).length = descentC2σi.len k := by
  fin_cases k <;> simp [cellWord2, descentC2σi]

lemma cellWord2_mem (k : Fin 4) :
    ∀ l ∈ cellWord2 i j k, l ∈ ({i, j} : Set B) := by
  fin_cases k <;> simp [cellWord2]

lemma cellElem2_0 : cellElem2 cs i j 0 = 1 := by
  simp [cellElem2, cellWord2, wordProd_nil]

lemma cellElem2_1 : cellElem2 cs i j 1 = σ i := by
  simp [cellElem2, cellWord2, wordProd_cons, wordProd_nil]

lemma cellElem2_2 : cellElem2 cs i j 2 = σ j := by
  simp [cellElem2, cellWord2, wordProd_cons, wordProd_nil]

lemma cellElem2_3 : cellElem2 cs i j 3 = σ i * σ j := by
  simp [cellElem2, cellWord2, wordProd_cons, wordProd_nil]

/-! ## The commutation relation from `(σᵢσⱼ)² = 1` -/

lemma commute2 (hm : M i j = 2) : σ i * σ j = σ j * σ i := by
  have hpow : (σ i * σ j) ^ 2 = 1 := by
    have := cs.simple_mul_simple_pow i j
    rwa [hm] at this
  rw [pow_two] at hpow
  have h2 : σ i * σ j = (σ i * σ j)⁻¹ :=
    eq_inv_of_mul_eq_one_left hpow
  rw [h2, mul_inv_rev, cs.inv_simple, cs.inv_simple]

/-! ## Faithfulness consequences of `IsReduced [i, j]` -/

lemma wordProd_ij : π [i, j] = σ i * σ j := by
  simp [wordProd_cons, wordProd_nil]

lemma simple_ne_of_reduced2 (hred : cs.IsReduced [i, j]) : σ i ≠ σ j := by
  intro heq
  have h1 : π [i, j] = 1 := by
    rw [wordProd_ij, heq, cs.simple_mul_simple_self]
  have h2 : ℓ (π [i, j]) = 2 := hred
  rw [h1, cs.length_one] at h2
  exact absurd h2 (by omega)

/-- Every cell word is reduced, given the faithfulness residue. -/
lemma cellWord2_isReduced (hred : cs.IsReduced [i, j]) (k : Fin 4) :
    cs.IsReduced (cellWord2 i j k) := by
  fin_cases k
  · exact isReduced_nil cs
  · exact isReduced_single cs i
  · exact isReduced_single cs j
  · exact hred

/-- The four cell elements are pairwise distinct, given the faithfulness
residue. -/
lemma cellElem2_injective (hred : cs.IsReduced [i, j]) :
    Function.Injective (cellElem2 cs i j) := by
  intro k k' heq
  have hlen : ∀ m : Fin 4, ℓ (cellElem2 cs i j m) = (cellWord2 i j m).length :=
    fun m => cellWord2_isReduced cs i j hred m
  have hL : (cellWord2 i j k).length = (cellWord2 i j k').length := by
    rw [← hlen k, ← hlen k', heq]
  have hne := simple_ne_of_reduced2 cs i j hred
  fin_cases k <;> fin_cases k' <;>
    first
    | rfl
    | (refine absurd hL ?_
       simp [cellWord2]
       done)
    | (refine absurd ?_ hne
       have heq' : cellElem2 cs i j 1 = cellElem2 cs i j 2 := heq
       rwa [cellElem2_1, cellElem2_2] at heq')
    | (refine absurd ?_ hne
       have heq' : cellElem2 cs i j 2 = cellElem2 cs i j 1 := heq
       rw [cellElem2_2, cellElem2_1] at heq'
       exact heq'.symm)

/-! ## Multiplication tables (16 explicit identities) -/

/-- Left multiplication by `σᵢ` permutes the cell by `![1, 0, 3, 2]`. -/
lemma simple_i_mul_cell2 (k : Fin 4) :
    σ i * cellElem2 cs i j k = cellElem2 cs i j (![1, 0, 3, 2] k) := by
  have hss := cs.simple_mul_simple_self i
  fin_cases k
  · show σ i * cellElem2 cs i j 0 = cellElem2 cs i j 1
    rw [cellElem2_0, cellElem2_1, mul_one]
  · show σ i * cellElem2 cs i j 1 = cellElem2 cs i j 0
    rw [cellElem2_1, cellElem2_0]
    exact hss
  · show σ i * cellElem2 cs i j 2 = cellElem2 cs i j 3
    rw [cellElem2_2, cellElem2_3]
  · show σ i * cellElem2 cs i j 3 = cellElem2 cs i j 2
    rw [cellElem2_3, cellElem2_2, ← mul_assoc, hss, one_mul]

/-- Left multiplication by `σⱼ` permutes the cell by `![2, 3, 0, 1]`
(commutation-bearing entries). -/
lemma simple_j_mul_cell2 (hm : M i j = 2) (k : Fin 4) :
    σ j * cellElem2 cs i j k = cellElem2 cs i j (![2, 3, 0, 1] k) := by
  have hss := cs.simple_mul_simple_self j
  have hc := commute2 cs i j hm
  fin_cases k
  · show σ j * cellElem2 cs i j 0 = cellElem2 cs i j 2
    rw [cellElem2_0, cellElem2_2, mul_one]
  · show σ j * cellElem2 cs i j 1 = cellElem2 cs i j 3
    rw [cellElem2_1, cellElem2_3]
    exact hc.symm
  · show σ j * cellElem2 cs i j 2 = cellElem2 cs i j 0
    rw [cellElem2_2, cellElem2_0]
    exact hss
  · show σ j * cellElem2 cs i j 3 = cellElem2 cs i j 1
    rw [cellElem2_3, cellElem2_1, ← mul_assoc, ← hc, mul_assoc,
      cs.simple_mul_simple_self, mul_one]

/-- Right multiplication by `σᵢ` is the `descentC2σi` table. -/
lemma cell2_mul_simple_i (hm : M i j = 2) (k : Fin 4) :
    cellElem2 cs i j k * σ i = cellElem2 cs i j (descentC2σi.t k) := by
  have hss := cs.simple_mul_simple_self i
  have hc := commute2 cs i j hm
  fin_cases k
  · show cellElem2 cs i j 0 * σ i = cellElem2 cs i j (descentC2σi.t 0)
    rw [show descentC2σi.t 0 = 1 from rfl, cellElem2_0, cellElem2_1, one_mul]
  · show cellElem2 cs i j 1 * σ i = cellElem2 cs i j (descentC2σi.t 1)
    rw [show descentC2σi.t 1 = 0 from rfl, cellElem2_1, cellElem2_0]
    exact hss
  · show cellElem2 cs i j 2 * σ i = cellElem2 cs i j (descentC2σi.t 2)
    rw [show descentC2σi.t 2 = 3 from rfl, cellElem2_2, cellElem2_3]
    exact hc.symm
  · show cellElem2 cs i j 3 * σ i = cellElem2 cs i j (descentC2σi.t 3)
    rw [show descentC2σi.t 3 = 2 from rfl, cellElem2_3, cellElem2_2, hc,
      mul_assoc, cs.simple_mul_simple_self, mul_one]

/-- Right multiplication by `σⱼ` is the `descentC2σj` table. -/
lemma cell2_mul_simple_j (k : Fin 4) :
    cellElem2 cs i j k * σ j = cellElem2 cs i j (descentC2σj.t k) := by
  have hss := cs.simple_mul_simple_self j
  fin_cases k
  · show cellElem2 cs i j 0 * σ j = cellElem2 cs i j (descentC2σj.t 0)
    rw [show descentC2σj.t 0 = 2 from rfl, cellElem2_0, cellElem2_2, one_mul]
  · show cellElem2 cs i j 1 * σ j = cellElem2 cs i j (descentC2σj.t 1)
    rw [show descentC2σj.t 1 = 3 from rfl, cellElem2_1, cellElem2_3]
  · show cellElem2 cs i j 2 * σ j = cellElem2 cs i j (descentC2σj.t 2)
    rw [show descentC2σj.t 2 = 0 from rfl, cellElem2_2, cellElem2_0]
    exact hss
  · show cellElem2 cs i j 3 * σ j = cellElem2 cs i j (descentC2σj.t 3)
    rw [show descentC2σj.t 3 = 1 from rfl, cellElem2_3, cellElem2_1, mul_assoc,
      hss, mul_one]

/-! ## The parabolic is exactly the cell -/

/-- **`W_{i,j}` is exactly the four cell elements** (`M i j = 2`). -/
theorem mem_parabolic2 (hm : M i j = 2) {x : W}
    (hx : x ∈ parabolic cs ({i, j} : Set B)) :
    ∃ k, x = cellElem2 cs i j k := by
  induction hx using Subgroup.closure_induction_left with
  | one => exact ⟨0, (cellElem2_0 cs i j).symm⟩
  | mul_left s hs y _ ih =>
    obtain ⟨k, rfl⟩ := ih
    obtain ⟨l, hl, rfl⟩ := hs
    rw [Set.mem_insert_iff, Set.mem_singleton_iff] at hl
    rcases hl with rfl | rfl
    · exact ⟨_, simple_i_mul_cell2 cs l j k⟩
    · exact ⟨_, simple_j_mul_cell2 cs i l hm k⟩
  | inv_mul_cancel s hs y _ ih =>
    obtain ⟨k, rfl⟩ := ih
    obtain ⟨l, hl, rfl⟩ := hs
    rw [Set.mem_insert_iff, Set.mem_singleton_iff] at hl
    rcases hl with rfl | rfl
    · rw [cs.inv_simple]
      exact ⟨_, simple_i_mul_cell2 cs l j k⟩
    · rw [cs.inv_simple]
      exact ⟨_, simple_j_mul_cell2 cs i l hm k⟩

/-! ## Unique minimal representatives and the factorization -/

lemma length_minRep_mul_cell2 (hred : cs.IsReduced [i, j]) {u : W}
    (hu : IsMinRep cs ({i, j} : Set B) u) (k : Fin 4) :
    ℓ (u * cellElem2 cs i j k) = ℓ u + (cellWord2 i j k).length :=
  length_minRep_mul_wordProd' cs ({i, j} : Set B) hu
    (cellWord2_mem i j k) (cellWord2_isReduced cs i j hred k)

/-- **Each coset has a unique minimal representative** (`M i j = 2`). -/
theorem isMinRep_unique2 (hm : M i j = 2) (hred : cs.IsReduced [i, j])
    {u u' : W} (hu : IsMinRep cs ({i, j} : Set B) u)
    (hu' : IsMinRep cs ({i, j} : Set B) u')
    (hc : SameCosetJ cs ({i, j} : Set B) u u') : u = u' := by
  obtain ⟨k, hk⟩ := mem_parabolic2 cs i j hm hc
  have hu'eq : u' = u * cellElem2 cs i j k := by
    rw [← hk]
    group
  have hlen : ℓ u' = ℓ u + (cellWord2 i j k).length := by
    rw [hu'eq]
    exact length_minRep_mul_cell2 cs i j hred hu k
  have h1 : ℓ u ≤ ℓ u' := hu u' hc
  have h2 : ℓ u' ≤ ℓ u := hu' u (sameCosetJ_symm cs _ hc)
  have h0 : (cellWord2 i j k).length = 0 := by omega
  have hk0 : k = 0 := by
    fin_cases k <;> simp_all [cellWord2]
  rw [hu'eq, hk0, cellElem2_0, mul_one]

/-- The factorization map `(min reps) × Fin 4 → W`. -/
noncomputable def cellMap2 :
    {u : W // IsMinRep cs ({i, j} : Set B) u} × Fin 4 → W :=
  fun p => p.1.val * cellElem2 cs i j p.2

/-- **The parabolic factorization is a bijection** (`M i j = 2`). -/
theorem cellMap2_bijective (hm : M i j = 2) (hred : cs.IsReduced [i, j]) :
    Function.Bijective (cellMap2 cs i j) := by
  constructor
  · rintro ⟨⟨u, hu⟩, k⟩ ⟨⟨u', hu'⟩, k'⟩ heq
    simp only [cellMap2] at heq
    have hcoset : SameCosetJ cs ({i, j} : Set B) u u' := by
      show u⁻¹ * u' ∈ parabolic cs ({i, j} : Set B)
      have h' : u' = (u * cellElem2 cs i j k) * (cellElem2 cs i j k')⁻¹ := by
        rw [heq]
        group
      have hval : u⁻¹ * u'
          = cellElem2 cs i j k * (cellElem2 cs i j k')⁻¹ := by
        rw [h']
        group
      rw [hval]
      exact (parabolic cs _).mul_mem
        (wordProd_mem_parabolic cs _ (cellWord2_mem i j k))
        ((parabolic cs _).inv_mem
          (wordProd_mem_parabolic cs _ (cellWord2_mem i j k')))
    have huu : u = u' := isMinRep_unique2 cs i j hm hred hu hu' hcoset
    subst huu
    have hcell : cellElem2 cs i j k = cellElem2 cs i j k' :=
      mul_left_cancel heq
    have hkk := cellElem2_injective cs i j hred hcell
    rw [hkk]
  · intro w
    obtain ⟨u, hcoset, humin⟩ := exists_minRep cs ({i, j} : Set B) w
    have hmem : u⁻¹ * w ∈ parabolic cs ({i, j} : Set B) := by
      have := (parabolic cs ({i, j} : Set B)).inv_mem hcoset
      simpa [mul_inv_rev] using this
    obtain ⟨k, hk⟩ := mem_parabolic2 cs i j hm hmem
    refine ⟨(⟨u, humin⟩, k), ?_⟩
    show u * cellElem2 cs i j k = w
    rw [← hk]
    group

/-! ## The CommutingCosetStructure, constructed -/

/-- **The commuting coset structure of any `M i j = 2` pair**, constructed
from the Coxeter system modulo the single faithfulness residue
`IsReduced [i, j]`. The far-commutation reduction's coset hypothesis,
discharged. -/
noncomputable def commutingTransversal (hm : M i j = 2)
    (hred : cs.IsReduced [i, j]) : CommutingCosetStructure W :=
  letI e := Equiv.ofBijective _ (cellMap2_bijective cs i j hm hred)
  { C := {u : W // IsMinRep cs ({i, j} : Set B) u}
    equiv := e.symm
    len := cs.length
    len0 := fun u => ℓ u.val
    ti := fun w => w * σ i
    tj := fun w => w * σ j
    len_add := by
      intro w
      have hw : cellMap2 cs i j (e.symm w) = w := e.apply_symm_apply w
      conv_lhs => rw [← hw]
      show ℓ ((e.symm w).1.val * cellElem2 cs i j (e.symm w).2)
        = ℓ (e.symm w).1.val + descentC2σi.len (e.symm w).2
      rw [length_minRep_mul_cell2 cs i j hred (e.symm w).1.prop,
        cellWord2_length]
    ti_eq := by
      intro w
      have hw : cellMap2 cs i j (e.symm w) = w := e.apply_symm_apply w
      have hstep : w * σ i
          = cellMap2 cs i j ((e.symm w).1, descentC2σi.t (e.symm w).2) := by
        conv_lhs => rw [← hw]
        show (e.symm w).1.val * cellElem2 cs i j (e.symm w).2 * σ i
          = (e.symm w).1.val * cellElem2 cs i j (descentC2σi.t (e.symm w).2)
        rw [mul_assoc, cell2_mul_simple_i cs i j hm]
      show e.symm (w * σ i) = ((e.symm w).1, descentC2σi.t (e.symm w).2)
      rw [hstep]
      exact e.symm_apply_apply _
    tj_eq := by
      intro w
      have hw : cellMap2 cs i j (e.symm w) = w := e.apply_symm_apply w
      have hstep : w * σ j
          = cellMap2 cs i j ((e.symm w).1, descentC2σj.t (e.symm w).2) := by
        conv_lhs => rw [← hw]
        show (e.symm w).1.val * cellElem2 cs i j (e.symm w).2 * σ j
          = (e.symm w).1.val * cellElem2 cs i j (descentC2σj.t (e.symm w).2)
        rw [mul_assoc, cell2_mul_simple_j]
      show e.symm (w * σ j) = ((e.symm w).1, descentC2σj.t (e.symm w).2)
      rw [hstep]
      exact e.symm_apply_apply _ }

/-- **THE PAYOFF — far commutation at general rank, from the Coxeter
system**: on the length-rule module `W → R`, the right-multiplication
descent actions of any `M i j = 2` pair commute, given only the
cell-faithfulness residue. Together with `braid_at_pair` and the merged
all-ranks quadratic, all three Hecke presentation-law kinds now flow from
`CoxeterSystem` data. -/
theorem far_commute_at_pair {R : Type*} [CommRing R] (hm : M i j = 2)
    (hred : cs.IsReduced [i, j]) (h : R) (v : W → R) :
    mulStep (commutingTransversal cs i j hm hred).Di h
        (mulStep (commutingTransversal cs i j hm hred).Dj h v)
      = mulStep (commutingTransversal cs i j hm hred).Dj h
          (mulStep (commutingTransversal cs i j hm hred).Di h v) :=
  CommutingCosetStructure.far_commute_of_commuting _ h v

end QOU.Machinery.CoxeterParabolic
