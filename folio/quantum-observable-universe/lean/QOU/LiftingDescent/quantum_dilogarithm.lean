import Mathlib.Data.Real.Basic

/-!
# QOU.Torsion.quantum_dilogarithm — `tr_trans(ϱ, p_i) = Φ_q(z_i)`

**Definition / Proposition** ([`def:quantum-dilogarithm`](../../../quantum-observable-universe/mass-endomorphism/quantum-dilogarithm.md)).

*In the archimedean realisation, the transient trace contribution
`tr_trans(ϱ, p_i)` from the topological decomposition of mass
evaluates to the quantum dilogarithm `Φ_q(z_i)`, where `z_i` is the
spectral coordinate of `p_i` in the Briggs–Klein chart.*

The Lean encoding records the equation as a class field of an
abstract `QuantumDilogarithmContext`.

## Base ring (AGENTS.md §7c) — `ℝ` here is required, not a gratuitous specialisation

The statement above is explicitly the **archimedean realisation** ("*In the
archimedean realisation, …*"), and the object it names forces that: `Φ_q` is the
**Faddeev quantum dilogarithm**, a transcendental analytic function (an infinite
product / integral representation), not a rational or polynomial construct. It
has no meaning over a generic `{R : Type*} [CommRing R]`, and neither does the
`spectralCoord` chart coordinate it is evaluated at. This block therefore sits on
the observation side of the substrate→archimedean wall by construction.

Consistent with `docs/audits/2026-06-25-lean-library-tree-7c-coverage-gap.md`,
which already records the dilogarithm files as **legitimately archimedean** —
they are named there among the files a directory-based heuristic wrongly flagged.

Recorded here so §7c sweeps stop re-flagging the module: a bare grep sees a
`Torsion` module whose every field is `ℝ`-typed and scores a base-ring
candidate, which it is not.

-- Ref: [leitner2026] quantum-observable-universe/mass-endomorphism/quantum-dilogarithm.md
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
-- Ref: [leitner2026] quantum-observable-universe/mass-endomorphism/quantum-dilogarithm.md
theorem quantum_dilogarithm
    [ctx : QuantumDilogarithmContext] (ϱ p : ℝ) :
    ctx.trTransient ϱ p = ctx.Phi_q (ctx.spectralCoord p) :=
  ctx.claim_tr_trans_eq_Phi_q ϱ p

end QOU.Torsion
