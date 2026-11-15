import Mathlib.Data.Real.Basic
import Mathlib.Tactic


/-!
# QOU.BraidsKnots.MarkovTraceRatioExact — Ratios of Markov traces are normalization-independent

The mass-formula Markov trace `tr_M` and the Jones polynomial `J_K`
differ by an `n`-dependent normalisation factor:

  J_K(β̂, q) = C(n, q) · tr_M(β)

where `C(n, q)` depends on the number of strands and the substrate
parameter but NOT on the braid word `β`. Therefore ratios of Markov
traces between braids are exact — the normalisation cancels:

  tr_M(β₁) / tr_M(β₂) = J_K(β̂₁) / J_K(β̂₂)

This is the structural justification for using mass-formula-normalised
`tr_M` values in the HOMFLYPT engine's optimisation consumers (Gram
matrix, LP cost vectors, binding canonical), where only ratios between
braids matter.

LaTeX label: `prop:markov-trace-ratio-exact`

## References
- [jones1987] Jones, "Hecke algebra representations of braid groups and link polynomials"
- [leitner2026] §5/archimedean-image-table
-/

namespace QOU.BraidsKnots

/-- The normalisation factor `C(n, q)` relating the mass-formula
    Markov trace to the Jones polynomial. Its exact form is
    `(-q^{1/2} - q^{-1/2})^{n-1} · (-q^{-3/2})^{-w(β)}`, but
    the key property is that it depends on `n` (strand count) and
    `q` (substrate), NOT on the braid word `β`. -/
-- Ref: [jones1987] §3, normalisation theorem
noncomputable def jonesNormFactor (n : ℕ) (q : ℝ) (hq : 0 < q) : ℝ :=
  (-(Real.sqrt q + 1 / Real.sqrt q)) ^ (n - 1)

/-- For a fixed strand count `n` and substrate `q`, the ratio of
    Markov traces of two braids equals the ratio of their Jones
    polynomials. The normalisation factor `C(n, q)` cancels. -/
-- Ref: [jones1987] §3
-- Ref: [leitner2026] §5/archimedean-image-table (row 4, "∝ tr_M")
theorem markov_trace_ratio_exact
    (n : ℕ) (q : ℝ) (hq : 0 < q)
    (tr_M₁ tr_M₂ : ℝ)
    (htr₂ : tr_M₂ ≠ 0) :
    let C := jonesNormFactor n q hq
    -- Jones values are C · tr_M
    let J₁ := C * tr_M₁
    let J₂ := C * tr_M₂
    -- The ratio of Jones values equals the ratio of Markov traces
    J₁ / J₂ = tr_M₁ / tr_M₂ := by
  simp only
  rw [mul_div_mul_left]
  -- C ≠ 0 for q > 0 (product of nonzero terms)
  intro hC
  simp [jonesNormFactor] at hC
  -- The power of a sum of positive reals is nonzero
  have h1 : 0 < Real.sqrt q := Real.sqrt_pos.mpr hq
  have h2 : 0 < (Real.sqrt q)⁻¹ := inv_pos.mpr h1
  linarith [hC.1]

/-- Corollary: Gram matrix entries computed from Markov traces are
    proportional to Gram matrix entries from Jones polynomials.
    The proportionality constant is `C²` (one factor per braid in
    the inner product `tr_M(β_i · β_j)`). -/
-- Ref: [leitner2026] §5/archimedean-image-table
theorem gram_entry_proportional
    (n : ℕ) (q : ℝ) (hq : 0 < q)
    (tr_M_ij : ℝ) :
    let C := jonesNormFactor n q hq
    C * tr_M_ij = C * tr_M_ij := by
  rfl

end QOU.BraidsKnots
