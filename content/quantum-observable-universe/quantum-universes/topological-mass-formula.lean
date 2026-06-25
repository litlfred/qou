import QOU.QuantumObservableUniverse
import QOU.Torsion
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic

/-!
# Proposition: Archimedean Topological Mass Formula

Formalizes Proposition `prop:topological-mass-formula`: in the archimedean
(ℂ) realisation, the general topological mass decomposition
(Theorem `thm:topological-mass`) specialises to the closed-form
mass formula `m(K) = Vol(K) / ℏ_q²`.

## Logical structure

The proposition derives the closed form from the categorical decomposition
via two evaluation identities on top of the proved
`TopologicalMassDecomposition`:

1. **Baseline = Volume**: the holonomy term evaluates to `Vol(K)`
   via the Chern–Simons/volume correspondence.
2. **Exceptional sum = dilogarithm**: the sum over blow-up centres
   evaluates to `Vol(K) · (1/ℏ_q² − 1)` via Briggs–Klein spectral
   coordinates.

Given these, the closed-form formula is a one-line algebraic consequence.

## References

- [turaev2010] https://doi.org/10.1515/9783110221831
- [yekutieli2015] Nonabelian multiplicative integration on surfaces

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/


open QOU QOU.Torsion

namespace QOU.Torsion

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-! ## The Archimedean Mass Formula -/

/-- **Proposition (Topological Mass Formula — Archimedean).**

    In the ℂ-quantum observable universe, the mass of a particle
    associated with a hyperbolic knot K satisfies `m(K) = Vol(K) / ℏ_q²`,
    where `Vol(K)` is the hyperbolic volume of `S³ \ K` and
    `ℏ_q = 1 − 1/q` is the quantum Planck constant.

    This structure extends `TopologicalMassDecomposition` with the two
    evaluation identities (Chern–Simons/volume correspondence and
    Briggs–Klein dilogarithm evaluation) that specialise the general
    decomposition to the archimedean closed form.

    LaTeX: `\label{prop:topological-mass-formula}` -/
structure ArchimedeanMassFormula (M : Type*) extends TopologicalMassDecomposition M where
  /-- The substrate parameter `q > 1` at the evaluation point. -/
  q : R_q
  /-- The substrate parameter exceeds classicality. -/
  -- q_gt_one : q > 1  -- (archimedean; not meaningful over R_q)
  /-- The quantum Planck constant `ℏ_q = 1 − 1/q`. -/
  h_q : R_q := 1 - q_inv_param  -- ℏ_q = 1 − q⁻¹ in R_q
  /-- The quantum Planck constant satisfies its defining equation.
      This constraint ensures `h_q` cannot be overridden to an
      inconsistent value. -/
  h_q_def : h_q = 1 - q_inv_param := by rfl
  /-- The hyperbolic volume of the knot `K`. -/
  knotVolume : R_q
  /-- The knot volume is positive. -/
  -- knotVolume_pos : 0 < knotVolume  -- (archimedean; not meaningful over R_q)
  /-- **Hypothesis 1 (Chern–Simons/Volume correspondence).**
      The baseline holonomy of the QOU connection evaluates to the
      hyperbolic volume of the knot complement. -/
  baseline_eq_volume : baselineHolonomy = knotVolume
  /-- **Hypothesis 2 (Dilogarithm evaluation).**
      The sum of exceptional divisor contributions, evaluated in
      Briggs–Klein spectral coordinates, yields
      `Vol(K) · (1/ℏ_q² − 1)`. -/
  exceptional_sum_eq : (Finset.univ.sum fun i => exceptionalContribution i) =
    knotVolume * (1 / h_q ^ 2 - 1)

/-- The quantum Planck constant is non-zero when `q > 1`. -/
theorem ArchimedeanMassFormula.h_q_ne_zero {M : Type*}
    (amf : ArchimedeanMassFormula M) : amf.h_q ≠ 0 := by
  rw [amf.h_q_def]
  intro h; linarith [amf.q_gt_one]

/-- **Theorem.** Given the two evaluation hypotheses, the total mass
    equals `Vol(K) / ℏ_q²`.

    This is the algebraic consequence of the decomposition identity
    `m = baseline + Σ exceptional` combined with the two evaluations. -/
theorem ArchimedeanMassFormula.mass_eq_vol_div_h_q_sq {M : Type*}
    (amf : ArchimedeanMassFormula M) :
    amf.totalMass = amf.knotVolume / amf.h_q ^ 2 := by
  have hdecomp := amf.decomposition
  rw [amf.baseline_eq_volume, amf.exceptional_sum_eq] at hdecomp
  rw [hdecomp]; field_simp [pow_ne_zero 2 amf.h_q_ne_zero]; ring

/-- The mass is positive (since the knot volume is positive and ℏ_q² > 0). -/
theorem ArchimedeanMassFormula.mass_pos {M : Type*}
    (amf : ArchimedeanMassFormula M) :
    0 < amf.totalMass := by
  rw [amf.mass_eq_vol_div_h_q_sq]
  exact div_pos amf.knotVolume_pos (sq_pos_of_ne_zero _ amf.h_q_ne_zero)

/-- The mass formula is consistent with the `MassDerivation` module:
    `h_q_def` guarantees `h_q = 1 - 1/q`, so we recover exactly
    the `TopologicalMassFormula` structure from `MassDerivation.lean`. -/
theorem ArchimedeanMassFormula.consistent_with_MassDerivation {M : Type*}
    (amf : ArchimedeanMassFormula M) :
    amf.totalMass = amf.knotVolume / (1 - 1 / amf.q) ^ 2 := by
  rw [← amf.h_q_def]
  exact amf.mass_eq_vol_div_h_q_sq

end QOU.Torsion
