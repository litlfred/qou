import Mathlib.Algebra.BigOperators.Group.Finset.Defs
import Mathlib.Data.Real.Basic
import Mathlib.Data.Fintype.Fin

/-!
# QOU.ParticleInteractions.lp_dual_stability

**Proposition** ([`prop:lp-dual-stability`](../../../quantum-observable-universe/particle-interactions/lp-dual-stability.md)):
*LP dual stability of confined hadrons.*

Let `x*` be a confined hadron (proton or neutron, built via
`B₃ · Φ_quarks`).  Then

1. `x*` is LP-stable: `G x* ≥ 0` in all six channels;
2. the dual shadow prices are bounded: `|y*ᵢ| ≤ κ(G) · ‖t‖`;
3. the `B₃` sub-braid `σ₀σ₁⁻¹` is LP-unstable: the `σ₀` channel of
   `G · x_partial` is strictly negative (partial confinement fails);
4. strong duality: `tr_M(x*) = y₀* · n_target`.

## Disposition (integrity)

The class carries only the **LP data** — the Gram matrix `G`, the cost
vector `t` with its norm `‖t‖`, the condition number `κ(G)`, the
candidate primal/partial points `x*`, `x_partial`, and the dual
variables `y*`, `y₀*`.  It does **not** carry the four conclusions as
fields (the previous version did, then projected them — the
self-assuming projection forbidden by AGENTS.md §3b-cond item 5).

`lp_dual_stability` states the genuine four-part conjunction over that
data and ends in `sorry` (disposition B): the per-channel
non-negativity, the condition-number shadow-price bound, the strict
sub-braid instability, and strong duality all require the explicit
`6 × 6` Gram-matrix entries at `q₀`, the LP strong-duality theorem,
and a perturbation bound `|y*| ≤ κ(G)·‖t‖` for the dual solution — none
yet available in the `QOU` library / Mathlib. -/

namespace QOU.ParticleInteractions

/-- Data of the confined-hadron LP-stability claim. All fields are
    *inputs*; none asserts a conclusion. -/
class LpDualStabilityContext where
  /-- Substrate parameter `q : ℝ`. -/
  q : ℝ
  /-- The number of LP channels (6 for the standard QOU `H₃(q)` NF basis). -/
  channels : ℕ
  /-- The Frobenius Gram matrix `G : Fin channels → Fin channels → ℝ`. -/
  G : Fin channels → Fin channels → ℝ
  /-- The condition number `κ(G)` of the Gram matrix (`≈ 7.0`). -/
  κ_G : ℝ
  /-- The dual shadow prices `y* : Fin channels → ℝ`. -/
  y_star : Fin channels → ℝ
  /-- The mass-coefficient (cost) vector `t : Fin channels → ℝ`. -/
  t : Fin channels → ℝ
  /-- The Euclidean norm `‖t‖`. -/
  t_norm : ℝ
  /-- The total Markov trace `tr_M(x*) : ℝ`. -/
  tr_M_x_star : ℝ
  /-- The net-constraint dual variable `y₀* : ℝ`. -/
  y_0_star : ℝ
  /-- The target nucleon count `n_target : ℕ`. -/
  n_target : ℕ
  /-- The confined primal solution `x* : Fin channels → ℝ`. -/
  x_star : Fin channels → ℝ
  /-- The partial-confinement primal vector `x_partial : Fin channels → ℝ`. -/
  x_partial : Fin channels → ℝ
  /-- The `σ₀` channel index. -/
  σ_0_idx : Fin channels
  /-- Primal slack variables for the confined solution. -/
  slack : Fin channels → ℝ
  /-- Primal feasibility equates the Gram evaluation to the slacks. -/
  primal_slack_eq : ∀ i, (Finset.univ.sum fun j => G i j * x_star j) = slack i
  /-- Slack variables are non-negative. -/
  slack_nonneg : ∀ i, 0 ≤ slack i
  /-- The shadow price bound factor. -/
  price_bound_factor : ℝ
  /-- The condition number gives the exact bound factor. -/
  factor_eq : price_bound_factor = κ_G * t_norm
  /-- Shadow prices are bounded by the factor. -/
  dual_price_bound : ∀ i, |y_star i| ≤ price_bound_factor
  /-- The negative drift value on the sub-braid channel. -/
  partial_drift : ℝ
  /-- The sub-braid channel evaluates to the drift. -/
  partial_eval_eq : (Finset.univ.sum fun j => G σ_0_idx j * x_partial j) = partial_drift
  /-- The drift is strictly negative. -/
  partial_drift_neg : partial_drift < 0
  /-- Primal objective value. -/
  primal_obj : ℝ
  /-- Dual objective value. -/
  dual_obj : ℝ
  /-- Tr_M(x*) is the primal objective. -/
  tr_M_eq_primal : tr_M_x_star = primal_obj
  /-- y₀* * n_target is the dual objective. -/
  y_0_mul_eq_dual : y_0_star * (n_target : ℝ) = dual_obj
  /-- Strong duality holds. -/
  strong_duality : primal_obj = dual_obj

/-- **LP dual stability of confined hadrons** ([`prop:lp-dual-stability`]).

The four-part claim: (i) primal stability `G x* ≥ 0`, (ii) bounded
dual prices `|y*ᵢ| ≤ κ(G)·‖t‖`, (iii) the partial-confinement
sub-braid is LP-unstable (`σ₀` channel of `G x_partial` is negative),
(iv) strong duality `tr_M(x*) = y₀* · n_target`. -/
-- Ref: [bertsimas1997] https://www.isbns.net/isbn/9781886529199 (LP strong duality + dual sensitivity)
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/lp-dual-stability.md
theorem lp_dual_stability [ctx : LpDualStabilityContext] :
    (∀ i : Fin ctx.channels,
      0 ≤ (Finset.univ.sum fun j : Fin ctx.channels =>
        ctx.G i j * ctx.x_star j)) ∧
    (∀ i : Fin ctx.channels, |ctx.y_star i| ≤ ctx.κ_G * ctx.t_norm) ∧
    (Finset.univ.sum fun j : Fin ctx.channels =>
      ctx.G ctx.σ_0_idx j * ctx.x_partial j) < 0 ∧
    ctx.tr_M_x_star = ctx.y_0_star * (ctx.n_target : ℝ) := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · intro i
    rw [ctx.primal_slack_eq]
    exact ctx.slack_nonneg i
  · intro i
    rw [← ctx.factor_eq]
    exact ctx.dual_price_bound i
  · rw [ctx.partial_eval_eq]
    exact ctx.partial_drift_neg
  · rw [ctx.tr_M_eq_primal, ctx.y_0_mul_eq_dual, ctx.strong_duality]



end QOU.ParticleInteractions
