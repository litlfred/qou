/-
# The translate-matrix bound, in the house

`RothAuxiliaryPolynomial.seminorm_translateMatrix_le` is stated for an arbitrary
submultiplicative seminorm.  `house` is one, and this file is the instantiation — the last of
the four inputs `Siegel over a number field` needs.

⚠⚠ **A measurement I published and got wrong by an order of magnitude.**

The previous commit recorded that `Mathlib.NumberTheory.NumberField.House` was `470` of `3322`
transitive imports away from this project's built closure, and framed the next step as *a fork*:
a 470-module Mathlib build against re-deriving the integral-basis bookkeeping by hand.

**Both numbers were wrong.**  Building it took **40 modules and about four minutes** (`3390 →
3430` oleans; `SiegelsLemma` before it was `3`, which the estimate did get right).  There was no
fork.  `House` was cheap and was plainly the right route.

The cause: the import-cone script matched `^import` with `re.MULTILINE` over the **whole file**,
so it collected `import` lines appearing inside docstrings and comments — and once the root
module `Mathlib` was picked up that way, the cone inflated toward all of Mathlib.  The first run
happened to read only the first 20 kB of each file, which hid most of the damage but not all of
it, and I reported the result as a measurement without validating the script against a case whose
answer I already knew.

⚠ The general shape, which this arc has now hit in three forms: a *weaker true theorem*
(correction 24), a *hypothesis nobody discharges* (correction 25), and now an **unvalidated
measurement** — all three read exactly like the sound version and none of them is caught by
anything mechanical.  The check that would have caught this one costs nothing: `SiegelsLemma`'s
estimate was `3`, and it was verifiable in thirty seconds.  I verified the cheap one and
extrapolated the expensive one.

⚠ Not Mathlib-only, and **not in the default closure**: this file imports
`Mathlib.NumberTheory.NumberField.House`, which a fresh container must build first
(`lake build Mathlib.NumberTheory.NumberField.House`, ~4 min).  It is a separate module from
`RothAuxiliaryPolynomial` for exactly that reason — the core development stays light and the
number-field dependency is opt-in.
-/
import QOU.Mathlib.RothAuxiliaryPolynomial
import Mathlib.NumberTheory.NumberField.House

namespace MvPolynomial

open NumberField

variable {K : Type*} [Field K] [NumberField K]


theorem submultSeminorm_house : SubmultSeminorm (house : K → ℝ) :=
  ⟨house_nonneg, by simp [house], by simp [house],
    fun a b => by simpa using house_sum_le_sum_house (Finset.univ : Finset (Fin 2)) ![a, b],
    house_mul_le⟩

/-- **Roth's matrix entries, bounded in the house.** -/
theorem house_translateMatrix_le {σ : Type*} [DecidableEq σ] (α : σ → K) {B : ℝ}
    (hB1 : 1 ≤ B) (hα : ∀ h, house (α h) ≤ B) (n i : σ →₀ ℕ) :
    house (translateMatrix α i n) ≤ (2 * B) ^ (n.sum fun _ e => e) :=
  seminorm_translateMatrix_le submultSeminorm_house α hB1 hα _ n rfl i

end MvPolynomial
