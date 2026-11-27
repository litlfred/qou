import Mathlib.RingTheory.Polynomial.Cyclotomic.Roots
import Mathlib.RingTheory.Polynomial.Vieta
import Mathlib.RingTheory.RootsOfUnity.Complex
import QOU.MassTheory.CyclotomicBoundaryCertified

/-!
# Power-sum test for products of cyclotomic polynomials

If `P = c · X^j · ∏ Φ_k` in `ℤ[X]` (`IsCycloProduct`), write `d = deg P` and let `a₁`, `a₂` be
the coefficients of `X^(d-1)` and `X^(d-2)`. Two facts follow.

* `c` divides every coefficient of `P` (each `Φ_k` is monic).
* Over `ℂ`, `P = c ∏ (X - z)` with every `|z| ≤ 1` (the roots are `0` or roots of unity).
  Vieta then gives `a₁² - 2c·a₂ = c²·∑ z²`, so `|a₁² - 2c·a₂| ≤ c²·d`.

The second fact is the obstruction for the triangular `n` of
`conj:cyclotomic-boundary-at-keystone`, where `c = 1` and the divisibility test is empty.
The theorems at the end are the arithmetic half of the all-`n` argument: they take the top
three coefficients of the cleared tail `P_n` as **hypotheses** (named `_of_topCoeffs`). The
combinatorial step that supplies those coefficients for every `n` (counting partitions by
`∑ (i+j)` near the staircase) is proved on paper in the content block and is not formalised
here.
-/

namespace QOU.Mass.CyclotomicPowerSum

open Polynomial QOU.Mass.CyclotomicBoundaryCertified

section Esymm

variable {R : Type*} [CommRing R]

theorem esymm_zero' (s : Multiset R) : s.esymm 0 = 1 := by
  simp [Multiset.esymm, Multiset.powersetCard_zero_left]

theorem esymm_cons_succ (a : R) (s : Multiset R) (n : ℕ) :
    (a ::ₘ s).esymm (n + 1) = s.esymm (n + 1) + a * s.esymm n := by
  simp only [Multiset.esymm, Multiset.powersetCard_cons, Multiset.map_add, Multiset.sum_add,
    Multiset.map_map, Function.comp_def, Multiset.prod_cons, Multiset.sum_map_mul_left]

