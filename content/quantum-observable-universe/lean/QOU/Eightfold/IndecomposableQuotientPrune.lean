import Mathlib.Algebra.Module.Submodule.Basic
import Mathlib.LinearAlgebra.Span.Basic
import Mathlib.Tactic

/-!
# Products of degree-1 elements vanish in the indecomposable quotient

**Bean `qou-ox7v`, settled — and it kills route B (`qou-wnhk`) of epic
`qou-2q85`.**

## The question this settles

Route B proposed: build a depth-1 stratum `ℋ_q^(1,K)`, then use the
depth-additivity of the `q`-shuffle (`ℋ_q^(n₁) *_q ℋ_q^(n₂) ⊆ ℋ_q^(n₁+n₂)`) to
**square** it into `ℋ_q^(2,K)`, where the hyperbolic volume lives.

I then raised a worry (roast R1) that the shuffle filtration and the K-theory
weight tower "cannot match as graded algebras", on a rank count. **That worry
was wrong and is retracted.** They match. The mismatch was mine: I compared the
whole weight-2 graded piece against `K_3^ind`, which is only one summand of it.

The corpus states the resolution itself, at
`appendix-surreals/k-theory-period-rosetta.md:22`:

> `K_*^ind` denotes the indecomposable part of higher K-theory, **modulo the
> image of products of lower K-groups**.

So the weight-2 piece splits into a **decomposable** part — products of weight-1
elements, `log · log` — and an **indecomposable** part, which is what
`K_3^ind`, hence Bloch–Wigner, hence the volume, *is*.

**The shuffle-square of a depth-1 object lands in the decomposable part, which
is exactly what the indecomposable quotient discards.** Route B cannot reach the
volume by squaring — not because the gradings disagree, but because squaring
produces precisely the summand the target is defined to exclude.

## What is proved here

The invariant behind that sentence, in the generality it actually holds: for any
bilinear `mul : A₁ →ₗ A₁ →ₗ A₂`, every product `mul a b` dies in
`A₂ ⧸ decomposable mul`. Nothing about knots, periods or `q` is used — which is
the point. The obstruction is not special to this corpus; it is what
"indecomposable" means.

## Scope

**(b), a structural exclusion**, with the invariant exhibited rather than
asserted — but the exclusion is of **squaring as a route to an indecomposable
target**, not of route B's ingredients. Building `ℋ_q^(1,K)` may still be worth
doing for its own sake; what is excluded is reaching the volume from it by
multiplication.

It says nothing about the **coproduct** route (A, `qou-jopk`): `Δ_q`'s `2 = 2+0`
split is not a product of two degree-1 elements, so this theorem does not touch
it.

-- Ref: [manuscript] bean `qou-ox7v`, epic `qou-2q85`
-- Ref: [manuscript] `appendix-surreals/k-theory-period-rosetta.md` (the `ind` gloss)
-/

namespace QOU.Eightfold.IndecomposableQuotient

variable {R : Type*} [CommRing R]
variable {A₁ A₂ : Type*} [AddCommGroup A₁] [AddCommGroup A₂] [Module R A₁] [Module R A₂]

/-- The **decomposable** submodule of the degree-2 piece: the span of all
products of two degree-1 elements. This is the object the `ind` qualifier
quotients by. -/
def decomposable (mul : A₁ →ₗ[R] A₁ →ₗ[R] A₂) : Submodule R A₂ :=
  Submodule.span R {x : A₂ | ∃ a b : A₁, mul a b = x}

/-- Every product of two degree-1 elements is decomposable. -/
theorem mul_mem_decomposable (mul : A₁ →ₗ[R] A₁ →ₗ[R] A₂) (a b : A₁) :
    mul a b ∈ decomposable mul :=
  Submodule.subset_span ⟨a, b, rfl⟩

/-- **The prune.** In the indecomposable quotient `A₂ ⧸ decomposable`, every
product of two degree-1 elements is **zero**.

Read on the corpus's dictionary: a shuffle-square of depth-1 elements is zero in
the part of weight 2 that `K_3^ind` — and hence the hyperbolic volume — lives
in. Squaring cannot reach an indecomposable target. -/
theorem mkQ_mul_eq_zero (mul : A₁ →ₗ[R] A₁ →ₗ[R] A₂) (a b : A₁) :
    (decomposable mul).mkQ (mul a b) = 0 :=
  (Submodule.Quotient.mk_eq_zero _).mpr (mul_mem_decomposable mul a b)

/-- The same for an arbitrary element of the decomposable part: the whole image
of the multiplication is killed, not just its generators. -/
theorem mkQ_eq_zero_of_mem_decomposable (mul : A₁ →ₗ[R] A₁ →ₗ[R] A₂) {x : A₂}
    (hx : x ∈ decomposable mul) : (decomposable mul).mkQ x = 0 :=
  (Submodule.Quotient.mk_eq_zero _).mpr hx

/-- **Non-vacuity.** The prune is not true merely because the quotient collapses:
for the zero multiplication the decomposable part is `⊥`, so the quotient is all
of `A₂` and is nontrivial whenever `A₂` is. The theorem therefore has content
about *which* elements die, not about everything dying. -/
theorem decomposable_zero_eq_bot :
    decomposable (0 : A₁ →ₗ[R] A₁ →ₗ[R] A₂) = ⊥ := by
  apply le_antisymm _ bot_le
  rw [decomposable, Submodule.span_le]
  rintro x ⟨a, b, rfl⟩
  simp

end QOU.Eightfold.IndecomposableQuotient
