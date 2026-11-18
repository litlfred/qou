import Mathlib.Analysis.SpecialFunctions.Exp
import QOU.FluidDynamics.q_ns_energy_and_decay

/-!
# QOU.FluidDynamics.q_ns_wellposedness

Content block
[`thm:q-ns-wellposedness`](../../../quantum-observable-universe/fluid-dynamics/q-ns-wellposedness.md):
*Global regularity of the $q$-deformed Navier--Stokes equation*.

The block's claim: for a divergence-free initial velocity 1-form
`v₀ ∈ ker(δ_q|_{Ω¹(A)})` with finite Frobenius norm, the q-deformed
Navier--Stokes system admits a **unique global solution**
`(v, p) : [0, ∞) → ker(δ_q|_{Ω¹(A)}) × A` such that

1. **smoothness**: `t ↦ v(t)` is smooth in the internal hom of `𝐂`;
2. **energy inequality**: `‖v(t)‖_A² + 2ν_q ∫₀ᵗ ‖d_q v(s)‖_A² ds ≤ ‖v₀‖_A²`
   for all `t ≥ 0`;
3. **spectral decay**: the `Δ_q`-eigencomponents satisfy
   `|v̂_k(t)| ≤ |v̂_k(0)| · exp(−ν_q [k]_q² t)`.

## Disposition (integrity) — what is assumed, and what is proved

**Previously** the class carried a single field `wellposedness_holds`
whose type was *verbatim the conclusion below*, and the theorem was
`ctx.wellposedness_holds`: a self-assuming projection (AGENTS.md
§3b-cond item 5).  The file's own docstring asserted the opposite — that
it was `sorry`'d and that nothing in the class assumed any part of the
conclusion — which was false on all three counts.  Recorded in
`docs/audits/2026-08-29-q-ns-conjecture-statement-strength.md`; the
declaration is in `lean-vacuity-review-ledger.json` under
`proof-no-self-assuming-projection`, verdict `genuine`.

**Now** the four claims are separated by what each actually needs, and
only the genuinely open ones are hypotheses:

| block property | here |
|---|---|
| existence + uniqueness | `existence_uniqueness` — **assumed** (Millennium-adjacent; bean `qou-t28w`, tier B) |
| (i) smoothness | `smooth_of_isSolution` — **assumed** (regularity; the same open problem) |
| (ii) energy inequality | `q_ns_energy_inequality` — **proved** here |
| (iii) spectral decay | `q_ns_spectral_decay` — **proved** here |

(ii) and (iii) are discharged by
[`q_ns_energy_and_decay`](q_ns_energy_and_decay.lean), from the
*equations* — the pointwise energy balance `E' + 2ν_q D ≤ 0` and the
modal inequality `d/dt|v̂_k| ≤ −ν_q [k]_q² |v̂_k|` — rather than from any
assumption about the integrated bounds themselves.  No field of the
class is, or implies, either conclusion.

What remains assumed is exactly the open problem, no more: that a
solution exists, is unique, and is smooth.

## References

- [leitner2026] quantum-observable-universe/fluid-dynamics/q-ns-wellposedness.md
  (`thm:q-ns-wellposedness`)
-/

namespace QOU.FluidDynamics

open Set

/-- Carrier data and hypotheses for [`thm:q-ns-wellposedness`].

    The fields split into three kinds, and the split is the point:

    * **data** — carriers, the initial datum, the norm / dissipation /
      eigencomponent functionals, the rate functionals, and the opaque
      `Smooth` / `IsSolution` *predicates* (which fix what the words
      mean, and assert nothing);
    * **the equations** — `energy_balance` and `modal_inequality`, the
      pointwise differential statements the q-NS system makes, plus the
      analytic regularity needed to integrate them;
    * **the open inputs** — `existence_uniqueness` and
      `smooth_of_isSolution`, and nothing else.

    Neither the energy inequality nor the spectral-decay bound appears
    as a field; both are theorems below. -/
