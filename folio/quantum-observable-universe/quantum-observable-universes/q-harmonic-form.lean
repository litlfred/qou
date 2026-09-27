import QOU.QuantumObservableUniverse.Particles
import Mathlib.Data.Real.Basic


/-!
# QOU.QHarmonicForm

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/QHarmonicForm.lean (monolithic).
That file no longer exists — the library was split, and `QHarmonicForm` now lives at
  content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/Particles.lean

**Archimedean realisation.** A q-harmonic form (particle) is the
archimedean realisation of a section in the kernel of the q-Laplacian
`Δ_q = d_q δ_q + δ_q d_q`. The Reeb decomposition and the per-point
q-Laplacian value are evaluated over `ℝ` (matching
`QOU.ReebDecomposition`, whose components are `M → ℝ`).
-/

namespace QOU

universe u v

/-- **q-Harmonic form (Particle)**: a section `α` in the kernel of the
    q-Laplacian `Δ_q = d_q δ_q + δ_q d_q`, i.e. `Δ_q α = 0`.

    LaTeX: `\label{def:q-harmonic-form}` -/
structure QHarmonicForm' (M : Type*) extends ReebDecomposition M where
  /-- The q-Laplacian value `Δ_q(α)` at each point. -/
  q_laplacian : M → ℝ
  /-- The q-Laplacian vanishes: `Δ_q α = 0`. -/
  q_laplacian_vanishes : ∀ (p : M), q_laplacian p = 0

end QOU
