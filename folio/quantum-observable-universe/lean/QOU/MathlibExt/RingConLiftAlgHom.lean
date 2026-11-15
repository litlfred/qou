/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.RingTheory.Congruence.Basic
import Mathlib.Algebra.Algebra.Equiv
import Mathlib.Algebra.RingQuot

/-!
# An algebra hom out of a `RingCon` quotient — the first-isomorphism lift Mathlib lacks

## The gap, measured against the pinned Mathlib

`Mathlib/GroupTheory/Congruence/Basic.lean` has `Con.lift`, for **monoid** congruences.
There is no ring analogue: `Mathlib/RingTheory/Congruence/` has no `lift`, and
`Mathlib/RingTheory/TwoSidedIdeal/` carries `ker`, `mem_ker` and `ker_eq_bot` and **no**
`lift` or `quotientKerEquivOfSurjective`.  So the two halves of the first isomorphism
theorem can be in hand — a surjection and an identification of its kernel with the
congruence — and there is still no way to turn them into an `≃ₐ`.

This file supplies the missing map, over a generic `CommRing R`.

## Why it lives here rather than beside its application

Split out of `QOU.SchurWeyl.WtraceRadicalQuotient` under §7c: that file mixes this generic
content with an `ℝ`-only application, and `scripts/check-sidecars.sh` flags the mix.  Nothing
here mentions `ℝ`, needs an ordering, or takes a square root.

## 🛑 `traceQuotEquiv` does NOT go through this file

Stated here as well as there, because the temptation to assume otherwise is exactly what a
reader does with a general-purpose lemma sitting next to its apparent use.
`WtraceRadicalQuotient.twoRowQuotHom` is **inlined** against the corpus's own algebra
instances, because two `Algebra ℝ` instances on the quotient type do not unify (Mathlib's
`RingCon.instAlgebraQuotient` against the corpus's
`QBeta.MarkovTraceQuotient.instAlgebraTraceQuot`).  So this is the general-purpose piece —
the one that would go upstream — and it is **not** on that result's critical path.

-- Ref: [leitner2026] bean qou-8iru.
-/

namespace QOU.MathlibExt.RingConLiftAlgHom

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
variable {B : Type*} [Ring B] [Algebra R B]

/-- **An algebra hom out of a `RingCon` quotient.**  The ring-theoretic analogue of
Mathlib's `Con.lift`, which exists only for monoid congruences. -/
def liftAlgHom (c : RingCon A) (f : A →ₐ[R] B) (H : ∀ x y : A, c x y → f x = f y) :
    c.Quotient →ₐ[R] B where
  toFun := Quotient.lift (⇑f) H
  map_one' := map_one f
  map_mul' := by rintro ⟨a⟩ ⟨b⟩; exact map_mul f a b
  map_zero' := map_zero f
  map_add' := by rintro ⟨a⟩ ⟨b⟩; exact map_add f a b
  commutes' r := f.commutes r

@[simp] theorem liftAlgHom_coe (c : RingCon A) (f : A →ₐ[R] B)
    (H : ∀ x y : A, c x y → f x = f y) (a : A) :
    liftAlgHom c f H (a : c.Quotient) = f a := rfl

@[simp] theorem liftAlgHom_mk (c : RingCon A) (f : A →ₐ[R] B)
    (H : ∀ x y : A, c x y → f x = f y) (a : A) :
    liftAlgHom c f H (c.mk' a) = f a := rfl

/-- The lift is **injective** exactly when the congruence is the whole kernel. -/
theorem liftAlgHom_injective (c : RingCon A) (f : A →ₐ[R] B)
    (H : ∀ x y : A, c x y → f x = f y) (Hconv : ∀ x y : A, f x = f y → c x y) :
    Function.Injective (liftAlgHom c f H) := by
  rintro ⟨a⟩ ⟨b⟩ hab
  have h : f a = f b := hab
  exact Quotient.sound (Hconv a b h)

end QOU.MathlibExt.RingConLiftAlgHom
