import Mathlib.Tactic
import QOU.Nuclear.NucleonDownQuarkStrand

/-!
# A down-letter curl contributes nothing to the framing-corrected mass

Beans `qou-myts`, `qou-99qc`. Owner, 2026-11-27, fork G1 of
`docs/audits/2026-11-27-nucleon-down-quark-strand.md`: read a down letter as a curl on its own
strand (a Markov stabilisation `x·σₙ^{±1}`).

`def:mass-identity` defines the mass of a braid class as the **framing-corrected** trace
`(1 + q²)ⁿ · q^{-n-2w(β)} · tr(ρ(β))`, and `BraidKnotOctonion.MassTraceMarkovClass`
(`jonesTot_isMarkovInvariant`, `massClass`) proves it constant on braid classes. Each
stabilisation adds one strand (factor `(1 + q²)·q⁻¹`, `strandFactor`) and one unit of writhe
(factor `q^{∓2}`, `writheFactor`), and multiplies the raw trace by `z_D` or `z̄_D`.

## What is proved (generic `[Field R]`, no numerical value)

* `curl_pos_cancels`: `(1 + q²)·q⁻¹ · q⁻² · z_D = 1`.
* `curl_neg_cancels`: `(1 + q²)·q⁻¹ · q² · z̄_D = 1`.
* `curl_corrected_ratio_one`: so the framing-corrected weights of an up curl and a down curl are
  equal; the raw ratio `z_D / z̄_D = q⁴` (`curl_ratio`) is exactly the writhe-factor ratio
  `q²/q⁻² = q⁴` (`writhe_ratio_eq_curl_ratio`).

So under the corpus mass, the curl reading of a down letter gives a nucleon split of **zero**:
the `q⁴` of `NucleonDownQuarkStrand.curl_split` is the raw (framed) trace's, and the writhe
correction removes it. The non-zero curl split exists only if the mass is the raw trace, which is
not the corpus definition.

## What is NOT claimed

* Which trace the nucleon mass should use. That is an owner decision (card of 2026-11-27).
* Anything about the through-strand (`K`-weight) reading, which is not a stabilisation.

-- Ref: [leitner2026] folio/quantum-observable-universe/mass-endomorphism/mass-identity.md
-- Ref: [jones1987] https://doi.org/10.2307/1971403 §5 (writhe normalisation of the Markov trace)
-/

namespace QOU.Nuclear.NucleonCurlFramingCancels

open QOU.Nuclear.NucleonDownQuarkStrand

variable {R : Type*} [Field R]

/-- Strand factor of one stabilisation in the framing-corrected trace. -/
def strandF (q : R) : R := (1 + q ^ 2) * q⁻¹

/-- A positive curl: one strand, writhe `+1`, raw factor `z_D`. Net factor `1`. -/
theorem curl_pos_cancels (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    strandF q * (q⁻¹) ^ 2 * zD q = 1 := by
  unfold strandF zD
  have : (1 : R) + q ^ 2 = q ^ 2 + 1 := by ring
  rw [this]
  field_simp

/-- A negative curl: one strand, writhe `−1`, raw factor `z̄_D`. Net factor `1`. -/
theorem curl_neg_cancels (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    strandF q * q ^ 2 * zbarD q = 1 := by
  rw [zbarD_eq q hq hq2]
  unfold strandF
  have : (1 : R) + q ^ 2 = q ^ 2 + 1 := by ring
  rw [this]
  field_simp

/-- Up curl and down curl have the same framing-corrected weight. -/
theorem curl_corrected_ratio_one (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    strandF q * (q⁻¹) ^ 2 * zD q = strandF q * q ^ 2 * zbarD q := by
  rw [curl_pos_cancels q hq hq2, curl_neg_cancels q hq hq2]

/-- The raw curl ratio `q⁴` is exactly the writhe-factor ratio `q² / q⁻²`. -/
theorem writhe_ratio_eq_curl_ratio (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    zD q / zbarD q = q ^ 2 / (q⁻¹) ^ 2 := by
  have hz : zbarD q ≠ 0 := by
    rw [zbarD_eq q hq hq2]
    exact one_div_ne_zero (mul_ne_zero hq hq2)
  rw [curl_ratio q hq hq2, mul_div_assoc, div_self hz, mul_one]
  field_simp

end QOU.Nuclear.NucleonCurlFramingCancels
