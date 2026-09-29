import QOU.Mathlib.HookProductMonoidBridge

/-!
# QOU.Mathlib.ContentProductRows — the content side of the level-`r` specialisation, by rows

`HookProductMonoidBridge` reindexes the **hook** product of a `YoungDiagram` by rows.  This file does
the same for the **content** product — the numerator of `QBeta.WenzlWeight.schurPrincipal`.

| | |
|---|---|
| `rowLen_eq_zero_of_colLen_le` | rows past `colLen 0` are empty |
| `prodContentF_rows` | `∏_{c ∈ μ} f(r − c₁ + c₂) = ∏_{i<r} ∏_{j<rowLen i} f(r − i + j)` |
| `schurNumExponent` | on a cell of an `≤ r`-row diagram, `r + content c` is the natural `r − c₁ + c₂` |
| `prodContentF_rows_one_sub_pow` | the q-instance, in `schurPrincipal`'s own `zpow` form |
| `prodContentF_mul_descFactF` | the content side in `descFactF` form, division-free |

Row `i`'s inner product is a **contiguous block** `f(r−i), f(r−i+1), …, f(r−i+μ_i−1)`, so
`SYTBeta.prod_block_mul_descFactF` turns it into `descFactF f β_i / descFactF f (r−1−i)` — the top
index `r − i + μ_i − 1` **is** `β_i` at `r` rows.  That is the cancellation the hook side is waiting
for.

The outer range is `r`, not `colLen 0`: rows past the last nonzero one contribute an empty product,
which is exactly the zero-padding convention `SYTBetaZeroPadding` fixes for the hook side.

## Base ring (§7c)

Generic `[CommMonoid M]`; the q-instance is over `[Field R]` because `schurPrincipal` is.  Arguments
stay in `ℕ` once `schurNumExponent` has discharged the `zpow`.

LaTeX label: `lem:content-product-rows`
-/

namespace QOU.Mathlib.SYTBeta

open YoungDiagram

variable {M : Type*} [CommMonoid M]

/-- Rows past `colLen 0` are empty. -/
theorem rowLen_eq_zero_of_colLen_le {μ : YoungDiagram} {i : ℕ} (hi : μ.colLen 0 ≤ i) :
    μ.rowLen i = 0 := by
  by_contra h
  have hmem : ((i, 0) : ℕ × ℕ) ∈ μ := mem_iff_lt_rowLen.mpr (Nat.pos_of_ne_zero h)
  exact absurd (mem_iff_lt_colLen.mp hmem) (by omega)

/-- **The content product, reindexed by rows.**

`∏_{c ∈ μ.cells} f(r − c₁ + c₂) = ∏_{i < r} ∏_{j < rowLen i} f(r − i + j)`.

The outer range is `r`, so the statement is already in the zero-padded convention: rows past the last
nonzero one contribute an empty product. -/
theorem prodContentF_rows (f : ℕ → M) (r : ℕ) (μ : YoungDiagram) (hr : μ.colLen 0 ≤ r) :
    ∏ c ∈ μ.cells, f (r - c.1 + c.2)
      = ∏ i ∈ Finset.range r, ∏ j ∈ Finset.range (μ.rowLen i), f (r - i + j) := by
  rw [cells_biUnion' μ, Finset.prod_biUnion (rows_disjoint μ (μ.colLen 0))]
  have hext : ∏ i ∈ Finset.range r, ∏ j ∈ Finset.range (μ.rowLen i), f (r - i + j)
      = ∏ i ∈ Finset.range (μ.colLen 0), ∏ j ∈ Finset.range (μ.rowLen i), f (r - i + j) := by
    rw [← Finset.prod_range_mul_prod_Ico _ hr]
    have hone : ∏ i ∈ Finset.Ico (μ.colLen 0) r,
        ∏ j ∈ Finset.range (μ.rowLen i), f (r - i + j) = 1 := by
      refine Finset.prod_eq_one fun i hi => ?_
      rw [Finset.mem_Ico] at hi
      rw [rowLen_eq_zero_of_colLen_le hi.1]
      simp
    rw [hone, mul_one]
  rw [hext]
  refine Finset.prod_congr rfl fun i _ => ?_
  rw [row_prodF]

/-- On a cell of a diagram with at most `r` rows, `schurPrincipal`'s integer exponent
`r + content c` is the natural number `r − c₁ + c₂`. -/
theorem schurNumExponent {r : ℕ} {μ : YoungDiagram} (hr : μ.colLen 0 ≤ r) {c : ℕ × ℕ}
    (hc : c ∈ μ.cells) :
    (r : ℤ) + QOU.QBeta.WenzlWeight.content c = ((r - c.1 + c.2 : ℕ) : ℤ) := by
  have hmem : (c.1, c.2) ∈ μ := by simpa using (YoungDiagram.mem_cells c).mp hc
  have h1 : c.1 < μ.colLen 0 :=
    lt_of_lt_of_le (mem_iff_lt_colLen.mp hmem) (μ.colLen_anti 0 c.2 (Nat.zero_le _))
  unfold QOU.QBeta.WenzlWeight.content
  have : c.1 ≤ r := by omega
  push_cast [Nat.cast_sub this]
  ring

/-- **The q-instance, in `schurPrincipal`'s own `zpow` form.** -/
theorem prodContentF_rows_one_sub_pow {R : Type*} [Field R] (Q : R) (r : ℕ) (μ : YoungDiagram)
    (hr : μ.colLen 0 ≤ r) :
    ∏ c ∈ μ.cells, (1 - Q ^ ((r : ℤ) + QOU.QBeta.WenzlWeight.content c))
      = ∏ i ∈ Finset.range r, ∏ j ∈ Finset.range (μ.rowLen i), (1 - Q ^ (r - i + j)) := by
  rw [← prodContentF_rows (fun n => 1 - Q ^ n) r μ hr]
  refine Finset.prod_congr rfl fun c hc => ?_
  rw [schurNumExponent hr hc, zpow_natCast]

/-! ## The content side in `descFactF` form -/

/-- **The content side, division-free.**

`∏_{c ∈ μ} f(r − c₁ + c₂) · ∏_{i<r} descFactF f (r−1−i) = ∏_{i<r} descFactF f (r − i + μ_i − 1)`.

The right-hand product is `∏_i descFactF f β_i` at `r` rows — the *same* object the hook side
produces (`SYTBetaGapVandermonde.prodHooksF_mul_pair_prod`).  Dividing the two therefore cancels it,
leaving the Vandermonde over a `μ`-independent constant: exactly the shape the branching ratio needs.

The left-hand correction `∏_{i<r} descFactF f (r−1−i)` is `μ`-independent, so it cancels too when the
ratio of two diagrams is taken. -/
theorem prodContentF_mul_descFactF (f : ℕ → M) (r : ℕ) (μ : YoungDiagram) (hr : μ.colLen 0 ≤ r) :
    (∏ c ∈ μ.cells, f (r - c.1 + c.2)) * ∏ i ∈ Finset.range r, descFactF f (r - 1 - i)
      = ∏ i ∈ Finset.range r, descFactF f (r - i + μ.rowLen i - 1) := by
  rw [prodContentF_rows f r μ hr, ← Finset.prod_mul_distrib]
  refine Finset.prod_congr rfl fun i hi => ?_
  rw [Finset.mem_range] at hi
  rw [show r - 1 - i = (r - i) - 1 from by omega]
  exact prod_block_mul_descFactF f (r - i) (μ.rowLen i) (by omega)

end QOU.Mathlib.SYTBeta
