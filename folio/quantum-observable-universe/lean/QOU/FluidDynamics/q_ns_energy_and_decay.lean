import Mathlib.Analysis.ODE.Gronwall

/-!
# QOU.FluidDynamics.q_ns_energy_and_decay

Infrastructure for [`thm:q-ns-wellposedness`]: the two *derivable* halves
of the block's claim.

## Why this file exists

`q_ns_wellposedness.lean` carried the block's whole conclusion —
existence, uniqueness, smoothness, the energy inequality and the
spectral-decay bound — as a single class field, and projected it.  That
is the self-assuming shape AGENTS.md §3b-cond item 5 forbids, and it is
also *imprecise about what is actually open*: it puts the energy
inequality and the spectral decay, which are consequences of the
equations, on the same footing as global existence, which is not.

Two of the three properties do **not** need any q-NS-specific
infrastructure.  Given the evolution's own differential inequalities,
they are Grönwall comparisons and are proved here, unconditionally:

| block property | status here |
|---|---|
| (i) existence + uniqueness | **open** — stays a hypothesis (Millennium-adjacent) |
| (ii) energy inequality | **derived** — `energy_inequality_of_balance` |
| (iii) `Δ_q`-spectral decay | **derived** — `modal_decay_of_deriv_le` |

Both are stated for a generic scalar trajectory, so they carry no q-NS
commitments of their own and cannot smuggle the conclusion back in: they
say *if the flow satisfies the pointwise balance / modal inequality, then
the integrated bound holds*, which is the honest content.

## References

- [leitner2026] quantum-observable-universe/fluid-dynamics/q-ns-wellposedness.md
  (`thm:q-ns-wellposedness`), properties (ii) and (iii)
-/

namespace QOU.FluidDynamics

open Set

/-- **Modal exponential decay from the modal differential inequality.**

    If a real trajectory `a` satisfies `a' t ≤ -c · a t` on `[0, T)`,
    then `a t ≤ a 0 · exp (-c t)` on `[0, T]`.

    Applied to the `Δ_q`-eigencomponent `a = |v̂_k|` with
    `c = ν_q [k]_q²`, this is property (iii) of
    [`thm:q-ns-wellposedness`].  The eigenvalue enters only as the
    constant `c`; nothing here knows about `q`, which is the point —
    the decay is a consequence of the modal inequality, not an extra
    assumption about solutions. -/
theorem modal_decay_of_deriv_le
    {a a' : ℝ → ℝ} {c T : ℝ}
    (hcont : ContinuousOn a (Icc 0 T))
    (hderiv : ∀ t ∈ Ico 0 T, HasDerivWithinAt a (a' t) (Ici t) t)
    (hineq : ∀ t ∈ Ico 0 T, a' t ≤ -c * a t) :
    ∀ t ∈ Icc 0 T, a t ≤ a 0 * Real.exp (-c * t) := by
  intro t ht
  have key :=
    le_gronwallBound_of_liminf_deriv_right_le (f := a) (f' := a')
      (δ := a 0) (K := -c) (ε := 0)
      hcont
      (fun x hx r hr => (hderiv x hx).liminf_right_slope_le hr)
      le_rfl
      (fun x hx => by simpa using hineq x hx)
      t ht
  simpa [gronwallBound_ε0, sub_zero] using key

/-- **Energy inequality from the pointwise energy balance.**

    Let `E` be the squared norm `‖v(t)‖²_A` and `Dcum` the cumulative
    dissipation `t ↦ ∫₀ᵗ ‖d_q v(s)‖²_A ds`.  If the balance
    `E' t + 2 ν_q · D t ≤ 0` holds pointwise — the differential form of
    the energy identity — then the *integrated* inequality

    `E t + 2 ν_q · Dcum t ≤ E 0`

    holds on `[0, T]`.  This is property (ii) of
    [`thm:q-ns-wellposedness`].

    Note what is and is not assumed: the hypothesis is the pointwise
    balance (a statement about the equations), and the conclusion is the
    integrated bound (the statement the block makes).  Assuming the
    latter directly, as the previous encoding did, assumes the theorem. -/
theorem energy_inequality_of_balance
    {E Dcum E' D : ℝ → ℝ} {ν T : ℝ}
    (hcont : ContinuousOn (fun t => E t + 2 * ν * Dcum t) (Icc 0 T))
    (hderiv : ∀ t ∈ Ico 0 T,
      HasDerivWithinAt (fun s => E s + 2 * ν * Dcum s) (E' t + 2 * ν * D t) (Ici t) t)
    (hbal : ∀ t ∈ Ico 0 T, E' t + 2 * ν * D t ≤ 0)
    (hD0 : Dcum 0 = 0) :
    ∀ t ∈ Icc 0 T, E t + 2 * ν * Dcum t ≤ E 0 := by
  intro t ht
  have key :=
    le_gronwallBound_of_liminf_deriv_right_le
      (f := fun s => E s + 2 * ν * Dcum s)
      (f' := fun s => E' s + 2 * ν * D s)
      (δ := E 0) (K := 0) (ε := 0)
      hcont
      (fun x hx r hr => (hderiv x hx).liminf_right_slope_le hr)
      (by simp [hD0])
      (fun x hx => by simpa using hbal x hx)
      t ht
  simpa [gronwallBound_ε0, sub_zero] using key

end QOU.FluidDynamics
