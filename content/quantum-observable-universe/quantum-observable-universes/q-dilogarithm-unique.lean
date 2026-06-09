import QOU.Basic
import QOU.QuantumObservableUniverses.QAnalysis


/-!
# QOU.QDilogarithm.unique — uniqueness of the q-dilogarithm up to shift

The level-2 primitive satisfying the pentagon identity is unique up to
a level-1 shift.

LaTeX: `\label{prop:q-dilogarithm-unique}`

## Honest statement (2026-06-09 axiom audit)

The previous version recorded an external axiom referencing an
auto-bound `QDilogarithm` — never imported, hence unchecked, and the
noted `Subsingleton` reading would have been too strong (uniqueness
holds only *up to a level-1 shift*).

This file now imports the relocated `QDilogarithm` structure
(`QOU.QuantumObservableUniverses.QAnalysis`) and states the genuine
content as a single **honest §3b-cond conditional axiom**: two
pentagon-satisfying level-2 primitives with the same level-1 data
(`log_q`, `mul`, `compl`, `div`) have equal `Li2` first component.
This is the universal property of the q-dilogarithm as the generator
of the centre of `H_q^{⊗2}` modulo shuffle-products ([kassel1995]);
it is retained as a named axiom pending a Mathlib formalisation of the
pentagon universal property — not a false `Subsingleton`.

## References

- [manuscript] §2-quantum-observable-universes/q-dilogarithm-unique
- [kassel1995] Quantum Groups (Springer GTM 155), §IV
-/

namespace QOU

/-- **Pentagon-normalised uniqueness of the q-dilogarithm (conditional,
    named categorical input).**

    Two `QDilogarithm H` with the same level-1 data agree on the
    first component of `Li2`.  The §3b-cond conditional content
    (pentagon universal property, [kassel1995]); replaces an unchecked
    external axiom on an auto-bound carrier. -/
-- Ref: [kassel1995] Quantum Groups, §IV
axiom QDilogarithm.unique_axiom {H : Type*} [Add H] (L₁ L₂ : QDilogarithm H)
    (h_log : L₁.log_q = L₂.log_q)
    (h_mul : L₁.mul = L₂.mul)
    (h_compl : L₁.compl = L₂.compl)
    (h_div : L₁.div = L₂.div) :
    L₁.Li2.1 = L₂.Li2.1

/-- **Uniqueness of the q-dilogarithm up to shift (conditional).**
    Wrapper over `unique_axiom`. -/
-- Ref: [kassel1995] Quantum Groups, §IV
theorem QDilogarithm.unique {H : Type*} [Add H] (L₁ L₂ : QDilogarithm H)
    (h_log : L₁.log_q = L₂.log_q)
    (h_mul : L₁.mul = L₂.mul)
    (h_compl : L₁.compl = L₂.compl)
    (h_div : L₁.div = L₂.div) :
    L₁.Li2.1 = L₂.Li2.1 :=
  QDilogarithm.unique_axiom L₁ L₂ h_log h_mul h_compl h_div

end QOU
