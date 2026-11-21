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

- [leitner2026] §2-quantum-observable-universes
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
-- Ref: [leitner2026] §2
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
-- Ref: [leitner2026] §2
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


/-- **q-Exponential data**: an abstract grouplike of the q-shuffle Hopf
    algebra, characterised by the flow equation `D_q g = g`.

    Relocated here 2026-09-06, completing the relocation this module was
    created for: the 2026-06-09 audit moved `QDilogarithm` so that the
    companion `*-unique.lean` display files could import a real structure,
    but left `QExponential` and `QLogarithm` inlined in four siblings
    apiece.  Their uniqueness axioms were refuted from those inline
    copies; see `QAnalysisUniquenessCounterexamples`. -/
-- Ref: [kassel1995] Quantum Groups (Springer GTM 155), §III.3
structure QExponential (H : Type*) where
  /-- The grouplike element `e_q ∈ H`. -/
  e_q : H
  /-- Coproduct on `H`, encoded as `coprod : H → H × H`. -/
  coprod : H → H × H
  /-- Counit on `H`. -/
  counit : H → Archimedean.R_q
  /-- q-Jackson derivative on `H`. -/
  D_q : H → H
  /-- Grouplike axiom: `Δ_q(e_q) = (e_q, e_q)`. -/
  grouplike : coprod e_q = (e_q, e_q)
  /-- Counit: `ε(e_q) = 1`. -/
  counit_eq_one : counit e_q = 1
  /-- Flow equation: `D_q e_q = e_q`. -/
  flow_invariant : D_q e_q = e_q

/-- **q-Logarithm data**: an abstract primitive element of the q-shuffle
    Hopf algebra, characterised by primitivity
    `Δ_q(log_q) = log_q ⊗ 1 + 1 ⊗ log_q` and vanishing counit
    `ε(log_q) = 0`.

    Relocated here 2026-09-06 alongside `QExponential`. -/
-- Ref: [kassel1995] Quantum Groups (Springer GTM 155), §IV.3
structure QLogarithm (H : Type*) where
  /-- The primitive element `log_q ∈ H`. -/
  log_q : H
  /-- Coproduct on `H`, encoded as `coprod : H → H × H`. -/
  coprod : H → H × H
  /-- Counit on `H`. -/
  counit : H → Archimedean.R_q
  /-- The unit / grouplike `1 ∈ H` against which primitivity is taken. -/
  one : H
  /-- Primitivity (left component). -/
  primitive_left : (coprod log_q).1 = log_q
  /-- Primitivity (right component). -/
  primitive_right : (coprod log_q).2 = log_q
  /-- Vanishing counit: `ε(log_q) = 0`. -/
  counit_eq_zero : counit log_q = 0

end

end QOU
