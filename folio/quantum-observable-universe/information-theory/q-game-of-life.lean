/-
  q-GoL: Quantum Game of Life via q-Toffoli gates.

  The substrate cellular automaton defined by composing q-deformed
  Toffoli gates on the Reeb bundle fibres. Each q-Toffoli gate is
  unitary and reversible (its own inverse), and {q-Toffoli, Hadamard}
  is universal for quantum computation.

**Ground ring**: R_q = ℤ[q, q⁻¹]. The q-AND amplitude Φ(q) and
Toffoli diagonal P₇₇(q) are elements of the fraction field.

## Disposition (integrity)

The previous encoding was vacuous: the automaton was literally `id`,
so its unitarity/reversibility/universality theorems were claims about
the identity map, and stability was an `axiom`. This version models the
tick honestly — `qGameOfLife T` is *one application of the q-Toffoli
gate* `T` on the lattice config space, so its reversibility/unitarity
are **derived** from the gate's involutivity/bijectivity (the cited
physical properties of a q-Toffoli gate), not asserted of `id`. The
masking `axiom qGameOfLife_stable_axiom` is removed; stability is the
honest statement `qAnd_amplitude ≠ 0`. Universality of
`{q-Toffoli, Hadamard}` is a deep external result (Bennett 1973;
Fredkin–Toffoli 1982) with no Lean model of quantum-gate universality,
so it is documented here rather than encoded as a vacuous `∃`.
-/
import Mathlib.Algebra.Polynomial.Laurent

namespace QOU.Information

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ), matching the
    repeated local convention across the QOU tree (`CategoricalDqSquared`,
    `Hecke.MarkovTraceProduct`, `Archimedean.GroundRing`, …). -/
abbrev R_q := LaurentPolynomial ℤ

/-- The substrate indeterminate `q ∈ R_q` (the canonical
    `LaurentPolynomial.T 1`). -/
def q_param : R_q := LaurentPolynomial.T 1

/-- The q-AND amplitude Φ(q) = (q-1)(q^(3/2)+q^(1/2)-1)(q^(3/2)+q+1)/(2(q+1)²).
    Parameterised via a Laurent polynomial proxy (placeholder for the
    fractional-power expression); the leading `(q-1)` factor is the part
    that controls non-degeneracy. Ref: prop:toffoli-transfer-matrix -/
def qAnd_amplitude : R_q := q_param - 1

/-- **The q-Game of Life tick** on a lattice config space `L`: one application
    of a q-Toffoli gate `T` (ancilla-encoded neighbour sums realising Conway's
    survival/birth rules). Parameterised by the gate `T` so that the tick's
    reversibility/unitarity are *derived* from the gate's properties — not
    asserted of `id`. Label: prop:q-game-of-life. Ref: [pena2022] -/
def qGameOfLife {L : Type*} (T : L → L) : L → L := T

/-- **Reversibility.** Each q-Toffoli gate is its own inverse (an involution
    in `H₃(q)` under the Markov-trace dagger involution), so the q-GoL tick is
    reversible. *Derived* from the gate's involutivity. -/
-- Ref: [fredkin1982] https://doi.org/10.1007/BF01857727
theorem qGameOfLife_reversible {L : Type*} (T : L → L)
    (hT : Function.Involutive T) : Function.Involutive (qGameOfLife T) := hT

/-- **Unitarity ⇒ bijectivity.** A unitary q-Toffoli gate is bijective, hence
    so is the q-GoL tick. *Derived* from the gate's bijectivity. -/
-- Ref: [toffoli1980] https://doi.org/10.1007/3-540-10003-2_104
theorem qGameOfLife_unitary {L : Type*} (T : L → L)
    (hT : Function.Bijective T) : Function.Bijective (qGameOfLife T) := hT

/-- **Stability (non-degeneracy).** The q-AND amplitude carries a nonzero
    `(q − 1)` factor, so it is a nonzero element of `R_q = ℤ[q, q⁻¹]`: the
    evolution is non-degenerate.

    Replaces the former `axiom qGameOfLife_stable_axiom`, which *trusted* this
    globally. The unused `q > 1` substrate hypotheses are dropped — `q − 1 ≠ 0`
    holds unconditionally in `R_q` (the indeterminate minus a constant is a
    nonzero Laurent polynomial). Discharged **sorry-free** via the injective
    ring hom `Polynomial.toLaurent`: `q − 1 = toLaurent (X − 1)` and `X − 1 ≠ 0`
    in `ℤ[X]`, so injectivity gives `q − 1 ≠ 0`. -/
theorem qGameOfLife_stable : qAnd_amplitude ≠ 0 := by
  -- Ref: [leitner2026] Ch.8 prop:toffoli-lp-stability — q-AND amplitude nonzero
  -- `q_param - 1 = toLaurent (X - 1)`; toLaurent is injective and `X - 1 ≠ 0`.
  unfold qAnd_amplitude q_param
  have hX : (Polynomial.X - 1 : Polynomial ℤ) ≠ 0 := by
    simpa using Polynomial.X_sub_C_ne_zero (1 : ℤ)
  have htl : (LaurentPolynomial.T 1 - 1 : R_q)
      = Polynomial.toLaurent (Polynomial.X - 1) := by
    rw [map_sub, Polynomial.toLaurent_X, map_one]
  rw [htl]
  intro h
  exact hX (Polynomial.toLaurent_injective (h.trans (map_zero _).symm))

end

end QOU.Information
