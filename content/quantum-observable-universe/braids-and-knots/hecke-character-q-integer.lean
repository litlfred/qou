/-
  Hecke character identity: h·[n]_q = qⁿ − q⁻ⁿ.

  The q-integer [n]_q = (qⁿ−q⁻ⁿ)/(q−q⁻¹) satisfies
  h·[n]_q = qⁿ−q⁻ⁿ where h = q−q⁻¹ is the Hecke parameter.

  This is the key identity connecting the Hecke character
  χ_{(2,1)}(σ₁ⁿ) on V_(2,1) to the q-integer tower.

  -- Ref: [jones1987] https://doi.org/10.2307/1971403
-/

import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

namespace QOU.BraidsAndKnots

variable (q : ℝ) (hq : q ≠ 0)

/-- The q-integer [n]_q = (qⁿ−q⁻ⁿ)/(q−q⁻¹). -/
noncomputable def qInteger (n : ℕ) : ℝ := (q^n - q⁻¹^n) / (q - q⁻¹)

/-- h·[n]_q = qⁿ−q⁻ⁿ: the Hecke parameter times the q-integer
  equals the numerator of the q-integer definition. -/
theorem hecke_times_qInteger (n : ℕ) (hh : q - q⁻¹ ≠ 0) :
    (q - q⁻¹) * qInteger q n = q^n - q⁻¹^n := by
  unfold qInteger
  field_simp

/-- [2]_q = q + q⁻¹. -/
theorem qInteger_two (hq : q ≠ 0) (hh : q - q⁻¹ ≠ 0) :
    qInteger q 2 = q + q⁻¹ := by
  unfold qInteger
  field_simp
  ring

/-- [3]_q = q² + 1 + q⁻². -/
theorem qInteger_three (hq : q ≠ 0) (hh : q - q⁻¹ ≠ 0) :
    qInteger q 3 = q^2 + 1 + q⁻¹^2 := by
  unfold qInteger
  field_simp
  ring

/-- The meson mass ratio identity:
  h·[5]_q = q⁵ − q⁻⁵.
  This gives the kaon-to-pion character factor. -/
theorem hecke_times_qInteger_five (hh : q - q⁻¹ ≠ 0) :
    (q - q⁻¹) * qInteger q 5 = q^5 - q⁻¹^5 :=
  hecke_times_qInteger q 5 hh

/-- **q-Lambert single-term identity** (the structural root of the
  Li_2^q simple-pole / branch-point analysis, PRs #1657/#1666).

  `[n]_q · (q − q⁻¹) · q⁻ⁿ = 1 − q⁻²ⁿ`.

  Equivalently `1/[n]_q = (q − q⁻¹)·q⁻ⁿ/(1 − q⁻²ⁿ)`: the inverse
  q-integer is a single geometric (Lambert) kernel in `q⁻²ⁿ`. Summing
  the geometric series gives the Lambert expansion
  `1/[n]_q = (q − q⁻¹)·Σ_{m≥0} q⁻⁽²ᵐ⁺¹⁾ⁿ`, whose `m`-terms each carry a
  simple pole at `z = q^{2m+1}` of the Rogers dilogarithm derivative
  `−ln_q(1−z)/z`. The *simple*-pole order is exactly why `z = q₀` is an
  integrable logarithmic **branch point** (not a pole) of `Li_2^q`, and
  why the `+i0` continuation's imaginary part is the `z`-INDEPENDENT
  residue `π·Res` that cancels in the m_e-normalised ratio
  (`qbeta_li2q_imaginary_quantization.py`, PR #1666 — the reality gate).

  Proof is `field_simp` + `ring` over `ℝ` (algebraic; the pole/branch
  analysis is archimedean, real `q > 0`). -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
theorem qLambert_single_term (n : ℕ) (hh : q - q⁻¹ ≠ 0) :
    qInteger q n * (q - q⁻¹) * q⁻¹^n = 1 - q⁻¹^(2*n) := by
  unfold qInteger
  rw [two_mul, pow_add]
  field_simp
  ring

end QOU.BraidsAndKnots
