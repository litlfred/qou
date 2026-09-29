import Mathlib.Tactic
import Mathlib.Algebra.Group.Invertible.Basic
import QOU.QBeta.FiveTwoDTSpectrumSplit

/-!
# QOU.QBeta.SaddleOffsetBarGrade — chirality-grade ≠ q↔q⁻¹ Laurent bar-grade

**Formalize-first honest negative for the `qou-q86o` "origin-centred only at
`q = 1`" leg of the owner's saddle-vector picture.**

The sibling gate `IotaOddSaddleOffsetAmphichiral` (#4577) proves the certified
saddle offset `o = c⁺ − c⁻` vanishes iff the knot is (ι-fixed) amphichiral, by
*modelling* the chirality swap `(a,b) ↦ (b,a)` **as** the bar involution
`q ↔ q⁻¹`.  The numerical probe `saddle_offset_zero_location_probe.py`
(`qou-q86o`, #4583) shows those two involutions are **genuinely different at the
q-series level**: the certified offset is odd under the *chirality* swap, but its
*q*-dependence is **not** odd under `q ↔ q⁻¹` — its `q → 0` constant coefficient
is the certified datum `chiralityOdd 4 3 = 1 ≠ 0`, whereas any object that is
genuinely antisymmetric under `q ↔ q⁻¹` has a *zero* constant coefficient.

This file states that structural fact honestly.  It is the reason the "the
offset is origin-centred **only** at `q = 1`" leg is **not** delivered by the
bar-fixed-point argument: that argument makes any genuinely `q ↔ q⁻¹`-odd object
vanish at the fixed point `q = q⁻¹ = 1` for free, but the certified DT offset is
**not** such an object — it is a cross-chirality difference whose non-trivial
content lives at `q → 0`, with its own zero-crossing at a small finite
`q ≈ 0.089` (the root of the DT expansion `1 − 9q − 28q² + …`, a substrate-free
convergence-region root — see the probe/audit).

## The two gradings

Write a Laurent-coefficient sequence as `g : ℤ → R`, where `g n` is the
coefficient of `qⁿ`.  The bar involution `q ↦ q⁻¹` sends `qⁿ ↦ q⁻ⁿ`, i.e. acts
on coefficients by `n ↦ -n`.  Thus:

* **q↔q⁻¹ bar-grade.** `g` is *bar-odd in the modulus* — `BarAntisym g` — when
  `g (-n) = - g n` for all `n`.
* **chirality-grade.** The certified offset is odd under the *chirality* swap
  `c⁺ ↔ c⁻` (the #4577 gate); this is a **different** involution on a
  **different** index set (the two chirality labels), not on the q-degree.

## What is proved (non-vacuous, sorry-free, falsifiable)

* `barAntisym_const_zero` — the bar-fixed-point vanishing, generic
  `{R} [Ring R] [Invertible 2]`: a `q↔q⁻¹`-odd object has zero constant
  coefficient.  (This is exactly the mechanism the "q = 1" leg would need.)
* `barAntisym_const_zero_int` — the same over `ℤ` (a domain), no `Invertible 2`.
* `offsetConst_eq_one` — the certified offset's `q → 0` constant coefficient is
  `chiralityOdd (Splus0 0 1) (Sminus0 0 2) = 1` (reused from
  `FiveTwoDTSpectrumSplit`, not a fresh number).
* `certified_offset_not_barAntisym` — **the headline**: no Laurent object whose
  constant coefficient equals the certified offset datum can be `q↔q⁻¹`-odd.
  Hence the certified offset's `q = 1` vanishing is **not** delivered by the
  bar-fixed-point argument.
* `barAntisym_nontrivial` — anti-vacuity: a genuinely `q↔q⁻¹`-odd object exists
  (`g n = n`), and it *does* have zero constant coefficient — so the hypothesis
  of `barAntisym_const_zero` is satisfiable, and the headline is a real
  distinction, not a vacuous one.

## Discipline

§7c: generic `{R}` theory; concrete grounding over `ℤ` (no archimedean
construct).  No `sorry`, no `True := trivial`, no `native_decide`, no axiom
substituting for a proof.  Scope-(a): a structural *narrowing* of the picture
(the offset's `q = 1` vanishing is only the trivial fixed-point one, distinct
from the DT datum) — it invokes no proved invariant to exclude an ingredient,
derives no physical number, wires no `c_k`, inverts no `Q_β`/CODATA.  Standalone
library file (like its dependency `FiveTwoDTSpectrumSplit`), verified
`lean`-direct; not added to the `QBeta` aggregator.
-/

namespace QOU.QBeta.SaddleOffsetBarGrade

open QOU.QBeta.FiveTwoDTSpectrumSplit

/-- A Laurent-coefficient sequence `g : ℤ → R` is **q↔q⁻¹-antisymmetric**
(bar-odd in the modulus): the bar involution `q ↦ q⁻¹`, acting on coefficients by
`n ↦ -n`, negates it. -/
def BarAntisym {R : Type*} [Neg R] (g : ℤ → R) : Prop := ∀ n : ℤ, g (-n) = - g n

/-- **Bar-fixed-point vanishing (generic).**  A `q↔q⁻¹`-odd Laurent object has
zero constant (degree-0) coefficient.  This is the mechanism that forces any
genuinely bar-odd object to vanish at the fixed point `q = q⁻¹ = 1`. -/
theorem barAntisym_const_zero {R : Type*} [CommRing R] [Invertible (2 : R)]
    {g : ℤ → R} (h : BarAntisym g) : g 0 = 0 := by
  have h0 : g 0 = - g 0 := by simpa using h 0
  have h2 : (2 : R) * g 0 = 0 := by linear_combination h0
  calc
    g 0 = ⅟(2 : R) * ((2 : R) * g 0) := by
          rw [← mul_assoc, invOf_mul_self, one_mul]
    _ = ⅟(2 : R) * 0 := by rw [h2]
    _ = 0 := mul_zero _

/-- **Bar-fixed-point vanishing over `ℤ`** (a domain — no `Invertible 2` needed). -/
theorem barAntisym_const_zero_int {g : ℤ → ℤ} (h : BarAntisym g) : g 0 = 0 := by
  have h0 : g 0 = - g 0 := by simpa using h 0
  omega

/-- The certified `q → 0` constant coefficient of the 5₂ offset is the merged
distinguisher's ι-odd datum `chiralityOdd 4 3 = 1` (reused, not a fresh number). -/
def offsetConst : ℤ := chiralityOdd (Splus0 0 1) (Sminus0 0 2)

@[simp] theorem offsetConst_eq_one : offsetConst = 1 := by decide

/-- **Headline (honest negative).**  No Laurent object whose constant coefficient
equals the certified offset datum can be `q↔q⁻¹`-antisymmetric.  Hence the
certified saddle offset's `q = 1` vanishing is **not** delivered by the
bar-fixed-point argument — the offset is a cross-chirality difference (constant
coefficient `1 ≠ 0`), not a genuinely bar-odd-in-`q` object. -/
theorem certified_offset_not_barAntisym
    (g : ℤ → ℤ) (hconst : g 0 = offsetConst) (hbar : BarAntisym g) : False := by
  have hz : g 0 = 0 := barAntisym_const_zero_int hbar
  rw [hconst, offsetConst_eq_one] at hz
  exact one_ne_zero hz

/-- **Anti-vacuity.**  A genuinely `q↔q⁻¹`-odd object exists (`g n = n`); it does
have zero constant coefficient, so `barAntisym_const_zero`'s hypothesis is
satisfiable and the headline distinction is real, not vacuous. -/
theorem barAntisym_nontrivial : BarAntisym (fun n : ℤ => n) ∧ (fun n : ℤ => n) 0 = 0 := by
  refine ⟨?_, rfl⟩
  intro n
  simp

end QOU.QBeta.SaddleOffsetBarGrade
