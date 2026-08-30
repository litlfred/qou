import QOU.Hecke.TwBasisPerm

/-!
# QOU.Hecke.TwBasisBraid — the braid relations for the `T_w` operators

Continues bean `qou-twwf`.  `QOU.Hecke.TwBasis` proved the Hecke **quadratic**
relation for the right-multiplication operators `Rs i` on `W →₀ R`, for an
arbitrary Coxeter system.  What is missing for a representation of `H_n(q)` is
the **braid** side of the presentation:

* distant generators commute, `Rs i ∘ Rs j = Rs j ∘ Rs i` for `|i - j| ≥ 2`;
* adjacent generators braid, `Rs i ∘ Rs j ∘ Rs i = Rs j ∘ Rs i ∘ Rs j`.

Abstractly both need Coxeter combinatorics Mathlib does not have (the strong
exchange property, parabolic subgroups, minimal coset representatives).  For
type `Aₙ` they instead reduce to a finite case analysis, because
`QOU.Hecke.TwBasisPerm.rsFun_perm` makes the branch condition a comparison of
`w` at two adjacent points.

## What is proved here

* `swap_comm_of_ne` — transpositions with disjoint supports commute.
* `Rs_comm_single` / `Rs_comm` — **the commuting relation**, for any two
  generators whose four indices are pairwise distinct.
* `Rs_comm_of_lt` — the same, from the usual hypothesis `i + 1 < j`.

The adjacent braid relation is not proved here.
-/

open Equiv Classical
namespace QOU.Hecke.TwBasis
open QOU.Hecke.SymmetricCoxeter

variable {n : ℕ} {R : Type*} [CommRing R] (q : R)

/-- Two transpositions with disjoint supports commute. -/
theorem swap_comm_of_ne {α : Type*} [DecidableEq α] {a b c d : α}
    (h1 : a ≠ c) (h2 : a ≠ d) (h3 : b ≠ c) (h4 : b ≠ d) :
    Equiv.swap a b * Equiv.swap c d = Equiv.swap c d * Equiv.swap a b := by
  ext x
  simp only [Equiv.Perm.mul_apply, Equiv.swap_apply_def]
  split_ifs <;> simp_all

/-- `Rs i` on a basis vector, with the branch condition read off `v` directly. -/
theorem Rs_single_perm (i : Fin n) (v : Perm (Fin (n + 1))) :
    Rs (permCoxeterSystem n) q i (Finsupp.single v (1 : R)) =
      if v i.castSucc < v i.succ then
        Finsupp.single (v * Equiv.swap i.castSucc i.succ) (1 : R)
      else (q - 1) • Finsupp.single v (1 : R)
             + q • Finsupp.single (v * Equiv.swap i.castSucc i.succ) (1 : R) := by
  rw [Rs_single, rsFun_perm]

/-- **The commuting relation on a basis vector.**  When the four indices moved by
    `sᵢ` and `sⱼ` are pairwise distinct, the two operators commute. -/
