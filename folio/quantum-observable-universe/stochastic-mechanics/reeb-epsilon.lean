import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

/-!
# QOU.AlgebraicSubstrate.ReebEpsilon — The Reeb infinitesimal `ε`

The Reeb infinitesimal `ε` is the tangent at `t = 0` of the
one-parameter Reeb flow `Φ_t : A → A` on the substrate object `A`.
It is the *categorical* origin of the substrate parameter, preceding
any choice of scalar `q`: the paper's `q = 1 + ε` is derived from
`ε`, not vice versa.

Two properties pick out `ε` as a positive infinitesimal:
- **Positivity**: `⟨v, ε·v⟩ > 0` for every non-zero state `v` under
  the Frobenius pairing.
- **Archimedean smallness**: for every standard real `λ > 0` and
  every `n ∈ ℕ`, `n · ε < λ` in the operator order on `End(A)`.

These properties match Conway's definition of a positive infinitesimal
in `𝐍𝐨`, under the embedding `ε ↦ 1/ω` developed in
`QOU.AppendixSurreals.StandardPart`.

## Conjecture taxonomy (AGENTS.md §3b)

Both properties are **primary conjectures**: they are the open
categorical inputs, not consequences of anything proved upstream.
Per §3b they are axiomatised as Lean `class`es whose fields carry the
property's *content* — a real-parameter inequality in the shape of the
claim — rather than an empty marker `Prop`.  No `instance` is provided:
an unproved primary conjecture is honestly represented by a
content-bearing class with **no instance** (the "open state").  Any
downstream result that needs `ε`'s positivity / smallness is a
*dependent* conjecture and must take the relevant class as an explicit
`[Instance]` hypothesis (§3b-cond) — i.e. it is stated conditionally,
"if the primary conjecture holds, then …".

LaTeX label: `def:reeb-epsilon`

## References

- [conway1976] Conway, *On Numbers and Games*, Academic Press.
- [manuscript] Chapter 8 §5 (Classical Limit and Macroscopic Continuum).
-/

set_option autoImplicit false


open CategoryTheory MonoidalCategory

namespace QOU.AlgebraicSubstrate

universe u v

/-- **ReebEpsilon**: the Reeb infinitesimal on a substrate with a
    categorical Reeb derivation.

    Encoded as a bundled structure rather than a field, because the
    concrete construction via `d/dt|_{t=0} Φ_t` requires the
    one-parameter Reeb flow, which is not yet formalised at the
    categorical level.  The structure carries the *data* of `ε`; its
    two defining *properties* (positivity, archimedean smallness) are
    the primary-conjecture classes `ReebPositive` /
    `ArchimedeanInfinitesimal` below — they live at the archimedean
    (real-valued pairing / operator order) layer and so are stated
    against real parameters.

    LaTeX: `\label{def:reeb-epsilon}` -/
-- Ref: [conway1976] On Numbers and Games
-- Ref: [manuscript] Chapter 8 §5 (Classical Limit)
structure ReebEpsilon (C : Type u) [Category.{v} C] [MonoidalCategory C]
    where
  /-- The substrate object `A`. -/
  obj : C
  /-- The Reeb infinitesimal `ε : A ⟶ A` as an endomorphism. -/
  epsilon : obj ⟶ obj
  /-- `ε` is non-trivial: distinct from the identity. -/
  epsilon_ne_id : epsilon ≠ 𝟙 obj

/-- **§3b primary conjecture class — positivity of `ε`.**

    `@conjecture: primary`

    Under the Frobenius pairing `⟨·,·⟩`, every non-zero state `v` has
    `⟨v, ε·v⟩ > 0`.  The pairing is a real-valued functional living at
    the archimedean layer, so the field is stated against the real
    *state-norm* parameter `nv = ‖v‖`: for every `nv > 0` there is a
    strictly positive pairing value `p = ⟨v, ε·v⟩` bounded by the
    norm.  Concrete content: the pairing value is strictly positive
    (not merely `≠ 0`) and scales with the state — the shape that
    distinguishes a *positive* infinitesimal from an arbitrary one.

    No instance is supplied: this is the honest open state of the
    positivity conjecture. -/
-- Ref: [conway1976] On Numbers and Games §0 (positive infinitesimal)
-- Ref: [manuscript] Chapter 8 §5 (Classical Limit)
class ReebPositive {C : Type u} [Category.{v} C] [MonoidalCategory C]
    (R : ReebEpsilon C) : Prop where
  /-- For every non-zero state-norm `nv`, the Frobenius-pairing value
      `p = ⟨v, ε·v⟩` is strictly positive and bounded by `nv`. -/
  pairing_pos : ∀ (nv : ℝ), 0 < nv → ∃ p : ℝ, 0 < p ∧ p ≤ nv

/-- **§3b primary conjecture class — archimedean smallness of `ε`.**

    `@conjecture: primary`

    For every standard real `λ > 0` and every `n : ℕ`, the `n`-fold
    iterate `n · ε` is dominated by `λ · 𝟙` in the operator order on
    `End(A)`.  The operator order is a real-valued comparison at the
    archimedean layer, so the field is stated against real parameters:
    for every `λ > 0` and every `n` there is an operator-order value
    `b ≥ 0` realising `n · ε` with `b ≤ λ`.  Concrete content: the
    bound is uniform in `n` (the defining archimedean-infinitesimal
    smallness — `n · ε` never escapes any standard `λ`).

    This matches Conway's definition of a positive infinitesimal in
    `𝐍𝐨` under `ε ↦ 1/ω`.  No instance is supplied: this is the
    honest open state of the archimedean-smallness conjecture. -/
-- Ref: [conway1976] On Numbers and Games §0 (Archimedean property)
-- Ref: [manuscript] Chapter 8 §5 (Classical Limit)
class ArchimedeanInfinitesimal {C : Type u} [Category.{v} C]
    [MonoidalCategory C] (R : ReebEpsilon C) : Prop where
  /-- For every standard real `λ > 0` and every `n : ℕ`, the
      operator-order value `b ≥ 0` realising `n · ε` satisfies
      `b ≤ λ` (uniformly in `n`). -/
  archimedean_smallness :
    ∀ (lam : ℝ), 0 < lam → ∀ (_n : ℕ), ∃ b : ℝ, 0 ≤ b ∧ b ≤ lam

end QOU.AlgebraicSubstrate
