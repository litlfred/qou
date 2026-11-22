import QOU.MathlibExt.OcneanuTrace
import Mathlib.Tactic

/-!
# The Markov trace is NOT bond-multiplicative at `n = 4`: the interleaved cross term

`computations/probes/markov_multiplicativity_interleaved_probe.py` (bean `qou-ls86`, 2026-08-18)
proved by exact algebra that on `H₃` the interleaved word `s₀ s₁ s₀` has the same Markov trace
as the sequential `s₀² s₁` — the single interleaved word of `H₃` is a cyclic rotation of a
sequential one — and concluded the per-bond product formula is exact there. It then flagged
the general-`n` question as **open**, naming `s₀ s₁ s₀ s₂ s₁` as an `n = 4` word with no such
rotation.

This file settles that instance: **the product formula fails at `n = 4`.** From the Ocneanu
axioms alone — `tr 1 = 1`, the trace property, Markov stabilisation `tr(x gₙ) = z·tr x` for
`x ∈ Hₙ` — plus the Hecke quadratic `g² = h·g + 1` and the braid relation, both taken as
hypotheses on the generators,

    tr(s₀ s₁ s₀ s₂ s₁) = z (z² + h z + h² z²)
    tr(s₀² s₁² s₂)     = z (h z + 1)²                  (the per-bond product)
    difference         = z (z² − h z − 1)               (`interleaved_sub_sequential`)

The factor `z² − h z − 1` is the corpus's **convention-D Markov defect** (bean `qou-19jc`; by
`qou-xzrj` it equals `−(q⁴+q²+1)/q² · y₍₂,₁₎`, the two-row Wedderburn weight). At convention D,
`z = q³/(q²+1)`, `h = q − q⁻¹`, it is `−(q⁴+q²+1)/(q²+1)²` (`markovDefect_convD`), strictly
negative for real `q > 0` (`crossTerm_neg_convD`): the interleaved trace is *smaller*, so an
interleaved word class carries **extra** log-suppression — extra binding.

## What this is and is not

* **Positive existence, exact.** A multi-bond cross term exists in the framework's own trace,
  for interleaved word classes, with an exact closed form. Independently confirmed in the 16-dim
  spin-½ representation (`markov_trace_n4_interleaved_cross_term_probe.py`, 11/11).
* **No production number moves.** `atom_braid_word_3A` is sequential (one inter-nucleon letter,
  no generator recurring after its neighbour), so the production trace's bare-product
  implementation is exact for the production word class. This is a candidate *source* for the
  multi-bond term `qou-ls86` closed at `n = 3`, not a correction.
* **Which word class a nucleus is** remains the carrier blocker (`qou-5vhf`). Nothing is wired
  and nothing is fitted.

## Base ring (§7c)

The abstract identity is over a generic `CommRing R` acting on a generic `Ring A` — the
`MarkovTrace` structure of `QOU.MathlibExt.OcneanuTrace`, whose T1–T3 are exactly the axioms
used. The convention-D closed form is over a generic `Field`; only the sign statement is over
`ℝ` (an ordering claim, archimedean by nature).

-- Ref: [leitner2026] computations/probes/markov_multiplicativity_interleaved_probe.py
-- Ref: [leitner2026] computations/probes/markov_trace_n4_interleaved_cross_term_probe.py
-- Ref: [jones1987] https://doi.org/10.2307/1971403 — the Markov trace on the Hecke tower.
-/

namespace QOU.MathlibExt.InterleavedCrossTerm

open QOU.MathlibExt.OcneanuTrace

section Abstract

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
variable (T : MarkovTrace R A)

/-- `tr(g₀) = z`: Markov stabilisation of the unit. -/
theorem tr_g0 : T.tr (T.g 0) = T.z := by
  have h := T.markov 0 (1 : A) (T.H 0).one_mem
  rw [one_mul, T.tr_one, mul_one] at h
  exact h

/-- `tr(g₀ g₁) = z²`. -/
theorem tr_g0_g1 : T.tr (T.g 0 * T.g 1) = T.z ^ 2 := by
  rw [T.markov 1 (T.g 0) (T.g_mem 0), tr_g0, sq]

