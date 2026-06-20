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

Ref: [manuscript] rem:two-observer-parallelogram, def:q-flat-connection
-/

namespace QOU.LocalQ

variable {R : Type*} [Ring R]

/-- The observation commutator (ring/Lie bracket) of two germ-level
    substrate perturbations at a point `p`. Non-trivial precisely
    because the germ algebra `A/𝔪_p²` is non-commutative. -/
def obsCommutator (a b : R) : R := a * b - b * a

/-- **Two-observer parallelogram** at a point `p`: a pair of
    observation perturbations `δq₁, δq₂ ∈ R` together with the
    `q`-curvature value `Fq` on the loop they span, satisfying the
    parallelogram identity `[δq₁, δq₂] = Fq`. -/
structure ObservationParallelogram (R : Type*) [Ring R] where
  /-- First observer's germ-level perturbation of the substrate. -/
  δq₁ : R
  /-- Second observer's germ-level perturbation of the substrate. -/
  δq₂ : R
  /-- The `q`-curvature 2-form evaluated on the loop. -/
  Fq : R
  /-- The parallelogram identity: the observation commutator equals
      the `q`-curvature on the loop. -/
  parallelogram : obsCommutator δq₁ δq₂ = Fq

namespace ObservationParallelogram

/-- **Germ-commutator = q-curvature.** The commutator of the two
    observations equals the `q`-curvature 2-form on the loop. -/
theorem commutator_eq_curvature (P : ObservationParallelogram R) :
    obsCommutator P.δq₁ P.δq₂ = P.Fq :=
  P.parallelogram

/-- The two observers **agree** (vanishing parallelogram) iff the
    `q`-curvature vanishes — the boson / `q`-flat case. -/
theorem agree_iff_flat (P : ObservationParallelogram R) :
    obsCommutator P.δq₁ P.δq₂ = 0 ↔ P.Fq = 0 := by
  rw [P.parallelogram]

/-- **Antisymmetry of the q-curvature.** Swapping the two observers
    negates the curvature: `F_q` is a genuine 2-form on the loop. -/
theorem curvature_antisymm
    (P Q : ObservationParallelogram R)
    (h₁ : Q.δq₁ = P.δq₂) (h₂ : Q.δq₂ = P.δq₁) :
    Q.Fq = - P.Fq := by
  rw [← Q.parallelogram, ← P.parallelogram, h₁, h₂]
  unfold obsCommutator
  rw [neg_sub]

end ObservationParallelogram

end QOU.LocalQ
