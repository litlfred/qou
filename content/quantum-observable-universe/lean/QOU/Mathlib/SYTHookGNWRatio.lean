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

end QOU.Mathlib.SYTBetaLagrange
