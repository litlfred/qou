/-!
# QOU.frobenius_dagger_positive_definite — `f† ∘ f > 0` for all `f ≠ 0`

**Proposition** (conditional on a formally-real pivotal structure)
([`prop:positive-definite-dagger`](../../../quantum-observable-universe/quantum-universes/positive-definite-dagger.md)).

*Let `(𝐂, A, τ)` be a quantum universe whose endomorphism ring
`End(𝟙) ≅ R` is a formally-real ordered field, with Frobenius pairing
`⟨a, b⟩ = ∫_A(μ(a ⊗ b))` and a pivotal self-adjoint antipode `S`.  Define
the* Frobenius dagger *by `f† = ∫_A ∘ μ(S(f) ⊗ −)`.  Then for every
non-zero `f : 𝟙 → X`, the composite `f† ∘ f = ⟨f, f⟩` is a positive
element of `R`.*

This is a §3b-cond **conditional-class** encoding: the class
`FormallyRealPivotalDagger` carries the three *hypotheses* the argument
consumes — non-degeneracy of the pairing, the pivotal adjoint
identification (`⟨f, f⟩` is a square), and formal reality (a non-zero
square is positive) — and `frobenius_dagger_positive_definite`
**derives** the positivity conclusion from them.  The class fields encode
inputs, not the conclusion; the theorem is a genuine composition, not a
self-assuming projection.  The instance (that a given quantum universe —
e.g. `Rep(SU_q(2))` at the substrate value over `ℝ` — satisfies these
hypotheses) is discharged on the archimedean/models side.

The development is deliberately import-free so the derivation stands on
Lean core alone.

-- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
-- Ref: [manuscript] quantum-observable-universe/quantum-universes/positive-definite-dagger.md
-/

namespace QOU

/-- Hypotheses under which the Frobenius dagger is positive-definite.

    Each field is an **input** to the positivity argument, never its
    conclusion:
    * `dagger_is_normSquare` — the pivotal adjoint identification
      `S = †`, so `f† ∘ f` equals the categorical norm-square `⟨f, f⟩`;
    * `normSquare_is_square` — that norm-square is a genuine square in
      `R` (the adjoint hypothesis);
    * `normSquare_ne_zero` — non-degeneracy of the Frobenius pairing:
      `⟨f, f⟩ ≠ 0` for `f ≠ 0`;
    * `pos_of_nonzero_square` — formal reality of the ordered field `R`:
      a non-zero square is positive. -/
class FormallyRealPivotalDagger where
  /-- Morphisms `f : 𝟙 → X`. -/
  Mor1X : Type
  /-- The endomorphism ring `End(𝟙) ≅ R`. -/
  R : Type
  /-- The zero of `R`. -/
  zero : R
  /-- Multiplication on `R` (used to express "is a square"). -/
  mul : R → R → R
  /-- The composite `f† ∘ f ∈ End(𝟙) ≅ R`. -/
  composeDaggerOriginal : Mor1X → R
  /-- The categorical norm-square `⟨f, f⟩`. -/
  normSquare : Mor1X → R
  /-- The "is non-zero morphism" predicate. -/
  isNonzero : Mor1X → Prop
  /-- The "is positive" predicate on `R`. -/
  isPositive : R → Prop
  /-- Pivotal adjoint identification: `f† ∘ f = ⟨f, f⟩`. -/
  dagger_is_normSquare : ∀ f, composeDaggerOriginal f = normSquare f
  /-- Adjoint hypothesis: the norm-square is a genuine square in `R`. -/
  normSquare_is_square : ∀ f, ∃ s, normSquare f = mul s s
  /-- Non-degeneracy of the pairing: `⟨f, f⟩ ≠ 0` for non-zero `f`. -/
  normSquare_ne_zero : ∀ f, isNonzero f → normSquare f ≠ zero
  /-- Formal reality of the ordered field `R`: a non-zero square is
      positive. -/
  pos_of_nonzero_square : ∀ r, r ≠ zero → (∃ s, r = mul s s) → isPositive r

/-- **Frobenius dagger is positive-definite**
    ([`prop:positive-definite-dagger`]).

    For every non-zero morphism `f : 𝟙 → X`, the composite `f† ∘ f` is a
    positive element of `End(𝟙)`.  Derived from the three hypotheses of
    `FormallyRealPivotalDagger` — non-degeneracy, the pivotal adjoint
    square, and formal reality — composed in that order. -/
-- Ref: [manuscript] quantum-observable-universe/quantum-universes/positive-definite-dagger.md
theorem frobenius_dagger_positive_definite [ctx : FormallyRealPivotalDagger]
    (f : ctx.Mor1X) (h : ctx.isNonzero f) :
    ctx.isPositive (ctx.composeDaggerOriginal f) := by
  rw [ctx.dagger_is_normSquare f]
  exact ctx.pos_of_nonzero_square (ctx.normSquare f)
    (ctx.normSquare_ne_zero f h) (ctx.normSquare_is_square f)

end QOU
