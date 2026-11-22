import Mathlib.Algebra.Ring.Basic
import Mathlib.Tactic

/-!
# QOU.LocalQ.ObservationParallelogram

Germ-commutator = q-curvature (Route 2a of the local-q programme,
[`docs/scope/2026-06-16-local-q-evolution-routes.md`]).

At a point `p`, two independent observations perturb the substrate
parameter by germ-level increments `δq₁, δq₂` living in the germ
algebra `A/𝔪_p²` (generally **non-commutative** via the Hopf
structure — see `rem:two-observer-parallelogram`). Their commutator is
the local seed of `δq` and is identified with the `q`-curvature 2-form
on the loop spanned by the two observation directions
(`def:q-flat-connection`):

  `[δq₁, δq₂] = F_q`.

This file formalises that identity over an abstract non-commutative
ring `R` of germ-level perturbations, together with two structural
consequences: the observers agree iff the `q`-curvature vanishes (the
boson / `q`-flat case), and the curvature is antisymmetric in the two
observers (it is a 2-form on the loop).

## Encoding (restructured 2026-07-04 — from a projection stub)

The previous encoding carried `Fq` as a structure *field* together with
a field `parallelogram : obsCommutator δq₁ δq₂ = Fq` whose type IS the
theorem's conclusion; `commutator_eq_curvature` returned that field
verbatim (the self-assuming projection forbidden by AGENTS.md §3b-cond
item 5).  Now the structure carries only the two observation increments
as *data*, the `q`-curvature on the loop is **defined** as the
transport defect around the parallelogram — the difference of the two
path-ordered first-order transports `(1 + δq₁)(1 + δq₂)` and
`(1 + δq₂)(1 + δq₁)` — and the identity `[δq₁, δq₂] = F_q` is
**derived** by genuine (non-commutative) ring algebra, along with both
consequences.

Ref: [leitner2026] rem:two-observer-parallelogram, def:q-flat-connection
-/

namespace QOU.LocalQ

variable {R : Type*} [Ring R]

/-- The observation commutator (ring/Lie bracket) of two germ-level
    substrate perturbations at a point `p`. Non-trivial precisely
    because the germ algebra `A/𝔪_p²` is non-commutative. -/
def obsCommutator (a b : R) : R := a * b - b * a

/-- **Two-observer parallelogram** at a point `p`: the pair of
    observation perturbations `δq₁, δq₂ ∈ R` spanning the infinitesimal
    loop.  Only the two increments are data; the `q`-curvature on the
    loop is *defined* below as the transport defect around the
    parallelogram, and the parallelogram identity `[δq₁, δq₂] = F_q`
    is *derived* (`commutator_eq_curvature`). -/
structure ObservationParallelogram (R : Type*) [Ring R] where
  /-- First observer's germ-level perturbation of the substrate. -/
  δq₁ : R
  /-- Second observer's germ-level perturbation of the substrate. -/
  δq₂ : R

namespace ObservationParallelogram

/-- First-order transport of the first observation: the germ-level
    increment acts on the fibre as `1 + δq₁` (identity plus the
    perturbation). -/
def transport₁ (P : ObservationParallelogram R) : R := 1 + P.δq₁

/-- First-order transport of the second observation. -/
def transport₂ (P : ObservationParallelogram R) : R := 1 + P.δq₂

/-- The `q`-curvature 2-form evaluated on the loop, **defined** as the
    transport defect around the parallelogram: the difference between
    transporting first along observer 1 then observer 2 and the
    opposite ordering,
    `F_q = (1 + δq₁)(1 + δq₂) − (1 + δq₂)(1 + δq₁)`. -/
def Fq (P : ObservationParallelogram R) : R :=
  P.transport₁ * P.transport₂ - P.transport₂ * P.transport₁

/-- **Germ-commutator = q-curvature.** The commutator of the two
    observations equals the `q`-curvature 2-form on the loop: the
    linear (`1·δq`) terms of the two path-ordered transports cancel and
    only the second-order ordering defect `δq₁δq₂ − δq₂δq₁` survives.
    Derived by non-commutative ring algebra, not assumed. -/
theorem commutator_eq_curvature (P : ObservationParallelogram R) :
    obsCommutator P.δq₁ P.δq₂ = P.Fq := by
  simp only [obsCommutator, Fq, transport₁, transport₂]
  noncomm_ring

/-- The two observers **agree** (vanishing parallelogram) iff the
    `q`-curvature vanishes — the boson / `q`-flat case. -/
theorem agree_iff_flat (P : ObservationParallelogram R) :
    obsCommutator P.δq₁ P.δq₂ = 0 ↔ P.Fq = 0 := by
  rw [P.commutator_eq_curvature]

/-- **Antisymmetry of the q-curvature.** Swapping the two observers
    negates the curvature: `F_q` is a genuine 2-form on the loop. -/
theorem curvature_antisymm
    (P Q : ObservationParallelogram R)
    (h₁ : Q.δq₁ = P.δq₂) (h₂ : Q.δq₂ = P.δq₁) :
    Q.Fq = - P.Fq := by
  simp only [Fq, transport₁, transport₂, h₁, h₂]
  noncomm_ring

end ObservationParallelogram

end QOU.LocalQ
