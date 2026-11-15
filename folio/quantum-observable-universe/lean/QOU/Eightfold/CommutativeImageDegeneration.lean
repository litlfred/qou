import Mathlib.Algebra.Ring.Defs
import Mathlib.RingTheory.Ideal.Span
import Mathlib.Tactic

/-!
# The `H₃(q)` operator basis degenerates in any commutative image

**Bean `qou-yb2b`, the degenerate branch.** The owner's question was whether
the knot-as-operator action extends across the knot complement, *"or show that
they degenerate there"*. This file settles the second disjunct, and it does so
with no topology at all — which is the point.

## What is being asked, and why this answers it algebraically

`fundamental-knots-operator-basis.md` gives the interaction operators as a
**six**-element Gröbner–Shirshov basis of `H₃(q)`: `1`, `σ₀`, `σ₁`, `L₊ = σ₀σ₁`,
`L₋ = σ₁σ₀`, `e⁻ = σ₀σ₁σ₀`. The whole particle catalogue is carried by the fact
that these six are *distinct*.

Now suppose the operator action lands on a piece whose invariant is **free of
rank 1** over the ground ring — a skein module that collapses to the ground
ring, the case for a simply-connected piece. An action on a rank-1 free module
is an algebra map into `End_R(R) ≅ R`, which is **commutative**. So the question
"does the action degenerate on the exceptional divisor?" reduces to: *what is
the image of `H₃(q)` in a commutative ring?*

The answer proved below is that it collapses hard, in two independent steps:

* **`braid_forces_eq`** — the braid relation `σ₀σ₁σ₀ = σ₁σ₀σ₁` in a commutative
  target says `s₀s₁(s₀ − s₁) = 0`, and the Hecke quadratic makes each `sᵢ` a
  **unit**, so `s₀ = s₁`. The two generators become the same element.
* **`image_le_span_one_s`** — the Hecke quadratic `s² = (q − q⁻¹)s + 1` then
  puts every one of the six basis images in `span R {1, s}`.

So a **six**-dimensional operator algebra has an image of dimension **at most
two**, and `σ₀ = σ₁`, `L₊ = L₋ = s²`, `e⁻ = s³`. The distinctions the particle
catalogue rests on are not merely hard to see there — they are gone.

## Scope, stated precisely

This is an **algebraic** theorem about commutative images. It becomes a
statement about the exceptional divisor only via the premise *"the invariant
there is free of rank 1"*, which is **not proved here and is not assumed
anywhere below** — no theorem in this file mentions a manifold, a skein module
or a divisor. What the file supplies is the invariant that a formalize-first
pass owes before any search: **if** the rank-1 premise holds, the extension
question is settled negatively and no amount of machinery recovers the six
operators. Establishing the premise is the open half (`qou-yb2b`).

Note also that this is a **scope-(a)** result in the AGENTS.md sense for the
extension programme as a whole: it excludes rank-1 targets, not the extension.
A target of rank ≥ 2 is untouched by everything here.

-- Ref: [leitner2026] `braids-and-knots/fundamental-knots-operator-basis.md`
-- Ref: [leitner2026] bean `qou-yb2b` (the sewing / degeneration question)
-/

namespace QOU.Eightfold

variable {R : Type*} [CommRing R]

/-- The Hecke quadratic relation in the form `s² = (q − q⁻¹)·s + 1`, carrying
the inverse as an explicit element `qi` so the statement lives over a plain
`CommRing` (AGENTS.md §7c: no gratuitous field or `ℝ`). -/
def HeckeQuad (q qi s : R) : Prop := s * s = (q - qi) * s + 1

/-- **Every Hecke generator is a unit.** Immediate from the quadratic:
`s * (s - (q - qi)) = 1`. This is what makes the cancellation in
`braid_forces_eq` legitimate without any domain hypothesis. -/
theorem isUnit_of_heckeQuad {q qi s : R} (h : HeckeQuad q qi s) : IsUnit s :=
  isUnit_of_mul_eq_one s (s - (q - qi)) <| by
    have h' : s * s = (q - qi) * s + 1 := h
    linear_combination h'

/-- The Hecke quadratic in factored form: `(s - q) * (s + qi) = 0`, given
`q * qi = 1`. Valid over any `CommRing` — the *disjunction* `s = q ∨ s = -qi`
needs a domain and is `eq_or_eq_of_heckeQuad` below. -/
theorem heckeQuad_factor {q qi s : R} (hq : q * qi = 1) (h : HeckeQuad q qi s) :
    (s - q) * (s + qi) = 0 := by
  have hs : s * s = (q - qi) * s + 1 := h
  linear_combination hs - hq

