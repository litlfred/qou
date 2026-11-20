import QOU.AppendixSurreals.StandardPart

/-!
# QOU.AppendixSurreals.LocalInfinitesimalField — conjecture carrier

**§3b-cond class axiomatisation** for content block
[`conj:local-infinitesimal-field`](../../../appendix-surreals/local-infinitesimal-field.md):
*Substrate parameter as a local infinitesimal field `ε(x)`*.

Primary conjecture carrier with **no instance** — the honest open state per
AGENTS.md §3b-tax.

## What changed (bean `qou-ffwk`)

The previous field schema was a scalar plus a field asserting that it vanishes,
inhabited by `⟨0, rfl⟩`. The class chose its own witness, so it asserted nothing
and a downstream `[LocalInfinitesimalField]` hypothesis was not a meaningful
conditional.

## Why the scheme and sheaf are *not* modelled

The block sets the conjecture up over a scheme `X` — `ε ∈ Γ(X, 𝔪_X)`, a section
of the sheaf of infinitesimals, with `X` a functor `CRing → Set` evaluated at
the valuation ring of finite surreals. Mathlib's `AlgebraicGeometry.Scheme` and
`Topology.Sheaves` are both available in this tree, so that framing *could* be
written down.

It is deliberately not, because **none of the three claims uses it**. Read them
back: `ε(x)` differs from `ε(y)` somewhere; `st(ε(x)) = 0` everywhere; the
leading coefficient is globally constant. Every one is an extensional statement
about the family `x ↦ ε(x)`. Restricting/gluing, the structure sheaf, and the
`X(𝒪) ↠ X(ℝ)` standard-part map are all *setting* — they explain where the
family comes from and why it is interesting, and the conjecture would be neither
stronger nor weaker if `X` were a bare type.

Wrapping the family in a `Scheme` would therefore assert structure the claims
never consume, which is the same defect in the opposite direction from the
schema this file used to carry: a placeholder asserts too little, decoration
asserts too much. `X` stays an abstract index type, and the sheaf framing lives
in this docstring where a reader can find it.

If a later result actually needs locality — gluing local `ε`s, or a stalkwise
argument — that is the point to introduce the sheaf, and the class statement
below will still be what it restricts to.

## What is encoded

* **Part 1 — local variation.** "`ε(x)` may differ from `ε(y)` for distinct
  `x, y`." Encoded as genuine non-constancy. This is the whole point of the
  conjecture: a *global* `ε` is exactly what the appendix already has, so a
  carrier that permitted a constant family would assert nothing new.
* **Part 2 — standard-part global constant.** "`st(ε(x)) = 0` for all `x`, so
  the classical substrate is `q = 1` everywhere." Encoded as infinitesimality,
  which is the block's own framing (`ε` is a section of the sheaf of
  *infinitesimals*); `standardPart_eq_zero` below derives the `st` form from it
  using the corpus's own `StandardPart` API.
* **Part 3 — birthday-uniform at archimedean scale.** "The leading surreal
  coefficient of `ε(x)` is globally constant and equals `q₀ − 1`." Encoded
  against a caller-supplied `leadingCoeff`, for the reason below.

`leadingCoeff` is the coefficient of `ω⁻¹` in Conway normal form. It does not
exist in this tree, and it is **not** `OmegaOrder.Ow`, which is the leading
*exponent*. Rather than invent it, it enters as a parameter — the same choice as
the `archimedean_agreement` pipelines and `DiophantineBirthday`'s trajectory.
See `Asymptotics.lean` for why the Conway-normal-form machinery is not available
from Mathlib.

`q₀` is a parameter too, not a literal. Writing `0.11` into a carrier would fix a
substrate pin inside a conjecture and require re-editing whenever the pin moves.

## Base ring (§7c)

`K` is a generic `[SurrealField K]`. `ℝ` enters only through `standardPart` and
`leadingCoeff`'s codomain — the archimedean shadow the conjecture is *about* —
and through `SurrealField`'s own `ofReal`. No numerical substrate value appears.
-/

namespace QOU.AppendixSurreals

open SurrealField

universe u v

/-- **The substrate parameter is a local infinitesimal field.**

The conjecture of
[`conj:local-infinitesimal-field`](../../../appendix-surreals/local-infinitesimal-field.md):
`q(x) = 1 + ε(x)` fluctuates from point to point, every fluctuation is
infinitesimal, and the leading surreal coefficient is nevertheless globally
constant.

Parameters are the caller's data:

* `X` — the index type of points (the block's scheme, taken extensionally;
  see the header);
* `ε x` — the local infinitesimal at `x`;
* `leadingCoeff` — the `ω⁻¹` coefficient in Conway normal form, which this tree
  does not construct;
* `q₀` — the archimedean substrate value, a parameter rather than a literal.

An instance **is** the conjecture, for that data. None is provided. -/
class LocalInfinitesimalField (X : Type v) (K : Type u) [SurrealField K]
    (ε : X → K) (leadingCoeff : K → ℝ) (q₀ : ℝ) : Prop where
  /-- **Part 2.** Every local value is infinitesimal, so the classical
      substrate is `q = 1` at every point. -/
  infinitesimal : ∀ x : X, IsInfinitesimal (ε x)
  /-- **Part 1 — local variation.** The family is genuinely non-constant.
      Without this the conjecture collapses to the global `ε` the appendix
      already has, so a carrier permitting a constant family would assert
      nothing new. -/
  local_variation : ∃ x y : X, ε x ≠ ε y
  /-- **Part 3.** The leading `ω⁻¹` coefficient is globally constant and equals
      the archimedean substrate deviation. -/
  leadingCoeff_const : ∀ x : X, leadingCoeff (ε x) = q₀ - 1

