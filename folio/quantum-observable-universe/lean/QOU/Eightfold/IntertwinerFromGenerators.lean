/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Algebra.Group.Subgroup.Basic
import Mathlib.GroupTheory.QuotientGroup.Defs

/-!
# An intertwining verified on generators holds everywhere

When two representations are compared up to conjugacy, one is tempted to verify the
comparison by SAMPLING: evaluate both sides on many group elements and see whether they
agree.  A sample can only ever corroborate, and enlarging it does not change that -- so
the question becomes how large a sample suffices, and one starts looking for a bound on
word length.

**That is the wrong instrument, and this file is why.**  Conjugation by a fixed element is
itself a homomorphism, so `x ↦ A · ρ₁ x · A⁻¹` and `ρ₂` are two homomorphisms; two
homomorphisms agreeing on a GENERATING SET are equal.  The verification is therefore
finite at word length one, and the conclusion is equality on the whole group rather than
agreement on a sample.  No character theory, no irreducibility, no trace algebra and no
word-length bound enters.

`twist_trivial_of_mem` is the companion step: a twist by a homomorphism landing in a
normal subgroup `N` is invisible in `H ⧸ N`.  Applied with `N` the scalars of a matrix
group, a scalar-valued twist disappears in the projective quotient, which is what lets an
intertwining "up to a scalar character" be an honest isomorphism projectively.

Both are stated for an arbitrary group; nothing here refers to matrices, fields or
representations.
-/

namespace QOU.Eightfold.IntertwinerFromGenerators

variable {G H : Type*} [Group G] [Group H]

/-- **Two homomorphisms agreeing on a generating set are equal.**  This is the reason a
verification on generators is a proof and not a sample. -/
theorem eqOn_of_eqOn_generators (f g : G →* H) {S : Set G}
    (hS : Subgroup.closure S = ⊤) (h : ∀ s ∈ S, f s = g s) (x : G) : f x = g x := by
  have hx : x ∈ Subgroup.closure S := by rw [hS]; exact Subgroup.mem_top x
  induction hx using Subgroup.closure_induction with
  | mem s hs => exact h s hs
  | one => simp
  | mul a b _ _ ha hb => simp [ha, hb]
  | inv a _ ha => simp [ha]

/-- Conjugation by a fixed element, packaged as a homomorphism, so that
`eqOn_of_eqOn_generators` applies to it. -/
@[simps]
def conjHom (A : H) (f : G →* H) : G →* H where
  toFun x := A * f x * A⁻¹
  map_one' := by simp
  map_mul' x y := by
    simp only [map_mul]
    simp [mul_assoc]

/-- **The word-length bound for verifying an intertwining is one.**  If a single `A`
conjugates `ρ₁` to `ρ₂` on a generating set, it does so on every element of the group.

This is what makes a finite check a proof: the conclusion is an identity on all of `G`,
not agreement on the elements tested. -/
theorem conj_eq_of_eqOn_generators (ρ₁ ρ₂ : G →* H) (A : H) {S : Set G}
    (hS : Subgroup.closure S = ⊤) (h : ∀ s ∈ S, A * ρ₁ s * A⁻¹ = ρ₂ s) (x : G) :
    A * ρ₁ x * A⁻¹ = ρ₂ x :=
  eqOn_of_eqOn_generators (conjHom A ρ₁) ρ₂ hS h x

/-- **A twist by a homomorphism into `N` is invisible in `H ⧸ N`.**  With `N` the scalars
of a matrix group, a scalar-valued character twist vanishes projectively -- so an
intertwining that holds only up to such a twist is an honest isomorphism there. -/
theorem twist_trivial_of_mem (ρ lam : G →* H) (N : Subgroup H) [N.Normal]
    (hlam : ∀ x, lam x ∈ N) (x : G) :
    (QuotientGroup.mk (lam x * ρ x) : H ⧸ N) = QuotientGroup.mk (ρ x) := by
  rw [QuotientGroup.eq]
  have h : (ρ x)⁻¹ * (lam x)⁻¹ * ((ρ x)⁻¹)⁻¹ ∈ N :=
    ‹N.Normal›.conj_mem _ (N.inv_mem (hlam x)) (ρ x)⁻¹
  simpa [mul_inv_rev, mul_assoc] using h

end QOU.Eightfold.IntertwinerFromGenerators
