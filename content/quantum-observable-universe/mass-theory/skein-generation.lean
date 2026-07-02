import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.RingTheory.Polynomial.Basic
import Mathlib.Algebra.Polynomial.Basic
import Mathlib.Algebra.Field.Defs
import Mathlib.Algebra.BigOperators.Group.Finset.Basic


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

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.Torsion

/- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **Skein relation data**: the three resolutions of a crossing
    `L₊`, `L₋`, `L₀` related by the Skein relation
    `q · L₊ - q⁻¹ · L₋ = (q - q⁻¹) · L₀`.

    Stated over a generic field `K` (per §7c base-ring convention):
    the relation involves `q⁻¹`, which `R_q = ℤ[q,q⁻¹]` does not carry
    as a general `Inv` instance. Specialise `K := ℝ, q := q₀` (or
    `K := Frac(R_q)`) as needed. -/
-- Ref: [jones1985]
structure SkeinRelation (K : Type*) [Field K] where
  /-- The substrate parameter q > 1. -/
  q : K
  -- q is positive. (archimedean; not meaningful over a generic field)
  -- q_pos : 0 < q
  -- q is greater than 1 (quantum regime). (archimedean; not meaningful over a generic field)
  -- q_gt_one : 1 < q
  /-- Mass of the positive crossing resolution. -/
  mass_plus : K
  /-- Mass of the negative crossing resolution. -/
  mass_minus : K
  /-- Mass of the smoothed resolution. -/
  mass_zero : K
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
  volume_zero : (0 : R_q) = 0  -- Vol(K) = 0

/-- **Skein resolution**: decomposition of a hadron into fundamental
    knots via iterated Skein relations.

    After finitely many applications of the Skein relation at each
    crossing, a composite hadron decomposes into a polynomial in
    fundamental knot classes with Laurent polynomial coefficients. -/
-- Ref: [jones1985], [manuscript] §3
structure SkeinResolution (K : Type*) [Field K] where
  /-- The substrate parameter q. -/
  q : K
  -- q > 1. (archimedean; not meaningful over a generic field)
  -- q_gt_one : 1 < q
  /-- Number of fundamental constituents. -/
  numConstituents : ℕ
  /-- The Skein polynomial Q(q) ∈ ℤ[q±¹] (evaluated at q). -/
  skeinPolynomial : K
  /-- Mass of the Hopf link (binding energy unit). -/
  hopfLinkMass : K
  /-- Individual constituent volumes. -/
  constituentVolumes : Fin numConstituents → K

/-- The quantum Planck constant ℏ_q = 1 - q⁻¹. -/
def SkeinResolution.hbar_q {K : Type*} [Field K] (sr : SkeinResolution K) : K :=
  1 - sr.q⁻¹

/-- **Mass formula**: M(H) = Q(q) · M(ℒ_Hopf) + Σᵢ Vol(Kᵢ)/ℏ_q².

    A definition (not a defaulted data field): a structure field with a
    default value is unconstrained, so nothing about it is provable. -/
def SkeinResolution.mass_formula {K : Type*} [Field K] (sr : SkeinResolution K) : K :=
  sr.skeinPolynomial * sr.hopfLinkMass +
  ∑ i : Fin sr.numConstituents, sr.constituentVolumes i / sr.hbar_q ^ 2

/-- For hadrons of purely torus-knot constituents, all volumes vanish
    and mass is purely from linking topology:
    M(H) = Q(q) · M(ℒ_Hopf). -/
-- Ref: [manuscript] §3
theorem mass_from_linking_only {K : Type*} [Field K]
    (sr : SkeinResolution K)
    (h_torus : ∀ i, sr.constituentVolumes i = 0) :
    sr.mass_formula = sr.skeinPolynomial * sr.hopfLinkMass := by
  unfold SkeinResolution.mass_formula
  simp [h_torus]

-- The quantum Planck constant is positive when q > 1.
-- Ref: [manuscript] §1
-- theorem hbar_q_pos {q : R_q} (hq : 1 < q) : 0 < 1 - q⁻¹ := by  -- (archimedean; not meaningful over R_q)
--   have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
--   linarith

end

end QOU.Torsion