/-- **Two eigenvalues, in a domain.** The classical statement: a Hecke
generator acts by `q` or by `-q⁻¹` — the symmetric and antisymmetric channels
of AGENTS.md §7a. -/
theorem eq_or_eq_of_heckeQuad [IsDomain R] {q qi s : R} (hq : q * qi = 1)
    (h : HeckeQuad q qi s) : s = q ∨ s = -qi := by
  rcases mul_eq_zero.mp (heckeQuad_factor hq h) with h' | h'
  · exact Or.inl (by linear_combination h')
  · exact Or.inr (by linear_combination h')

/-- **The braid relation collapses the two generators.**

In a commutative target the braid relation `σ₀σ₁σ₀ = σ₁σ₀σ₁` reads
`s₀²s₁ = s₁²s₀`, i.e. `s₀s₁(s₀ − s₁) = 0`; both factors are units by
`isUnit_of_heckeQuad`, so `s₀ = s₁`.

This is the first half of the degeneration, and it needs **only** the braid
relation plus the quadratic — no eigenvalue case split, no domain, no
conjugacy argument. -/
theorem braid_forces_eq {q qi s₀ s₁ : R}
    (h₀ : HeckeQuad q qi s₀) (h₁ : HeckeQuad q qi s₁)
    (hbraid : s₀ * s₁ * s₀ = s₁ * s₀ * s₁) : s₀ = s₁ := by
  have hu : IsUnit (s₀ * s₁) := (isUnit_of_heckeQuad h₀).mul (isUnit_of_heckeQuad h₁)
  have key : s₀ * s₁ * (s₀ - s₁) = 0 := by linear_combination hbraid
  have hz := hu.mul_right_eq_zero.mp key
  linear_combination hz

/-! ## The six basis images

With `s₀ = s₁ = s`, the six Gröbner–Shirshov normal forms become
`1, s, s, s·s, s·s, s·s·s`. Each lies in the span of `{1, s}`, by repeated use
of the quadratic. -/

/-- `s²` lies in `span R {1, s}` — directly the quadratic. -/
theorem sq_mem_span {q qi s : R} (h : HeckeQuad q qi s) :
    s * s ∈ Ideal.span ({1, s} : Set R) := by
  have hs : s * s = (q - qi) * s + 1 * 1 := by rw [h]; ring
  rw [hs]
  exact Ideal.add_mem _
    (Ideal.mul_mem_left _ _ (Ideal.subset_span (by simp)))
    (Ideal.mul_mem_left _ _ (Ideal.subset_span (by simp)))

/-- `s³` lies in `span R {1, s}` too: `s³ = (q − qi)·s² + s`, and `s²` is
already in the span. -/
theorem cube_mem_span {q qi s : R} (h : HeckeQuad q qi s) :
    s * s * s ∈ Ideal.span ({1, s} : Set R) := by
  have h3 : s * s * s = (q - qi) * (s * s) + s := by
    calc s * s * s = ((q - qi) * s + 1) * s := by rw [h]
      _ = (q - qi) * (s * s) + s := by ring
  rw [h3]
  exact Ideal.add_mem _
    (Ideal.mul_mem_left _ _ (sq_mem_span h))
    (Ideal.subset_span (by simp))

/-- **The degeneration theorem.** In any commutative image, all six
Gröbner–Shirshov basis operators of `H₃(q)` — `1`, `σ₀`, `σ₁`, `L₊`, `L₋`,
`e⁻` — lie in `span R {1, s}`, and `σ₀ = σ₁`, `L₊ = L₋`.

A six-dimensional operator algebra with an at-most-two-dimensional image: the
particle catalogue's distinctions do not survive. -/
theorem operator_basis_degenerates {q qi s₀ s₁ : R}
    (h₀ : HeckeQuad q qi s₀) (h₁ : HeckeQuad q qi s₁)
    (hbraid : s₀ * s₁ * s₀ = s₁ * s₀ * s₁) :
    s₀ = s₁ ∧ s₀ * s₁ = s₁ * s₀ ∧
      ((1 : R) ∈ Ideal.span ({1, s₀} : Set R) ∧
       s₀ ∈ Ideal.span ({1, s₀} : Set R) ∧
       s₀ * s₁ ∈ Ideal.span ({1, s₀} : Set R) ∧
       s₀ * s₁ * s₀ ∈ Ideal.span ({1, s₀} : Set R)) := by
  have heq : s₀ = s₁ := braid_forces_eq h₀ h₁ hbraid
  refine ⟨heq, mul_comm _ _, Ideal.subset_span (by simp),
    Ideal.subset_span (by simp), ?_, ?_⟩
  · rw [← heq]; exact sq_mem_span h₀
  · rw [← heq]; exact cube_mem_span h₀

end QOU.Eightfold
