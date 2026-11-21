import Mathlib.Tactic

/-!
# The 5₂ gluing rows at the cubic shape — the algebraic spine of the two-bridge derivation

Companion to `computations/probes/two_bridge_layered_nz_probe.py` (bean `qou-yvyd`). That probe
builds the layered triangulation of the two-bridge knot complement `S³ ∖ 5₂ = S(7,3)` from the
Farey word `RL` (two flip tetrahedra per letter on the 4-punctured sphere, the end folds found by
exhaustive search under manifold / one-cusp / `H₁ = ℤ` / geometric filters) and finds the complete
structure with shapes

  `z₀ = z₁ = θ`,  `z₂ = z₃ = θ² − 1`,   where  `θ³ − θ + 1 = 0`,

the cubic of discriminant `−23` — the shape field of `5₂`, which the search never sees. Its four
derived edge rows, in rect form `Π z^a (1−z)^b = ±1`, are

  `(1,1,−1,−1 | 1,1,1,1 ; +)`, `(0,0,−1,−1 | −2,−2,−1,−1 ; +)`,
  `(−1,0,1,1 | 1,0,0,0 ; −)`, `(0,−1,1,1 | 0,1,0,0 ; −)`.

The probe verifies each row exactly by reduction modulo `θ³ − θ + 1` in `ℚ[θ]`; this file states
the same identities as theorems over any commutative ring in which `θ³ − θ + 1 = 0`, with the
denominators cleared. Nothing geometric is asserted here (that `Im θ > 0` for the complex root
picks the orientation is the probe's `Im z > 0` check); these are the exact identities the
geometry rests on, in the sense of the formalize-first rule.

-- Ref: [leitner2026] computations/probes/two_bridge_layered_nz_probe.py
-- Ref: library/arxiv-0808.2716v4 §2.4 (Futer–Kalfagianni–Purcell) — two-bridge layering.
-/

namespace QOU.Mass.FiveTwoGluingFromFareyWord

variable {K : Type*} [CommRing K]

/-- The shape field of `5₂`: the cubic `x³ − x + 1` has discriminant `−4·(−1)³ − 27·1² = −23`. -/
theorem shape_cubic_discriminant : (-4 : ℤ) * (-1) ^ 3 - 27 * 1 ^ 2 = -23 := by norm_num

/-- Row 3, `(−1,0,1,1 | 1,0,0,0 ; −)`: `−(1 − z₀) z₂ z₃ / z₀ = 1`, cleared of the denominator, at
`z₀ = θ`, `z₂ = z₃ = θ² − 1`. -/
theorem row_three {θ : K} (h : θ ^ 3 - θ + 1 = 0) :
    -(1 - θ) * (θ ^ 2 - 1) ^ 2 = θ := by
  linear_combination (θ ^ 2 - θ - 1) * h

/-- Row 4 is row 3 with `z₁` in place of `z₀`; the shapes coincide, so it is the same identity. -/
theorem row_four {θ : K} (h : θ ^ 3 - θ + 1 = 0) :
    -(1 - θ) * (θ ^ 2 - 1) ^ 2 = θ :=
  row_three h

/-- Row 1, `(1,1,−1,−1 | 1,1,1,1 ; +)`: `z₀ z₁ (1−z₀)(1−z₁)(1−z₂)(1−z₃) / (z₂ z₃) = 1`, cleared:
`θ² (1−θ)² (2−θ²)² = (θ²−1)²`. -/
theorem row_one {θ : K} (h : θ ^ 3 - θ + 1 = 0) :
    θ ^ 2 * (1 - θ) ^ 2 * (2 - θ ^ 2) ^ 2 = (θ ^ 2 - 1) ^ 2 := by
  linear_combination ((θ - 1) ^ 2 * (θ ^ 3 - 3 * θ - 1)) * h

/-- Row 2, `(0,0,−1,−1 | −2,−2,−1,−1 ; +)`: `1 / (z₂ z₃ (1−z₀)² (1−z₁)² (1−z₂)(1−z₃)) = 1`,
cleared: `(θ²−1)² (1−θ)⁴ (2−θ²)² = 1`. -/
theorem row_two {θ : K} (h : θ ^ 3 - θ + 1 = 0) :
    (θ ^ 2 - 1) ^ 2 * (1 - θ) ^ 4 * (2 - θ ^ 2) ^ 2 = 1 := by
  linear_combination ((θ ^ 3 - 2 * θ ^ 2 - θ + 3) *
    (θ ^ 6 - 2 * θ ^ 5 - 2 * θ ^ 4 + 6 * θ ^ 3 - θ ^ 2 - 4 * θ + 1)) * h

/-- All four derived rows hold at the cubic shape, bundled. -/
theorem all_rows {θ : K} (h : θ ^ 3 - θ + 1 = 0) :
    θ ^ 2 * (1 - θ) ^ 2 * (2 - θ ^ 2) ^ 2 = (θ ^ 2 - 1) ^ 2 ∧
    (θ ^ 2 - 1) ^ 2 * (1 - θ) ^ 4 * (2 - θ ^ 2) ^ 2 = 1 ∧
    -(1 - θ) * (θ ^ 2 - 1) ^ 2 = θ :=
  ⟨row_one h, row_two h, row_three h⟩

/-! ### The cusp rows (added 2026-09-07, PR #6985)

`two_bridge_cusp_rows_apoly_probe.py` derives the meridian row `(0,0,1,0 | 1,1,0,1 ; +)` — the
Bézout complement of the homological longitude, pinned as the meridian by the Dehn-filling test —
and the longitude row `(0,0,5,−1 | 4,4,−3,7 ; +)`. At the cubic shape both are `1`; with
`z₂ = z₃` the longitude row is the fourth power of the meridian row, so one identity carries
both. -/

/-- The meridian row at the cubic shape: `z₂ (1−z₀)(1−z₁)(1−z₃) = (θ²−1)(1−θ)²(2−θ²) = 1`. -/
theorem meridian_row {θ : K} (h : θ ^ 3 - θ + 1 = 0) :
    (θ ^ 2 - 1) * (1 - θ) ^ 2 * (2 - θ ^ 2) = 1 := by
  linear_combination (-θ ^ 3 + 2 * θ ^ 2 + θ - 3) * h

/-- The longitude row at the cubic shape, `z₂⁵ z₃⁻¹ (1−z₀)⁴(1−z₁)⁴(1−z₂)⁻³(1−z₃)⁷` with
`z₂ = z₃`, cleared: `(θ²−1)⁴ (1−θ)⁸ (2−θ²)⁴ = 1` — the fourth power of the meridian identity. -/
theorem longitude_row {θ : K} (h : θ ^ 3 - θ + 1 = 0) :
    (θ ^ 2 - 1) ^ 4 * (1 - θ) ^ 8 * (2 - θ ^ 2) ^ 4 = 1 := by
  have hm := meridian_row h
  calc (θ ^ 2 - 1) ^ 4 * (1 - θ) ^ 8 * (2 - θ ^ 2) ^ 4
      = ((θ ^ 2 - 1) * (1 - θ) ^ 2 * (2 - θ ^ 2)) ^ 4 := by ring
    _ = 1 := by rw [hm]; ring

end QOU.Mass.FiveTwoGluingFromFareyWord
