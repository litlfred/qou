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
open QOU.Mathlib.SYTEnum (removeCorner IsCorner betaProdGap betaFactProd sorted_removeCorner
  prodHooks_mul_betaProdGap betaProdGap_pos prodHooks_pos removeCorner_pos)
open QOU.BraidKnot.IdentityI (prodHooks)

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

/-- **Generic Vandermonde double-product split at pivot column `c`.**  The full product
`∏_p ∏_{q>p} f p q` factors as `[c-row: ∏_{q>c} f c q] · [c-col: ∏_{p<c} f p c] · [rest: pairs
touching neither `c`]`.  This is the structural identity behind the per-corner Vandermonde-side ratio:
applied to `f p q = γ p − γ q` for `γ` and for the `c`-updated `γ'`, the `rest` factors cancel and the
`c`-row/`c`-col factors give the `wall_split` numerator/denominator. -/
theorem splitVand (f : Fin k → Fin k → ℚ) (c : Fin k) :
    (∏ p : Fin k, ∏ q ∈ univ.filter (p < ·), f p q)
      = (∏ q ∈ univ.filter (c < ·), f c q)
        * (∏ p ∈ univ.filter (· < c), f p c)
        * (∏ p ∈ univ.erase c, ∏ q ∈ (univ.filter (p < ·)).erase c, f p q) := by
  rw [← Finset.mul_prod_erase univ (fun p => ∏ q ∈ univ.filter (p < ·), f p q) (mem_univ c)]
  rw [mul_assoc]
  congr 1
  have hper : ∀ p ∈ univ.erase c, (∏ q ∈ univ.filter (p < ·), f p q)
      = (if p < c then f p c else 1) * (∏ q ∈ (univ.filter (p < ·)).erase c, f p q) := by
    intro p _
    by_cases hpc : p < c
    · rw [if_pos hpc]
      have hcmem : c ∈ univ.filter (p < ·) := by rw [mem_filter]; exact ⟨mem_univ _, hpc⟩
      rw [← Finset.mul_prod_erase _ _ hcmem]
    · rw [if_neg hpc]
      have hcnmem : c ∉ univ.filter (p < ·) := by
        rw [mem_filter]; push_neg; intro _; exact le_of_not_lt hpc
      rw [Finset.erase_eq_of_notMem hcnmem, one_mul]
  rw [Finset.prod_congr rfl hper, Finset.prod_mul_distrib]
  congr 1
  rw [← Finset.prod_filter]
  congr 1
  ext p
  simp only [mem_filter, mem_erase, mem_univ, and_true, true_and]
  constructor
  · rintro ⟨_, hpc⟩; exact hpc
  · intro hpc; exact ⟨ne_of_lt hpc, hpc⟩

