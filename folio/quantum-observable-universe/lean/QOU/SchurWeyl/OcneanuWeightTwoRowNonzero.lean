/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.OcneanuWeight

/-!
# The Ocneanu weight is NONZERO on the at-most-two-row shapes

`ocneanuWeight_conventionD_eq_zero_of_three_rows` kills every shape with a third
row.  This is the complementary half: at convention `D` the weight of a shape with
**at most** two rows is nonzero, under exactly the genericity `wtrace` already
carries.

## 🛑 This was recorded as blocked on Wenzl's theorem. It is not.

`QOU/SchurWeyl/WtraceRadicalTwoRow.lean` and bean `qou-s7z2` both state that the
`⊆` half of "the radical is the `ℓ(λ) ≥ 3` blocks" needs the ≤2-row weights to be
nonzero, and that the corpus has that only through
`WenzlWeightVanishing.conventionD_ocneanuWeight_eq_zero_iff_of_wenzl`, which is
**conditional on the class `IsOcneanuWeightSystem`** — a class whose own docstring
says an instance *"is exactly Wenzl's theorem, and is exactly what remains
unformalised."*

**That reasoning went through the wrong object.** The class exists to relate an
*opaque* candidate weight `y` to `schurPrincipal`; `ocneanuWeight` is not opaque —
it is a closed form, and the non-vanishing follows from it directly.

## The computation

At `z = q³/(q²+1)` the per-cell numerator factor collapses:

`q^{2i}(q² − 1 − q·z) + q^{2j+1}·z = (q^{2j+4} − q^{2i}) / (q² + 1)`

because `q² − 1 − q⁴/(q²+1) = −1/(q²+1)`.  So the factor vanishes **iff**
`q^{2(c+2)} = 1` where `c = j − i` is the cell's content — which recovers
`ocneanuNumFactor_eq_zero_of_content_neg_two` as the case `c = −2`, and shows
there is nothing else to worry about: for a shape with at most two rows every
cell has `i ≤ 1`, hence content `c ≥ −1`, hence `c + 2 ≥ 1`, and
`(q²)^k ≠ 1` for `k ≥ 1` is `hgen`.

The denominator needs the same hypothesis and nothing more: `hookLength` is
positive on a cell of the diagram, because a cell's own arm contains it.

## What this unblocks

The `⊆` direction of the radical identification at the `wtrace` carrier. The only
remaining inputs are a standard matrix-pairing fact and the block-isolation
construction — neither of which is Wenzl's theorem.
-/

namespace QOU.SchurWeyl

open YoungDiagram

/-- **A cell's hook length is positive** — its own arm contains it. -/
theorem hookLength_pos {mu : YoungDiagram} {c : ℕ × ℕ} (hc : c ∈ mu.cells) :
    0 < hookLength mu c := by
  classical
  have hmem : c ∈ mu.cells.filter (fun d => d.1 = c.1 ∧ c.2 ≤ d.2) := by
    simp [Finset.mem_filter, hc]
  have h1 : 0 < (mu.cells.filter (fun d => d.1 = c.1 ∧ c.2 ≤ d.2)).card :=
    Finset.card_pos.mpr ⟨c, hmem⟩
  simp only [hookLength]
  omega

/-- **The numerator factor at convention `D`, in closed form.**

`q² − 1 − q·z = −1/(q²+1)` at `z = q³/(q²+1)`, which collapses the two terms into
a single difference of powers. -/
theorem ocneanuNumFactor_conventionD {R : Type*} [Field R] (q : R)
    (hq21 : q ^ 2 + 1 ≠ 0) (i j : ℕ) :
    q ^ (2 * i) * (q ^ 2 - 1 - q * (q ^ 3 / (q ^ 2 + 1)))
        + q ^ (2 * j + 1) * (q ^ 3 / (q ^ 2 + 1))
      = (q ^ (2 * j + 4) - q ^ (2 * i)) / (q ^ 2 + 1) := by
  field_simp
  ring

/-- **The numerator factor is nonzero off content `−2`**, given `hgen`.

`i ≤ j + 1` is what an at-most-two-row shape supplies (`i ≤ 1 ≤ j + 1`); it makes
the exponent gap `j + 2 - i` positive, and `hgen` does the rest. -/
theorem ocneanuNumFactor_conventionD_ne_zero {R : Type*} [Field R] (q : R)
    (hq0 : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℕ, 0 < k → (q ^ 2 : R) ^ k ≠ 1) (i j : ℕ) (hij : i ≤ j + 1) :
    q ^ (2 * i) * (q ^ 2 - 1 - q * (q ^ 3 / (q ^ 2 + 1)))
        + q ^ (2 * j + 1) * (q ^ 3 / (q ^ 2 + 1)) ≠ 0 := by
  rw [ocneanuNumFactor_conventionD q hq21 i j]
  refine div_ne_zero ?_ hq21
  have hsplit : q ^ (2 * j + 4) - q ^ (2 * i)
      = q ^ (2 * i) * ((q ^ 2) ^ (j + 2 - i) - 1) := by
    rw [mul_sub, mul_one, ← pow_mul, ← pow_add]
    congr 2
    omega
  rw [hsplit]
  exact mul_ne_zero (pow_ne_zero _ hq0)
    (sub_ne_zero_of_ne (hgen _ (by omega)))

/-- **At most two rows means every cell has `i ≤ 1`.** -/
theorem row_le_one_of_rowLen_two_eq_zero {mu : YoungDiagram} (h : mu.rowLen 2 = 0)
    {c : ℕ × ℕ} (hc : c ∈ mu.cells) : c.1 ≤ 1 := by
  by_contra hlt
  have h2 : (2, c.2) ∈ mu := mu.up_left_mem (by omega) le_rfl hc
  rw [mem_iff_lt_rowLen, h] at h2
  omega

/-- **The Ocneanu weight is nonzero on the at-most-two-row shapes** at convention
`D`, under exactly the genericity `wtrace` already carries.

Complementary to `ocneanuWeight_conventionD_eq_zero_of_three_rows`, and — see the
module docstring — **not** conditional on Wenzl's theorem. -/
theorem ocneanuWeight_conventionD_ne_zero_of_two_rows {R : Type*} [Field R] (q : R)
    (hq0 : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℕ, 0 < k → (q ^ 2 : R) ^ k ≠ 1)
    (mu : YoungDiagram) (h : mu.rowLen 2 = 0) :
    ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) mu ≠ 0 := by
  rw [ocneanuWeight]
  refine div_ne_zero (Finset.prod_ne_zero_iff.mpr ?_) (Finset.prod_ne_zero_iff.mpr ?_)
  · intro c hc
    exact ocneanuNumFactor_conventionD_ne_zero q hq0 hq21 hgen c.1 c.2
      (le_trans (row_le_one_of_rowLen_two_eq_zero h hc) (by omega))
  · intro c hc
    refine sub_ne_zero_of_ne ?_
    rw [pow_mul]
    exact hgen _ (hookLength_pos hc)

end QOU.SchurWeyl
