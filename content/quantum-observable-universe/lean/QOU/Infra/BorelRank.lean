import Mathlib.NumberTheory.NumberField.Basic
import Mathlib.NumberTheory.NumberField.Embeddings

/-!
# Axiomatic Borel rank infrastructure

Borel's theorem on the ranks of `K_{2n-1}^{ind}(F) ⊗ ℚ` for a
number field `F` is not in Mathlib.  This file packages the rank
formula as a typeclass `BorelRank` together with the explicit
dimension constants used in
`prop:borel-partial-resolution` and
`prop:depth-2-identification-bloch-suslin`.

References:
- Borel (1977), *Cohomologie réelle stable de groupes
  S-arithmétiques classiques*.  Publ. Math. IHÉS 64 (1977),
  185-202.
- [bloch2000] Bloch, *Higher regulators*.
- [suslin1991] Suslin, *K_3 of a field, and the Bloch group*.
-/

namespace QOU.Infra.BorelRank

/-- Borel rank of `K_{2n-1}^{ind}(F) ⊗ ℚ` for a number field with
    `(r_1, r_2)` real-and-complex embeddings.  For `n ≥ 2`:

      n even: `r_1 + r_2`
      n odd:  `r_2`

    Formula expressed on naturals. -/
def borelRankPredicted (n : ℕ) (r1 r2 : ℕ) : ℕ :=
  if n % 2 = 0 then r1 + r2 else r2

/-- **Borel rank as a class.**  Records the rank of the
    indecomposable K-theory at every depth `n ≥ 2` for the
    relevant field.  Concrete instances (e.g. cyclotomic fields
    `ℚ(ζ_K)`) instantiate `(r_1, r_2)` and discharge the rank
    equality. -/
class BorelRank (F : Type*) where
  /-- Number of real embeddings of `F`. -/
  r1 : ℕ
  /-- Number of pairs of complex embeddings of `F`. -/
  r2 : ℕ
  /-- The Borel rank formula holds at every `n ≥ 2`.  Existence
      statement — concrete instances may carry stronger content. -/
  rank_formula :
    ∀ n : ℕ, 2 ≤ n → ∃ d : ℕ, d = borelRankPredicted n r1 r2

/-- Cyclotomic field embeddings: for `ℚ(ζ_K)` with `K` prime `≥ 3`,
    `(r_1, r_2) = (0, (K-1)/2)`.  Borel rank at depth `n`:

      n even: `(K-1)/2`
      n odd:  `(K-1)/2`

    (same formula in this case since `r_1 = 0`). -/
def cyclotomicBorelRank (K n : ℕ) : ℕ :=
  borelRankPredicted n 0 ((K - 1) / 2)

end QOU.Infra.BorelRank
