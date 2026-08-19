import QOU.SchurWeyl.SeminormalRep
import QOU.SchurWeyl.QJucysMurphy
import QOU.SchurWeyl.HoefsmitRepGeneral

/-!
# `QOU.SchurWeyl.QJucysMurphyEigen` — the `q`-Jucys–Murphy eigenvalue (bean `qou-t8qh`)

Ram (1997) Thm 4.1: on the seminormal representation the Jucys–Murphy element `L_k` acts
**diagonally**, with eigenvalue `q^{2·cellContent}` at the cell holding the corresponding value.

This is the one input still missing from `QJucysMurphy.barSymJMSum_block_eigenvalue` — the last
real `sorry` in the SchurWeyl tree.  (Its other blocker, `hoefsmit_seminormal_rep`, is proved.)

## The crux, and why the theorem is true

The recursion is pure conjugation, `L_{k+1} = σ_k L_k σ_k`, so the inductive step conjugates a
diagonal matrix `D` by `S = genMat q (k+1)`.  For that to stay diagonal the off-diagonal of
`S · D · S` must vanish, and on a size-`2` orbit it is

  `offDiag(-d) · (a(d)·q^{2c} + a(-d)·q^{2(c+d)})`,

with `a = seminormalParam` and `d` the axial distance.  The bracket is **identically zero**:

  `1/(1 - q^{-2d}) = -q^{2d}/(1 - q^{2d})`,

which is `seminormalParam_weighted_cancel` below.  On a size-`1` orbit `S` is already diagonal with
entry `a(±1)`, and `a(1) = q`, `a(-1) = -q⁻¹`, so `a(d)² = q^{2d}` — exactly the content shift.

Base ring `ℝ` (the seminormal parameters are archimedean, §7c).
-/

namespace QOU.SchurWeyl

namespace Seminormal

/-- **The weighted cancellation behind the JM eigenvalue.**  Weighting the two seminormal
parameters of a size-`2` orbit by the `q^{2·content}` of their own cells makes them cancel:

  `a(d)·q^{2c} + a(-d)·q^{2(c+d)} = 0`.

This is exactly the off-diagonal of `S · D · S` on that orbit, so it is what keeps the conjugate
of a diagonal matrix diagonal — the inductive step of Ram's Theorem 4.1. -/
theorem seminormalParam_weighted_cancel (q : ℝ) (hq : q ≠ 0) {d : ℤ}
    (hd : q ^ (2 * d) ≠ 1) (c : ℤ) :
    seminormalParam q d * q ^ (2 * c) + seminormalParam q (-d) * q ^ (2 * (c + d)) = 0 := by
  have hx0 : q ^ (2 * d) ≠ 0 := zpow_ne_zero _ hq
  have hx1 : 1 - q ^ (2 * d) ≠ 0 := sub_ne_zero_of_ne (Ne.symm hd)
  have hneg : q ^ (-2 * d : ℤ) = (q ^ (2 * d))⁻¹ := by
    rw [show (-2 * d : ℤ) = -(2 * d) by ring, zpow_neg]
  have hcd : q ^ (2 * (c + d)) = q ^ (2 * c) * q ^ (2 * d) := by
    rw [show (2 * (c + d) : ℤ) = 2 * c + 2 * d by ring, zpow_add₀ hq]
  rw [seminormalParam, seminormalParam, hneg, hcd,
    show (-2 * -d : ℤ) = 2 * d by ring]
  -- make the two powers opaque; what is left is an identity in `x`, `y`, `q`
  set x := q ^ (2 * d) with hxdef
  set y := q ^ (2 * c) with hydef
  have hxi1 : 1 - x⁻¹ ≠ 0 := by
    intro h
    apply hx1
    have hx : x⁻¹ = 1 := by linarith [h]
    have := congrArg (fun t => x * t) hx
    simp only [mul_inv_cancel₀ hx0, mul_one] at this
    linarith [this]
  -- the bracket vanishes: (1 - x⁻¹)⁻¹ = -x·(1 - x)⁻¹
  have hbr : (1 - x⁻¹)⁻¹ + x * (1 - x)⁻¹ = 0 := by
    have hxi : (1 - x⁻¹) = (x - 1) * x⁻¹ := by field_simp
    have h2 : (x - 1)⁻¹ = -(1 - x)⁻¹ := by
      rw [show x - 1 = -(1 - x) by ring, inv_neg]
    rw [hxi, mul_inv, inv_inv, h2]
    ring
  linear_combination ((q - q⁻¹) * y) * hbr

