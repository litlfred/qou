/-
# The monodromy Jordan structure at every rank — the τ-functor's domain object at q = i, pinned

Functor-assignment brick on the `TauRhoHodgeLift` wall. The F-construction's
T2 (merged #4040) computed that the cover's local monodromy is the H₂(i)
module — a genuine Jordan block, `(σ − i)² = 0`, non-semisimple — by
explicit Burau-at-i matrices. This file proves the SAME structure on the
length-rule module of ANY descent structure, at every rank, by pure algebra
from the merged all-ranks quadratic:

* **`monodromy_h`** — at the monodromy point `q = i` the Hecke parameter is
  `h = q − q⁻¹ = 2i`;
* **`eigenvalues_collide_at_monodromy`** — the two channel eigenvalues
  `q` and `−q⁻¹` COINCIDE at `q = i` (both `= i`): the e₊/e₋ channel pair
  (merged #4056) degenerates exactly at the monodromy point — the general-
  rank reason the T4 Markov weights are singular there and the T2 module is
  non-semisimple;
* **`jordan_sq_zero`** — `(σ − i)² = 0` on the length-rule module at every
  rank: the nilpotent part of the monodromy is universal, not a rank-3
  accident;
* **`jordan_nilpotent_ne_zero`** — `σ ≠ i·id` (witnessed on the constant
  state at a descent point, which every inhabited descent structure has):
  the Jordan block is GENUINE — the module is non-semisimple at `q = i` at
  every rank.

Together: the τ-functor's domain-side object at the assignment point
(T2's `q = i` evaluation) is now pinned at all ranks — Jordan structure,
channel degeneration, and (from the merged `channel_plus_star`) the
ρ-equivariance. What remains of `TauRhoHodgeLift` is the assignment map
itself onto the geometric side, whose target carries the matching
structure by T1–T3.

HONESTY (STRICT): this pins the DOMAIN data; the functor's existence and
naturality are untouched and stay open. Wall-1 note recorded in the audit:
Mathlib's Coxeter development (`GroupTheory.Coxeter.*` at the pinned rev)
carries no exchange/lifting property, so deriving the coset data of the
merged braid/far-commutation reductions from `CoxeterSystem` is blocked on
an upstream Mathlib gap, not on this corpus. Nothing wired; `1/(8π)` stays
phase-4.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/
import QOU.Machinery.HeckeDescentQuadratic
import Mathlib.Data.Complex.Basic

namespace QOU.Machinery.HeckeGeneral

open Complex

variable {W : Type*}

/-- At the monodromy point `q = i`, the Hecke parameter is `h = 2i`. -/
theorem monodromy_h : (I : ℂ) - I⁻¹ = 2 * I := by
  rw [Complex.inv_I]
  ring

/-- **The channel eigenvalues collide at the monodromy point**: `q = −q⁻¹`
at `q = i`. The e₊ eigenvalue `q` and the e₋ eigenvalue `−q⁻¹` of the
merged channel pair coincide — the general-rank source of the T2
non-semisimplicity and the T4 weight singularity at `q = i`. -/
theorem eigenvalues_collide_at_monodromy : -(I : ℂ)⁻¹ = I := by
  rw [Complex.inv_I]
  ring

/-- The nilpotent part of the monodromy action: `N = σ − i·id`. -/
noncomputable def monodromyN (D : DescentStructure W) (v : W → ℂ) : W → ℂ :=
  mulStep D (2 * I) v - I • v

/-- **`(σ − i)² = 0` at every rank** — the T2 Jordan-block relation, proved
on the length-rule module of ANY descent structure by pure algebra from
the all-ranks quadratic (`σ² = 2i·σ + 1` and `i² = −1`). -/
theorem jordan_sq_zero (D : DescentStructure W) (v : W → ℂ) :
    monodromyN D (monodromyN D v) = 0 := by
  unfold monodromyN
  have hsub : mulStep D (2 * I) v - I • v
      = mulStep D (2 * I) v + (-I) • v := by
    funext u
    simp only [Pi.sub_apply, Pi.add_apply, Pi.smul_apply, smul_eq_mul]
    ring
  rw [hsub, mulStep_add, mulStep_smul, mulStep_quadratic]
  funext u
  simp only [Pi.add_apply, Pi.sub_apply, Pi.smul_apply, Pi.zero_apply, smul_eq_mul]
  trans ((I * I + 1) * v u)
  · ring
  · rw [Complex.I_mul_I]
    ring

/-- Every inhabited descent structure has a descent point: since the step
never fixes the rank, either `u₀` or `t u₀` is a descent. -/
theorem exists_descent_point (D : DescentStructure W) (u₀ : W) :
    ∃ u, D.len (D.t u) < D.len u := by
  rcases lt_or_gt_of_ne (D.len_ne u₀) with hlt | hgt
  · exact ⟨u₀, hlt⟩
  · exact ⟨D.t u₀, by rw [D.t_invol]; exact hgt⟩

/-- **The Jordan block is genuine**: `σ ≠ i·id` at the monodromy point —
witnessed on the constant state at a descent point. With `jordan_sq_zero`,
the length-rule module at `q = i` is non-semisimple at EVERY rank: the T2
finding is universal. -/
theorem jordan_nilpotent_ne_zero (D : DescentStructure W) (u₀ : W) :
    mulStep D (2 * I) (fun _ => (1 : ℂ)) ≠ I • (fun _ => (1 : ℂ)) := by
  obtain ⟨u, hu⟩ := exists_descent_point D u₀
  intro hcontra
  have h := congrFun hcontra u
  simp only [mulStep, if_pos hu, Pi.smul_apply, smul_eq_mul, mul_one] at h
  -- h : 1 + 2i = i — impossible
  have : (1 : ℂ) + 2 * I = I := h
  have hre := congrArg Complex.re this
  simp at hre

end QOU.Machinery.HeckeGeneral
