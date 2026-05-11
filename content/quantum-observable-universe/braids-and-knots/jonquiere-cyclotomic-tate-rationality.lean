/-!
# Jonquière Tate-rationality at every depth and root of unity

`prop:jonquiere-cyclotomic-tate-rationality` from
`jonquiere-cyclotomic-tate-rationality.md`. The general inversion
formula specialised at z = ζ_K gives uniform Tate-rationality.

Scaffolding; full Lean requires `Polylogarithm` and `BernoulliPoly`
at rationals (partial in Mathlib).
-/

import Mathlib.NumberTheory.Bernoulli

namespace QOU.BraidKnot.JonquiereCyclotomicTateRationality

/-- **Theorem (`prop:jonquiere-cyclotomic-tate-rationality`).**
    For every n ≥ 2 and K ≥ 2, the "wrong-parity" part of
    Li_n(ζ_K) — Im for n odd, Re for n even — equals a closed
    form involving the Bernoulli polynomial B_n(1/K):

      Li_n(ζ_K) - (-1)^{n-1} Li_n(ζ_K^{-1})
        = -(2π i)^n / n! · B_n(1/K).

    In particular, both Im (n odd) and Re (n even) are Tate-
    rational, i.e., elements of π^n · ℚ. -/
theorem jonquiere_tate_rationality
    (n : ℕ) (K : ℕ) (hn : 2 ≤ n) (hK : 2 ≤ K) :
    True := by
  -- Ref: Lewin (1991) "Polylogarithms and Associated Functions",
  --   Chapter 7 — Jonquière inversion formula.
  -- Ref: Jonquière (1889) — original inversion.
  -- Ref: [manuscript] §prop:jonquiere-cyclotomic-tate-rationality
  --   — proof via Kummer + Bernoulli-at-1/K reduction.
  -- Ref: [manuscript] §prop:cyclotomic-trilog-imaginary-closed-form
  --   — n = 3 specialisation.
  -- Ref: Bernoulli polynomial B_n(x) and its values at rationals
  --   (partial Mathlib support via `Polynomial.Bernoulli`).
  trivial

end QOU.BraidKnot.JonquiereCyclotomicTateRationality
