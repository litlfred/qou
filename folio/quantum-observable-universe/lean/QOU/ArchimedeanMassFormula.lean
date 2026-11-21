import QOU.QuantumObservableUniverse
import QOU.Torsion
import QOU.MathlibExt.ManifoldVolumePositive
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# Conjecture: Archimedean Topological Mass Formula

Formalizes Proposition `conj:topological-mass-formula`: in the archimedean
(ℂ) realisation, the general topological mass decomposition
(`conj:topological-mass`, open since 2026-11-20) specialises to the closed-form
mass formula `m(K) = Vol(K) / ℏ_q²`.

## Logical structure

The proposition derives the closed form from the categorical decomposition
via two evaluation identities on top of `TopologicalMassDecomposition`,
whose `decomposition` field carries the equality of `conj:topological-mass`
as a hypothesis:

1. **Baseline = Volume**: the holonomy term evaluates to `Vol(K)`
   via the Chern–Simons/volume correspondence.
2. **Exceptional sum = dilogarithm**: the sum over blow-up centres
   evaluates to `Vol(K) · (1/ℏ_q² − 1)` via Briggs–Klein spectral
   coordinates.

Given these, the closed-form formula is a one-line algebraic consequence.

## References

- [turaev2010] https://doi.org/10.1515/9783110221831
- [yekutieli2015] Nonabelian multiplicative integration on surfaces
-/


open QOU QOU.Torsion

namespace QOU.Torsion

/-! ## The Archimedean Mass Formula -/

/-- **Conjecture carrier (Topological Mass Formula — Archimedean).**

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
  /-- The substrate parameter `q > 1` at the evaluation point. -/
  q : ℝ
  /-- The substrate parameter exceeds classicality. -/
  q_gt_one : q > 1
  /-- The quantum Planck constant `ℏ_q = 1 − 1/q`. -/
  h_q : ℝ := 1 - 1 / q
  /-- The quantum Planck constant satisfies its defining equation.
      This constraint ensures `h_q` cannot be overridden to an
      inconsistent value. -/
  h_q_def : h_q = 1 - 1 / q := by rfl
  /-- The type of 3-manifolds (knot complements) carrying the
      triangulation-to-volume bridge.  Bean `qou-dx7g`: until 2026-11-20
      `knotVolume` was a free real, so "`Vol(K)`" referred to no knot and
      `knotVolume = baselineHolonomy = 1` satisfied the structure. -/
  KnotSpace : Type
  /-- The hyperbolic-volume bridge on `KnotSpace` (Thurston's theorem, carried
      as a hypothesis; `QOU.MathlibExt.HyperbolicVolumeBridge`). -/
  volBridge : QOU.MathlibExt.HyperbolicVolumeBridge KnotSpace
  /-- The knot complement `S³ \ K`. -/
  knot : KnotSpace
  /-- `K` is hyperbolic: some ideal triangulation realises its complement. -/
  knot_hyperbolic : ∃ (n : ℕ) (T : QOU.MathlibExt.IdealTriangulation n),
    volBridge.Realises T knot
  /-- The hyperbolic volume of the knot `K`. -/
  knotVolume : ℝ
  /-- **`Vol(K)` is the volume of the knot**, not a free real: it is the bridge
      volume of the realised complement. -/
  knotVolume_eq_vol : knotVolume = volBridge.vol knot
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

/-- **The knot volume is positive** — derived (bean `qou-dx7g`), no longer a
    field: the complement is realised by a triangulation, which the bridge
    requires to be nonempty, and nonempty ideal triangulations have positive
    volume (`ManifoldVolumePositive.vol_pos_of_realises'`). -/
theorem ArchimedeanMassFormula.knotVolume_pos {M : Type*}
    (amf : ArchimedeanMassFormula M) : 0 < amf.knotVolume := by
  obtain ⟨n, T, hT⟩ := amf.knot_hyperbolic
  rw [amf.knotVolume_eq_vol]
  exact @QOU.MathlibExt.ManifoldVolumePositive.vol_pos_of_realises' _ amf.volBridge n T
    amf.knot hT

/-- The quantum Planck constant is non-zero when `q > 1`. -/
theorem ArchimedeanMassFormula.h_q_ne_zero {M : Type*}
    (amf : ArchimedeanMassFormula M) : amf.h_q ≠ 0 := by
  rw [amf.h_q_def]
  have hq := amf.q_gt_one
  have hq_ne : amf.q ≠ 0 := ne_of_gt (lt_trans zero_lt_one hq)
  intro h
  have : 1 / amf.q = 1 := by linarith
  have : amf.q = 1 := by field_simp at this; linarith
  linarith

/-- **Theorem.** Given the two evaluation hypotheses, the total mass
    equals `Vol(K) / ℏ_q²`.

    This is the algebraic consequence of the decomposition identity
    `m = baseline + Σ exceptional` combined with the two evaluations. -/
theorem ArchimedeanMassFormula.mass_eq_vol_div_h_q_sq {M : Type*}
    (amf : ArchimedeanMassFormula M) :
    amf.totalMass = amf.knotVolume / amf.h_q ^ 2 := by
  -- From TopologicalMassDecomposition: totalMass = baseline + Σ exceptional
  have hdecomp := amf.decomposition
  -- Substitute the two evaluation hypotheses
  rw [amf.baseline_eq_volume, amf.exceptional_sum_eq] at hdecomp
  -- Now: totalMass = knotVolume + knotVolume * (1/h_q² - 1)
  -- Simplify: = knotVolume * (1 + 1/h_q² - 1) = knotVolume / h_q²
  have h_ne : amf.h_q ^ 2 ≠ 0 := pow_ne_zero 2 amf.h_q_ne_zero
  rw [hdecomp]
  field_simp
  ring

/-- The mass is positive (since the knot volume is positive and ℏ_q² > 0). -/
theorem mass_pos {M : Type*}
    (amf : ArchimedeanMassFormula M) :
    0 < amf.totalMass := by
  rw [amf.mass_eq_vol_div_h_q_sq]
  apply div_pos amf.knotVolume_pos
  exact sq_pos_of_ne_zero amf.h_q_ne_zero

/-- The mass formula is consistent with the `MassDerivation` module:
    `h_q_def` guarantees `h_q = 1 - 1/q`, so we recover exactly
    the `TopologicalMassFormula` structure from `MassDerivation.lean`. -/
theorem consistent_with_MassDerivation {M : Type*}
    (amf : ArchimedeanMassFormula M) :
    amf.totalMass = amf.knotVolume / (1 - 1 / amf.q) ^ 2 := by
  rw [← amf.h_q_def]
  exact amf.mass_eq_vol_div_h_q_sq

end QOU.Torsion
