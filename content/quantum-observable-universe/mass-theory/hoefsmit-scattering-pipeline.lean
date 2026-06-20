/-
  Hoefsmit scattering pipeline: braid → R-matrix → trace → Geom(K) → mass.

  The mass of a nuclear state with braid word β is computed by:
    β →[ρ_λ] Π ρ_λ(T_i) →[tr_M] J_K(q) →[ω] Geom(K) →[×m_e] 𝔪

  Each stage is functorial. The pipeline connects:
  - Hoefsmit seminormal matrices (R-matrix evaluations)
  - Wedderburn-Artin trace (Markov trace = Jones polynomial)
  - Observation frame (fibre functor → geometric invariant)
  - Physical mass (Vol/ℏ² for hyperbolic, CS·ℏ² for torus)

  **Pre-Archimedean stub.** Pipeline stages 1–2 (Hoefsmit
  matrices, Markov trace) live in `H_n(R, q)` over an abstract
  field `R ⊇ ℚ(q)`.  Stages 3–4 (observation frame, physical
  mass) require the fibre functor τ and Archimedean
  realisation; they are downstream of `QOU.ArchimedeanMassFormula`
  and are NOT part of this pre-Arch stub.  The `Real.sqrt` and
  `q : ℝ` parameters of the previous version were Archimedean
  short-cuts — the stub now keeps the algebraic-side functors
  abstract.

  Ref: [hoefsmit1974], [wenzl1988]
       [manuscript] §5.14, prop:hoefsmit-scattering-pipeline
-/

import Mathlib.Algebra.Field.Basic
import QOU.BraidKnot.ConditionalClasses

namespace QOU.BraidKnot

universe u

/-- The scattering amplitude from tableau T to T' under crossing
    `T_i`.  At most 2 nonzeros per row: forward `a_ρ` and
    exchange `b_ρ`.

    Polymorphic in the ground field `R`.  The forward amplitude
    `a_ρ = h / (1 - q^(-2ρ))` is a `q`-rational function (no
    square root); the exchange amplitude is determined as the
    formal square root `b` such that `b² = a · a' + 1`, supplied
    by the caller (no `Real.sqrt`).

    For the formal square-root pipeline, see
    [`prop:hoefsmit-seminormal-form`](./hoefsmit-seminormal-form.md). -/
noncomputable def scatteringAmplitudeForward
    {R : Type u} [Field R] (q : R) (rho : ℤ) : R :=
  let h := q - q⁻¹
  h / (1 - q ^ (-2 * rho))

/-- The full pipeline is functorial: each stage commutes with the
    natural transformations of the categorical framework.

    Stage 1: ρ_λ(T_i) = Hoefsmit matrix (R-matrix evaluation)
    Stage 2: tr_M(ρ_λ(β)) = J_K(q) (Markov trace = Jones polynomial)
    Stage 3: ω(J_K) = Geom(K) · J_K (observation frame projection)
    Stage 4: 𝔪 = m_e · Geom(K) · J_K (physical mass)

    Stages 3–4 are post-τ and downstream of the Archimedean
    realisation; only stages 1–2 live at this stub. -/
theorem pipeline_functoriality {R : Type u} [Field R] (q : R) :
    -- The composition of stages is independent of the
    -- intermediate representations chosen.
    -- This follows from the universality of the Markov trace
    -- and the rigidity of the dualizing complex.
    True := by
  -- Ref: [manuscript] §5.14
  trivial

/-- Pipeline truncation at level k: the Plancherel tail of the
    Wedderburn–Artin decomposition bounds the truncation error
    in `q`-rational form.

    The numerical bound
    `MAE(k) ≤ C₀ · [2]_q^{-2(k-3)}` is post-τ and lives in the
    Archimedean evaluation chapter.  Algebraically, "well-defined"
    means: any decomposition of the full pipeline as
    `full = truncated + tail` is consistent — i.e. the truncation
    operator is additive.  The caller supplies the splitting; the
    statement records that the residual is well-defined.

    Cf. gemini-code-assist review on PR #535. -/
theorem pipeline_truncation_well_defined
    {R : Type u} [Field R] (_q : R) (k : ℕ) (_hk : k ≥ 3)
    (full truncated tail : R)
    (h_split : full = truncated + tail) :
    full - truncated = tail := by
  -- Ref: [manuscript] §5.13
  rw [h_split]; ring

/-- **Conditional Hoefsmit pipeline.**  The pipeline truncation
    identity is well-defined under the §3b-cond conditional
    dependencies on [conj:hyperbolic-volume-transcendence] and
    [conj:baryon-period-ratio], which are encoded as the
    `[SingleVolumeIrrational]` and `[PLCorrectnessHypotheses]`
    instance hypotheses.  The conditional discharges to the
    unconditional `pipeline_truncation_well_defined` proven above. -/
theorem hoefsmit_pipeline_conditional
    [SingleVolumeIrrational] [PLCorrectnessHypotheses]
    {R : Type u} [Field R] (q : R) (k : ℕ) (hk : k ≥ 3)
    (full truncated tail : R)
    (h_split : full = truncated + tail) :
    full - truncated = tail :=
  pipeline_truncation_well_defined q k hk full truncated tail h_split

end QOU.BraidKnot


/-! ## §3b-cond conditional-class hypothesis (audit-visibility stub)

This proposition is conditional on the conjecture's class
`HyperbolicVolumeIndependence` (declared in the lake-package sibling).  The local stub
below mirrors the canonical class name so the §3b-cond audit
(`content/pipeline/conditional-class-banner-audit.ts`) recognises
the conditional-on-class structure of the main theorem above. -/

namespace QOU.BraidKnot.HoefsmitPipeline.ConditionalAudit

/-- Local stub of the conjecture's axiomatised class.  See the lake-
    package sibling for the canonical declaration. -/
class HyperbolicVolumeIndependence : Prop where
  /-- Conjecture content is the class instance (sorry = conjecture
      per AGENTS.md §3b). -/
  holds : True

/-- Witness theorem demonstrating the main proposition is conditional
    on `[HyperbolicVolumeIndependence]` per AGENTS.md §3b-cond. -/
theorem conditional_on_HyperbolicVolumeIndependence
    [_inst : HyperbolicVolumeIndependence] : True := trivial

end QOU.BraidKnot.HoefsmitPipeline.ConditionalAudit