/-- **Size-`1` orbit: the scalar squares to the content shift.**  At axial distance `±1` the
generator acts by the scalar `a(±1)` (`q` resp. `-q⁻¹`), and its square is `q^{2d}` — exactly the
factor by which `q^{2·content}` changes when the content moves by `d`.  This is the inadmissible
branch of the inductive step. -/
theorem seminormalParam_sq_of_one (q : ℝ) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    seminormalParam q 1 ^ 2 = q ^ (2 * (1 : ℤ)) := by
  rw [seminormalParam_one q hq hq2]
  norm_num [← zpow_natCast]

theorem seminormalParam_sq_of_neg_one (q : ℝ) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    seminormalParam q (-1) ^ 2 = q ^ (2 * (-1 : ℤ)) := by
  rw [seminormalParam_neg_one q hq hq2]
  rw [show (2 * (-1 : ℤ)) = -2 by ring, zpow_neg]
  field_simp

/-- The inadmissible branch in one statement: for `d = ±1`, `a(d)² · q^{2c} = q^{2(c+d)}`. -/
theorem seminormalParam_sq_mul (q : ℝ) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) {d : ℤ}
    (hd : d = 1 ∨ d = -1) (c : ℤ) :
    seminormalParam q d ^ 2 * q ^ (2 * c) = q ^ (2 * (c + d)) := by
  have hcd : q ^ (2 * (c + d)) = q ^ (2 * c) * q ^ (2 * d) := by
    rw [show (2 * (c + d) : ℤ) = 2 * c + 2 * d by ring, zpow_add₀ hq]
  rcases hd with rfl | rfl
  · rw [hcd, seminormalParam_sq_of_one q hq hq2]; ring
  · rw [hcd, seminormalParam_sq_of_neg_one q hq hq2]; ring

/-! ## The full entry-level inductive step

Both entries of `S · D · S` on a size-`2` orbit reduce to the *same* cancellation. Writing
`c` for the content seen by `D` at `T` and `c + d` for the one at `s·T`:

* the **off-diagonal** is `offDiag(d) · (a(d)q^{2c} + a(-d)q^{2(c+d)})`, which is `0`;
* the **diagonal** is `a(d)²q^{2c} + offDiag(-d)offDiag(d)·q^{2(c+d)}`, and using
  `offDiag_mul_neg` (`offDiag(d)offDiag(-d) = 1 + a(d)a(-d)`) it collapses to
  `a(d)·(a(d)q^{2c} + a(-d)q^{2(c+d)}) + q^{2(c+d)} = q^{2(c+d)}`.

So one identity governs the whole step — which is why the induction closes.
-/

open SeminormalRep in
/-- **Off-diagonal entry of the step vanishes.** -/
theorem jmStep_offDiag (q : ℝ) (hq : q ≠ 0) {d : ℤ} (hd : q ^ (2 * d) ≠ 1) (c : ℤ) :
    offDiag q d * q ^ (2 * c) * seminormalParam q d
      + seminormalParam q (-d) * q ^ (2 * (c + d)) * offDiag q d = 0 := by
  have hcancel := seminormalParam_weighted_cancel q hq hd c
  linear_combination offDiag q d * hcancel

open SeminormalRep in
/-- **Diagonal entry of the step is the shifted content.**  `a(d)²q^{2c}` plus the
off-diagonal round trip equals `q^{2(c+d)}` exactly. -/
theorem jmStep_diag (q : ℝ) (hq : q ≠ 0) {d : ℤ} (hd0 : d ≠ 0) (hd : q ^ (2 * d) ≠ 1)
    (c : ℤ) :
    seminormalParam q d ^ 2 * q ^ (2 * c)
        + offDiag q (-d) * offDiag q d * q ^ (2 * (c + d))
      = q ^ (2 * (c + d)) := by
  have hcancel := seminormalParam_weighted_cancel q hq hd c
  have hprod : offDiag q d * offDiag q (-d)
      = 1 + seminormalParam q d * seminormalParam q (-d) := offDiag_mul_neg q hd0
  linear_combination seminormalParam q d * hcancel + q ^ (2 * (c + d)) * hprod

