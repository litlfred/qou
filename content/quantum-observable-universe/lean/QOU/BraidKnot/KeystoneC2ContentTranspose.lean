import QOU.BraidKnot.IdentityIContentDecomposition

/-!
# Keystone C2 — transpose-invariance of the content & hook sums (Σ-core of `W_λ = W_{λ'}`)

The s5-so3 keystone's **necessary condition C2** is the conjugation symmetry of the q-Plancherel
weight `W_λ = d_q(λ)²/[n]_q!`, i.e. `W_λ = W_{λ'}` under transpose `λ ↦ λ'`.  On the QOU side this
is the **chirality flip** (content `c(i,j) = j − i` negates under transpose), so C2 says the weight
is chirality-blind.

`KeystoneChiralityInvolution.lean` machine-checks C2 at the **cell / example** level (the single-cell
`cellContent_transpose_neg`, the self-conjugate electron `(3,1,1)`).  The **global** statement is the
transpose-invariance of the symmetric content / hook data — which this file establishes at the
**Σ-level** for **both** the squared-content and squared-hook sums, in the same self-contained
`List ℕ` model as
`IdentityIContentDecomposition` (no `Mathlib.YoungDiagram`), reusing that file's column-length
duality and `cell_fubini` transpose.

* `conj` — the transpose of a partition in the `List ℕ` model: row `j` of the conjugate is the
  `j`-th column length `colLen l j`.  (For a weakly-decreasing `l` this is exactly
  `MathlibExt.QPartitionCombinatorics.Partition.conjugate`, whose mapping function
  `(l.filter (· > j)).length` is definitionally `colLen l j`.)
* `sumSqContents_conj` — **the content-square sum is transpose-invariant**:
  `Σ_c c(c)² (λ') = Σ_c c(c)² (λ)`.  Since content negates under transpose and squaring kills the
  sign, the per-cell summand is preserved and `cell_fubini` matches the cell sets.  This is the
  chirality-blindness of `Σ c²` — the Σ-core of C2 for the content moment that the keystone defect
  cubic and the Plancherel mean are built from.
* `colLen_conj` + `sumSqHooks_conj` — **the hook-square sum is transpose-invariant**:
  `Σ_c h_c² (λ') = Σ_c h_c² (λ)`.  The hook is transpose-symmetric (`h_λ(i,j) = h_{λ'}(j,i)`), via the
  column-length **involution** `colLen (conj l) c = λ_c`.  This is the moment that feeds `d_q(λ)` and
  hence `W_λ = W_{λ'}` directly, so the two results together give the full Σ-core of C2.

Base ring `ℤ`; nothing archimedean (no `q₀`).  No fit.
-/

namespace QOU.BraidKnot.IdentityI

open Finset

/-- **Transpose (conjugate) of a partition** in the `List ℕ` model: row `j` of the conjugate is the
`j`-th column length `colLen l j`, for `j` ranging over the columns `[0, λ_1)`.  For a
weakly-decreasing `l` this coincides with `Partition.conjugate l`. -/
def conj (l : List ℕ) : List ℕ := (List.range (l.headD 0)).map (colLen l)

/-- The conjugate has one row per column of `l`. -/
@[simp] theorem conj_length (l : List ℕ) : (conj l).length = l.headD 0 := by
  simp [conj]

/-- Row `j` of the conjugate is the `j`-th column length (for `j` a genuine column). -/
theorem conj_getD (l : List ℕ) (j : ℕ) (hj : j < l.headD 0) :
    (conj l).getD j 0 = colLen l j := by
  simp only [conj, List.getD_eq_getElem?_getD, List.getElem?_map, List.getElem?_range hj,
    Option.map_some, Option.getD_some]

