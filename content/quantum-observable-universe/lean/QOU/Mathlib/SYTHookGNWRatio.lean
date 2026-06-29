import QOU.Mathlib.SYTHookGNWWiring

/-!
# QOU.Mathlib.SYTHookGNWRatio — the per-corner hook ratio (toward `gnwHookIdentity`)

`SYTHookGNWWiring` proved the Vandermonde/factorial casts of `betaProdGap`/`betaFactProd`.  This file
builds the **per-corner hook ratio** `prodHooks(l)/prodHooks(l∖c) = β_c·∏_{j≠c}(β_c−1−β_j)/(β_c−β_j)`
that, summed over corners (non-corners vanish) against `betaLagrange`, closes `gnwHookIdentity`.

First piece: the **factorial side**.  For a non-row-drop corner `removeCorner l c = l.set c (l[c]−1)`
(no length change); `betaFactProd` factors depend only on `l[i]` and the drop length, so only factor `c`
changes (`β_c!/(β_c−1)! = β_c`).

Pure `ℕ`/`ℚ` combinatorics; nothing archimedean; no fit.
-/

namespace QOU.Mathlib.SYTBetaLagrange

open Finset

/-- `betaNatVal (l.set c v)` agrees with `l` off index `c`. -/
theorem betaNatVal_set_ne (l : List ℕ) (c v : ℕ) {i : ℕ} (hi : i ≠ c) :
    betaNatVal (l.set c v) i = betaNatVal l i := by
  unfold betaNatVal
  rw [List.length_set]
  congr 1
  rw [List.getD_eq_getElem?_getD, List.getD_eq_getElem?_getD, List.getElem?_set_ne (Ne.symm hi)]

/-- `betaNatVal (l.set c (l[c]−1))` at `c` is `betaNatVal l c − 1` (needs the row positive). -/
theorem betaNatVal_set_self (l : List ℕ) (c : ℕ) (hc : c < l.length) (hpos : 1 ≤ l.getD c 0) :
    betaNatVal (l.set c (l.getD c 0 - 1)) c = betaNatVal l c - 1 := by
  unfold betaNatVal
  rw [List.length_set]
  have hg : (l.set c (l.getD c 0 - 1)).getD c 0 = l.getD c 0 - 1 := by
    rw [List.getD_eq_getElem?_getD, List.getElem?_set_self hc, Option.getD_some]
  rw [hg]; omega

/-- **Factorial side of the per-corner ratio (non-row-drop).** `betaFactProd l = β_c · betaFactProd(l∖c)`
with `l∖c = l.set c (l[c]−1)`: only factor `c` changes, contributing `β_c!/(β_c−1)! = β_c`. -/
theorem betaFactProd_ratio (l : List ℕ) (c : ℕ) (hc : c < l.length) (hpos : 1 ≤ l.getD c 0) :
    (QOU.Mathlib.SYTEnum.betaFactProd l : ℚ)
      = (betaNatVal l c : ℚ) * (QOU.Mathlib.SYTEnum.betaFactProd (l.set c (l.getD c 0 - 1)) : ℚ) := by
  have hb1 : 1 ≤ betaNatVal l c := by unfold betaNatVal; omega
  rw [betaFactProd_cast, betaFactProd_cast, List.length_set,
      ← Finset.mul_prod_erase (Finset.range l.length)
        (fun i => ((betaNatVal l i).factorial : ℚ)) (Finset.mem_range.mpr hc),
      ← Finset.mul_prod_erase (Finset.range l.length)
        (fun i => ((betaNatVal (l.set c (l.getD c 0 - 1)) i).factorial : ℚ))
        (Finset.mem_range.mpr hc),
      betaNatVal_set_self l c hc hpos, ← mul_assoc]
  congr 1
  · rw [← Nat.cast_mul]
    congr 1
    obtain ⟨m, hm⟩ : ∃ m, betaNatVal l c = m + 1 := ⟨betaNatVal l c - 1, by omega⟩
    rw [hm, Nat.add_sub_cancel, Nat.factorial_succ]
  · apply Finset.prod_congr rfl
    intro i hi
    rw [Finset.mem_erase] at hi
    rw [betaNatVal_set_ne l c _ hi.1]

/-! ## Vandermonde side: the pairs form of `betaProdGap` (enabler for the gap ratio) -/

/-- The row-`i` gap factor as a product over the actual upper indices `j ∈ (i, k)`, dropping the
`m ↦ i+1+m` reindex (`Finset.prod_Ico_eq_prod_range`). -/
theorem row_range_eq_Ioo (l : List ℕ) (i : ℕ) :
    ∏ m ∈ Finset.range (l.length - 1 - i), (betaNat l i - betaNat l (i + 1 + m))
      = ∏ j ∈ Finset.Ioo i l.length, (betaNat l i - betaNat l j) := by
  rw [← Nat.Ico_succ_left, Finset.prod_Ico_eq_prod_range,
      show l.length - 1 - i = l.length - (i + 1) from by omega]