theorem esymm_one' (s : Multiset R) : s.esymm 1 = s.sum := by
  induction s using Multiset.induction_on with
  | empty => simp [Multiset.esymm]
  | cons a s ih => rw [esymm_cons_succ, ih, esymm_zero', Multiset.sum_cons]; ring

theorem two_mul_esymm_two (s : Multiset R) :
    2 * s.esymm 2 = s.sum ^ 2 - (s.map (· ^ 2)).sum := by
  induction s using Multiset.induction_on with
  | empty => simp [Multiset.esymm]
  | cons a s ih =>
    rw [esymm_cons_succ, mul_add, ih, esymm_one', Multiset.sum_cons, Multiset.map_cons,
      Multiset.sum_cons]
    ring

end Esymm

/-- The roots of `X^j · ∏ Φ_k` over `ℂ`, listed with multiplicity. -/
noncomputable def rootMultiset (j : ℕ) (s : Multiset ℕ) : Multiset ℂ :=
  Multiset.replicate j 0 + s.bind (fun k => (primitiveRoots k ℂ).val)

theorem cyclotomic_complex_eq (k : ℕ) :
    cyclotomic k ℂ = ((primitiveRoots k ℂ).val.map (fun z => X - C z)).prod := by
  rcases Nat.eq_zero_or_pos k with rfl | hk
  · simp
  · rw [cyclotomic_eq_prod_X_sub_primitiveRoots (Complex.isPrimitiveRoot_exp k hk.ne'),
      Finset.prod_eq_multiset_prod]

theorem map_eq_rootMultiset (c : ℤ) (j : ℕ) (s : Multiset ℕ) :
    (C c * X ^ j * (s.map (fun k => cyclotomic k ℤ)).prod).map (Int.castRingHom ℂ) =
      C (c : ℂ) * ((rootMultiset j s).map (fun z => X - C z)).prod := by
  simp only [Polynomial.map_mul, Polynomial.map_pow, Polynomial.map_X,
    Polynomial.map_multiset_prod, Multiset.map_map, Function.comp_def, map_cyclotomic,
    cyclotomic_complex_eq, rootMultiset, Multiset.map_add, Multiset.prod_add,
    Multiset.map_replicate, Multiset.prod_replicate, Multiset.map_bind, Multiset.prod_bind,
    map_zero, sub_zero, eq_intCast, mul_assoc]
  rw [Polynomial.map_intCast, ← Polynomial.C_eq_intCast]

theorem norm_le_one_of_mem_rootMultiset {j : ℕ} {s : Multiset ℕ} {z : ℂ}
    (hz : z ∈ rootMultiset j s) : ‖z‖ ≤ 1 := by
  rcases Multiset.mem_add.1 hz with h | h
  · rw [Multiset.eq_of_mem_replicate h]; simp
  · obtain ⟨k, -, hk⟩ := Multiset.mem_bind.1 h
    have hk0 : 0 < k := by
      rcases Nat.eq_zero_or_pos k with rfl | hk0
      · simp at hk
      · exact hk0
    exact ((mem_primitiveRoots hk0).1 hk).norm'_eq_one hk0.ne' |>.le

/-- **Divisibility test.** In a cyclotomic product the leading coefficient divides every
coefficient. -/
theorem leadingCoeff_dvd_coeff {P : ℤ[X]} (hP : IsCycloProduct P) (i : ℕ) :
    P.leadingCoeff ∣ P.coeff i := by
  obtain ⟨c, j, s, rfl⟩ := hP
  have hmon : (X ^ j * (s.map (fun k => cyclotomic k ℤ)).prod).Monic :=
    (monic_X_pow j).mul (monic_multiset_prod_of_monic _ _ (fun k _ => cyclotomic.monic k ℤ))
  rw [mul_assoc, leadingCoeff_mul, leadingCoeff_C, hmon.leadingCoeff, mul_one, coeff_C_mul]
  exact dvd_mul_right _ _

/-- **Power-sum test.** For `P = c · X^j · ∏ Φ_k` of degree `d ≥ 2`,
`|a₁² - 2c·a₂| ≤ c²·d`, where `a₁, a₂` are the coefficients of `X^(d-1), X^(d-2)`. The
quantity `(a₁² - 2c·a₂)/c²` is the sum of the squares of the roots. -/
theorem abs_powerSum_two_le {P : ℤ[X]} (hP : IsCycloProduct P) (hd : 2 ≤ P.natDegree) :
    |P.coeff (P.natDegree - 1) ^ 2 - 2 * P.leadingCoeff * P.coeff (P.natDegree - 2)| ≤
      P.leadingCoeff ^ 2 * P.natDegree := by
  obtain ⟨c, j, s, rfl⟩ := hP
  set M := rootMultiset j s
  set Q : ℂ[X] := (M.map (fun z => X - C z)).prod
  have hmap := map_eq_rootMultiset c j s
  set P : ℤ[X] := C c * X ^ j * (s.map (fun k => cyclotomic k ℤ)).prod with hPdef
  have hc : c ≠ 0 := by
    rintro rfl; simp [P] at hd
  have hQdeg : Q.natDegree = Multiset.card M := natDegree_multiset_prod_X_sub_C_eq_card M
  have hPdeg : P.natDegree = Multiset.card M := by
    rw [← natDegree_map_eq_of_injective (RingHom.injective_int (Int.castRingHom ℂ)) P, hmap,
      natDegree_C_mul (by exact_mod_cast hc), hQdeg]
  have hcoeff : ∀ i, ((P.coeff i : ℤ) : ℂ) = (c : ℂ) * Q.coeff i := by
    intro i
    have := congrArg (fun p => p.coeff i) hmap
    simpa [coeff_map, coeff_C_mul] using this
  have hlead : P.leadingCoeff = c := by
    have hmon : (X ^ j * (s.map (fun k => cyclotomic k ℤ)).prod).Monic :=
      (monic_X_pow j).mul (monic_multiset_prod_of_monic _ _ (fun k _ => cyclotomic.monic k ℤ))
    rw [hPdef, mul_assoc, leadingCoeff_mul, leadingCoeff_C, hmon.leadingCoeff, mul_one]
  rw [hlead, hPdeg]
  set m := Multiset.card M with hm
  have hm2 : 2 ≤ m := hPdeg ▸ hd
  have h1 : Q.coeff (m - 1) = -M.sum := by
    rw [Multiset.prod_X_sub_C_coeff M (by omega), show m - (m - 1) = 1 by omega, esymm_one']
    ring
  have h2 : 2 * Q.coeff (m - 2) = M.sum ^ 2 - (M.map (· ^ 2)).sum := by
    rw [Multiset.prod_X_sub_C_coeff M (by omega), show m - (m - 2) = 2 by omega,
      ← two_mul_esymm_two]
    ring
  -- transfer to ℂ
  have key : (((P.coeff (m - 1) ^ 2 - 2 * c * P.coeff (m - 2) : ℤ)) : ℂ) =
      (c : ℂ) ^ 2 * (M.map (· ^ 2)).sum := by
    push_cast
    rw [hcoeff, hcoeff, h1]
    linear_combination (-(c : ℂ) ^ 2) * h2
  have hnorm : ‖(M.map (· ^ 2)).sum‖ ≤ (m : ℝ) := by
    calc ‖(M.map (· ^ 2)).sum‖ ≤ (M.map (fun z => ‖z ^ 2‖)).sum := by
          have := norm_multiset_sum_le (M.map (· ^ 2))
          rwa [Multiset.map_map, Function.comp_def] at this
      _ ≤ (M.map (fun _ => (1 : ℝ))).sum := by
          apply Multiset.sum_map_le_sum_map
          intro z hz
          rw [norm_pow]
          exact pow_le_one₀ (norm_nonneg z) (norm_le_one_of_mem_rootMultiset hz)
      _ = m := by simp [hm]
  have : ((|P.coeff (m - 1) ^ 2 - 2 * c * P.coeff (m - 2)| : ℤ) : ℝ) ≤
      ((c ^ 2 * m : ℤ) : ℝ) := by
    rw [Int.cast_abs, ← Complex.norm_intCast, key, norm_mul, norm_pow, Complex.norm_intCast]
    push_cast
    rw [sq_abs]
    exact mul_le_mul_of_nonneg_left hnorm (sq_nonneg _)
  exact_mod_cast this

/-! ## Arithmetic half of the all-`n` argument

The hypotheses are the top coefficients of the cleared tail `P_n`, as computed on paper in
`conj:cyclotomic-boundary-at-keystone` (and checked against the exact `P_n` for `n ≤ 28`). -/

/-- **Triangular `n = T_{j+1}`, `j ≥ 3`.** If `P` has leading coefficient `1`,
`a₁ = j(j+1)`, `a₂ = j + j(j-1)²(j-2)/4` and degree `j(j+1)(j+2)(3j+1)/12`, then `P` is not a
cyclotomic product: the root power sum `a₁² - 2a₂` exceeds the degree by
`j(j-1)(3j²+41j+14)/12 > 0`. -/
theorem not_isCycloProduct_triangular_of_topCoeffs {P : ℤ[X]} {j : ℤ} (hj : 3 ≤ j)
    (hlead : P.leadingCoeff = 1) (h1 : P.coeff (P.natDegree - 1) = j * (j + 1))
    (h2 : 4 * P.coeff (P.natDegree - 2) = 4 * j + j * (j - 1) ^ 2 * (j - 2))
    (hd : 12 * (P.natDegree : ℤ) = j * (j + 1) * (j + 2) * (3 * j + 1)) :
    ¬ IsCycloProduct P := by
  intro hP
  have hd2 : 2 ≤ P.natDegree := by
    have : (24 : ℤ) ≤ 12 * (P.natDegree : ℤ) := by rw [hd]; nlinarith
    omega
  have hb := abs_powerSum_two_le hP hd2
  rw [hlead] at hb
  have hle := (le_abs_self _).trans hb
  rw [h1] at hle
  have hpos : 0 < j * (j - 1) * (3 * j ^ 2 + 41 * j + 14) := by
    apply mul_pos (mul_pos (by omega) (by omega)); nlinarith
  nlinarith

/-- **`n = T_{j+1} - 1`, `j ≥ 3`.** Leading coefficient `j+1` and `2a₁ = j²(j-1)`: since
`j²(j-1) ≡ -2 (mod j+1)`, the leading coefficient does not divide `a₁`. -/
theorem not_isCycloProduct_rEqJ_of_topCoeffs {P : ℤ[X]} {j : ℤ} (hj : 3 ≤ j)
    (hlead : P.leadingCoeff = j + 1)
    (h1 : 2 * P.coeff (P.natDegree - 1) = j ^ 2 * (j - 1)) :
    ¬ IsCycloProduct P := by
  intro hP
  obtain ⟨k, hk⟩ := hlead ▸ leadingCoeff_dvd_coeff hP (P.natDegree - 1)
  have h2 : (j + 1) ∣ 2 := ⟨j ^ 2 - 2 * j + 2 - 2 * k, by linear_combination h1 - 2 * hk⟩
  have := Int.le_of_dvd (by norm_num) h2
  omega

/-- **`n = T_j + 1`, `j ≥ 4`, `j ≠ 5`.** Leading coefficient `j+1` and
`2a₁ = j(j-1)(j-2) ≡ -6 (mod j+1)`. -/
theorem not_isCycloProduct_rEqOne_of_topCoeffs {P : ℤ[X]} {j : ℤ} (hj : 4 ≤ j) (hj5 : j ≠ 5)
    (hlead : P.leadingCoeff = j + 1)
    (h1 : 2 * P.coeff (P.natDegree - 1) = j * (j - 1) * (j - 2)) :
    ¬ IsCycloProduct P := by
  intro hP
  obtain ⟨k, hk⟩ := hlead ▸ leadingCoeff_dvd_coeff hP (P.natDegree - 1)
  have h6 : (j + 1) ∣ 6 := ⟨j ^ 2 - 4 * j + 6 - 2 * k, by linear_combination h1 - 2 * hk⟩
  have hle := Int.le_of_dvd (by norm_num) h6
  have hj4 : j = 4 := by omega
  subst hj4
  norm_num at h6

end QOU.Mass.CyclotomicPowerSum
