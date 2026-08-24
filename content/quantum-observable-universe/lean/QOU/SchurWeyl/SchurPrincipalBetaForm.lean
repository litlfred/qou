import QOU.Mathlib.RowLenAddCell
import QOU.Mathlib.SYTBetaGapVandermonde

/-!
# QOU.SchurWeyl.SchurPrincipalBetaForm — both sides of `schurPrincipal` in β-form

`ContentProductRows` and `SYTBetaGapVandermonde` express the numerator and the denominator of
`QBeta.WenzlWeight.schurPrincipal` in terms of `descFactF` at the β-numbers.  They index differently
— the hook side by a **List** over `range |l|`, the content side by a **Finset** over `range r` —
and they measure β against different things.  This file lands both on one common form, `betaR`.

| | |
|---|---|
| `paddedRowLens r μ` | `μ.rowLens` extended with empty rows to length `r` |
| `betaR r μ i` | `μ_i + (r − 1 − i)`, the β-number **at `r` rows** |
| `betaNum_paddedRowLens` | `betaNum (paddedRowLens r μ) i = betaR r μ i` |
| `hookSide_betaR` | `∏_c f(h(c)) · ∏_{i<j<r} f(β_i − β_j) = ∏_{i<r} descFactF f β_i` |
| `contentSide_betaR` | `∏_c f(r − c₁ + c₂) · ∏_{i<r} descFactF f (r−1−i) = ∏_{i<r} descFactF f β_i` |
| `contentProd_mul_descFactF_eq` | the two, equated — the `∏_i descFactF f β_i` cancels |
| `schurPrincipal_mul_const` | **`s_μ · C = Q^{n(μ)} · ∏_{i<j<r}(1 − Q^{β_i−β_j})`**, `C` independent of `μ` |

The last row is the point: the right-hand sides are *the same product*, so the numerator over the
denominator is the Vandermonde `∏_{i<j} f(β_i − β_j)` over the **`μ`-independent** constant
`∏_{i<r} descFactF f (r−1−i)`.  In a ratio of two diagrams that constant cancels outright.

## Base ring (§7c)

Generic `[CommMonoid M]` for the shape lemmas.  No `ℝ`, no ordering.

LaTeX label: `lem:schur-principal-beta-form`
-/

namespace QOU.SchurWeyl

open YoungDiagram Finset QOU.Mathlib.SYTBeta

variable {M : Type*} [CommMonoid M]

/-- `μ.rowLens` extended with empty rows to length `r`. -/
def paddedRowLens (r : ℕ) (μ : YoungDiagram) : List ℕ :=
  μ.rowLens ++ List.replicate (r - μ.rowLens.length) 0

/-- The β-number of row `i` **at `r` rows**: `μ_i + (r − 1 − i)`. -/
def betaR (r : ℕ) (μ : YoungDiagram) (i : ℕ) : ℕ := μ.rowLen i + (r - 1 - i)

theorem length_paddedRowLens {r : ℕ} {μ : YoungDiagram} (hr : μ.colLen 0 ≤ r) :
    (paddedRowLens r μ).length = r :=
  length_append_replicate_zero _ r (by rwa [length_rowLens])

theorem getD_paddedRowLens (r : ℕ) (μ : YoungDiagram) (i : ℕ) :
    (paddedRowLens r μ).getD i 0 = μ.rowLen i := by
  rw [paddedRowLens, getD_append_replicate_zero, getD_rowLens]

theorem sorted_paddedRowLens (r : ℕ) (μ : YoungDiagram) :
    List.Sorted (· ≥ ·) (paddedRowLens r μ) :=
  sorted_append_replicate_zero μ.rowLens_sorted _

theorem betaNum_paddedRowLens {r : ℕ} {μ : YoungDiagram} (hr : μ.colLen 0 ≤ r) (i : ℕ) :
    betaNum (paddedRowLens r μ) i = betaR r μ i := by
  rw [betaNum, getD_paddedRowLens, length_paddedRowLens hr, betaR]

theorem prodHooksF_paddedRowLens (f : ℕ → M) (r : ℕ) (μ : YoungDiagram) :
    prodHooksF f (paddedRowLens r μ) = prodHooksF f μ.rowLens :=
  prodHooksF_append_replicate_zero f _ _

