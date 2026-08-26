import Mathlib.Analysis.InnerProductSpace.EuclideanDist
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Tactic

/-!
# QOU.HeckeAlgebra.Common — abstract Hecke-algebra-at-q₀ types

Foundational types for the Iwahori-Hecke algebra `H_n(q)` at the
QOU substrate parameter `q = q_0`, exposed at the level of detail
needed by the `QOU.BraidKnot.*` SDP-uniqueness theorems.

## What this module provides

- `heckeDim n` — `n!`, the dimension of `H_n(q)` over `ℂ` (and
  hence over `ℝ` once we forget complex structure).
- `HeckeElement n` — abstract elements of `H_n(q_0)` represented
  as real Euclidean-space vectors (placeholder representation
  sufficient for the convex-analysis arguments downstream).
- `frobeniusInner` — the standard Frobenius inner product on
  `H_n(q_0)`, exposed as the inner product on the underlying
  Euclidean space.
- `markovTrace` — the Markov trace `H_n(q_0) → ℝ` (axiomatised;
  concrete categorical definition lives in the rendered manuscript
  and Python compute layer, not yet ported to Lean).

## Categorical content (axiomatised)

The Hecke algebra `H_n(q)` has a Wedderburn decomposition
`H_n(q) ≅ ⊕_{λ ⊢ n} M_{d_λ}(ℂ)` and a canonical Markov trace
satisfying `tr_M(σ_i σ_{i+1} σ_i) = tr_M(σ_{i+1} σ_i σ_{i+1})`
(the cubic relation) and the trace cyclicity
`tr_M(xy) = tr_M(yx)`.  This module exposes these as Lean axioms
so downstream SDP-uniqueness theorems can apply
`QOU.MathlibExt.SDP.strict_complementarity_unique` to concrete
Hecke-algebra-valued primal points.

## References

- [kassel2008] Kassel-Turaev, *Braid Groups*, Springer GTM 247.
  https://doi.org/10.1007/978-0-387-68548-9
- [wenzl1988] Wenzl, *Hecke algebras of type A_n and subfactors*,
  Inventiones Math. 92 (1988), 349-383.
- [hoefsmit1974] Hoefsmit, *Representations of Hecke algebras of
  finite groups with BN-pairs of classical type* (1974).
-/

namespace QOU.HeckeAlgebra

/-- **Hecke-algebra dimension** at `n` strands.  For type `A_{n-1}`,
    `dim_ℂ H_n(q) = n!`.  We use this dimension count whether `q`
    is a formal parameter or the QOU substrate value `q_0`. -/
def heckeDim (n : ℕ) : ℕ := n.factorial

/-- **Abstract Hecke-algebra element** at `n` strands and parameter
    `q_0`.  Represented as a vector in `EuclideanSpace ℝ` of
    dimension `heckeDim n`, sufficient for the convex-analysis
    arguments used downstream (Frobenius inner product, strict
    convexity).  The full algebraic structure (multiplication,
    Hecke relations, generators σ_i) is *not* exposed here; this
    module captures only the linear-algebra layer needed for the
    SDP arguments.

    Concrete categorical structure (Wedderburn decomposition,
    Markov trace, generator action) is in scope for future work
    once the Lean port of the Hoefsmit / Wenzl machinery lands. -/
abbrev HeckeElement (n : ℕ) : Type :=
  EuclideanSpace ℝ (Fin (heckeDim n))

/-- **Frobenius inner product** on `H_n(q_0)`.  Standard inner
    product on the underlying Euclidean space, exposed under the
    QOU naming convention.  Symmetric, bilinear, positive-definite. -/
noncomputable def frobeniusInner {n : ℕ} (x y : HeckeElement n) : ℝ :=
  inner ℝ x y

/-- The Frobenius inner product is positive on non-zero elements:
    `frobeniusInner x x > 0` for `x ≠ 0`.  Inherited from
    Mathlib's `EuclideanSpace` inner-product structure. -/
theorem frobeniusInner_self_pos {n : ℕ} {x : HeckeElement n} (hx : x ≠ 0) :
    0 < frobeniusInner x x := by
  unfold frobeniusInner
  exact real_inner_self_pos.mpr hx

/-- The Frobenius inner product is bilinear-symmetric: `⟨x, y⟩ = ⟨y, x⟩`. -/
theorem frobeniusInner_symm {n : ℕ} (x y : HeckeElement n) :
    frobeniusInner x y = frobeniusInner y x := by
  unfold frobeniusInner
  exact real_inner_comm y x

