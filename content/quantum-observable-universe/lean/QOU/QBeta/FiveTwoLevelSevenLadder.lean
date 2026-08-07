import Mathlib.Tactic.LinearCombination

/-!
# The level-7 ladder: the three numerators follow from three five-term instances

Bean `qou-fivt` (Route 11).  Companion to `FiveTwoCyclotomicBloch.lean`.

Route 8 transports the 5₂ saddle sum rule to the totally real cyclotomic field
`ℚ(ζ₇)⁺`; Route 9 reduces it to three explicit values

    Re[2·L(wₖ) + L(−wₖ)] = mₖ·π²/42,   m = (17, 5, −1),   wₖ = 1 + 2cos(2πk/7).

Reducing to `(0,1)` by reflection / inversion / Landen and writing
`q = w₁/(1+w₁)`, `r = w₂/(1+w₂)`, `s = −w₃` (with `1/w₁ = w₃/(w₃−1) = 1 − w₂`),
the three targets become linear statements in `L 1`, `L w₂`, `L q`, `L r`, `L s`.

This file proves them from **three instances of the five-term relation**, taken as
hypotheses, with `L` an **abstract** function — matching the corpus's existing
style in `FiveTwoSaddleSumRule.lean` (where `Li` is abstract and the reflection
identity is an explicit hypothesis).  So nothing here depends on a dilogarithm
implementation, on `qou-clx8`, or on the Bloch group.

The three instances, all with arguments in `(0,1)`:

* `hA` — five-term at `x = y = w₂`
* `hB` — five-term at `x = 1 − w₂`, `y = q`
* `hC` — five-term at `x = w₂`, `y = s`

and the certificate is

    7·T₁ =   hA − 4·hB + 2·hC
    7·T₂ = 4·hA − 2·hB +   hC
    7·T₃ = 2·hA −   hB + 4·hC

The coefficient triples are cyclic shifts of `(1, 2, 4)` — the quadratic residues
mod 7 — which is where the `/7` in `mₖ/7` comes from.

**Scope.** This derives the three numerators *given* the five-term instances and
reflection.  It does **not** prove the five-term relation, the inversion/Landen
extensions, or Route 8's transport.  The 5₂ sum rule remains **verified to 80 dps,
unproved**.
-/

namespace QOU.QBeta.FiveTwoLevelSevenLadder

variable {R : Type*} [CommRing R]

/-- The three level-7 numerators, from three five-term instances plus reflection.

`L1` stands for `L 1`; it is kept abstract so the statement needs no evaluation.

The targets are stated **with the `7` cleared**, as `7·Tₖ = mₖ·L1`. Dividing by
`7` would need `Field R` *and* `CharZero R` — in characteristic `7` the divided
form is false, and `ring` correctly refuses it. Cleared, the certificate has
**integer** coefficients and the result holds over any `CommRing`. -/
theorem numerators_of_five_term
    (L : R → R) (L1 w2 q r s : R)
    -- reflection `L(1−x) = L(1) − L(x)` at the four points used
    (hrw : L (1 - w2) = L1 - L w2)
    (hrq : L (1 - q) = L1 - L q)
    (hrr : L (1 - r) = L1 - L r)
    (hrs : L (1 - s) = L1 - L s)
    -- five-term instances, arguments all in (0,1)
    (hA : 2 * L w2 - L (1 - q) - 2 * L r = 0)
    (hB : L (1 - w2) + L q - L (1 - q) - L (1 - s) - L w2 = 0)
    (hC : L w2 + L s - L (1 - w2) - L (1 - s) - L (1 - r) = 0) :
    (7 * (2 * L1 + 2 * L w2 - L q) = 17 * L1)
      ∧ (7 * (2 * L w2 - L r) = 5 * L1)
      ∧ (7 * (-(2 * L1) + 2 * L w2 + L s) = -L1) := by
  rw [hrw, hrq, hrs] at hB
  rw [hrq] at hA
  rw [hrw, hrs, hrr] at hC
  refine ⟨?_, ?_, ?_⟩
  · linear_combination hA - 4 * hB + 2 * hC
  · linear_combination 4 * hA - 2 * hB + hC
  · linear_combination 2 * hA - hB + 4 * hC

/-- Summing the three numerators: `17 + 5 − 1 = 21`, and `21/7 = 3`.

In the `π²` normalisation this is `Σₖ Re[2L(wₖ)+L(−wₖ)] = π²/2 = 3·L(1)`, which is
Route 8's target and hence the 5₂ sum rule. -/
theorem sum_of_numerators
    (L : R → R) (L1 w2 q r s : R)
    (hrw : L (1 - w2) = L1 - L w2)
    (hrq : L (1 - q) = L1 - L q)
    (hrr : L (1 - r) = L1 - L r)
    (hrs : L (1 - s) = L1 - L s)
    (hA : 2 * L w2 - L (1 - q) - 2 * L r = 0)
    (hB : L (1 - w2) + L q - L (1 - q) - L (1 - s) - L w2 = 0)
    (hC : L w2 + L s - L (1 - w2) - L (1 - s) - L (1 - r) = 0) :
    7 * ((2 * L1 + 2 * L w2 - L q) + (2 * L w2 - L r)
        + (-(2 * L1) + 2 * L w2 + L s)) = 21 * L1 := by
  obtain ⟨h1, h2, h3⟩ := numerators_of_five_term L L1 w2 q r s hrw hrq hrr hrs hA hB hC
  linear_combination h1 + h2 + h3

end QOU.QBeta.FiveTwoLevelSevenLadder
