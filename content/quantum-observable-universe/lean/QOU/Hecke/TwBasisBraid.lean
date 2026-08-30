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
* `swap_braid` — `(ab)(bc)(ab) = (bc)(ab)(bc)`, both sides being `(ac)`.
* `Rs_braid_single` / `Rs_braid` — **the braid relation** for adjacent
  generators, `Rs i ∘ Rs j ∘ Rs i = Rs j ∘ Rs i ∘ Rs j` when `j = i + 1`.

Together with `QOU.Hecke.TwBasis.Rs_sq` this is the whole Hecke presentation
holding for the operators `Rs`, which is what a representation of `H_n(q)` on
`W →₀ R` requires.  Building that algebra map, and reading the linear
independence of the `T_w` off it, is the next step and is not done here.

## How the braid case goes through

The three points `i`, `i+1`, `i+2` carry three distinct values of `w`, so their
order is one of six.  In each, `rsFun_perm` turns every branch into a
comparison already in context, and the six group elements of the rank-2 coset
normalise under `s² = 1`, `t² = 1` and `sts = tst`.  So `simp only` with the
value lemmas and the six comparison facts runs the whole computation; three of
the six orders need `module` afterwards to match coefficients, and two of the
eight `rcases` branches are order-inconsistent.

One trap worth recording: with `simp only` the **discharger** for a conditional
rewrite sees only the lemmas listed.  A positive side condition `P` closes on
`P = True`, but a negative one `¬ P` becomes `¬ False` and then goes nowhere
unless `not_false_eq_true` is in the list.  Omitting it does not fail loudly —
simp silently leaves the `Rs` unapplied, and the error surfaces much later as
`module` reporting `1 = 0`.
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

/-- **The braid relation for transpositions**: `(ab)(bc)(ab) = (bc)(ab)(bc)`, both
    sides being `(ac)`. -/
theorem swap_braid {α : Type*} [DecidableEq α] {a b c : α}
    (hab : a ≠ b) (hac : a ≠ c) (hbc : b ≠ c) :
    Equiv.swap a b * Equiv.swap b c * Equiv.swap a b
      = Equiv.swap b c * Equiv.swap a b * Equiv.swap b c := by
  have hR : Equiv.swap b c * Equiv.swap a b * Equiv.swap b c = Equiv.swap c a :=
    Equiv.swap_mul_swap_mul_swap hab hac
  have hL : Equiv.swap a b * Equiv.swap b c * Equiv.swap a b = Equiv.swap c a := by
    rw [Equiv.swap_comm a b, Equiv.swap_comm b c,
      Equiv.swap_mul_swap_mul_swap hbc.symm hac.symm, Equiv.swap_comm a c]
  rw [hL, hR]

/-- `Rs i` on a basis vector when the length goes up. -/
theorem Rs_single_up (i : Fin n) (v : Perm (Fin (n + 1)))
    (h : v i.castSucc < v i.succ) :
    Rs (permCoxeterSystem n) q i (Finsupp.single v (1 : R))
      = Finsupp.single (v * Equiv.swap i.castSucc i.succ) (1 : R) := by
  rw [Rs_single_perm, if_pos h]

/-- `Rs i` on a basis vector when the length goes down. -/
theorem Rs_single_dn (i : Fin n) (v : Perm (Fin (n + 1)))
    (h : ¬ v i.castSucc < v i.succ) :
    Rs (permCoxeterSystem n) q i (Finsupp.single v (1 : R))
      = (q - 1) • Finsupp.single v (1 : R)
        + q • Finsupp.single (v * Equiv.swap i.castSucc i.succ) (1 : R) := by
  rw [Rs_single_perm, if_neg h]