/-- `tr(g₀²) = h z + 1` from the Hecke quadratic. -/
theorem tr_g0_sq (h : R) (hq0 : T.g 0 * T.g 0 = h • T.g 0 + 1) :
    T.tr (T.g 0 * T.g 0) = h * T.z + 1 := by
  rw [hq0, map_add, map_smul, tr_g0, T.tr_one, smul_eq_mul]

/-- `tr(g₀² g₁) = z (h z + 1)`. -/
theorem tr_g0sq_g1 (h : R) (hq0 : T.g 0 * T.g 0 = h • T.g 0 + 1) :
    T.tr (T.g 0 * T.g 0 * T.g 1) = T.z * (h * T.z + 1) := by
  have hmem : T.g 0 * T.g 0 ∈ T.H 1 := (T.H 1).mul_mem (T.g_mem 0) (T.g_mem 0)
  rw [T.markov 1 _ hmem, tr_g0_sq T h hq0]

/-- **The `n = 3` identity of `qou-ls86`:** `tr(g₀ g₁ g₀) = tr(g₀² g₁)` by cyclicity alone. -/
theorem tr_g0_g1_g0 (h : R) (hq0 : T.g 0 * T.g 0 = h • T.g 0 + 1) :
    T.tr (T.g 0 * T.g 1 * T.g 0) = T.z * (h * T.z + 1) := by
  rw [T.tr_mul_comm (T.g 0 * T.g 1) (T.g 0), ← mul_assoc, tr_g0sq_g1 T h hq0]

/-- `tr(g₁ g₀ g₁ g₀) = h·z(hz+1) + z²` via the braid relation and the Hecke quadratic. -/
theorem tr_g1_g0_g1_g0 (h : R) (hq0 : T.g 0 * T.g 0 = h • T.g 0 + 1)
    (hbraid : T.g 0 * T.g 1 * T.g 0 = T.g 1 * T.g 0 * T.g 1) :
    T.tr (T.g 1 * T.g 0 * T.g 1 * T.g 0) = h * (T.z * (h * T.z + 1)) + T.z ^ 2 := by
  have hw : T.g 1 * T.g 0 * T.g 1 * T.g 0 = T.g 0 * T.g 1 * (h • T.g 0 + 1) := by
    rw [← hbraid, mul_assoc (T.g 0 * T.g 1), hq0]
  rw [hw, mul_add, mul_one, mul_smul_comm, map_add, map_smul, smul_eq_mul, ← mul_assoc,
    tr_g0_g1_g0 T h hq0, tr_g0_g1]
  ring

/-- **The interleaved word.** `tr(g₀ g₁ g₀ g₂ g₁) = z (z² + h z + h² z²)`: rotate the trailing
`g₁` to the front (trace property), peel `g₂` (Markov), then the `H₃` word above. -/
theorem tr_interleaved (h : R) (hq0 : T.g 0 * T.g 0 = h • T.g 0 + 1)
    (hbraid : T.g 0 * T.g 1 * T.g 0 = T.g 1 * T.g 0 * T.g 1) :
    T.tr (T.g 0 * T.g 1 * T.g 0 * T.g 2 * T.g 1)
      = T.z * (h * (T.z * (h * T.z + 1)) + T.z ^ 2) := by
  have h0 : T.g 0 ∈ T.H 2 := T.H_mono (by norm_num) (T.g_mem 0)
  have h1 : T.g 1 ∈ T.H 2 := T.g_mem 1
  have hmem : T.g 1 * T.g 0 * T.g 1 * T.g 0 ∈ T.H 2 :=
    (T.H 2).mul_mem ((T.H 2).mul_mem ((T.H 2).mul_mem h1 h0) h1) h0
  rw [T.tr_mul_comm (T.g 0 * T.g 1 * T.g 0 * T.g 2) (T.g 1)]
  have hassoc : T.g 1 * (T.g 0 * T.g 1 * T.g 0 * T.g 2)
      = T.g 1 * T.g 0 * T.g 1 * T.g 0 * T.g 2 := by
    simp only [mul_assoc]
  rw [hassoc, T.markov 2 _ hmem, tr_g1_g0_g1_g0 T h hq0 hbraid]

