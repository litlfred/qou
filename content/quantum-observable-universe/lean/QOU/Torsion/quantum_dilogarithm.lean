/-!
# QOU.Torsion.quantum_dilogarithm — `tr_trans(ϱ, p_i) = Φ_q(z_i)`

**Definition / Proposition** ([`def:quantum-dilogarithm`](../../../quantum-observable-universe/lifting-and-descent/quantum-dilogarithm.md)).

*In the archimedean realisation, the transient trace contribution
`tr_trans(ϱ, p_i)` from the topological decomposition of mass
evaluates to the quantum dilogarithm `Φ_q(z_i)`, where `z_i` is the
spectral coordinate of `p_i` in the Briggs–Klein chart.*

The Lean encoding records the equation as a class field of an
abstract `QuantumDilogarithmContext`.

-- Ref: [manuscript] quantum-observable-universe/lifting-and-descent/quantum-dilogarithm.md
-/

namespace QOU.Torsion

/-- Abstract context for the quantum-dilogarithm transient-trace identity. -/
class QuantumDilogarithmContext where
  /-- The substrate parameter `q`. -/
  q : ℝ
  /-- The transient-trace function `tr_trans(ϱ, p)`. -/
  trTransient : ℝ → ℝ → ℝ      -- (ϱ-spectral, p-spectral) → ℝ
  /-- The quantum-dilogarithm function `Φ_q(z)`. -/
  Phi_q : ℝ → ℝ
  /-- The Briggs–Klein spectral coordinate of `p`. -/
  spectralCoord : ℝ → ℝ        -- p → z_i
  /-- Manuscript identification — the transient piece of the
      mass-decomposition lift coincides with `Φ_q(z)` at the
      Briggs–Klein spectral coordinate of `p`. -/
  claim_tr_trans_eq_Phi_q : ∀ ϱ p : ℝ,
    trTransient ϱ p = Phi_q (spectralCoord p)

/-- **Quantum-dilogarithm identification** ([`def:quantum-dilogarithm`]).

    The transient-trace contribution coincides with the quantum
    dilogarithm at the Briggs–Klein spectral coordinate. -/
-- Ref: [manuscript] quantum-observable-universe/lifting-and-descent/quantum-dilogarithm.md
theorem quantum_dilogarithm
    [ctx : QuantumDilogarithmContext] (ϱ p : ℝ) :
    ctx.trTransient ϱ p = ctx.Phi_q (ctx.spectralCoord p) :=
  ctx.claim_tr_trans_eq_Phi_q ϱ p

end QOU.Torsion
