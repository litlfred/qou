import QOU.Archimedean.GroundRing
import Mathlib.Data.Real.Basic


/-!
# QOU.QuantumObservableUniverses.QAnalysis — q-analysis display structures

Authoritative library home for three q-analysis structures previously
defined only inside content-object display snippets
(`quantum-observable-universes/q-resolvent.lean`, `q-heat-equation.lean`,
`q-dilogarithm.lean`).  Relocated here (2026-06-09 axiom audit) so the
companion `*-unique.lean` display files can `import` the real structures
and carry genuinely type-checked uniqueness statements rather than
referencing auto-bound type variables.

Ground ring `R_q = ℤ[q, q⁻¹]` is taken from `QOU.Archimedean.GroundRing`.

## References

- [manuscript] §2-quantum-observable-universes
- [kassel1995] Quantum Groups (Springer GTM 155), §IV.4
-/

namespace QOU

noncomputable section

/-- **q-Resolvent data.** Packages the q-Laplacian `delta_q`, the
    spectral parameter `s`, and an inverse witness for `s + delta_q`
    in the convolution algebra `𝓗_q`. -/
-- Ref: [kassel1995] Quantum Groups, §IV.4
structure QResolvent (H : Type*) where
  /-- The q-Laplacian endomorphism. -/
  delta_q : H → H
  /-- The spectral parameter. -/
  s : H
  /-- The resolvent `R_q(s)`. -/
  R : H → H
  /-- Inverse witness: `R ∘ delta_q = id`. -/
  inverse_witness : ∀ x : H, R (delta_q x) = x

/-- **q-Heat equation data**: a one-parameter family with q-Laplacian,
    satisfying `∂ₜ u = -Δ_q u` pointwise (algebraic shadow of the PDE). -/
-- Ref: [manuscript] §2
structure QHeatEquation (S : Type*) where
  /-- Time-dependent section `u : ℝ → S → Archimedean.R_q`. -/
  u : ℝ → S → Archimedean.R_q
  /-- Time-derivative `∂ₜ u`. -/
  dt_u : ℝ → S → Archimedean.R_q
  /-- q-Laplacian applied to `u`. -/
  dq_u : ℝ → S → Archimedean.R_q
  /-- The evolution equation `∂ₜ u(t,x) = -Δ_q u(t,x)`. -/
  evolves : ∀ (t : ℝ) (x : S), dt_u t x = -dq_u t x

/-- **q-Dilogarithm data**: a level-2 iterated primitive of `H_q`
    characterised by the pentagon identity.  The pentagon relation is
    additive, so the carrier `H` is required to support `+`. -/
-- Ref: [manuscript] §2
structure QDilogarithm (H : Type*) [Add H] where
  /-- The level-2 primitive `Li₂_q ∈ H × H`. -/
  Li2 : H × H
  /-- The level-1 primitive `log_q ∈ H`. -/
  log_q : H
  /-- Evaluation map. -/
  Li2_eval : H → H
  /-- Binary composition for pentagon arguments. -/
  mul : H → H → H
  /-- Complement `x ↦ 1 - x`. -/
  compl : H → H
  /-- Division `(x,y) ↦ x/y`. -/
  div : H → H → H
  /-- **Pentagon identity** (5-term relation). -/
  pentagon : ∀ (x y : H),
    Li2_eval y + Li2_eval x =
      Li2_eval (mul x y) +
      Li2_eval (div (mul x (compl y)) (compl (mul x y))) +
      Li2_eval (div (mul y (compl x)) (compl (mul x y)))

end

end QOU