theorem Rs_comm_single (i j : Fin n) (w : Perm (Fin (n + 1)))
    (h1 : i.castSucc ≠ j.castSucc) (h2 : i.castSucc ≠ j.succ)
    (h3 : i.succ ≠ j.castSucc) (h4 : i.succ ≠ j.succ) :
    Rs (permCoxeterSystem n) q i (Rs (permCoxeterSystem n) q j (Finsupp.single w (1 : R)))
      = Rs (permCoxeterSystem n) q j
          (Rs (permCoxeterSystem n) q i (Finsupp.single w (1 : R))) := by
  have hcomm : w * Equiv.swap i.castSucc i.succ * Equiv.swap j.castSucc j.succ
             = w * Equiv.swap j.castSucc j.succ * Equiv.swap i.castSucc i.succ := by
    rw [mul_assoc, mul_assoc, swap_comm_of_ne h1 h2 h3 h4]
  have hta : (w * Equiv.swap j.castSucc j.succ) i.castSucc = w i.castSucc := by
    simp [Equiv.Perm.mul_apply, Equiv.swap_apply_of_ne_of_ne h1 h2]
  have htb : (w * Equiv.swap j.castSucc j.succ) i.succ = w i.succ := by
    simp [Equiv.Perm.mul_apply, Equiv.swap_apply_of_ne_of_ne h3 h4]
  have hsc : (w * Equiv.swap i.castSucc i.succ) j.castSucc = w j.castSucc := by
    simp [Equiv.Perm.mul_apply,
      Equiv.swap_apply_of_ne_of_ne (Ne.symm h1) (Ne.symm h3)]
  have hsd : (w * Equiv.swap i.castSucc i.succ) j.succ = w j.succ := by
    simp [Equiv.Perm.mul_apply,
      Equiv.swap_apply_of_ne_of_ne (Ne.symm h2) (Ne.symm h4)]
  set s := Equiv.swap i.castSucc i.succ
  set t := Equiv.swap j.castSucc j.succ
  by_cases hj : w j.castSucc < w j.succ <;> by_cases hi : w i.castSucc < w i.succ
  · rw [Rs_single_perm q j w, if_pos hj, Rs_single_perm q i (w * t), hta, htb, if_pos hi,
      Rs_single_perm q i w, if_pos hi, Rs_single_perm q j (w * s), hsc, hsd, if_pos hj, hcomm]
  · rw [Rs_single_perm q j w, if_pos hj, Rs_single_perm q i (w * t), hta, htb, if_neg hi,
      Rs_single_perm q i w, if_neg hi, map_add, map_smul, map_smul,
      Rs_single_perm q j w, if_pos hj, Rs_single_perm q j (w * s), hsc, hsd, if_pos hj, hcomm]
  · rw [Rs_single_perm q j w, if_neg hj, map_add, map_smul, map_smul,
      Rs_single_perm q i w, if_pos hi, Rs_single_perm q i (w * t), hta, htb, if_pos hi,
      Rs_single_perm q j (w * s), hsc, hsd, if_neg hj, hcomm]
  · rw [Rs_single_perm q j w, if_neg hj, map_add, map_smul, map_smul,
      Rs_single_perm q i w, if_neg hi, map_add, map_smul, map_smul,
      Rs_single_perm q i (w * t), hta, htb, if_neg hi,
      Rs_single_perm q j w, if_neg hj,
      Rs_single_perm q j (w * s), hsc, hsd, if_neg hj, hcomm]
    module

/-- **The commuting relation, as an operator identity.** -/
theorem Rs_comm (i j : Fin n)
    (h1 : i.castSucc ≠ j.castSucc) (h2 : i.castSucc ≠ j.succ)
    (h3 : i.succ ≠ j.castSucc) (h4 : i.succ ≠ j.succ) :
    (Rs (permCoxeterSystem n) q i) ∘ₗ (Rs (permCoxeterSystem n) q j)
      = (Rs (permCoxeterSystem n) q j) ∘ₗ (Rs (permCoxeterSystem n) q i) := by
  apply Finsupp.lhom_ext'
  intro w
  apply LinearMap.ext_ring
  simpa using Rs_comm_single q i j w h1 h2 h3 h4

/-- **Distant generators commute** — the braid-side relation for `|i - j| ≥ 2`. -/
theorem Rs_comm_of_lt (i j : Fin n) (h : (i : ℕ) + 1 < (j : ℕ)) :
    (Rs (permCoxeterSystem n) q i) ∘ₗ (Rs (permCoxeterSystem n) q j)
      = (Rs (permCoxeterSystem n) q j) ∘ₗ (Rs (permCoxeterSystem n) q i) := by
  have hne : ∀ a b : Fin (n + 1), (a : ℕ) ≠ (b : ℕ) → a ≠ b :=
    fun a b hab hh => hab (by rw [hh])
  exact Rs_comm q i j (hne _ _ (by simp; omega)) (hne _ _ (by simp; omega))
    (hne _ _ (by simp; omega)) (hne _ _ (by simp; omega))

end QOU.Hecke.TwBasis