end Seminormal

/-! ## The diagonal of JM eigenvalues, and the base case -/

namespace SeminormalRep

open QOU.Mathlib (StandardYoungTableau)
open TableauCells Seminormal

variable {μ : YoungDiagram}

/-- **The `q`-JM eigenvalue matrix at value `v`**: diagonal, with `q^{2·content}` read off the
cell holding `v` in each tableau. -/
noncomputable def jmDiagVal (q : ℝ) (v : ℕ) :
    Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) ℝ :=
  Matrix.diagonal (fun T => q ^ (2 * cellContent (cellOf T v)))

@[simp] theorem jmDiagVal_diag (q : ℝ) (v : ℕ) (T : StandardYoungTableau μ) :
    jmDiagVal (μ := μ) q v T T = q ^ (2 * cellContent (cellOf T v)) := by
  simp [jmDiagVal]

theorem jmDiagVal_of_ne (q : ℝ) (v : ℕ) {T' T : StandardYoungTableau μ} (h : T' ≠ T) :
    jmDiagVal (μ := μ) q v T' T = 0 := by
  simp [jmDiagVal, Matrix.diagonal_apply_ne _ h]

/-- **Base case.**  Value `1` sits at `(0,0)` in every standard tableau
(`TableauCells.cellOf_one`), whose content is `0`, so the eigenvalue matrix is the identity —
matching `ρ(L₀) = ρ(1) = 1`. -/
theorem jmDiagVal_one (q : ℝ) (hcard : 0 < μ.cells.card) :
    jmDiagVal (μ := μ) q 1 = 1 := by
  unfold jmDiagVal
  rw [← Matrix.diagonal_one]
  congr 1
  funext T
  rw [cellOf_one T hcard]
  norm_num [cellContent]

/-- The content advances by the axial distance: `content(cell of k+1) = content(cell of k) + d`.
Immediate from the definition of `axialDist` as a content difference. -/
theorem cellContent_succ (T : StandardYoungTableau μ) (k : ℕ) :
    cellContent (cellOf T (k + 1)) = cellContent (cellOf T k) + axialDist T k := by
  unfold axialDist axialDistance
  ring

/-- **The inductive step, as a matrix identity.**  Conjugating the eigenvalue matrix at value
`k` by the generator matrix `genMat q k` gives the eigenvalue matrix at value `k+1`.

