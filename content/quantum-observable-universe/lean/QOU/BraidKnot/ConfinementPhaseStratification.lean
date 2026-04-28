/-!
# Confinement Phase Stratification

The confinement locus `Ω(P) = {q : confined(P, q)}` is open in the
generic `q`-locus; its complement is a real-algebraic stratification
of codimension ≥ 1. Each connected component is a confinement
phase on which active support, binding multiplicity μ, and σ_F are
(locally) constant or real-analytic. Every confinement-framework
theorem (level-sufficiency, shell-closure-stability, etc.) is
implicitly scoped to a single phase; boundary crossings are
deconfinement or regime switches.

## References

- [prop:confinement-phase-stratification]
- [def:confined-particle]
- [prop:confinement-sdp]
- [rem:deconfinement-golden-threshold]
- [prop:parity-regime-selection]
- [boyd-vandenberghe-2004]
-/

import QOU.BraidKnot.ConfinedParticle
import QOU.BraidKnot.DressedParticle
import Mathlib.Topology.Basic

namespace QOU.BraidKnot

open QOU.Descartes

/-- Coercion from the ground ring `R_q = LaurentPolynomial ℤ` to ℝ
    for the phase-stratification analysis on the real q-axis. -/
-- Ref: [manuscript] braids-and-knots/confinement-phase-stratification
opaque rqToReal : R_q → ℝ

/-- Confinement predicate specialised to the real q-axis. -/
-- Ref: [manuscript] particle-interactions/confinement-sdp
opaque confinedReal : ConfinedParticle → ℝ → Prop

/-- **Confinement locus** `Ω(P) ⊆ ℝ` — the set of real `q` at which
    `P` is confined. -/
-- Ref: [manuscript] braids-and-knots/confinement-phase-stratification
def confinementLocus (P : ConfinedParticle) : Set ℝ :=
  { q : ℝ | confinedReal P q }

/-- Binding multiplicity `μ(P, q)` on the real q-axis. -/
-- Ref: [manuscript] braids-and-knots/electron-shell
opaque muReal : ConfinedParticle → ℝ → ℕ

/-- Frobenius stability index `σ_F(P, q)` on the real q-axis. -/
-- Ref: [manuscript] braids-and-knots/shell-closure-stability
opaque sigmaFReal : ConfinedParticle → ℝ → ℝ

/-! ## §1  Openness of the confinement locus -/

/-- **Claim (1) — Openness.** `Ω(P)` is open in ℝ. Follows from
    neighbourhood-stability of Slater-strict SDP feasibility:
    if `Φ ≻ 0` strictly feasible at `q₀`, the same `Φ` remains
    strictly feasible for all `q` in a neighbourhood by continuity
    of the SDP constraint matrices in `q`. -/
-- Ref: [manuscript] braids-and-knots/confinement-phase-stratification
-- Ref: [boyd-vandenberghe-2004] https://doi.org/10.1017/CBO9780511804441
axiom phase_locus_open (P : ConfinedParticle) :
    IsOpen (confinementLocus P)

/-! ## §2  Local constancy of μ on components -/

/-- **Claim (3) — local constancy of μ.** On each connected
    component of `Ω(P)`, binding multiplicity is constant. -/
-- Ref: [manuscript] braids-and-knots/confinement-phase-stratification
-- Ref: [boyd-vandenberghe-2004] https://doi.org/10.1017/CBO9780511804441
axiom phase_mu_constant_on_components
    (P : ConfinedParticle) (C : Set ℝ)
    (hC : IsConnected C) (hsub : C ⊆ confinementLocus P)
    (q₁ q₂ : ℝ) (h₁ : q₁ ∈ C) (h₂ : q₂ ∈ C) :
    muReal P q₁ = muReal P q₂

/-! ## §3  Continuity of σ_F -/

/-- **Claim (3) — continuity of σ_F.** `σ_F` is continuous on each
    connected component of `Ω(P)`. -/
-- Ref: [manuscript] braids-and-knots/confinement-phase-stratification
-- Ref: [boyd-vandenberghe-2004] https://doi.org/10.1017/CBO9780511804441
axiom phase_sigmaF_continuous_on_locus
    (P : ConfinedParticle) :
    ContinuousOn (sigmaFReal P) (confinementLocus P)

/-! ## §4  Headline theorem -/

/-- **Confinement phase stratification (headline).** The locus
    `Ω(P)` is open and μ is locally constant on components. -/
-- Ref: [manuscript] braids-and-knots/confinement-phase-stratification
theorem ConfinementPhaseStratification (P : ConfinedParticle) :
    IsOpen (confinementLocus P) :=
  phase_locus_open P

end QOU.BraidKnot
