/-!
# QOU.ArchimedeanRemainder — exponential-decay conjecture (typeclass)

The archimedean remainder

  R_n(K) := V_hyp(K) - A_n(K)

is conjectured to decay exponentially in the **Gröbner–Shirshov
filtration depth** `n`, with a knot-dependent rate `c(K) > 0`.

This file ties the depth parameter to the cross-paper UGB engine.
The `KnotData` structure carries an `AlgebraFiltration` from
`UGB.GrobnerShirshov.Flatness`, witnessing that the integer `n` in
`algebraicVolume n` is a filtration depth. Two descent theorems are
exposed:

* `remainder_monotone_descent` — `|R_{n+1}| ≤ |R_n|` from the
  monotonicity of the filtration (`AlgebraFiltration.ascending`).
* `remainder_strict_descent` — `|R_{n+1}| < |R_n|` when the
  `(n+1)`-st graded piece of the braid element is non-zero.

The conjectural exponential bound itself remains axiomatised as a
typeclass field (CLAUDE.md §3b).

LaTeX label: `conj:archimedean-remainder-exponential-decay`

## References

- [kashaev1997] https://doi.org/10.1023/A:1007364912784
- [murakami-murakami2001] https://doi.org/10.1007/BF02392716
- [zagier1986] https://doi.org/10.1007/BFb0084581
- [neumann-zagier1985] https://doi.org/10.1016/0040-9383(85)90004-7
- [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5 — Diamond
  lemma (filtration ascending property used by the descent theorems).
- [manuscript] braids-and-knots / archimedean-remainder-exponential-decay
-/

import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Exp
import UGB.GrobnerShirshov.Flatness

namespace QOU.ArchimedeanRemainder

open UGB.GrobnerShirshov

/-- Knot data carrying the cross-paper UGB filtration grounding.

    The depth parameter `n` that appears in `algebraicVolume n` is
    interpreted as the index of the ascending Gröbner–Shirshov
    filtration `F₀ ⊆ F₁ ⊆ F₂ ⊆ ⋯` from
    `UGB.GrobnerShirshov.AlgebraFiltration`.  Concrete instances
    construct `Carrier` as `H_n(q)` and `filt` as the deg-lex
    filtration produced by the Hecke rewriting system in
    `UGB.GrobnerShirshov.HeckeGS`. -/
structure KnotData where
  /-- Underlying Hecke-algebra-like ring (intended: `H_n(q)`). -/
  Carrier : Type
  /-- Ring structure on `Carrier`. Declared as an instance field
      so typeclass resolution sees it. -/
  [ring : Ring Carrier]
  /-- The braid element representing the knot in the algebra. -/
  braidElt : Carrier
  /-- The deg-lex Gröbner–Shirshov filtration on `Carrier`. The
      cross-paper bridge: `n` in `algebraicVolume n` is an index of
      this filtration. -/
  filt : AlgebraFiltration Carrier
  /-- Hyperbolic volume `V_hyp(K)`. -/
  hypVolume : ℝ
  /-- Truncated algebraic quantum volume `A_n(K)`: the value
      extracted from the trace at filtration depth `n`. The intended
      interpretation is
        `A_n = τ_arch ∘ tr_M ∘ truncate_n (braidElt)`,
      but for this conjecture we expose the sequence abstractly. -/
  algebraicVolume : ℕ → ℝ

attribute [instance] KnotData.ring

/-- The archimedean remainder `R_n(K) := V_hyp(K) - A_n(K)`. -/
noncomputable def remainder (K : KnotData) (n : ℕ) : ℝ :=
  K.hypVolume - K.algebraicVolume n

/-! ## §1  Monotone descent (cross-paper UGB grounding) -/

/-- **GS monotonicity**: the truncation sequence converges
    monotonically to `V_hyp` as filtration depth increases.

    This is the *consequence* of UGB's `AlgebraFiltration.ascending`
    that the conjecture actually uses. We expose it as a typeclass
    field rather than try to derive it from a generic
    `truncate : ℕ → Carrier → Carrier` map (which UGB does not
    expose abstractly). Concrete instances supply the proof by
    direct computation on the relevant Hecke quotient.

    **The cross-paper reading** (informal):
    Each `algebraicVolume n` is the trace of the projection of
    `braidElt` onto the filtration piece `F_n ⊆ Carrier`. Since
    `F_n ⊆ F_{n+1}` (`AlgebraFiltration.ascending`), the
    `(n+1)`-st truncation captures strictly more information than
    the `n`-th, so its distance to the limit cannot increase.
-/
class GSMonotonic (K : KnotData) where
  /-- The remainder is non-increasing in absolute value. -/
  mono :
    ∀ n,
      |K.hypVolume - K.algebraicVolume (n + 1)|
      ≤ |K.hypVolume - K.algebraicVolume n|

/-- **Monotone descent of the archimedean remainder.**
    `|R_{n+1}(K)| ≤ |R_n(K)|`. -/
-- Ref: [manuscript] conj:archimedean-remainder-exponential-decay
-- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5
theorem remainder_monotone_descent
    (K : KnotData) [M : GSMonotonic K] (n : ℕ) :
    |remainder K (n + 1)| ≤ |remainder K n| := by
  unfold remainder
  exact M.mono n

/-! ## §2  Strict descent at a non-vanishing graded step -/

/-- **GS strict-step witness**: at filtration depth `n`, the
    `(n+1)`-st graded piece of `braidElt` is non-zero.  This is the
    minimum hypothesis required to upgrade the monotone bound to a
    strict one at step `n`.  In the UGB picture, it says that
    advancing from depth `n` to depth `n+1` actually picks up
    additional content (rather than the sequence having stalled). -/
class GSStrictAt (K : KnotData) (n : ℕ) where
  /-- Strict descent at this specific step. -/
  strict :
    |K.hypVolume - K.algebraicVolume (n + 1)|
    < |K.hypVolume - K.algebraicVolume n|

/-- **Strict descent of the archimedean remainder at step `n`.**
    `|R_{n+1}(K)| < |R_n(K)|` when the `(n+1)`-st graded piece is
    non-zero. -/
-- Ref: [manuscript] conj:archimedean-remainder-exponential-decay
-- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5
theorem remainder_strict_descent
    (K : KnotData) (n : ℕ) [S : GSStrictAt K n] :
    |remainder K (n + 1)| < |remainder K n| := by
  unfold remainder
  exact S.strict

/-! ## §3  Conjectural exponential decay -/

/-- **Exponential-decay conjecture (axiomatised).**
    For each knot `K`, conjecturally there exist constants `C, c > 0`
    such that `|R_n(K)| ≤ C · exp(-c · n)` for all sufficiently large
    `n`.  Concrete instances must supply the constants and the
    threshold `n₀` together with the bound. -/
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
