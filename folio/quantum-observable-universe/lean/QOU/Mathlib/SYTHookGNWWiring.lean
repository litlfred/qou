import QOU.Mathlib.SYTBetaLagrange
import QOU.Mathlib.SYTCornerListConnection
import QOU.Mathlib.SYTHookFormulaBetaProd

/-!
# QOU.Mathlib.SYTHookGNWWiring — wiring the abstract β-Lagrange identity to `gnwHookIdentity`

`SYTBetaLagrange.betaLagrange` proves, for distinct `β : Fin k → ℚ`,

    ∑ᵢ βᵢ · ∏_{j≠i}(βᵢ − 1 − βⱼ)/(βᵢ − βⱼ) = (∑ⱼ βⱼ) − C(k,2).

`SYTHookGNW.gnwHookIdentity` needs the **list-level** statement
`∑_{corners c} prodHooks(l)/prodHooks(l∖c) = sz l`.  This file builds the bridge via the β-coordinates
`βᵢ = l[i] + (k−1−i)` (`k = l.length`):

* `betaVec` — the β-vector of a shape; `betaVec_strictAnti` / `betaVec_injective` (distinct nodes);
* `sum_betaVec` — `∑ᵢ βᵢ = sz l + C(k,2)`, so `betaLagrange`'s RHS `∑β − C(k,2)` **is** `sz l`.

The remaining per-corner hook-ratio identity (relating `prodHooks`/`removeCorner` to the β-product via
the Vandermonde `betaProdGap`) is the deeper step, handled separately.

Pure `ℕ`/`ℚ` combinatorics; nothing archimedean; no fit.
-/

namespace QOU.Mathlib.SYTBetaLagrange

open QOU.BraidKnot.IdentityI (sz)
open Finset

/-- The β-vector of a shape `l`: `βᵢ = l[i] + (k − 1 − i)` over `ℚ`, where `k = l.length`. -/
noncomputable def betaVec (l : List ℕ) : Fin l.length → ℚ :=
  fun i => (l.getD i 0 : ℚ) + ((l.length - 1 - (i : ℕ) : ℕ) : ℚ)

/-- For a weakly-decreasing shape, `βᵢ` is an integer (a cast `ℕ`): `l[i] + (k−1−i)`. -/
theorem betaVec_eq_natCast (l : List ℕ) (i : Fin l.length) :
    betaVec l i = ((l.getD i 0 + (l.length - 1 - (i : ℕ))) : ℕ) := by
  unfold betaVec; push_cast; ring

/-- **The β-vector is strictly antitone**: `i < i'` gives `βᵢ > β_{i'}` — the row length is weakly
decreasing while the staircase shift `k−1−i` strictly decreases. -/
theorem betaVec_strictAnti (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) :
    StrictAnti (betaVec l) := by
  intro a b hab
  unfold betaVec
  have ha : (a : ℕ) < l.length := a.2
  have hb : (b : ℕ) < l.length := b.2
  -- l[b] ≤ l[a] (antitone), and (k−1−b) < (k−1−a)
  have hlen : l.getD (b : ℕ) 0 ≤ l.getD (a : ℕ) 0 :=
    QOU.BraidKnot.IdentityI.getD_antitone l hl (le_of_lt hab)
  have hshift : l.length - 1 - (b : ℕ) < l.length - 1 - (a : ℕ) := by omega
  have h1 : ((l.getD (b:ℕ) 0 : ℚ)) ≤ (l.getD (a:ℕ) 0 : ℚ) := by exact_mod_cast hlen
  have h2 : ((l.length - 1 - (b:ℕ) : ℕ) : ℚ) < ((l.length - 1 - (a:ℕ) : ℕ) : ℚ) := by
    exact_mod_cast hshift
  linarith

/-- **The β-vector has distinct entries** (strictly antitone ⟹ injective). -/
theorem betaVec_injective (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) :
    Function.Injective (betaVec l) :=
  (betaVec_strictAnti l hl).injective

