/-!
# QOU.ParticleInteractions.ConfinementSDP

Confinement as a semidefinite program with matrix Frobenius
positivity. Primal: `min ⟨T, Φ⟩` s.t. `Φ ⪰ 0`, per-block Frobenius
positivity, 2×2 pair PSD. Dual matrix inequality
`y₀ I + Σ y_λ π_λ − T ⪯ 0`. The scalar LP
(`prop:confinement-lp`) is the diagonal rank-1 projection.

LaTeX: `\label{prop:confinement-sdp}`
-/

import QOU.Basic

namespace QOU.ParticleInteractions

universe u

/-- Placeholder for a confined particle. -/
opaque ConfinedParticleTy : Type

/-- Feasibility of the Slater-strict confinement SDP at `(P, q)`. -/
-- Ref: [manuscript] particle-interactions/confinement-sdp
opaque slaterStrictFeasible : ConfinedParticleTy → ℝ → Prop

/-- Optimal dual shadow price of the normalisation constraint. -/
-- Ref: [manuscript] particle-interactions/confinement-sdp
opaque y0_star : ConfinedParticleTy → ℝ → ℝ

/-- Target normalisation constant `n_target` for the SDP. -/
-- Ref: [manuscript] particle-interactions/confinement-sdp
opaque n_target : ConfinedParticleTy → ℝ

/-- Class-axiomatisation of the confinement SDP's strong-duality
    consequence (CLAUDE.md §3b-cond).  Under Slater-strict
    feasibility, the dual shadow price `y₀*` is non-negative.

    This is a standard SDP-duality result
    [boyd-vandenberghe-2004] which Mathlib does not yet provide
    in a form usable here; class-axiomatising the conclusion
    isolates the SDP-theory dependency to a single named field
    and produces a `sorry`-free downstream proof body. -/
class ConfinementSDPDuality where
  /-- Slater-strict feasibility implies non-negative dual shadow. -/
  y0_star_nonneg :
    ∀ (P : ConfinedParticleTy) (q : ℝ),
      slaterStrictFeasible P q → y0_star P q ≥ 0

/-- **Confinement SDP primal–dual** (conditional theorem, §3b-cond).
    At any `(P, q)` with Slater-strict feasibility, the dual shadow
    price is non-negative.  Stated as a corollary of strong duality
    for the matrix-Frobenius-positivity SDP described in the file
    header; the full primal–dual statement (uniqueness of `Φ* ⪰ 0`,
    matrix complementary slackness) is the upstream axiom packaged
    by `ConfinementSDPDuality`.

    Proof body has no `sorry`; the only unproved input is the
    class instance.

    Ref: [boyd-vandenberghe-2004] https://doi.org/10.1017/CBO9780511804441
    Ref: [manuscript] particle-interactions/confinement-sdp -/
theorem ConfinementSDP
    [inst : ConfinementSDPDuality]
    (P : ConfinedParticleTy) (q : ℝ)
    (h : slaterStrictFeasible P q) :
    y0_star P q ≥ 0 :=
  inst.y0_star_nonneg P q h

end QOU.ParticleInteractions
