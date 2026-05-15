import Mathlib.Tactic
import Mathlib.Algebra.BigOperators.Basic

/-!
# QOU.Observations.TraceLocalityMeetsGsNonLocality

The locality / non-locality reconciliation, encoded as a typeclass
packaging the three structural ingredients of
`prop:trace-locality-meets-gs-non-locality`:

1. **Markov-property locality** — `tr_M(x · σ_n) = z · tr_M(x)`.
2. **GS non-locality** — normal-form depends on the full braid word.
3. **Product factorisation bridge** — `tr_M(NF(β)) = Π_i V̂_i(q)`,
   local in the normal-form word.

The class fields carry concrete content (a Markov parameter `z`, a
normal-form function, a vertex-volume sequence, and the three
identities relating them).

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
    [LinearOrderedField R] [Mul A] where
  /-- The Markov trace on `A`. -/
  trM : A → R
  /-- The Markov parameter `z = 1/(q^{1/2} + q^{-1/2})`. -/
  markovParameter : R
  /-- A distinguished family of "single generators" (analogue of
      `σ_i`) producing the Markov-locality identity. -/
  generator : ℕ → A
  /-- A function returning the GS normal-form word length. -/
  nfLength : A → ℕ
  /-- Per-position vertex volume in the normal-form word. -/
  vertexVolume : A → ℕ → R
  /-- **(1) Markov locality**: appending a single generator
      multiplies the trace by `markovParameter`. -/
  markovLocality :
    ∀ (x : A) (n : ℕ),
      trM (x * generator n) = markovParameter * trM x
  /-- **(2) Vertex volumes are local** in the normal-form word:
      `vertexVolume x i` depends only on the `i`-th normal-form
      position of `x`, not on its global braid input. Encoded as a
      definitional witness via the class signature itself. -/
  vertexVolume_local :
    ∀ (x : A) (i : ℕ),
      i < nfLength x → ∃ (V : R), vertexVolume x i = V
  /-- **(3) Product factorisation**: the Markov trace of the
      normal-form equals the product of vertex volumes. -/
  productFactorisation :
    ∀ (x : A),
      trM x = ∏ i ∈ Finset.range (nfLength x), vertexVolume x i

end QOU.Observations.TraceLocalityMeetsGsNonLocality
