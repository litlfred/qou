/-
# Wenzl level-integer stratum vanishing

The Jones–Wenzl principal specialisation used throughout the mass/binding compute,

  `s_λ(1, Q, …, Q^{r-1}) = Q^{n(λ)} · ∏_{x ∈ λ} (1 - Q^{r + c(x)}) / ∏_{x ∈ λ} (1 - Q^{h(x)})`,

carries the numerator factor `∏_{x ∈ λ} (1 - Q^{r + c(x)})`, where `c(i,j) = j - i`
is the **content** of the cell `(i,j)`.  This file proves the exact combinatorial
fact that governs the *level-integer ladder*:

  **a partition with strictly more than `k` rows always has a cell of content `-k`.**

Consequently, at integer level `r = k` that cell contributes the factor
`1 - Q^(k + (-k)) = 1 - Q^0 = 0`, so the **entire `ℓ(λ) > k` stratum is
annihilated** — for any `Q`, in any field.

Why this matters (stated without over-claiming): the effective level `r` of the
substrate specialisation tends to `2` in the combinatorial limit, so this lemma is
the reason the `ℓ(λ) ≥ 3` stratum *degenerates* there, and the reason a ladder of
level-integer points exists at all.

**Scope.**  These are statements about partitions and about a formal product over
contents.  They are NOT statements about any binding energy, about `Δ_λ`, or about
where any sign crossing sits; nothing here evaluates the substrate modulus, and
nothing here is evidence for a physical magnitude.  Base ring is a generic
`Field K` (§7c) — needed only because the exponent `k + c` is an *integer* and may
be negative; no ordering, no archimedean construct, and in particular no `ℝ`.
-/
import Mathlib.Algebra.Field.Defs
import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Data.List.Basic

namespace QOU.BraidsAndKnots

/-- A list containing `0` has zero product.  Proved here rather than cited so the
file depends on no unstable lemma name. -/
private theorem prod_eq_zero_of_mem_zero {M : Type*} [MonoidWithZero M] :
    ∀ {l : List M}, (0 : M) ∈ l → l.prod = 0
  | _ :: rest, h => by
      rcases List.mem_cons.mp h with h1 | h2
      · simp [List.prod_cons, ← h1]
      · simp [List.prod_cons, prod_eq_zero_of_mem_zero h2]

/-- Contents `c(i,j) = j - i` of the cells of the rows `lam`, where the first row of
`lam` is row index `i`.  A row of length `len` contributes `len` cells with contents
`0 - i, 1 - i, …, (len-1) - i`. -/
def contentsFrom : ℕ → List ℕ → List ℤ
  | _, [] => []
  | i, len :: rest =>
      ((List.range len).map (fun j : ℕ => (j : ℤ) - (i : ℤ))) ++ contentsFrom (i + 1) rest

/-- Contents of a partition presented as its list of row lengths. -/
def partitionContents (lam : List ℕ) : List ℤ := contentsFrom 0 lam

/-- **Level-integer vanishing law, combinatorial half (indexed form).**
If every row of `lam` is nonempty, then row `k` of the block starting at index `i`
supplies a cell of content `-(i + k)`. -/
theorem neg_mem_contentsFrom
    (lam : List ℕ) (hpos : ∀ x ∈ lam, 0 < x) (i k : ℕ) (hk : k < lam.length) :
    (-((i : ℤ) + (k : ℤ))) ∈ contentsFrom i lam := by
  induction lam generalizing i k with
  | nil => simp at hk
  | cons len rest ih =>
    cases k with
    | zero =>
      -- the first cell of the current row has content `0 - i = -(i + 0)`
      have hlen : 0 < len := hpos len (List.mem_cons_self ..)
      have h0 : (0 : ℕ) ∈ List.range len := List.mem_range.mpr hlen
      have hmap : ((0 : ℕ) : ℤ) - (i : ℤ)
          ∈ (List.range len).map (fun j : ℕ => (j : ℤ) - (i : ℤ)) :=
        List.mem_map.mpr ⟨0, h0, rfl⟩
      have he : ((0 : ℕ) : ℤ) - (i : ℤ) = -((i : ℤ) + ((0 : ℕ) : ℤ)) := by omega
      rw [he] at hmap
      exact List.mem_append_left _ hmap
    | succ k' =>
      -- recurse into the remaining rows, whose block index is `i + 1`
      have hk' : k' < rest.length := by
        simpa [List.length_cons, Nat.succ_lt_succ_iff] using hk
      have hpos' : ∀ x ∈ rest, 0 < x := fun x hx => hpos x (List.mem_cons_of_mem _ hx)
      have h := ih hpos' (i + 1) k' hk'
      have he : (-(((i + 1 : ℕ) : ℤ) + (k' : ℤ))) = (-((i : ℤ) + ((k' + 1 : ℕ) : ℤ))) := by
        omega
      exact List.mem_append_right _ (he ▸ h)

/-- **Level-integer vanishing law, combinatorial half.**
A partition with strictly more than `k` rows — all rows nonempty — has a cell of
content `-k`, namely the first cell of row `k`.

The positivity hypothesis is essential, not decorative: for `lam = [3, 0]` and
`k = 1`, row `1` is empty and `-1` is *not* a content (checked below). -/
theorem neg_mem_partitionContents_of_lt_length
    (lam : List ℕ) (hpos : ∀ x ∈ lam, 0 < x) (k : ℕ) (hk : k < lam.length) :
    (-(k : ℤ)) ∈ partitionContents lam := by
  have := neg_mem_contentsFrom lam hpos 0 k hk
  simpa [partitionContents] using this

/-- **Level-integer vanishing law, algebraic half.**
At integer level `k`, the principal-specialisation numerator
`∏_{x ∈ λ} (1 - Q^(k + c(x)))` vanishes for every partition with strictly more than
`k` rows — for *any* `Q` in *any* field, including `Q = 0`.

This is the exact statement that generates the level-integer ladder: raising the
level past `k` is what re-admits the `(k+1)`-row stratum. -/
theorem principalSpec_numerator_eq_zero_of_lt_length
    {K : Type*} [Field K] (Q : K)
    (lam : List ℕ) (hpos : ∀ x ∈ lam, 0 < x) (k : ℕ) (hk : k < lam.length) :
    ((partitionContents lam).map (fun c => 1 - Q ^ ((k : ℤ) + c))).prod = 0 := by
  refine prod_eq_zero_of_mem_zero (List.mem_map.mpr ⟨-(k : ℤ), ?_, ?_⟩)
  · exact neg_mem_partitionContents_of_lt_length lam hpos k hk
  · simp

/-! ### Non-vacuity guards

Machine-checked evidence that the positivity hypothesis is load-bearing rather than
decorative: dropping it makes the statement FALSE. -/

/-- With an empty row, `-1` is genuinely absent from the contents — so
`neg_mem_partitionContents_of_lt_length` really does need `hpos`. -/
example : (-(1 : ℤ)) ∉ partitionContents [3, 0] := by decide

/-- With all rows nonempty, `-1` is present, as the theorem asserts. -/
example : (-(1 : ℤ)) ∈ partitionContents [3, 2] := by decide

end QOU.BraidsAndKnots
