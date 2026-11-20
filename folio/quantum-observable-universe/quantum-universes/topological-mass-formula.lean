import QOU.QuantumObservableUniverse
import QOU.Torsion
import Mathlib.Data.Real.Basic

/-!
# Proposition: Archimedean Topological Mass Formula

Formalizes Proposition `conj:topological-mass-formula`: in the archimedean
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

## Base ring (§7c)

This is an **archimedean** object: division `1/ℏ_q²`, the ordering
`q > 1`, and positivity `0 < Vol(K)` are all used, and the parent
`TopologicalMassDecomposition` already types `totalMass`,
`baselineHolonomy`, and `exceptionalContribution` over `ℝ`.  The
formula therefore lives over `ℝ` (the substrate parameter is evaluated
at `q₀ ≈ 1.1097` post-`τ`-functor).

## References

- [turaev2010] https://doi.org/10.1515/9783110221831
- [yekutieli2015] Nonabelian multiplicative integration on surfaces
-/


open QOU QOU.Torsion

namespace QOU.Torsion

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

    LaTeX: `\label{conj:topological-mass-formula}` -/
structure ArchimedeanMassFormula (M : Type*) extends TopologicalMassDecomposition M where
  /-- The substrate parameter `q` at the evaluation point. -/
  q : ℝ
  /-- The substrate parameter exceeds classicality (`q > 1`). -/
  q_gt_one : q > 1
  /-- The quantum Planck constant `ℏ_q = 1 − 1/q`. -/
  h_q : ℝ := 1 - 1 / q
  /-- The quantum Planck constant satisfies its defining equation.
      This constraint ensures `h_q` cannot be overridden to an
      inconsistent value. -/
  h_q_def : h_q = 1 - 1 / q := by rfl
  /-- The hyperbolic volume of the knot `K`. -/
  knotVolume : ℝ
  /-- The knot volume is positive. -/
  knotVolume_pos : 0 < knotVolume
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

/-- The quantum Planck constant is non-zero when `q > 1`
    (then `1/q < 1`, so `ℏ_q = 1 − 1/q > 0`). -/
theorem ArchimedeanMassFormula.h_q_ne_zero {M : Type*}
    (amf : ArchimedeanMassFormula M) : amf.h_q ≠ 0 := by
  rw [amf.h_q_def]
  have hq : (0 : ℝ) < amf.q := by linarith [amf.q_gt_one]
  have hlt : 1 / amf.q < 1 := by rw [div_lt_one hq]; exact amf.q_gt_one
  have hpos : (0 : ℝ) < 1 - 1 / amf.q := by linarith
  exact ne_of_gt hpos

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
  have hsq : 0 < amf.h_q ^ 2 := by
    have := amf.h_q_ne_zero
    positivity
  exact div_pos amf.knotVolume_pos hsq

/-- The mass formula is consistent with the `MassDerivation` module:
    `h_q_def` guarantees `h_q = 1 - 1/q`, so we recover exactly
    the `TopologicalMassFormula` structure from `MassDerivation.lean`. -/
theorem ArchimedeanMassFormula.consistent_with_MassDerivation {M : Type*}
    (amf : ArchimedeanMassFormula M) :
    amf.totalMass = amf.knotVolume / (1 - 1 / amf.q) ^ 2 := by
  rw [← amf.h_q_def]
  exact amf.mass_eq_vol_div_h_q_sq

end QOU.Torsion
