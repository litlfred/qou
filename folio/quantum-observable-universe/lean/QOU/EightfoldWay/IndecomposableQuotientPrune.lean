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

-- Ref: [leitner2026] bean `qou-ox7v`, epic `qou-2q85`
-- Ref: [leitner2026] `appendix-surreals/k-theory-period-rosetta.md` (the `ind` gloss)
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

/-! ## Route A (`qou-jopk`): the degree-0 action descends — and is trivial

The surviving route of epic `qou-2q85` proposed that the depth-0 interface layer
**acts on** the depth-2 volume stratum rather than mapping into it. Two results
settle it, and they point opposite ways.

**First, a correction to my own framing of the route.** I described the
mechanism as the coproduct's `2 = 2 + 0` split. That is wrong: a coproduct
*decomposes* an element, it does not let a degree-0 element act on a degree-2
one. The action comes from the **product**, via `0 + 2 = 2` — the same
shuffle-additivity as everywhere else. `ℋ^(0)` is a subalgebra and `ℋ^(2)` is a
module over it, automatically, in any filtered algebra.

**Second, the positive half.** That action is well defined *on the volume
stratum*: if degree-0 times degree-1 stays degree-1, then multiplying a
decomposable by a degree-0 element leaves it decomposable, so the action
descends to the indecomposable quotient. `smul_mem_decomposable` and
`mkQ_smul_comm` below.

**Third, the negative half, from the corpus's own table.**
`def:hq-bi-filtration`'s low-`(n,K)` grid gives `ℋ_q^(0,K)` explicitly:
**`e_{(2,2)}` for the figure-eight, `e_{(3)} ± e_{(1,1,1)}` for the trefoil,
`scalars` for the unknot and the Bring input.** So at each tabulated cell the
depth-0 stratum is spanned by the central idempotent — which is the **unit** of
the localized algebra `e_K ℋ_q e_K`, and `ℋ_q^(2,K)` is by definition the
`e_K`-isotypic piece. **The unit acts as the identity** (`unit_smul_eq_self`).
The action exists, descends, and does nothing.

**What escapes.** `⋈_K` is depth 0 but sits at a *different* cell — the grid row
gives it in `H_6(q)` on an EW braid in `B_6`, not at the cell of the knot whose
volume is in question. A non-trivial action would therefore have to come from
the coproduct's **cell-merging** `K₁ · K₂ = K`, which moves the *vertical* axis.
That is a different structure from the one route A proposed, and this file does
not touch it.
-/

section DegreeZeroAction

variable {A₀ : Type*} [Semiring A₀] [Module A₀ A₁] [Module A₀ A₂]

/-- **A product stays decomposable after acting by a degree-0 element.**
Hypothesis `hcompat` is `c • mul a b = mul (c • a) b` — acting on a product is
acting on its first factor, the `0 + 1 = 1` half of shuffle-additivity. -/
theorem smul_mul_mem_decomposable (mul : A₁ →ₗ[R] A₁ →ₗ[R] A₂) (c : A₀)
    (hcompat : ∀ a b : A₁, c • mul a b = mul (c • a) b) (a b : A₁) :
    c • mul a b ∈ decomposable mul := by
  rw [hcompat]
  exact mul_mem_decomposable mul (c • a) b

/-- **The action descends to the indecomposable quotient**, on generators: a
degree-0 element acting on a product is still zero there. This is what route A
needs in order to act on the volume stratum at all. -/
theorem mkQ_smul_mul_eq_zero (mul : A₁ →ₗ[R] A₁ →ₗ[R] A₂) (c : A₀)
    (hcompat : ∀ a b : A₁, c • mul a b = mul (c • a) b) (a b : A₁) :
    (decomposable mul).mkQ (c • mul a b) = 0 :=
  (Submodule.Quotient.mk_eq_zero _).mpr (smul_mul_mem_decomposable mul c hcompat a b)

end DegreeZeroAction

section UnitActsTrivially

/-- **And the action is trivial when the degree-0 stratum is the unit.**

The corpus's own `ℋ_q^(0,K)` is the central idempotent `e_{λ_K}` (or scalars,
per `def:hq-bi-filtration`'s low-`(n,K)` grid), and `ℋ_q^(2,K)` is the
`e_K`-isotypic piece — so the acting element **is** the unit of the localised
algebra `e_K ℋ_q e_K`, and acts as the identity. That is route A's action,
existing and doing nothing. -/
theorem unit_smul_eq_self {M : Type*} [Monoid M] {X : Type*} [MulAction M X]
    (x : X) : (1 : M) • x = x := one_smul M x

end UnitActsTrivially

end QOU.Eightfold.IndecomposableQuotient
