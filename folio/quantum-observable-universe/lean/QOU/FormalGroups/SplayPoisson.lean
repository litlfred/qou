/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.LinearAlgebra.FreeProduct.Basic

/-!
# Poisson structures on splays

This file formalises §1 of F. Leitner, *Non-Commutative Formal Groups in Positive
Characteristic*, arXiv:math/0602138 (`library/arxiv-math-0602138v1`). The paper is the
owner's source for the skewed-Poisson material cited as `[fred2005]`.

What is formalised, by paper reference:

* §1, before Def. 1.1: a *Poisson structure* on an algebra `A` is "a skew-symmetric
  bi-derivation `π` which satisfies the Jacobi identity" (`PoissonStructure`).
* Def. 1.1.1: the *splay* of a family of commutative algebras `Aᵢ`, whose splay algebra is
  their coproduct `∐ᵢ Aᵢ` in the category of algebras. Mathlib's free product
  `LinearAlgebra.FreeProduct R A` is that coproduct (`SplayAlgebra`).
* Def. 1.1.3: internal symmetry `π(Aᵢ, Aᵢ) = 0`, and a Poisson structure *on a splay* is a
  Poisson structure on the splay algebra with internal symmetry (`SplayPoisson`).
* Def. 1.1.4: Poisson morphisms (`IsPoissonMorphism`).
* Def. 1.1.5: vanishing on constants. The paper *assumes* this for every Poisson structure;
  here it is proved to follow from the derivation law (`PoissonStructure.vanishesOnConstants`).
* Def. 1.1.6: strongly filtered (`StronglyFiltered`).
* Example 1.2: the commutator `π_c(a, b) = ab − ba` is a Poisson structure, and it vanishes
  exactly when `A` is commutative (`commutatorPoisson`, `commutatorPoisson_eq_zero_iff`).
  By Rmk. 2.3.1 of the paper, the bracket on `Dist(G)` used in §3 is this commutator.

Not formalised here: strong multiplicativity (Def. 1.11, which needs the symmetrised product
`· : T ⊗ T → T` through `S X`), the PBW theorem 1.9 and the main Theorem 3.7.
-/

namespace QOU.FormalGroups

open LinearAlgebra

section Poisson

variable (R : Type*) [CommRing R] (A : Type*) [Ring A] [Algebra R A]

/-- A Poisson structure on an `R`-algebra `A` (arXiv:math/0602138, §1, before Def. 1.1): a
skew-symmetric `R`-bilinear bi-derivation satisfying the Jacobi identity. `A` need not be
commutative, so each derivation law keeps the order of the factors. -/
structure PoissonStructure where
  /-- The bracket `π`, as an `R`-bilinear map. -/
  bracket : A →ₗ[R] A →ₗ[R] A
  /-- Skew-symmetry. -/
  skew : ∀ a b, bracket a b = -bracket b a
  /-- Derivation in the first argument. -/
  leibniz_left : ∀ a b c, bracket (a * b) c = a * bracket b c + bracket a c * b
  /-- Derivation in the second argument. -/
  leibniz_right : ∀ a b c, bracket a (b * c) = b * bracket a c + bracket a b * c
  /-- The Jacobi identity. -/
  jacobi : ∀ a b c,
    bracket a (bracket b c) + bracket b (bracket c a) + bracket c (bracket a b) = 0

variable {R A}

namespace PoissonStructure

/-- Given skew-symmetry, the second derivation law follows from the first. So the two
readings of "bi-derivation" (derivation in each argument, or in the first plus skew) agree. -/
theorem leibniz_right_of_left (π : A →ₗ[R] A →ₗ[R] A) (hskew : ∀ a b, π a b = -π b a)
    (hl : ∀ a b c, π (a * b) c = a * π b c + π a c * b) (a b c : A) :
    π a (b * c) = b * π a c + π a b * c := by
  rw [hskew, hl, hskew c a, hskew b a]
  noncomm_ring

/-- Def. 1.1.5 of arXiv:math/0602138: `π` vanishes on constants if `π(1, a) = 0 = π(a, 1)`
for every `a`. -/
def VanishesOnConstants (π : PoissonStructure R A) : Prop :=
  ∀ a : A, π.bracket 1 a = 0 ∧ π.bracket a 1 = 0

