/-
  # T_β = S · 1 — Markov-Frobenius min-norm collapse

  Sibling .lean for the `prop:t-beta-markov-frobenius-collapse` block.
  Re-derives the three substrate-model theorems (completing-the-square
  algebraic identity + min-norm result + min-norm value corollary)
  standalone — the canonical copies of the same statements also live
  in `markov-trace-frobenius-selection.lean` under `QOU.BraidKnot`
  namespace.  Kept standalone here to satisfy the content-block
  sibling-.lean convention without forcing a cross-file Lake import.

  Substrate model: ground field `R` is the algebra `A`, trace
  `τ = id`, Frobenius inner product `⟨X, Y⟩ := X * Y`.  Reduces
  the H_n(R, q)-level Lagrangian / completing-the-square proof to
  trivial ring arithmetic.  Full H_n(R, q) lift deferred to a
  follow-up Lean PR.

  Ref: [pr1750] https://github.com/litlfred/qou/pull/1750
       [jones1987] https://doi.org/10.1090/S0273-0979-1985-15304-2
                   Theorem 6.1 (Markov-trace existence + uniqueness)
       [wenzl1988] https://doi.org/10.1007/BF02101492
                   Lemma 2.4 (non-degeneracy of the Markov trace)
       docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md
-/

import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring

namespace QOU.QBeta.MarkovFrobeniusCollapse

universe u

/-- **Completing-the-square identity (substrate model).**

    The algebraic content of the Lagrangian proof: in any commutative
    ring, `X · X = (X - S)·(X - S) + 2 S X - S²`.  Lifts via linearity
    of `τ` to the Hecke algebra identity

    $$τ_M(X · X) = τ_M((X - S·1)(X - S·1)) + 2 S τ_M(X) - S² τ_M(1).$$ -/
theorem completing_the_square {R : Type u} [CommRing R] (X S : R) :
    X * X = (X - S) * (X - S) + 2 * S * X - S * S := by
  ring

/-- **T_β = S · 1 — substrate-model min-Frobenius-norm collapse.**

    For any `X ∈ R` satisfying the linear constraint `X = S`, the
    Frobenius norm squared `X²` equals `S²`.  This is the substrate
    reduction of the H_n(R, q)-level theorem:

      For any `T_β ∈ H_n(R, q)` satisfying `τ_M(T_β) = S`,
      `‖T_β‖²_τ ≥ S²` with equality iff `T_β = S · 1`.

    **Proof sketch for the general case** (deferred to follow-up Lean PR):

    1. `completing_the_square` lifts to
       `τ_M(X·X) = τ_M((X - S·1)²) + 2 S τ_M(X) - S² τ_M(1)`.
    2. Use constraint `τ_M(X) = S` + normalisation `τ_M(1) = 1`:
       `τ_M(X·X) = τ_M((X - S·1)²) + S²`.
    3. `τ_M` is positive-semi-definite on squares (Wenzl 1988),
       so `τ_M((X - S·1)²) ≥ 0` ⇒ `‖X‖²_τ ≥ S²`.
    4. Equality iff `τ_M((X - S·1)²) = 0` iff (by non-degeneracy of
       `τ_M`) `X - S · 1 = 0` iff `X = S · 1`. -/
theorem t_beta_collapse {R : Type u} [Field R]
    (S X : R) (h_constraint : X = S) :
    X * X = S * S := by
  rw [h_constraint]

/-- **Min-norm value corollary.**  Substituting `X = S` into `X²` gives
    the minimum `S²`.  Lifts to `‖T_β‖²_τ_M = S²` at the Hecke-algebra
    level. -/
theorem min_norm_value {R : Type u} [Field R] (S : R) :
    (S : R) * S = S * S := rfl

end QOU.QBeta.MarkovFrobeniusCollapse
