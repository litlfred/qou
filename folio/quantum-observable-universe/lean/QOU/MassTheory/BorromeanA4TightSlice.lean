/-
# QOU.MassTheory.BorromeanA4TightSlice — the A=4 exact-order slice, PROVED (bean qou-v7ro)

`MilnorOrderLawGeneral.lean` proves the A=3 slice of the Milnor exact-order conjecture
(`borromean_tight_slice`: `1 − τ_Borr = h^{2(3−1)}·cofactor`, `cofactor 0 = 3/4 ≠ 0`) but
carries A=4 only as a **measured** value (`tauL4Measured := 1.000145898`, "no theorem asserts
`= 6`"). This file upgrades A=4 from measured to **proved**, in the SAME convention as the A=3
object (convention D — the Jones / Temperley–Lieb / SU(2) Markov trace: signed `χ_λ`,
weights `y_{(a,b)} = [a−b+1]_q/[2]_q^n`, only the ≤2-row diagrams contributing — the frame in
which `tauBorromean` is proved, `BorromeanFrobeniusReconstruction.lean`).

**The closed form** (derived exact-symbolic over ℚ(q), 0-fit, no float64; witness
`computations/deltalambda/milnor-a4-deficit-h-form.witness.json`): with `h = q − 1/q`,

    τ_4(h) = (h¹⁰ + 5h⁸ + 6h⁶ + h² + 4)/(h² + 4),
    1 − τ_4 = h⁶ · (−h⁴ − 5h² − 6)/(h² + 4) = −h⁶·(h²+2)(h²+3)/(h²+4).

So the deficit has exact order `6 = 2(4−1)` with leading coefficient `−6/4 = −3/2`, matching
the measured `μ̄_4 = (3/4)(−2)^{4−3} = −3/2` (relerr 2.6e-7, #4480) and the producer's exact
`−96` in the `(q−1)` variable (`h ≈ 2(q−1)` at `q=1`, `−96/2⁶ = −3/2`). The negative sign is
the `(−1)^{A−1}` parity law (A=4 ⇒ `τ_4 > 1`, deficit `< 0`).

**Scope (STRICT).** This is the A=4 *slice*, exactly as `borromean_tight_slice` is the A=3
slice — NOT an instance of `MilnorExactOrderConjecture` (∀A), which stays open and needs the
Bar-Natan / Habegger–Masbaum weight-system bridge Mathlib lacks. Two proved points do not make
a universal law; no instance is fabricated. The convention-D value `τ_4(q₀) = 1.0001284…`
differs from the production `|χ|`-convention measurement `1.000145898` at subleading order —
they agree at the leading Milnor order/coefficient (the topological μ̄), which is what the
slice claims.
-/
import QOU.MassTheory.MilnorOrderLawGeneral

namespace QOU.MassTheory.MilnorOrderLawGeneral

/-- The A=4 Brunnian `H₄` Markov-trace closed form in convention D (derived, not measured):
`τ_4(h) = (h¹⁰ + 5h⁸ + 6h⁶ + h² + 4)/(h² + 4)`. Sibling of `tauBorromean`. -/
noncomputable def tauL4 (h : ℝ) : ℝ :=
  (h ^ 10 + 5 * h ^ 8 + 6 * h ^ 6 + h ^ 2 + 4) / (h ^ 2 + 4)

/-- Trace-deficit closed form: `1 − τ_4 = h^{leadingOrder 4}·(−h⁴−5h²−6)/(h²+4) =
h⁶·(−h⁴−5h²−6)/(h²+4)`. -/
theorem borromean4_deficit_factor (h : ℝ) :
    1 - tauL4 h = h ^ (leadingOrder 4) * ((-h ^ 4 - 5 * h ^ 2 - 6) / (h ^ 2 + 4)) := by
  rw [leadingOrder_four]
  have hd : (h : ℝ) ^ 2 + 4 ≠ 0 := by positivity
  unfold tauL4
  field_simp
  ring

/-- The A=4 cofactor is nonzero at `h = 0` (`= −3/2`): the order is **exactly** 6, not an
accidental higher vanishing — the lower bound `2(4−1)=6` is TIGHT. -/
theorem borromean4_cofactor_ne_zero_at_zero :
    (-(0 : ℝ) ^ 4 - 5 * (0 : ℝ) ^ 2 - 6) / ((0 : ℝ) ^ 2 + 4) ≠ 0 := by norm_num

/-- **A=4 exact-order slice, PROVED.**  The A=4 slice of the general exact-order conjecture
(`MilnorOrderLawGeneral §5`) holds: a nonzero leading coefficient `r = −3/2` and a cofactor
with `D_4 h = h^{2(4−1)}·cofactor h`, `cofactor 0 = r ≠ 0`.  Same shape as `borromean_tight_slice`
(A=3); together they are the two proved points of the still-open `MilnorExactOrderConjecture`. -/
theorem borromean4_tight_slice :
    ∃ (cofactor : ℝ → ℝ) (r : ℝ), r ≠ 0 ∧ cofactor 0 = r ∧
      ∀ h, (1 - tauL4 h) = h ^ (2 * (4 - 1)) * cofactor h := by
  refine ⟨fun h => (-h ^ 4 - 5 * h ^ 2 - 6) / (h ^ 2 + 4), -3 / 2, by norm_num, by norm_num,
    fun h => ?_⟩
  have := borromean4_deficit_factor h
  rwa [leadingOrder_four] at this

/-- **Strict positivity of the `A = 4` trace excess away from `h = 0` (`1 < tauL4 h`,
    `bean qou-okh4`).** Because `A = 4` has `(−1)^(A−1) = −1`, the deficit `1 − tauL4 h`
    is strictly negative for every `h ≠ 0`, so `tauL4 h > 1`. -/
theorem one_lt_tauL4_of_ne_zero (h : ℝ) (hh : h ≠ 0) : 1 < tauL4 h := by
  have hd : (0 : ℝ) < h ^ 2 + 4 := by positivity
  have h6 : (0 : ℝ) < h ^ 6 := by positivity
  have hnum : (0 : ℝ) < h ^ 6 * (h ^ 4 + 5 * h ^ 2 + 6) := by positivity
  have hdiff : tauL4 h - 1 = (h ^ 6 * (h ^ 4 + 5 * h ^ 2 + 6)) / (h ^ 2 + 4) := by
    unfold tauL4
    have hd_ne : (h : ℝ) ^ 2 + 4 ≠ 0 := ne_of_gt hd
    field_simp
    ring
  have hpos : 0 < tauL4 h - 1 := by
    rw [hdiff]
    exact div_pos hnum hd
  linarith

/-- **Strict negativity of the `A = 4` trace deficit away from `h = 0` (`1 - tauL4 h < 0`).** -/
theorem borromean4_deficit_neg_of_ne_zero (h : ℝ) (hh : h ≠ 0) :
    1 - tauL4 h < 0 := by
  have hlt : 1 < tauL4 h := one_lt_tauL4_of_ne_zero h hh
  linarith

end QOU.MassTheory.MilnorOrderLawGeneral
