import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic

/-!
# The two-nucleon total binding is framing-invariant, and floored at `α·log 4`

`computations/probes/ribbon_twist_t_selective_probe.py` established that the
ribbon twist is **T-odd** (`θ_{λ'} = θ_λ⁻¹`, so the `T = 1` channel picks up
`q^{+f}` and `T = 0` picks up `q^{-f}`) where the writhe is T-blind, and that a
framing `f ≥ 3` reproduces the required *sign* structure — the first construction
on this axis to do so. It flagged that `f = 3` is a threshold rather than a
derivation, and left open whether a framing can be derived.

**This file closes that route, and it closes it without ever deriving `f`.**
The question "which `f`?" turns out not to matter: the quantity nature measures
most sharply is invariant under the entire T-odd class.

## The invariant

Write the two channel bindings as `B_T = -α·log μ_T`. A T-odd rescaling by any
`t > 0` sends `(μ₊, μ₋) ↦ (μ₊·t, μ₋/t)` — the ribbon twist is the special case
`t = q^f`. Then

    B₊ + B₋ = -α·log(μ₊·t) - α·log(μ₋/t) = -α·log(μ₊·μ₋),

because the `log t` terms cancel identically. **The total is a framing
invariant**: it is the same for `f = 0`, `f = 3`, `f = 10`, or the `f = -8.297`
that would reproduce the deuteron alone.

## The floor

`InterfaceScalar.mu_sum_eq_one` gives `μ₊ + μ₋ = 1`, so AM–GM caps the product at
`μ₊·μ₋ ≤ 1/4`, with equality only at `μ₊ = μ₋ = 1/2`. Since `-log` is decreasing,

    B₊ + B₋ = -α·log(μ₊·μ₋) ≥ α·log 4.

This is a floor over **every** convex two-channel decomposition — not just the
substrate's. No choice of `z`, no convention, no interface offset, no crossing
assignment, and no T-odd rescaling can push the total below it.

## The measurement

At `α = E₀ = 4.185981 MeV`:

    floor           α·log 4              = 5.8030 MeV
    substrate       -α·log(μ₊μ₋)         = 7.0377 MeV   (μ₊μ₋ = 0.186142)
    nature          B(³S₁) + B(¹S₀)      = 2.2246 - 0.0736 = 2.1510 MeV

The substrate over-binds the two-nucleon total by **3.27×**, and the floor
over-binds it by **2.70× no matter what the projector scalars are**. Satisfying
the floor at all would need `α ≤ 2.1510/log 4 = 1.5516 MeV`, against the
framework's `4.1860 MeV`.

The `¹S₀` entry is the virtual-state energy `ℏ²/(m_N a²) = 41.47/23.74² = 0.0736
MeV`, entered with a negative sign because the channel is unbound. Note the floor
argument barely depends on it: even taking the `T = 1` binding to be exactly `0`,
nature's total is `2.2246 MeV` and the floor still over-binds by `2.61×`.

## What this proves, and in what scope

**Scope-(b) — a proved invariant excludes an ingredient.** No T-odd
rescaling of the two isospin channels — ribbon twist at any framing, or any other
`(μ₊, μ₋) ↦ (μ₊t, μ₋/t)` — can reproduce both two-nucleon channel energies,
because it cannot change their sum, and the sum is already wrong. The earlier
honesty flag on `f = 3` ("it is a fit") is superseded by something stronger:
**there is no `f` to find.**

**The sub-normalisation escape is closed too — in the opposite direction.** The
intuitive repair is "the two isospin channels carry only a fraction `s < 1` of
the trace, because the colour-only fibre lacks a spin or spatial factor, so the
floor drops." It does not. Under `μ₊ + μ₋ = s` the cap is `μ₊μ₋ ≤ s²/4`, which
*shrinks* with `s`, so a smaller normalisation binds *harder*. Reaching nature's
total forces `1 < s` (`reaching_target_forces_over_unit_sum`) — at the substrate
target, `s ≥ 1.547` — and a projector decomposition of a single normalised trace
cannot exceed `1`. So this route makes the discrepancy worse, not better.

