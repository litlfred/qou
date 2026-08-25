import Mathlib.Algebra.Ring.Basic
import Mathlib.Tactic.Ring

/-!
# Meson GMOR fusion identity: [3]_q · [4]_q = [2]_q + [4]_q + [6]_q

The q-Clebsch–Gordan fusion of SU(2)_q irreps. This is the q-deformed
version of the classical CG identity dim(V₁ ⊗ V₃/₂) = dim(V₁/₂ ⊕ V₃/₂ ⊕ V₅/₂),
i.e. 3·4 = 2+4+6.

In the meson sector this is the 2-body qq̄ fusion that gives
`m_K²/m_π² = [3]_q · [4]_q = [2]_q + [4]_q + [6]_q` to 203 ppm (derived,
no fit). See `prop:meson-kaon-pion-fusion-identity` for the categorical
context.

## References

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU.BraidKnot

variable {R : Type*} [CommRing R]

/- The unnormalised q-integer `[n]_q · (q − q⁻¹) = q^n − q^{-n}`, stated as a
polynomial identity in `q` and its inverse `qi`. Working with `q` and `qi`
as independent ring variables subject to `q · qi = 1` (the unit hypothesis)
keeps the proof entirely within `CommRing` — no field, no division.

The classical Clebsch–Gordan content here is `(q-q⁻¹) · [n]_q = q^n - q^{-n}`. -/

/-- q-Clebsch–Gordan fusion in the **multiplied-through** form: clearing
the denominator `(q − q⁻¹)` from `[3]_q · [4]_q = [2]_q + [4]_q + [6]_q`
yields a ring identity. This is the math-exact derived piece behind the
meson GMOR fusion `m_K²/m_π² = [3]_q · [4]_q`.

Base ring (AGENTS.md §7c): stated over a bare `CommRing` with the inverse
carried as the companion variable `qi` subject to the unit relation
`q · qi = 1` — the division-free `ℤ[q, q⁻¹]` form the module docstring
above describes.  A field instance is recovered by taking `qi = q⁻¹` and
`hq = mul_inv_cancel₀`.  The difference of the two sides factors through
the unit relation, so the proof is one `ring` identity plus `hq`; no
`field_simp`, no inverse. -/
theorem meson_qCG_3x4 (q qi : R) (hq : q * qi = 1) :
    (q^3 - qi^3) * (q^4 - qi^4)
    = (q - qi) *
      ((q^2 - qi^2) + (q^4 - qi^4) + (q^6 - qi^6)) := by
  refine sub_eq_zero.mp ?_
  have key :
      (q^3 - qi^3) * (q^4 - qi^4)
        - (q - qi) * ((q^2 - qi^2) + (q^4 - qi^4) + (q^6 - qi^6))
      = (q^3 + q^5 + qi^3 + qi^5 - (q + qi) * (q * qi) * (1 + q * qi))
          * (q * qi - 1) := by
    ring
  rw [key, hq]
  ring

/-- Decategorified form: at `q = 1` the q-Clebsch–Gordan reduces to the
classical SU(2) dimension identity `3 · 4 = 2 + 4 + 6` (the classical
limit observed in `meson_3x4_structural_origin.py`). -/
theorem meson_qCG_3x4_classical : (3 : ℕ) * 4 = 2 + 4 + 6 := by decide

end QOU.BraidKnot
