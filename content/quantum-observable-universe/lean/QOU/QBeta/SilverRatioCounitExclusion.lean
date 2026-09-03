/-
# QOU.QBeta — the silver-ratio evaluation behind the `epsNPq` exclusion

Bean `qou-avt6`. Supports the scope-(b) exclusion: **no difference of two
typed-crossing words has counit `epsNPq`.**

## The argument, in full, and what this file does and does not carry

A typed crossing `(c = 1, d)` is the algebra element `σ_g + d`; the Hecke
relation `σ⁻¹ = σ − h` makes the four templates `d ∈ {0, −h, −h/2, …}` read off
as `σ`, `σ⁻¹`, the average, and the colour-weighted crossing. The Frobenius
counit sends `σ ↦ q`, so

    ε(σ_g + d) = q + d ∈ { q, q⁻¹, [2]_q/2 }
    ⟹ ε(any typed word) = q^m · ([2]_q/2)^c.

`epsNPq = h(h−2)/2 = (q²−1)(q²−2q−1)/(2q²)` carries the irreducible factor
`q² − 2q − 1`, whose positive root is the **silver ratio** `1 + √2`. So `epsNPq`
vanishes there, while `[2]_q/2` evaluates to exactly `√2`. A typed-word
difference vanishing at the silver ratio therefore forces

    (1 + √2)^(m₁ − m₂) = (√2)^(c₂ − c₁),

and absolute norms in `ℤ[√2]` (`|N(1+√2)| = 1`, the fundamental unit;
`|N(√2)| = 2`) force `c₁ = c₂`, then `m₁ = m₂` since `1 + √2 > 1`. The
difference is then identically zero — which `epsNPq` is not. Contradiction.

**This file formalises the EVALUATION FACTS the argument turns on**, which are
the part specific to this corpus and were not previously recorded anywhere:
`epsNP` vanishes at the silver ratio, `[2]_q/2 = √2` there, and — the control —
`chiBlock3` does *not* vanish there, so the argument does not prove too much.

**It does NOT formalise the unit-group step** (`(1+√2)^a = (√2)^b → a = b = 0`).
That step is standard algebraic number theory, not corpus-specific, and is left
outside Lean deliberately rather than `sorry`-ed: nothing here asserts it, and
no theorem below depends on it. Formalising it needs `Zsqrtd 2` and norm
multiplicativity; tracked in `qou-avt6`.

Sorry-free.
-/
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.QBeta

open Real

/-- The silver ratio `1 + √2`, the positive root of `q² − 2q − 1`. -/
noncomputable def silver : ℝ := 1 + Real.sqrt 2

/-- `√2 > 0`, used throughout. -/
theorem sqrt_two_pos : (0 : ℝ) < Real.sqrt 2 :=
  Real.sqrt_pos.mpr (by norm_num)

/-- `(√2)² = 2`. -/
@[simp] theorem sq_sqrt_two : (Real.sqrt 2) ^ 2 = 2 := Real.sq_sqrt (by norm_num)

/-- **The silver ratio is a root of `q² − 2q − 1`.** -/
theorem silver_root : silver ^ 2 - 2 * silver - 1 = 0 := by
  unfold silver
  have h : (Real.sqrt 2) ^ 2 = 2 := sq_sqrt_two
  nlinarith [h]

/-- `1 < silver`; used to force the exponent on the unit to vanish. -/
theorem one_lt_silver : (1 : ℝ) < silver := by
  unfold silver; linarith [sqrt_two_pos]

/-- `silver ≠ 0`. -/
theorem silver_ne_zero : silver ≠ 0 := by
  have := one_lt_silver; intro h; rw [h] at this; norm_num at this

/-- The corpus's asserted counit `ε(Δ)`, as a function of `q`:
    `epsNP q = (q²−1)(q²−2q−1)/(2q²)`.  Mirrors
    `QOU.Interactions.QBetaEnergyScale.epsNPq`. -/
noncomputable def epsNP (q : ℝ) : ℝ := (q ^ 2 - 1) * (q ^ 2 - 2 * q - 1) / (2 * q ^ 2)

/-- Half the quantum integer, `[2]_q/2 = (q²+1)/(2q)` — the counit of the
    `averaged` typed crossing `σ − h/2`. -/
noncomputable def bracket2half (q : ℝ) : ℝ := (q ^ 2 + 1) / (2 * q)

/-- The verified per-block character `χ₍₃₎(β_n − β_p)`, as a function of `q`.
    Mirrors `chi_block_3`; used here only as the CONTROL. -/
noncomputable def chiBlock3 (q : ℝ) : ℝ := -(q ^ 2 - 1) * (q ^ 2 + 1) ^ 2 / (4 * q)

/-- **`epsNP` vanishes at the silver ratio.** This is what makes the exclusion
    run: the target of the search is zero at a point where every candidate is a
    product of units. -/
theorem epsNP_silver : epsNP silver = 0 := by
  unfold epsNP
  rw [show silver ^ 2 - 2 * silver - 1 = 0 from silver_root]
  simp

/-- **`[2]_q/2 = √2` exactly at the silver ratio.** The second evaluation the
    argument turns on: it is what makes the right-hand side of the forced
    equation a power of `√2` rather than of an arbitrary real. -/
theorem bracket2half_silver : bracket2half silver = Real.sqrt 2 := by
  unfold bracket2half silver
  have h2 : (Real.sqrt 2) ^ 2 = 2 := sq_sqrt_two
  have hpos : (0 : ℝ) < 1 + Real.sqrt 2 := by linarith [sqrt_two_pos]
  field_simp
  nlinarith [h2, sqrt_two_pos]

/-- **CONTROL — `chiBlock3` does NOT vanish at the silver ratio.**

`chiBlock3` *is* a difference of two typed-word counits (namely
`q¹·([2]_q/2)² − q³·([2]_q/2)²`), so if the exclusion argument also excluded it
the argument would be proving too much. It does not: the value here is
`−12 − 8√2 ≠ 0`. -/
theorem chiBlock3_silver_ne_zero : chiBlock3 silver ≠ 0 := by
  unfold chiBlock3 silver
  have h2 : (Real.sqrt 2) ^ 2 = 2 := sq_sqrt_two
  have hs : (0 : ℝ) < Real.sqrt 2 := sqrt_two_pos
  have hpos : (0 : ℝ) < 1 + Real.sqrt 2 := by linarith
  have hnum : -((1 + Real.sqrt 2) ^ 2 - 1) * ((1 + Real.sqrt 2) ^ 2 + 1) ^ 2 < 0 := by
    nlinarith [h2, hs]
  intro hzero
  rw [div_eq_zero_iff] at hzero
  rcases hzero with h | h
  · linarith [hnum, h.le, h.ge]
  · linarith [hpos]

/-- **The two evaluations together**, as the single statement the exclusion
    cites: at the silver ratio the target vanishes while the control does not. -/
theorem silver_separates_target_from_control :
    epsNP silver = 0 ∧ chiBlock3 silver ≠ 0 :=
  ⟨epsNP_silver, chiBlock3_silver_ne_zero⟩

end QOU.QBeta
