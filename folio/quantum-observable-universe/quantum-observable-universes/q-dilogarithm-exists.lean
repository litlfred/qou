import QOU.QuantumObservableUniverses.QAnalysisUniquenessCounterexamples


/-!
# QOU.QDilogarithm.exists — existence of the q-dilogarithm

LaTeX: `\label{prop:q-dilogarithm-exists}`

## What changed 2026-09-06

This file previously held

    axiom QDilogarithm.exists_axiom :
        ∀ (H : Type*) [Add H], Nonempty (QDilogarithm H)

**The axiom is false.**  It quantified over *every* carrier with an
`Add`, including `Empty`, where the `log_q : H` field cannot be
supplied.  Refutation:
`QOU.QAnalysisCounterexamples.not_qDilogarithm_exists_over_every_add_carrier`.

Unlike the five uniqueness axioms deleted the same day, this one was
repairable in substance rather than wrong in substance: over an
`AddZeroClass` the type genuinely is inhabited, and
`QOU.QAnalysisCounterexamples.QDilogarithm.nonempty_of_addZeroClass`
proves it **with no axiom**.

## The claim this establishes is weaker than the prose

Being explicit, because the axiom's disappearance should not read as a
promotion: the witness is the all-zero record, so what is proved is that
the *structure is inhabited*, not that the shuffle-recursion
construction of `Li₂^q` exists.  The pentagon identity is satisfied
because `Li2_eval` is constantly zero, which is a solution of the
five-term relation and not the intended one.

The same caveat applies to the sibling existence results
`QExponential.exists_in_shuffle_hopf` and
`QLogarithm.exists_in_shuffle_hopf`, whose own comments say the witness
is trivial and the intended Kassel construction is sharper.  Those
records are, field for field, the counterexamples that refute the
corresponding uniqueness axioms.

## References

- [leitner2026] §2-quantum-observable-universes/q-dilogarithm-exists
- [kassel1995] Quantum Groups, §IV (iterated primitives)
-/

namespace QOU

open QOU.QAnalysisCounterexamples

/-- **Existence of the q-dilogarithm structure over an `AddZeroClass`.**

    Inhabitation of `QDilogarithm H`, with no axiom.  See the module
    docstring: this is strictly weaker than the shuffle-recursion
    construction the proposition's prose describes, and the `Add`-only
    form it replaces is false. -/
-- Ref: [kassel1995] Quantum Groups (Springer GTM 155), §IV
theorem QDilogarithm.exists_of_addZeroClass (H : Type*) [AddZeroClass H] :
    Nonempty (QDilogarithm H) :=
  QDilogarithm.nonempty_of_addZeroClass H

end QOU
