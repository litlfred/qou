import HeckeTemperleyLieb.KnotFactor

/-!
# QOU.BraidKnot.KnotFactorFrobeniusPairing

The **braid-level** carrier of `conj:knot-factor-frobenius-pairing`: the Markov
trace factors through the Frobenius pairing with a canonical knot factor,

  `tr_M(x) = τ(x · κ)`.

## Retyped 2026-11-22 (owner card "3: Both, inside reconcile work")

The class used to carry the knot factor as a braid word (`ClosedBraid n`, a
`List ℤ`) and both traces as unconstrained functions on words, with no instance.
In that form the factorisation could not be proved or refuted: nothing tied the
two functions to an algebra.  The knot factor is now an element of the algebra,
the traces are linear and cyclic, and the knot factor is central.

In this form the statement is **inhabited for every trace on `H_n(q)`**, every
`q ≠ 0` and every splitting (`ofHecke`), by `QOU.Hecke.KnotFactor`: the knot
factor is `κ = Σ_λ y_λ s_λ e_λ`, with `y_λ` the trace's block weights and `s_λ`
the abstract Schur elements, and it is unique.

What stays open on this half: the Markov (Ocneanu) trace is not yet a linear
functional on `QOU.Hecke.IwahoriHecke K q n`, so `ofHecke` is applied to it only
once that definition exists.  The binding half (`binding = E₀ · trace defect`)
is re-scoped in `QOU.Conjectures.KnotFactorFrobeniusPairing`.

LaTeX label: `conj:knot-factor-frobenius-pairing`

## References

- [geckpfeiffer2000] §7.2, §8.1 (symmetrizing trace, Schur elements)
- [jones1985] https://www.jstor.org/stable/2007074
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/

namespace QOU.BraidKnot

open QOU.MathlibExt QOU.Hecke.KnotFactor

/-- **Knot-factor Frobenius pairing on a `K`-algebra `A`.**  A cyclic linear
    trace `markovTrace`, a pairing trace `pairingTrace`, and a central element
    `knotFactor` with `markovTrace x = pairingTrace (x · knotFactor)`. -/
class KnotFactorFrobeniusPairing (K : Type*) [Field K] (A : Type*) [Ring A]
    [Algebra K A] where
  /-- The Markov trace, as a linear functional. -/
  markovTrace : A →ₗ[K] K
  /-- It is a trace. -/
  markovTrace_comm : ∀ x y : A, markovTrace (x * y) = markovTrace (y * x)
  /-- The trace defining the Frobenius pairing `⟨x, y⟩ = pairingTrace (x y)`. -/
  pairingTrace : A →ₗ[K] K
  /-- The knot factor, an element of the algebra. -/
  knotFactor : A
  /-- The knot factor is central. -/
  knotFactor_central : ∀ x : A, knotFactor * x = x * knotFactor
  /-- **The factorisation.**  The Markov trace is the Frobenius pairing with the
      knot factor. -/
  factorisation_holds : ∀ x : A, markovTrace x = pairingTrace (x * knotFactor)

/-- The factorisation, read off an instance. -/
theorem markov_trace_factors {K : Type*} [Field K] {A : Type*} [Ring A] [Algebra K A]
    [inst : KnotFactorFrobeniusPairing K A] (x : A) :
    inst.markovTrace x = inst.pairingTrace (x * inst.knotFactor) :=
  inst.factorisation_holds x

/-- **The factorisation holds in `H_n(q)`** for every trace `t`, every `q ≠ 0`
    and every splitting, with the pairing given by the symmetrizing trace `τ`.
    A `def`, not a global instance: the trace `t` is data the caller supplies. -/
noncomputable def ofHecke {K : Type*} [Field K] {q : K} {n : ℕ}
    {ι : Type*} [Fintype ι] [DecidableEq ι]
    {J : ι → Type*} [∀ i, Fintype (J i)] [∀ i, DecidableEq (J i)]
    (hq : q ≠ 0)
    (E : QOU.Hecke.IwahoriHecke K q n ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (a : ∀ i, J i) (t : QOU.Hecke.IwahoriHecke K q n →ₗ[K] K)
    (ht : ∀ x y, t (x * y) = t (y * x)) :
    KnotFactorFrobeniusPairing K (QOU.Hecke.IwahoriHecke K q n) where
  markovTrace := t
  markovTrace_comm := ht
  pairingTrace := QOU.Hecke.TwBasis.tau K q n
  knotFactor := knotFactor E t (QOU.Hecke.TwBasis.tau K q n) a
  knotFactor_central := knotFactor_comm E t _ a
  factorisation_holds := hecke_trace_eq_tau_mul_knotFactor hq E a t ht

end QOU.BraidKnot
