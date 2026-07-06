import QOU.QuantumObservableUniverse.CategoricalFoundations


/-!
# QOU.QuantumUniverse.exists_instance — existence of a quantum universe

Trivial witness: R-Mod with A = R.  Richer witness: Rep(SU_q(2)).

LaTeX: `\label{prop:quantum-universe-exists}`

## References

- [manuscript] §1-quantum-universes/quantum-universe-exists
- [kassel1995] Quantum Groups (Springer GTM 155), §XI
-/

namespace QOU

/-- **External axiom (§3b-cond pattern): QuantumUniverse.exists_instance.**

    Encodes the categorical content pending Mathlib infrastructure
    or a structure-tightening refactor: a concrete witness (R-Mod or
    Rep(SU_q(2))) requires category/monoidal-category instances not yet
    provided. Ref: [kassel1995] Quantum Groups, §XI. -/
-- Ref: [kassel1995] Quantum Groups, §XI
axiom QuantumUniverse.exists_instance_axiom (k : Type*) [Field k] :
    Nonempty (QuantumUniverse k)

/-- **Existence of a quantum universe over a base field `k`.**

    Records the claim that a `QuantumUniverse k` term exists for every
    field `k`, discharged via the external axiom above. -/
-- Ref: [kassel1995] Quantum Groups, §XI
theorem QuantumUniverse.exists_instance (k : Type*) [Field k] :
    Nonempty (QuantumUniverse k) :=
  QuantumUniverse.exists_instance_axiom k

end QOU
