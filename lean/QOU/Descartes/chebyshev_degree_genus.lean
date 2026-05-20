/-!
# QOU.Descartes.chebyshev_degree_genus — Chebyshev degree equals Seifert genus

**Lemma** ([`lem:chebyshev-degree-genus`](../../../quantum-observable-universe/descartes-universe/chebyshev-degree-genus.md)).

*Let `a : ℕ → Polynomial ℤ` be the Hecke recurrence*

```
  a 0       = 0
  a 1       = 1
  a (n + 2) = s · a (n+1) + a n
```

*(where `s = Polynomial.X`).  Substituting `u = s²`, for every odd
positive `p`, the polynomial `a p` is a polynomial in `u = s²` of
degree `(p - 1) / 2 = g(T_{2,p})` with leading coefficient `1`.*

The statement below records the recurrence, the half-degree shape,
and the leading-coefficient claim as separate fields of a `Prop`-
returning theorem.  Discharging the body requires a strong-induction
argument on the recurrence depth (see manuscript).

-- Ref: [manuscript] quantum-observable-universe/descartes-universe/chebyshev-degree-genus.md
-/

import Mathlib.Algebra.Polynomial.Basic
import Mathlib.Data.Nat.Prime.Defs

namespace QOU.Descartes

open Polynomial

/-- The Hecke recurrence `a` over `Polynomial ℤ`, indexed by ℕ.

    `a 0 = 0`, `a 1 = 1`, `a (n+2) = X · a (n+1) + a n`.
    These are the Chebyshev-like polynomials whose specialisation at
    `s = q^{1/2} + q^{-1/2}` recovers the Markov-trace evaluations of
    the torus-knot family `T_{2,n}` in the Iwahori–Hecke algebra. -/
noncomputable def heckeRecurrence : ℕ → Polynomial ℤ
  | 0          => 0
  | 1          => 1
  | (n + 2)    => Polynomial.X * heckeRecurrence (n + 1) + heckeRecurrence n

/-- **Chebyshev degree equals Seifert genus** ([`lem:chebyshev-degree-genus`]).

    For every odd `p`, the Hecke recurrence polynomial `a p` has
    `Polynomial.natDegree = p - 1`, equal to twice the Seifert genus
    `g(T_{2,p}) = (p - 1) / 2`.  Equivalently, when re-expressed via
    `u = X²` the resulting polynomial in `u` has degree `(p - 1) / 2`
    and leading coefficient `1`.

    The full degree-and-leading-coefficient pair is captured as a
    conjunction; the proof proceeds by strong induction on the
    recurrence depth (Markov-trace tower; see manuscript). -/
-- Ref: [manuscript] quantum-observable-universe/descartes-universe/chebyshev-degree-genus.md
-- Ref: [kassel2008] Braid Groups (GTM 247), §4 (Hecke recurrence)
theorem chebyshev_degree_genus
    (p : ℕ) (hp_odd : Odd p) (hp_pos : 0 < p) :
    (heckeRecurrence p).natDegree = p - 1 ∧
    (heckeRecurrence p).leadingCoeff = 1 := by
  -- Strong induction on `p` via the Hecke recurrence (see manuscript).
  sorry

end QOU.Descartes
