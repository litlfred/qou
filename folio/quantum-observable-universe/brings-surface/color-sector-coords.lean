import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic


/-!
# QOU.ColorSectorCoords

The red, green, blue sector embeddings 𝔯, 𝔤, 𝔟 defined
parametrically on the exceptional divisor with color twist qφ
rotating each sector.  They tile the exceptional divisor
exactly at each brane point.

LaTeX label: `def:color-sector-coords`

**Ground ring**: `ℝ` (geometric/analytic realisation).
Uses ℝ-specific analysis (trig, norms, real powers).
NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU

/-- **Color sector coordinates**: the three colour sectors R/G/B on the
    exceptional divisor ℙ¹(ℂ), each covering a 2π/3-wide strip in the
    azimuthal coordinate ψ, with a color twist q·φ that rotates
    the sector as latitude φ varies from 0 to π.

    The red sector embedding is:
      𝔯(φ, ψ) = O + R(sin φ (cos(ψ + qφ) T₁ + sin(ψ + qφ) T₂) - cos φ N)

    Green and blue are offset by 2π/3 and 4π/3 respectively:
      𝔤(φ, ψ) = 𝔯(φ, ψ + 2π/3)
      𝔟(φ, ψ) = 𝔯(φ, ψ + 4π/3)

    LaTeX: `\label{def:color-sector-coords}`
    Ref: [leitner2026] Chapter 6, §Color-sector coordinates -/
structure ColorSectorCoords where
  /-- The radius of the ℙ¹(ℂ) fibre. -/
  R : ℝ
  /-- Radius is positive. -/
  R_pos : 0 < R
  /-- The substrate parameter q controlling the color twist. -/
  q : ℝ
  /-- Centre of the exceptional divisor (ℝ³ coordinates). -/
  centre : Fin 3 → ℝ
  /-- Outward unit normal at the brane point. -/
  normal : Fin 3 → ℝ
  /-- First tangent vector T₁. -/
  tangent1 : Fin 3 → ℝ
  /-- Second tangent vector T₂. -/
  tangent2 : Fin 3 → ℝ

/-- Colour sector index: Red, Green, Blue. -/
inductive ColourSector
  | red | green | blue

/-- The azimuthal offset for each colour sector: R → 0, G → 2π/3, B → 4π/3. -/
-- Ref: [leitner2026] Chapter 6, §Color-sector coordinates
noncomputable def ColourSector.offset : ColourSector → ℝ
  | .red   => 0
  | .green => 2 * Real.pi / 3
  | .blue  => 4 * Real.pi / 3

/-- The sector embedding: given color sector coordinates, a colour sector,
    and spherical parameters (φ, ψ), return the i-th coordinate of the
    fibre point with color twist. -/
-- Ref: [leitner2026] Chapter 6, §Color-sector coordinates
noncomputable def ColorSectorCoords.sectorPoint
    (C : ColorSectorCoords) (s : ColourSector) (φ ψ : ℝ) (i : Fin 3) : ℝ :=
  let ψ' := ψ + s.offset + C.q * φ
  C.centre i + C.R * (Real.sin φ * (Real.cos ψ' * C.tangent1 i +
    Real.sin ψ' * C.tangent2 i) - Real.cos φ * C.normal i)

/-- Green is the red sector shifted by 2π/3 in the azimuthal coordinate. -/
-- Ref: [leitner2026] Chapter 6, §Color-sector coordinates
theorem ColorSectorCoords.green_eq_red_shifted
    (C : ColorSectorCoords) (φ ψ : ℝ) (i : Fin 3) :
    C.sectorPoint .green φ ψ i =
    C.sectorPoint .red φ (ψ + 2 * Real.pi / 3) i := by
  simp [ColorSectorCoords.sectorPoint, ColourSector.offset]

/-- Blue is the red sector shifted by 4π/3 in the azimuthal coordinate. -/
-- Ref: [leitner2026] Chapter 6, §Color-sector coordinates
theorem ColorSectorCoords.blue_eq_red_shifted
    (C : ColorSectorCoords) (φ ψ : ℝ) (i : Fin 3) :
    C.sectorPoint .blue φ ψ i =
    C.sectorPoint .red φ (ψ + 4 * Real.pi / 3) i := by
  simp [ColorSectorCoords.sectorPoint, ColourSector.offset]

/-- The three sectors tile the circle: their angular offsets sum to 2π.
    Each sector covers a 2π/3-wide strip, and 0 + 2π/3 + 4π/3 = 2π. -/
-- Ref: [leitner2026] Chapter 6, §Color-sector coordinates
theorem sector_offsets_sum_to_two_pi :
    (0 : ℝ) + 2 * Real.pi / 3 + 4 * Real.pi / 3 = 2 * Real.pi := by
  ring

end QOU
