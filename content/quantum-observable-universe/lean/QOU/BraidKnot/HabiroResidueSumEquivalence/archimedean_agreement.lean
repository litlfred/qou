import Mathlib.Tactic

/-!
# QOU.BraidKnot.HabiroResidueSumEquivalence.archimedean_agreement — conjectural class

**§3b-cond class axiomatisation** for content block
[`conj:gs-archimedean-agreement-trace`](../../../../mass-theory/gs-archimedean-agreement-trace.md):
*Archimedean agreement: Habiro polynomial trace evaluates to GB mass*.

This is a **primary conjecture** (§3b-tax) carrier with **no instance** — the
honest open state.  Downstream theorems may take
`[archimedean_agreement traceEval gbMass ε]` as an explicit `[Instance]`
hypothesis to derive unconditional Lean theorems modulo this single
conjectural input (per §3b-cond).

## Field schema — content-bearing (bean `qou-ffwk`)

The conjecture is the scalar agreement, for a closed braid `K` with Habiro
polynomial trace `T_K(u) ∈ ℤ[u]` and Gröbner–Shirshov mass
`𝔪_GB(K, q₀)`,

$$ T_K(\sqrt{q_0}) \;\approx\; \mathfrak{m}_{\mathrm{GB}}(K, q_0), $$

i.e. `|traceEval − gbMass| ≤ ε` at a tolerance `ε ≥ 0`.  The class is
parameterised by the three reals `(traceEval, gbMass, ε)` and asserts that
bound in the *shape of the claim* (the Round-11 pattern of
`QOU.AlgebraicSubstrate.ConditionalClasses`).  This is **falsifiable** — e.g.
`archimedean_agreement 0 1 0` is uninhabited (`|0 − 1| ≤ 0` is false) — so
the fields carry the conjecture's content and are *not* trivially inhabited
by a constant (the `residual = 0` placeholder they replace was).

§7c: `ℝ` is genuinely required — the claim is about the archimedean
evaluation `T_K(√q₀)` past the substrate→archimedean wall.
-/

namespace QOU.BraidKnot.HabiroResidueSumEquivalence

/-- **§3b-cond hypothesis class** for `conj:gs-archimedean-agreement-trace`.

    Archimedean agreement: for a closed braid `K`, the Habiro polynomial
    trace evaluated at `√q₀` (`traceEval`) agrees with the Gröbner–Shirshov
    mass `𝔪_GB(K, q₀)` (`gbMass`) to within a tolerance `ε ≥ 0`.

    Conjectural class — see
    [`conj:gs-archimedean-agreement-trace`](../../../../mass-theory/gs-archimedean-agreement-trace.md). -/
class archimedean_agreement (traceEval gbMass ε : ℝ) : Prop where
  /-- The tolerance is non-negative. -/
  tol_nonneg : 0 ≤ ε
  /-- The archimedean Habiro trace agrees with the GB mass within `ε`. -/
  agree : |traceEval - gbMass| ≤ ε

/-! ## The carrier is content-bearing (falsifiability)

These are the §3b-tax "the carrier must assert something" obligations, proved
rather than asserted.  They are theorems *about the class*, not instances of
it — the conjecture itself remains open (no instance below). -/

/-- **Exact agreement at zero tolerance.**  At `ε = 0` the class forces
    `traceEval = gbMass`.  So the fields are not inert bookkeeping: they pin
    the archimedean evaluation exactly in the sharp case. -/
theorem eq_of_tol_zero {traceEval gbMass : ℝ}
    [h : archimedean_agreement traceEval gbMass 0] : traceEval = gbMass := by
  have := h.agree
  rw [abs_nonpos_iff, sub_eq_zero] at this
  exact this

/-- **The carrier is falsifiable.**  `archimedean_agreement 0 1 0` is
    *uninhabited*: it would force `0 = 1`.  This is the property the replaced
    `residual : ℝ` / `residual = 0` schema lacked — that one was inhabited by
    `⟨0, rfl⟩` for every parameter choice, so it asserted nothing. -/
theorem not_agreement_zero_one_zero : ¬ archimedean_agreement 0 1 0 := by
  intro h
  have : (0 : ℝ) = 1 := @eq_of_tol_zero 0 1 h
  exact zero_ne_one this

/-- **Monotone in the tolerance.**  A tighter agreement implies a looser one;
    the family is a genuine nested hierarchy of claims, not a flat tag. -/
theorem mono_tol {traceEval gbMass ε ε' : ℝ} (hεε' : ε ≤ ε')
    [h : archimedean_agreement traceEval gbMass ε] :
    archimedean_agreement traceEval gbMass ε' :=
  ⟨le_trans h.tol_nonneg hεε', le_trans h.agree hεε'⟩

/-- **Symmetry in the two evaluated quantities.**  The claim is a genuine
    two-sided comparison. -/
theorem symm {traceEval gbMass ε : ℝ}
    [h : archimedean_agreement traceEval gbMass ε] :
    archimedean_agreement gbMass traceEval ε :=
  ⟨h.tol_nonneg, by rw [abs_sub_comm]; exact h.agree⟩

-- **No instance is provided — that is the honest open state** (AGENTS.md
-- §3b-tax).  History: this file previously carried
--     axiom conj_archimedean_agreement : archimedean_agreement
--     noncomputable instance : archimedean_agreement := conj_archimedean_agreement
-- so every downstream `[archimedean_agreement]` resolved for free and the
-- assumption was invisible outside `#print axioms`.  (The removed comment
-- called it a `sorry` representing the open conjecture; it was an `axiom`,
-- which is strictly stronger — a `sorry` at least surfaces as `sorryAx`.)
-- The axiom was removed (PR #3793); the field schema is now refined from the
-- trivially-inhabited `residual = 0` placeholder to the parameter-quantified
-- agreement bound above (bean `qou-ffwk`), so a downstream
-- `[archimedean_agreement traceEval gbMass ε]` hypothesis is now a meaningful
-- conditional.  A genuine instance still requires a derivation or a certified
-- archimedean evaluation, never `⟨0, rfl⟩`.
end QOU.BraidKnot.HabiroResidueSumEquivalence