/-- **Riesz weight of the Markov trace.**

    `HeckeElement n` is a finite-dimensional real inner-product space, so by
    Riesz representation EVERY `ℝ`-linear functional on it is `⟪w, ·⟫` for a
    unique `w`.  The Markov trace is such a functional, so nothing is lost by
    carrying it as its weight vector rather than as an opaque function: the two
    presentations have exactly the same content.

    What IS gained is that linearity stops being assumed.  See
    `markovTrace_linear` below, which was an `axiom` until 2026-08-26.

    The weight itself stays `opaque` because its VALUE is genuinely not
    formalised here — categorically it is the Jones-Markov combination
    `Σ_λ y_λ χ^λ` (`QOU.HeckeAlgebra.MarkovTrace.markovTraceOnWedderburn`
    carries that form against a Wedderburn decomposition).  An `opaque`
    datum asserts nothing; an opaque function plus an asserted property
    asserts something unprovable.  This is the difference. -/
-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457 §3 (the trace is the y_λ-weighted block-trace sum, hence linear)
opaque markovTraceWeight : (n : ℕ) → HeckeElement n

/-- **Markov trace** on `H_n(q_0)`, as the linear functional with Riesz weight
    `markovTraceWeight n`.

    The full categorical definition (Jones-Markov coefficients `y_λ`,
    partition-sum decomposition) lives in the rendered manuscript and the Python
    compute layer; what is formalised here is that the trace is a linear
    functional, which is the only property the downstream SDP-uniqueness
    arguments use.

    **Cyclicity is a separate matter** and remains an axiom
    (`MarkovTrace.MarkovTrace_cyclic`): it constrains this functional against
    `heckeMul`, which is itself `opaque`, so it is not expressible from the
    linear-algebra layer alone.

    🛑 **This does NOT pin the trace to a non-zero function.** Taking
    `markovTraceWeight n = 0` satisfies this definition and every axiom stated
    about `markovTrace` in `QOU.HeckeAlgebra.MarkovTrace`, since each of those
    reads `0 = 0` under it. That was already true of the previous `opaque`
    presentation and is unchanged here — but it is worth stating where a reader
    will see it, because a sharper version of the same degeneracy was a live
    defect: bean `qou-ck1f` found `MarkovTrace_markov_axiom` binding its Markov
    parameter with `∀ (z : ℝ)`, which PROVED `tr_M ≡ 0`. Removing that binder
    removed the proof of degeneracy; it did not add anything excluding it.
    Nothing in this layer forces `tr_M ≠ 0`. -/
-- Ref: [kassel2008] https://doi.org/10.1007/978-0-387-68548-9 §13.6 (Markov trace H_n(q) → ℝ)
noncomputable def markovTrace (n : ℕ) (x : HeckeElement n) : ℝ :=
  frobeniusInner (markovTraceWeight n) x

/-- The Markov trace is linear in its argument: this is the only structural
    property of `markovTrace` used by the SDP-uniqueness arguments downstream.

    **Was an `axiom` until 2026-08-26**, on the stated ground that the
    categorical definition had not been ported. That reasoning conflated two
    things: the trace's *value* (genuinely not formalised, and still carried
    opaquely in `markovTraceWeight`) with its *linearity*, which is a property
    of the shape `⟪w, ·⟫` and needs no value at all. Riesz representation makes
    the two presentations equivalent, so this costs nothing and discharges the
    assumption. -/
theorem markovTrace_linear (n : ℕ) :
    IsLinearMap ℝ (fun x : HeckeElement n => markovTrace n x) := by
  constructor
  · intro x y
    simp only [markovTrace, frobeniusInner, inner_add_right]
  · intro c x
    simp only [markovTrace, frobeniusInner, real_inner_smul_right, smul_eq_mul]

/-- **Absolute Markov trace** — the modulus of the Markov trace
    used in the QOU mass formula `M = ρ · m_e · |tr_M(T_w)|`.
    Always non-negative. -/
noncomputable def absMarkovTrace (n : ℕ) (x : HeckeElement n) : ℝ :=
  |markovTrace n x|

theorem absMarkovTrace_nonneg (n : ℕ) (x : HeckeElement n) :
    0 ≤ absMarkovTrace n x := abs_nonneg _

end QOU.HeckeAlgebra