/-- **C2, Σ-level (content moment): the squared-content sum is transpose-invariant.**
`Σ_{c ∈ λ'} c(c)² = Σ_{c ∈ λ} c(c)²` for any weakly-decreasing partition.  Content negates under
transpose (`c(i,j) = j − i ↦ i − j`); squaring kills the sign, so the per-cell summand is preserved,
and `cell_fubini` (the column-length duality of `IdentityIContentDecomposition`) matches the
row-indexed cells of `λ` with the column-indexed cells of `λ'`. -/
theorem sumSqContents_conj (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    sumSqContents (conj l) = sumSqContents l := by
  -- Expand both sides to Finset double sums over the cell index sets.
  unfold sumSqContents
  simp_rw [list_range_map_sum]
  -- LHS: rows of `conj l` (length = headD), each of width `colLen l r`.
  rw [conj_length]
  have hL : ∀ r ∈ Finset.range (l.headD 0),
      (∑ c ∈ Finset.range ((conj l).getD r 0), ((c : ℤ) - (r : ℤ)) ^ 2)
        = ∑ c ∈ Finset.range (colLen l r), ((c : ℤ) - (r : ℤ)) ^ 2 := by
    intro r hr; rw [conj_getD l r (Finset.mem_range.mp hr)]
  rw [Finset.sum_congr rfl hL]
  -- The goal's RHS is exactly `cell_fubini`'s row-indexed LHS for `g i j = (j − i)²`; rewrite it to
  -- the column-indexed form, which matches the conjugate's `(c − r)²` cell sum (equal by neg square).
  rw [cell_fubini l hl (fun i j => ((j : ℤ) - (i : ℤ)) ^ 2)]
  apply Finset.sum_congr rfl; intro j _; apply Finset.sum_congr rfl; intro i _
  ring

/-! ## The hook moment — completing the C2 Σ-core

`sumSqHooks` is likewise transpose-invariant, the moment that enters `d_q(λ)` and hence
`W_λ = W_{λ'}` directly.  The extra ingredient beyond the content case is the column-length
**involution** `colLen (conj l) c = λ_c` (conjugate-of-conjugate), proved below from the existing
indicator-sum / duality / `min` machinery; the hook then matches under transpose
(`h_λ(i,j) = h_{λ'}(j,i)`) and `cell_fubini` finishes. -/

/-- **Column-length involution.** The `c`-th column length of the conjugate is the `c`-th part of
`l`: `colLen (conj l) c = λ_c`.  Proof: `colLen (conj l) c = #{r < λ_1 : c < colLen l r}`
(`colLen_eq_indicator_sum` + `conj_getD`), then `c < colLen l r ↔ r < λ_c` (`colLen_duality`), and
`#{r < λ_1 : r < λ_c} = min λ_1 λ_c = λ_c` (`sum_indicator_lt_eq_min` + `getD_le_headD`). -/
theorem colLen_conj (l : List ℕ) (hl : l.Sorted (· ≥ ·)) (c : ℕ) :
    colLen (conj l) c = l.getD c 0 := by
  rw [colLen_eq_indicator_sum, conj_length]
  have hcongr : ∀ k ∈ Finset.range (l.headD 0),
      (if c < (conj l).getD k 0 then (1 : ℕ) else 0) = (if k < l.getD c 0 then 1 else 0) := by
    intro k hk
    rw [conj_getD l k (Finset.mem_range.mp hk)]
    simp only [colLen_duality l hl c k]
  rw [Finset.sum_congr rfl hcongr, sum_indicator_lt_eq_min]
  exact min_eq_right (getD_le_headD l hl c)

/-- **C2, Σ-level (hook moment): the squared-hook sum is transpose-invariant.**
`Σ_c h_c² (λ') = Σ_c h_c² (λ)`.  The hook is transpose-symmetric (`h_λ(i,j) = h_{λ'}(j,i)`): the
conjugate's hook at `(r,c)` is `(colLen l r − c) + (λ_c − r) − 1`, equal — commuting arm and leg —
to `l`'s hook at `(c,r)`; `colLen_conj` supplies the leg and `cell_fubini` matches the cell sets.
This is the moment that feeds `d_q(λ)` and thus `W_λ = W_{λ'}` (C2). -/
theorem sumSqHooks_conj (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    sumSqHooks (conj l) = sumSqHooks l := by
  unfold sumSqHooks
  simp_rw [list_range_map_sum]
  rw [conj_length]
  have hL : ∀ r ∈ Finset.range (l.headD 0),
      (∑ c ∈ Finset.range ((conj l).getD r 0),
        ((((conj l).getD r 0 - c) + (colLen (conj l) c - r) - 1 : ℕ) : ℤ) ^ 2)
        = ∑ c ∈ Finset.range (colLen l r),
            (((l.getD c 0 - r) + (colLen l r - c) - 1 : ℕ) : ℤ) ^ 2 := by
    intro r hr
    rw [conj_getD l r (Finset.mem_range.mp hr)]
    apply Finset.sum_congr rfl; intro c _
    rw [colLen_conj l hl c, Nat.add_comm (colLen l r - c) (l.getD c 0 - r)]
  rw [Finset.sum_congr rfl hL,
    cell_fubini l hl (fun i j => (((l.getD i 0 - j) + (colLen l j - i) - 1 : ℕ) : ℤ) ^ 2)]

end QOU.BraidKnot.IdentityI
