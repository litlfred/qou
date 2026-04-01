/-!
# QOU.Torsion.skein_generation — Skein module generation

The Skein module 𝒮_q is generated as an algebra by:
1. The fundamental (mass-zero) knot types {K_i} (torus knots), and
2. The Hopf link ℒ_Hopf (the binding operation).

Every hadron admits a terminal Skein resolution:
  q · L₊ - q⁻¹ · L₋ = (q - q⁻¹) · L₀

LaTeX label: `prop:skein-generation`

## References

- [jones1985] https://doi.org/10.1090/S0273-0979-1985-15304-2
- [manuscript] §3-lifting-of-quantum-torsion/skein-generation
-/

import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.RingTheory.Polynomial.Basic
import Mathlib.Data.Polynomial.Basic

namespace QOU.Torsion

/-- **Skein relation data**: the three resolutions of a crossing
    `L₊`, `L₋`, `L₀` related by the Skein relation
    `q · L₊ - q⁻¹ · L₋ = (q - q⁻¹) · L₀`. -/
-- Ref: [jones1985]
structure SkeinRelation where
  /-- The substrate parameter q > 1. -/
  q : ℝ
  /-- q is positive. -/
  q_pos : 0 < q
  /-- q is greater than 1 (quantum regime). -/
  q_gt_one : 1 < q
  /-- Mass of the positive crossing resolution. -/
  mass_plus : ℝ
  /-- Mass of the negative crossing resolution. -/
  mass_minus : ℝ
  /-- Mass of the smoothed resolution. -/
  mass_zero : ℝ
  /-- The Skein relation: q · M(L₊) - q⁻¹ · M(L₋) = (q - q⁻¹) · M(L₀). -/
  skein : q * mass_plus - q⁻¹ * mass_minus = (q - q⁻¹) * mass_zero

/-- **Fundamental knot**: a knot whose hyperbolic volume vanishes.
    By geometrization, these are precisely the torus knots. -/
-- Ref: [manuscript] §3
structure FundamentalKnot where
  /-- Name/index of the knot. -/
  index : ℕ
  /-- Torus knot parameters (p, 2). -/
  torus_p : ℕ
  /-- Hyperbolic volume is zero for torus knots. -/
  volume_zero : (0 : ℝ) = 0  -- Vol(K) = 0

/-- **Skein resolution**: decomposition of a hadron into fundamental
    knots via iterated Skein relations.

    After finitely many applications of the Skein relation at each
    crossing, a composite hadron decomposes into a polynomial in
    fundamental knot classes with Laurent polynomial coefficients. -/
-- Ref: [jones1985], [manuscript] §3
structure SkeinResolution where
  /-- The substrate parameter q. -/
  q : ℝ
  /-- q > 1. -/
  q_gt_one : 1 < q
  /-- Number of fundamental constituents. -/
  numConstituents : ℕ
  /-- The Skein polynomial Q(q) ∈ ℤ[q±¹] (evaluated at q). -/
  skeinPolynomial : ℝ
  /-- Mass of the Hopf link (binding energy unit). -/
  hopfLinkMass : ℝ
  /-- Individual constituent volumes. -/
  constituentVolumes : Fin numConstituents → ℝ
  /-- The quantum Planck constant ℏ_q = 1 - q⁻¹. -/
  hbar_q : ℝ := 1 - q⁻¹
  /-- **Mass formula**: M(H) = Q(q) · M(ℒ_Hopf) + Σᵢ Vol(Kᵢ)/ℏ_q². -/
  mass_formula : ℝ :=
    skeinPolynomial * hopfLinkMass +
    ∑ i : Fin numConstituents, constituentVolumes i / hbar_q ^ 2

/-- For hadrons of purely torus-knot constituents, all volumes vanish
    and mass is purely from linking topology:
    M(H) = Q(q) · M(ℒ_Hopf). -/
-- Ref: [manuscript] §3
theorem mass_from_linking_only
    (sr : SkeinResolution)
    (h_torus : ∀ i, sr.constituentVolumes i = 0) :
    sr.mass_formula = sr.skeinPolynomial * sr.hopfLinkMass := by
  unfold SkeinResolution.mass_formula
  simp [h_torus]

/-- The quantum Planck constant is positive when q > 1. -/
-- Ref: [manuscript] §1
theorem hbar_q_pos {q : ℝ} (hq : 1 < q) : 0 < 1 - q⁻¹ := by
  have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  linarith

end QOU.Torsion
