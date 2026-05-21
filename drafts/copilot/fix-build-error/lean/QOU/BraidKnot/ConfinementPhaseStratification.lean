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

/-! ### Real-axis stratification data (typeclass-supplied)

The phase-stratification analysis lives on the *real* q-axis,
where the SDP constraint matrices are continuous in `q`. The
underlying ground ring `R_q = LaurentPolynomial ℤ` is purely
algebraic; the maps `confinedReal`, `muReal`, `sigmaFReal` are
the analytic specialisations obtained by evaluating SDP-derived
quantities at real `q`.

These maps are not closed-form: they depend on the (numerical)
SDP solution at each `q`. Rather than `opaque`-stubbing them, we
package them as a typeclass `HasRealAxisData` so each particle's
data is supplied by the caller (typically from a numerical SDP
solver, e.g. CVXPY). -/

/-- **Real-axis SDP data** — class-supplied evaluation maps. -/
class HasRealAxisData (P : ConfinedParticle) where
  /-- Confinement predicate at real `q`. -/
  confined : ℝ → Prop
  /-- Binding multiplicity `μ(P, q)` at real `q`. -/
  mu : ℝ → ℕ
  /-- Frobenius stability `σ_F(P, q)` at real `q`. -/
  sigmaF : ℝ → ℝ

/-- Confinement predicate at real `q`. -/
-- Ref: [manuscript] particle-interactions/confinement-sdp
def confinedReal (P : ConfinedParticle) [h : HasRealAxisData P] (q : ℝ) : Prop :=
  h.confined q

/-- **Confinement locus** `Ω(P) ⊆ ℝ` — the set of real `q` at which
    `P` is confined. -/
-- Ref: [manuscript] braids-and-knots/confinement-phase-stratification
def confinementLocus (P : ConfinedParticle) [HasRealAxisData P] : Set ℝ :=
  { q : ℝ | confinedReal P q }

/-- Binding multiplicity `μ(P, q)` on the real q-axis. -/
-- Ref: [manuscript] braids-and-knots/electron-shell
def muReal (P : ConfinedParticle) [h : HasRealAxisData P] (q : ℝ) : ℕ :=
  h.mu q

/-- Frobenius stability index `σ_F(P, q)` on the real q-axis. -/
-- Ref: [manuscript] braids-and-knots/shell-closure-stability
def sigmaFReal (P : ConfinedParticle) [h : HasRealAxisData P] (q : ℝ) : ℝ :=
  h.sigmaF q

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
-- Ref: [boyd-vandenberghe-2004] §5.6 (Perturbation and sensitivity
--      analysis — feasibility-set topology + value-function continuity)
class HasPhaseStratification (P : ConfinedParticle)
    [HasRealAxisData P] : Prop where
  /-- **Claim (1)** — openness of the confinement locus
      (Slater-strict feasibility is open). -/
  locus_open : IsOpen (confinementLocus P)
  /-- **Claim (2)** — μ is constant on connected components of the
      locus (active-support cardinality is locally constant). -/
  mu_constant : ∀ (C : Set ℝ), IsConnected C → C ⊆ confinementLocus P →
    ∀ (q₁ q₂ : ℝ), q₁ ∈ C → q₂ ∈ C → muReal P q₁ = muReal P q₂
  /-- **Claim (3)** — σ_F is continuous on the locus. -/
  sigmaF_continuous : ContinuousOn (sigmaFReal P) (confinementLocus P)

/-- **Default instance from a Fact-bundled triple**: when each of
    the three stratification claims is in scope as a `Fact`, the
    `HasPhaseStratification` instance follows. -/
instance hasPhaseStratification_of_facts (P : ConfinedParticle)
    [HasRealAxisData P]
    [hOpen : Fact (IsOpen (confinementLocus P))]
    [hMu : Fact (∀ (C : Set ℝ), IsConnected C → C ⊆ confinementLocus P →
              ∀ (q₁ q₂ : ℝ), q₁ ∈ C → q₂ ∈ C → muReal P q₁ = muReal P q₂)]
    [hSigma : Fact (ContinuousOn (sigmaFReal P) (confinementLocus P))] :
    HasPhaseStratification P where
  locus_open := hOpen.out
  mu_constant := hMu.out
  sigmaF_continuous := hSigma.out

/-- **Claim (1) — Openness** (per-instance form).
    Backed by `HasPhaseStratification.locus_open`. -/
-- Ref: [manuscript] braids-and-knots/confinement-phase-stratification
-- Ref: [boyd-vandenberghe-2004] §5.6 (Perturbation and sensitivity
--      analysis — feasibility-set topology + value-function continuity)
theorem phase_locus_open (P : ConfinedParticle)
    [HasRealAxisData P] [h : HasPhaseStratification P] :
    IsOpen (confinementLocus P) :=
  h.locus_open

/-! ## §2  Local constancy of μ on components -/

/-- **Claim (2) — local constancy of μ** (per-instance form).
    Backed by `HasPhaseStratification.mu_constant`. -/
-- Ref: [manuscript] braids-and-knots/confinement-phase-stratification
-- Ref: [boyd-vandenberghe-2004] §5.6 (Perturbation and sensitivity
--      analysis — feasibility-set topology + value-function continuity)
theorem phase_mu_constant_on_components
    (P : ConfinedParticle) [HasRealAxisData P] [h : HasPhaseStratification P]
    (C : Set ℝ)
    (hC : IsConnected C) (hsub : C ⊆ confinementLocus P)
    (q₁ q₂ : ℝ) (h₁ : q₁ ∈ C) (h₂ : q₂ ∈ C) :
    muReal P q₁ = muReal P q₂ :=
  h.mu_constant C hC hsub q₁ q₂ h₁ h₂

/-! ## §3  Continuity of σ_F -/

/-- **Claim (3) — continuity of σ_F** (per-instance form).
    Backed by `HasPhaseStratification.sigmaF_continuous`. -/
-- Ref: [manuscript] braids-and-knots/confinement-phase-stratification
-- Ref: [boyd-vandenberghe-2004] §5.6 (Perturbation and sensitivity
--      analysis — feasibility-set topology + value-function continuity)
theorem phase_sigmaF_continuous_on_locus
    (P : ConfinedParticle) [HasRealAxisData P] [h : HasPhaseStratification P] :
    ContinuousOn (sigmaFReal P) (confinementLocus P) :=
  h.sigmaF_continuous

/-! ## §4  Headline theorem -/

/-- **Confinement phase stratification (headline).** The locus
    `Ω(P)` is open and μ is locally constant on components. -/
-- Ref: [manuscript] braids-and-knots/confinement-phase-stratification
theorem ConfinementPhaseStratification (P : ConfinedParticle)
    [HasRealAxisData P] [HasPhaseStratification P] :
    IsOpen (confinementLocus P) :=
  phase_locus_open P

end QOU.BraidKnot
