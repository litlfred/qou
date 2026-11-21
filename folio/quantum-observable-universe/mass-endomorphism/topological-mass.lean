import Mathlib.Algebra.Module.Basic
import Mathlib.Analysis.Normed.Group.Basic
import Mathlib.Analysis.Normed.Ring.Basic
import Mathlib.Data.Real.Basic
import Mathlib.LinearAlgebra.Projection
import Mathlib.Tactic


/-!
# QOU.Torsion.topological_mass — Topological decomposition of mass

The mass m(γ) of a closed cycle γ : 𝟙 → A decomposes via the descent
involution τₙ into descended and transient contributions:

  m(γ) = ‖tr_desc(γ)‖ + Σᵢ ‖tr_trans(γ, pᵢ)‖

where the first term is the trace restricted to 𝒜^desc (the baseline
drag from the Frobenius–Hopf structure) and each summand extracts the
transient contribution localised at the i-th blow-up centre.

This is a categorical statement: the decomposition follows from the
idempotent splitting of End_𝒞(A_{n+1}) and the linearity of the trace.

## References

- [leitner2026] §3 Lifting and Descent

**Ground ring**: `ℝ` (geometric/analytic realisation).
Uses ℝ-specific analysis (trig, norms, real powers).
NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Torsion

variable {R : Type*} [NormedCommRing R]

/-! ## Mass decomposition via idempotent splitting -/

/-- The categorical mass of a cycle, defined as ‖tr((λ ⊗ id) ∘ Δ ∘ γ)‖. -/
noncomputable def categoricalMass (traceValue : R) : ℝ :=
  ‖traceValue‖

/-- Decomposition data: the descended and transient trace contributions,
    derived from an idempotent splitting. -/
structure MassDecomposition (R : Type*) [NormedCommRing R] where
  /-- The descended trace: tr restricted to 𝒜^desc = im(τ). -/
  descendedTrace : R
  /-- The transient trace: tr restricted to 𝒜^trans = ker(τ). -/
  transientTrace : R
  /-- The total cycle trace value (before decomposition). -/
  totalTrace : R
  /-- The total trace decomposes as descended + transient.
      This follows from the idempotent splitting: any x decomposes
      as τ(x) + (x - τ(x)), so tr(x) = tr(τ(x)) + tr(x - τ(x)). -/
  decomposition : totalTrace = descendedTrace + transientTrace

/-- **Topological Decomposition of Mass** (trace-level):

    From the algebraic decomposition `tr = tr_desc + tr_trans`,
    the mass decomposes as:
    `m(γ) = ‖tr_desc + tr_trans‖`

    The triangle inequality gives:
    `m(γ) ≤ ‖tr_desc‖ + ‖tr_trans‖`

    This is always valid. Equality holds when the descended and transient
    components are "Frobenius-orthogonal" (norm-additive). -/
-- Ref: [leitner2026] §3, Theorem: Topological decomposition of mass
theorem mass_upper_bound (md : MassDecomposition R) :
    categoricalMass md.totalTrace ≤
    categoricalMass md.descendedTrace + categoricalMass md.transientTrace := by
  unfold categoricalMass
  rw [md.decomposition]
  exact norm_add_le md.descendedTrace md.transientTrace

/-- **Norm additivity for non-negative traces**: when both the descended
    and transient trace values are non-negative — as guaranteed by the
    Frobenius pairing in the archimedean realisation, where trace values
    are norms of holonomies — the mass decomposes exactly (not just as
    an upper bound).

    For `R = ℝ`, this is provable from non-negativity alone, eliminating
    the need for an axiom.  The original product-zero hypothesis
    (`descendedTrace * transientTrace = 0`) was mathematically incorrect:
    in a `NormedCommRing` without zero divisors (such as `ℝ`) it forces
    one component to vanish (making the decomposition vacuous), and in
    rings with zero divisors it does not imply norm additivity.

    The correct physical content is that both trace components are
    non-negative reals: the descended trace is `‖Hol_{∇_A}(γ₀)‖ ≥ 0`
    and each transient trace is `‖Φ_q(zᵢ)‖ ≥ 0`.  For non-negative
    reals, `‖a + b‖ = |a + b| = a + b = |a| + |b| = ‖a‖ + ‖b‖`. -/
-- Ref: [leitner2026] §3, Theorem: Topological decomposition of mass
-- Ref: [kock2004] Kock, "Frobenius Algebras and 2D Topological Quantum Field Theories," CUP LMS Student Texts 59, 2004
theorem norm_additivity_of_nonneg_traces
    (md : MassDecomposition ℝ)
    -- The descended trace is non-negative (norm of holonomy).
    (h_desc_nonneg : 0 ≤ md.descendedTrace)
    -- The transient trace is non-negative (norm of dilogarithm).
    (h_trans_nonneg : 0 ≤ md.transientTrace) :
    ‖md.totalTrace‖ = ‖md.descendedTrace‖ + ‖md.transientTrace‖ := by
  rw [md.decomposition, Real.norm_of_nonneg (add_nonneg h_desc_nonneg h_trans_nonneg),
      Real.norm_of_nonneg h_desc_nonneg, Real.norm_of_nonneg h_trans_nonneg]

/-- **Exact mass decomposition** under non-negativity of traces:
    m(γ) = m_desc(γ) + m_trans(γ). -/
-- Ref: [leitner2026] §3, Theorem: Topological decomposition of mass
theorem mass_decomposition_exact
    (md : MassDecomposition ℝ)
    (h_desc_nonneg : 0 ≤ md.descendedTrace)
    (h_trans_nonneg : 0 ≤ md.transientTrace) :
    categoricalMass md.totalTrace =
    categoricalMass md.descendedTrace + categoricalMass md.transientTrace := by
  unfold categoricalMass
  exact norm_additivity_of_nonneg_traces md h_desc_nonneg h_trans_nonneg

/-- The descended trace equals the trace of the base-level cycle γ₀,
    because τₙ projects onto im(ℓₙ) ≅ End_𝒞(Aₙ). -/
-- Ref: [leitner2026] §3, Theorem: Topological decomposition of mass
theorem descended_trace_is_base_level
    {N : Type*} [AddCommGroup N] [Module R N]
    {M : Type*} [AddCommGroup M] [Module R M]
    (ℓ : N →ₗ[R] M) (𝔡 : M →ₗ[R] N)
    (retraction : 𝔡 ∘ₗ ℓ = LinearMap.id)
    (trN : N →ₗ[R] R) (trM : M →ₗ[R] R)
    (trace_compat : ∀ x, trN (𝔡 x) = trM x)
    (γ₀ : N) :
    trM (ℓ γ₀) = trN γ₀ := by
  rw [← trace_compat (ℓ γ₀)]; congr 1
  simpa [LinearMap.comp_apply] using congr_fun (congr_arg DFunLike.coe retraction) γ₀

/-- The idempotent decomposition produces a valid MassDecomposition. -/
-- Ref: [leitner2026] §3
theorem idempotent_gives_mass_decomposition
    {M : Type*} [AddCommGroup M] [Module R M]
    (τ : M →ₗ[R] M) (h_idem : τ ∘ₗ τ = τ)
    (tr : M →ₗ[R] R) (x : M) :
    tr x = tr (τ x) + tr (x - τ x) := by
  rw [map_sub, add_sub_cancel]

end QOU.Torsion
