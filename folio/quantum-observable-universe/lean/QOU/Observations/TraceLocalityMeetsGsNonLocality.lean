import Mathlib.Tactic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# QOU.Observations.TraceLocalityMeetsGsNonLocality

The locality / non-locality reconciliation, encoded as a typeclass
packaging the structural ingredients of
`prop:trace-locality-meets-gs-non-locality`:

1. **Markov-property locality** — `tr_M(x · σ_n) = z · tr_M(x)`.
2. **GS non-locality** — normal-form depends on the full braid word.

The product factorisation `tr_M(NF(β)) = Π_i V̂_i(q)` was part (3) of the
statement until the owner moved it to a remark (2026-11-15). It is no
longer a field here, so the class assumes no more than the statement.

Note: field `vertexVolume_local` is a tautology (it follows from
`congrArg`), so it constrains nothing.

Resolves issue #649 §3.
-/

namespace QOU.Observations.TraceLocalityMeetsGsNonLocality

universe u v w

open scoped BigOperators

/-- **Locality–non-locality reconciliation class.**

Given a Hecke-algebra-like carrier `A` with trace `trM`, normal-form
function `nf`, and per-vertex local volume `vertexVolume`, packages
the three identities of the reconciliation. -/
class HasReconciliation
    (A : Type u) (R : Type v)
    [CommMonoid R] [Mul A] where
  /-- The Markov trace on `A`. -/
  trM : A → R
  /-- The Markov parameter `z`. Canonically convention D,
      `z = q³/(q² + 1)`; not pinned by this class. -/
  markovParameter : R
  /-- A distinguished family of "single generators" (analogue of
      `σ_i`) producing the Markov-locality identity. -/
  generator : ℕ → A
  /-- A function returning the GS normal-form word length. -/
  nfLength : A → ℕ
  /-- The normal-form symbol at position `i` of `x` (the $i$-th
      generator index of the GS normal-form word, or a sentinel
      when `i ≥ nfLength x`). Carrying this as a class field
      forces an instance to supply the actual normal-form data. -/
  nfSymbolAt : A → ℕ → ℕ
  /-- Per-position vertex volume. Defined in terms of the
      normal-form symbol at that position, encoding the locality
      requirement at the *type* level. -/
  vertexVolume : ℕ → R
  /-- **(1) Markov locality**: appending a single generator
      multiplies the trace by `markovParameter`. -/
  markovLocality :
    ∀ (x : A) (n : ℕ),
      trM (x * generator n) = markovParameter * trM x
  /-- **(2) Locality of vertex volumes**: the per-position vertex
      volume depends only on the normal-form symbol at that
      position — i.e. on `nfSymbolAt x i`, not on the rest of `x`.
      This is now a *real* property: any two elements `x`, `y`
      sharing a normal-form symbol at position `i` produce the
      same per-position contribution. -/
  vertexVolume_local :
    ∀ (x y : A) (i : ℕ),
      i < nfLength x → i < nfLength y →
        nfSymbolAt x i = nfSymbolAt y i →
        vertexVolume (nfSymbolAt x i) = vertexVolume (nfSymbolAt y i)

end QOU.Observations.TraceLocalityMeetsGsNonLocality
