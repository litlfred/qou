import Mathlib.Algebra.Ring.Defs


/-!
# Pair commutation at the traced-volume level

The traced volumes `V̂_i ∈ ℤ[q^{±1/2}, z]` of a closed braid live
in a **commutative** Laurent polynomial ring, hence pairwise
commute. This is the algebraic content closing audit GAP 17a /
the "Pentagon → uv-commutation" subconjecture in
`rem:mass-endomorphism-jet-tower`.

Per AGENTS.md §3b, this is a `lemma` (provable, not conjectural).

-- Ref: [leitner2026] lem:vhat-pair-commutation-trace
-- Ref: [leitner2026] def:algebraic-quantum-volume
-- Ref: [leitner2026] prop:markov-pair-z2
-- Ref: [kassel1995] Ch. X (Hecke algebras and Markov trace)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
-/

namespace QOU.BraidKnot

/-- The pair commutation lemma at traced-volume level.

    For any commutative ring `R` (instantiated in the QOU narrative
    as `ℤ[q^{±1/2}, z]`) and any two elements `V_i, V_j : R`, the
    product is symmetric: `V_i * V_j = V_j * V_i`.

    This is the algebraic core of the lemma. The Markov-trace
    consequence `tr_M (V_i V_j) = tr_M (V_j V_i) = z²` follows by
    `R`-linearity of `tr_M` and the pair Markov-trace identity
    `prop:markov-pair-z2`; we do not formalise the trace here
    because the underlying Hecke-algebra layer is in
    `QOU.BraidKnot.MarkovTrace` and is orthogonal to the lemma's
    content. -/
-- Ref: [leitner2026] lem:vhat-pair-commutation-trace
theorem VhatPairCommutationTrace
    {R : Type*} [CommRing R] (V_i V_j : R) :
    V_i * V_j = V_j * V_i :=
  mul_comm V_i V_j

/-- The trace consequence, stated parametrically.  Given any
    `R`-linear trace `tr` and any two elements that commute (which
    they always do in a commutative ring), the trace is symmetric
    under swap. -/
-- Ref: [leitner2026] lem:vhat-pair-commutation-trace §"Statement"
theorem trace_symmetric
    {R : Type*} [CommRing R] (tr : R → R) (V_i V_j : R) :
    tr (V_i * V_j) = tr (V_j * V_i) := by
  rw [VhatPairCommutationTrace V_i V_j]

end QOU.BraidKnot
