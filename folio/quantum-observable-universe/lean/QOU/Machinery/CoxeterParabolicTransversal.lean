/-
# The parabolic transversal — DihedralCosetStructure derived from any Coxeter system

The assembly brick promised by the exchange proof (`CoxeterReflectionCocycle`,
merged #4102): for ANY Coxeter system and any generator pair `i, j` with
`M i j = 3`, the coset datum of the merged braid reduction
(`DihedralCosetStructure`, #4059) is CONSTRUCTED — no longer a hypothesis.
The braid relation on the length-rule module at general rank therefore
holds modulo exactly ONE residual fact per pair:

    `cs.IsReduced [i, j, i]`

— the faithfulness of the 6-element dihedral cell. This is the Tits
faithfulness residue: a theorem of Coxeter theory (via the geometric
representation, not yet in Mathlib), decidable in any concrete system;
every other obligation of the coset datum is discharged here
unconditionally from the proved exchange property:

* **`mem_parabolic3`** — the parabolic `W_{i,j}` is exactly the six cell
  elements `e, sᵢ, sⱼ, sⱼsᵢ, sᵢsⱼ, sᵢsⱼsᵢ` (closure induction on left
  multiplication; the 12 product identities use only `σ² = 1` and the
  braid relation, itself derived from `(σᵢσⱼ)³ = 1`).
* **`isMinRep_unique`** — each coset has a UNIQUE minimal representative
  (the unconditional lifting lemma forces the connecting cell element to
  have length 0).
* **`cellMap3_bijective`** — the parabolic factorization
  `W ≃ (min reps) × Fin 6`.
* **`dihedralTransversal`** — the `DihedralCosetStructure` itself: length
  additivity from the lifting lemma; cell-wise right-multiplication
  action matching the `decide`-checked `descentH3σ₀` / `descentH3σ₁`
  tables.
* **`braid_at_pair`** — the payoff: the braid relation on the length-rule
  module `W → R`, for every `M i j = 3` pair of every Coxeter system,
  given the cell-faithfulness residue.

HONESTY (STRICT): sorry-free; the ONLY hypothesis beyond Mathlib's
`CoxeterSystem` is the reducedness of the single word `[i, j, i]` — stated
explicitly in every result that needs it, never smuggled through an
instance. Nothing wired; `1/(8π)` stays phase-4. Base ring: generic
`[CommRing R]` at the module payoff (§7c).

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Machinery.CoxeterReflectionCocycle
import QOU.Machinery.HeckeDihedralBraidReduction

namespace QOU.Machinery.CoxeterParabolic

open CoxeterSystem List
open QOU.Machinery.HeckeGeneral

variable {B W : Type*} [Group W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W)

local prefix:100 "ℓ" => cs.length
local prefix:100 "π" => cs.wordProd
local prefix:100 "σ" => cs.simple

variable (i j : B)

/-! ## The six-element cell -/

/-- The six cell words of the `{i, j}` parabolic (`M i j = 3`), ordered to
match the merged `descentH3σ₀` tables: `e, sᵢ, sⱼ, sⱼsᵢ, sᵢsⱼ, sᵢsⱼsᵢ`. -/
def cellWord3 : Fin 6 → List B := ![[], [i], [j], [j, i], [i, j], [i, j, i]]

/-- The six cell elements. -/
noncomputable def cellElem3 (k : Fin 6) : W := π (cellWord3 i j k)

lemma cellWord3_length (k : Fin 6) :
    (cellWord3 i j k).length = descentH3σ₀.len k := by
  fin_cases k <;> simp [cellWord3, descentH3σ₀]

lemma cellWord3_mem (k : Fin 6) :
    ∀ l ∈ cellWord3 i j k, l ∈ ({i, j} : Set B) := by
  fin_cases k <;> simp [cellWord3]

lemma cellElem3_0 : cellElem3 cs i j 0 = 1 := by
  simp [cellElem3, cellWord3, wordProd_nil]

lemma cellElem3_1 : cellElem3 cs i j 1 = σ i := by
  simp [cellElem3, cellWord3, wordProd_cons, wordProd_nil]

lemma cellElem3_2 : cellElem3 cs i j 2 = σ j := by
  simp [cellElem3, cellWord3, wordProd_cons, wordProd_nil]

lemma cellElem3_3 : cellElem3 cs i j 3 = σ j * σ i := by
  simp [cellElem3, cellWord3, wordProd_cons, wordProd_nil]

lemma cellElem3_4 : cellElem3 cs i j 4 = σ i * σ j := by
  simp [cellElem3, cellWord3, wordProd_cons, wordProd_nil]

lemma cellElem3_5 : cellElem3 cs i j 5 = σ i * σ j * σ i := by
  simp [cellElem3, cellWord3, wordProd_cons, wordProd_nil, mul_assoc]

/-! ## Relations: the braid from `(σᵢσⱼ)³ = 1` -/

/-- The braid relation `σᵢσⱼσᵢ = σⱼσᵢσⱼ`, from the Coxeter relation at
`M i j = 3`. -/
lemma braid3 (hm : M i j = 3) : σ i * σ j * σ i = σ j * σ i * σ j := by
  have hpow : (σ i * σ j) ^ 3 = 1 := by
    have := cs.simple_mul_simple_pow i j
    rwa [hm] at this
  have h1 : (σ i * σ j * σ i) * (σ j * σ i * σ j) = 1 := by
    have hexp : (σ i * σ j) ^ 3 = (σ i * σ j * σ i) * (σ j * σ i * σ j) := by
      rw [pow_succ, pow_succ, pow_one]
      group
    rw [← hexp, hpow]
  have h2 : σ i * σ j * σ i = (σ j * σ i * σ j)⁻¹ :=
    eq_inv_of_mul_eq_one_left h1
  rw [h2, mul_inv_rev, mul_inv_rev, cs.inv_simple, cs.inv_simple, ← mul_assoc]

/-! ## Faithfulness consequences of `IsReduced [i, j, i]` -/

lemma wordProd_iji : π [i, j, i] = σ i * σ j * σ i := by
  simp [wordProd_cons, wordProd_nil, mul_assoc]

lemma simple_ne_of_reduced (hred : cs.IsReduced [i, j, i]) : σ i ≠ σ j := by
  intro heq
  have h1 : π [i, j, i] = σ i := by
    rw [wordProd_iji, ← heq, mul_assoc, cs.simple_mul_simple_self, mul_one]
  have h2 : ℓ (π [i, j, i]) = 3 := hred
  rw [h1, cs.length_simple] at h2
  exact absurd h2 (by omega)

lemma isReduced_ij (hred : cs.IsReduced [i, j, i]) : cs.IsReduced [i, j] :=
  isReduced_of_isReduced_concat cs hred

lemma isReduced_ji (hred : cs.IsReduced [i, j, i]) : cs.IsReduced [j, i] := by
  have hij : ℓ (π [i, j]) = 2 := isReduced_ij cs i j hred
  show ℓ (π [j, i]) = 2
  have hinv : π [j, i] = (π [i, j])⁻¹ := by
    simp [wordProd_cons, wordProd_nil, mul_inv_rev, cs.inv_simple]
  rw [hinv, cs.length_inv, hij]

lemma isReduced_single (c : B) : cs.IsReduced [c] := by
  show ℓ (π [c]) = 1
  simp [wordProd_cons, wordProd_nil, cs.length_simple]

lemma isReduced_nil : cs.IsReduced ([] : List B) := by
  show ℓ (π ([] : List B)) = 0
  simp [wordProd_nil]

/-- Every cell word is reduced, given the faithfulness residue. -/
lemma cellWord3_isReduced (hred : cs.IsReduced [i, j, i]) (k : Fin 6) :
    cs.IsReduced (cellWord3 i j k) := by
  fin_cases k
  · exact isReduced_nil cs
  · exact isReduced_single cs i
  · exact isReduced_single cs j
  · exact isReduced_ji cs i j hred
  · exact isReduced_ij cs i j hred
  · exact hred

/-- The six cell elements are pairwise distinct, given the faithfulness
residue. -/
lemma cellElem3_injective (hred : cs.IsReduced [i, j, i]) :
    Function.Injective (cellElem3 cs i j) := by
  intro k k' heq
  have hlen : ∀ m : Fin 6, ℓ (cellElem3 cs i j m) = (cellWord3 i j m).length :=
    fun m => cellWord3_isReduced cs i j hred m
  have hL : (cellWord3 i j k).length = (cellWord3 i j k').length := by
    rw [← hlen k, ← hlen k', heq]
  have hne := simple_ne_of_reduced cs i j hred
  have h34 : ¬ (σ j * σ i = σ i * σ j) := by
    intro heq34
    have h5 : σ i * σ j * σ i = σ j := by
      calc σ i * σ j * σ i = σ j * σ i * σ i := by rw [← heq34]
        _ = σ j := by rw [mul_assoc, cs.simple_mul_simple_self, mul_one]
    have h2 : ℓ (π [i, j, i]) = 3 := hred
    rw [wordProd_iji, h5, cs.length_simple] at h2
    exact absurd h2 (by omega)
  fin_cases k <;> fin_cases k' <;>
    first
    | rfl
    | (refine absurd hL ?_
       simp [cellWord3]
       done)
    | (refine absurd ?_ hne
       have heq' : cellElem3 cs i j 1 = cellElem3 cs i j 2 := heq
       rwa [cellElem3_1, cellElem3_2] at heq')
    | (refine absurd ?_ hne
       have heq' : cellElem3 cs i j 2 = cellElem3 cs i j 1 := heq
       rw [cellElem3_2, cellElem3_1] at heq'
       exact heq'.symm)
    | (refine absurd ?_ h34
       have heq' : cellElem3 cs i j 3 = cellElem3 cs i j 4 := heq
       rwa [cellElem3_3, cellElem3_4] at heq')
    | (refine absurd ?_ h34
       have heq' : cellElem3 cs i j 4 = cellElem3 cs i j 3 := heq
       rw [cellElem3_4, cellElem3_3] at heq'
       exact heq'.symm)

/-! ## Multiplication tables (24 explicit identities) -/

/-- Left multiplication by `σᵢ` permutes the cell by `![1, 0, 4, 5, 2, 3]`. -/
lemma simple_i_mul_cell3 (k : Fin 6) :
    σ i * cellElem3 cs i j k = cellElem3 cs i j (![1, 0, 4, 5, 2, 3] k) := by
  have hss := cs.simple_mul_simple_self i
  fin_cases k
  · show σ i * cellElem3 cs i j 0 = cellElem3 cs i j 1
    rw [cellElem3_0, cellElem3_1, mul_one]
  · show σ i * cellElem3 cs i j 1 = cellElem3 cs i j 0
    rw [cellElem3_1, cellElem3_0]
    exact hss
  · show σ i * cellElem3 cs i j 2 = cellElem3 cs i j 4
    rw [cellElem3_2, cellElem3_4]
  · show σ i * cellElem3 cs i j 3 = cellElem3 cs i j 5
    rw [cellElem3_3, cellElem3_5, ← mul_assoc]
  · show σ i * cellElem3 cs i j 4 = cellElem3 cs i j 2
    rw [cellElem3_4, cellElem3_2, ← mul_assoc, hss, one_mul]
  · show σ i * cellElem3 cs i j 5 = cellElem3 cs i j 3
    rw [cellElem3_5, cellElem3_3, ← mul_assoc, ← mul_assoc, hss, one_mul]

/-- Left multiplication by `σⱼ` permutes the cell by `![2, 3, 0, 1, 5, 4]`
(two braid-bearing entries). -/
lemma simple_j_mul_cell3 (hm : M i j = 3) (k : Fin 6) :
    σ j * cellElem3 cs i j k = cellElem3 cs i j (![2, 3, 0, 1, 5, 4] k) := by
  have hss := cs.simple_mul_simple_self j
  have hb := braid3 cs i j hm
  fin_cases k
  · show σ j * cellElem3 cs i j 0 = cellElem3 cs i j 2
    rw [cellElem3_0, cellElem3_2, mul_one]
  · show σ j * cellElem3 cs i j 1 = cellElem3 cs i j 3
    rw [cellElem3_1, cellElem3_3]
  · show σ j * cellElem3 cs i j 2 = cellElem3 cs i j 0
    rw [cellElem3_2, cellElem3_0]
    exact hss
  · show σ j * cellElem3 cs i j 3 = cellElem3 cs i j 1
    rw [cellElem3_3, cellElem3_1, ← mul_assoc, hss, one_mul]
  · show σ j * cellElem3 cs i j 4 = cellElem3 cs i j 5
    rw [cellElem3_4, cellElem3_5, ← mul_assoc, ← hb]
  · show σ j * cellElem3 cs i j 5 = cellElem3 cs i j 4
    rw [cellElem3_5, cellElem3_4, ← mul_assoc, ← mul_assoc, ← hb, mul_assoc,
      cs.simple_mul_simple_self, mul_one]

/-- Right multiplication by `σᵢ` is the `descentH3σ₀` table. -/
lemma cell3_mul_simple_i (k : Fin 6) :
    cellElem3 cs i j k * σ i = cellElem3 cs i j (descentH3σ₀.t k) := by
  have hss := cs.simple_mul_simple_self i
  fin_cases k
  · show cellElem3 cs i j 0 * σ i = cellElem3 cs i j (descentH3σ₀.t 0)
    rw [show descentH3σ₀.t 0 = 1 from rfl, cellElem3_0, cellElem3_1, one_mul]
  · show cellElem3 cs i j 1 * σ i = cellElem3 cs i j (descentH3σ₀.t 1)
    rw [show descentH3σ₀.t 1 = 0 from rfl, cellElem3_1, cellElem3_0]
    exact hss
  · show cellElem3 cs i j 2 * σ i = cellElem3 cs i j (descentH3σ₀.t 2)
    rw [show descentH3σ₀.t 2 = 3 from rfl, cellElem3_2, cellElem3_3]
  · show cellElem3 cs i j 3 * σ i = cellElem3 cs i j (descentH3σ₀.t 3)
    rw [show descentH3σ₀.t 3 = 2 from rfl, cellElem3_3, cellElem3_2, mul_assoc,
      hss, mul_one]
  · show cellElem3 cs i j 4 * σ i = cellElem3 cs i j (descentH3σ₀.t 4)
    rw [show descentH3σ₀.t 4 = 5 from rfl, cellElem3_4, cellElem3_5]
  · show cellElem3 cs i j 5 * σ i = cellElem3 cs i j (descentH3σ₀.t 5)
    rw [show descentH3σ₀.t 5 = 4 from rfl, cellElem3_5, cellElem3_4, mul_assoc,
      hss, mul_one]

/-- Right multiplication by `σⱼ` is the `descentH3σ₁` table (two
braid-bearing entries). -/
lemma cell3_mul_simple_j (hm : M i j = 3) (k : Fin 6) :
    cellElem3 cs i j k * σ j = cellElem3 cs i j (descentH3σ₁.t k) := by
  have hss := cs.simple_mul_simple_self j
  have hb := braid3 cs i j hm
  fin_cases k
  · show cellElem3 cs i j 0 * σ j = cellElem3 cs i j (descentH3σ₁.t 0)
    rw [show descentH3σ₁.t 0 = 2 from rfl, cellElem3_0, cellElem3_2, one_mul]
  · show cellElem3 cs i j 1 * σ j = cellElem3 cs i j (descentH3σ₁.t 1)
    rw [show descentH3σ₁.t 1 = 4 from rfl, cellElem3_1, cellElem3_4]
  · show cellElem3 cs i j 2 * σ j = cellElem3 cs i j (descentH3σ₁.t 2)
    rw [show descentH3σ₁.t 2 = 0 from rfl, cellElem3_2, cellElem3_0]
    exact hss
  · show cellElem3 cs i j 3 * σ j = cellElem3 cs i j (descentH3σ₁.t 3)
    rw [show descentH3σ₁.t 3 = 5 from rfl, cellElem3_3, cellElem3_5, ← hb]
  · show cellElem3 cs i j 4 * σ j = cellElem3 cs i j (descentH3σ₁.t 4)
    rw [show descentH3σ₁.t 4 = 1 from rfl, cellElem3_4, cellElem3_1, mul_assoc,
      hss, mul_one]
  · show cellElem3 cs i j 5 * σ j = cellElem3 cs i j (descentH3σ₁.t 5)
    rw [show descentH3σ₁.t 5 = 3 from rfl, cellElem3_5, cellElem3_3, hb,
      mul_assoc, hss, mul_one]

/-! ## The parabolic is exactly the cell -/

/-- **`W_{i,j}` is exactly the six cell elements** — closure induction on
left multiplication. -/
theorem mem_parabolic3 (hm : M i j = 3) {x : W}
    (hx : x ∈ parabolic cs ({i, j} : Set B)) :
    ∃ k, x = cellElem3 cs i j k := by
  induction hx using Subgroup.closure_induction_left with
  | one => exact ⟨0, (cellElem3_0 cs i j).symm⟩
  | mul_left s hs y _ ih =>
    obtain ⟨k, rfl⟩ := ih
    obtain ⟨l, hl, rfl⟩ := hs
    rw [Set.mem_insert_iff, Set.mem_singleton_iff] at hl
    rcases hl with rfl | rfl
    · exact ⟨_, simple_i_mul_cell3 cs l j k⟩
    · exact ⟨_, simple_j_mul_cell3 cs i l hm k⟩
  | inv_mul_cancel s hs y _ ih =>
    obtain ⟨k, rfl⟩ := ih
    obtain ⟨l, hl, rfl⟩ := hs
    rw [Set.mem_insert_iff, Set.mem_singleton_iff] at hl
    rcases hl with rfl | rfl
    · rw [cs.inv_simple]
      exact ⟨_, simple_i_mul_cell3 cs l j k⟩
    · rw [cs.inv_simple]
      exact ⟨_, simple_j_mul_cell3 cs i l hm k⟩

/-! ## Unique minimal representatives and the factorization -/

/-- Length additivity of a minimal representative against a cell element
(the unconditional lifting lemma, specialised). -/
lemma length_minRep_mul_cell3 (hred : cs.IsReduced [i, j, i]) {u : W}
    (hu : IsMinRep cs ({i, j} : Set B) u) (k : Fin 6) :
    ℓ (u * cellElem3 cs i j k) = ℓ u + (cellWord3 i j k).length :=
  length_minRep_mul_wordProd' cs ({i, j} : Set B) hu
    (cellWord3_mem i j k) (cellWord3_isReduced cs i j hred k)

/-- **Each coset has a unique minimal representative.** -/
theorem isMinRep_unique (hm : M i j = 3) (hred : cs.IsReduced [i, j, i])
    {u u' : W} (hu : IsMinRep cs ({i, j} : Set B) u)
    (hu' : IsMinRep cs ({i, j} : Set B) u')
    (hc : SameCosetJ cs ({i, j} : Set B) u u') : u = u' := by
  obtain ⟨k, hk⟩ := mem_parabolic3 cs i j hm hc
  have hu'eq : u' = u * cellElem3 cs i j k := by
    rw [← hk]
    group
  have hlen : ℓ u' = ℓ u + (cellWord3 i j k).length := by
    rw [hu'eq]
    exact length_minRep_mul_cell3 cs i j hred hu k
  have h1 : ℓ u ≤ ℓ u' := hu u' hc
  have h2 : ℓ u' ≤ ℓ u := hu' u (sameCosetJ_symm cs _ hc)
  have h0 : (cellWord3 i j k).length = 0 := by omega
  have hk0 : k = 0 := by
    fin_cases k <;> simp_all [cellWord3]
  rw [hu'eq, hk0, cellElem3_0, mul_one]

/-- The factorization map `(min reps) × Fin 6 → W`. -/
noncomputable def cellMap3 :
    {u : W // IsMinRep cs ({i, j} : Set B) u} × Fin 6 → W :=
  fun p => p.1.val * cellElem3 cs i j p.2

/-- **The parabolic factorization is a bijection.** -/
theorem cellMap3_bijective (hm : M i j = 3) (hred : cs.IsReduced [i, j, i]) :
    Function.Bijective (cellMap3 cs i j) := by
  constructor
  · rintro ⟨⟨u, hu⟩, k⟩ ⟨⟨u', hu'⟩, k'⟩ heq
    simp only [cellMap3] at heq
    have hcoset : SameCosetJ cs ({i, j} : Set B) u u' := by
      show u⁻¹ * u' ∈ parabolic cs ({i, j} : Set B)
      have h' : u' = (u * cellElem3 cs i j k) * (cellElem3 cs i j k')⁻¹ := by
        rw [heq]
        group
      have hval : u⁻¹ * u'
          = cellElem3 cs i j k * (cellElem3 cs i j k')⁻¹ := by
        rw [h']
        group
      rw [hval]
      exact (parabolic cs _).mul_mem
        (wordProd_mem_parabolic cs _ (cellWord3_mem i j k))
        ((parabolic cs _).inv_mem
          (wordProd_mem_parabolic cs _ (cellWord3_mem i j k')))
    have huu : u = u' := isMinRep_unique cs i j hm hred hu hu' hcoset
    subst huu
    have hcell : cellElem3 cs i j k = cellElem3 cs i j k' :=
      mul_left_cancel heq
    have hkk := cellElem3_injective cs i j hred hcell
    rw [hkk]
  · intro w
    obtain ⟨u, hcoset, humin⟩ := exists_minRep cs ({i, j} : Set B) w
    have hmem : u⁻¹ * w ∈ parabolic cs ({i, j} : Set B) := by
      have := (parabolic cs ({i, j} : Set B)).inv_mem hcoset
      simpa [mul_inv_rev] using this
    obtain ⟨k, hk⟩ := mem_parabolic3 cs i j hm hmem
    refine ⟨(⟨u, humin⟩, k), ?_⟩
    show u * cellElem3 cs i j k = w
    rw [← hk]
    group

/-! ## The DihedralCosetStructure, constructed -/

/-- **The dihedral coset structure of any `M i j = 3` pair**, constructed
from the Coxeter system modulo the single faithfulness residue
`IsReduced [i, j, i]`. The braid reduction's coset hypothesis, discharged. -/
noncomputable def dihedralTransversal (hm : M i j = 3)
    (hred : cs.IsReduced [i, j, i]) : DihedralCosetStructure W :=
  letI e := Equiv.ofBijective _ (cellMap3_bijective cs i j hm hred)
  { C := {u : W // IsMinRep cs ({i, j} : Set B) u}
    equiv := e.symm
    len := cs.length
    len0 := fun u => ℓ u.val
    ti := fun w => w * σ i
    tj := fun w => w * σ j
    len_add := by
      intro w
      have hw : cellMap3 cs i j (e.symm w) = w := e.apply_symm_apply w
      conv_lhs => rw [← hw]
      show ℓ ((e.symm w).1.val * cellElem3 cs i j (e.symm w).2)
        = ℓ (e.symm w).1.val + descentH3σ₀.len (e.symm w).2
      rw [length_minRep_mul_cell3 cs i j hred (e.symm w).1.prop,
        cellWord3_length]
    ti_eq := by
      intro w
      have hw : cellMap3 cs i j (e.symm w) = w := e.apply_symm_apply w
      have hstep : w * σ i
          = cellMap3 cs i j ((e.symm w).1, descentH3σ₀.t (e.symm w).2) := by
        conv_lhs => rw [← hw]
        show (e.symm w).1.val * cellElem3 cs i j (e.symm w).2 * σ i
          = (e.symm w).1.val * cellElem3 cs i j (descentH3σ₀.t (e.symm w).2)
        rw [mul_assoc, cell3_mul_simple_i]
      show e.symm (w * σ i) = ((e.symm w).1, descentH3σ₀.t (e.symm w).2)
      rw [hstep]
      exact e.symm_apply_apply _
    tj_eq := by
      intro w
      have hw : cellMap3 cs i j (e.symm w) = w := e.apply_symm_apply w
      have hstep : w * σ j
          = cellMap3 cs i j ((e.symm w).1, descentH3σ₁.t (e.symm w).2) := by
        conv_lhs => rw [← hw]
        show (e.symm w).1.val * cellElem3 cs i j (e.symm w).2 * σ j
          = (e.symm w).1.val * cellElem3 cs i j (descentH3σ₁.t (e.symm w).2)
        rw [mul_assoc, cell3_mul_simple_j cs i j hm]
      show e.symm (w * σ j) = ((e.symm w).1, descentH3σ₁.t (e.symm w).2)
      rw [hstep]
      exact e.symm_apply_apply _ }

/-- **THE PAYOFF — the braid relation at general rank, from the Coxeter
system**: on the length-rule module `W → R`, the right-multiplication
descent actions of any `M i j = 3` pair satisfy the braid relation, given
only the cell-faithfulness residue. -/
theorem braid_at_pair {R : Type*} [CommRing R] (hm : M i j = 3)
    (hred : cs.IsReduced [i, j, i]) (h : R) (v : W → R) :
    mulStep (dihedralTransversal cs i j hm hred).Di h
        (mulStep (dihedralTransversal cs i j hm hred).Dj h
          (mulStep (dihedralTransversal cs i j hm hred).Di h v))
      = mulStep (dihedralTransversal cs i j hm hred).Dj h
          (mulStep (dihedralTransversal cs i j hm hred).Di h
            (mulStep (dihedralTransversal cs i j hm hred).Dj h v)) :=
  DihedralCosetStructure.braid_of_dihedral _ h v

end QOU.Machinery.CoxeterParabolic
