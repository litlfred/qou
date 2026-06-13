import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic

/-!
# QOU.Archimedean.EHartreeTraceRatio

**Round-20 algebraic core of `conj:e-hartree-categorical-derivation`.**

Round 19 (`e_hartree_round19_dressed_scalar_block.py`) computed the dressed
scalar `(2,2)`-block character at K-shell dressing `m = 5`:
`χ₂₂ = h·([4]_q/[2]_q)²` with `h = q − q⁻¹`.  Round 20
(`e_hartree_round20_trace_ratio.py`) formed the trace-ratio
`ρ₂₂ := χ₂₂ / (q·[9]_q·[10]_q)²` and found `ρ₂₂ = C(q)·α_EM²` with
`C(q) = h·([4]_q/[2]_q)² = h·(q² + q⁻²)²` an `O(1)` element of `R` and
`α_EM = 1/(q·[9]_q·[10]_q)`.

This file proves, **sorry-free over `ℝ`** (archimedean, `0 < q`; CLAUDE.md §7c),
the two purely-algebraic facts underpinning round 20:

* `qbracket_four_div_two` — the bracket reduction `[4]_q / [2]_q = q² + q⁻²`
  (the dressed `(2,2)` q-dimension `dim_q V_(2,2)`).
* `trace_ratio_factorisation` — `χ₂₂ / cplx² = χ₂₂ · α²` with `α = 1/cplx`,
  the `α²`-scaling step (pure field algebra, `cplx ≠ 0`).

The deep input — that the dressed seminormal character *equals*
`h·([4]_q/[2]_q)²` — is verified numerically in the round-19 witness and is the
character-theory content; it is the cited/granted ingredient here (the
seminormal-trace formalisation is the standing open part).  These lemmas
discharge the algebra that turns that character value into the `α_EM²` shape.
-/

namespace QOU.Archimedean.EHartreeTraceRatio

/-- Balanced q-integer `[n]_q = (qⁿ − (q⁻¹)ⁿ)/(q − q⁻¹)` over `ℝ`. -/
noncomputable def qbracket (q : ℝ) (n : ℕ) : ℝ :=
  (q ^ n - (q⁻¹) ^ n) / (q - q⁻¹)

/-- For `0 < q` and `q ≠ 1`, the amplitude `q − q⁻¹` is nonzero. -/
theorem qsub_inv_ne (q : ℝ) (hq : 0 < q) (hq1 : q ≠ 1) : q - q⁻¹ ≠ 0 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  rw [sub_ne_zero]
  intro h
  apply hq1
  -- h : q = q⁻¹ ⟹ q² = 1 ⟹ (q-1)(q+1) = 0 ⟹ q = 1 (since q > 0)
  have hqq : q * q = 1 := by field_simp at h; linarith [h]
  have hfac : (q - 1) * (q + 1) = 0 := by nlinarith [hqq]
  rcases mul_eq_zero.mp hfac with h1 | h2
  · linarith [h1]
  · linarith [h2, hq]

/-- For `0 < q` and `q ≠ 1`, `q² − (q⁻¹)² ≠ 0` (the `[2]`-amplitude squared). -/
theorem qsq_sub_inv_sq_ne (q : ℝ) (hq : 0 < q) (hq1 : q ≠ 1) :
    q ^ 2 - (q⁻¹) ^ 2 ≠ 0 := by
  have hd := qsub_inv_ne q hq hq1
  intro h
  apply hd
  have hfac : q ^ 2 - (q⁻¹) ^ 2 = (q - q⁻¹) * (q + q⁻¹) := by ring
  rw [hfac] at h
  rcases mul_eq_zero.mp h with h1 | h2
  · exact h1
  · have hpos : 0 < q + q⁻¹ := by positivity
    linarith [h2, hpos]

/-- **The bracket reduction `[4]_q / [2]_q = q² + q⁻²`.**

This is `dim_q V_(2,2)`, the q-dimension of the scalar Wedderburn block that
activates under K-shell dressing (round 19); it is the `C(q)`-defining factor
in the round-20 trace-ratio.  Holds for `0 < q`, `q ≠ 1`. -/
theorem qbracket_four_div_two (q : ℝ) (hq : 0 < q) (hq1 : q ≠ 1) :
    qbracket q 4 / qbracket q 2 = q ^ 2 + (q⁻¹) ^ 2 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hd := qsub_inv_ne q hq hq1
  have hd2 := qsq_sub_inv_sq_ne q hq hq1
  have hb2 : qbracket q 2 ≠ 0 := by unfold qbracket; exact div_ne_zero hd2 hd
  rw [div_eq_iff hb2]
  unfold qbracket
  field_simp
  ring

/-- **Trace-ratio factorisation (round 20).**

With nonzero force-carrier complexity `cplx = q·[9]_q·[10]_q`, the molecular
scalar-block trace-ratio `χ₂₂ / cplx²` equals `χ₂₂ · α²` where the EM coupling
is `α = 1/cplx`.  Pure field algebra — this is the step that exhibits the
`α_EM²` scaling once the dressed character `χ₂₂` and the complexity normaliser
are in hand. -/
theorem trace_ratio_factorisation (chi22 cplx : ℝ) (hc : cplx ≠ 0) :
    chi22 / cplx ^ 2 = chi22 * (1 / cplx) ^ 2 := by
  field_simp

/-- **Round-20 trace-ratio, assembled.**

Given the round-19 dressed character `chi22 = h·(q²+q⁻²)²` and the complexity
`cplx = q·[9]_q·[10]_q ≠ 0`, the trace-ratio equals `C(q)·α²` with the *derived*
`O(1)` coefficient `C(q) = h·(q²+q⁻²)²` and `α = 1/cplx`.  Sorry-free; the
content is exactly `trace_ratio_factorisation` with `C(q)` named. -/
theorem trace_ratio_eq_C_mul_alpha_sq
    (q cplx : ℝ) (hc : cplx ≠ 0)
    (chi22 : ℝ) (hchi : chi22 = (q - q⁻¹) * (q ^ 2 + (q⁻¹) ^ 2) ^ 2) :
    chi22 / cplx ^ 2
      = ((q - q⁻¹) * (q ^ 2 + (q⁻¹) ^ 2) ^ 2) * (1 / cplx) ^ 2 := by
  rw [hchi]
  exact trace_ratio_factorisation _ cplx hc

end QOU.Archimedean.EHartreeTraceRatio