/-- **The hook side, in `betaR` form.** -/
theorem hookSide_betaR (f : ℕ → M) {r : ℕ} {μ : YoungDiagram} (hr : μ.colLen 0 ≤ r) :
    (∏ c ∈ μ.cells, f (QOU.QBeta.WenzlWeight.hook μ c)) *
        (∏ i ∈ Finset.range r, ∏ k ∈ Finset.range (r - (i + 1)),
          f (betaR r μ i - betaR r μ (i + 1 + k)))
      = ∏ i ∈ Finset.range r, descFactF f (betaR r μ i) := by
  have hlen := length_paddedRowLens hr
  have hkey := prodHooksF_mul_pair_prod f (paddedRowLens r μ) (sorted_paddedRowLens r μ)
  rw [hlen] at hkey
  rw [prodHooksF_rowLens_wenzl f μ, ← prodHooksF_paddedRowLens f r μ]
  rw [show (∏ i ∈ Finset.range r, ∏ k ∈ Finset.range (r - (i + 1)),
        f (betaR r μ i - betaR r μ (i + 1 + k)))
      = ∏ i ∈ Finset.range r, ∏ k ∈ Finset.range (r - (i + 1)),
        f (betaNum (paddedRowLens r μ) i - betaNum (paddedRowLens r μ) (i + 1 + k)) from
      Finset.prod_congr rfl fun i _ => Finset.prod_congr rfl fun k _ => by
        rw [betaNum_paddedRowLens hr, betaNum_paddedRowLens hr]]
  rw [hkey, list_range_map_prod']
  refine Finset.prod_congr rfl fun i hi => ?_
  rw [Finset.mem_range] at hi
  rw [getD_paddedRowLens, List.length_drop, hlen, betaR]
  congr 1
  omega

/-- **The content side, in `betaR` form.** -/
theorem contentSide_betaR (f : ℕ → M) {r : ℕ} {μ : YoungDiagram} (hr : μ.colLen 0 ≤ r) :
    (∏ c ∈ μ.cells, f (r - c.1 + c.2)) * (∏ i ∈ Finset.range r, descFactF f (r - 1 - i))
      = ∏ i ∈ Finset.range r, descFactF f (betaR r μ i) := by
  rw [prodContentF_mul_descFactF f r μ hr]
  refine Finset.prod_congr rfl fun i hi => ?_
  rw [Finset.mem_range] at hi
  rw [betaR]
  congr 1
  omega

/-- **The two sides, equated.**

`∏_c f(r − c₁ + c₂) · ∏_{i<r} descFactF f (r−1−i) = ∏_c f(h(c)) · ∏_{i<j<r} f(β_i − β_j)`.

Both equal `∏_{i<r} descFactF f β_i`, which therefore cancels: the numerator over the denominator is
the Vandermonde over a **`μ`-independent** constant. -/
theorem contentProd_mul_descFactF_eq (f : ℕ → M) {r : ℕ} {μ : YoungDiagram}
    (hr : μ.colLen 0 ≤ r) :
    (∏ c ∈ μ.cells, f (r - c.1 + c.2)) * (∏ i ∈ Finset.range r, descFactF f (r - 1 - i))
      = (∏ c ∈ μ.cells, f (QOU.QBeta.WenzlWeight.hook μ c)) *
          (∏ i ∈ Finset.range r, ∏ k ∈ Finset.range (r - (i + 1)),
            f (betaR r μ i - betaR r μ (i + 1 + k))) := by
  rw [contentSide_betaR f hr, hookSide_betaR f hr]

/-! ## The closed form -/

/-- **`schurPrincipal` in Vandermonde form, division-free.**

`s_μ(1,Q,…,Q^{r−1}) · ∏_{i<r} descFactF (1−Qⁿ) (r−1−i) = Q^{n(μ)} · ∏_{i<j<r} (1 − Q^{β_i−β_j})`.

The left-hand constant does **not** depend on `μ` — it is the empty-partition contribution — so in a
ratio of two diagrams it cancels outright, leaving `Q^{n(ν)−n(μ)}` times a ratio of Vandermondes.
That is the branching ratio, and the remaining work is to identify `∏_{i<j}(1 − Q^{β_i−β_j})` with
`vandPairProd r (fun i => Q^{β_i})` up to a monomial.

The only hypothesis beyond `μ` having at most `r` rows is that the hook product is nonzero — the
same genericity `schurPrincipal_eq_zero_iff` already carries, and exactly what makes the
`schurPrincipal` quotient well-posed in the first place. -/
theorem schurPrincipal_mul_const {R : Type*} [Field R] (Q : R) {r : ℕ} {μ : YoungDiagram}
    (hr : μ.colLen 0 ≤ r)
    (hD : (∏ c ∈ μ.cells, (1 - Q ^ QOU.QBeta.WenzlWeight.hook μ c)) ≠ 0) :
    QOU.QBeta.WenzlWeight.schurPrincipal r Q μ
        * (∏ i ∈ Finset.range r, descFactF (fun n => 1 - Q ^ n) (r - 1 - i))
      = Q ^ QOU.QBeta.WenzlWeight.nPart μ
          * ∏ i ∈ Finset.range r, ∏ k ∈ Finset.range (r - (i + 1)),
              (1 - Q ^ (betaR r μ i - betaR r μ (i + 1 + k))) := by
  have hnum : (∏ c ∈ μ.cells, (1 - Q ^ ((r : ℤ) + QOU.QBeta.WenzlWeight.content c)))
      = ∏ c ∈ μ.cells, (1 - Q ^ (r - c.1 + c.2)) :=
    Finset.prod_congr rfl fun c hc => by rw [schurNumExponent hr hc, zpow_natCast]
  have hkey := contentProd_mul_descFactF_eq (fun n => 1 - Q ^ n) hr
  rw [QOU.QBeta.WenzlWeight.schurPrincipal, Finset.prod_div_distrib, hnum]
  field_simp
  linear_combination (Q ^ QOU.QBeta.WenzlWeight.nPart μ) * hkey

end QOU.SchurWeyl
