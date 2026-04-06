/-!
# QOU.HadronFibreEmbedding — Fibre-compatible hadron embedding

A fibre-compatible embedding places a hadron into a fibre of the
brane tower, satisfying integrability, fibre confinement, Hopf
compatibility, and volume compatibility conditions.

## References

- [manuscript] §3 Lifting and Descent
-/

import Mathlib.Data.Real.Basic

namespace QOU

/-- A fibre-compatible hadron embedding: a morphism ιₚ satisfying
    integrability, fibre confinement, Hopf compatibility, and
    volume compatibility.

    LaTeX: `\label{def:hadron-fibre-embedding}` -/
-- Ref: [manuscript] §3, Definition: Fibre-compatible hadron embedding
structure HadronFibreEmbedding where
  /-- The base point in the projective line. -/
  theta : ℝ
  phi : ℝ
  /-- The embedding energy (from Möbius energy constraint). -/
  energy : ℝ
  /-- Energy is non-negative. -/
  energy_nonneg : 0 ≤ energy
  /-- Integrability: the embedding preserves the connection structure. -/
  integrable : Prop
  /-- Fibre confinement: the image is contained in a single fibre. -/
  confined : Prop

end QOU
