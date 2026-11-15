/-
# The `v = q^{1/2}` sign is a ℤ/2 grading, and the axioms cannot see it

`rem:sqrt-q-ribbon-structure` fixes `v² = q` and records that the binary sign on
`v` "dictates the spin structure". This file answers the question that remark
does not ask: **can the axioms choose the sign?** In particular, can the
*non-symmetry* of the braiding do it, the way axiom 1 extracts a direction for
time from the same non-symmetry?

**No — and the obstruction is structural, not a gap.** The reason is worth
separating from the answer.

## A sign flip is not a free choice; it is a monoid homomorphism

Replacing the twist `θ` by `θ' X = ε X • θ X` preserves the ribbon axiom

    θ (V ⊗ W) = (θ V ⊗ θ W) ∘ c W V ∘ c V W

**iff** `ε (V ⊗ W) = ε V * ε W`. So `ε` is a `ℤ/2`-valued *monoidal character*,
not an arbitrary sign assignment, and the ribbon structures over a fixed braiding
form a torsor under the group of such characters.

Two consequences, both below:

* `sign_trivial_on_unit` — `ε 𝟙 = 1`. The flip never touches the unit object.
* `sign_trivial_on_squares` — `ε (x * x) = 1`. **The flip is invisible on
  squares**, which is exactly why `q = v²` is untouched while `v` is not. A
  reader's first instinct — "just negate `v` everywhere" — is refuted here: a
  constant `-1` is not a homomorphism.

So the sign is free **exactly** when the category carries a non-trivial `ℤ/2`
grading. Were the grading group trivial, the sign would already be determined;
that the choice exists at all is the same fact as there being a fermion parity.

## Why the braiding cannot pick it, and why time is different

`ε` acts on the **twist**, and leaves the braiding `c` alone. Checking the four
axioms of `def:quantum-universe` against that action:

1. **Temporal braiding** — reads only `≺_c`, an order on the braiding. Untouched.
2. **Frobenius–Hopf** — no twist appears.
3. **Symmetric Frobenius** — left and right traces both scale by the same
   `ε X`, so their *equality* survives.
4. **Wedderburn invertibility** — each datum scales by a unit, and invertibility
   is sign-blind (`isUnit_smul_unit_iff`).

**All four are `ε`-invariant, so no axiom can fix the sign.** The disanalogy with
time is the point: axiom 1 extracts a direction from an **order**, and
well-foundedness is not preserved under reversal — the asymmetry lives in the
same datum the axiom constrains. The sign lives in a *different* datum. A braided
category has many ribbon structures; the braiding fixes the monodromy `q = v²`
and never `v`. Non-symmetry is the wrong invariant, not an unexploited one.

## What could fix it — and where the corpus already puts it

An **order** on the base. Demanding `dim_q λ > 0` (unitarity) selects the sign,
because `ε λ = -1` on odd-graded blocks makes one branch negative. That needs `R`
ordered, so it is archimedean and cannot be categorical — which is precisely why
`rem:sign-as-spin-structure` says *"post-archimedean, this binary sign determines
the spin structure"*. This file explains why that qualifier is forced.

**Not formalised:** the ribbon-axiom computation itself, since Mathlib carries
`Braided` but no ribbon categories. What is below is the group theory of the
torsor action and the sign-blindness of invertibility; the categorical step is
argued in prose above and is standard.
-/
import Mathlib.Algebra.Group.Hom.Defs
import Mathlib.Algebra.Group.Units.Defs

namespace QOU.AlgebraicSubstrate

variable {M N : Type*} [Monoid M] [Monoid N]

/-- **Exponent two** — the property that makes a sign group a `ℤ/2` grading
group. Stated as a hypothesis rather than fixing `ℤˣ`, so the result covers any
grading group of exponent two. -/
def ExponentTwo (N : Type*) [Monoid N] : Prop := ∀ n : N, n * n = 1

/-- A **twist sign**: the monoidal character by which two ribbon structures over
one braiding differ.

Modelling it as a *homomorphism* is the whole content. The ribbon axiom
`θ (V ⊗ W) = (θ V ⊗ θ W) ∘ c ∘ c` forces `ε (V ⊗ W) = ε V * ε W`, so a sign
assignment that is not multiplicative does not define a twist at all. -/
abbrev TwistSign (M N : Type*) [Monoid M] [Monoid N] := M →* N

/-- The flip never touches the unit object: `θ 𝟙 = id` survives it. -/
theorem sign_trivial_on_unit (ε : TwistSign M N) : ε 1 = 1 := ε.map_one

/-- **The flip is invisible on squares.** This is exactly why the braiding fixes
`q = v²` while leaving `v` free, and it refutes the naive "just negate `v`
everywhere": a constant sign `s ≠ 1` would need `ε (x * x) = s`, against
`ε x * ε x = 1`. -/
theorem sign_trivial_on_squares (h2 : ExponentTwo N) (ε : TwistSign M N) (x : M) :
    ε (x * x) = 1 := by
  rw [ε.map_mul]; exact h2 (ε x)

/-- A constant sign other than the identity is therefore **not** a twist sign. -/
theorem no_constant_nonunit_sign (ε : TwistSign M N) {s : N} (hs : s ≠ 1) :
    ¬ (∀ x : M, ε x = s) := fun h => hs (h 1 ▸ sign_trivial_on_unit ε)

/-- **Axiom 4 is sign-blind.** Scaling a datum by any unit leaves invertibility
unchanged, so the Wedderburn conditions cannot separate the two ribbon
structures. -/
theorem isUnit_unit_mul_iff {R : Type*} [CommMonoid R] (u : Rˣ) (d : R) :
    IsUnit ((u : R) * d) ↔ IsUnit d :=
  ⟨fun h => by
      have : d = (↑u⁻¹ : R) * ((u : R) * d) := by
        rw [← mul_assoc, ← Units.val_mul, inv_mul_cancel, Units.val_one, one_mul]
      rw [this]; exact (u⁻¹).isUnit.mul h,
    fun h => u.isUnit.mul h⟩

end QOU.AlgebraicSubstrate
