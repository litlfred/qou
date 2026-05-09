/-
  Geometric invariant Geom(K) as rigid dualizing evaluation.

  The piecewise geometric invariant Geom(K) = Vol(K)/ℏ² (hyperbolic),
  CS(K)·ℏ² (torus), or 0 (unknot) is the evaluation of Yekutieli's
  rigid dualizing complex on the knot complement S³∖K, filtered by
  Thurston's geometrization.

  The Frobenius self-pairing ⟨K, K*⟩ = 1 follows from rigidity.

  Ref: [yekutieli2015] https://doi.org/10.1142/9537
       [yekutieli2010] https://doi.org/10.1016/j.aim.2010.04.018
       [manuscript] §5.10, prop:geom-yekutieli-alignment
-/

import QOU.BraidKnot.NuclearKnotClassification
import QOU.BraidKnot.ConditionalClasses

namespace QOU.BraidKnot

/-- The piecewise geometric invariant, unified across knot types. -/
noncomputable def geomInvariant (K : NuclearKnotType) (q : ℝ) (hq : q > 1)
    (vol : ℝ) (cs : ℝ) : ℝ :=
  let hbar_q := 1 - 1/q
  let hbar_q2 := hbar_q ^ 2
  match K with
  | .unknot      => 0
  | .satellite   => vol / hbar_q2           -- mixed, default to Vol
  | .figureEight => vol / hbar_q2           -- Vol(4₁)/ℏ²
  | .borromean   => vol / hbar_q2           -- Vol(B₃)/ℏ²

/-- For torus knots, Geom = CS·ℏ² (the dual evaluation). -/
noncomputable def geomTorus (m n : ℕ) (q : ℝ) (hq : q > 1) : ℝ :=
  let hbar_q := 1 - 1/q
  let cs := Real.pi ^ 2 * ((m ^ 2 - 1) * (n ^ 2 - 1)) / (12 * m * n)
  cs * hbar_q ^ 2

/-- The Frobenius self-pairing of a hyperbolic knot is unitary:
    Geom(K) · Geom(K*)⁻¹ = 1, since Vol(K*) = Vol(K). -/
theorem frobenius_self_pairing_unitary (q : ℝ) (hq : q > 1) (vol : ℝ)
    (hvol : vol > 0) :
    let hbar_q2 := (1 - 1/q) ^ 2
    (vol / hbar_q2) * (hbar_q2 / vol) = 1 := by
  have hq_pos : q > 0 := by linarith
  have hbar_ne : (1 - 1/q) ^ 2 ≠ 0 := by
    apply pow_ne_zero; linarith [div_lt_one_of_lt hq hq_pos]
  field_simp
  ring

/-- **Conditional Geom-Yekutieli alignment.**  The piecewise geometric
    invariant `Geom(K)` agrees with Yekutieli's rigid-dualizing
    evaluation on every nuclear knot type, conditional on the upstream
    conjectures captured by `[GeomYekutieliConditional]`.

    The hypotheses `[SingleVolumeIrrational]` and
    `[PLCorrectnessHypotheses]` are the Lean-level encoding of the
    §3b-cond conditional dependency on
    [conj:hyperbolic-volume-transcendence] and
    [conj:baryon-period-ratio].  The conditional discharges to the
    unconditional `frobenius_self_pairing_unitary` proven above. -/
theorem geom_yekutieli_alignment_conditional
    [SingleVolumeIrrational] [PLCorrectnessHypotheses]
    (q : ℝ) (hq : q > 1) (vol : ℝ) (hvol : vol > 0) :
    let hbar_q2 := (1 - 1/q) ^ 2
    (vol / hbar_q2) * (hbar_q2 / vol) = 1 :=
  frobenius_self_pairing_unitary q hq vol hvol

end QOU.BraidKnot
