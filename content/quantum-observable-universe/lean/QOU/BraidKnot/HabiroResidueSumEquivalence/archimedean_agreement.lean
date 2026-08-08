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
