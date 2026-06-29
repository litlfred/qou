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

end QOU.Mathlib.SYTBetaLagrange
