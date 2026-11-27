/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under CC BY 4.0 as described in the repository LICENSE.
-/
import QOU.StandardModel.InfinitesimalPureBraid
import QOU.BraidsAndKnots.RationalAssociator.DrinfeldKohno
import Mathlib.Algebra.FreeAlgebra
import Mathlib.Algebra.RingQuot

/-!
# The universal enveloping algebra `U(𝔱ₙ)` of the Drinfeld–Kohno Lie algebra, for every `n`

Bean `qou-bgq9`.  `InfinitesimalPureBraid.lean` states the Drinfeld–Kohno relations as a
predicate `IsInfPureBraid` on a family in a ring.  `RationalAssociator/DrinfeldKohno.lean`
states them on three and four strands (`DK3`, `DK4`), and `UniversalDK.lean` builds a truncated
`U(𝔱₄)`.  This file builds the universal object for every `n` and every commutative ring `R`:

* `UT R n` — the free `R`-algebra on `t_{ij}` (`i < j`) modulo the far and near relations.
  This is `U(𝔱ₙ)`, the associated graded of the group algebra of the pure braid group
  (Kohno's theorem, which is **not** proved here).
* `ut_isInfPureBraid` — the generators `ut i j` satisfy the relations.
* `lift` / `lift_ut` — the universal property: a family satisfying `IsInfPureBraid` in any
  `R`-algebra extends uniquely to an algebra map out of `UT R n` (`lift_unique`).
* `toPerm` — hence the transposition representation `U(𝔱ₙ) → R[Sₙ]`, `t_{ij} ↦ (i j)`.
* `dk3_of_isInfPureBraid`, `dk4_of_isInfPureBraid` — any such family on three or four strands
  satisfies `DK3` / `DK4`, so the `RationalAssociator` results, which are stated for elements
  satisfying `DK3` / `DK4`, apply to `UT R 3`, `UT R 4` and to every representation of them.

No measured values.
-/

namespace QOU.QFTMath.InfPureBraid

/-- Generators of `𝔱ₙ`: unordered pairs, stored as `i < j`. -/
def Gen (n : ℕ) := {p : Fin n × Fin n // p.1 < p.2}

variable (R : Type*) [CommRing R] (n : ℕ)

/-- The generator `t_{ij}` in the free algebra, symmetric in `i, j` and `0` on the diagonal. -/
noncomputable def ft (i j : Fin n) : FreeAlgebra R (Gen n) :=
  if h : i < j then FreeAlgebra.ι R ⟨(i, j), h⟩
  else if h' : j < i then FreeAlgebra.ι R ⟨(j, i), h'⟩ else 0

/-- The Drinfeld–Kohno relations, as a relation on the free algebra. -/
inductive Rel : FreeAlgebra R (Gen n) → FreeAlgebra R (Gen n) → Prop
  | far (i j a b : Fin n) (hia : i ≠ a) (hib : i ≠ b) (hja : j ≠ a) (hjb : j ≠ b) :
      Rel (ft R n i j * ft R n a b) (ft R n a b * ft R n i j)
  | near (i j l : Fin n) (hij : i ≠ j) (hil : i ≠ l) (hjl : j ≠ l) :
      Rel (ft R n i j * (ft R n i l + ft R n j l)) ((ft R n i l + ft R n j l) * ft R n i j)

/-- `U(𝔱ₙ)` over `R`. -/
abbrev UT := RingQuot (Rel R n)

/-- The quotient map from the free algebra. -/
noncomputable def mk : FreeAlgebra R (Gen n) →ₐ[R] UT R n := RingQuot.mkAlgHom R (Rel R n)

/-- The generator `t_{ij}` of `U(𝔱ₙ)`. -/
noncomputable def ut (i j : Fin n) : UT R n := mk R n (ft R n i j)

theorem ft_symm (i j : Fin n) : ft R n i j = ft R n j i := by
  unfold ft
  rcases lt_trichotomy i j with h | h | h
  · simp [h, not_lt.mpr h.le]
  · subst h; simp
  · simp [h, not_lt.mpr h.le]

/-- **The generators of `U(𝔱ₙ)` satisfy the Drinfeld–Kohno relations.** -/
theorem ut_isInfPureBraid : IsInfPureBraid (ut R n) where
  symm i j := by unfold ut; rw [ft_symm]
  far i j a b hia hib hja hjb := by
    unfold Commute SemiconjBy ut
    rw [← map_mul, ← map_mul]
    exact RingQuot.mkAlgHom_rel R (Rel.far i j a b hia hib hja hjb)
  near i j l hij hil hjl := by
    unfold Commute SemiconjBy ut
    rw [← map_add, ← map_mul, ← map_mul]
    exact RingQuot.mkAlgHom_rel R (Rel.near i j l hij hil hjl)

variable {R n}
variable {A : Type*} [Ring A] [Algebra R A]

/-- The free-algebra lift of a family `s`. -/
noncomputable def freeLift (s : Fin n → Fin n → A) : FreeAlgebra R (Gen n) →ₐ[R] A :=
  FreeAlgebra.lift R fun g => s g.1.1 g.1.2

theorem freeLift_ft (s : Fin n → Fin n → A) (hs : IsInfPureBraid s) (hdiag : ∀ i, s i i = 0)
    (i j : Fin n) : freeLift (R := R) s (ft R n i j) = s i j := by
  unfold ft freeLift
  rcases lt_trichotomy i j with h | h | h
  · simp [h]
  · subst h; simp [hdiag]
  · simp [h, not_lt.mpr h.le, hs.symm j i]

/-- **Universal property.**  A family satisfying the Drinfeld–Kohno relations (and vanishing on
the diagonal) extends to an algebra map out of `U(𝔱ₙ)`. -/
noncomputable def lift (s : Fin n → Fin n → A) (hs : IsInfPureBraid s) (hdiag : ∀ i, s i i = 0) :
    UT R n →ₐ[R] A :=
  RingQuot.liftAlgHom R ⟨freeLift s, by
    intro x y h
    cases h with
    | far i j a b hia hib hja hjb =>
      simp only [map_mul, freeLift_ft s hs hdiag]
      exact hs.far i j a b hia hib hja hjb
    | near i j l hij hil hjl =>
      simp only [map_mul, map_add, freeLift_ft s hs hdiag]
      exact hs.near i j l hij hil hjl⟩

theorem lift_ut (s : Fin n → Fin n → A) (hs : IsInfPureBraid s) (hdiag : ∀ i, s i i = 0)
    (i j : Fin n) : lift (R := R) s hs hdiag (ut R n i j) = s i j := by
  unfold lift ut mk
  rw [RingQuot.liftAlgHom_mkAlgHom_apply, freeLift_ft s hs hdiag]

/-- Uniqueness: an algebra map out of `U(𝔱ₙ)` is determined by the images of the `ut i j`. -/
theorem lift_unique (f g : UT R n →ₐ[R] A) (h : ∀ i j, f (ut R n i j) = g (ut R n i j)) :
    f = g := by
  apply RingQuot.ringQuot_ext'
  apply FreeAlgebra.hom_ext
  funext x
  have hx : FreeAlgebra.ι R x = ft R n x.1.1 x.1.2 := by
    unfold ft; simp [x.2]
  simp only [Function.comp_apply, AlgHom.comp_apply, hx]
  exact h x.1.1 x.1.2

/-- The transposition representation `U(𝔱ₙ) → R[Sₙ]`, `t_{ij} ↦ (i j)` for `i ≠ j`.  On the
diagonal the transposition family is `(i i) = 1`, so it is first corrected to vanish there. -/
noncomputable def permFamily (i j : Fin n) : MonoidAlgebra R (Equiv.Perm (Fin n)) :=
  if i = j then 0 else QOU.QFTMath.InfPureBraid.t R i j

theorem permFamily_isInfPureBraid : IsInfPureBraid (permFamily (R := R) (n := n)) := by
  have h := transposition_isInfPureBraid (n := n) R
  refine ⟨?_, ?_, ?_⟩
  · intro i j
    unfold permFamily
    by_cases hij : i = j
    · subst hij; rfl
    · rw [if_neg hij, if_neg (Ne.symm hij), h.symm]
  · intro i j a b hia hib hja hjb
    unfold permFamily
    by_cases hij : i = j
    · rw [if_pos hij]; exact Commute.zero_left _
    by_cases hab : a = b
    · rw [if_pos hab]; exact Commute.zero_right _
    rw [if_neg hij, if_neg hab]
    exact h.far i j a b hia hib hja hjb
  · intro i j l hij hil hjl
    unfold permFamily
    rw [if_neg hij, if_neg hil, if_neg hjl]
    exact h.near i j l hij hil hjl

/-- **The transposition representation of `U(𝔱ₙ)`.** -/
noncomputable def toPerm : UT R n →ₐ[R] MonoidAlgebra R (Equiv.Perm (Fin n)) :=
  lift permFamily permFamily_isInfPureBraid (fun i => by unfold permFamily; simp)

theorem toPerm_ut {i j : Fin n} (hij : i ≠ j) :
    toPerm (R := R) (ut R n i j) = MonoidAlgebra.of R _ (Equiv.swap i j) := by
  unfold toPerm
  rw [lift_ut]
  unfold permFamily
  rw [if_neg hij]
  rfl

/-! ## Three and four strands: the `RationalAssociator` relations -/

open QOU.BraidsAndKnots.RationalAssociator

/-- A Drinfeld–Kohno family on three strands satisfies `DK3`. -/
theorem dk3_of_isInfPureBraid {B : Type*} [Ring B] {s : Fin 3 → Fin 3 → B}
    (hs : IsInfPureBraid s) : DK3 (s 0 1) (s 0 2) (s 1 2) where
  n12_3 := hs.near 0 1 2 (by decide) (by decide) (by decide)
  n13_2 := by
    have := hs.near 0 2 1 (by decide) (by decide) (by decide)
    rwa [hs.symm 2 1] at this
  n23_1 := by
    have := hs.near 1 2 0 (by decide) (by decide) (by decide)
    rwa [hs.symm 1 0, hs.symm 2 0] at this

/-- A Drinfeld–Kohno family on four strands satisfies `DK4`. -/
theorem dk4_of_isInfPureBraid {B : Type*} [Ring B] {s : Fin 4 → Fin 4 → B}
    (hs : IsInfPureBraid s) :
    DK4 (s 0 1) (s 0 2) (s 0 3) (s 1 2) (s 1 3) (s 2 3) where
  f12_34 := hs.far 0 1 2 3 (by decide) (by decide) (by decide) (by decide)
  f13_24 := hs.far 0 2 1 3 (by decide) (by decide) (by decide) (by decide)
  f14_23 := hs.far 0 3 1 2 (by decide) (by decide) (by decide) (by decide)
  n12_3 := hs.near 0 1 2 (by decide) (by decide) (by decide)
  n13_2 := by
    have := hs.near 0 2 1 (by decide) (by decide) (by decide); rwa [hs.symm 2 1] at this
  n23_1 := by
    have := hs.near 1 2 0 (by decide) (by decide) (by decide)
    rwa [hs.symm 1 0, hs.symm 2 0] at this
  n12_4 := hs.near 0 1 3 (by decide) (by decide) (by decide)
  n14_2 := by
    have := hs.near 0 3 1 (by decide) (by decide) (by decide); rwa [hs.symm 3 1] at this
  n24_1 := by
    have := hs.near 1 3 0 (by decide) (by decide) (by decide)
    rwa [hs.symm 1 0, hs.symm 3 0] at this
  n13_4 := hs.near 0 2 3 (by decide) (by decide) (by decide)
  n14_3 := by
    have := hs.near 0 3 2 (by decide) (by decide) (by decide); rwa [hs.symm 3 2] at this
  n34_1 := by
    have := hs.near 2 3 0 (by decide) (by decide) (by decide)
    rwa [hs.symm 2 0, hs.symm 3 0] at this
  n23_4 := hs.near 1 2 3 (by decide) (by decide) (by decide)
  n24_3 := by
    have := hs.near 1 3 2 (by decide) (by decide) (by decide); rwa [hs.symm 3 2] at this
  n34_2 := by
    have := hs.near 2 3 1 (by decide) (by decide) (by decide)
    rwa [hs.symm 2 1, hs.symm 3 1] at this

/-- The generators of `U(𝔱₄)` satisfy `DK4`. -/
theorem ut4_dk4 : DK4 (ut R 4 0 1) (ut R 4 0 2) (ut R 4 0 3) (ut R 4 1 2) (ut R 4 1 3) (ut R 4 2 3) :=
  dk4_of_isInfPureBraid (ut_isInfPureBraid R 4)

end QOU.QFTMath.InfPureBraid
