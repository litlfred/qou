import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Group.Invertible.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

/-!
# Meson EM sinh-channel correction: closed-form identity

The substrate Planck-quantum truncation `(1 + ℏ_q − ℏ_q²/2)` that closes
the meson m_K²/m_π² ratio to sub-ppm has a clean rational-polynomial
closed form `(3q² − 1)/(2q²) = (3 − q⁻²)/2`. This file proves the
chain of ring identities.

## Structural reading

- Numerator `3q² − 1`: **3** is the number of saturating-genus
  generation torus knots on Bring's surface (T(2,3), T(2,5), T(2,7) —
  the three generations); `q²` is the substrate's squared coupling.
- Denominator `2q²`: 2 is the EM-self-energy halving (Casimir);
  `q²` puts the correction on the substrate-natural scale.

Per #1417's `[n]_q = sinh(nλ)/sinh(λ)` theorem (sinh = Coulomb), this
is the sinh-channel categorical correction on the qq̄ pair, modulo a
rigorous derivation of the truncation order from first principles.

## References

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/


namespace QOU.BraidKnot

/-! §7c: the identities below are **exact in `q`** and need no field at all.
Two invertibility facts carry the whole content, each in its weakest form:

* `q` enters only through `q` and `q⁻¹`, so it is carried as a **unit**
  `q : Rˣ` of a bare `CommRing R` and the inverse is the coercion `↑q⁻¹` —
  not a field inverse of a nonzero element.
* halving the EM self-energy needs only `[Invertible (2 : R)]`, written `⅟(2 : R)`;
  that is the exact characteristic condition (`2` a unit), strictly weaker than the
  former `[Field R] [CharZero R]`.

No ordering, radical or `Real.*` construct appears, so nothing here crosses the
substrate→archimedean wall; the physical meson EM correction factors are obtained
downstream by instantiating `R := ℝ`, `q := Units.mk0 q_0 _`. -/

variable {R : Type*} [CommRing R] [Invertible (2 : R)]

/-- The substrate Planck quantum `ℏ_q = (q − 1)·q⁻¹ = 1 − q⁻¹`.

    `q` is carried as a unit of `R`, so `q⁻¹` is the unit inverse (§7c) and no
    field structure is required. -/
def hbarQ (q : Rˣ) : R := ((q : R) - 1) * ((↑q⁻¹ : R))

omit [Invertible (2 : R)] in
/-- `ℏ_q = 1 − q⁻¹` — the division-free normal form of the Planck quantum,
    the identity `(q − 1)·q⁻¹ = 1 − q⁻¹` that the unit relation `q·q⁻¹ = 1`
    supplies. -/
theorem hbarQ_eq (q : Rˣ) : hbarQ q = 1 - ((↑q⁻¹ : R)) := by
  unfold hbarQ
  rw [sub_mul, q.mul_inv, one_mul]

/-- The sinh-channel EM correction factor in closed form:
    `1 + ℏ_q − ℏ_q²·⅟2 = (3q² − 1)·⅟2·(q⁻¹)²` (i.e. `(3q² − 1)/(2q²)`). -/
theorem meson_EM_closed_form (q : Rˣ) :
    1 + hbarQ q - (hbarQ q) ^ 2 * ⅟(2 : R)
      = (3 * (q : R) ^ 2 - 1) * ⅟(2 : R) * ((↑q⁻¹ : R)) ^ 2 := by
  have hqi : (q : R) * ((↑q⁻¹ : R)) = 1 := q.mul_inv
  have h2 : (2 : R) * ⅟(2 : R) = 1 := mul_invOf_self 2
  unfold hbarQ
  linear_combination
    (1 - 4 * ⅟(2 : R) * (q : R) * ((↑q⁻¹ : R)) - 4 * ⅟(2 : R)
      + 2 * ⅟(2 : R) * ((↑q⁻¹ : R))) * hqi
    + (((↑q⁻¹ : R)) - 2) * h2

/-- Equivalent form: `(3q² − 1)·⅟2·(q⁻¹)² = (3 − (q⁻¹)²)·⅟2`. -/
theorem meson_EM_closed_form_inverse (q : Rˣ) :
    (3 * (q : R) ^ 2 - 1) * ⅟(2 : R) * ((↑q⁻¹ : R)) ^ 2
      = (3 - ((↑q⁻¹ : R)) ^ 2) * ⅟(2 : R) := by
  have hqi : (q : R) * ((↑q⁻¹ : R)) = 1 := q.mul_inv
  linear_combination (3 * ⅟(2 : R) * ((q : R) * ((↑q⁻¹ : R)) + 1)) * hqi

/-- Equivalent form: `1 + ℏ_q − ℏ_q²·⅟2 = 1 + (1 − (q⁻¹)²)·⅟2`. -/
theorem meson_EM_closed_form_planck (q : Rˣ) :
    1 + hbarQ q - (hbarQ q) ^ 2 * ⅟(2 : R)
      = 1 + (1 - ((↑q⁻¹ : R)) ^ 2) * ⅟(2 : R) := by
  have hqi : (q : R) * ((↑q⁻¹ : R)) = 1 := q.mul_inv
  have h2 : (2 : R) * ⅟(2 : R) = 1 := mul_invOf_self 2
  unfold hbarQ
  linear_combination
    (1 - ⅟(2 : R) * (q : R) * ((↑q⁻¹ : R)) - ⅟(2 : R)
      + 2 * ⅟(2 : R) * ((↑q⁻¹ : R))) * hqi
    + (((↑q⁻¹ : R)) - 1) * h2

end QOU.BraidKnot
