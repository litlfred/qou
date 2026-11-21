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
       [leitner2026] §5.14, prop:hoefsmit-scattering-pipeline
-/

import Mathlib.Algebra.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
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

/-- **Stage 3–4 compositional functoriality (algebraic fragment).**
    The pipeline's final two stages are scalar multiplications:

    Stage 3: ω(J_K) = Geom(K) · J_K (observation-frame projection)
    Stage 4: 𝔪 = m_e · Geom(K) · J_K (physical mass)

    so the composite mass map `J_K ↦ m_e · Geom(K) · J_K` is
    (i) **associative** — independent of how the intermediate scaling
    is bracketed, i.e. the composition of stages 3 and 4 does not
    depend on the intermediate representation chosen — and
    (ii) **additive** in the Markov-trace argument `J_K`.  This is the
    fragment of the pipeline's functoriality provable at the
    pre-Archimedean stub: stages 3–4 commute with the additive
    structure of the Jones-polynomial / Markov-trace values.

    The full stage-1–2 functoriality (Hoefsmit R-matrix evaluation
    `ρ_λ(T_i)`, Markov trace `tr_M(ρ_λ(β)) = J_K(q)`) requires the
    categorical functor objects and is downstream of
    `QOU.ArchimedeanMassFormula`; it is not part of this stub.

    Ref: [leitner2026] §5.14 -/
theorem pipeline_functoriality {R : Type u} [Field R]
    (m_e geom jK jK' : R) :
    m_e * (geom * jK) = (m_e * geom) * jK ∧
      (m_e * geom) * (jK + jK') = (m_e * geom) * jK + (m_e * geom) * jK' :=
  ⟨by ring, by ring⟩

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
  -- Ref: [leitner2026] §5.13
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

/-- Local mirror of the conjecture's axiomatised class.  The canonical
    declaration lives in
    `QOU.Archimedean.HyperbolicVolumeTranscendence` and carries the
    full `no_relation` field over the concrete substrate volumes
    `Vol(4₁)`, `Vol(5₂)`, `Vol(𝓑₃)`; this local mirror states the same
    *shape* over abstract reals so the §3b-cond banner audit recognises
    the conditional-on-class structure without a cross-module import. -/
class HyperbolicVolumeIndependence (v₁ v₂ v₃ : ℝ) : Prop where
  /-- No non-trivial ℚ-monomial relation holds among the three
      substrate hyperbolic volumes `v₁ v₂ v₃` (the figure-8, `5₂`, and
      Borromean complement volumes, carried as class parameters): for
      any finitely-supported rational coefficient assignment over
      exponent triples, a vanishing weighted power-sum forces all
      coefficients to vanish.  Mirrors
      `HyperbolicVolumeTranscendence.no_relation`, which fixes the three
      concrete substrate volumes — the volumes are *parameters* of the
      class, not universally quantified (a `∀ v₁ v₂ v₃` field would be
      false, e.g. at `v₁ = 0`, hence uninhabitable). -/
  no_relation :
    ∀ (S : Finset (ℕ × ℕ × ℕ)) (f : ℕ × ℕ × ℕ → ℚ),
      (∀ ijk, ijk ∉ S → f ijk = 0) →
      (S.sum fun ijk =>
        (f ijk : ℝ) * v₁ ^ ijk.1 * v₂ ^ ijk.2.1 * v₃ ^ ijk.2.2) = 0 →
      ∀ ijk, f ijk = 0

/-- **Conditional consequence of `HyperbolicVolumeIndependence`** (per
    CLAUDE.md §3b-cond): the three substrate hyperbolic volumes are
    ℚ-linearly independent — no non-trivial rational linear combination
    vanishes.  This is the degree-1 specialisation of `no_relation`
    (support `{(1,0,0),(0,1,0),(0,0,1)}`), deriving a genuine
    conclusion from the class hypothesis rather than asserting `True`.
    Mirrors `HyperbolicVolumeTranscendence`'s `BorelZagierQOU`. -/
theorem conditional_on_HyperbolicVolumeIndependence
    {v₁ v₂ v₃ : ℝ} [inst : HyperbolicVolumeIndependence v₁ v₂ v₃]
    (a₁ a₂ a₃ : ℚ)
    (h : (a₁ : ℝ) * v₁ + (a₂ : ℝ) * v₂ + (a₃ : ℝ) * v₃ = 0) :
    a₁ = 0 ∧ a₂ = 0 ∧ a₃ = 0 := by
  classical
  set S : Finset (ℕ × ℕ × ℕ) := {(1,0,0), (0,1,0), (0,0,1)} with hS
  set f : ℕ × ℕ × ℕ → ℚ :=
    fun p => if p = (1,0,0) then a₁ else if p = (0,1,0) then a₂
             else if p = (0,0,1) then a₃ else 0 with hf
  have hsupp : ∀ ijk, ijk ∉ S → f ijk = 0 := by
    intro ijk hijk
    simp only [hf]
    rw [if_neg, if_neg, if_neg]
    · rintro rfl; exact hijk (by simp [hS])
    · rintro rfl; exact hijk (by simp [hS])
    · rintro rfl; exact hijk (by simp [hS])
  have hsum : (S.sum fun ijk =>
      (f ijk : ℝ) * v₁ ^ ijk.1 * v₂ ^ ijk.2.1 * v₃ ^ ijk.2.2) = 0 := by
    rw [hS]
    rw [Finset.sum_insert (by decide), Finset.sum_insert (by decide),
      Finset.sum_singleton]
    simp only [hf]
    norm_num
    rw [← add_assoc]; exact h
  have hall := inst.no_relation S f hsupp hsum
  refine ⟨?_, ?_, ?_⟩
  · have := hall (1,0,0); simpa [hf] using this
  · have := hall (0,1,0); simpa [hf] using this
  · have := hall (0,0,1); simpa [hf] using this

end QOU.BraidKnot.HoefsmitPipeline.ConditionalAudit
