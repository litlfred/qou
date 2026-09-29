/-
# The Tits residue collapsed — cell faithfulness ⟺ simple-distinctness

The transversal bricks (merged #4124, #4291) carried one residual
hypothesis per generator pair: reducedness of the cell word
(`IsReduced [i,j,i]` at `m = 3`, `IsReduced [i,j]` at `m = 2`). This file
collapses that residue to its irreducible core:

    `IsReduced [i, j, i]  ⟺  σᵢ ≠ σⱼ`      (M i j = 3)
    `IsReduced [i, j]    ⟺  σᵢ ≠ σⱼ`      (M i j = 2)

The forward directions were proved with the transversals. The hard
directions are new and use the reflection cocycle (merged #4102)
quantitatively: **distinct reflections with `η = 1` bound the length
from below** (`three_le_length_of_eta` / `two_le_length_of_eta`), because
every such reflection occurs in the inversion sequence of a reduced
word. The inversion sequence of the cell word is computed explicitly —
`[σⱼ, σᵢσⱼσᵢ, σᵢ]` at `m = 3` (the first entry collapsing by the braid
relation), `[σᵢ, σⱼ]` at `m = 2` — and simple-distinctness makes its
entries pairwise distinct, forcing `ℓ ≥` the word length.

Consequently the coset structures need only simple-distinctness:
**`dihedralTransversal'`** / **`commutingTransversal'`** and the payoff
laws **`braid_at_pair'`** / **`far_commute_at_pair'`** take
`σᵢ ≠ σⱼ` in place of the reducedness hypothesis. What remains of Tits
faithfulness, per pair, is exactly the statement that distinct
generators have distinct images — nothing about lengths or words
survives in the residue.

HONESTY (STRICT): sorry-free; `σᵢ ≠ σⱼ` for `i ≠ j` in a GENERAL
Coxeter system is genuinely open here (it is where the geometric
representation is classically used) and remains an explicit hypothesis;
at concrete systems it is decidable through any faithful quotient (cf.
the merged A₃ instantiation). Nothing wired; `1/(8π)` stays phase-4.

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Machinery.CoxeterCommutingTransversal

namespace QOU.Machinery.CoxeterParabolic

open CoxeterSystem List
open QOU.Machinery.HeckeGeneral
open scoped Classical

variable {B W : Type*} [Group W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W)

local prefix:100 "ℓ" => cs.length
local prefix:100 "π" => cs.wordProd
local prefix:100 "σ" => cs.simple

/-! ## Counting: distinct `η = 1` reflections bound the length below -/

/-- Two distinct elements with `η = 1` force `ℓ(w) ≥ 2`: both occur in
the inversion sequence of a reduced word for `w`. -/
lemma two_le_length_of_eta {w t₁ t₂ : W} (h12 : t₁ ≠ t₂)
    (h1 : eta cs w t₁ = 1) (h2 : eta cs w t₂ = 1) : 2 ≤ ℓ w := by
  obtain ⟨ω, hlen, rfl⟩ := cs.exists_reduced_word w
  have m1 := mem_rightInvSeq_of_eta_eq_one cs h1
  have m2 := mem_rightInvSeq_of_eta_eq_one cs h2
  have hsub : ({t₁, t₂} : Finset W) ⊆ (cs.rightInvSeq ω).toFinset := by
    intro t ht
    rw [Finset.mem_insert, Finset.mem_singleton] at ht
    rcases ht with rfl | rfl <;> exact List.mem_toFinset.mpr ‹_›
  have hcard : ({t₁, t₂} : Finset W).card = 2 := by
    rw [Finset.card_insert_of_notMem (by simpa using h12),
      Finset.card_singleton]
  calc 2 = ({t₁, t₂} : Finset W).card := hcard.symm
    _ ≤ (cs.rightInvSeq ω).toFinset.card := Finset.card_le_card hsub
    _ ≤ (cs.rightInvSeq ω).length := List.toFinset_card_le _
    _ = ω.length := cs.length_rightInvSeq ω
    _ = ℓ (π ω) := hlen

/-- Three pairwise-distinct elements with `η = 1` force `ℓ(w) ≥ 3`. -/
lemma three_le_length_of_eta {w t₁ t₂ t₃ : W} (h12 : t₁ ≠ t₂)
    (h13 : t₁ ≠ t₃) (h23 : t₂ ≠ t₃) (h1 : eta cs w t₁ = 1)
    (h2 : eta cs w t₂ = 1) (h3 : eta cs w t₃ = 1) : 3 ≤ ℓ w := by
  obtain ⟨ω, hlen, rfl⟩ := cs.exists_reduced_word w
  have m1 := mem_rightInvSeq_of_eta_eq_one cs h1
  have m2 := mem_rightInvSeq_of_eta_eq_one cs h2
  have m3 := mem_rightInvSeq_of_eta_eq_one cs h3
  have hsub : ({t₁, t₂, t₃} : Finset W) ⊆ (cs.rightInvSeq ω).toFinset := by
    intro t ht
    rw [Finset.mem_insert, Finset.mem_insert, Finset.mem_singleton] at ht
    rcases ht with rfl | rfl | rfl <;> exact List.mem_toFinset.mpr ‹_›
  have hcard : ({t₁, t₂, t₃} : Finset W).card = 3 := by
    rw [Finset.card_insert_of_notMem (by simp [h12, h13]),
      Finset.card_insert_of_notMem (by simpa using h23),
      Finset.card_singleton]
  calc 3 = ({t₁, t₂, t₃} : Finset W).card := hcard.symm
    _ ≤ (cs.rightInvSeq ω).toFinset.card := Finset.card_le_card hsub
    _ ≤ (cs.rightInvSeq ω).length := List.toFinset_card_le _
    _ = ω.length := cs.length_rightInvSeq ω
    _ = ℓ (π ω) := hlen

/-! ## The `m = 3` collapse -/

variable (i j : B)

/-- **Cell faithfulness from simple-distinctness at `m = 3`**: if
`σᵢ ≠ σⱼ` then `[i, j, i]` is reduced — the inversion sequence
`[σⱼ, σᵢσⱼσᵢ, σᵢ]` has pairwise-distinct entries, so the length is at
least 3. -/
theorem isReduced_iji_of_simple_ne (hm : M i j = 3) (hne : σ i ≠ σ j) :
    cs.IsReduced [i, j, i] := by
  have hb := braid3 cs i j hm
  have hssi := cs.simple_mul_simple_self i
  have hssj := cs.simple_mul_simple_self j
  -- the three inversion-sequence entries are pairwise distinct
  have h13 : σ i ≠ σ i * σ j * σ i := by
    intro h
    apply hne
    calc σ i = σ i * (σ i * σ j * σ i) * σ i := by rw [← h, hssi, one_mul]
      _ = (σ i * σ i) * σ j * (σ i * σ i) := by group
      _ = σ j := by rw [hssi, one_mul, mul_one]
  have h23 : σ i * σ j * σ i ≠ σ j := by
    intro h
    apply hne
    have hjj : σ j * (σ i * σ j) = σ j * 1 := by
      rw [mul_one]
      calc σ j * (σ i * σ j) = σ j * σ i * σ j := by rw [mul_assoc]
        _ = σ i * σ j * σ i := hb.symm
        _ = σ j := h
    have hij1 : σ i * σ j = 1 := mul_left_cancel hjj
    calc σ i = σ i * (σ j * σ j) := by rw [hssj, mul_one]
      _ = (σ i * σ j) * σ j := by rw [mul_assoc]
      _ = σ j := by rw [hij1, one_mul]
  -- the inversion sequence of the cell word
  have hris : cs.rightInvSeq [i, j, i] = [σ j, σ i * σ j * σ i, σ i] := by
    have e0 : (π [j, i])⁻¹ * σ i * π [j, i] = σ j := by
      have hpji : π [j, i] = σ j * σ i := by
        simp [wordProd_cons, wordProd_nil]
      rw [hpji, mul_inv_rev, cs.inv_simple, cs.inv_simple]
      calc σ i * σ j * σ i * (σ j * σ i)
          = (σ i * σ j * σ i) * σ j * σ i := by group
        _ = (σ j * σ i * σ j) * σ j * σ i := by rw [hb]
        _ = σ j * σ i * (σ j * σ j) * σ i := by group
        _ = σ j * (σ i * σ i) := by rw [hssj]; group
        _ = σ j := by rw [hssi, mul_one]
    have e1 : (π [i])⁻¹ * σ j * π [i] = σ i * σ j * σ i := by
      have hpi : π [i] = σ i := by simp [wordProd_cons, wordProd_nil]
      rw [hpi, cs.inv_simple]
    simp only [rightInvSeq, wordProd_nil, inv_one, one_mul, mul_one]
    rw [show ((π [j, i])⁻¹ * σ i * π [j, i] : W) = σ j from e0,
      show ((π [i])⁻¹ * σ j * π [i] : W) = σ i * σ j * σ i from e1]
  -- the three entries have η = 1
  have hcount : ∀ t ∈ [σ j, σ i * σ j * σ i, σ i],
      eta cs (π [i, j, i]) t = 1 := by
    intro t ht
    rw [eta_wordProd, hris]
    fin_cases ht
    · rw [parityCount_cons, parityCount_cons, parityCount_cons,
        parityCount_nil, if_pos rfl, if_neg h23, if_neg hne]
      decide
    · rw [parityCount_cons, parityCount_cons, parityCount_cons,
        parityCount_nil, if_neg (Ne.symm h23), if_pos rfl, if_neg h13]
      decide
    · rw [parityCount_cons, parityCount_cons, parityCount_cons,
        parityCount_nil, if_neg (Ne.symm hne), if_neg (Ne.symm h13),
        if_pos rfl]
      decide
  have hlow : 3 ≤ ℓ (π [i, j, i]) := by
    refine three_le_length_of_eta cs (t₁ := σ j) (t₂ := σ i * σ j * σ i)
      (t₃ := σ i) (Ne.symm h23) (Ne.symm hne) h13.symm ?_ ?_ ?_ <;>
      exact hcount _ (by simp)
  have hupper : ℓ (π [i, j, i]) ≤ 3 := by
    simpa using cs.length_wordProd_le [i, j, i]
  show ℓ (π [i, j, i]) = [i, j, i].length
  simp only [List.length_cons, List.length_nil]
  omega

/-- **The `m = 3` residue, collapsed**: cell faithfulness is exactly
simple-distinctness. -/
theorem isReduced_iji_iff (hm : M i j = 3) :
    cs.IsReduced [i, j, i] ↔ σ i ≠ σ j :=
  ⟨simple_ne_of_reduced cs i j, isReduced_iji_of_simple_ne cs i j hm⟩

/-! ## The `m = 2` collapse -/

/-- **Cell faithfulness from simple-distinctness at `m = 2`**: the
inversion sequence of `[i, j]` is `[σᵢ, σⱼ]`. -/
theorem isReduced_ij_of_simple_ne (hm : M i j = 2) (hne : σ i ≠ σ j) :
    cs.IsReduced [i, j] := by
  have hc := commute2 cs i j hm
  have hssj := cs.simple_mul_simple_self j
  have hris : cs.rightInvSeq [i, j] = [σ i, σ j] := by
    have e0 : (π [j])⁻¹ * σ i * π [j] = σ i := by
      have hpj : π [j] = σ j := by simp [wordProd_cons, wordProd_nil]
      rw [hpj, cs.inv_simple]
      calc σ j * σ i * σ j = σ i * σ j * σ j := by rw [← hc]
        _ = σ i * (σ j * σ j) := by rw [mul_assoc]
        _ = σ i := by rw [hssj, mul_one]
    simp only [rightInvSeq, wordProd_nil, inv_one, one_mul, mul_one]
    rw [show ((π [j])⁻¹ * σ i * π [j] : W) = σ i from e0]
  have hcount : ∀ t ∈ [σ i, σ j], eta cs (π [i, j]) t = 1 := by
    intro t ht
    rw [eta_wordProd, hris]
    fin_cases ht
    · rw [parityCount_cons, parityCount_cons, parityCount_nil,
        if_pos rfl, if_neg (Ne.symm hne)]
      decide
    · rw [parityCount_cons, parityCount_cons, parityCount_nil,
        if_neg hne, if_pos rfl]
      decide
  have hlow : 2 ≤ ℓ (π [i, j]) := by
    refine two_le_length_of_eta cs (t₁ := σ i) (t₂ := σ j) hne ?_ ?_ <;>
      exact hcount _ (by simp)
  have hupper : ℓ (π [i, j]) ≤ 2 := by
    simpa using cs.length_wordProd_le [i, j]
  show ℓ (π [i, j]) = [i, j].length
  simp only [List.length_cons, List.length_nil]
  omega

/-- **The `m = 2` residue, collapsed.** -/
theorem isReduced_ij_iff (hm : M i j = 2) :
    cs.IsReduced [i, j] ↔ σ i ≠ σ j :=
  ⟨simple_ne_of_reduced2 cs i j, isReduced_ij_of_simple_ne cs i j hm⟩

/-! ## The transversals and presentation laws, from simple-distinctness -/

/-- The dihedral coset structure from `σᵢ ≠ σⱼ` alone. -/
noncomputable def dihedralTransversal' (hm : M i j = 3) (hne : σ i ≠ σ j) :
    DihedralCosetStructure W :=
  dihedralTransversal cs i j hm (isReduced_iji_of_simple_ne cs i j hm hne)

/-- The commuting coset structure from `σᵢ ≠ σⱼ` alone. -/
noncomputable def commutingTransversal' (hm : M i j = 2) (hne : σ i ≠ σ j) :
    CommutingCosetStructure W :=
  commutingTransversal cs i j hm (isReduced_ij_of_simple_ne cs i j hm hne)

variable {R : Type*} [CommRing R]

/-- **Braid at every rank from simple-distinctness.** -/
theorem braid_at_pair' (hm : M i j = 3) (hne : σ i ≠ σ j) (h : R)
    (v : W → R) :
    mulStep (dihedralTransversal' cs i j hm hne).Di h
        (mulStep (dihedralTransversal' cs i j hm hne).Dj h
          (mulStep (dihedralTransversal' cs i j hm hne).Di h v))
      = mulStep (dihedralTransversal' cs i j hm hne).Dj h
          (mulStep (dihedralTransversal' cs i j hm hne).Di h
            (mulStep (dihedralTransversal' cs i j hm hne).Dj h v)) :=
  DihedralCosetStructure.braid_of_dihedral _ h v

/-- **Far commutation at every rank from simple-distinctness.** -/
theorem far_commute_at_pair' (hm : M i j = 2) (hne : σ i ≠ σ j) (h : R)
    (v : W → R) :
    mulStep (commutingTransversal' cs i j hm hne).Di h
        (mulStep (commutingTransversal' cs i j hm hne).Dj h v)
      = mulStep (commutingTransversal' cs i j hm hne).Dj h
          (mulStep (commutingTransversal' cs i j hm hne).Di h v) :=
  CommutingCosetStructure.far_commute_of_commuting _ h v

end QOU.Machinery.CoxeterParabolic
