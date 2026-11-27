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

**Ring symbol for `√2` (bean `qou-dk7p`).** Every statement is over an ordered
field `K` with `√2` a symbol `r`, `0 < r`, `r² = 2`, so the evaluations live in
`ℚ(√2)` and no completed real enters. The `ℝ` forms with `Real.sqrt 2`, under
their original names, are in
`QOU/Transcendental/Nuclear/SilverRatioCounitExclusionReal.lean`.

Sorry-free.
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination

namespace QOU.QBeta

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- The silver ratio `1 + r`, `r = √2` a symbol: the positive root of `q² − 2q − 1`. -/
def silverOf (r : K) : K := 1 + r

/-- **The silver ratio is a root of `q² − 2q − 1`.** -/
theorem silverOf_root {r : K} (hr2 : r ^ 2 = 2) :
    silverOf r ^ 2 - 2 * silverOf r - 1 = 0 := by
  unfold silverOf
  linear_combination hr2

/-- `1 < silver`; used to force the exponent on the unit to vanish. -/
theorem one_lt_silverOf {r : K} (hr : 0 < r) : (1 : K) < silverOf r := by
  unfold silverOf; linarith

/-- `silver ≠ 0`. -/
theorem silverOf_ne_zero {r : K} (hr : 0 < r) : silverOf r ≠ 0 :=
  ne_of_gt (lt_trans zero_lt_one (one_lt_silverOf hr))

/-- The corpus's asserted counit `ε(Δ)`, as a function of `q`:
    `epsNP q = (q²−1)(q²−2q−1)/(2q²)`.  Mirrors
    `QOU.Interactions.QBetaEnergyScale.epsNPq`. -/
def epsNP (q : K) : K := (q ^ 2 - 1) * (q ^ 2 - 2 * q - 1) / (2 * q ^ 2)

/-- Half the quantum integer, `[2]_q/2 = (q²+1)/(2q)` — the counit of the
    `averaged` typed crossing `σ − h/2`. -/
def bracket2half (q : K) : K := (q ^ 2 + 1) / (2 * q)

/-- The verified per-block character `χ₍₃₎(β_n − β_p)`, as a function of `q`.
    Mirrors `chi_block_3`; used here only as the CONTROL. -/
def chiBlock3 (q : K) : K := -(q ^ 2 - 1) * (q ^ 2 + 1) ^ 2 / (4 * q)

/-- **`epsNP` vanishes at the silver ratio.** This is what makes the exclusion
    run: the target of the search is zero at a point where every candidate is a
    product of units. -/
theorem epsNP_silverOf {r : K} (hr2 : r ^ 2 = 2) : epsNP (silverOf r) = 0 := by
  unfold epsNP
  rw [silverOf_root hr2]
  simp

/-- **`[2]_q/2 = √2` exactly at the silver ratio.** The second evaluation the
    argument turns on: it is what makes the right-hand side of the forced
    equation a power of `√2` rather than of an arbitrary element. -/
theorem bracket2half_silverOf {r : K} (hr : 0 < r) (hr2 : r ^ 2 = 2) :
    bracket2half (silverOf r) = r := by
  unfold bracket2half silverOf
  have hpos : (0 : K) < 1 + r := by linarith
  field_simp
  nlinarith [hr2, hr]

/-- **CONTROL — `chiBlock3` does NOT vanish at the silver ratio.**

`chiBlock3` *is* a difference of two typed-word counits (namely
`q¹·([2]_q/2)² − q³·([2]_q/2)²`), so if the exclusion argument also excluded it
the argument would be proving too much. It does not: the value here is
`−12 − 8√2 ≠ 0`. -/
theorem chiBlock3_silverOf_ne_zero {r : K} (hr : 0 < r) (hr2 : r ^ 2 = 2) :
    chiBlock3 (silverOf r) ≠ 0 := by
  unfold chiBlock3 silverOf
  have hpos : (0 : K) < 1 + r := by linarith
  have hnum : -((1 + r) ^ 2 - 1) * ((1 + r) ^ 2 + 1) ^ 2 < 0 := by
    nlinarith [hr2, hr]
  intro hzero
  rw [div_eq_zero_iff] at hzero
  rcases hzero with h | h
  · linarith [hnum, h.le, h.ge]
  · linarith [hpos]

/-- **The two evaluations together**, as the single statement the exclusion
    cites: at the silver ratio the target vanishes while the control does not. -/
theorem silverOf_separates_target_from_control {r : K} (hr : 0 < r) (hr2 : r ^ 2 = 2) :
    epsNP (silverOf r) = 0 ∧ chiBlock3 (silverOf r) ≠ 0 :=
  ⟨epsNP_silverOf hr2, chiBlock3_silverOf_ne_zero hr hr2⟩

end QOU.QBeta