**Scope-(a) — what is genuinely untouched.** The floor needs (i) a two-element
decomposition with `μ₊ + μ₋ ≤ 1` and (ii) one channel-independent `α`. It is
escaped only by breaking one of those:

* a channel-**dependent** `α`, or an `α` that is not `E₀`;
* a binding law that is not `-α·log μ`;
* **more than two** channels sharing the trace — with `k > 2` the cap is
  `∏ μ_i ≤ k^{-k}` and the floor is `α·k·log k`, which *rises* with `k`, so this
  too points the wrong way for a repair that keeps `α`;
* the two-nucleon states not being spectral projections of this trace at all.

The surviving direction is therefore `α`, not the interface: satisfying the floor
needs `α ≤ 2.1510/log 4 = 1.5516 MeV` against `E₀ = 4.1860 MeV`. That reframes
bean `qou-brg3`'s sibling question — the issue is not that the colour-only fibre
is too small to host `³S₁`/`¹S₀`, it is that the energy scale attached to the
interface is ~2.7× too large.

## Base ring (§7c)

`ℝ` throughout: the content is `Real.log` plus an ordering, i.e. archimedean.
The purely algebraic half (`μ₊ + μ₋ = 1`) already lives over a generic `R` in
`InterfaceScalar.mu_sum_eq_one` and is not restated here.

-- Ref: [manuscript] computations/probes/ribbon_twist_t_selective_probe.py
-- Ref: [manuscript] computations/probes/framing_derivation_attempt_probe.py
-- Ref: [machleidt2001] https://doi.org/10.1103/PhysRevC.63.024001
-/

namespace QOU.QBeta

open Real

/-- **The convex product is capped at `1/4`.** AM–GM in the form that matters
here: a pair summing to `1` has product at most `1/4`, with equality exactly at
the balanced point. -/
theorem convex_pair_prod_le_quarter {μp μm : ℝ} (hsum : μp + μm = 1) :
    μp * μm ≤ 1 / 4 := by
  nlinarith [sq_nonneg (μp - μm)]

/-- The same cap under a *sub*-unit normalisation `μ₊ + μ₋ ≤ 1`. Carrying less
than the whole trace makes the product smaller, not larger — which is the step
that decides the direction of the escape in `reaching_target_forces_over_unit_sum`
below. -/
theorem prod_le_quarter_of_sum_le_one {μp μm : ℝ}
    (hp : 0 < μp) (hm : 0 < μm) (hsum : μp + μm ≤ 1) :
    μp * μm ≤ 1 / 4 := by
  nlinarith [sq_nonneg (μp - μm)]

/-- **The floor, from the product cap alone.** Isolated so that both the
convex case and the sub-unit case share it. -/
theorem total_binding_floor_of_prod_le_quarter {α μp μm : ℝ}
    (hα : 0 < α) (hp : 0 < μp) (hm : 0 < μm) (hprod : μp * μm ≤ 1 / 4) :
    α * Real.log 4 ≤ (-α * Real.log μp) + (-α * Real.log μm) := by
  have hpm : 0 < μp * μm := mul_pos hp hm
  have key : Real.log μp + Real.log μm ≤ -Real.log 4 := by
    have hlog : Real.log (μp * μm) ≤ Real.log (1 / 4) := Real.log_le_log hpm hprod
    rwa [Real.log_mul (ne_of_gt hp) (ne_of_gt hm), one_div, Real.log_inv] at hlog
  nlinarith [mul_le_mul_of_nonneg_left key (le_of_lt hα)]

/-- **A T-odd rescaling cannot move the total.** Sending `(μ₊, μ₋) ↦ (μ₊·t,
μ₋/t)` leaves `B₊ + B₋` exactly where it was, because the two `log t`
contributions enter with opposite signs and cancel.

