/-
MinPlusValuationBound.lean — why the min-plus (tropical) computation of
α_shift is a BOUND, and why the bound can be strict.

CONTEXT.  On a seminormal channel of dimension > 1 the character is a sum over
standard-tableau paths, `χ(w) = Σ_paths ∏_k (entry at step k)`.  Addendum 39
derived the per-entry `q → 0` valuations; the pole order is then read off a
MIN-PLUS matrix product over those integers
(`computations/meson/alpha_shift_min_plus_probe.py`, which reproduces the
measured valuation on 44 of 46 (word, λ) pairs and 22 of 24 multi-dimensional
channels).

THE POINT OF THIS FILE.  That computation is an INEQUALITY, not an identity, and
the distinction is the whole content:

  * `val` is multiplicative on products, so each path contributes the SUM of its
    entry valuations — the "plus" of min-plus;
  * `val` is non-archimedean on sums, so the total is at LEAST the minimum over
    paths — the "min", and only a lower bound;
  * cancellation among the minimal paths makes it STRICT, which is exactly the
    two measured misses.

The first version of that probe asserted the identity and failed on those two.
Stating the bound is not a weakening — it is the correct statement, and the
strictness witness below is what makes it non-vacuous.

Generic `AddCommMonoid` / `CommMonoid`; no `ℝ`, nothing archimedean, and no
calibration input — `α_shift` is a valuation in the formal `q` and consumes
none of CAL-1/2/3.

@module QOU.BraidKnot.MinPlusValuationBound
-/

import Mathlib.Algebra.Order.Monoid.Unbundled.WithTop
import Mathlib.Algebra.Group.Basic
import Mathlib.Order.WithBot
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

set_option autoImplicit false

namespace QOU.BraidKnot

/-- Valuations take values in `ℤ ∪ {⊤}`, with `⊤` the valuation of zero. -/
abbrev Val := WithTop Int

variable {R : Type*}

/-- The minimum valuation over a list of terms — the "min" of min-plus. -/
def minVal [AddCommMonoid R] (val : R → Val) : List R → Val
  | [] => ⊤
  | x :: rest => min (val x) (minVal val rest)

/-- **The bound.**  For a non-archimedean valuation, the valuation of a sum is
at least the minimum of the valuations of its terms.  This is what makes the
min-plus matrix product a valid lower bound on `val(χ)`, hence a valid UPPER
bound on the pole order — and it is only a bound. -/
theorem minVal_le_val_sum [AddCommMonoid R] (val : R → Val)
    (hzero : val 0 = ⊤)
    (hadd : ∀ a b : R, min (val a) (val b) ≤ val (a + b)) :
    ∀ l : List R, minVal val l ≤ val l.sum := by
  intro l
  induction l with
  | nil => simp [minVal, hzero]
  | cons x rest ih =>
      show min (val x) (minVal val rest) ≤ val (x + rest.sum)
      exact le_trans (min_le_min (le_refl (val x)) ih) (hadd x rest.sum)

/-- Product along a path.  Defined here rather than imported: `List.sum` is
available in this build but `List.prod` is not, and a local definition keeps the
import surface minimal. -/
def pathProd [CommMonoid R] : List R → R
  | [] => 1
  | x :: rest => x * pathProd rest

/-- The sum of valuations along one path — the "plus" of min-plus.  A
multiplicative valuation turns a product of entries into a sum of integers,
which is why each path contributes a single integer weight. -/
def sumVal [CommMonoid R] (val : R → Val) : List R → Val
  | [] => 0
  | x :: rest => val x + sumVal val rest

theorem sumVal_eq_val_prod [CommMonoid R] (val : R → Val)
    (hone : val 1 = 0) (hmul : ∀ a b : R, val (a * b) = val a + val b) :
    ∀ l : List R, sumVal val l = val (pathProd l) := by
  intro l
  induction l with
  | nil => simpa [sumVal, pathProd] using hone.symm
  | cons x rest ih =>
      show val x + sumVal val rest = val (x * pathProd rest)
      rw [hmul, ih]

/-- **Non-vacuity: the bound can be STRICT.**  Two terms of equal finite
valuation can cancel, sending the sum's valuation to `⊤`.  This is the measured
failure mode — two of forty-six (word, λ) pairs, both on channels of dimension
`> 1`, where the minimal paths cancel and the min-plus value under-states the
true valuation. -/
theorem exists_strict_of_cancel :
    ∃ (val : Int → Val), (∀ a b : Int, min (val a) (val b) ≤ val (a + b))
      ∧ min (val 1) (val (-1)) < val (1 + (-1)) := by
  refine ⟨fun n => if n = 0 then ⊤ else (0 : Val), ?_, ?_⟩
  · intro a b
    by_cases hab : a + b = 0
    · simp [hab]
    · by_cases ha : a = 0
      · simp [ha]
      · simp [ha, hab]
  · norm_num

/-- The one-dimensional case has nothing to cancel against: a single-term sum
attains the bound with equality.  So strictness is a genuinely
multi-dimensional phenomenon, matching the measurement. -/
theorem minVal_singleton_eq [AddCommMonoid R] (val : R → Val) (x : R) :
    minVal val [x] = val [x].sum := by
  simp [minVal]

end QOU.BraidKnot
