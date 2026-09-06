import QOU.QuantumObservableUniverses.QAnalysisUniqueness
import QOU.QuantumObservableUniverses.QAnalysisUniquenessCounterexamples


/-!
# prop:q-logarithm-unique — witness extract

The formalisation lives in the library:

* `QOU.QLogarithm.unique_of_prim_rigid`
  (`QOU/QuantumObservableUniverses/QAnalysisUniqueness.lean`)

`QLogarithm` itself was relocated into
`QOU/QuantumObservableUniverses/QAnalysis.lean` on 2026-09-06; this file
previously inlined a copy of it.

## What changed 2026-09-06

This file previously held an unconditional

    axiom QLogarithm.unique_axiom … : ℓ₁.log_q = ℓ₂.log_q

**The axiom is false.**  `coprod := fun x => (x, x)` satisfies both
primitivity fields and a constant zero counit satisfies
`counit_eq_zero`, for *every* `log_q`.  Refutation:
`QOU.QAnalysisCounterexamples.not_qLogarithm_unique`.

The live statement is conditional on `prim_rigid` -- verbatim the step
the narrative proof `prf:q-logarithm-unique` asserts, *"a primitive
fixed by `D_q` with trivial counit vanishes"* -- and on the additivity
that proof silently uses when it forms `ℓ₁ - ℓ₂`.
-/

namespace QOU.QLogarithmUniqueWitness

open QOU QOU.QAnalysisCounterexamples

/-- The library statement, conditional on primitive rigidity. -/
example {H : Type*} [AddCommGroup H] (l₁ l₂ : QLogarithm H)
    (h_coprod : l₁.coprod = l₂.coprod) (h_counit : l₁.counit = l₂.counit)
    (hΔ_fst : ∀ x y : H, (l₁.coprod (x - y)).1 = (l₁.coprod x).1 - (l₁.coprod y).1)
    (hΔ_snd : ∀ x y : H, (l₁.coprod (x - y)).2 = (l₁.coprod x).2 - (l₁.coprod y).2)
    (hε_sub : ∀ x y : H, l₁.counit (x - y) = l₁.counit x - l₁.counit y)
    (prim_rigid : ∀ x : H, (l₁.coprod x).1 = x → (l₁.coprod x).2 = x →
                            l₁.counit x = 0 → x = 0) :
    l₁.log_q = l₂.log_q :=
  QLogarithm.unique_of_prim_rigid l₁ l₂ h_coprod h_counit hΔ_fst hΔ_snd hε_sub prim_rigid

/-- The unconditional form that stood here as an axiom is refuted. -/
example :
    ¬ (∀ {H : Type} (ℓ₁ ℓ₂ : QLogarithm H),
        ℓ₁.coprod = ℓ₂.coprod → ℓ₁.counit = ℓ₂.counit → ℓ₁.one = ℓ₂.one →
        ℓ₁.log_q = ℓ₂.log_q) :=
  not_qLogarithm_unique

end QOU.QLogarithmUniqueWitness
