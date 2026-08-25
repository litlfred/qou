import QOU.BraidKnot.HabiroResidueSumEquivalence.archimedean_agreement

/-!
# QOU.BraidKnot.HabiroResidueSumEquivalence.protonExample.archimedean_agreement — conjecture carrier

**§3b-cond class axiomatisation** for content block
[`conj:gs-archimedean-agreement-residue`](../../../../mass-theory/gs-archimedean-agreement-residue.md):
*Archimedean agreement (proton instance): degree-48 Habiro trace at `u₀`*.

This is a **conjecture**: the class is a primary conjecture carrier with **no
instance** — the honest open state per AGENTS.md §3b-tax.

## What changed (bean `qou-ffwk`)

The previous field schema — a scalar `residual : ℝ` plus a field asserting it
vanishes — is inhabited by `⟨0, rfl⟩`: the class chose its own witness, so it asserted
nothing and a downstream `[archimedean_agreement]` hypothesis was not a
meaningful conditional. The two compared quantities are now class **parameters**,
so an instance must discharge the claim for the caller's data. Shape reviewed on
PR #3793 (closed unmerged 2026-08-03); this lands its class body.

## Faithfulness

The block states one identity, at one braid: the degree-48 Markov-normalised
Habiro trace of the proton, evaluated at `u₀`, against the proton
Gröbner–Shirshov mass, agreeing "to machine precision". So this carrier is
**not** quantified over braids — that is the generic sibling's job — and the
tolerance is explicit rather than hidden inside an equality.

The block's recorded value for the agreement is deliberately **not** written
into the class. A carrier that fixes a decimal asserts more than the conjecture
does and would have to be re-edited whenever the pin moves; the value belongs in
the block and its witness, and the instance that eventually discharges this
class is where it enters.

`specialises` below derives this carrier from the generic one, so the two are
ordered rather than independent: anyone establishing the generic conjecture gets
the proton case, and nobody has to assert it twice.

## Base ring (§7c)

`ℝ` is required for the same reason as the generic sibling: the claim is about
an archimedean evaluation compared against a mass, on the observable side of the
substrate wall by construction.
-/

namespace QOU.BraidKnot.HabiroResidueSumEquivalence.protonExample

/-- **Archimedean agreement (proton instance)**: the proton's degree-48
Markov-normalised Habiro trace, evaluated at `u₀`, agrees with the proton
Gröbner–Shirshov mass within `ε`.

Conjectural class — see
[`conj:gs-archimedean-agreement-residue`](../../../../mass-theory/gs-archimedean-agreement-residue.md).

Parameters are the caller's data: the two evaluated quantities and the certified
tolerance. An instance **is** the conjecture, for that data. None is provided. -/
class archimedean_agreement (habiroTraceEval gbMass ε : ℝ) : Prop where
  /-- The tolerance is a tolerance: a negative `ε` would make the class empty
      rather than open, which is a different and wrong claim. -/
  tolerance_nonneg : 0 ≤ ε
  /-- **The conjecture**, at the proton braid. -/
  agree : |habiroTraceEval - gbMass| ≤ ε

-- **No instance is provided — that is the honest open state** (AGENTS.md
-- §3b-tax).  History: this file previously carried
--     axiom conj_archimedean_agreement : archimedean_agreement
--     noncomputable instance : archimedean_agreement := conj_archimedean_agreement
-- so every downstream `[archimedean_agreement]` resolved for free and the
-- assumption was invisible outside `#print axioms`.  (The removed comment
-- called it a `sorry` representing the open conjecture; it was an `axiom`,
-- which is strictly stronger — a `sorry` at least surfaces as `sorryAx`.)
-- Removed, not completed.  The field schema is now content-bearing as well;
-- see the header.

/-- **The proton case follows from the generic conjecture.**

The block says the proton identity *"specializes the generic archimedean
agreement to the proton"*; this is that sentence, checked. It is a genuine
derivation rather than a restatement — the generic class is quantified over
braids and this one is not, so the two statements differ and one implies the
other. -/
theorem specialises {Braid : Type*} {habiroTraceEval gbMass : Braid → ℝ} {ε : ℝ}
    [h : QOU.BraidKnot.HabiroResidueSumEquivalence.archimedean_agreement
      Braid habiroTraceEval gbMass ε] (proton : Braid) :
    archimedean_agreement (habiroTraceEval proton) (gbMass proton) ε :=
  ⟨h.tolerance_nonneg, h.agree proton⟩

end QOU.BraidKnot.HabiroResidueSumEquivalence.protonExample
