import QOU.QuantumObservableUniverse.CategoricalFoundations
import QOU.QuantumObservableUniverse.TrivialWitness


/-!
# QOU.QuantumUniverse.exists_instance — existence of a quantum universe

Trivial witness: R-Mod with A = R.  Richer witness: Rep(SU_q(2)).

LaTeX: `\label{prop:quantum-universe-exists}`

## References

- [manuscript] §1-quantum-universes/quantum-universe-exists
- [kassel1995] Quantum Groups (Springer GTM 155), §XI
-/

namespace QOU

universe w

/-- **Existence of a quantum universe over a commutative ring `R`.**

    **This was an `axiom` until 2026-08-16.**  The axiom's own docstring named
    the witness — *"a concrete witness (R-Mod or Rep(SU_q(2))) requires
    category/monoidal-category instances not yet provided"* — and that turned
    out to be false: the instances are provided.  `ModuleCat R` with `A = 𝟙`
    discharges every field, so the claim is now a theorem and the axiom is
    retired.

    Built in
    [`QOU/QuantumObservableUniverse/TrivialWitness.lean`](../lean/QOU/QuantumObservableUniverse/TrivialWitness.lean);
    `#print axioms` reports only `propext`, `Classical.choice`, `Quot.sound`.

    Note the hypothesis weakened from `[Field k]` to `[CommRing R]` — the
    witness never needed a field, matching `def:quantum-universe`, which asks
    for an `R`-linear category over a commutative ring.

    This does **not** extend to `QuantumObservableUniverse`: at `A = 𝟙` the
    augmentation ideal vanishes, so `adjoint_nontrivial` fails.  QOU existence
    still rests on its own cited `sorry`. -/
-- Ref: [manuscript] §1-quantum-universes/quantum-universe-exists
theorem QuantumUniverse.exists_instance (R : Type w) [CommRing R] :
    Nonempty (QuantumUniverse.{w + 1, w, w, w, w} R) :=
  QOU.TrivialWitness.nonempty_quantumUniverse R

end QOU
