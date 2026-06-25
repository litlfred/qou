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

/-! ## Bridge 3 — `conj l` is sorted; `qDim`'s nested `foldl` is a double `Finset.prod` -/

/-- `colLen` is antitone in the column index `j`: wider columns sit at the left.  (Each row
indicator `[j < λ_k]` only shrinks as `j` grows.) -/
theorem colLen_antitone (l : List ℕ) {j₁ j₂ : ℕ} (h : j₁ ≤ j₂) :
    colLen l j₂ ≤ colLen l j₁ := by
  rw [colLen_eq_indicator_sum, colLen_eq_indicator_sum]
  apply Finset.sum_le_sum
  intro k _
  by_cases hk : j₂ < l.getD k 0
  · rw [if_pos hk, if_pos (lt_of_le_of_lt h hk)]
  · rw [if_neg hk]; exact Nat.zero_le _

/-- The merged conjugate `conj l` is itself weakly decreasing: its rows are the column lengths
`colLen l j`, which decrease in `j` (`colLen_antitone`). -/
theorem conj_sorted (l : List ℕ) : (conj l).Sorted (· ≥ ·) := by
  show List.Pairwise (· ≥ ·) (conj l)
  rw [List.pairwise_iff_getElem]
  intro i j _ _ hij
  simp only [conj, List.getElem_map, List.getElem_range]
  exact colLen_antitone l (le_of_lt hij)

/-- `(l.get? i).getD 0 = l.getD i 0` — the inner `qDim` row-length bound, normalised (agrees both
in range, where `get? = some`, and out of range, where both are the default `0`). -/
theorem getQ_getD (l : List ℕ) (i : ℕ) : (l.get? i).getD 0 = l.getD i 0 := by
  rw [List.get?_eq_getElem?, ← List.getD_eq_getElem?_getD]

/-- A multiplicative `foldl` over `range n` is the `Finset.prod` (product analog of the additive
`list_range_map_sum`, but written directly on the `foldl` shape `qDim` uses). -/
theorem foldl_mul_range {M : Type*} [CommMonoid M] (n : ℕ) (f : ℕ → M) :
    (List.range n).foldl (fun acc i => acc * f i) 1 = ∏ i ∈ Finset.range n, f i := by
  induction n with
  | zero => simp
  | succ m ih =>
    rw [List.range_succ, List.foldl_append, ih, Finset.prod_range_succ]
    simp

/-- **`qDim` as a double `Finset.prod`.** Unfold the nested `foldl` denominator into a `Finset`
double product, with the inner row-length bound normalised to `l.getD i 0` (`getQ_getD`). -/
theorem qDim_eq_prod (q : ℝ) (l : List ℕ) :
    qDim q l = qFactorial q (Partition.size l) /
      ∏ i ∈ Finset.range l.length,
        ∏ j ∈ Finset.range (l.getD i 0), qBracket q (Partition.hookLength l i j) := by
  unfold qDim
  simp only [foldl_mul_range, getQ_getD, Partition.length]

/-- **C2 — the genuine q-version: the q-hook-length dimension is transpose-invariant**,
`d_q(λ) = d_q(λ')`, hence the q-Plancherel weight `W_λ = d_q(λ)²/[n]_q!` satisfies `W_λ = W_{λ'}`
(the s5-so3 keystone's necessary condition C2 — the weight is chirality-blind).

`qDim q λ = [|λ|]_q! / ∏_c [h_c]_q`.  Both inputs are transpose-invariant: the size `|λ|` by
`sz_conj`, and the `qBracket`-weighted hook product by `qHookProd_conj` (rewriting each genuine
cell's `Partition.hookLength` to the merged `colLen`-hook via `hookLength_eq`, on both `conj l`
— sorted by `conj_sorted` — and `l`).  So the q-dimension is too. -/
theorem qDim_conj (q : ℝ) (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    qDim q (Partition.conjugate l) = qDim q l := by
  have e1 : (∏ i ∈ Finset.range (conj l).length, ∏ j ∈ Finset.range ((conj l).getD i 0),
              qBracket q (Partition.hookLength (conj l) i j))
          = ∏ i ∈ Finset.range (conj l).length, ∏ j ∈ Finset.range ((conj l).getD i 0),
              qBracket q ((conj l).getD i 0 - j + (colLen (conj l) j - i) - 1) := by
    apply Finset.prod_congr rfl; intro i hi
    apply Finset.prod_congr rfl; intro j hj
    rw [hookLength_eq (conj l) (conj_sorted l) i j
          (Finset.mem_range.mp hi) (Finset.mem_range.mp hj)]
  have e2 : (∏ i ∈ Finset.range l.length, ∏ j ∈ Finset.range (l.getD i 0),
              qBracket q (Partition.hookLength l i j))
          = ∏ i ∈ Finset.range l.length, ∏ j ∈ Finset.range (l.getD i 0),
              qBracket q (l.getD i 0 - j + (colLen l j - i) - 1) := by
    apply Finset.prod_congr rfl; intro i hi
    apply Finset.prod_congr rfl; intro j hj
    rw [hookLength_eq l hl i j (Finset.mem_range.mp hi) (Finset.mem_range.mp hj)]
  have hnum : Partition.size (conj l) = Partition.size l := sz_conj l hl
  rw [conjugate_eq_conj l hl, qDim_eq_prod, qDim_eq_prod, hnum, e1, e2, qHookProd_conj q l hl]

/-! ## C2 at the weight level — the q-Plancherel weight `W_λ = W_{λ′}` -/

/-- The **q-Plancherel weight** of a partition `λ ⊢ n`: `W_λ = d_q(λ)² / [n]_q!`.  This is the
quantity whose conjugation symmetry `W_λ = W_{λ′}` is the s5-so3 keystone's necessary condition
C2 (the weight is *chirality-blind*). -/
noncomputable def qPlancherelWeight (q : ℝ) (lam : Partition) : ℝ :=
  qDim q lam ^ 2 / qFactorial q (Partition.size lam)

/-- **Keystone necessary condition C2 (weight level): `W_λ = W_{λ′}`.**  The q-Plancherel weight is
transpose-invariant — the direct corollary of `qDim_conj` (the q-dimension `d_q` is transpose-
invariant) and `sz_conj` (`|λ′| = |λ|`, so the `[n]_q!` normaliser is unchanged).  This is the
keystone's chirality-blindness of the weight, now Lean-proved for the genuine q-weight at any real
`q` (no fit, no `q₀`). -/
theorem qPlancherelWeight_conj (q : ℝ) (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    qPlancherelWeight q (Partition.conjugate l) = qPlancherelWeight q l := by
  unfold qPlancherelWeight
  rw [qDim_conj q l hl, conjugate_eq_conj l hl,
    show Partition.size (conj l) = Partition.size l from sz_conj l hl]

end QOU.BraidKnot.IdentityI
