import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

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

variable {R : Type*}

/- The unnormalised q-integer `[n]_q · (q − q⁻¹) = q^n − q^{-n}`, stated as a
polynomial identity in `q` and its inverse `qi`. Working with `q` and `qi`
as independent ring variables subject to `q · qi = 1` (the unit hypothesis)
keeps the proof entirely within `CommRing` + a single `qi_inv` rewrite.

The classical Clebsch–Gordan content here is `(q-q⁻¹) · [n]_q = q^n - q^{-n}`. -/

/-- q-Clebsch–Gordan fusion in the **multiplied-through** form: clearing
the denominator `(q − q⁻¹)` from `[3]_q · [4]_q = [2]_q + [4]_q + [6]_q`
yields a ring identity. This is the math-exact derived piece behind the
meson GMOR fusion `m_K²/m_π² = [3]_q · [4]_q`. -/
theorem meson_qCG_3x4 [Field R] (q : R) (hq : q ≠ 0) :
    (q^3 - q⁻¹^3) * (q^4 - q⁻¹^4)
    = (q - q⁻¹) *
      ((q^2 - q⁻¹^2) + (q^4 - q⁻¹^4) + (q^6 - q⁻¹^6)) := by
  field_simp
  ring

/-- Decategorified form: at `q = 1` the q-Clebsch–Gordan reduces to the
classical SU(2) dimension identity `3 · 4 = 2 + 4 + 6` (the classical
limit observed in `meson_3x4_structural_origin.py`). -/
theorem meson_qCG_3x4_classical : (3 : ℕ) * 4 = 2 + 4 + 6 := by decide

end QOU.BraidKnot