class QNsWellposednessContext where
  /-- The substrate parameter `q : ℝ`. -/
  q : ℝ
  q_gt_one : 1 < q
  /-- The kinematic viscosity `ν_q = ½(1 − q⁻¹) > 0`. -/
  ν_q : ℝ
  ν_q_eq : ν_q = (1 - q⁻¹) / 2
  ν_q_pos : 0 < ν_q
  /-- Carrier of divergence-free velocity 1-forms `ker(δ_q|_{Ω¹(A)})`. -/
  Velocity : Type
  /-- Carrier of pressures (elements of the algebra `A`). -/
  Pressure : Type
  /-- The divergence-free initial velocity `v₀` (finite Frobenius norm). -/
  v₀ : Velocity
  /-- Squared Frobenius (`L²`) norm `‖·‖_A²` on velocities. -/
  norm_sq : Velocity → ℝ
  /-- Cumulative dissipation `t ↦ ∫₀ᵗ ‖d_q v(s)‖_A² ds`. -/
  dissipation : (ℝ → Velocity) → ℝ → ℝ
  /-- The `k`-th `Δ_q`-eigencomponent magnitude `|v̂_k|`. -/
  v_hat : ℕ → Velocity → ℝ
  /-- The q-integer `[k]_q`; `Δ_q|_{V_k} = [k]_q² id`. -/
  q_int : ℕ → ℝ
  /-- Smoothness predicate.  Opaque *definition* data — which
      trajectories count as smooth — not an assumption that any
      trajectory is smooth. -/
  Smooth : (ℝ → Velocity) → Prop
  /-- Solution predicate.  Opaque *definition* data — which trajectories
      count as solutions — not an assumption that one exists. -/
  IsSolution : (ℝ → Velocity × Pressure) → Prop
  /-- Rate of change of the kinetic energy along a trajectory, `E'(t)`. -/
  energyRate : (ℝ → Velocity) → ℝ → ℝ
  /-- Instantaneous dissipation `D(t) = ‖d_q v(t)‖_A²`. -/
  dissipationRate : (ℝ → Velocity) → ℝ → ℝ
  /-- Rate of change of the `k`-th eigencomponent magnitude. -/
  modalRate : ℕ → (ℝ → Velocity) → ℝ → ℝ
  /-- **OPEN INPUT.**  Global existence and uniqueness of the q-NS
      solution.  This is the Millennium-adjacent content of the block
      and the only substantive thing assumed here (with
      `smooth_of_isSolution`).  Bean `qou-t28w`, tier B. -/
  -- Ref: [leitner2026] quantum-observable-universe/fluid-dynamics/q-ns-wellposedness.md (thm:q-ns-wellposedness)
  existence_uniqueness : ∃! sol : ℝ → Velocity × Pressure, IsSolution sol
  /-- **OPEN INPUT.**  Interior regularity: a solution is smooth in the
      internal hom of `𝐂`.  Block property (i). -/
  -- Ref: [leitner2026] quantum-observable-universe/fluid-dynamics/q-ns-wellposedness.md (thm:q-ns-wellposedness)
  smooth_of_isSolution : ∀ sol, IsSolution sol → Smooth (fun t => (sol t).1)
  /-- A solution starts at the initial datum. -/
  initial_datum : ∀ sol, IsSolution sol → (sol 0).1 = v₀
  /-- Cumulative dissipation vanishes at `t = 0` (it is an integral
      from `0`). -/
  dissipation_zero : ∀ sol, IsSolution sol →
    dissipation (fun s => (sol s).1) 0 = 0
  /-- Analytic regularity of the energy functional along a solution. -/
  energy_continuousOn : ∀ sol, IsSolution sol → ∀ T : ℝ,
    ContinuousOn
      (fun t => norm_sq (sol t).1 + 2 * ν_q * dissipation (fun s => (sol s).1) t)
      (Icc 0 T)
  /-- The energy functional differentiates to the sum of its rates. -/
  energy_hasDeriv : ∀ sol, IsSolution sol → ∀ T : ℝ, ∀ t ∈ Ico 0 T,
    HasDerivWithinAt
      (fun s => norm_sq (sol s).1 + 2 * ν_q * dissipation (fun s => (sol s).1) s)
      (energyRate (fun s => (sol s).1) t
        + 2 * ν_q * dissipationRate (fun s => (sol s).1) t)
      (Ici t) t
  /-- **THE EQUATION** (energy balance): the differential form of the
      q-NS energy identity.  Note this is a statement about the *rates*,
      i.e. about the equations — not about the integrated bound, which
      is derived from it in `q_ns_energy_inequality`. -/
  energy_balance : ∀ sol, IsSolution sol → ∀ t : ℝ, 0 ≤ t →
    energyRate (fun s => (sol s).1) t
      + 2 * ν_q * dissipationRate (fun s => (sol s).1) t ≤ 0
  /-- Analytic regularity of each eigencomponent along a solution. -/
  modal_continuousOn : ∀ sol, IsSolution sol → ∀ (k : ℕ) (T : ℝ),
    ContinuousOn (fun t => v_hat k (sol t).1) (Icc 0 T)
  /-- Each eigencomponent differentiates to its modal rate. -/
  modal_hasDeriv : ∀ sol, IsSolution sol → ∀ (k : ℕ) (T : ℝ), ∀ t ∈ Ico 0 T,
    HasDerivWithinAt (fun s => v_hat k (sol s).1)
      (modalRate k (fun s => (sol s).1) t) (Ici t) t
  /-- **THE EQUATION** (modal inequality): `Δ_q` acts on the `k`-th
      eigenspace by `[k]_q²`, so the eigencomponent obeys
      `d/dt |v̂_k| ≤ −ν_q [k]_q² |v̂_k|`.  Again a statement about the
      rate; the exponential bound is derived in
      `q_ns_spectral_decay`. -/
  modal_inequality : ∀ sol, IsSolution sol → ∀ (k : ℕ) (t : ℝ), 0 ≤ t →
    modalRate k (fun s => (sol s).1) t
      ≤ -(ν_q * (q_int k) ^ 2) * v_hat k (sol t).1