-- **No instance is provided — that is the honest open state** (AGENTS.md
-- §3b-tax).  History: this file previously carried
--     axiom conj_local_infinitesimal_field : LocalInfinitesimalField
--     noncomputable instance : LocalInfinitesimalField := conj_local_infinitesimal_field
-- i.e. the conjecture was asserted by `axiom` and installed as a global
-- instance, so every downstream `[LocalInfinitesimalField]` resolved for free
-- and the assumption was invisible outside `#print axioms`.  Removed, not
-- completed.  The field schema is now content-bearing as well; see the header.
--
-- Note for `qou-ffwk`'s inventory: that bean greps for the old vanishing
-- field's name, which is deliberately written nowhere in this file — not even
-- in this history — so the file drops out of the grep instead of matching it
-- forever from its own changelog.

namespace LocalInfinitesimalField

variable {X : Type v} {K : Type u} [SurrealField K]
  {ε : X → K} {leadingCoeff : K → ℝ} {q₀ : ℝ}

/-- **The classical substrate is `q = 1` everywhere** — the block's part 2 in
its own `st` form, derived rather than assumed.

The class states infinitesimality, which is the block's framing (`ε` is a
section of the sheaf of *infinitesimals*); this is the consequence the block
actually spells out. Uses the corpus's own `standardPart_of_infinitesimal`. -/
theorem standardPart_eq_zero [h : LocalInfinitesimalField X K ε leadingCoeff q₀]
    (x : X) : standardPart (ε x) = 0 :=
  standardPart_of_infinitesimal (h.infinitesimal x)

/-- **The archimedean shadow really is constant**, across every pair of points —
the sense in which the fluctuation is invisible classically. -/
theorem standardPart_const [LocalInfinitesimalField X K ε leadingCoeff q₀]
    (x y : X) : standardPart (ε x) = standardPart (ε y) := by
  rw [standardPart_eq_zero (leadingCoeff := leadingCoeff) (q₀ := q₀) x,
      standardPart_eq_zero (leadingCoeff := leadingCoeff) (q₀ := q₀) y]

/-- **The leading coefficient agrees across points** — part 3 in the form the
block states it ("globally constant"), rather than pinned to `q₀ − 1`. -/
theorem leadingCoeff_eq [h : LocalInfinitesimalField X K ε leadingCoeff q₀]
    (x y : X) : leadingCoeff (ε x) = leadingCoeff (ε y) := by
  rw [h.leadingCoeff_const x, h.leadingCoeff_const y]

/-! ### Inhabitation depends on the data

Not an `instance`, so typeclass resolution cannot pick it up and silently close
a downstream hypothesis. -/

/-- **Refuted over a one-point index** — the property the old schema lacked
entirely.

`local_variation` cannot hold when there is nowhere to vary, so the conjecture
is genuinely falsifiable by the shape of `X` alone. Under the previous schema
`⟨0, rfl⟩` closed the class for every choice of everything, including a
one-point scheme, so "the substrate fluctuates" had nothing to fail against.

This is also the precise sense in which the conjecture says more than the
appendix's existing global `ε`. -/
theorem not_of_subsingleton [Subsingleton X]
    (ε : X → K) (leadingCoeff : K → ℝ) (q₀ : ℝ) :
    ¬ LocalInfinitesimalField X K ε leadingCoeff q₀ := by
  rintro ⟨-, ⟨x, y, hxy⟩, -⟩
  exact hxy (congrArg ε (Subsingleton.elim x y))

/-- **Distinct witness points exist**: any index type carrying a
    `LocalInfinitesimalField` contains at least two distinct points `x ≠ y`. -/
theorem exists_distinct_points [h : LocalInfinitesimalField X K ε leadingCoeff q₀] :
    ∃ x y : X, x ≠ y := by
  rcases h.local_variation with ⟨x, y, hxy⟩
  exact ⟨x, y, fun heq => hxy (congrArg ε heq)⟩

/-- **Pairwise fluctuations are infinitesimal**: for any two points `x, y : X`,
    the difference `ε x - ε y` is infinitesimal in `K`. -/
theorem sub_infinitesimal [h : LocalInfinitesimalField X K ε leadingCoeff q₀]
    (x y : X) : IsInfinitesimal (ε x - ε y) := by
  rw [sub_eq_add_neg]
  exact (h.infinitesimal x).add (h.infinitesimal y).neg

/-- **No constant surreal represents the local infinitesimal field**:
    for every `c : K`, `ε` is not identically equal to `c`. -/
theorem not_forall_eq_const [h : LocalInfinitesimalField X K ε leadingCoeff q₀]
    (c : K) : ¬ (∀ x : X, ε x = c) := by
  intro hconst
  rcases h.local_variation with ⟨x, y, hxy⟩
  exact hxy (by rw [hconst x, hconst y])

end LocalInfinitesimalField

end QOU.AppendixSurreals
