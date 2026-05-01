/-!
# QOU.ArchimedeanRemainder — exponential-decay conjecture (typeclass)

The archimedean remainder

  R_n(K) := V_hyp(K) - A_n(K)

is conjectured to decay exponentially in the Gröbner–Shirshov filtration
depth `n`, with a knot-dependent rate `c(K) > 0`. The conjecture is
**open in general** (proved for specific families: figure-eight,
certain torus knots). Following the CLAUDE.md §3b convention for
formalising open conjectures we package it as a Lean typeclass; any
instance is conjecture-bearing, downstream theorems consuming
`[DecayConjecture]` are conditional on it.

LaTeX label: `conj:archimedean-remainder-exponential-decay`

## References

- [kashaev1997] https://doi.org/10.1023/A:1007364912784
- [murakami-murakami2001] https://doi.org/10.1007/BF02392716
- [zagier1986] https://doi.org/10.1007/BFb0084581
- [neumann-zagier1985] https://doi.org/10.1016/0040-9383(85)90004-7
- [manuscript] braids-and-knots / archimedean-remainder-exponential-decay
-/

import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Exp

namespace QOU.ArchimedeanRemainder

/-- Abstract knot-data carrier. The actual knot type is supplied by
    the concrete instance — for the conjecture statement we only need
    `hypVolume`, `algebraicVolume`, and a depth parameter. -/
structure KnotData where
  /-- Hyperbolic volume `V_hyp(K)`. -/
  hypVolume : ℝ
  /-- Truncated algebraic quantum volume at depth `n`,
      `A_n(K) = τ_arch(Vol_q(β_K)) computed up to GS depth n`. -/
  algebraicVolume : ℕ → ℝ

/-- The archimedean remainder `R_n(K) := V_hyp(K) - A_n(K)`. -/
noncomputable def remainder (K : KnotData) (n : ℕ) : ℝ :=
  K.hypVolume - K.algebraicVolume n

/-- **Exponential-decay conjecture (axiomatised).**
    For each knot `K`, conjecturally there exist constants `C, c > 0`
    such that `|R_n(K)| ≤ C · exp(-c · n)` for all sufficiently large
    `n`.

    Any concrete instance must supply the constants and the threshold
    `n₀` together with the bound. -/
class DecayConjecture (K : KnotData) where
  /-- Multiplicative constant. -/
  C : ℝ
  /-- Decay rate `c > 0`. -/
  c : ℝ
  /-- Threshold above which the bound holds. -/
  n₀ : ℕ
  /-- Positivity of the multiplicative constant. -/
  C_pos : 0 < C
  /-- Strict positivity of the decay rate. -/
  c_pos : 0 < c
  /-- **The conjecture itself**: the exponential bound.
      This field plays the role of `sorry` for the conjecture. -/
  decay_holds :
    ∀ n, n₀ ≤ n →
      |remainder K n| ≤ C * Real.exp (-(c * (n : ℝ)))

/-- Re-export of the bound for callers that have a `[DecayConjecture]`
    instance in scope. -/
-- Ref: [manuscript] conj:archimedean-remainder-exponential-decay
theorem remainder_bounded (K : KnotData) [D : DecayConjecture K]
    (n : ℕ) (hn : D.n₀ ≤ n) :
    |remainder K n| ≤ D.C * Real.exp (-(D.c * (n : ℝ))) :=
  D.decay_holds n hn

/-- The decay constants are positive (re-export of the
    `DecayConjecture` fields). -/
-- Ref: [manuscript] conj:archimedean-remainder-exponential-decay
theorem decay_constants_pos (K : KnotData) [D : DecayConjecture K] :
    0 < D.C ∧ 0 < D.c :=
  ⟨D.C_pos, D.c_pos⟩

end QOU.ArchimedeanRemainder