/-- **Energy inequality** ([`thm:q-ns-wellposedness`] property (ii)):
    `‖v(t)‖_A² + 2ν_q ∫₀ᵗ ‖d_q v(s)‖_A² ds ≤ ‖v₀‖_A²`.

    **Proved**, from the pointwise energy balance — not assumed. -/
theorem q_ns_energy_inequality [ctx : QNsWellposednessContext]
    (sol : ℝ → ctx.Velocity × ctx.Pressure) (hsol : ctx.IsSolution sol)
    (t : ℝ) (ht : 0 ≤ t) :
    ctx.norm_sq (sol t).1
      + 2 * ctx.ν_q * ctx.dissipation (fun s => (sol s).1) t
      ≤ ctx.norm_sq ctx.v₀ := by
  have key :=
    energy_inequality_of_balance
      (E := fun s => ctx.norm_sq (sol s).1)
      (Dcum := fun s => ctx.dissipation (fun s => (sol s).1) s)
      (E' := fun s => ctx.energyRate (fun s => (sol s).1) s)
      (D := fun s => ctx.dissipationRate (fun s => (sol s).1) s)
      (ν := ctx.ν_q) (T := t)
      (ctx.energy_continuousOn sol hsol t)
      (fun s hs => ctx.energy_hasDeriv sol hsol t s hs)
      (fun s hs => ctx.energy_balance sol hsol s hs.1)
      (ctx.dissipation_zero sol hsol)
      t ⟨ht, le_rfl⟩
  rw [← ctx.initial_datum sol hsol]
  exact key

/-- **`Δ_q`-spectral decay** ([`thm:q-ns-wellposedness`] property (iii)):
    `|v̂_k(t)| ≤ |v̂_k(0)| · exp(−ν_q [k]_q² t)`.

    **Proved**, from the modal differential inequality — not assumed. -/
theorem q_ns_spectral_decay [ctx : QNsWellposednessContext]
    (sol : ℝ → ctx.Velocity × ctx.Pressure) (hsol : ctx.IsSolution sol)
    (k : ℕ) (t : ℝ) (ht : 0 ≤ t) :
    ctx.v_hat k (sol t).1
      ≤ ctx.v_hat k ctx.v₀ * Real.exp (-(ctx.ν_q * (ctx.q_int k) ^ 2) * t) := by
  have key :=
    modal_decay_of_deriv_le
      (a := fun s => ctx.v_hat k (sol s).1)
      (a' := fun s => ctx.modalRate k (fun s => (sol s).1) s)
      (c := ctx.ν_q * (ctx.q_int k) ^ 2) (T := t)
      (ctx.modal_continuousOn sol hsol k t)
      (fun s hs => ctx.modal_hasDeriv sol hsol k t s hs)
      (fun s hs => ctx.modal_inequality sol hsol k s hs.1)
      t ⟨ht, le_rfl⟩
  rw [← ctx.initial_datum sol hsol]
  exact key

/-- **Global regularity of the q-deformed Navier--Stokes equation**
    ([`thm:q-ns-wellposedness`]).

    The block's full claim, assembled.  Existence, uniqueness and
    smoothness are the class's open inputs; the energy inequality and the
    spectral decay are the two theorems above, and are **derived** from
    the equations rather than assumed.

    This is a conditional theorem in the §3b-cond sense and is honest
    about which conjunct carries the open problem — unlike the previous
    encoding, in which every conjunct was assumed at once. -/
theorem q_ns_wellposedness [ctx : QNsWellposednessContext] :
    (∃! sol : ℝ → ctx.Velocity × ctx.Pressure, ctx.IsSolution sol) ∧
    (∀ sol : ℝ → ctx.Velocity × ctx.Pressure, ctx.IsSolution sol →
      ctx.Smooth (fun t => (sol t).1) ∧
      (∀ t : ℝ, 0 ≤ t →
        ctx.norm_sq (sol t).1
          + 2 * ctx.ν_q * ctx.dissipation (fun s => (sol s).1) t
          ≤ ctx.norm_sq ctx.v₀) ∧
      (∀ (k : ℕ) (t : ℝ), 0 ≤ t →
        ctx.v_hat k (sol t).1
          ≤ ctx.v_hat k ctx.v₀
              * Real.exp (-(ctx.ν_q * (ctx.q_int k) ^ 2) * t))) :=
  ⟨ctx.existence_uniqueness, fun sol hsol =>
    ⟨ctx.smooth_of_isSolution sol hsol,
     fun t ht => q_ns_energy_inequality sol hsol t ht,
     fun k t ht => q_ns_spectral_decay sol hsol k t ht⟩⟩

/-- **Uniqueness of global q-NS trajectories**: any two trajectories satisfying
    `ctx.IsSolution` are identical. -/
theorem q_ns_solution_eq_of_isSolution [ctx : QNsWellposednessContext]
    (sol₁ sol₂ : ℝ → ctx.Velocity × ctx.Pressure)
    (hsol₁ : ctx.IsSolution sol₁) (hsol₂ : ctx.IsSolution sol₂) :
    sol₁ = sol₂ := by
  obtain ⟨sol, _, huniq⟩ := ctx.existence_uniqueness
  exact (huniq sol₁ hsol₁).trans (huniq sol₂ hsol₂).symm

/-- **Kinetic energy bound**: when cumulative dissipation at time `t ≥ 0` is
    non-negative, the kinetic energy `‖v(t)‖_A²` never exceeds its initial value
    `‖v₀‖_A²`. -/
theorem q_ns_kinetic_energy_bounded [ctx : QNsWellposednessContext]
    (sol : ℝ → ctx.Velocity × ctx.Pressure) (hsol : ctx.IsSolution sol)
    (t : ℝ) (ht : 0 ≤ t)
    (hdiss : 0 ≤ ctx.dissipation (fun s => (sol s).1) t) :
    ctx.norm_sq (sol t).1 ≤ ctx.norm_sq ctx.v₀ := by
  have h_en := q_ns_energy_inequality sol hsol t ht
  have h_visc : 0 ≤ 2 * ctx.ν_q * ctx.dissipation (fun s => (sol s).1) t := by
    have hpos := ctx.ν_q_pos
    nlinarith
  linarith

/-- **Spectral mode monotonicity bound**: for any mode `k`, non-negative time `t ≥ 0`,
    and non-negative initial mode amplitude `0 ≤ |v̂_k(0)|`, the `k`-th eigencomponent
    at time `t` never exceeds its initial amplitude. -/
theorem q_ns_spectral_mode_nonincreasing [ctx : QNsWellposednessContext]
    (sol : ℝ → ctx.Velocity × ctx.Pressure) (hsol : ctx.IsSolution sol)
    (k : ℕ) (t : ℝ) (ht : 0 ≤ t)
    (hv₀ : 0 ≤ ctx.v_hat k ctx.v₀) :
    ctx.v_hat k (sol t).1 ≤ ctx.v_hat k ctx.v₀ := by
  have h_dec := q_ns_spectral_decay sol hsol k t ht
  have h_prod_nonneg : 0 ≤ (ctx.ν_q * (ctx.q_int k) ^ 2) * t :=
    mul_nonneg (mul_nonneg (le_of_lt ctx.ν_q_pos) (sq_nonneg (ctx.q_int k))) ht
  have h_rate_nonpos : -(ctx.ν_q * (ctx.q_int k) ^ 2) * t ≤ 0 := by
    linarith
  have h_exp : Real.exp (-(ctx.ν_q * (ctx.q_int k) ^ 2) * t) ≤ 1 :=
    Real.exp_le_one_iff.mpr h_rate_nonpos
  have h_mul :
      ctx.v_hat k ctx.v₀ * Real.exp (-(ctx.ν_q * (ctx.q_int k) ^ 2) * t)
        ≤ ctx.v_hat k ctx.v₀ * 1 :=
    mul_le_mul_of_nonneg_left h_exp hv₀
  linarith

end QOU.FluidDynamics
