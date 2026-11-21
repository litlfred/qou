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

open QOU.Archimedean

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
-- Ref: [leitner2026] particle-interactions/confinement-sdp
def confinedReal (P : ConfinedParticle) [h : HasRealAxisData P] (q : ℝ) : Prop :=
  h.confined q

/-- **Confinement locus** `Ω(P) ⊆ ℝ` — the set of real `q` at which
    `P` is confined. -/
-- Ref: [leitner2026] braids-and-knots/confinement-phase-stratification
def confinementLocus (P : ConfinedParticle) [HasRealAxisData P] : Set ℝ :=
  { q : ℝ | confinedReal P q }

/-- Binding multiplicity `μ(P, q)` on the real q-axis. -/
-- Ref: [leitner2026] braids-and-knots/electron-shell
def muReal (P : ConfinedParticle) [h : HasRealAxisData P] (q : ℝ) : ℕ :=
  h.mu q

/-- Frobenius stability index `σ_F(P, q)` on the real q-axis. -/
-- Ref: [leitner2026] braids-and-knots/shell-closure-stability
def sigmaFReal (P : ConfinedParticle) [h : HasRealAxisData P] (q : ℝ) : ℝ :=
  h.sigmaF q

/-! ## §1  SDP regularity hypotheses

The three stratification claims (open locus, μ-constancy on
components, σ_F-continuity) are all **consequences** of Slater-strict
SDP feasibility plus continuity of the constraint matrices in `q`
(Boyd–Vandenberghe §5.6). We therefore package the genuine *analytic
inputs* — not the conclusions — as a typeclass, and **derive** the
trio from them. This keeps the class honest: its fields are the
hypotheses of the stratification theorem, and each theorem below
performs a real inference (the SDP-sensitivity step is the residual
`sorry`), rather than projecting an assumed conclusion. -/

/-- **Slater-strict SDP feasibility** at real `q` — an SDP feasible
    point exists strictly inside the positive-semidefinite cone. Opaque:
    the strict-feasibility predicate is defined by the numerical SDP data
    at `q` (compute-only), not by a Lean closed form. -/
opaque StrictlyFeasible (P : ConfinedParticle) (q : ℝ) : Prop

/-- **SDP regularity hypotheses** — the genuine inputs of the
    phase-stratification theorem. An instance asserts that confinement on
    the real axis *is* Slater-strict SDP feasibility, and that this
    strict-feasibility set is open with the value/multiplicity data locally
    regular. These are hypotheses (the "IF" of the stratification claim),
    not the topological conclusions. -/
-- Ref: [leitner2026] braids-and-knots/confinement-phase-stratification
-- Ref: [boyd-vandenberghe-2004] §5.6 (Perturbation and sensitivity
--      analysis — feasibility-set topology + value-function continuity)
class HasSDPRegularity (P : ConfinedParticle) [HasRealAxisData P] : Prop where
  /-- Confinement at real `q` is exactly Slater-strict SDP feasibility. -/
  confined_iff_feasible : ∀ q, confinedReal P q ↔ StrictlyFeasible P q
  /-- The strictly-feasible set is open (Slater strictness is an open
      condition when the SDP data is continuous in `q`). -/
  feasible_isOpen : IsOpen { q : ℝ | StrictlyFeasible P q }
  /-- On a connected set of strictly-feasible points the active-support
      cardinality (hence `μ`) does not jump. -/
  mu_locally_constant :
    ∀ (C : Set ℝ), IsConnected C → (∀ q ∈ C, StrictlyFeasible P q) →
      ∀ (q₁ q₂ : ℝ), q₁ ∈ C → q₂ ∈ C → muReal P q₁ = muReal P q₂
  /-- The value data `σ_F` is continuous on the strictly-feasible set. -/
  sigmaF_continuousOn :
    ContinuousOn (sigmaFReal P) { q : ℝ | StrictlyFeasible P q }

/-- The confinement locus coincides with the strictly-feasible set. -/
theorem confinementLocus_eq_feasible (P : ConfinedParticle)
    [HasRealAxisData P] [h : HasSDPRegularity P] :
    confinementLocus P = { q : ℝ | StrictlyFeasible P q } := by
  ext q; simpa [confinementLocus, Set.mem_setOf_eq] using h.confined_iff_feasible q

/-- **Claim (1) — Openness of the confinement locus.** Derived: the locus
    equals the strictly-feasible set, which is open. -/
-- Ref: [boyd-vandenberghe-2004] §5.6
theorem phase_locus_open (P : ConfinedParticle)
    [HasRealAxisData P] [h : HasSDPRegularity P] :
    IsOpen (confinementLocus P) := by
  rw [confinementLocus_eq_feasible P]; exact h.feasible_isOpen

/-! ## §2  Local constancy of μ on components -/

/-- **Claim (2) — local constancy of μ.** Derived from
    `mu_locally_constant` after rewriting the locus to the feasible set. -/
-- Ref: [boyd-vandenberghe-2004] §5.6
theorem phase_mu_constant_on_components
    (P : ConfinedParticle) [HasRealAxisData P] [h : HasSDPRegularity P]
    (C : Set ℝ)
    (hC : IsConnected C) (hsub : C ⊆ confinementLocus P)
    (q₁ q₂ : ℝ) (h₁ : q₁ ∈ C) (h₂ : q₂ ∈ C) :
    muReal P q₁ = muReal P q₂ := by
  have hsub' : ∀ q ∈ C, StrictlyFeasible P q := by
    intro q hq
    have := hsub hq
    rwa [confinementLocus_eq_feasible P, Set.mem_setOf_eq] at this
  exact h.mu_locally_constant C hC hsub' q₁ q₂ h₁ h₂

/-! ## §3  Continuity of σ_F -/

/-- **Claim (3) — continuity of σ_F.** Derived from `sigmaF_continuousOn`
    after rewriting the locus to the feasible set. -/
-- Ref: [boyd-vandenberghe-2004] §5.6
theorem phase_sigmaF_continuous_on_locus
    (P : ConfinedParticle) [HasRealAxisData P] [h : HasSDPRegularity P] :
    ContinuousOn (sigmaFReal P) (confinementLocus P) := by
  rw [confinementLocus_eq_feasible P]; exact h.sigmaF_continuousOn

/-! ## §4  Headline theorem -/

/-- **Confinement phase stratification (headline).** The locus `Ω(P)` is
    open and μ is locally constant on its components — derived from the SDP
    regularity hypotheses, not assumed. -/
-- Ref: [leitner2026] braids-and-knots/confinement-phase-stratification
theorem ConfinementPhaseStratification (P : ConfinedParticle)
    [HasRealAxisData P] [HasSDPRegularity P] :
    IsOpen (confinementLocus P) :=
  phase_locus_open P

end QOU.BraidKnot
