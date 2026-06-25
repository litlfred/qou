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

end QOU.BraidKnot.IdentityI
