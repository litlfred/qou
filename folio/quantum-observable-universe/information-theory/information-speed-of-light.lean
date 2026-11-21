import Mathlib.Algebra.Ring.Units


/-!
# QOU.Information.speedOfLight — Speed of light as Lieb–Robinson velocity

The speed of light c_q := 1/(q - 1) is the ratio of the spatial coupling
weight to the temporal coupling weight of the q-connection.

LaTeX label: `def:information-speed-of-light`

## Base ring (AGENTS.md §7c)

Generic `[CommRing k]`.  Nothing here is archimedean — there is no ordering,
no `Real.*` construct, no radical; the content is the single reciprocal
relation `c_q · (q − 1) = 1`.  A field was only ever needed because the two
reciprocals were written as divisions, so both are now carried as **units**:

* `q : kˣ` — the substrate parameter, invertible in the ground ring
  `ℤ[q, q⁻¹]` by construction, so `q⁻¹` is a ring element `↑q⁻¹`;
* `d : kˣ` with `↑d = q − 1` — the temporal coupling weight.  Over a field
  "`q − 1` is a unit" is exactly the old side condition `q ≠ 1`, so no
  generality is lost (recover the field instance with `Units.mk0`).

The ratio statement is correspondingly given in its division-free
(multiplicative) form `c_q · ℏ_q = q⁻¹`; `isUnit_hbar` below proves
`ℏ_q = 1 − q⁻¹` is a unit, so the quoted quotient form
`c_q = q⁻¹ / (1 − q⁻¹)` follows by multiplying through and is not weakened.

## References
- [leitner2026] §9/information-speed-of-light
-/

namespace QOU.Information

variable {k : Type*} [CommRing k]

/-- **Speed of light** at substrate parameter q.

    c_q := 1 / (q - 1)

    The ratio of spatial to temporal information transfer within
    a light cone: spatial coupling weight q⁻¹ divided by temporal
    coupling weight ℏ_q = 1 - q⁻¹.

    §7c: the temporal weight `q − 1` is carried as the unit `d : kˣ`, so
    `c_q` is the ring element `↑d⁻¹` — no field structure is required. -/
-- Ref: [leitner2026] §9/information-speed-of-light
def speedOfLight (d : kˣ) : k := (↑d⁻¹ : k)

/-- **Defining relation, division-free**: `c_q · (q − 1) = 1`, where
    `↑d = q − 1`. This is the whole content of `c_q = 1/(q − 1)`. -/
-- Ref: [leitner2026] §9/information-speed-of-light
theorem speedOfLight_mul (d : kˣ) : speedOfLight d * (d : k) = 1 :=
  Units.inv_mul d

/-- The quantum Planck constant `ℏ_q = 1 − q⁻¹` is a unit, namely
    `↑(d · q⁻¹)` with `↑d = q − 1`.  Consequently the narrative's quotient
    presentation `c_q = q⁻¹ / ℏ_q` is equivalent to the multiplicative form
    proved below — de-specialising to `CommRing` loses nothing. -/
-- Ref: [leitner2026] §9/information-speed-of-light
theorem isUnit_hbar (q d : kˣ) (hd : (d : k) = (q : k) - 1) :
    IsUnit ((1 : k) - (↑q⁻¹ : k)) := by
  have h1 : (1 : k) - (↑q⁻¹ : k) = ((d * q⁻¹ : kˣ) : k) := by
    rw [Units.val_mul, hd, sub_mul, Units.mul_inv, one_mul]
  rw [h1]
  exact Units.isUnit _

/-- **The speed of light equals the ratio `q⁻¹ / ℏ_q`**, stated division-free
    as `c_q · ℏ_q = q⁻¹` with `ℏ_q = 1 − q⁻¹` (the R[h] pattern).

    `1/(q−1) = q⁻¹ · q/(q−1) = q⁻¹/((q−1)/q) = q⁻¹/(1 − q⁻¹)`, i.e.
    `c_q · (1 − q⁻¹) = q⁻¹`. -/
-- Ref: [leitner2026] §9/information-speed-of-light
theorem speedOfLight_mul_hbar (q d : kˣ) (hd : (d : k) = (q : k) - 1) :
    speedOfLight d * ((1 : k) - (↑q⁻¹ : k)) = (↑q⁻¹ : k) := by
  have h1 : (1 : k) - (↑q⁻¹ : k) = (d : k) * (↑q⁻¹ : k) := by
    rw [hd, sub_mul, Units.mul_inv, one_mul]
  rw [h1, speedOfLight, ← mul_assoc, Units.inv_mul, one_mul]

end QOU.Information