/-- **The sequential (per-bond product) word.** `tr(g₀² g₁² g₂) = z (h z + 1)²`. -/
theorem tr_sequential (h : R) (hq0 : T.g 0 * T.g 0 = h • T.g 0 + 1)
    (hq1 : T.g 1 * T.g 1 = h • T.g 1 + 1) :
    T.tr (T.g 0 * T.g 0 * (T.g 1 * T.g 1) * T.g 2) = T.z * (h * T.z + 1) ^ 2 := by
  have h0 : T.g 0 ∈ T.H 2 := T.H_mono (by norm_num) (T.g_mem 0)
  have h1 : T.g 1 ∈ T.H 2 := T.g_mem 1
  have hmem : T.g 0 * T.g 0 * (T.g 1 * T.g 1) ∈ T.H 2 :=
    (T.H 2).mul_mem ((T.H 2).mul_mem h0 h0) ((T.H 2).mul_mem h1 h1)
  rw [T.markov 2 _ hmem, hq1, mul_add, mul_one, mul_smul_comm, map_add, map_smul, smul_eq_mul,
    tr_g0sq_g1 T h hq0, tr_g0_sq T h hq0]
  ring

/-- **THE CROSS TERM.** The interleaved word and the per-bond product differ by exactly
`z (z² − h z − 1)`. The product formula is not exact at `n = 4`. -/
theorem interleaved_sub_sequential (h : R) (hq0 : T.g 0 * T.g 0 = h • T.g 0 + 1)
    (hq1 : T.g 1 * T.g 1 = h • T.g 1 + 1)
    (hbraid : T.g 0 * T.g 1 * T.g 0 = T.g 1 * T.g 0 * T.g 1) :
    T.tr (T.g 0 * T.g 1 * T.g 0 * T.g 2 * T.g 1) - T.tr (T.g 0 * T.g 0 * (T.g 1 * T.g 1) * T.g 2)
      = T.z * (T.z ^ 2 - h * T.z - 1) := by
  rw [tr_interleaved T h hq0 hbraid, tr_sequential T h hq0 hq1]
  ring

end Abstract

section ConventionD

/-- The convention-D Markov defect `z² − h z − 1` at `z = q³/(q²+1)`, `h = q − q⁻¹`, in closed
form: `−(q⁴+q²+1)/(q²+1)²`. -/
theorem markovDefect_convD {K : Type*} [Field K] (q : K) (h2 : q ^ 2 + 1 ≠ 0) :
    (q ^ 3 / (q ^ 2 + 1)) ^ 2 - (q - q⁻¹) * (q ^ 3 / (q ^ 2 + 1)) - 1
      = -(q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 := by
  field_simp
  ring

/-- **The cross term is strictly negative at convention D for every real `q > 0`:** the
interleaved trace is smaller than the per-bond product, so an interleaved word class carries
extra log-suppression (extra binding). -/
theorem crossTerm_neg_convD (q : ℝ) (hq : 0 < q) :
    (q ^ 3 / (q ^ 2 + 1)) * ((q ^ 3 / (q ^ 2 + 1)) ^ 2 - (q - q⁻¹) * (q ^ 3 / (q ^ 2 + 1)) - 1)
      < 0 := by
  have h2 : q ^ 2 + 1 ≠ 0 := by positivity
  rw [markovDefect_convD q h2]
  have hz : 0 < q ^ 3 / (q ^ 2 + 1) := by positivity
  have hd : -(q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 < 0 := by
    apply div_neg_of_neg_of_pos
    · have : 0 < q ^ 4 + q ^ 2 + 1 := by positivity
      linarith
    · positivity
  exact mul_neg_of_pos_of_neg hz hd

end ConventionD

end QOU.MathlibExt.InterleavedCrossTerm