The ribbon twist is the case `t = q^f`, so this says the total binding is
**independent of the framing** — the quantity is blind to the one parameter the
twist route had to offer. -/
theorem t_odd_rescaling_preserves_total {α μp μm t : ℝ}
    (hp : μp ≠ 0) (hm : μm ≠ 0) (ht : t ≠ 0) :
    (-α * Real.log (μp * t)) + (-α * Real.log (μm / t))
      = (-α * Real.log μp) + (-α * Real.log μm) := by
  rw [Real.log_mul hp ht, Real.log_div hm ht]
  ring

/-- **The floor.** For any convex pair of channel scalars and any positive
energy scale, the total binding is at least `α·log 4`.

This is where `μ₊ + μ₋ = 1` (`InterfaceScalar.mu_sum_eq_one`) does the work: it
is not merely "both channels bind" (which follows from `μ_T < 1` alone) but a
*quantitative lower bound on their sum*, which is what makes the comparison with
nature decisive rather than qualitative. -/
theorem convex_total_binding_floor {α μp μm : ℝ}
    (hα : 0 < α) (hp : 0 < μp) (hm : 0 < μm) (hsum : μp + μm = 1) :
    α * Real.log 4 ≤ (-α * Real.log μp) + (-α * Real.log μm) :=
  total_binding_floor_of_prod_le_quarter hα hp hm (convex_pair_prod_le_quarter hsum)

/-- **No T-odd rescaling reaches a target below the floor.** Combining the two
previous results: the rescaling cannot change the total, and the total is floored,
so every target strictly below `α·log 4` is unreachable for **every** `t > 0`.

With `α = E₀` the floor is `5.8030 MeV` and nature's two-nucleon total is
`2.1510 MeV`, so this applies to the physical target. The ribbon-twist route is
closed without ever deciding what `f` is. -/
theorem no_t_odd_rescaling_reaches_target {α μp μm t target : ℝ}
    (hα : 0 < α) (hp : 0 < μp) (hm : 0 < μm) (hsum : μp + μm = 1)
    (ht : 0 < t) (hlt : target < α * Real.log 4) :
    target < (-α * Real.log (μp * t)) + (-α * Real.log (μm / t)) := by
  rw [t_odd_rescaling_preserves_total (ne_of_gt hp) (ne_of_gt hm) (ne_of_gt ht)]
  exact lt_of_lt_of_le hlt (convex_total_binding_floor hα hp hm hsum)

/-- **The obvious escape is closed, and closed in the opposite direction.**

The natural repair to reach for is "the two isospin channels carry only a
fraction `s < 1` of the trace normalisation — a spin or spatial factor the
colour-only fibre lacks — so the floor drops." **It does not drop; it rises.**

Under `μ₊ + μ₋ = s` the AM–GM cap is `μ₊μ₋ ≤ s²/4`, which *shrinks* with `s`, so
a smaller normalisation makes the product smaller and hence the total binding
*larger*. Reaching any target below `α·log 4` therefore forces `1 < s`: the two
channels would have to carry **more** weight than the whole trace.

For a spectral projector decomposition of a single normalised trace that is not
available (`s ≤ 1` by construction — `InterfaceScalar.mu_sum_eq_one` has `s = 1`
exactly). So this closes the sub-normalisation route rather than opening it: at
the substrate target the requirement is `s ≥ 1.547`.

Recorded because the wrong direction is the intuitive one, and an earlier
revision of the companion probe asserted it. -/
theorem reaching_target_forces_over_unit_sum {α μp μm s target : ℝ}
    (hα : 0 < α) (hp : 0 < μp) (hm : 0 < μm) (hs : μp + μm = s)
    (hlt : target < α * Real.log 4)
    (hreach : (-α * Real.log μp) + (-α * Real.log μm) ≤ target) :
    1 < s := by
  by_contra hcon
  push_neg at hcon
  have hsum : μp + μm ≤ 1 := by rw [hs]; exact hcon
  have := total_binding_floor_of_prod_le_quarter hα hp hm
    (prod_le_quarter_of_sum_le_one hp hm hsum)
  linarith

end QOU.QBeta