-- The six order branches each use a different subset of the comparison facts; the
-- linter flags the ones idle in a given branch, and trimming them breaks the others.
set_option linter.unusedSimpArgs false in
/-- **The braid relation on a basis vector**, for adjacent generators. -/
theorem Rs_braid_single (i j : Fin n) (hji : (j : ℕ) = (i : ℕ) + 1)
    (w : Perm (Fin (n + 1))) :
    Rs (permCoxeterSystem n) q i (Rs (permCoxeterSystem n) q j
        (Rs (permCoxeterSystem n) q i (Finsupp.single w (1 : R))))
      = Rs (permCoxeterSystem n) q j (Rs (permCoxeterSystem n) q i
          (Rs (permCoxeterSystem n) q j (Finsupp.single w (1 : R)))) := by
  -- the three points moved by the two generators
  have hb : j.castSucc = i.succ := by
    apply Fin.ext
    simp only [Fin.coe_castSucc, Fin.val_succ, hji]
  have hab : i.castSucc ≠ i.succ := (Fin.castSucc_lt_succ i).ne
  have hac : i.castSucc ≠ j.succ := by
    intro h
    have h1 : (i.castSucc : ℕ) = (j.succ : ℕ) := congrArg Fin.val h
    simp only [Fin.coe_castSucc, Fin.val_succ, hji] at h1
    omega
  have hbc : i.succ ≠ j.succ := by
    intro h
    have h1 : (i.succ : ℕ) = (j.succ : ℕ) := congrArg Fin.val h
    simp only [Fin.val_succ, hji] at h1
    omega
  -- `Rs j`, with its transposition written in terms of `i.succ`
  have hj_up : ∀ v : Perm (Fin (n + 1)), v i.succ < v j.succ →
      Rs (permCoxeterSystem n) q j (Finsupp.single v (1 : R))
        = Finsupp.single (v * Equiv.swap i.succ j.succ) (1 : R) := by
    intro v h; rw [Rs_single_perm q j v, hb, if_pos h]
  have hj_dn : ∀ v : Perm (Fin (n + 1)), ¬ v i.succ < v j.succ →
      Rs (permCoxeterSystem n) q j (Finsupp.single v (1 : R))
        = (q - 1) • Finsupp.single v (1 : R)
          + q • Finsupp.single (v * Equiv.swap i.succ j.succ) (1 : R) := by
    intro v h; rw [Rs_single_perm q j v, hb, if_neg h]
  -- how the two transpositions move the three points
  have vsa : ∀ v : Perm (Fin (n + 1)),
      (v * Equiv.swap i.castSucc i.succ) i.castSucc = v i.succ := by
    intro v; simp [Equiv.Perm.mul_apply]
  have vsb : ∀ v : Perm (Fin (n + 1)),
      (v * Equiv.swap i.castSucc i.succ) i.succ = v i.castSucc := by
    intro v; simp [Equiv.Perm.mul_apply]
  have vsc : ∀ v : Perm (Fin (n + 1)),
      (v * Equiv.swap i.castSucc i.succ) j.succ = v j.succ := by
    intro v
    simp [Equiv.Perm.mul_apply, Equiv.swap_apply_of_ne_of_ne (Ne.symm hac) (Ne.symm hbc)]
  have vta : ∀ v : Perm (Fin (n + 1)),
      (v * Equiv.swap i.succ j.succ) i.castSucc = v i.castSucc := by
    intro v
    simp [Equiv.Perm.mul_apply, Equiv.swap_apply_of_ne_of_ne hab hac]
  have vtb : ∀ v : Perm (Fin (n + 1)),
      (v * Equiv.swap i.succ j.succ) i.succ = v j.succ := by
    intro v; simp [Equiv.Perm.mul_apply]
  have vtc : ∀ v : Perm (Fin (n + 1)),
      (v * Equiv.swap i.succ j.succ) j.succ = v i.succ := by
    intro v; simp [Equiv.Perm.mul_apply]
  -- the rank-2 group relations
  have gss : ∀ v : Perm (Fin (n + 1)),
      v * Equiv.swap i.castSucc i.succ * Equiv.swap i.castSucc i.succ = v :=
    fun v => Equiv.mul_swap_mul_self _ _ v
  have gtt : ∀ v : Perm (Fin (n + 1)),
      v * Equiv.swap i.succ j.succ * Equiv.swap i.succ j.succ = v :=
    fun v => Equiv.mul_swap_mul_self _ _ v
  have gsts : ∀ v : Perm (Fin (n + 1)),
      v * Equiv.swap i.castSucc i.succ * Equiv.swap i.succ j.succ
          * Equiv.swap i.castSucc i.succ
        = v * Equiv.swap i.succ j.succ * Equiv.swap i.castSucc i.succ
          * Equiv.swap i.succ j.succ := by
    intro v
    calc v * Equiv.swap i.castSucc i.succ * Equiv.swap i.succ j.succ
            * Equiv.swap i.castSucc i.succ
        = v * (Equiv.swap i.castSucc i.succ * Equiv.swap i.succ j.succ
            * Equiv.swap i.castSucc i.succ) := by simp [mul_assoc]
      _ = v * (Equiv.swap i.succ j.succ * Equiv.swap i.castSucc i.succ
            * Equiv.swap i.succ j.succ) := by rw [swap_braid hab hac hbc]
      _ = v * Equiv.swap i.succ j.succ * Equiv.swap i.castSucc i.succ
            * Equiv.swap i.succ j.succ := by simp [mul_assoc]
  -- the three values are pairwise distinct, so their order is strict and total
  have nab : w i.castSucc ≠ w i.succ := fun h => hab (w.injective h)
  have nbc : w i.succ ≠ w j.succ := fun h => hbc (w.injective h)
  have nac : w i.castSucc ≠ w j.succ := fun h => hac (w.injective h)
  rcases nab.lt_or_gt with h1 | h1 <;> rcases nbc.lt_or_gt with h2 | h2 <;>
    rcases nac.lt_or_gt with h3 | h3
  · simp only [Rs_single_up q i, Rs_single_dn q i, hj_up, hj_dn, map_add, map_smul,
      vsa, vsb, vsc, vta, vtb, vtc, gss, gtt, gsts,
      h1, h2, h3, asymm h1, asymm h2, asymm h3, not_false_eq_true]
  · exact absurd (h1.trans h2) (asymm h3)
  · simp only [Rs_single_up q i, Rs_single_dn q i, hj_up, hj_dn, map_add, map_smul,
      vsa, vsb, vsc, vta, vtb, vtc, gss, gtt, gsts,
      h1, h2, h3, asymm h1, asymm h2, asymm h3, not_false_eq_true]
  · simp only [Rs_single_up q i, Rs_single_dn q i, hj_up, hj_dn, map_add, map_smul,
      vsa, vsb, vsc, vta, vtb, vtc, gss, gtt, gsts,
      h1, h2, h3, asymm h1, asymm h2, asymm h3, not_false_eq_true]
    module
  · simp only [Rs_single_up q i, Rs_single_dn q i, hj_up, hj_dn, map_add, map_smul,
      vsa, vsb, vsc, vta, vtb, vtc, gss, gtt, gsts,
      h1, h2, h3, asymm h1, asymm h2, asymm h3, not_false_eq_true]
  · simp only [Rs_single_up q i, Rs_single_dn q i, hj_up, hj_dn, map_add, map_smul,
      vsa, vsb, vsc, vta, vtb, vtc, gss, gtt, gsts,
      h1, h2, h3, asymm h1, asymm h2, asymm h3, not_false_eq_true]
    module
  · exact absurd (h2.trans h1) (asymm h3)
  · simp only [Rs_single_up q i, Rs_single_dn q i, hj_up, hj_dn, map_add, map_smul,
      vsa, vsb, vsc, vta, vtb, vtc, gss, gtt, gsts,
      h1, h2, h3, asymm h1, asymm h2, asymm h3, not_false_eq_true]
    module

/-- **The braid relation, as an operator identity.**  Adjacent generators braid. -/
theorem Rs_braid (i j : Fin n) (hji : (j : ℕ) = (i : ℕ) + 1) :
    (Rs (permCoxeterSystem n) q i) ∘ₗ (Rs (permCoxeterSystem n) q j)
        ∘ₗ (Rs (permCoxeterSystem n) q i)
      = (Rs (permCoxeterSystem n) q j) ∘ₗ (Rs (permCoxeterSystem n) q i)
        ∘ₗ (Rs (permCoxeterSystem n) q j) := by
  apply Finsupp.lhom_ext'
  intro w
  apply LinearMap.ext_ring
  simpa using Rs_braid_single q i j hji w

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
