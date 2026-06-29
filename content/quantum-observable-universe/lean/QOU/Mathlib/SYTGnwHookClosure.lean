import QOU.Mathlib.SYTHookGNWWiring

/-!
# QOU.Mathlib.SYTGnwHookClosure — closing `SYTHookGNW.gnwHookIdentity` (WIP scaffold)

`SYTHookGNW.gnwHookIdentity` (`∑_{corners c} prodHooks(l)/prodHooks(l∖c) = sz l`) is the sole
remaining gap of the GNW route to the SYT hook-length formula.  This file collects the **β-Lagrange
side** building blocks for its closure; the full reduction is:

Let `β = betaVec l` (`βᵢ = l[i] + (k−1−i)`, distinct, antitone).  `SYTBetaLagrange.betaLagrange`
already proves, sorry-free,

    ∑_{i : Fin k} βᵢ · ∏_{j≠i}(βᵢ − 1 − βⱼ) / vWeight βᵢ = (∑ⱼ βⱼ) − C(k,2) = sz l   (`sum_betaVec_sub`).

The closure has three steps:

1. **Per-corner ratio = β-Lagrange term** (`per_corner_ratio`, the remaining gap).  For a corner `c`,
   `prodHooks(l)/prodHooks(l∖c) = βc · ∏_{j≠c}(βc − 1 − βj) / vWeight βc`.  Via the proved
   `prodHooks_mul_betaProdGap` (`prodHooks · betaProdGap = betaFactProd`) and the casts
   `betaProdGap_cast` / `betaFactProd_cast`, this reduces to: the factorial side contributes `βc`
   (`betaFactProd(l)/betaFactProd(l∖c) = βc`), and the Vandermonde side contributes the lower-and-upper-
   triangular split product handled by `wall_split` below.  The **row-drop corner** (`l[c]=1`, the last
   row vanishes, `k → k−1`, every `β` shifts by `−1`) needs separate handling — the heavy combinatorial
   `betaVec ∘ removeCorner` step.  *(open: the documented multi-session core.)*

2. **Non-corner terms vanish** (`betaLagrange_term_zero`, proved below).  At a non-corner row `i`
   (`l[i] = l[i+1]`, no strict descent), `βᵢ − 1 = β_{i+1}`, so the `j = i+1` factor of
   `∏_{j≠i}(βᵢ − 1 − βⱼ)` is `0`, killing the whole term.  Hence the β-Lagrange sum over `Fin k` equals
   the sum over corners only.

3. **Assembly**: `∑_{corners} prodHooks-ratio = ∑_{corners} β-Lagrange-term = ∑_{Fin k} β-Lagrange-term
   = sz l` (steps 1 + 2 + `betaLagrange` + `sum_betaVec_sub`).

Proved here so far, sorry-free: step 2 (`betaLagrange_term_zero`), the algebraic core of step 1's
Vandermonde side (`wall_split`), and — for a **middle corner** (`l[c] ≥ 2`, length preserved) — the
structural `betaVec ∘ removeCorner` lemmas plus the **factorial side** of the per-corner ratio
(`betaFactProd_ratio_middle`: `betaFactProd l = βc · betaFactProd(l∖c)`).  Remaining: the middle-corner
`betaProdGap` ratio (the double-product reindexing onto `wall_split`), the **row-drop corner**, and the
corner-sum assembly.  Pure `ℚ`/`ℕ` combinatorics; nothing archimedean; no fit.
-/

namespace QOU.Mathlib.SYTBetaLagrange

open Finset
open QOU.Mathlib.SYTEnum (removeCorner IsCorner)

variable {k : ℕ}

/-- **The Vandermonde-ratio split (algebraic core of step 1).**  The lower-and-upper-triangular factors of
`betaProdGap(l∖c)/betaProdGap(l)` reassemble the β-Lagrange numerator's denominator-paired product:

    (∏_{i<c}(βᵢ − βc + 1)/(βᵢ − βc)) · (∏_{j>c}(βc − 1 − βj)/(βc − βj))
      = ∏_{j≠c}(βc − 1 − βj)/(βc − βj).