/-- **`betaProdGap(l∖c)` as a Vandermonde product over `Fin l.length` (middle corner).**  Transports
`betaProdGapFin (removeCorner l c)` (over `Fin (l∖c).length`) along the length equality onto
`Fin l.length`, with nodes `β' = betaVec l` updated at `c` by `−1` (`Function.update`).  This puts
`betaProdGap(l∖c)` in the same index world as `betaProdGap l`, so `splitVand` applies to both. -/
theorem betaProdGap_removeCorner_middle_Fin (l : List ℕ) (c : ℕ)
    (hl : List.Sorted (· ≥ ·) l) (hc : IsCorner l c)
    (hpos : ∀ a ∈ l, 0 < a) (hmid : 2 ≤ l.getD c 0) :
    ((betaProdGap (removeCorner l c) : ℕ) : ℚ)
      = ∏ p : Fin l.length, ∏ q ∈ univ.filter (p < ·),
          (Function.update (betaVec l) ⟨c, hc.1⟩ (betaVec l ⟨c, hc.1⟩ - 1) p
            - Function.update (betaVec l) ⟨c, hc.1⟩ (betaVec l ⟨c, hc.1⟩ - 1) q) := by
  have hlen : (removeCorner l c).length = l.length := removeCorner_length_middle l c hpos hmid
  set β' := Function.update (betaVec l) (⟨c, hc.1⟩ : Fin l.length) (betaVec l ⟨c, hc.1⟩ - 1) with hβ'
  have hpt : ∀ (j : ℕ) (hj : j < (removeCorner l c).length) (hj' : j < l.length),
      betaVec (removeCorner l c) ⟨j, hj⟩ = β' ⟨j, hj'⟩ := by
    intro j hj hj'
    rw [betaVec_eq_betaNat, betaNat_removeCorner_middle l c hl hc hpos hmid j, hβ',
        Function.update_apply]
    by_cases hjc : j = c
    · subst hjc
      rw [if_pos rfl, if_pos (by rw [Fin.ext_iff]), betaVec_eq_betaNat]
    · rw [if_neg hjc, if_neg (by rw [Fin.ext_iff]; exact hjc), betaVec_eq_betaNat]
  rw [betaProdGapFin (removeCorner l c) (sorted_removeCorner l c hl hc)]
  apply Finset.prod_nbij' (fun p => Fin.cast hlen p) (fun p => Fin.cast hlen.symm p)
  · intro p _; exact mem_univ _
  · intro p _; exact mem_univ _
  · intro p _; apply Fin.ext; simp
  · intro p _; apply Fin.ext; simp
  · intro p _
    apply Finset.prod_nbij' (fun q => Fin.cast hlen q) (fun q => Fin.cast hlen.symm q)
    · intro q hq; rw [mem_filter] at hq ⊢; refine ⟨mem_univ _, ?_⟩
      rw [Fin.lt_def] at hq ⊢; simpa using hq.2
    · intro q hq; rw [mem_filter] at hq ⊢; refine ⟨mem_univ _, ?_⟩
      rw [Fin.lt_def] at hq ⊢; simpa using hq.2
    · intro q _; apply Fin.ext; simp
    · intro q _; apply Fin.ext; simp
    · intro q _
      rw [hpt p.val p.2 (by rw [← hlen]; exact p.2), hpt q.val q.2 (by rw [← hlen]; exact q.2)]
      congr 1 <;> (apply Fin.ext; simp)

/-- **Vandermonde-side of the per-corner ratio (middle corner), cross-multiplied.**

    betaProdGap(l∖c) · ∏_{j≠c}(βc − βj)  =  betaProdGap(l) · ∏_{j≠c}(βc − 1 − βj).

Both `betaProdGap`s are put in Fin-`k` Vandermonde form (`betaProdGapFin`,
`betaProdGap_removeCorner_middle_Fin`) and split with `splitVand` at the pivot `cF = ⟨c,_⟩`.  The
`rest` factors (pairs avoiding `cF`) are equal since `β' = betaVec l` only changed at `cF`; the
`c`-row/`c`-col factors of `β'` are `βc−1−βq` / `βp−βc+1`, and `wall_split` (cleared of denominators)
recombines them into the `∏_{j≠c}` factors — exactly this cross-multiplied identity. -/
theorem vand_ratio_middle (l : List ℕ) (c : ℕ)
    (hl : List.Sorted (· ≥ ·) l) (hc : IsCorner l c)
    (hpos : ∀ a ∈ l, 0 < a) (hmid : 2 ≤ l.getD c 0) :
    ((betaProdGap (removeCorner l c) : ℕ) : ℚ)
        * (∏ j ∈ univ.erase (⟨c, hc.1⟩ : Fin l.length), (betaVec l ⟨c, hc.1⟩ - betaVec l j))
      = ((betaProdGap l : ℕ) : ℚ)
        * (∏ j ∈ univ.erase (⟨c, hc.1⟩ : Fin l.length), (betaVec l ⟨c, hc.1⟩ - 1 - betaVec l j)) := by
  set cF : Fin l.length := ⟨c, hc.1⟩ with hcF
  set β := betaVec l with hβdef
  set β' := Function.update β cF (β cF - 1) with hβ'
  have hinj : Function.Injective β := betaVec_injective l hl
  rw [betaProdGapFin l hl, betaProdGap_removeCorner_middle_Fin l c hl hc hpos hmid,
      splitVand (fun p q => β' p - β' q) cF, splitVand (fun p q => β p - β q) cF]
  have hR : (∏ p ∈ univ.erase cF, ∏ q ∈ (univ.filter (p < ·)).erase cF, (β' p - β' q))
      = ∏ p ∈ univ.erase cF, ∏ q ∈ (univ.filter (p < ·)).erase cF, (β p - β q) := by
    apply Finset.prod_congr rfl; intro p hp
    apply Finset.prod_congr rfl; intro q hq
    rw [mem_erase] at hp; rw [mem_erase] at hq
    rw [hβ', Function.update_of_ne hp.1, Function.update_of_ne hq.1]
  have hcrow : (∏ q ∈ univ.filter (cF < ·), (β' cF - β' q))
      = ∏ q ∈ univ.filter (cF < ·), (β cF - 1 - β q) := by
    apply Finset.prod_congr rfl; intro q hq
    rw [mem_filter] at hq
    rw [hβ', Function.update_self, Function.update_of_ne (ne_of_gt hq.2)]
  have hccol : (∏ p ∈ univ.filter (· < cF), (β' p - β' cF))
      = ∏ p ∈ univ.filter (· < cF), (β p - β cF + 1) := by
    apply Finset.prod_congr rfl; intro p hp
    rw [mem_filter] at hp
    rw [hβ', Function.update_self, Function.update_of_ne (ne_of_lt hp.2)]; ring
  rw [hR, hcrow, hccol]
  have hws := wall_split β hinj cF
  have hd1 : ∀ p ∈ univ.filter (· < cF), β p - β cF ≠ 0 := by
    intro p hp; rw [mem_filter] at hp; exact sub_ne_zero.mpr (fun e => (ne_of_lt hp.2) (hinj e))
  have hd2 : ∀ q ∈ univ.filter (cF < ·), β cF - β q ≠ 0 := by
    intro q hq; rw [mem_filter] at hq; exact sub_ne_zero.mpr (fun e => (ne_of_gt hq.2) (hinj e.symm))
  have hd3 : ∀ j ∈ univ.erase cF, β cF - β j ≠ 0 := by
    intro j hj; rw [mem_erase] at hj; exact sub_ne_zero.mpr (fun e => hj.1 (hinj e).symm)
  rw [Finset.prod_div_distrib, Finset.prod_div_distrib, Finset.prod_div_distrib] at hws
  have hP1 : (∏ p ∈ univ.filter (· < cF), (β p - β cF)) ≠ 0 := Finset.prod_ne_zero_iff.mpr hd1
  have hP2 : (∏ q ∈ univ.filter (cF < ·), (β cF - β q)) ≠ 0 := Finset.prod_ne_zero_iff.mpr hd2
  have hP3 : (∏ j ∈ univ.erase cF, (β cF - β j)) ≠ 0 := Finset.prod_ne_zero_iff.mpr hd3
  field_simp [hP1, hP2, hP3] at hws
  linear_combination (∏ p ∈ univ.erase cF, ∏ q ∈ (univ.filter (p < ·)).erase cF, (β p - β q)) * hws

/-- **The per-corner hook ratio = β-Lagrange term (middle corner).**

    prodHooks(l) / prodHooks(l∖c)  =  βc · ∏_{j≠c}(βc − 1 − βj) / vWeight β c,

i.e. exactly the `c`-th summand of `betaLagrange`.  Combines the factorial side
(`betaFactProd_ratio_middle`, contributing `βc`) and the Vandermonde side (`vand_ratio_middle`),
linked through `prodHooks · betaProdGap = betaFactProd` (`prodHooks_mul_betaProdGap`) for both `l` and
`l∖c`.  The algebra clears denominators (`betaProdGap l ≠ 0`) and closes by a single
`linear_combination` of the four multiplicative facts. -/
theorem per_corner_ratio_middle (l : List ℕ) (c : ℕ)
    (hl : List.Sorted (· ≥ ·) l) (hc : IsCorner l c)
    (hpos : ∀ a ∈ l, 0 < a) (hmid : 2 ≤ l.getD c 0) :
    (prodHooks l : ℚ) / (prodHooks (removeCorner l c) : ℚ)
      = betaVec l ⟨c, hc.1⟩
          * (∏ j ∈ univ.erase (⟨c, hc.1⟩ : Fin l.length), (betaVec l ⟨c, hc.1⟩ - 1 - betaVec l j))
          / vWeight (betaVec l) ⟨c, hc.1⟩ := by
  set cF : Fin l.length := ⟨c, hc.1⟩ with hcF
  set β := betaVec l with hβdef
  have hlc_sorted := sorted_removeCorner l c hl hc
  have hinj : Function.Injective β := betaVec_injective l hl
  have h1q : (prodHooks l : ℚ) * (betaProdGap l : ℚ) = (betaFactProd l : ℚ) := by
    exact_mod_cast prodHooks_mul_betaProdGap l hl
  have h2q : (prodHooks (removeCorner l c) : ℚ) * (betaProdGap (removeCorner l c) : ℚ)
      = (betaFactProd (removeCorner l c) : ℚ) := by
    exact_mod_cast prodHooks_mul_betaProdGap (removeCorner l c) hlc_sorted
  have hfac := betaFactProd_ratio_middle l c hl hc hpos hmid
  have hvand := vand_ratio_middle l c hl hc hpos hmid
  rw [← hβdef, ← hcF] at hvand
  have hphc : (prodHooks (removeCorner l c) : ℚ) ≠ 0 := by
    have := prodHooks_pos (removeCorner l c) hlc_sorted (removeCorner_pos l c); positivity
  have hbpl : (betaProdGap l : ℚ) ≠ 0 := by have := betaProdGap_pos l hl; positivity
  have hvw : vWeight β cF ≠ 0 := vWeight_ne_zero β hinj cF
  have hvwdef : vWeight β cF = ∏ j ∈ univ.erase cF, (β cF - β j) := rfl
  have hbeta : betaNat l c = β cF := by rw [hβdef, hcF, betaVec_eq_betaNat]
  rw [hbeta] at hfac
  rw [div_eq_div_iff hphc hvw, hvwdef]
  refine mul_right_cancel₀ hbpl ?_
  linear_combination (∏ j ∈ univ.erase cF, (β cF - β j)) * h1q
    + (∏ j ∈ univ.erase cF, (β cF - β j)) * hfac
    - (β cF) * (∏ j ∈ univ.erase cF, (β cF - β j)) * h2q
    + (β cF) * (prodHooks (removeCorner l c) : ℚ) * hvand

/-! ## Row-drop corner structure (the `l[c] = 1` case)

A **row-drop corner** is a corner `c` with row length `l[c] = 1`.  Because the shape is sorted-positive,
this forces `c = k − 1` (the last row): `l[c+1] < l[c] = 1` means `l[c+1] = 0`, impossible for a row
strictly inside a positive shape.  Deleting it removes the whole last row, so `removeCorner l c = take c`
and the length drops `k → k − 1`.  The staircase shift `(length − 1 − j)` then drops by one for every
`j`, so `betaNat`/`betaNatVal` **shift uniformly by `−1`** (all nodes, not just `c`) — the structurally
different feature from the middle corner. -/

/-- A row-drop corner is the last row. -/
theorem rowdrop_c_last (l : List ℕ) (c : ℕ) (hc : IsCorner l c)
    (hpos : ∀ a ∈ l, 0 < a) (hone : l.getD c 0 = 1) : c = l.length - 1 := by
  have hclt : c < l.length := hc.1
  have hnext : l.getD (c+1) 0 < l.getD c 0 := hc.2
  rw [hone] at hnext
  by_contra hne
  have hc1 : c + 1 < l.length := by omega
  have : 0 < l.getD (c+1) 0 := by
    rw [QOU.Mathlib.SYTEnum.getD_eq_getElem' l (c+1) hc1]
    exact hpos _ (List.getElem_mem hc1)
  omega

/-- Deleting a row-drop corner truncates the last row: `removeCorner l c = l.take c`. -/
theorem removeCorner_eq_take_rowdrop (l : List ℕ) (c : ℕ) (hc : IsCorner l c)
    (hpos : ∀ a ∈ l, 0 < a) (hone : l.getD c 0 = 1) :
    removeCorner l c = l.take c := by
  have hclt : c < l.length := hc.1
  have hclast : c = l.length - 1 := rowdrop_c_last l c hc hpos hone
  have hdrop : l.drop (c+1) = [] := List.drop_eq_nil_of_le (by omega)
  unfold removeCorner
  rw [hone, List.set_eq_take_append_cons_drop, if_pos hclt, hdrop, List.filter_append]
  have htake : (l.take c).filter (· != 0) = l.take c := by
    rw [List.filter_eq_self]; intro a ha
    simpa using (hpos a (List.mem_of_mem_take ha)).ne'
  rw [htake]; simp

/-- The length drops by one for a row-drop corner. -/
theorem removeCorner_length_rowdrop (l : List ℕ) (c : ℕ) (hc : IsCorner l c)
    (hpos : ∀ a ∈ l, 0 < a) (hone : l.getD c 0 = 1) :
    (removeCorner l c).length = l.length - 1 := by
  rw [removeCorner_eq_take_rowdrop l c hc hpos hone, List.length_take]
  have := rowdrop_c_last l c hc hpos hone
  omega

/-- **Uniform β-number shift (row-drop, `ℕ`).**  `betaNatVal(l∖c) j = betaNatVal l j − 1` for every
`j < c`: deleting the last row drops the staircase shift `(length − 1 − j)` by one. -/
theorem betaNatVal_removeCorner_rowdrop (l : List ℕ) (c : ℕ) (hc : IsCorner l c)
    (hpos : ∀ a ∈ l, 0 < a) (hone : l.getD c 0 = 1) (j : ℕ) (hj : j < c) :
    betaNatVal (removeCorner l c) j = betaNatVal l j - 1 := by
  have hlen := removeCorner_length_rowdrop l c hc hpos hone
  have htake := removeCorner_eq_take_rowdrop l c hc hpos hone
  have hclast := rowdrop_c_last l c hc hpos hone
  unfold betaNatVal
  rw [hlen, htake]
  have hgd : (l.take c).getD j 0 = l.getD j 0 := by
    rw [QOU.Mathlib.SYTEnum.getD_eq_getElem' (l.take c) j (by rw [List.length_take]; omega),
        QOU.Mathlib.SYTEnum.getD_eq_getElem' l j (by omega), List.getElem_take]
  rw [hgd]; omega

/-- **Uniform β-number shift (row-drop, `ℚ`).**  `betaNat(l∖c) j = betaNat l j − 1` for `j < c`. -/
theorem betaNat_removeCorner_rowdrop (l : List ℕ) (c : ℕ) (hc : IsCorner l c)
    (hpos : ∀ a ∈ l, 0 < a) (hone : l.getD c 0 = 1) (j : ℕ) (hj : j < c) :
    betaNat (removeCorner l c) j = betaNat l j - 1 := by
  have hlen := removeCorner_length_rowdrop l c hc hpos hone
  have htake := removeCorner_eq_take_rowdrop l c hc hpos hone
  have hclast := rowdrop_c_last l c hc hpos hone
  unfold betaNat
  rw [hlen, htake]
  have hgd : (l.take c).getD j 0 = l.getD j 0 := by
    rw [QOU.Mathlib.SYTEnum.getD_eq_getElem' (l.take c) j (by rw [List.length_take]; omega),
        QOU.Mathlib.SYTEnum.getD_eq_getElem' l j (by omega), List.getElem_take]
  rw [hgd]
  have h1 : ((l.length - 1 - 1 - j : ℕ) : ℚ) = ((l.length - 1 - j : ℕ) : ℚ) - 1 := by
    have he : l.length - 1 - 1 - j = (l.length - 1 - j) - 1 := by omega
    rw [he, Nat.cast_sub (by omega : 1 ≤ l.length - 1 - j), Nat.cast_one]
  rw [h1]; push_cast; ring


/-! ## Row-drop per-corner ratios (factorial side `∏_{j<c} βⱼ` and Vandermonde side) -/

theorem betaNatVal_c_rowdrop (l : List ℕ) (c : ℕ) (hc : IsCorner l c)
    (hpos : ∀ a ∈ l, 0 < a) (hone : l.getD c 0 = 1) : betaNatVal l c = 1 := by
  have hclast := rowdrop_c_last l c hc hpos hone
  unfold betaNatVal; omega

theorem length_eq_succ_rowdrop (l : List ℕ) (c : ℕ) (hc : IsCorner l c)
    (hpos : ∀ a ∈ l, 0 < a) (hone : l.getD c 0 = 1) : l.length = c + 1 := by
  have hclast := rowdrop_c_last l c hc hpos hone
  have := hc.1; omega

theorem betaFactProd_ratio_rowdrop (l : List ℕ) (c : ℕ) (hc : IsCorner l c)
    (hpos : ∀ a ∈ l, 0 < a) (hone : l.getD c 0 = 1) :
    ((betaFactProd l : ℕ) : ℚ)
      = (∏ i ∈ range c, (betaNatVal l i : ℚ)) * ((betaFactProd (removeCorner l c) : ℕ) : ℚ) := by
  have hlen := length_eq_succ_rowdrop l c hc hpos hone
  have hlenrc_c : (removeCorner l c).length = c := by
    rw [removeCorner_length_rowdrop l c hc hpos hone, hlen]; omega
  rw [betaFactProd_cast l, betaFactProd_cast (removeCorner l c), hlen, hlenrc_c]
  rw [Finset.prod_range_succ, betaNatVal_c_rowdrop l c hc hpos hone]
  simp only [Nat.factorial_one, Nat.cast_one, mul_one]
  rw [← Finset.prod_mul_distrib]
  apply Finset.prod_congr rfl
  intro i hi
  rw [mem_range] at hi
  rw [betaNatVal_removeCorner_rowdrop l c hc hpos hone i hi]
  -- (betaNatVal l i)! = betaNatVal l i * (betaNatVal l i - 1)!
  have hbi : 1 ≤ betaNatVal l i := by unfold betaNatVal; omega
  rw [← Nat.cast_mul, Nat.mul_factorial_pred (by omega)]

theorem betaProdGap_ratio_rowdrop (l : List ℕ) (c : ℕ) (hl : List.Sorted (· ≥ ·) l)
    (hc : IsCorner l c) (hpos : ∀ a ∈ l, 0 < a) (hone : l.getD c 0 = 1) :
    ((betaProdGap l : ℕ) : ℚ)
      = (∏ i ∈ range c, (betaNat l i - betaNat l c))
        * ((betaProdGap (removeCorner l c) : ℕ) : ℚ) := by
  have hlen := length_eq_succ_rowdrop l c hc hpos hone
  have hlenrc_c : (removeCorner l c).length = c := by
    rw [removeCorner_length_rowdrop l c hc hpos hone, hlen]; omega
  rw [betaProdGap_cast l hl, betaProdGap_cast (removeCorner l c) (sorted_removeCorner l c hl hc),
      hlen, hlenrc_c]
  simp only [Nat.add_sub_cancel]
  rw [Finset.prod_range_succ, Nat.sub_self, Finset.range_zero,
      Finset.prod_empty, mul_one, ← Finset.prod_mul_distrib]
  apply Finset.prod_congr rfl
  intro i hi
  rw [mem_range] at hi
  rw [show c - i = (c - 1 - i) + 1 from by omega, Finset.prod_range_succ,
      show i + 1 + (c - 1 - i) = c from by omega, mul_comm]
  congr 1
  apply Finset.prod_congr rfl
  intro m hm
  rw [mem_range] at hm
  rw [betaNat_removeCorner_rowdrop l c hc hpos hone i (by omega),
      betaNat_removeCorner_rowdrop l c hc hpos hone (i + 1 + m) (by omega)]
  ring


/-! ## Row-drop per-corner ratio = β-Lagrange term (matching the middle-corner form) -/

-- reindex: products over univ.erase (last node) ↔ products over range c
theorem prod_erase_last_eq_range (l : List ℕ) (c : ℕ) (hc : IsCorner l c)
    (hpos : ∀ a ∈ l, 0 < a) (hone : l.getD c 0 = 1) (f : ℚ → ℚ) :
    ∏ j ∈ univ.erase (⟨c, hc.1⟩ : Fin l.length), f (betaVec l j)
      = ∏ i ∈ range c, f (betaNat l i) := by
  have hlen := length_eq_succ_rowdrop l c hc hpos hone
  apply Finset.prod_nbij (fun (j : Fin l.length) => (j : ℕ))
  · intro j hj
    rw [mem_erase] at hj
    rw [mem_range]
    have hjl : (j : ℕ) < l.length := j.2
    have : (j : ℕ) ≠ c := fun e => hj.1 (Fin.ext e)
    omega
  · intro a _ b _ hab; exact Fin.ext hab
  · intro i hi
    simp only [Finset.coe_range, Set.mem_Iio] at hi
    refine ⟨⟨i, by omega⟩, ?_, rfl⟩
    simp only [Finset.mem_coe, mem_erase]
    exact ⟨Fin.ne_of_val_ne (Nat.ne_of_lt hi), mem_univ _⟩
  · intro j _
    rw [betaVec_eq_betaNat]

theorem betaNat_c_rowdrop_one (l : List ℕ) (c : ℕ) (hc : IsCorner l c)
    (hpos : ∀ a ∈ l, 0 < a) (hone : l.getD c 0 = 1) : betaNat l c = 1 := by
  have hclast := rowdrop_c_last l c hc hpos hone
  unfold betaNat
  have : l.length - 1 - c = 0 := by omega
  rw [this, hone]; norm_num

-- ∏ (-(f i)) = (-1)^c · ∏ f i  over range c
theorem prod_neg_range (c : ℕ) (f : ℕ → ℚ) :
    ∏ i ∈ range c, (-(f i)) = (-1)^c * ∏ i ∈ range c, f i := by
  induction c with
  | zero => simp
  | succ n ih => rw [Finset.prod_range_succ, Finset.prod_range_succ, ih, pow_succ]; ring

set_option maxRecDepth 8000 in
theorem per_corner_ratio_rowdrop (l : List ℕ) (c : ℕ)
    (hl : List.Sorted (· ≥ ·) l) (hc : IsCorner l c)
    (hpos : ∀ a ∈ l, 0 < a) (hone : l.getD c 0 = 1) :
    (prodHooks l : ℚ) / (prodHooks (removeCorner l c) : ℚ)
      = betaVec l ⟨c, hc.1⟩
          * (∏ j ∈ univ.erase (⟨c, hc.1⟩ : Fin l.length), (betaVec l ⟨c, hc.1⟩ - 1 - betaVec l j))
          / vWeight (betaVec l) ⟨c, hc.1⟩ := by
  have hlen := length_eq_succ_rowdrop l c hc hpos hone
  set cF : Fin l.length := ⟨c, hc.1⟩ with hcF
  have hlc_sorted := sorted_removeCorner l c hl hc
  have hbc1 : betaVec l cF = 1 := by
    rw [hcF, betaVec_eq_betaNat]; exact betaNat_c_rowdrop_one l c hc hpos hone
  have hvwdef : vWeight (betaVec l) cF = ∏ j ∈ univ.erase cF, (betaVec l cF - betaVec l j) := rfl
  have he1 : ∏ j ∈ univ.erase cF, (betaVec l cF - 1 - betaVec l j)
      = ∏ i ∈ range c, (betaVec l cF - 1 - betaNat l i) :=
    prod_erase_last_eq_range l c hc hpos hone (fun x => betaVec l cF - 1 - x)
  have he2 : ∏ j ∈ univ.erase cF, (betaVec l cF - betaVec l j)
      = ∏ i ∈ range c, (betaVec l cF - betaNat l i) :=
    prod_erase_last_eq_range l c hc hpos hone (fun x => betaVec l cF - x)
  rw [hvwdef, he1, he2, hbc1]
  have h1q : (prodHooks l : ℚ) * (betaProdGap l : ℚ) = (betaFactProd l : ℚ) := by
    exact_mod_cast prodHooks_mul_betaProdGap l hl
  have h2q : (prodHooks (removeCorner l c) : ℚ) * (betaProdGap (removeCorner l c) : ℚ)
      = (betaFactProd (removeCorner l c) : ℚ) := by
    exact_mod_cast prodHooks_mul_betaProdGap (removeCorner l c) hlc_sorted
  have hfac := betaFactProd_ratio_rowdrop l c hc hpos hone
  have hvand := betaProdGap_ratio_rowdrop l c hl hc hpos hone
  have hbnc : betaNat l c = 1 := betaNat_c_rowdrop_one l c hc hpos hone
  rw [hbnc] at hvand
  have hphc : (prodHooks (removeCorner l c) : ℚ) ≠ 0 := by
    have := prodHooks_pos (removeCorner l c) hlc_sorted (removeCorner_pos l c); positivity
  have hbpc : (betaProdGap (removeCorner l c) : ℚ) ≠ 0 := by
    have := betaProdGap_pos (removeCorner l c) hlc_sorted; positivity
  have hinj : Function.Injective (betaVec l) := betaVec_injective l hl
  have hden : ∀ i ∈ range c, (1 : ℚ) - betaNat l i ≠ 0 := by
    intro i hi; rw [mem_range] at hi
    have hiv : betaVec l (⟨i, by omega⟩ : Fin l.length) = betaNat l i := betaVec_eq_betaNat l _
    have hfne : (⟨i, by omega⟩ : Fin l.length) ≠ cF := Fin.ne_of_val_ne (Nat.ne_of_lt hi)
    have hbne : betaNat l i ≠ 1 := by
      rw [← hiv, ← hbc1]; exact fun e => hfne (hinj e)
    intro e; apply hbne; linarith
  have hP : (∏ i ∈ range c, ((1:ℚ) - betaNat l i)) ≠ 0 := Finset.prod_ne_zero_iff.mpr hden
  rw [one_mul, div_eq_div_iff hphc hP]
  have hsn : (∏ i ∈ range c, ((1:ℚ) - 1 - betaNat l i)) = (-1)^c * ∏ i ∈ range c, betaNat l i := by
    rw [← prod_neg_range]; apply Finset.prod_congr rfl; intro i _; ring
  have hsd : (∏ i ∈ range c, ((1:ℚ) - betaNat l i)) = (-1)^c * ∏ i ∈ range c, (betaNat l i - 1) := by
    rw [← prod_neg_range]; apply Finset.prod_congr rfl; intro i _; ring
  rw [hsn, hsd]
  have hcast : (∏ i ∈ range c, (betaNatVal l i : ℚ)) = ∏ i ∈ range c, betaNat l i := by
    apply Finset.prod_congr rfl; intro i _; unfold betaNat betaNatVal; push_cast; ring
  rw [hcast] at hfac
  refine mul_right_cancel₀ hbpc ?_
  linear_combination (-((-1:ℚ)^c * prodHooks l)) * hvand + ((-1:ℚ)^c) * h1q
    + ((-1:ℚ)^c) * hfac - ((-1:ℚ)^c * ∏ i ∈ range c, betaNat l i) * h2q

end QOU.Mathlib.SYTBetaLagrange