Every entry reduces to `Seminormal.jmStep_diag` / `jmStep_offDiag` (size-`2` orbits) or
`Seminormal.seminormalParam_sq_mul` (size-`1` orbits). -/
theorem genMat_conj_jmDiagVal (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (k : ℕ) (hk : 1 ≤ k) (hkn : k + 1 ≤ μ.cells.card) :
    genMat q k hk hkn * jmDiagVal q k * genMat q k hk hkn = jmDiagVal q (k + 1) := by
  classical
  have hkI : k ∈ Set.Icc 1 μ.cells.card := ⟨hk, by omega⟩
  have hkI' : k + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hkn⟩
  ext T' T
  set d := axialDist T k with hd
  have hd0 : d ≠ 0 := axialDist_ne_zero T hkI hkI'
  have hdq : q ^ (2 * d) ≠ 1 := zpow_ne_one hq0 hq2 (by omega)
  have hc : cellContent (cellOf T (k + 1)) = cellContent (cellOf T k) + d :=
    cellContent_succ T k
  -- collapse the inner product: the middle factor is diagonal
  have hAD : ∀ U, (genMat q k hk hkn * jmDiagVal q k :
        Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) ℝ) T' U
      = genMat q k hk hkn T' U * q ^ (2 * cellContent (cellOf U k)) := by
    intro U
    rw [Matrix.mul_apply, Finset.sum_eq_single U]
    · rw [jmDiagVal_diag]
    · intro b _ hb
      rw [jmDiagVal_of_ne q k hb, mul_zero]
    · intro h; exact absurd (Finset.mem_univ U) h
  rw [Matrix.mul_apply]
  simp only [hAD]
  by_cases hadm : SwapAdmissible T k
  · -- size-2 orbit
    set S₀ := swapTableau T k hk hkn hadm with hS₀
    have hne : S₀ ≠ T := swapTableau_ne T hk hkn hadm
    have hadm' : SwapAdmissible S₀ k := swapAdmissible_swapTableau T hk hkn hadm
    have hback : swapTableau S₀ k hk hkn hadm' = T := swapTableau_involutive T hk hkn hadm
    have hdS : axialDist S₀ k = -d := axialDist_swapTableau T hk hkn hadm
    have hcS : cellContent (cellOf S₀ k) = cellContent (cellOf T k) + d := by
      rw [hS₀, cellOf_swapTableau_self T hk hkn hadm, hc]
    rw [sum_mul_genMat_column q k hk hkn hadm
      (fun U => genMat q k hk hkn T' U * q ^ (2 * cellContent (cellOf U k)))]
    simp only [← hS₀, hcS, ← hd]
    by_cases hT' : T' = T
    · -- diagonal entry
      have h1 : genMat q k hk hkn T' T = seminormalParam q d := by
        rw [hT', genMat_diag, ← hd]
      have h2 : genMat q k hk hkn T' S₀ = offDiag q (-d) := by
        have hsw := genMat_swap q k hk hkn hadm' (by rw [hback]; exact hne.symm)
        rw [hback, hdS] at hsw
        rw [hT']; exact hsw
      have h3 : jmDiagVal q (k + 1) T' T = q ^ (2 * (cellContent (cellOf T k) + d)) := by
        rw [hT', jmDiagVal_diag, hc]
      rw [h1, h2, h3]
      have hstep := jmStep_diag q hq0 hd0 hdq (cellContent (cellOf T k))
      linear_combination hstep
    · by_cases hT'S : T' = S₀
      · -- off-diagonal entry: vanishes
        have h1 : genMat q k hk hkn T' T = offDiag q d := by
          rw [hT'S]; exact genMat_swap q k hk hkn hadm hne
        have h2 : genMat q k hk hkn T' S₀ = seminormalParam q (-d) := by
          rw [hT'S, genMat_diag, hdS]
        rw [h1, h2, jmDiagVal_of_ne q (k + 1) hT']
        have hstep := jmStep_offDiag q hq0 hdq (cellContent (cellOf T k))
        linear_combination hstep
      · -- outside the orbit: both factors vanish
        rw [genMat_apply_of_ne q k hk hkn hT' hadm hT'S,
          genMat_apply_of_ne q k hk hkn hT'S hadm' (by rw [hback]; exact hT'),
          jmDiagVal_of_ne q (k + 1) hT']
        ring
  · -- size-1 orbit: the column is the diagonal alone
    have hdpm : d = 1 ∨ d = -1 := by
      rcases axialDist_trichotomy T hkI hkI' with h | h | h
      · exact Or.inl (by rw [hd]; exact h)
      · exact Or.inr (by rw [hd]; exact h)
      · exact absurd h hadm
    rw [Finset.sum_eq_single T]
    · by_cases hT' : T' = T
      · have h1 : genMat q k hk hkn T' T = seminormalParam q d := by
          rw [hT', genMat_diag, ← hd]
        have h2 : genMat q k hk hkn T T = seminormalParam q d := by
          rw [genMat_diag, ← hd]
        have h3 : jmDiagVal q (k + 1) T' T = q ^ (2 * (cellContent (cellOf T k) + d)) := by
          rw [hT', jmDiagVal_diag, hc]
        rw [h1, h2, h3]
        have hstep := seminormalParam_sq_mul q hq0 hq2 hdpm (cellContent (cellOf T k))
        linear_combination hstep
      · rw [genMat_of_not_admissible q k hk hkn hT' hadm,
          jmDiagVal_of_ne q (k + 1) hT']
        ring
    · intro b _ hb
      rw [genMat_of_not_admissible q k hk hkn hb hadm, mul_zero]
    · intro h; exact absurd (Finset.mem_univ T) h

/-- **Ram (1997) Thm 4.1, for this construction.**  The `q`-Jucys–Murphy element `L_k` acts on
the seminormal representation as the diagonal matrix reading `q^{2·content}` at the cell holding
value `k+1`.

Induction on `k`: the base is `L₀ = 1` with value `1` at the corner (`jmDiagVal_one`), and the
step is the conjugation identity `genMat_conj_jmDiagVal`, since `L_{k+1} = σ_k L_k σ_k`. -/
theorem seminormalRep_qJM (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (hN : μ.cells.card = n + 1) :
    ∀ k : ℕ, k ≤ n →
      seminormalRep q hq0 hq2 n hN (qJM ℝ q q⁻¹ n k) = jmDiagVal q (k + 1)
  | 0, _ => by
      rw [qJM_zero, map_one, jmDiagVal_one q (by omega)]
  | (k + 1), hk => by
      have hkn : k < n := by omega
      rw [qJM_succ ℝ q q⁻¹ n hkn, map_mul, map_mul,
        seminormalRep_σ, seminormalRep_qJM q hq0 hq2 n hN k (by omega)]
      show genMat q (k + 1) _ _ * jmDiagVal q (k + 1) * genMat q (k + 1) _ _ = _
      rw [genMat_conj_jmDiagVal q hq0 hq2 (k + 1) (by omega) (by omega)]

/-- The inverse eigenvalue matrix: diagonal with `q^{-2·content}`. -/
noncomputable def jmDiagValInv (q : ℝ) (v : ℕ) :
    Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) ℝ :=
  Matrix.diagonal (fun T => q ^ (-(2 * cellContent (cellOf T v))))

theorem jmDiagVal_mul_inv (q : ℝ) (hq0 : q ≠ 0) (v : ℕ) :
    jmDiagVal (μ := μ) q v * jmDiagValInv q v = 1 := by
  rw [jmDiagVal, jmDiagValInv, Matrix.diagonal_mul_diagonal, ← Matrix.diagonal_one]
  congr 1
  funext T
  rw [← zpow_add₀ hq0]
  simp

theorem jmDiagValInv_mul (q : ℝ) (hq0 : q ≠ 0) (v : ℕ) :
    jmDiagValInv (μ := μ) q v * jmDiagVal q v = 1 := by
  rw [jmDiagVal, jmDiagValInv, Matrix.diagonal_mul_diagonal, ← Matrix.diagonal_one]
  congr 1
  funext T
  rw [← zpow_add₀ hq0]
  simp

/-- **The inverse Murphy element acts by the inverse eigenvalue.**  Derived from the two-sided
inverse `qJM · qJMInv = 1 = qJMInv · qJM` plus uniqueness of inverses, so it needs no second
induction. -/
theorem seminormalRep_qJMInv (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ)
    (hN : μ.cells.card = n + 1) (k : ℕ) (hk : k ≤ n) :
    seminormalRep q hq0 hq2 n hN (qJMInv ℝ q q⁻¹ n k) = jmDiagValInv q (k + 1) := by
  have hqi : q * q⁻¹ = 1 := mul_inv_cancel₀ hq0
  have h2 := congrArg (seminormalRep q hq0 hq2 n hN) (qJMInv_mul_qJM ℝ q q⁻¹ n hqi k hk)
  rw [map_mul, map_one, seminormalRep_qJM q hq0 hq2 n hN k hk] at h2
  -- `X · D = 1` and `D · D⁻¹ = 1` give `X = D⁻¹`
  calc seminormalRep q hq0 hq2 n hN (qJMInv ℝ q q⁻¹ n k)
      = seminormalRep q hq0 hq2 n hN (qJMInv ℝ q q⁻¹ n k) * 1 := by rw [mul_one]
    _ = seminormalRep q hq0 hq2 n hN (qJMInv ℝ q q⁻¹ n k)
          * (jmDiagVal q (k + 1) * jmDiagValInv q (k + 1)) := by
        rw [jmDiagVal_mul_inv q hq0]
    _ = (seminormalRep q hq0 hq2 n hN (qJMInv ℝ q q⁻¹ n k) * jmDiagVal q (k + 1))
          * jmDiagValInv q (k + 1) := by rw [mul_assoc]
    _ = jmDiagValInv q (k + 1) := by rw [h2, one_mul]

end SeminormalRep

end QOU.SchurWeyl
