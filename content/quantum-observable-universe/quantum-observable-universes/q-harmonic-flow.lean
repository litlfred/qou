import Mathlib.Algebra.Group.Basic
import Mathlib.Tactic

/-!
# QOU.LocalQ.QHarmonicFlow

q-harmonic-map heat flow for the substrate field `δq(p)` (Route 2b of the
local-q programme,
[`docs/scope/2026-06-16-local-q-evolution-routes.md`] Step 3).

Route 2a (`prop:germ-commutator-q-curvature`) gives the *kinematic* half:
the germ `δq(p)` is the `q`-curvature on the loop. Route 2b supplies the
*dynamical* half — a candidate **time-evolution law** for the substrate
field promoting `q(p)` itself to a diffusing field:

  `∂_t q = -Δ_q q`,   `Δ_q = q⁻²Δ + q⁻¹(1-q⁻¹)𝔠 + (1-q⁻¹)²Δ_ξ`.

**ANSATZ (conjecture).** The specific PDE is a *new postulate*, not a
theorem in the corpus: `prop:q-gaussian-solves-q-heat` governs diffusion
of a scalar density *at fixed `q`*; making `q` itself the diffusing field
is the conjectural content. Here it is axiomatised as a Lean `class` whose
*instance* is the conjecture; the structural consequence below
(stationary configurations are exactly the `q`-harmonic ones) is then
**verified, sorry-free, conditional on the class** — the §3b conditional-
class pattern.

The flow is stated abstractly: `q` is a configuration in an additive
group `V`, `dq` is its time-derivative `∂_t q`, and `Δq` is the
`q`-Laplacian. No archimedean structure is required (the structural
content is `dq = -Δq q`), so this lives ring/group-generic per §7c.

Ref: [manuscript] docs/scope/2026-06-16-local-q-evolution-routes.md Step 3,
prop:germ-commutator-q-curvature, prop:q-gaussian-solves-q-heat
-/

namespace QOU.LocalQ

/-- **q-harmonic-map heat flow (ANSATZ).** A substrate-field configuration
    `q ∈ V`, its time-derivative `dq = ∂_t q`, and the `q`-Laplacian
    `Δq`, postulated to satisfy the gradient/heat-flow law
    `∂_t q = -Δ_q q`.

    The *existence* of such a structure for the physical substrate field
    is the conjecture (Route 2b Step 3 ansatz); every theorem in this
    namespace is a verified consequence *conditional on* the class. -/
class QHarmonicFlow (V : Type*) [AddCommGroup V] where
  /-- The substrate-field configuration `q(p)` (a single time-slice). -/
  q : V
  /-- The time-derivative `∂_t q` of the configuration. -/
  dq : V
  /-- The `q`-Laplacian `Δ_q` acting on field configurations. -/
  Δq : V → V
  /-- The `q`-Laplacian annihilates the zero configuration (it is a
      second-order linear differential operator with no zeroth-order
      term). -/
  Δq_zero : Δq 0 = 0
  /-- **The ansatz**: the q-harmonic-map heat-flow law `∂_t q = -Δ_q q`. -/
  flow : dq = - Δq q

namespace QHarmonicFlow

variable {V : Type*} [AddCommGroup V] [QHarmonicFlow V]

/-- **Fixed points are exactly the q-harmonic configurations.** The flow is
    stationary (`∂_t q = 0`) iff the configuration is `q`-harmonic
    (`Δ_q q = 0`). Verified, conditional on the `QHarmonicFlow` class. -/
theorem stationary_iff_qharmonic :
    (dq : V) = 0 ↔ (Δq (V := V) (q (V := V))) = 0 := by
  rw [flow (V := V), neg_eq_zero]

/-- **The vacuum is a fixed point.** When the configuration is the trivial
    (zero) field, the flow is stationary — the vacuum constant `q ≡ q₀`
    is the trivial `q`-harmonic section. -/
theorem vacuum_stationary (hq : (q : V) = 0) : (dq : V) = 0 := by
  rw [flow (V := V), hq, Δq_zero (V := V), neg_zero]

end QHarmonicFlow

end QOU.LocalQ
