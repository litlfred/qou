---
# qou-4670
title: CriticalExponent carrier boxed alpha=4/3, a value p2-critical-exponent.md calls OPEN
status: in-progress
type: task
priority: high
created_at: 2026-08-30T09:27:07Z
updated_at: 2026-08-30T09:28:00Z
---

## The defect

`QOU.AlgebraicSubstrate.CriticalExponent` was re-encoded on 2026-08-30 under
`qou-93hu`, replacing a vacuous numeral identity `(3*4 : ℕ) = 12` with

    class CriticalExponent (α : ℝ) : Prop where
      alpha_eq : α = 4 / 3

That fixed the vacuity and introduced a worse defect in the same edit: **4/3
is not a result the corpus holds.**

`content/quantum-observable-universe/fluid-dynamics/p2-critical-exponent.md`
gives the exponent under a heading that says so — *"Result (closure-dependent
— two heuristic values, neither rigorous)"* — and offers TWO:

  - α = 1     under the dissipation closure  ε = ν_q·Ω
  - α = 4/3   under the Kolmogorov cascade closure, *up to logs*

and then, verbatim: *"Neither closure is rigorous; the true α is fixed by the
actual q-Navier–Stokes enstrophy spectrum (the turbulence-closure problem) and
is open. The two values bracket it under their respective hypotheses."*

So the field asserted as settled a value its own source calls open, and picked
the larger of two bracketing candidates. Under its own closure it carries a
logarithmic correction, so it is not even a clean power law.

## The corpus had already decided against this

- Bean `qou-15gb` (**completed** 2026-07-18) is exactly this reconciliation:
  *"tier the two values ... state each conditional on named closure"*.
- `regularity-breakdown.ts` authorNotes: the exponent *"is now presented as
  closure-dependent, not a single boxed value"*.
- The established encoding names its closure:
  `QOU.FluidDynamics.enstrophy_alpha_one_of_dissipation_closure`
  (`lean/QOU/FluidDynamics/q_ns_classical_bridge.lean:135`).
- The UPSTREAM carrier `QOU.FluidDynamics.CriticalExponent`
  (`fluid-dynamics/p2-critical-exponent.lean`) deliberately leaves the
  exponent unconstrained and says so in its own docstring: *"the divergence
  rate is not encoded, and `criticalExponent` is accordingly unconstrained by
  any field of this class."*

A closure-free `α = 4/3` re-boxed the value one namespace over, six weeks
after it was un-boxed.

## Why the arc's own gate did not catch it

`docs/audits/2026-08-30-qns-carriers-are-refutable.lean` tests REFUTABILITY,
and `α = 4/3` passes it cleanly — `CriticalExponent 2` is false. Refutability
rules out the *vacuous* carrier; it does not rule out the *fabricated* one.
The second question is separate and is a corpus-grep, not a Lean check: **is
the proposition this field states one the corpus actually asserts?** I ran the
grep for the vacuity and not for the number.

## The fix (landed)

    class CriticalExponent (enstrophy : ℝ → ℝ) (α : ℝ) : Prop where
      alpha_pos : 0 < α
      enstrophy_diverges :
        ∀ M : ℝ, ∀ ε : ℝ, 0 < ε →
          ∃ q : ℝ, 1 < q ∧ q - 1 < ε ∧ M < enstrophy q

Both fields transcribed from the upstream carrier; nothing invented. This is
what the .md asserts unhedged (*"diverges as Ω_max(q) ~ (q-1)^{-α} for some
α > 0"*). The value of α is left open, which is its actual state.

Consumers updated in `ConditionalCorollaries.lean`:
`critical_exponent_identity` (concluded `3α = 4`) is replaced by
`critical_exponent_enstrophy_unbounded`; the `α = 4/3` conjunct of
`qNS_cone_full_composition` is replaced by the divergence consequence.
`SurrealRateCalculus.lean` no longer binds the class at all (a sibling dropped
the decorative binders on main).

## Verification

lean-direct, restored oleans, no `lake build`:

  ConditionalClasses.lean            EXIT 0
  ConditionalCorollaries.lean        EXIT 0
  SurrealRateCalculus.lean           EXIT 0 (2 pre-existing deprecation warnings)
  2026-08-30-qns-carriers-are-refutable.lean  EXIT 0

Zero `sorry` in all four. The gate file now carries two refutations for this
carrier (one per field) and a real satisfiability witness — `enstrophy q =
(q-1)⁻¹` at α = 1, which needs the ε-argument rather than being a one-liner.

## Still open, and NOT closed by this

The asymptotic `Ω_max(q) ~ (q-1)^{-α}` relating the two parameters is still
absent, here and upstream. Encoding it needs the asymptotic; pinning α needs a
closure that is not rigorous. That is the honest open state.