The `i < c` factors flip sign per-factor: `(βᵢ − βc + 1)/(βᵢ − βc) = (βc − 1 − βᵢ)/(βc − βᵢ)`
(cross-multiplying, both equal `−(βᵢ − βc)² − (βᵢ − βc)`).  Then `erase c = {<c} ⊔ {>c}` recombines. -/
theorem wall_split (β : Fin k → ℚ) (hβ : Function.Injective β) (c : Fin k) :
    (∏ i ∈ univ.filter (· < c), (β i - β c + 1) / (β i - β c))
      * (∏ j ∈ univ.filter (c < ·), (β c - 1 - β j) / (β c - β j))
      = ∏ j ∈ univ.erase c, (β c - 1 - β j) / (β c - β j) := by
  have hsplit : univ.erase c = univ.filter (· < c) ∪ univ.filter (c < ·) := by
    ext x
    simp only [mem_erase, mem_univ, and_true, true_and, mem_union, mem_filter]
    constructor
    · intro hx; rcases lt_or_gt_of_ne hx with h | h
      · exact Or.inl h
      · exact Or.inr h
    · rintro (h | h)
      · exact ne_of_lt h
      · exact ne_of_gt h
  have hdis : Disjoint (univ.filter (· < c)) (univ.filter (c < ·)) := by
    rw [Finset.disjoint_left]; intro x h1 h2
    rw [mem_filter] at h1 h2; exact absurd (h1.2.trans h2.2) (lt_irrefl x)
  rw [hsplit, Finset.prod_union hdis]
  congr 1
  apply Finset.prod_congr rfl
  intro i hi
  rw [mem_filter] at hi
  have hne : β i ≠ β c := fun e => (ne_of_lt hi.2) (hβ e)
  have h1 : β i - β c ≠ 0 := sub_ne_zero.mpr hne
  have h2 : β c - β i ≠ 0 := sub_ne_zero.mpr (fun e => hne e.symm)
  field_simp
  ring

/-- **Non-corner vanishing (step 2).**  If `βᵢ − 1 = βⱼ` for some `j ≠ i` (the defining feature of a
non-corner row, where `l[i] = l[i+1]` forces `βᵢ − 1 = β_{i+1}`), the β-Lagrange summand at `i` is `0`:
the `j`-th factor of `∏_{j'≠i}(βᵢ − 1 − βⱼ')` vanishes. -/
theorem betaLagrange_term_zero (β : Fin k → ℚ) (i : Fin k)
    (j : Fin k) (hji : j ≠ i) (h : β i - 1 = β j) :
    β i * (∏ j' ∈ univ.erase i, (β i - 1 - β j')) / vWeight β i = 0 := by
  have hz : (∏ j' ∈ univ.erase i, (β i - 1 - β j')) = 0 := by
    apply Finset.prod_eq_zero (i := j)
    · rw [mem_erase]; exact ⟨hji, mem_univ j⟩
    · rw [h]; ring
  rw [hz]; simp

/-! ## Middle-corner `betaVec ∘ removeCorner` structure + factorial side (step 1, middle case)

A **middle corner** is a corner `c` with row length `l[c] ≥ 2`, so `removeCorner l c = l.set c (l[c]−1)`
keeps the row (no `filter` drop) and preserves the length `k`.  Then `betaNat`/`betaNatVal` change at
the single index `c` (by `−1`), and the factorial product picks up exactly `βc`. -/

/-- For a middle corner the length is preserved (the decremented row stays positive). -/
theorem removeCorner_length_middle (l : List ℕ) (c : ℕ)
    (hpos : ∀ a ∈ l, 0 < a) (hmid : 2 ≤ l.getD c 0) :
    (removeCorner l c).length = l.length := by
  unfold removeCorner
  rw [List.filter_eq_self.mpr (by
    intro a ha
    rcases List.mem_or_eq_of_mem_set ha with h | h
    · simpa using (hpos a h).ne'
    · subst h; simpa using Nat.sub_ne_zero_of_lt (by omega : 1 < l.getD c 0)), List.length_set]

/-- `betaNat ∘ removeCorner` at a middle corner: the single index `c` drops by `1`, the rest unchanged. -/
theorem betaNat_removeCorner_middle (l : List ℕ) (c : ℕ)
    (hl : List.Sorted (· ≥ ·) l) (hc : IsCorner l c)
    (hpos : ∀ a ∈ l, 0 < a) (hmid : 2 ≤ l.getD c 0) (j : ℕ) :
    betaNat (removeCorner l c) j = if j = c then betaNat l c - 1 else betaNat l j := by
  unfold betaNat
  rw [removeCorner_length_middle l c hpos hmid,
      QOU.Mathlib.SYTEnum.removeCorner_getD l c hl hc j]
  by_cases hj : j = c
  · subst hj
    rw [if_pos rfl, if_pos rfl]
    have h1 : (1 : ℕ) ≤ l.getD j 0 := by omega
    rw [Nat.cast_sub h1]; push_cast; ring
  · rw [if_neg hj, if_neg hj]

/-- `betaNatVal ∘ removeCorner` (the `ℕ`-valued β-number) at a middle corner. -/
theorem betaNatVal_removeCorner_middle (l : List ℕ) (c : ℕ)
    (hl : List.Sorted (· ≥ ·) l) (hc : IsCorner l c)
    (hpos : ∀ a ∈ l, 0 < a) (hmid : 2 ≤ l.getD c 0) (j : ℕ) :
    betaNatVal (removeCorner l c) j = if j = c then betaNatVal l c - 1 else betaNatVal l j := by
  unfold betaNatVal
  rw [removeCorner_length_middle l c hpos hmid,
      QOU.Mathlib.SYTEnum.removeCorner_getD l c hl hc j]
  by_cases hj : j = c
  · subst hj; rw [if_pos rfl, if_pos rfl]; omega
  · rw [if_neg hj, if_neg hj]