/-- Every Poisson structure vanishes on constants. The paper assumes this ("We will assume
for the remainder of this paper that all Poisson structures vanish on constants"); it
follows from the derivation law, since `π(1, a) = π(1 · 1, a) = 2 π(1, a)`. -/
theorem vanishesOnConstants (π : PoissonStructure R A) : π.VanishesOnConstants := by
  intro a
  have h1 : π.bracket 1 a = 0 := by
    have h := π.leibniz_left 1 1 a
    simp only [mul_one, one_mul] at h
    exact left_eq_add.mp h
  refine ⟨h1, ?_⟩
  rw [π.skew, h1, neg_zero]

/-- Def. 1.1.3 of arXiv:math/0602138: `π` has internal symmetry with respect to a family of
subalgebras `Sᵢ` if `π(Sᵢ, Sᵢ) = 0` for each `i`. -/
def HasInternalSymmetry {ι : Type*} (π : PoissonStructure R A) (S : ι → Subalgebra R A) :
    Prop :=
  ∀ i, ∀ x ∈ S i, ∀ y ∈ S i, π.bracket x y = 0

/-- The filtration index `A(k)` extended to all `k : ℤ` by `A(k) = 0` for `k < 0`. The paper
writes `A = ⋃_{n ≥ 0} A(n)` and uses `A(m+n−1)`; this records the reading `A(−1) = 0`. -/
def filtrationZ (F : ℕ → Submodule R A) (k : ℤ) : Submodule R A :=
  if k < 0 then ⊥ else F k.toNat

/-- Def. 1.1.6 of arXiv:math/0602138: for a filtration `A = ⋃ₙ A(n)`, `π` is strongly
filtered if `π(A(m), A(n)) ⊆ A(m+n−1)`. -/
def StronglyFiltered (π : PoissonStructure R A) (F : ℕ → Submodule R A) : Prop :=
  ∀ m n : ℕ, ∀ x ∈ F m, ∀ y ∈ F n,
    π.bracket x y ∈ filtrationZ F ((m : ℤ) + n - 1)

end PoissonStructure

/-- Def. 1.1.4 of arXiv:math/0602138: an algebra map `Φ` is a Poisson morphism from `π` to
`π'` if `Φ ∘ π = π' ∘ (Φ ⊗ Φ)`. -/
def IsPoissonMorphism {B : Type*} [Ring B] [Algebra R B] (π : PoissonStructure R A)
    (π' : PoissonStructure R B) (Φ : A →ₐ[R] B) : Prop :=
  ∀ a b, Φ (π.bracket a b) = π'.bracket (Φ a) (Φ b)

/-! ### Example 1.2: the commutator -/

variable (R A)

/-- The commutator bracket `π_c(a, b) = ab − ba` as an `R`-bilinear map. -/
def commutatorBracket : A →ₗ[R] A →ₗ[R] A :=
  LinearMap.mul R A - (LinearMap.mul R A).flip

@[simp]
theorem commutatorBracket_apply (a b : A) : commutatorBracket R A a b = a * b - b * a := by
  simp [commutatorBracket]

/-- Example 1.2 of arXiv:math/0602138: the commutator `π_c(a, b) = ab − ba` is a Poisson
structure on any algebra; skew-symmetry, both derivation laws and Jacobi follow from
associativity. -/
def commutatorPoisson : PoissonStructure R A where
  bracket := commutatorBracket R A
  skew a b := by simp
  leibniz_left a b c := by simp only [commutatorBracket_apply]; noncomm_ring
  leibniz_right a b c := by simp only [commutatorBracket_apply]; noncomm_ring
  jacobi a b c := by simp only [commutatorBracket_apply]; noncomm_ring

/-- Example 1.2 of arXiv:math/0602138: `π_c` vanishes if and only if `A` is commutative, so
`π_c` measures the non-commutativity of `A`. -/
theorem commutatorPoisson_eq_zero_iff :
    (∀ a b : A, (commutatorPoisson R A).bracket a b = 0) ↔ ∀ a b : A, a * b = b * a := by
  simp [commutatorPoisson, sub_eq_zero]

end Poisson

/-! ### Splays (Def. 1.1.1, 1.1.3) -/

section Splay

variable (R : Type*) [CommRing R] {I : Type*} [DecidableEq I]
  (A : I → Type*) [∀ i, CommRing (A i)] [∀ i, Algebra R (A i)]

/-- Def. 1.1.1 of arXiv:math/0602138: the splay algebra of commutative algebras `Aᵢ` is their
coproduct `∐ᵢ Aᵢ` in the category of `R`-algebras, i.e. their free product. -/
abbrev SplayAlgebra : Type _ := FreeProduct R A

/-- The coordinate algebra `Aᵢ` as a subalgebra of the splay algebra (the image of `ιᵢ`). -/
def coordinateSubalgebra (i : I) : Subalgebra R (SplayAlgebra R A) :=
  (FreeProduct.ι R A i).range

/-- Def. 1.1.3 of arXiv:math/0602138: a Poisson structure on the splay `T` of the `Aᵢ` is a
Poisson structure on the splay algebra with internal symmetry with respect to the `Aᵢ`. -/
structure SplayPoisson where
  /-- The underlying Poisson structure on the splay algebra. -/
  toPoissonStructure : PoissonStructure R (SplayAlgebra R A)
  /-- Internal symmetry: `π(Aᵢ, Aᵢ) = 0`. -/
  internal : toPoissonStructure.HasInternalSymmetry (coordinateSubalgebra R A)

/-- Internal symmetry stated on the coordinate maps: `π(ιᵢ a, ιᵢ b) = 0`. -/
theorem SplayPoisson.bracket_ι_ι (π : SplayPoisson R A) (i : I) (a b : A i) :
    π.toPoissonStructure.bracket (FreeProduct.ι R A i a) (FreeProduct.ι R A i b) = 0 :=
  π.internal i _ ⟨a, rfl⟩ _ ⟨b, rfl⟩

/-- The commutator bracket on the splay algebra has internal symmetry, because each `Aᵢ` is
commutative and `ιᵢ` is an algebra map. So `π_c` is a Poisson structure on the splay. -/
def commutatorSplayPoisson : SplayPoisson R A where
  toPoissonStructure := commutatorPoisson R (SplayAlgebra R A)
  internal := by
    rintro i _ ⟨a, rfl⟩ _ ⟨b, rfl⟩
    simp only [commutatorPoisson, commutatorBracket_apply]
    rw [← map_mul, ← map_mul, mul_comm, sub_self]

end Splay

end QOU.FormalGroups
