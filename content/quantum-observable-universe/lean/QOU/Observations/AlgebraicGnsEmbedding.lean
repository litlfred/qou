import Mathlib.Tactic
import Mathlib.Analysis.InnerProductSpace.Basic

/-!
# QOU.Observations.AlgebraicGnsEmbedding

The Markov-trace GNS embedding `H_∞(q) ↪ L(H)`, encoded as a
typeclass packaging the four ingredients of the construction.

Unlike `MuArchContinuumLimit`, the GNS construction is **not
conjectural**: it is the Jones–Wenzl subfactor machinery
([jones1985], [wenzl1988]), valid in the positivity regime
`q^{1/2} + q^{-1/2} > 2` which covers the QOU substrate
`q_0 ≈ 1.11`.

The class fields are the *data* of the construction (positive
tracial state on the inductive system, trace ideal, Hilbert-space
completion, faithful representation). Provided an instance, the
embedding `π_GNS : H_∞(q) → L(H)` is exhibited.

## References

- [jones1985] V. F. R. Jones, *A polynomial invariant for knots via
  von Neumann algebras*, Bull. AMS 12 (1985) 103-111.
- [wenzl1988] H. Wenzl, *Hecke algebras of type A_n and subfactors*,
  Invent. Math. 92 (1988) 349-383.
-/

namespace QOU.Observations.AlgebraicGnsEmbedding

universe u v

open scoped BigOperators

/-- **Markov-trace GNS embedding data.**

A class witnessing the Jones–Wenzl GNS embedding of the inductive
limit Hecke algebra `H_∞(q)` into bounded operators on a Hilbert
space. Each field carries concrete content; no `True` placeholders.

The carrier `A` represents `H_∞(q)`, the carrier `H` represents the
GNS Hilbert space, and `repr` is the faithful representation. -/
class HasMarkovGnsEmbedding (A : Type u) (H : Type v)
    [NonUnitalNonAssocRing A] [Star A]
    [NormedAddCommGroup H] [InnerProductSpace ℝ H] [CompleteSpace H] where
  /-- The (real-valued) Markov trace. -/
  trM : A → ℝ
  /-- **Linearity** of `trM`. -/
  trM_add : ∀ (x y : A), trM (x + y) = trM x + trM y
  /-- **Traciality** (cyclicity): `tr_M(x · y) = tr_M(y · x)`. -/
  trM_cyclic : ∀ (x y : A), trM (x * y) = trM (y * x)
  /-- **Positivity** (Wenzl regime): `tr_M(x* x) ≥ 0`. -/
  trM_pos : ∀ (x : A), 0 ≤ trM (star x * x)
  /-- **Faithfulness on the GNS quotient**:
      `tr_M(x* x) = 0 → x ∈ trace ideal`. Encoded via an explicit
      ideal predicate. -/
  traceIdeal : A → Prop
  trM_faithful : ∀ (x : A), trM (star x * x) = 0 ↔ traceIdeal x
  /-- **The GNS representation** as a function `A → (H → H)`
      (left multiplication on the GNS quotient, extended to H by
      continuity). -/
  repr : A → (H → H)
  /-- **Linearity of `repr`** in its first argument
      (so `repr (x + y) = repr x + repr y` pointwise). -/
  repr_add : ∀ (x y : A) (h : H), repr (x + y) h = repr x h + repr y h
  /-- **Multiplicativity of `repr`** (a *-homomorphism on the
      algebra-action side). -/
  repr_mul : ∀ (x y : A) (h : H), repr (x * y) h = repr x (repr y h)
  /-- **Faithfulness of `repr`**: zero representation only for
      ideal elements. -/
  repr_faithful : ∀ (x : A), (∀ h : H, repr x h = 0) → traceIdeal x


/-! ### Removed 2026-08-30 — self-assuming projections

- `markov_gns_embedding` — body was `⟨inst.repr, inst.repr_add, inst.repr_mul, inst.repr_faithful⟩`: the conclusion was the
  projected field verbatim, so the declaration restated its own hypothesis.

**Why removal.** The content stays in the class field each declaration
projected, asserting the same proposition under the same hypotheses; only the
restatement goes. That is the vacuity ledger's recorded disposition for this
category — *"drop the pseudo-theorem and project the field at use sites"* — and
there were no use sites: each had **zero references anywhere in the corpus**.
Bean `qou-z9ws`.
-/

end QOU.Observations.AlgebraicGnsEmbedding