/-- **`betaProdGap` as a pairs product** `∏_{i<j}(βᵢ−βⱼ)` organised by lower index `i` over `j ∈ (i,k)`.
This form isolates the index-`c` factors needed for the per-corner gap ratio. -/
theorem betaProdGap_cast_pairs (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) :
    ((QOU.Mathlib.SYTEnum.betaProdGap l : ℕ) : ℚ)
      = ∏ i ∈ Finset.range l.length, ∏ j ∈ Finset.Ioo i l.length,
          (betaNat l i - betaNat l j) := by
  rw [betaProdGap_cast l hl]
  exact Finset.prod_congr rfl (fun i _ => row_range_eq_Ioo l i)

/-- `betaNat = betaNatVal` as a `ℚ` cast. -/
theorem betaNat_eq (l : List ℕ) (i : ℕ) : betaNat l i = (betaNatVal l i : ℚ) := by
  unfold betaNat betaNatVal; push_cast; ring

/-- `betaNat (l.set c v)` agrees with `l` off `c` (cast of `betaNatVal_set_ne`). -/
theorem betaNat_set_ne (l : List ℕ) (c v : ℕ) {i : ℕ} (hi : i ≠ c) :
    betaNat (l.set c v) i = betaNat l i := by
  rw [betaNat_eq, betaNat_eq, betaNatVal_set_ne l c v hi]

/-- `betaNat (l.set c (l[c]−1))` at `c` is `betaNat l c − 1`. -/
theorem betaNat_set_self (l : List ℕ) (c : ℕ) (hc : c < l.length) (hpos : 1 ≤ l.getD c 0) :
    betaNat (l.set c (l.getD c 0 - 1)) c = betaNat l c - 1 := by
  have h1 : 1 ≤ betaNatVal l c := by unfold betaNatVal; omega
  rw [betaNat_eq, betaNatVal_set_self l c hc hpos, Nat.cast_sub h1, betaNat_eq]
  norm_num

