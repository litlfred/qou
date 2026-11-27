import Mathlib.Analysis.SpecialFunctions.Exp
import QOU.Transcendental.FluidDynamics.q_ns_energy_and_decay

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
3. **spectral decay, for transfer-free flows only** (weakened
   2026-11-27, owner ruling): if the nonlinear mode transfer into the
   `k`-th `Δ_q`-eigencomponent is nonpositive, then
   `|v̂_k(t)| ≤ |v̂_k(0)| · exp(−ν_q [k]_q² t)`.  The unrestricted
   per-mode clause was the modal law of the linear Stokes equation.

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
| (iii) spectral decay | `q_ns_spectral_decay_of_no_transfer` — **proved** here, for transfer-free flows only (2026-11-27) |

(ii) and (iii) are discharged by
[`q_ns_energy_and_decay`](q_ns_energy_and_decay.lean), from the
*equations* — the pointwise energy balance `E' + 2ν_q D ≤ 0` and the
modal balance `d/dt|v̂_k| ≤ −ν_q [k]_q² |v̂_k| + T_k` with nonlinear
transfer `T_k` — rather than from any
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
    * **the equations** — `energy_balance` and `modal_balance`, the
      pointwise differential statements the q-NS system makes, plus the
      analytic regularity needed to integrate them;
    * **the open inputs** — `existence_uniqueness` and
      `smooth_of_isSolution`, and nothing else.

    Neither the energy inequality nor the spectral-decay bound appears
    as a field.  The energy inequality is a theorem below; spectral decay
    is a theorem for transfer-free flows only. -/
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
  /-- The nonlinear mode-transfer term in the `k`-th modal equation:
      the rate at which the advection term moves amplitude into the
      `k`-th `Δ_q`-eigencomponent along a trajectory.  Opaque data; the
      class assumes nothing about its sign.  For the linear Stokes flow,
      and for Beltrami eigenfields (Lamb vector zero), it vanishes. -/
  transfer : ℕ → (ℝ → Velocity) → ℝ → ℝ
  /-- **THE EQUATION** (modal balance): `Δ_q` acts on the `k`-th
      eigenspace by `[k]_q²`, so the eigencomponent obeys
      `d/dt |v̂_k| ≤ −ν_q [k]_q² |v̂_k| + T_k`, with `T_k` the nonlinear
      transfer.  **Weakened 2026-11-27** (owner ruling, Carl, card "Weaken
      decay clause, keep Part A"): this field used to read
      `d/dt |v̂_k| ≤ −ν_q [k]_q² |v̂_k|` with no transfer term.  That is the
      modal law of the *linear* Stokes equation and forbids the triad
      transfer of the nonlinear flow (audit
      `2026-11-27-qns-part-a-enstrophy-order-parameter.md`).  Per-mode
      decay is now a theorem only for transfer-free flows
      (`q_ns_spectral_decay_of_no_transfer`). -/
  modal_balance : ∀ sol, IsSolution sol → ∀ (k : ℕ) (t : ℝ), 0 ≤ t →
    modalRate k (fun s => (sol s).1) t
      ≤ -(ν_q * (q_int k) ^ 2) * v_hat k (sol t).1
          + transfer k (fun s => (sol s).1) t

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

/-- **`Δ_q`-spectral decay for transfer-free flows**
    ([`thm:q-ns-wellposedness`] property (iii), as weakened 2026-11-27):
    if the nonlinear transfer into mode `k` is nonpositive along the
    solution, then `|v̂_k(t)| ≤ |v̂_k(0)| · exp(−ν_q [k]_q² t)`.

    **Proved**, from the modal balance.  The hypothesis `hnt` holds for the
    linear Stokes flow and for Beltrami eigenfields; it does **not** hold
    for the nonlinear flow in general, where triads move energy between
    modes. -/
theorem q_ns_spectral_decay_of_no_transfer [ctx : QNsWellposednessContext]
    (sol : ℝ → ctx.Velocity × ctx.Pressure) (hsol : ctx.IsSolution sol)
    (k : ℕ) (hnt : ∀ s, 0 ≤ s → ctx.transfer k (fun s => (sol s).1) s ≤ 0)
    (t : ℝ) (ht : 0 ≤ t) :
    ctx.v_hat k (sol t).1
      ≤ ctx.v_hat k ctx.v₀ * Real.exp (-(ctx.ν_q * (ctx.q_int k) ^ 2) * t) := by
  have key :=
    modal_decay_of_deriv_le
      (a := fun s => ctx.v_hat k (sol s).1)
      (a' := fun s => ctx.modalRate k (fun s => (sol s).1) s)
      (c := ctx.ν_q * (ctx.q_int k) ^ 2) (T := t)
      (ctx.modal_continuousOn sol hsol k t)
      (fun s hs => ctx.modal_hasDeriv sol hsol k t s hs)
      (fun s hs => by
        have h1 := ctx.modal_balance sol hsol k s hs.1
        have h2 := hnt s hs.1
        linarith)
      t ⟨ht, le_rfl⟩
  rw [← ctx.initial_datum sol hsol]
  exact key

/-- **Global regularity of the q-deformed Navier--Stokes equation**
    ([`thm:q-ns-wellposedness`]).

    The block's claim, assembled.  Existence, uniqueness and smoothness
    are the class's open inputs; the energy inequality is **derived** from
    the energy balance.  Per-mode spectral decay is no longer a conjunct
    (owner ruling 2026-11-27): it holds only for transfer-free flows and
    is stated separately as `q_ns_spectral_decay_of_no_transfer`. -/
theorem q_ns_wellposedness [ctx : QNsWellposednessContext] :
    (∃! sol : ℝ → ctx.Velocity × ctx.Pressure, ctx.IsSolution sol) ∧
    (∀ sol : ℝ → ctx.Velocity × ctx.Pressure, ctx.IsSolution sol →
      ctx.Smooth (fun t => (sol t).1) ∧
      (∀ t : ℝ, 0 ≤ t →
        ctx.norm_sq (sol t).1
          + 2 * ctx.ν_q * ctx.dissipation (fun s => (sol s).1) t
          ≤ ctx.norm_sq ctx.v₀)) :=
  ⟨ctx.existence_uniqueness, fun sol hsol =>
    ⟨ctx.smooth_of_isSolution sol hsol,
     fun t ht => q_ns_energy_inequality sol hsol t ht⟩⟩

/-- Canonical resting-fluid instance of `QNsWellposednessContext` at substrate
    parameter `q = 2` (`ν_q = 1/4 > 0`), with `Velocity = Unit`, `Pressure = Unit`,
    and unique stationary equilibrium trajectory `sol = fun _ => ((), ())`.
    Witnesses that all fields and differential hypotheses of
    `QNsWellposednessContext` are mutually consistent and non-vacuous. -/
noncomputable def canonicalQNsWellposednessContext : QNsWellposednessContext where
  q := 2
  q_gt_one := by norm_num
  ν_q := (1 - (2 : ℝ)⁻¹) / 2
  ν_q_eq := rfl
  ν_q_pos := by norm_num
  Velocity := Unit
  Pressure := Unit
  v₀ := ()
  norm_sq := fun _ => 0
  dissipation := fun _ _ => 0
  v_hat := fun _ _ => 0
  q_int := fun k => k
  Smooth := fun _ => True
  IsSolution := fun sol => sol = fun _ => ((), ())
  energyRate := fun _ _ => 0
  dissipationRate := fun _ _ => 0
  modalRate := fun _ _ _ => 0
  transfer := fun _ _ _ => 0
  existence_uniqueness := ⟨fun _ => ((), ()), rfl, fun _ h => h⟩
  smooth_of_isSolution := fun _ _ => trivial
  initial_datum := fun _ _ => rfl
  dissipation_zero := fun _ _ => rfl
  energy_continuousOn := fun _ _ _ => continuousOn_const
  energy_hasDeriv := fun _ _ _ t _ => by
    simpa using (hasDerivWithinAt_const t (Ici t) (0 : ℝ))
  energy_balance := fun _ _ _ _ => by norm_num
  modal_continuousOn := fun _ _ _ _ => continuousOn_const
  modal_hasDeriv := fun _ _ _ _ t _ => by
    simpa using (hasDerivWithinAt_const t (Ici t) (0 : ℝ))
  modal_balance := fun _ _ _ _ _ => by norm_num

/-- `QNsWellposednessContext` is non-vacuously inhabitable. -/
theorem nonempty_qNsWellposednessContext : Nonempty QNsWellposednessContext :=
  ⟨canonicalQNsWellposednessContext⟩

/-- Concrete evaluation of `q_ns_wellposedness` in `canonicalQNsWellposednessContext`. -/
theorem canonical_q_ns_wellposedness :
    letI := canonicalQNsWellposednessContext
    (∃! sol : ℝ → canonicalQNsWellposednessContext.Velocity ×
        canonicalQNsWellposednessContext.Pressure,
      canonicalQNsWellposednessContext.IsSolution sol) :=
  letI := canonicalQNsWellposednessContext
  q_ns_wellposedness.1

end QOU.FluidDynamics