/-- The middle-corner β-number `βc` is positive (`≥ 1`). -/
theorem betaNatVal_c_pos (l : List ℕ) (c : ℕ) (hmid : 2 ≤ l.getD c 0) :
    1 ≤ betaNatVal l c := by unfold betaNatVal; omega

/-- **Factorial side of the per-corner ratio (middle corner).**  `betaFactProd l = βc · betaFactProd(l∖c)`
— deleting a corner cell decrements one β-number by `1`, and `(βc)! = βc · (βc−1)!`. -/
theorem betaFactProd_ratio_middle (l : List ℕ) (c : ℕ)
    (hl : List.Sorted (· ≥ ·) l) (hc : IsCorner l c)
    (hpos : ∀ a ∈ l, 0 < a) (hmid : 2 ≤ l.getD c 0) :
    ((QOU.Mathlib.SYTEnum.betaFactProd l : ℕ) : ℚ)
      = betaNat l c * ((QOU.Mathlib.SYTEnum.betaFactProd (removeCorner l c) : ℕ) : ℚ) := by
  rw [betaFactProd_cast l, betaFactProd_cast (removeCorner l c),
      removeCorner_length_middle l c hpos hmid]
  have hcrange : c ∈ Finset.range l.length := Finset.mem_range.mpr hc.1
  rw [← Finset.mul_prod_erase _ _ hcrange, ← Finset.mul_prod_erase _ _ hcrange]
  have hprod : ∏ i ∈ (Finset.range l.length).erase c, ((betaNatVal (removeCorner l c) i).factorial : ℚ)
      = ∏ i ∈ (Finset.range l.length).erase c, ((betaNatVal l i).factorial : ℚ) := by
    apply Finset.prod_congr rfl
    intro i hi
    rw [Finset.mem_erase] at hi
    rw [betaNatVal_removeCorner_middle l c hl hc hpos hmid i, if_neg hi.1]
  rw [hprod, betaNatVal_removeCorner_middle l c hl hc hpos hmid c, if_pos rfl]
  have hbc : (1 : ℕ) ≤ betaNatVal l c := betaNatVal_c_pos l c hmid
  have hfac : (betaNatVal l c).factorial = betaNatVal l c * (betaNatVal l c - 1).factorial :=
    (Nat.mul_factorial_pred (by omega : betaNatVal l c ≠ 0)).symm
  have hbN : betaNat l c = (betaNatVal l c : ℚ) := by
    unfold betaNat betaNatVal; push_cast; ring
  rw [hbN, hfac]; push_cast; ring

/-! ## `betaProdGap` in standard Fin-k Vandermonde form (foundation for the Vandermonde-side ratio)

`betaProdGap_cast` gives the nested `range`/`betaNat` form `∏_{i<k} ∏_{m<k−1−i}(βᵢ − β_{i+1+m})`.  The
lemma below reindexes the inner range (`m ↦ i+1+m`) onto `Finset.filter (i < ·)`, giving the standard
Vandermonde double product `∏_p ∏_{q>p}(βₚ − β_q)` over `Fin k` with `β = betaVec l` — the form on which
`wall_split` operates for the per-corner Vandermonde-side ratio. -/
theorem betaProdGapFin (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) :
    ((QOU.Mathlib.SYTEnum.betaProdGap l : ℕ) : ℚ)
      = ∏ p : Fin l.length, ∏ q ∈ univ.filter (p < ·), (betaVec l p - betaVec l q) := by
  rw [betaProdGap_cast l hl,
      ← Fin.prod_univ_eq_prod_range
        (fun i => ∏ m ∈ range (l.length - 1 - i), (betaNat l i - betaNat l (i + 1 + m))) l.length]
  apply Finset.prod_congr rfl
  intro p _
  rw [betaVec_eq_betaNat]
  apply Finset.prod_bij (fun m (hm : m ∈ range (l.length - 1 - (p:ℕ))) =>
      (⟨(p : ℕ) + 1 + m, by rw [mem_range] at hm; have := p.2; omega⟩ : Fin l.length))
  · intro m hm
    rw [mem_filter]
    refine ⟨mem_univ _, ?_⟩
    rw [Fin.lt_def]; simp; omega
  · intro a ha b hb hab
    rw [Fin.mk.injEq] at hab; omega
  · intro q hq
    rw [mem_filter, Fin.lt_def] at hq
    refine ⟨(q : ℕ) - (p : ℕ) - 1, ?_, ?_⟩
    · rw [mem_range]; have := q.2; omega
    · rw [Fin.mk.injEq]; omega
  · intro m hm
    rw [betaVec_eq_betaNat]

end QOU.Mathlib.SYTBetaLagrange
