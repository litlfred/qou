import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# QOU.Archimedean.tau_leptonic_universality — tau leptonic universality

**Proposition** ([`prop:tau-leptonic-universality`](../../../quantum-observable-universe/archimedean-universe/tau-leptonic-universality.md)).

*Let `T_{3,5} = (σ₀ σ₁)⁵` be the weak vertex in `H₃(q)`, and let
`f(x) = 1 − 8x + 8x³ − x⁴ − 12 x² ln x` be the phase-space factor
for `τ → ℓ ν̄_ℓ ν_τ` with `x = (m_ℓ / m_τ)²`.  In the factorised
model, the Markov trace of the weak vertex is the universal matrix
element*

```
|M_e|² = |M_μ|² = |tr_Markov(T_{3,5})|²
```

*so the branching-ratio ratio reduces to the pure phase-space ratio:*

```
BR(τ → e) / BR(τ → μ) = f(m_e²/m_τ²) / f(m_μ²/m_τ²).
```

The Lean encoding defines the phase-space factor `phaseSpace` as an
explicit real-valued function of `x ∈ (0, 1)` and records the
universality claim as an equality of branching-ratio quotients.

-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/tau-leptonic-universality.md
-/

namespace QOU.Archimedean

/-- The leptonic-decay phase-space factor `f(x) = 1 − 8x + 8x³ − x⁴
    − 12 x² ln x`, defined for `x > 0` (the `ln x` is `Real.log`). -/
noncomputable def phaseSpace (x : ℝ) : ℝ :=
  1 - 8 * x + 8 * x ^ 3 - x ^ 4 - 12 * x ^ 2 * Real.log x

/-- Boundary value: `f(0) = 1` (massless-daughter limit).

    Strictly speaking `phaseSpace` evaluates to `1 - 0 - 0 - 0 - 12·0·log 0`
    at `x = 0`; the `12 x² · log x` term has limit 0 as `x → 0⁺`, and
    `Real.log 0 = 0` by Mathlib convention, so the formula evaluates
    to `1` at `x = 0`. -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/tau-leptonic-universality.md
theorem phaseSpace_at_zero : phaseSpace 0 = 1 := by
  simp [phaseSpace, Real.log_zero]

/-- Boundary value: `f(1) = 0` (degenerate daughter mass).

    `f(1) = 1 − 8 + 8 − 1 − 12·1·log 1 = 0 − 12·0 = 0`. -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/tau-leptonic-universality.md
theorem phaseSpace_at_one : phaseSpace 1 = 0 := by
  simp [phaseSpace, Real.log_one]

/-- Abstract context for the tau-leptonic-universality claim.

    The **factorisation hypotheses** `BR_ℓ_factored` encode the physical
    content of the manuscript: each leptonic branching fraction factors as a
    *universal* squared matrix element times the daughter-dependent
    phase-space factor,

      `BR(τ → ℓ) = |𝓜|² · f((m_ℓ / m_τ)²)`,

    with the **same** `weakVertexTraceSq = |tr_Markov(T_{3,5})|²` for both
    channels — this shared value is exactly the universality
    `|𝓜_e|² = |𝓜_μ|² = |tr_Markov((σ₀σ₁)⁵)|²`.  The Markov trace of the
    weak vertex is a property of the vertex alone (a class function on
    `H_3(q)`; cf. `QOU.MathlibExt.MarkovTrace.character_append_comm` — the
    trace is invariant under the braid word's cyclic structure), so it does
    not depend on the daughter lepton.  Its archimedean (real) evaluation at
    the substrate `q₀` is the scalar `weakVertexTraceSq`. -/
class TauLeptonicContext where
  -- Witness: computations/none
  /-- Electron rest mass (MeV). -/
  m_e : ℝ
  /-- Muon rest mass (MeV). -/
  m_μ : ℝ
  /-- Tau rest mass (MeV). -/
  m_τ : ℝ
  /-- Branching fraction `BR(τ → e ν̄_e ν_τ)`. -/
  BR_e : ℝ
  /-- Branching fraction `BR(τ → μ ν̄_μ ν_τ)`. -/
  BR_μ : ℝ
  /-- Positivity of masses. -/
  m_e_pos : 0 < m_e
  m_μ_pos : 0 < m_μ
  m_τ_pos : 0 < m_τ
  /-- BR_μ ≠ 0 so the ratio is well-defined. -/
  BR_μ_ne_zero : BR_μ ≠ 0
  /-- The **universal** squared weak matrix element
      `|𝓜|² = |tr_Markov(T_{3,5})|²` (real evaluation at `q₀`), shared by
      both leptonic channels. -/
  weakVertexTraceSq : ℝ
  /-- The universal matrix element is non-zero (the weak vertex is a
      non-trivial mediator), so it cancels in the branching ratio. -/
  weakVertexTraceSq_ne_zero : weakVertexTraceSq ≠ 0
  /-- Factorisation for `τ → e`: universal matrix element × phase space. -/
  BR_e_factored : BR_e = weakVertexTraceSq * phaseSpace ((m_e / m_τ) ^ 2)
  /-- Factorisation for `τ → μ` — **same** `weakVertexTraceSq` (universality). -/
  BR_μ_factored : BR_μ = weakVertexTraceSq * phaseSpace ((m_μ / m_τ) ^ 2)

/-- **Tau leptonic universality** ([`prop:tau-leptonic-universality`]).

    In the factorised model, the ratio of leptonic branching
    fractions equals the pure phase-space ratio:

      `BR(τ → e) / BR(τ → μ) = f(m_e²/m_τ²) / f(m_μ²/m_τ²)`.

    Stated against an abstract `TauLeptonicContext`; the matrix
    element universality
    `|M_e|² = |M_μ|² = |tr_Markov(T_{3,5})|²` is recorded in the
    `phaseSpace`-only RHS. -/
-- Ref: [leitner2026] quantum-observable-universe/predicted-spectra/tau-leptonic-universality.md
theorem tau_leptonic_universality [ctx : TauLeptonicContext] :
    ctx.BR_e / ctx.BR_μ
      = phaseSpace ((ctx.m_e / ctx.m_τ) ^ 2)
        / phaseSpace ((ctx.m_μ / ctx.m_τ) ^ 2) := by
  -- Substitute the two factorisations; the shared universal matrix element
  -- `weakVertexTraceSq = |tr_Markov(T_{3,5})|²` cancels between numerator and
  -- denominator (`mul_div_mul_left`, valid since it is non-zero), leaving the
  -- pure phase-space quotient.
  rw [ctx.BR_e_factored, ctx.BR_μ_factored,
      mul_div_mul_left _ _ ctx.weakVertexTraceSq_ne_zero]

end QOU.Archimedean
