import Mathlib.Tactic
import Mathlib.Algebra.Polynomial.Degree.Units
import QOU.Archimedean.lepton_continuant_recurrence

/-!
# QOU.Archimedean.lepton_continuant_generation_exclusion — why the ladder stops at three

**Interpretive derivation** for the three-generation gap
([`prop:lepton-meson-torus-knot-dictionary`](../../../quantum-observable-universe/particle-interactions/lepton-meson-torus-knot-dictionary.md),
bean `qou-x4qm`).

## The gap, made precise

Two corpus statements bracket the lepton ladder:

* `torus-embeddable-complete-proof` **proves** the embeddability bound
  `g(T(2,n)) = (n-1)/2 ≤ g(Σ₄) = 4`, so for `m = 2` the odd coprime
  windings are `n ∈ {3, 5, 7, 9}` — **four** admissible knots.
* `lepton-continuant-recurrence` assigns `T(2,n)` for `n = 3, 5, 7` to
  `e/μ/τ` — **three** generations.

So "why three generations" reduces to the single question *what excludes
`T(2,9)`?*  The dictionary's opening line asserts the answer —
"`n = 3, 5, 7, …` (odd primes)" — but the primality condition appears
exactly once in the whole corpus and is **asserted, never derived**.

## What this file derives

The candidate structural reason was stated in the dictionary author-note
as a hypothesis: `σ⁹ = (σ³)³` is a *harmonic* of generation 1 — the
braid word factors through a smaller winding — while `3, 5, 7` admit no
such factorisation.  Made precise on the normal-form data:

> The `σ`-coefficient `bₙ` of the Gröbner–Shirshov normal form of
> `T(2,n) = σ₀ⁿ` (the Morgan–Voyce continuant of
> `lepton_continuant_recurrence`) satisfies the **Fibonacci-polynomial
> divisibility** `b_a ∣ b_n ⟺ a ∣ n`.

Consequences on the genus-admissible windings `{3, 5, 7, 9}`, all proved
below over `Polynomial ℤ` (`X` = the Hecke parameter `h = q − q⁻¹`):

* `b₃ ∣ b₉` with the **explicit harmonic cofactor**
  `b₉ = b₃ · (X⁶ + 6X⁴ + 9X² + 1)` — winding 9's normal-form coefficient
  is a multiple of winding 3's (`t29_harmonic_of_first_generation`).
* `¬ (b₃ ∣ b₅)` and `¬ (b₃ ∣ b₇)` — the remainder is the unit `−1`, so
  `b₃` would have to be a unit of `Polynomial ℤ`; it is not (degree 2).

Since `3, 5, 7` are prime they have no proper odd divisor `> 1`, so
`b₃, b₅, b₇` are mutually non-divisible; `9 = 3·3` is the unique composite
in the window, and `b₉` factors through `b₃`.  This turns the asserted
"(odd primes)" into a **derived** statement at the normal-form level: the
generation windings are exactly the odd windings whose continuant
coefficient does not factor through a smaller one, i.e. the odd primes.

## Honest scope (scope-(a), not scope-(b))

This is a derivation of the *harmonic / factorisation* distinction on the
normal-form coefficient, **not** a proof that `T(2,9)` cannot be a
physical state: `T(2,9)` is a genuine prime knot of genus 4, and the map
from the continuant `net` to a physical mass is still open (the
`net` ratios are `O(1)` while the observed lepton ratios are `O(10²)` —
recorded as a *failed* validation in
`generation-count-t29-truncation.witness.json`, not patched with a fitted
scale).  What is closed here is the corpus's *asserted-not-derived*
primality parenthetical, replaced by the continuant-divisibility theorem.
The remaining bridge — "normal-form-independent winding ⟹ physical
generation", plus the mass map — stays open (bean `qou-x4qm`).

-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/lepton-meson-torus-knot-dictionary.md
-/

namespace QOU.Archimedean

open Polynomial

/-! ### Closed forms of the four genus-admissible continuant coefficients -/

/-- `b₃ = X² + 1`. -/
theorem morganVoyceB_three :
    morganVoyceB 3 = X ^ 2 + 1 := by
  simp only [morganVoyceB]; ring

/-- `b₅ = X⁴ + 3X² + 1`. -/
theorem morganVoyceB_five :
    morganVoyceB 5 = X ^ 4 + 3 * X ^ 2 + 1 := by
  simp only [morganVoyceB]; ring

/-- `b₇ = X⁶ + 5X⁴ + 6X² + 1`. -/
theorem morganVoyceB_seven :
    morganVoyceB 7 = X ^ 6 + 5 * X ^ 4 + 6 * X ^ 2 + 1 := by
  simp only [morganVoyceB]; ring

/-- `b₉ = X⁸ + 7X⁶ + 15X⁴ + 10X² + 1`. -/
theorem morganVoyceB_nine :
    morganVoyceB 9 = X ^ 8 + 7 * X ^ 6 + 15 * X ^ 4 + 10 * X ^ 2 + 1 := by
  simp only [morganVoyceB]; ring

/-! ### The harmonic factorisation: `b₃ ∣ b₉` -/

