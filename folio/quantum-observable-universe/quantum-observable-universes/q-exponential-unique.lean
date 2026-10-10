import QOU.QuantumObservableUniverses.QAnalysisUniqueness
import QOU.QuantumObservableUniverses.QAnalysisUniquenessCounterexamples


/-!
# prop:q-exponential-unique — witness extract

The formalisation lives in the library:

* `QOU.QExponential.unique_of_flow_rigid`
  (`QOU/QuantumObservableUniverses/QAnalysisUniqueness.lean`)

`QExponential` itself was relocated into
`QOU/QuantumObservableUniverses/QAnalysis.lean` on 2026-09-06; this file
previously inlined a fourth copy of it.

## What changed 2026-09-06

This file previously held an unconditional

    axiom QExponential.unique_axiom … : e₁.e_q = e₂.e_q

**The axiom is false.**  `coprod := fun x => (x, x)`, a constant counit
and `D_q := id` satisfy `grouplike`, `counit_eq_one` and
`flow_invariant` for *every* `e_q`, so two records agree on all three
hypothesised fields and differ in the concluded one.  Refutation:
`QOU.QAnalysisCounterexamples.not_qExponential_unique`.

The live statement is conditional on `flow_rigid` -- verbatim the step
the narrative proof `prf:q-exponential-unique` asserts, *"the flow
equation on primitives has only the trivial solution"* -- and on the
additivity that proof silently uses when it forms `e₁ - e₂`.
-/

namespace QOU.QExponentialUniqueWitness

open QOU QOU.QAnalysisCounterexamples

/-- The library statement, conditional on flow rigidity. -/
example {H : Type*} [AddCommGroup H] (e₁ e₂ : QExponential H)
    (h_counit : e₁.counit = e₂.counit) (h_Dq : e₁.D_q = e₂.D_q)
    (hD_sub : ∀ x y : H, e₁.D_q (x - y) = e₁.D_q x - e₁.D_q y)
    (hε_sub : ∀ x y : H, e₁.counit (x - y) = e₁.counit x - e₁.counit y)
    (flow_rigid : ∀ x : H, e₁.D_q x = x → e₁.counit x = 0 → x = 0) :
    e₁.e_q = e₂.e_q :=
  QExponential.unique_of_flow_rigid e₁ e₂ h_counit h_Dq hD_sub hε_sub flow_rigid

/-- The unconditional form that stood here as an axiom is refuted. -/
example :
    ¬ (∀ {H : Type} (e₁ e₂ : QExponential H),
        e₁.coprod = e₂.coprod → e₁.counit = e₂.counit → e₁.D_q = e₂.D_q →
        e₁.e_q = e₂.e_q) :=
  not_qExponential_unique

end QOU.QExponentialUniqueWitness
