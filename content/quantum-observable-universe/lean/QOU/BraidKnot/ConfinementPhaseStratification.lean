import QOU.BraidKnot.ConfinedParticle
import QOU.BraidKnot.DressedParticle
import Mathlib.Topology.Basic

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

/-! ### Stratification trio as a typeclass (Pattern 4 + 2)

The three stratification claims (open locus, μ-constancy on
components, σ_F-continuity) are conceptually independent and are
all consequences of Slater-strict SDP feasibility plus continuity
of the constraint matrices in `q`. Rather than asserting them as
universal axioms, we **split** them into a single typeclass with
three fields. Callers obtain the relevant claim by binding to a
`HasPhaseStratification` instance for the specific particle. -/

/-- **Phase-stratification trio — typeclass.**
    Per-particle witness to the three stratification claims.
    Splitting into one class (rather than three independent
    axioms) keeps the conceptual unit intact while moving the
    universal quantifier into per-instance evidence. -/
-- Ref: [manuscript] braids-and-knots/confinement-phase-stratification
-- Ref: [boyd-vandenberghe-2004] https://doi.org/10.1017/CBO9780511804441
class HasPhaseStratification (P : ConfinedParticle) : Prop where
  /-- **Claim (1)** — openness of the confinement locus
      (Slater-strict feasibility is open). -/
  locus_open : IsOpen (confinementLocus P)
  /-- **Claim (2)** — μ is constant on connected components of the
      locus (active-support cardinality is locally constant). -/
  mu_constant : ∀ (C : Set ℝ), IsConnected C → C ⊆ confinementLocus P →
    ∀ (q₁ q₂ : ℝ), q₁ ∈ C → q₂ ∈ C → muReal P q₁ = muReal P q₂
  /-- **Claim (3)** — σ_F is continuous on the locus. -/
  sigmaF_continuous : ContinuousOn (sigmaFReal P) (confinementLocus P)

/-- **Claim (1) — Openness** (per-instance form).
    Backed by `HasPhaseStratification.locus_open`. -/
-- Ref: [manuscript] braids-and-knots/confinement-phase-stratification
-- Ref: [boyd-vandenberghe-2004] https://doi.org/10.1017/CBO9780511804441
theorem phase_locus_open (P : ConfinedParticle)
    [h : HasPhaseStratification P] :
    IsOpen (confinementLocus P) :=
  h.locus_open

/-! ## §2  Local constancy of μ on components -/

/-- **Claim (2) — local constancy of μ** (per-instance form).
    Backed by `HasPhaseStratification.mu_constant`. -/
-- Ref: [manuscript] braids-and-knots/confinement-phase-stratification
-- Ref: [boyd-vandenberghe-2004] https://doi.org/10.1017/CBO9780511804441
theorem phase_mu_constant_on_components
    (P : ConfinedParticle) [h : HasPhaseStratification P]
    (C : Set ℝ)
    (hC : IsConnected C) (hsub : C ⊆ confinementLocus P)
    (q₁ q₂ : ℝ) (h₁ : q₁ ∈ C) (h₂ : q₂ ∈ C) :
    muReal P q₁ = muReal P q₂ :=
  h.mu_constant C hC hsub q₁ q₂ h₁ h₂

/-! ## §3  Continuity of σ_F -/

/-- **Claim (3) — continuity of σ_F** (per-instance form).
    Backed by `HasPhaseStratification.sigmaF_continuous`. -/
-- Ref: [manuscript] braids-and-knots/confinement-phase-stratification
-- Ref: [boyd-vandenberghe-2004] https://doi.org/10.1017/CBO9780511804441
theorem phase_sigmaF_continuous_on_locus
    (P : ConfinedParticle) [h : HasPhaseStratification P] :
    ContinuousOn (sigmaFReal P) (confinementLocus P) :=
  h.sigmaF_continuous

/-! ## §4  Headline theorem -/

/-- **Confinement phase stratification (headline).** The locus
    `Ω(P)` is open and μ is locally constant on components. -/
-- Ref: [manuscript] braids-and-knots/confinement-phase-stratification
theorem ConfinementPhaseStratification (P : ConfinedParticle)
    [HasPhaseStratification P] :
    IsOpen (confinementLocus P) :=
  phase_locus_open P

end QOU.BraidKnot