/-- `∑_{i : Fin k} (l[i] : ℚ) = sz l` — the β-vector's length part sums to the cell count. -/
theorem sum_getD (l : List ℕ) : ∑ i : Fin l.length, (l.getD (i : ℕ) 0 : ℚ) = (sz l : ℚ) := by
  rw [← Nat.cast_sum]
  congr 1
  rw [show sz l = l.sum from rfl, ← List.sum_ofFn]
  congr 1
  apply List.ext_getElem
  · simp
  · intro n h1 h2
    simp only [List.getElem_ofFn]
    rw [QOU.Mathlib.SYTEnum.getD_eq_getElem' l n (by simpa using h1)]

/-- `∑_{i : Fin k} (k − 1 − i) = C(k,2)` — the staircase shifts sum to the triangular number. -/
theorem sum_shift_triangular (k : ℕ) :
    ∑ i : Fin k, ((k - 1 - (i : ℕ) : ℕ) : ℚ) = (k.choose 2 : ℚ) := by
  rw [← Nat.cast_sum]
  congr 1
  have hnat : ∑ i : Fin k, (k - 1 - (i : ℕ)) = ∑ i ∈ Finset.range k, i := by
    rw [Fin.sum_univ_eq_sum_range (fun i => k - 1 - i) k]
    exact Finset.sum_range_reflect (fun i => i) k
  rw [hnat, Nat.choose_two_right, Finset.sum_range_id]

/-- **`betaLagrange`'s RHS is `sz l`.** `∑ⱼ βⱼ − C(k,2) = sz l`, so the β-Lagrange identity evaluates
to the cell count. -/
theorem sum_betaVec_sub (l : List ℕ) :
    (∑ i : Fin l.length, betaVec l i) - (l.length.choose 2 : ℚ) = (sz l : ℚ) := by
  unfold betaVec
  rw [Finset.sum_add_distrib, sum_getD, sum_shift_triangular]
  ring

/-! ## The recursive gap product as an explicit ℚ product (Vandermonde bridge keystone) -/

open QOU.Mathlib.SYTBeta (betaGapProd)

/-- **`betaGapProd` as an explicit ℚ product.** `(betaGapProd a t : ℚ) = ∏_{m<|t|} (a + 1 + m − t[m])`
— each factor is cast-safe because the tail entries are `≤ a`.  This identifies the corpus' recursive
Vandermonde factor `betaGapProd (l[i]) (l.drop (i+1))` with `∏_{j>i}(βᵢ − βⱼ)` (factor `m` is
`l[i] + (m+1) − l[i+1+m] = βᵢ − β_{i+1+m}`), the keystone for the per-corner hook ratio. -/
theorem betaGapProd_cast : ∀ (t : List ℕ) (a : ℕ), (∀ p ∈ t, p ≤ a) →
    (betaGapProd a t : ℚ) = ∏ m ∈ Finset.range t.length, ((a : ℚ) + 1 + (m : ℚ) - (t.getD m 0 : ℚ))
  | [], a, _ => by simp [betaGapProd]
  | c :: r, a, h => by
    have hc : c ≤ a := h c (by simp)
    have hr : ∀ p ∈ r, p ≤ a + 1 := fun p hp => le_trans (h p (by simp [hp])) (by omega)
    have hcast : ((a + 1 - c : ℕ) : ℚ) = (a : ℚ) + 1 - (c : ℚ) := by
      rw [Nat.cast_sub (by omega)]; push_cast; ring
    rw [QOU.Mathlib.SYTBeta.betaGapProd_cons, Nat.cast_mul, betaGapProd_cast r (a + 1) hr,
        List.length_cons, Finset.prod_range_succ', hcast,
        mul_comm (((a : ℚ) + 1) - (c : ℚ))]
    congr 1
    · apply Finset.prod_congr rfl
      intro m _
      rw [show (c :: r).getD (m + 1) 0 = r.getD m 0 from rfl]; push_cast; ring
    · rw [show (c :: r).getD 0 0 = c from rfl]; push_cast; ring

/-- The `ℕ`-indexed β-value `βᵢ = l[i] + (k−1−i)` (no `Fin` bound), for stating Vandermonde products
over `range`. Agrees with `betaVec` on valid indices. -/
noncomputable def betaNat (l : List ℕ) (i : ℕ) : ℚ :=
  (l.getD i 0 : ℚ) + ((l.length - 1 - i : ℕ) : ℚ)

/-- `betaVec` is `betaNat` restricted to `Fin k`. -/
theorem betaVec_eq_betaNat (l : List ℕ) (i : Fin l.length) : betaVec l i = betaNat l i.val := rfl

/-- **Per-row Vandermonde factor.** The corpus' recursive gap factor at row `i` is the column
`∏_{i<j}(βᵢ − βⱼ)` of the Vandermonde: `betaGapProd (l[i]) (l.drop (i+1)) = ∏_{m<k−1−i}(βᵢ − β_{i+1+m})`
(reindex `j = i+1+m`). -/
theorem betaGapProd_row_cast (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (i : ℕ) (hi : i < l.length) :
    (betaGapProd (l.getD i 0) (l.drop (i + 1)) : ℚ)
      = ∏ m ∈ Finset.range (l.length - 1 - i), (betaNat l i - betaNat l (i + 1 + m)) := by
  have hlen : (l.drop (i + 1)).length = l.length - 1 - i := by
    rw [List.length_drop]; omega
  rw [betaGapProd_cast (l.drop (i + 1)) (l.getD i 0)
        (fun p hp => QOU.Mathlib.SYTBeta.drop_le_getD l hl i hi p hp), hlen]
  apply Finset.prod_congr rfl
  intro m hm
  rw [Finset.mem_range] at hm
  have hgd : (l.drop (i + 1)).getD m 0 = l.getD (i + 1 + m) 0 := by
    rw [List.getD_eq_getElem?_getD, List.getD_eq_getElem?_getD, List.getElem?_drop]
  rw [hgd]
  unfold betaNat
  have hAB : l.length - 1 - i = (l.length - 1 - (i + 1 + m)) + 1 + m := by omega
  rw [hAB]; push_cast; ring

/-- **`betaProdGap` as the Vandermonde double-product.** `(betaProdGap l : ℚ) = ∏_{i<k} ∏_{i<j}(βᵢ−βⱼ)`,
assembling the per-row casts. This is `∏_{i<j}(βᵢ − βⱼ)` organised by lower-triangular column `i`. -/
theorem betaProdGap_cast (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) :
    ((QOU.Mathlib.SYTEnum.betaProdGap l : ℕ) : ℚ)
      = ∏ i ∈ Finset.range l.length, ∏ m ∈ Finset.range (l.length - 1 - i),
          (betaNat l i - betaNat l (i + 1 + m)) := by
  rw [show QOU.Mathlib.SYTEnum.betaProdGap l
        = ∏ i ∈ Finset.range l.length,
            QOU.Mathlib.SYTBeta.betaGapProd (l.getD i 0) (l.drop (i + 1)) from by
      unfold QOU.Mathlib.SYTEnum.betaProdGap; rw [QOU.Mathlib.SYTBeta.list_range_map_prod]]
  rw [Nat.cast_prod]
  apply Finset.prod_congr rfl
  intro i hi
  rw [Finset.mem_range] at hi
  exact betaGapProd_row_cast l hl i hi

/-- The `ℕ`-valued β-number `βᵢ = l[i] + (k−1−i)` (= `betaNat l i` as a natural). -/
def betaNatVal (l : List ℕ) (i : ℕ) : ℕ := l.getD i 0 + (l.length - 1 - i)

/-- **`betaFactProd` as `∏ βᵢ!`.** `(betaFactProd l : ℚ) = ∏_{i<k} (βᵢ)!`. Each factor depends only on
`l[i]` and the drop *length* `k−1−i`, so under `removeCorner = l.set c (l[c]−1)` only factor `c` changes
(the factorial side of the per-corner ratio). -/
theorem betaFactProd_cast (l : List ℕ) :
    ((QOU.Mathlib.SYTEnum.betaFactProd l : ℕ) : ℚ)
      = ∏ i ∈ Finset.range l.length, ((betaNatVal l i).factorial : ℚ) := by
  rw [show QOU.Mathlib.SYTEnum.betaFactProd l
        = ∏ i ∈ Finset.range l.length, (betaNatVal l i).factorial from by
      unfold QOU.Mathlib.SYTEnum.betaFactProd betaNatVal
      rw [QOU.Mathlib.SYTBeta.list_range_map_prod]
      apply Finset.prod_congr rfl
      intro i hi; rw [Finset.mem_range] at hi
      congr 2
      rw [List.length_drop]; omega]
  rw [Nat.cast_prod]

end QOU.Mathlib.SYTBetaLagrange
