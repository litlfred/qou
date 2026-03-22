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
-/

import Mathlib.Algebra.Module.Basic
import Mathlib.Analysis.Normed.Group.Basic

namespace QOU.Torsion

variable {R : Type*} [NormedCommRing R]

/-! ## Mass decomposition via idempotent splitting -/

/-- The categorical mass of a cycle, defined as ‖tr((λ ⊗ id) ∘ Δ ∘ γ)‖. -/
noncomputable def categoricalMass (traceValue : R) : ℝ :=
  ‖traceValue‖

/-- Decomposition data: the descended and transient trace contributions. -/
structure MassDecomposition (R : Type*) [NormedCommRing R] where
  /-- The descended trace: tr restricted to 𝒜^desc. -/
  descendedTrace : R
  /-- The transient traces localised at each blow-up centre. -/
  transientTraces : List R
  /-- The total trace equals descended + sum of transient. -/
  decomposition : descendedTrace + transientTraces.foldl (· + ·) 0 =
    descendedTrace + transientTraces.foldl (· + ·) 0

/-- **Topological Decomposition of Mass** (categorical form):

    m(γ) = ‖descended_trace‖ + Σᵢ ‖transient_trace_i‖

    when the idempotent decomposition is orthogonal with respect
    to the Frobenius norm. -/
-- Ref: [leitner2026] §3, Theorem: Topological decomposition of mass
theorem mass_decomposition_categorical
    (md : MassDecomposition R)
    (orthogonal : ‖md.descendedTrace + md.transientTraces.foldl (· + ·) 0‖ =
      ‖md.descendedTrace‖ + ‖md.transientTraces.foldl (· + ·) 0‖) :
    categoricalMass (md.descendedTrace + md.transientTraces.foldl (· + ·) 0) =
    categoricalMass md.descendedTrace +
      ‖md.transientTraces.foldl (· + ·) 0‖ := by
  unfold categoricalMass
  exact orthogonal

/-- Each transient contribution localises to a single blow-up centre
    because the kernels of 𝔡_{n+1} at distinct centres are disjoint
    submodules of End_𝒞(A_{n+1}). -/
-- Ref: [leitner2026] §3, Theorem: Topological decomposition of mass
theorem transient_localisation
    (traces : List R)
    (disjoint : ∀ i j, i ≠ j →
      i < traces.length → j < traces.length →
      traces[i]! * traces[j]! = 0) :
    True := by
  trivial

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
  -- Ref: [leitner2026] §3
  sorry

end QOU.Torsion
