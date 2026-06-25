import QOU.BraidKnot.KeystoneC2DimTranspose
import QOU.MathlibExt.QPartitionCombinatorics

/-!
# Keystone C2 — the genuine q-version `d_q(λ) = d_q(λ')` (in progress)

The merged `KeystoneC2DimTranspose` proves the `q = 1` case `f^λ = f^{λ'}`.  This file targets the
genuine keystone weight symmetry `qDim q (conjugate λ) = qDim q λ` (⇒ `W_λ = W_{λ'}`), where
`qDim` is `MathlibExt.QPartitionCombinatorics.qDim` — the `[n]_q! / ∏_c [h_c]_q` q-hook-length
dimension.

Strategy: rather than rebuild the column-length duality in that file's `foldl` / `get?` model, we
**bridge** to the merged `colLen`-based model and reuse the generic `cell_fubini_prod`.  The
reusable core below is `qHookProd_conj` — the `qBracket`-weighted hook product is
transpose-invariant — proved exactly as the merged `prodHooks_conj` with `qBracket q (·)` wrapping
the hook.  The remaining bridges (`Partition.conjugate = conj`, `Partition.hookLength = ` the
`colLen`-hook, `qDim`'s `foldl` ↔ `Finset.prod`) compose this into `qDim_conj`.

Base ring: `ℝ` only via `qBracket`/`qDim` (the q-dimension is genuinely archimedean); the transpose
combinatorics stays in `ℕ`.  No fit.
-/

namespace QOU.BraidKnot.IdentityI

open Finset QOU.MathlibExt.QPartitionCombinatorics

/-- **The `qBracket`-weighted hook product is transpose-invariant** (reusable core, ℝ).
`∏_c [h_c]_q (λ') = ∏_c [h_c]_q (λ)`, with the hook in the merged `colLen` model.  Proof: identical
to `prodHooks_conj` with `qBracket q (·)` wrapping the hook — the conjugate's hook at `(r,c)` equals
`λ`'s hook at `(c,r)` (`colLen_conj` + arm/leg commute), and `cell_fubini_prod` (at `M = ℝˣ`-style
multiplicative `ℝ`) matches the cell sets. -/
theorem qHookProd_conj (q : ℝ) (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    (∏ i ∈ Finset.range (conj l).length, ∏ j ∈ Finset.range ((conj l).getD i 0),
        qBracket q ((conj l).getD i 0 - j + (colLen (conj l) j - i) - 1))
      = ∏ i ∈ Finset.range l.length, ∏ j ∈ Finset.range (l.getD i 0),
          qBracket q (l.getD i 0 - j + (colLen l j - i) - 1) := by
  rw [conj_length]
  have hL : ∀ r ∈ Finset.range (l.headD 0),
      (∏ c ∈ Finset.range ((conj l).getD r 0),
        qBracket q ((conj l).getD r 0 - c + (colLen (conj l) c - r) - 1))
        = ∏ c ∈ Finset.range (colLen l r),
            qBracket q (l.getD c 0 - r + (colLen l r - c) - 1) := by
    intro r hr
    rw [conj_getD l r (Finset.mem_range.mp hr)]
    apply Finset.prod_congr rfl; intro c _
    rw [colLen_conj l hl c, Nat.add_comm (colLen l r - c) (l.getD c 0 - r)]
  rw [Finset.prod_congr rfl hL,
    cell_fubini_prod l hl (fun i j => qBracket q (l.getD i 0 - j + (colLen l j - i) - 1))]

/-! ## Bridge 1 — `Partition.conjugate = conj` (the two models' transpose agree on sorted partitions) -/

/-- `foldl Nat.max a t = a` when every element of `t` is `≤ a`. -/
theorem foldl_max_eq_of_le : ∀ (a : ℕ) (t : List ℕ), (∀ x ∈ t, x ≤ a) → t.foldl Nat.max a = a
  | a, [], _ => by simp
  | a, b :: s, h => by
    simp only [List.foldl_cons, Nat.max_eq_left (h b (by simp))]
    exact foldl_max_eq_of_le a s (fun x hx => h x (List.mem_cons_of_mem _ hx))

/-- For a weakly-decreasing partition, `Partition.maxPart l = λ_1` (the head). -/
theorem maxPart_eq_headD (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    Partition.maxPart l = l.headD 0 := by
  unfold Partition.maxPart
  cases l with
  | nil => rfl
  | cons a t =>
    obtain ⟨hat, _⟩ := List.sorted_cons.mp hl
    simp only [List.foldl_cons, List.headD_cons]
    rw [show Nat.max (Nat.max 0 0) a = a from by simp]
    exact foldl_max_eq_of_le a t hat

/-- **Bridge 1.** The `QPartitionCombinatorics` conjugate equals the merged `colLen`-conjugate on a
weakly-decreasing partition: same range (`maxPart = headD`) and definitionally-equal map function
(`(l.filter (· > j)).length = colLen l j`). -/
theorem conjugate_eq_conj (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    Partition.conjugate l = conj l := by
  unfold Partition.conjugate conj
  rw [maxPart_eq_headD l hl]
  rfl

/-! ## Bridge 2 — `Partition.hookLength = ` the `colLen`-hook -/

/-- For a weakly-decreasing partition with `λ_i > j` (so cell `(i,j)` exists), the leg count
`#{i' > i : λ_{i'} > j}` equals `colLen l j − (i+1)`: the first `i+1` rows all exceed `j`. -/
theorem leg_count (l : List ℕ) (hl : l.Sorted (· ≥ ·)) (i j : ℕ)
    (hi : i < l.length) (hj : j < l.getD i 0) :
    colLen l j = (i + 1) + ((l.drop (i + 1)).filter (fun p => j < p)).length := by
  have htake : ∀ x ∈ l.take (i + 1), j < x := by
    intro x hx
    obtain ⟨k, hk', hkx⟩ := List.mem_iff_getElem.mp hx
    have hk := hk'
    rw [List.length_take] at hk
    have hkl : k < l.length := by omega
    have hki : k ≤ i := by omega
    have hxk : x = l.getD k 0 := by
      rw [← hkx, List.getElem_take, List.getD_eq_getElem?_getD,
        List.getElem?_eq_getElem hkl, Option.getD_some]
    rw [hxk]
    exact lt_of_lt_of_le hj (getD_antitone l hl hki)
  have hcol : colLen l j = ((l.take (i + 1)).filter (fun p => j < p)).length
      + ((l.drop (i + 1)).filter (fun p => j < p)).length := by
    unfold colLen
    conv_lhs => rw [← List.take_append_drop (i + 1) l]
    rw [List.filter_append, List.length_append]
  rw [hcol, List.filter_eq_self.mpr (by simpa using htake), List.length_take,
    Nat.min_eq_left (by omega)]

/-- **Bridge 2.** `Partition.hookLength l i j` equals the merged `colLen`-hook
`(λ_i − j) + (colLen j − i) − 1` for a genuine cell of a weakly-decreasing partition. -/
theorem hookLength_eq (l : List ℕ) (hl : l.Sorted (· ≥ ·)) (i j : ℕ)
    (hi : i < l.length) (hj : j < l.getD i 0) :
    Partition.hookLength l i j = (l.getD i 0 - j) + (colLen l j - i) - 1 := by
  have hget : l.get? i = some (l.getD i 0) := by
    rw [List.get?_eq_getElem?, List.getElem?_eq_getElem hi, List.getD_eq_getElem?_getD,
      List.getElem?_eq_getElem hi, Option.getD_some]
  have hleg := leg_count l hl i j hi hj
  unfold Partition.hookLength
  rw [hget]
  simp only [hj, if_true, gt_iff_lt]
  omega

end QOU.BraidKnot.IdentityI