/-- **Winding 9 is a harmonic of generation 1.**  The normal-form
    `σ`-coefficient of `T(2,9)` is the product of `T(2,3)`'s coefficient
    and the explicit cofactor `X⁶ + 6X⁴ + 9X² + 1`, so `b₃ ∣ b₉`.  This
    is the precise form of `σ⁹ = (σ³)³ factors through generation 1` on
    the Gröbner–Shirshov normal-form data. -/
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/lepton-meson-torus-knot-dictionary.md
theorem t29_harmonic_of_first_generation :
    morganVoyceB 9 = morganVoyceB 3 * (X ^ 6 + 6 * X ^ 4 + 9 * X ^ 2 + 1) := by
  rw [morganVoyceB_three, morganVoyceB_nine]; ring

/-- `b₃ ∣ b₉` (the divisibility form of `t29_harmonic_of_first_generation`). -/
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/lepton-meson-torus-knot-dictionary.md
theorem b3_dvd_b9 : morganVoyceB 3 ∣ morganVoyceB 9 :=
  ⟨X ^ 6 + 6 * X ^ 4 + 9 * X ^ 2 + 1, t29_harmonic_of_first_generation⟩

/-! ### Non-divisibility for the prime windings 5 and 7 -/

/-- `X² + 1` is not a unit of `Polynomial ℤ` (it has degree 2), so it
    cannot divide `1`.  Used to turn a unit remainder into a
    non-divisibility. -/
private theorem b3_not_isUnit : ¬ IsUnit (X ^ 2 + 1 : Polynomial ℤ) := by
  intro hu
  have h0 : (X ^ 2 + 1 : Polynomial ℤ).natDegree = 0 :=
    natDegree_eq_zero_of_isUnit hu
  have h2 : (X ^ 2 + 1 : Polynomial ℤ).natDegree = 2 := by compute_degree!
  omega

/-- **Winding 5 is not a harmonic of generation 1.**  `b₅` leaves the
    unit remainder `−1` modulo `b₃` (`b₅ = b₃·(X²+2) − 1`), so a common
    divisor would divide `1`; but `b₃` is not a unit.  Hence `¬ (b₃ ∣ b₅)`. -/
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/lepton-meson-torus-knot-dictionary.md
theorem not_b3_dvd_b5 : ¬ morganVoyceB 3 ∣ morganVoyceB 5 := by
  rw [morganVoyceB_three, morganVoyceB_five]
  intro h
  have hmul : (X ^ 2 + 1 : Polynomial ℤ) ∣ (X ^ 2 + 1) * (X ^ 2 + 2) :=
    dvd_mul_right _ _
  have hone : (X ^ 2 + 1 : Polynomial ℤ) ∣ 1 := by
    have hsub := dvd_sub hmul h
    have hval : (X ^ 2 + 1 : Polynomial ℤ) * (X ^ 2 + 2) - (X ^ 4 + 3 * X ^ 2 + 1) = 1 := by
      ring
    rwa [hval] at hsub
  exact b3_not_isUnit (isUnit_of_dvd_one hone)

/-- **Winding 7 is not a harmonic of generation 1.**  `b₇ = b₃·(X⁴+4X²+2) − 1`,
    the same unit-remainder argument as `not_b3_dvd_b5`. -/
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/lepton-meson-torus-knot-dictionary.md
theorem not_b3_dvd_b7 : ¬ morganVoyceB 3 ∣ morganVoyceB 7 := by
  rw [morganVoyceB_three, morganVoyceB_seven]
  intro h
  have hmul : (X ^ 2 + 1 : Polynomial ℤ) ∣ (X ^ 2 + 1) * (X ^ 4 + 4 * X ^ 2 + 2) :=
    dvd_mul_right _ _
  have hone : (X ^ 2 + 1 : Polynomial ℤ) ∣ 1 := by
    have hsub := dvd_sub hmul h
    have hval : (X ^ 2 + 1 : Polynomial ℤ) * (X ^ 4 + 4 * X ^ 2 + 2)
        - (X ^ 6 + 5 * X ^ 4 + 6 * X ^ 2 + 1) = 1 := by ring
    rwa [hval] at hsub
  exact b3_not_isUnit (isUnit_of_dvd_one hone)

/-- **Generation-exclusion summary.**  Among the four genus-admissible odd
    windings `{3, 5, 7, 9}`, winding 9 is the unique one whose continuant
    coefficient factors through a smaller winding's (`b₃ ∣ b₉`), while the
    prime windings `3, 5, 7` are mutually non-divisible.  This is the
    derived content of the dictionary's asserted "(odd primes)": the
    generations are the odd windings whose normal-form coefficient does not
    factor through a smaller one. -/
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/lepton-meson-torus-knot-dictionary.md
theorem three_generation_windings_are_the_nonharmonic_ones :
    morganVoyceB 3 ∣ morganVoyceB 9 ∧
    ¬ morganVoyceB 3 ∣ morganVoyceB 5 ∧
    ¬ morganVoyceB 3 ∣ morganVoyceB 7 :=
  ⟨b3_dvd_b9, not_b3_dvd_b5, not_b3_dvd_b7⟩

end QOU.Archimedean
