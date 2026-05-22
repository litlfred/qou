/-!
# QOU.Descartes.morse_wall_q_moduli — Morse wall of the integration-limit pencil

The baryon integration-limit Möbius transformation
`a(q) = (4 - q) / (4*q + 3)` has fixed points at `q^2 + q - 1 = 0` —
i.e. at `1/φ` and `-φ` — and these constitute the **Morse wall** of
the q-family of SW actions `S_q` on `E_q`: the algebraic locus where
the integration-limit pencil's Möbius section becomes stationary.

This file proves the **polynomial Morse-wall identity**:

  given any commutative ring `R` and elements `q, u : R` such that
  `u * (4*q + 3) = 1` (i.e. `u` is a left-inverse of `4q+3`),
  the fixed-point equation `(4 - q) * u = q` is equivalent to the
  polynomial identity `4 * (q^2 + q - 1) = 0`.

The "4 *" multiplier on the RHS is the artefact of the algebraic
manipulation; it does NOT require `(4 : R)` to be a unit. Over rings
of characteristic 0 (or any ring where 4 is a non-zero-divisor),
this reduces to `q^2 + q - 1 = 0`, recovering the closed-form fixed
points `{1/φ, -φ}` after adjoining `√5 ∈ ℤ[ζ_5]`.

-- Ref: [pham1965] generalised Picard-Lefschetz formula
-- Ref: [seidel2008] Fukaya-Seidel category of a Lefschetz fibration
-- Ref: [arnold-gusein-zade-varchenko1988] Singularities II §10-11
-/

import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

namespace QOU.Descartes

/-- **Morse-wall identity.**
    Over any commutative ring `R` with element `q : R` and a
    left-inverse `u` of `4*q + 3` (i.e. `u * (4*q + 3) = 1`),
    the Möbius fixed-point equation `(4 - q) * u = q` is equivalent
    to the polynomial identity `4 * (q^2 + q - 1) = 0`.

    The multiplier `4` on the RHS is universal (no characteristic
    assumption); over rings where `(4 : R)` is a non-zero-divisor
    (e.g. characteristic 0), this collapses to `q^2 + q - 1 = 0`. -/
theorem morse_wall_q_moduli
    {R : Type*} [CommRing R] (q u : R)
    (hu : u * (4 * q + 3) = 1) :
    (4 - q) * u = q ↔ 4 * (q^2 + q - 1) = 0 := by
  refine ⟨?_, ?_⟩
  · -- Forward: (4 - q) * u = q  ⟹  4·(q²+q-1) = 0.
    -- Multiply hq by (4q+3) and use hu to eliminate u.
    intro hq
    have h2 : 4 - q = q * (4 * q + 3) := by
      have step : (4 - q) * (u * (4 * q + 3)) = q * (4 * q + 3) := by
        have : (4 - q) * (u * (4 * q + 3)) = (4 - q) * u * (4 * q + 3) := by ring
        rw [this, hq]
      rwa [hu, mul_one] at step
    -- h2 says 4 - q = 4q² + 3q, i.e. 4q² + 4q - 4 = 0.
    linear_combination -h2
  · -- Reverse: 4·(q²+q-1) = 0  ⟹  (4 - q) * u = q.
    -- The polynomial identity gives 4 - q = q·(4q+3); multiply by u
    -- on the right and use hu : u·(4q+3) = 1 to collapse.
    intro h
    have h2 : 4 - q = q * (4 * q + 3) := by linear_combination -h
    have step : (4 - q) * u = q * ((4 * q + 3) * u) := by
      rw [h2]; ring
    rw [step, mul_comm (4 * q + 3) u, hu, mul_one]

end QOU.Descartes