/-- `betaProdGap` as a single product over the pairs `(i, j)` with `i < j < k`. -/
theorem betaProdGap_cast_sigma (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) :
    ((QOU.Mathlib.SYTEnum.betaProdGap l : ℕ) : ℚ)
      = ∏ p ∈ (Finset.range l.length).sigma (fun i => Finset.Ioo i l.length),
          (betaNat l p.1 - betaNat l p.2) := by
  rw [betaProdGap_cast_pairs l hl, Finset.prod_sigma']

/-- `betaNat` is strictly antitone on indices `< length`: `i < j < k ⟹ βⱼ < βᵢ`. -/
theorem betaNat_lt (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) {i j : ℕ}
    (hij : i < j) (hj : j < l.length) : betaNat l j < betaNat l i := by
  rw [betaNat_eq, betaNat_eq]
  have hlen : l.getD j 0 ≤ l.getD i 0 := QOU.BraidKnot.IdentityI.getD_antitone l hl (le_of_lt hij)
  unfold betaNatVal
  have hsh : l.length - 1 - j < l.length - 1 - i := by omega
  have h2 : ((l.length - 1 - j : ℕ) : ℚ) < ((l.length - 1 - i : ℕ) : ℚ) := by exact_mod_cast hsh
  have h1 : ((l.getD j 0 : ℕ) : ℚ) ≤ ((l.getD i 0 : ℕ) : ℚ) := by exact_mod_cast hlen
  push_cast at h1 h2 ⊢
  linarith

/-- The gap factor `βᵢ − βⱼ` is nonzero for `i < j < k` (strict antitonicity). -/
theorem betaNat_ne (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) {i j : ℕ}
    (hij : i < j) (hj : j < l.length) : betaNat l i - betaNat l j ≠ 0 := by
  have := betaNat_lt l hl hij hj; intro h; linarith [sub_eq_zero.mp h]

/-- **The gap-ratio crux (R1 core).** The product of per-term ratios `(β'ᵢ−β'ⱼ)/(βᵢ−βⱼ)` over all
pairs `i<j<k` equals the GAP product `∏_{j≠c}(β_c−1−β_j)/(β_c−β_j)`.  Inner ratios are `1` off the
index-`c` factors (`hr1`); `i>c` columns vanish to `1`, `i<c` columns collapse to the single `j=c`
factor (sign-flipped to GAP shape), and the `i=c` column is GAP's `Ioo c k` part. -/
theorem gap_ratio_prod (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (c : ℕ)
    (hc : c < l.length) (hpos : 1 ≤ l.getD c 0) :
    (∏ i ∈ Finset.range l.length, ∏ j ∈ Finset.Ioo i l.length,
        (betaNat (l.set c (l.getD c 0 - 1)) i - betaNat (l.set c (l.getD c 0 - 1)) j)
          / (betaNat l i - betaNat l j))
      = ∏ j ∈ (Finset.range l.length).erase c,
          (betaNat l c - 1 - betaNat l j) / (betaNat l c - betaNat l j) := by
  set k := l.length with hk
  set lc := l.set c (l.getD c 0 - 1) with hlc
  -- the per-term ratio value
  have hne : ∀ i j, i < j → j < k → betaNat l i - betaNat l j ≠ 0 :=
    fun i j hij hj => betaNat_ne l hl hij hj
  -- ratio(i,j) = 1 when i ≠ c and j ≠ c
  have hr1 : ∀ i j, i ≠ c → j ≠ c → i < j → j < k →
      (betaNat lc i - betaNat lc j) / (betaNat l i - betaNat l j) = 1 := by
    intro i j hi hj hij hjk
    rw [betaNat_set_ne l c _ hi, betaNat_set_ne l c _ hj, div_self (hne i j hij hjk)]
  -- inner_i = 1 for i > c
  have hgt : ∀ i ∈ Finset.range k, c < i →
      (∏ j ∈ Finset.Ioo i k, (betaNat lc i - betaNat lc j) / (betaNat l i - betaNat l j)) = 1 := by
    intro i _ hci
    apply Finset.prod_eq_one
    intro j hj
    rw [Finset.mem_Ioo] at hj
    exact hr1 i j (by omega) (by omega) hj.1 hj.2
  -- inner_i = ratio(i,c) for i < c
  have hlt : ∀ i ∈ Finset.range k, i < c →
      (∏ j ∈ Finset.Ioo i k, (betaNat lc i - betaNat lc j) / (betaNat l i - betaNat l j))
        = (betaNat l c - 1 - betaNat l i) / (betaNat l c - betaNat l i) := by
    intro i _ hic
    rw [Finset.prod_eq_single c]
    · rw [betaNat_set_ne l c _ (by omega : i ≠ c), betaNat_set_self l c hc hpos]
      have h1 := hne i c hic hc
      have h2 : betaNat l c - betaNat l i ≠ 0 := by
        rw [sub_ne_zero] at h1 ⊢; exact h1.symm
      rw [div_eq_div_iff h1 h2]; ring
    · intro j hj hjc
      rw [Finset.mem_Ioo] at hj
      exact hr1 i j (by omega) hjc hj.1 hj.2
    · intro h; rw [Finset.mem_Ioo] at h; omega
  -- inner_c
  have heqc :
      (∏ j ∈ Finset.Ioo c k, (betaNat lc c - betaNat lc j) / (betaNat l c - betaNat l j))
        = ∏ j ∈ Finset.Ioo c k, (betaNat l c - 1 - betaNat l j) / (betaNat l c - betaNat l j) := by
    apply Finset.prod_congr rfl
    intro j hj
    rw [Finset.mem_Ioo] at hj
    rw [betaNat_set_self l c hc hpos, betaNat_set_ne l c _ (by omega : j ≠ c)]
  -- assemble: pull out i=c, restrict rest to range c, split erase c
  rw [← Finset.mul_prod_erase (Finset.range k) _ (Finset.mem_range.mpr hc), heqc]
  have hrest :
      (∏ i ∈ (Finset.range k).erase c, ∏ j ∈ Finset.Ioo i k,
          (betaNat lc i - betaNat lc j) / (betaNat l i - betaNat l j))
        = ∏ i ∈ Finset.range c, (betaNat l c - 1 - betaNat l i) / (betaNat l c - betaNat l i) := by
    rw [← Finset.prod_subset (s₁ := Finset.range c) (s₂ := (Finset.range k).erase c)]
    · apply Finset.prod_congr rfl
      intro i hi
      rw [Finset.mem_range] at hi
      exact hlt i (Finset.mem_range.mpr (by omega)) hi
    · intro i hi
      rw [Finset.mem_range] at hi
      rw [Finset.mem_erase, Finset.mem_range]; omega
    · intro i hi hni
      rw [Finset.mem_erase, Finset.mem_range] at hi
      rw [Finset.mem_range] at hni
      exact hgt i (Finset.mem_range.mpr hi.2) (by omega)
  rw [hrest]
  -- GAP over erase c = range c ∪ Ioo c k
  have hsplit : (Finset.range k).erase c = Finset.range c ∪ Finset.Ioo c k := by
    ext x; rw [Finset.mem_erase, Finset.mem_range, Finset.mem_union, Finset.mem_range, Finset.mem_Ioo]
    omega
  rw [hsplit, Finset.prod_union (by
    rw [Finset.disjoint_left]; intro a ha hb
    rw [Finset.mem_range] at ha; rw [Finset.mem_Ioo] at hb; omega)]
  ring

/-- **(R1) The per-corner gap ratio (non-row-drop), sorry-free.** For a corner `c`,
`betaProdGap (l.set c (l[c]−1)) = betaProdGap l · ∏_{j≠c}(β_c−1−β_j)/(β_c−β_j)`.  Factor each pairs
term `β'ᵢ−β'ⱼ = (βᵢ−βⱼ)·rᵢⱼ` (`mul_div_cancel₀`, gaps nonzero) and evaluate `∏ᵢ∏ⱼ rᵢⱼ` via
`gap_ratio_prod`. -/
theorem betaProdGap_ratio (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (c : ℕ)
    (hcorner : QOU.Mathlib.SYTEnum.IsCorner l c) :
    (QOU.Mathlib.SYTEnum.betaProdGap (l.set c (l.getD c 0 - 1)) : ℚ)
      = (QOU.Mathlib.SYTEnum.betaProdGap l : ℚ)
        * ∏ j ∈ (Finset.range l.length).erase c,
            (betaNat l c - 1 - betaNat l j) / (betaNat l c - betaNat l j) := by
  have hc : c < l.length := hcorner.1
  have hpos : 1 ≤ l.getD c 0 := by have := hcorner.2; omega
  have hl' : List.Sorted (· ≥ ·) (l.set c (l.getD c 0 - 1)) :=
    QOU.Mathlib.SYTEnum.sorted_set_corner l c hl hcorner
  rw [← gap_ratio_prod l hl c hc hpos,
      betaProdGap_cast_pairs (l.set c (l.getD c 0 - 1)) hl', betaProdGap_cast_pairs l hl]
  simp only [List.length_set]
  rw [← Finset.prod_mul_distrib]
  apply Finset.prod_congr rfl
  intro i hi
  rw [← Finset.prod_mul_distrib]
  apply Finset.prod_congr rfl
  intro j hj
  rw [Finset.mem_range] at hi; rw [Finset.mem_Ioo] at hj
  have hne := betaNat_ne l hl hj.1 hj.2
  field_simp

/-!
## Remaining design — the gap ratio, row-drop, and assembly (next pieces)

All scaffolding above is sorry-free.  The remaining route to `gnwHookIdentity`:

**(R1) Gap ratio (non-row-drop)** — DONE (`betaProdGap_ratio`). `betaProdGap (l.set c (l[c]−1)) = betaProdGap l ·
∏_{j∈(range k).erase c} (β_c−1−β_j)/(β_c−β_j)`.  Via the pairs form: factor each term
`β'ᵢ−β'ⱼ = (βᵢ−βⱼ)·rᵢⱼ` (`mul_div_cancel₀`, gaps nonzero by `betaNat_ne`), so
`betaProdGap(l∖c) = betaProdGap(l)·∏ᵢ∏ⱼ rᵢⱼ` (`prod_mul_distrib`).  Evaluate the inner
ratio product: `inner_i = 1` for `i>c`; `inner_c = ∏_{j∈Ioo c k}(β_c−1−β_j)/(β_c−β_j)`;
`inner_i = r_{i,c} = (βᵢ−β_c+1)/(βᵢ−β_c)` for `i<c` (`prod_eq_single c`, others `=1`).
Pull out `i=c` (`mul_prod_erase`), restrict the rest to `range c` (`prod_subset`, `i>c`
terms `=1`), and use the sign flip `(βᵢ−β_c+1)/(βᵢ−β_c) = (β_c−1−βᵢ)/(β_c−βᵢ)` (`ring`).
Split `erase c = range c ∪ Ioo c k`.

**(R2) Factorial × gap ⇒ per-corner ratio** — combine `betaFactProd_ratio` (= β_c) with
(R1) through identity (i) `prodHooks·betaProdGap = betaFactProd` (`prodHooks_mul_betaProdGap`,
`betaProdGap_pos`): `prodHooks(l)/prodHooks(l∖c) = β_c·∏_{j≠c}(β_c−1−β_j)/(β_c−β_j)`.

**(R3) Row-drop corner** (`l[c]=1`, last row, `k→k−1`) — separate but the same product
formula holds (β shifts uniformly; the βNat algebra still gives the same per-corner value).

**(R4) Assembly** — sum over `corners l`; non-corner rows vanish (`β_c−1 = β_{c+1}`); bridge
`corners ↔ Fin k` and apply `betaLagrange (betaVec l)` + `sum_betaVec_sub` (`= sz l`).
-/

end QOU.Mathlib.SYTBetaLagrange
