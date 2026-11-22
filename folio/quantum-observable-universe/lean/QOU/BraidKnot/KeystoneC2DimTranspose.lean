import QOU.BraidKnot.KeystoneC2ContentTranspose

/-!
# Keystone C2 — transpose-invariance of the SYT dimension (`f^λ = f^{λ'}`)

Capstone of the C2 Σ-core (`KeystoneC2ContentTranspose`): the classical (`q = 1`) case of the
keystone weight symmetry `d_q(λ) = d_q(λ')` ⇒ `W_λ = W_{λ'}`.

The hook-length **product** `∏_c h_c` is transpose-invariant (`prodHooks_conj`, the product analog of
`sumSqHooks_conj`, via a product cell-Fubini `cell_fubini_prod` + the `colLen_conj` involution), and
the size `|λ|` is preserved (`sz_conj`).  Hence the Frame–Robinson–Thrall dimension
`dimHLF λ = |λ|! / ∏_c h_c = #SYT(λ)` satisfies

  `dimHLF (conj l) = dimHLF l`,   i.e.  `f^λ = f^{λ'}`.

This is the `q = 1` specialisation of the genuine keystone identity `d_q(λ) = d_q(λ')`; the full
q-version `qDim (conjugate λ) = qDim λ` lives in `MathlibExt.QPartitionCombinatorics` (a `foldl` /
`get?` model that lacks the column-length duality used here) and is the natural next consumer — it
follows by instantiating `cell_fubini_prod` at the q-bracket of the hook in that model.

Base ring `ℕ`; nothing archimedean (no `q₀`).  No fit.
-/

namespace QOU.BraidKnot.IdentityI

open Finset

/-- List→Finset **product** bridge (product analog of `list_range_map_sum`). -/
theorem list_range_map_prod {M : Type*} [CommMonoid M] (n : ℕ) (f : ℕ → M) :
    ((List.range n).map f).prod = ∏ i ∈ Finset.range n, f i := by
  induction n with
  | zero => simp
  | succ m ih =>
    rw [List.range_succ, List.map_append, List.prod_append, ih, Finset.prod_range_succ]
    simp

/-- List→Finset **sum** bridge over a general `AddCommMonoid` (the file's `list_range_map_sum` is
`ℤ`-only; `sz_conj` below needs the `ℕ` instance). -/
theorem list_range_map_sum_gen {M : Type*} [AddCommMonoid M] (n : ℕ) (f : ℕ → M) :
    ((List.range n).map f).sum = ∑ i ∈ Finset.range n, f i := by
  induction n with
  | zero => simp
  | succ m ih =>
    rw [List.range_succ, List.map_append, List.sum_append, ih, Finset.sum_range_succ]
    simp

/-- **Product cell-Fubini** (product analog of `cell_fubini`): a row-indexed cell product equals the
column-indexed one, via the column-length duality `colLen_duality`. -/
theorem cell_fubini_prod {M : Type*} [CommMonoid M] (l : List ℕ) (hl : l.Sorted (· ≥ ·))
    (g : ℕ → ℕ → M) :
    ∏ i ∈ Finset.range l.length, ∏ j ∈ Finset.range (l.getD i 0), g i j
      = ∏ j ∈ Finset.range (l.headD 0), ∏ i ∈ Finset.range (colLen l j), g i j := by
  apply Finset.prod_comm'
  intro i j
  simp only [Finset.mem_range]
  constructor
  · rintro ⟨hi, hj⟩
    exact ⟨(colLen_duality l hl i j).mpr hj, lt_of_lt_of_le hj (getD_le_headD l hl i)⟩
  · rintro ⟨hi, hj⟩
    exact ⟨lt_of_lt_of_le hi (colLen_le_length l j), (colLen_duality l hl i j).mp hi⟩

/-- **The hook-length product is transpose-invariant**: `∏_c h_c (λ') = ∏_c h_c (λ)`.  Product analog
of `sumSqHooks_conj`: the conjugate's hook at `(r,c)` equals `l`'s hook at `(c,r)` (commute arm/leg
via `colLen_conj`), and `cell_fubini_prod` matches the cell sets. -/
theorem prodHooks_conj (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    prodHooks (conj l) = prodHooks l := by
  unfold prodHooks
  simp only []
  simp_rw [list_range_map_prod]
  rw [conj_length]
  have hL : ∀ r ∈ Finset.range (l.headD 0),
      (∏ c ∈ Finset.range ((conj l).getD r 0),
        ((conj l).getD r 0 - c + (colLen (conj l) c - r) - 1))
        = ∏ c ∈ Finset.range (colLen l r),
            (l.getD c 0 - r + (colLen l r - c) - 1) := by
    intro r hr
    rw [conj_getD l r (Finset.mem_range.mp hr)]
    apply Finset.prod_congr rfl; intro c _
    rw [colLen_conj l hl c, Nat.add_comm (colLen l r - c) (l.getD c 0 - r)]
  rw [Finset.prod_congr rfl hL,
    cell_fubini_prod l hl (fun i j => l.getD i 0 - j + (colLen l j - i) - 1)]

/-- **Size is transpose-invariant**: `|λ'| = |λ|` — both count the cells (`Σ_j colLen l j = Σ_i λ_i`). -/
theorem sz_conj (l : List ℕ) (hl : l.Sorted (· ≥ ·)) : sz (conj l) = sz l := by
  rw [sz, conj, list_range_map_sum_gen, sum_colLen_eq_sum_parts l hl, sum_range_getD_eq_sz]

/-- **C2 capstone (`q = 1`): the SYT dimension is transpose-invariant**, `f^λ = f^{λ'}`.
`dimHLF λ = |λ|! / ∏_c h_c`; both `|λ|` (`sz_conj`) and `∏_c h_c` (`prodHooks_conj`) are
transpose-invariant, so the Frame–Robinson–Thrall dimension is too.  This is the `q = 1`
specialisation of the keystone weight symmetry `W_λ = W_{λ'}` (necessary condition C2). -/
theorem dimHLF_conj (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    dimHLF (conj l) = dimHLF l := by
  rw [dimHLF, dimHLF, sz_conj l hl, prodHooks_conj l hl]

/-- Subtracting the hook-length product of a sorted partition from that of its conjugate yields zero. -/
theorem prodHooks_conj_sub_eq_zero (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    prodHooks (conj l) - prodHooks l = 0 := by
  rw [prodHooks_conj l hl, Nat.sub_self]

end QOU.BraidKnot.IdentityI
