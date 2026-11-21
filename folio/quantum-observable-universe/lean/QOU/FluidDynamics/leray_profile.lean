import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Fintype.Basic

/-!
# QOU.FluidDynamics.leray_profile — finite-dimensional Leray profile

**Galerkin reconstruction identity** for a finite truncation of a Leray profile
(see [`def:leray-profile`](../../../fluid-dynamics/leray-profile.md) and
`rem:leray-profile-construction`).

*If a profile `V` is written as a finite sum `Σ_n V_n · b_n` of basis functions
normalised to `1` at the origin, then `V(0) = Σ_n V_n`.*

**Re-scoped 2026-11-21 (issue #8864).** This file used to be the Lean sibling
of `prop:leray-profile` and described the basis as "weight-`j` matrix entries
of `SU_q(2)`". That description is withdrawn: a velocity field on `ℝ³` carries
only integer-degree vector spherical harmonics (half-integer spins cannot
occur, `IntegerSpin.even_of_neg_one_pow_eq_one`), and a finite truncation is
a Galerkin approximation, not an exact reduction. The theorem below is a
finite-sum evaluation; it says nothing about existence of a profile. The block
is now a definition (`def:leray-profile`) whose Lean sibling is
`fluid-dynamics/leray-profile.lean`.

## Formalisation notes
- **Base ring (§7c).** Generic `{R : Type*} [CommRing R]` — no `ℝ`.  The
  reconstruction identity is linear algebra over the substrate ring; the
  rescaling `√(T* − t)` is archimedean context that lives in the `.md`
  (a post-wall specialisation), not in the statement proved here.
- **Import fix.** The previous file imported the renamed (removed) module
  `Mathlib.Algebra.BigOperators.Basic` and so never compiled; the current
  path is `Mathlib.Algebra.BigOperators.Group.Finset.Basic`.
- **Non-degenerate conditional (§3b-cond cond. 5).** The class carries the
  genuine ansatz hypotheses — a finite *expansion* of `V` with
  basis entries normalised at `0` — and the theorem *derives* the
  reconstruction `V 0 = Σ_n V_coeff n` by evaluating the expansion
  (previously the identity itself was a class field). -/

namespace QOU.FluidDynamics

open Finset

/-- Hypotheses for the finite-dimensional Leray profile (§7c: generic
    `CommRing`, no `ℝ`).  `basis n` are the basis functions of a finite
    (Galerkin) truncation, normalised to `1` at the origin of the rescaled
    coordinate; `profile_expansion` is the truncated expansion itself. -/
class LerayProfileContext (R : Type*) [CommRing R] where
  /-- The Leray profile `V` on the rescaled coordinate. -/
  V : R → R
  /-- Number of retained basis functions minus one (truncation order). -/
  j_max : ℕ
  /-- Coefficients of the truncated expansion. -/
  V_coeff : Fin (j_max + 1) → R
  /-- Basis functions of the truncation. -/
  basis : Fin (j_max + 1) → R → R
  /-- **Normalisation:** each basis entry equals `1` at the origin. -/
  basis_at_zero : ∀ n, basis n 0 = 1
  /-- **Truncated expansion:** `V` is the finite sum of its components. -/
  profile_expansion : ∀ x : R, V x = ∑ n : Fin (j_max + 1), V_coeff n * basis n x

/-- **Galerkin reconstruction at the origin.**

    `V(0) = Σ_n V_coeff n` — *derived* by evaluating the finite ansatz
    `profile_expansion` at `0` and applying the basis normalisation
    (`mul_one` per component). -/
-- Ref: [leitner2026] quantum-observable-universe/fluid-dynamics/leray-profile-construction.md
theorem leray_profile {R : Type*} [CommRing R] [ctx : LerayProfileContext R] :
    ctx.V 0 = ∑ n : Fin (ctx.j_max + 1), ctx.V_coeff n := by
  rw [ctx.profile_expansion 0]
  exact Finset.sum_congr rfl fun n _ => by rw [ctx.basis_at_zero n, mul_one]

end QOU.FluidDynamics
