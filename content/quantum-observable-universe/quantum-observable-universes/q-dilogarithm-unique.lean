import QOU.QuantumObservableUniverses.QAnalysisUniqueness
import QOU.QuantumObservableUniverses.QAnalysisUniquenessCounterexamples


/-!
# prop:q-dilogarithm-unique — witness extract

The formalisation lives in the library:

* `QOU.QDilogarithm.eval_unique_of_pentagon_rigid`
  (`QOU/QuantumObservableUniverses/QAnalysisUniqueness.lean`)

This file carries no declaration of its own -- per AGENTS.md §0a a
sibling that re-declares a library result shadows it -- only `example`
extracts pinning what the library proves.

## What changed 2026-09-06

This file previously held

    axiom QDilogarithm.unique_axiom … : L₁.Li2.1 = L₂.Li2.1

together with a wrapper theorem `QDilogarithm.unique` consuming it.
**The axiom is false.**  `Li2` is not mentioned by the `pentagon` field
-- the pentagon constrains `Li2_eval`, a different field -- so `Li2` is
free data, and two records agreeing on `log_q`, `mul`, `compl` and `div`
can differ in it.  Refutation:
`QOU.QAnalysisCounterexamples.not_qDilogarithm_unique`.

The live statement therefore concludes about `Li2_eval`, the field the
pentagon actually constrains, and is conditional on `pentagon_rigid` --
the one-dimensionality step the narrative proof `prf:q-dilogarithm-unique`
already asserts in prose.
-/

namespace QOU.QDilogarithmUniqueWitness

open QOU QOU.QAnalysisCounterexamples

/-- The library statement is conditional on pentagon rigidity and
    concludes about `Li2_eval`. -/
example {H : Type*} [AddCommGroup H] (L₁ L₂ : QDilogarithm H)
    (h_mul : L₁.mul = L₂.mul) (h_compl : L₁.compl = L₂.compl)
    (h_div : L₁.div = L₂.div)
    (pentagon_rigid : ∀ f : H → H,
      (∀ x y : H, f y + f x =
        f (L₁.mul x y) +
        f (L₁.div (L₁.mul x (L₁.compl y)) (L₁.compl (L₁.mul x y))) +
        f (L₁.div (L₁.mul y (L₁.compl x)) (L₁.compl (L₁.mul x y)))) →
      f = 0) :
    L₁.Li2_eval = L₂.Li2_eval :=
  QDilogarithm.eval_unique_of_pentagon_rigid L₁ L₂ h_mul h_compl h_div pentagon_rigid

/-- The unconditional `Li2`-valued form that stood here as an axiom is
    refuted in the library. -/
example :
    ¬ (∀ {H : Type} [Add H] (L₁ L₂ : QDilogarithm H),
        L₁.log_q = L₂.log_q → L₁.mul = L₂.mul → L₁.compl = L₂.compl →
        L₁.div = L₂.div → L₁.Li2.1 = L₂.Li2.1) :=
  not_qDilogarithm_unique

end QOU.QDilogarithmUniqueWitness
