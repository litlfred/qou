import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# QOU.FluidDynamics.leray_profile — finite-dimensional Leray profile

**Proposition** ([`prop:leray-profile`](../../../quantum-observable-universe/fluid-dynamics/leray-profile.md)).

*Near the blowup time `T*`, the singular NS solution approaches a
self-similar Leray profile `V(ξ)` on the rescaled coordinate
`ξ = (x − x₀)/√(T* − t)`.  QOU representation theory constrains `V` to a
finite-dimensional ansatz: a sum of weight-`j` matrix entries of
`SU_q(2)` representations; in particular `V(0) = Σ_n V_n`.*

## Formalisation notes
- **Base ring (§7c).** Generic `{R : Type*} [CommRing R]` — no `ℝ`.  The
  reconstruction identity is linear algebra over the substrate ring; the
  rescaling `√(T* − t)` is archimedean context that lives in the `.md`
  (a post-wall specialisation), not in the statement proved here.
- **Import fix.** The previous file imported the renamed (removed) module
  `Mathlib.Algebra.BigOperators.Basic` and so never compiled; the current
  path is `Mathlib.Algebra.BigOperators.Group.Finset.Basic`.
- **Non-degenerate conditional (§3b-cond cond. 5).** The class carries the
  genuine ansatz hypotheses — a weight-component *expansion* of `V` with
  basis entries normalised at `0` — and the theorem *derives* the
  reconstruction `V 0 = Σ_n V_coeff n` by evaluating the expansion
  (previously the identity itself was a class field). -/

namespace QOU.FluidDynamics

open Finset

/-- Hypotheses for the finite-dimensional Leray profile (§7c: generic
    `CommRing`, no `ℝ`).  `basis n` are the weight-`n` matrix entries of
    the `SU_q(2)` ansatz, normalised to `1` at the origin of the rescaled
    coordinate; `profile_expansion` is the finite ansatz itself. -/
class LerayProfileContext (R : Type*) [CommRing R] where
  /-- The Leray profile `V` on the rescaled coordinate. -/
  V : R → R
  /-- Maximum spin level `j_max` in the finite-dimensional ansatz. -/
  j_max : ℕ
  /-- Ansatz coefficients, fixed by the singular gerbe data
      `(Σ, n*, κ_{n*})`. -/
  V_coeff : Fin (j_max + 1) → R
  /-- Weight-`n` matrix-entry basis functions of the ansatz. -/
  basis : Fin (j_max + 1) → R → R
  /-- **Normalisation:** each basis entry equals `1` at the origin. -/
  basis_at_zero : ∀ n, basis n 0 = 1
  /-- **Finite ansatz (the representation-theoretic input):** `V` is the
      finite sum of its weight components. -/
  profile_expansion : ∀ x : R, V x = ∑ n, V_coeff n * basis n x

/-- **Leray-profile reconstruction** ([`prop:leray-profile`]).

    `V(0) = Σ_n V_coeff n` — *derived* by evaluating the finite ansatz
    `profile_expansion` at `0` and applying the basis normalisation
    (`mul_one` per component). -/
-- Ref: [manuscript] quantum-observable-universe/fluid-dynamics/leray-profile.ts
theorem leray_profile {R : Type*} [CommRing R] [ctx : LerayProfileContext R] :
    ctx.V 0 = ∑ n : Fin (ctx.j_max + 1), ctx.V_coeff n := by
  rw [ctx.profile_expansion 0]
  exact Finset.sum_congr rfl fun n _ => by rw [ctx.basis_at_zero n, mul_one]

end QOU.FluidDynamics
