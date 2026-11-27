import QOU.BraidsAndKnots.RationalAssociator.GRTComposite
import Mathlib.Algebra.Polynomial.Roots
import Mathlib.LinearAlgebra.Dual.Lemmas
import Mathlib.LinearAlgebra.Matrix.Notation

/-!
# Stage 4: the (5.16)-exponential, the `grt` predicate, and the doubling induction

Bean `qou-3fdg` (stage 4, epic `qou-dk7p`). Drinfeld's numbering (1991, §5): (5.12) inversion,
(5.13) the `μ = 0` hexagon, (5.14) `t`-compatibility, (5.15) the pentagon, (5.16) the group law,
(5.17)–(5.20) the linearised conditions defining `grt`.

The goal (S4) of the audit `docs/audits/2026-11-27-grt-action-pentagon-Leibniz map.md` §9–§10 is:
for `y ∈ grt`, the (5.16)-exponential `Exp(y) = Σ_k L_y^k(1)/k!` lies in `GRT₁`, where
`L_y(z) = D_y(z) + z·y`, `D_y` the Leibniz map with `D_y(A) = [y, A]`, `D_y(B) = 0`.

This file proves:

* `leibD`: the Leibniz map of `ℚ⟨A, B⟩` with prescribed values on `A, B`, built from an algebra
  map into upper-triangular `2 × 2` matrices; Leibniz rule, scaling, and `ε ∘ D = 0`.
* `expPoly y K = Σ_{k<K} L_y^k(1)/k!` and the scaling identity
  `expTerm (x • y) k = x ^ k • expTerm y k` (`expTerm_smul`): the coefficients of `Exp(xy)` in `x`.
* `coeff_mem_of_doubling`: if `Σ_j (2^j − 2) x^j c_j ∈ F` for every `x ∈ ℚ`, then `c_j ∈ F` for
  `j ≠ 1`. This replaces the grading step (G) of §10: no grading of `U4 N` is needed.
* `eval_eq_zero_of_doubling`: the induction of §10, abstractly. A family of polynomials in `x`
  whose `x`-linear coefficients vanish, and which satisfies the **doubling hypothesis**
  `δ(2x) ≡ 2 δ(x) (mod F (d+1))` whenever all of them lie in `F d`, vanishes identically.
* `GrtU4 N y`: the `x`-linear parts of the four conditions of `GRT1U4 N` (Drinfeld's
  (5.17)–(5.20), (5.14) in the polynomial form of `TCompatPoly`).
* `defectPoly`: the four defects of `expPoly (x • y) K`, as polynomials in `x` over `U4 N`;
  `evq_defectPoly_*` evaluates them and `coeff_one_defectPoly` shows their `x`-linear
  coefficients are the `GrtU4` expressions.
* `grt1U4_expPoly_of_doubling`: **conditional (S4).** If `y` satisfies `GrtU4 N y` and the
  defects of `Exp(xy)` satisfy the doubling hypothesis, then `expPoly (x • y) K ∈ GRT1U4 N`
  for every `x`.

The doubling hypothesis is what steps (P) (one-parameter law `Exp(2xy) = Exp(xy) ∘ Exp(xy)`)
and (A) (top-defect additivity under (5.16)) of §10 would give. Neither is proved here; the
hypothesis is a named argument of the theorem, not an axiom. Nothing analytic is used.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

open Polynomial

/-! ### A Leibniz map on the free algebra with prescribed values on generators -/

section Leibniz

/-- The algebra map `p ↦ [[p, D p], [0, p]]` with `D (ι i) = d i`. -/
noncomputable def triHom (d : Fin 2 → FreeAlgebra ℚ (Fin 2)) :
    FreeAlgebra ℚ (Fin 2) →ₐ[ℚ] Matrix (Fin 2) (Fin 2) (FreeAlgebra ℚ (Fin 2)) :=
  FreeAlgebra.lift ℚ (fun i => !![FreeAlgebra.ι ℚ i, d i; 0, FreeAlgebra.ι ℚ i])

/-- The Leibniz map with `D (ι i) = d i`: the upper-right entry of `triHom d`. -/
noncomputable def leibD (d : Fin 2 → FreeAlgebra ℚ (Fin 2)) (p : FreeAlgebra ℚ (Fin 2)) :
    FreeAlgebra ℚ (Fin 2) :=
  triHom d p 0 1

theorem triHom_entries (d : Fin 2 → FreeAlgebra ℚ (Fin 2)) (p : FreeAlgebra ℚ (Fin 2)) :
    triHom d p 0 0 = p ∧ triHom d p 1 0 = 0 ∧ triHom d p 1 1 = p := by
  induction p using FreeAlgebra.induction with
  | grade0 r => simp [Matrix.algebraMap_matrix_apply]
  | grade1 i => simp [triHom]
  | mul p q hp hq =>
    obtain ⟨p0, p1, p2⟩ := hp
    obtain ⟨q0, q1, q2⟩ := hq
    simp only [map_mul, Matrix.mul_apply, Fin.sum_univ_two, p0, p1, p2, q0, q1, q2]
    simp
  | add p q hp hq =>
    obtain ⟨p0, p1, p2⟩ := hp
    obtain ⟨q0, q1, q2⟩ := hq
    simp [map_add, p0, p1, p2, q0, q1, q2]

/-- **Leibniz rule.** -/
theorem leibD_mul (d : Fin 2 → FreeAlgebra ℚ (Fin 2)) (p q : FreeAlgebra ℚ (Fin 2)) :
    leibD d (p * q) = p * leibD d q + leibD d p * q := by
  obtain ⟨p0, -, -⟩ := triHom_entries d p
  obtain ⟨-, -, q2⟩ := triHom_entries d q
  simp only [leibD, map_mul, Matrix.mul_apply, Fin.sum_univ_two, p0, q2]

theorem leibD_add (d : Fin 2 → FreeAlgebra ℚ (Fin 2)) (p q : FreeAlgebra ℚ (Fin 2)) :
    leibD d (p + q) = leibD d p + leibD d q := by
  simp [leibD, map_add]

theorem leibD_smul (d : Fin 2 → FreeAlgebra ℚ (Fin 2)) (r : ℚ) (p : FreeAlgebra ℚ (Fin 2)) :
    leibD d (r • p) = r • leibD d p := by
  simp [leibD, map_smul]

theorem leibD_algebraMap (d : Fin 2 → FreeAlgebra ℚ (Fin 2)) (r : ℚ) :
    leibD d (algebraMap ℚ (FreeAlgebra ℚ (Fin 2)) r) = 0 := by
  simp [leibD, Matrix.algebraMap_matrix_apply]

theorem leibD_one (d : Fin 2 → FreeAlgebra ℚ (Fin 2)) : leibD d 1 = 0 := by
  simpa using leibD_algebraMap d 1

theorem leibD_ι (d : Fin 2 → FreeAlgebra ℚ (Fin 2)) (i : Fin 2) :
    leibD d (FreeAlgebra.ι ℚ i) = d i := by
  simp [leibD, triHom]

/-- Scaling the prescribed values scales the Leibniz map. -/
theorem leibD_smul_left (d : Fin 2 → FreeAlgebra ℚ (Fin 2)) (x : ℚ) (p : FreeAlgebra ℚ (Fin 2)) :
    leibD (x • d) p = x • leibD d p := by
  induction p using FreeAlgebra.induction with
  | grade0 r => simp [leibD_algebraMap]
  | grade1 i => simp [leibD_ι]
  | mul p q hp hq => rw [leibD_mul, leibD_mul, hp, hq, mul_smul_comm, smul_mul_assoc, smul_add]
  | add p q hp hq => rw [leibD_add, leibD_add, hp, hq, smul_add]

/-- `ε ∘ D = 0` when `ε ∘ d = 0`. -/
theorem algebraMapInv_leibD (d : Fin 2 → FreeAlgebra ℚ (Fin 2))
    (hd : ∀ i, FreeAlgebra.algebraMapInv (d i) = 0) (p : FreeAlgebra ℚ (Fin 2)) :
    FreeAlgebra.algebraMapInv (leibD d p) = 0 := by
  induction p using FreeAlgebra.induction with
  | grade0 r => simp [leibD_algebraMap]
  | grade1 i => rw [leibD_ι, hd]
  | mul p q hp hq => rw [leibD_mul, map_add, map_mul, map_mul, hp, hq, mul_zero, zero_mul, add_zero]
  | add p q hp hq => rw [leibD_add, map_add, hp, hq, add_zero]

end Leibniz

/-! ### The (5.16)-exponential -/

section Exp

/-- The values of `D_y`: `D_y(A) = [y, A]`, `D_y(B) = 0`. -/
noncomputable def dY (y : FreeAlgebra ℚ (Fin 2)) : Fin 2 → FreeAlgebra ℚ (Fin 2) :=
  ![y * FreeAlgebra.ι ℚ 0 - FreeAlgebra.ι ℚ 0 * y, 0]

theorem dY_smul (x : ℚ) (y : FreeAlgebra ℚ (Fin 2)) : dY (x • y) = x • dY y := by
  funext i
  fin_cases i <;> simp [dY, smul_sub]

theorem algebraMapInv_dY (y : FreeAlgebra ℚ (Fin 2)) (i : Fin 2) :
    FreeAlgebra.algebraMapInv (dY y i) = 0 := by
  fin_cases i <;> simp [dY, FreeAlgebra.algebraMapInv]

/-- `L_y(z) = D_y(z) + z·y`: the generator of the (5.16)-flow in the direction `y`. -/
noncomputable def Ly (y z : FreeAlgebra ℚ (Fin 2)) : FreeAlgebra ℚ (Fin 2) :=
  leibD (dY y) z + z * y

theorem Ly_smul_left (x : ℚ) (y z : FreeAlgebra ℚ (Fin 2)) : Ly (x • y) z = x • Ly y z := by
  rw [Ly, Ly, dY_smul, leibD_smul_left, mul_smul_comm, smul_add]

theorem Ly_smul_right (y : FreeAlgebra ℚ (Fin 2)) (r : ℚ) (z : FreeAlgebra ℚ (Fin 2)) :
    Ly y (r • z) = r • Ly y z := by
  rw [Ly, Ly, leibD_smul, smul_mul_assoc, smul_add]

theorem iterate_Ly_smul (x : ℚ) (y : FreeAlgebra ℚ (Fin 2)) (k : ℕ) :
    (Ly (x • y))^[k] 1 = x ^ k • (Ly y)^[k] 1 := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [Function.iterate_succ_apply', Function.iterate_succ_apply', ih, Ly_smul_left,
      Ly_smul_right, smul_smul, pow_succ, mul_comm x]

/-- The `k`-th term `L_y^k(1)/k!` of the (5.16)-exponential. -/
noncomputable def expTerm (y : FreeAlgebra ℚ (Fin 2)) (k : ℕ) : FreeAlgebra ℚ (Fin 2) :=
  ((k.factorial : ℚ)⁻¹) • (Ly y)^[k] 1

/-- The truncated (5.16)-exponential `Σ_{k<K} L_y^k(1)/k!`. -/
noncomputable def expPoly (y : FreeAlgebra ℚ (Fin 2)) (K : ℕ) : FreeAlgebra ℚ (Fin 2) :=
  ∑ k ∈ Finset.range K, expTerm y k

/-- **Grading in `x`:** `Exp(xy) = Σ_k x^k e_k` with `e_k = expTerm y k`. -/
theorem expTerm_smul (x : ℚ) (y : FreeAlgebra ℚ (Fin 2)) (k : ℕ) :
    expTerm (x • y) k = x ^ k • expTerm y k := by
  rw [expTerm, expTerm, iterate_Ly_smul, smul_comm]

theorem expPoly_smul (x : ℚ) (y : FreeAlgebra ℚ (Fin 2)) (K : ℕ) :
    expPoly (x • y) K = ∑ k ∈ Finset.range K, x ^ k • expTerm y k := by
  simp only [expPoly, expTerm_smul]

theorem expTerm_zero (y : FreeAlgebra ℚ (Fin 2)) : expTerm y 0 = 1 := by
  simp [expTerm]

theorem expTerm_one (y : FreeAlgebra ℚ (Fin 2)) : expTerm y 1 = y := by
  simp [expTerm, Ly, leibD_one]

theorem algebraMapInv_Ly (y : FreeAlgebra ℚ (Fin 2)) (hy : FreeAlgebra.algebraMapInv y = 0)
    (z : FreeAlgebra ℚ (Fin 2)) : FreeAlgebra.algebraMapInv (Ly y z) = 0 := by
  rw [Ly, map_add, map_mul, algebraMapInv_leibD _ (algebraMapInv_dY y), hy, mul_zero, add_zero]

/-- The constant term of `Exp(y)` is `1` when `y` has none. -/
theorem algebraMapInv_expPoly (y : FreeAlgebra ℚ (Fin 2)) (hy : FreeAlgebra.algebraMapInv y = 0)
    {K : ℕ} (hK : 1 ≤ K) : FreeAlgebra.algebraMapInv (expPoly y K) = 1 := by
  obtain ⟨K, rfl⟩ := Nat.exists_eq_add_of_le' hK
  rw [expPoly, Finset.sum_range_succ', map_add, map_sum, expTerm_zero, map_one]
  have : ∀ k ∈ Finset.range K, FreeAlgebra.algebraMapInv (expTerm y (k + 1)) = 0 := by
    intro k _
    rw [expTerm, map_smul, Function.iterate_succ_apply', algebraMapInv_Ly y hy, smul_zero]
  rw [Finset.sum_eq_zero this, zero_add]

end Exp

/-! ### Polynomials in `x` and the doubling lemma -/

section Doubling

variable {R : Type*} [Ring R] [Algebra ℚ R]

/-- Evaluation of a polynomial over `R` at the central element `x ∈ ℚ`. -/
noncomputable def evq (x : ℚ) : R[X] →+* R :=
  eval₂RingHom' (RingHom.id R) (algebraMap ℚ R x) (fun a => (Algebra.commutes x a).symm)

theorem mul_algebraMap_eq_smul (r : ℚ) (a : R) : a * algebraMap ℚ R r = r • a := by
  rw [Algebra.smul_def, Algebra.commutes]

@[simp] theorem evq_C (x : ℚ) (a : R) : evq x (C a) = a := by simp [evq]

@[simp] theorem evq_X (x : ℚ) : evq x (X : R[X]) = algebraMap ℚ R x := by simp [evq]

theorem evq_eq_sum (x : ℚ) (p : R[X]) :
    evq x p = ∑ j ∈ Finset.range (p.natDegree + 1), x ^ j • p.coeff j := by
  change eval₂ (RingHom.id R) (algebraMap ℚ R x) p = _
  rw [eval₂_eq_sum_range]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [RingHom.id_apply, ← map_pow, mul_algebraMap_eq_smul]

theorem two_pow_ne_two {j : ℕ} (hj : j ≠ 1) : (2 : ℚ) ^ j ≠ 2 := by
  intro h
  apply hj
  have h' : (2 : ℕ) ^ j = 2 ^ 1 := by exact_mod_cast h
  exact Nat.pow_right_injective le_rfl h'

/-- **The doubling lemma.** In a `ℚ`-module, if `Σ_{j<n} (2^j − 2) x^j c_j ∈ F` for every
`x ∈ ℚ`, then `c_j ∈ F` for every `j < n` with `j ≠ 1`. -/
theorem coeff_mem_of_doubling {M : Type*} [AddCommGroup M] [Module ℚ M] (F : Submodule ℚ M)
    (c : ℕ → M) (n : ℕ)
    (h : ∀ x : ℚ, ∑ j ∈ Finset.range n, (((2 : ℚ) ^ j - 2) * x ^ j) • c j ∈ F)
    {j : ℕ} (hj : j < n) (hj1 : j ≠ 1) : c j ∈ F := by
  rw [← Submodule.Quotient.mk_eq_zero, ← Module.forall_dual_apply_eq_zero_iff ℚ]
  intro φ
  set P : ℚ[X] := ∑ i ∈ Finset.range n,
    C (((2 : ℚ) ^ i - 2) * φ (Submodule.Quotient.mk (c i))) * X ^ i with hPdef
  haveI : Infinite ℚ := Infinite.of_injective (Nat.cast : ℕ → ℚ) Nat.cast_injective
  have hP : P = 0 := by
    apply Polynomial.funext
    intro r
    have h0 : φ (F.mkQ (∑ i ∈ Finset.range n, (((2 : ℚ) ^ i - 2) * r ^ i) • c i)) = 0 := by
      rw [Submodule.mkQ_apply, (Submodule.Quotient.mk_eq_zero F).2 (h r), map_zero]
    simp only [map_sum, map_smul, Submodule.mkQ_apply, smul_eq_mul] at h0
    simp only [hPdef, eval_finset_sum, eval_mul, eval_C, eval_pow, eval_zero]
    rw [← h0]
    refine Finset.sum_congr rfl fun i _ => ?_
    simp only [Polynomial.eval_X]
    ring
  have hc := congrArg (fun p : ℚ[X] => p.coeff j) hP
  simp only [hPdef, finset_sum_coeff, coeff_C_mul_X_pow, coeff_zero] at hc
  rw [Finset.sum_ite_eq, if_pos (Finset.mem_range.2 hj)] at hc
  exact (mul_eq_zero.1 hc).resolve_left (sub_ne_zero.2 (two_pow_ne_two hj1))

/-- **The doubling induction (§10 of the audit), abstractly.** Let `F 0 ⊇ … ⊇ F N` be
submodules of `R` with `F 0 = R` and `F N = 0`, and `D i` a family of polynomials in `x` with
vanishing `x`-linear coefficients. Suppose (the doubling hypothesis) that whenever every
`D i (x)` lies in `F d`, every `D i (2x) − 2 D i (x)` lies in `F (d+1)`. Then every `D i (x)`
vanishes. No grading is used. -/
theorem eval_eq_zero_of_doubling {ι : Type*} (F : ℕ → Submodule ℚ R) (hF0 : ∀ r, r ∈ F 0)
    (N : ℕ) (hFN : ∀ r ∈ F N, r = 0) (D : ι → R[X]) (hlin : ∀ i, (D i).coeff 1 = 0)
    (hdouble : ∀ d, (∀ i x, evq x (D i) ∈ F d) →
      ∀ i x, evq (2 * x) (D i) - (2 : ℚ) • evq x (D i) ∈ F (d + 1)) :
    ∀ i x, evq x (D i) = 0 := by
  have key : ∀ d, ∀ i x, evq x (D i) ∈ F d := by
    intro d
    induction d with
    | zero => exact fun i x => hF0 _
    | succ d ih =>
      intro i x
      have hx : ∀ x : ℚ, ∑ j ∈ Finset.range ((D i).natDegree + 1),
          (((2 : ℚ) ^ j - 2) * x ^ j) • (D i).coeff j ∈ F (d + 1) := by
        intro x
        have h := hdouble d ih i x
        rw [evq_eq_sum, evq_eq_sum, Finset.smul_sum, ← Finset.sum_sub_distrib] at h
        convert h using 2 with j _
        rw [smul_smul, ← sub_smul, mul_pow]
        congr 1
        ring
      rw [evq_eq_sum]
      refine Submodule.sum_mem _ fun j hj => ?_
      by_cases hj1 : j = 1
      · subst hj1; rw [hlin, smul_zero]; exact Submodule.zero_mem _
      · exact Submodule.smul_mem _ _
          (coeff_mem_of_doubling _ _ _ hx (Finset.mem_range.1 hj) hj1)
  exact fun i x => hFN _ (key N i x)

omit [Algebra ℚ R] in
/-- The `x`-linear coefficient of a product. -/
theorem coeff_one_mul (p q : R[X]) :
    (p * q).coeff 1 = p.coeff 0 * q.coeff 1 + p.coeff 1 * q.coeff 0 := by
  rw [coeff_mul, Finset.Nat.sum_antidiagonal_eq_sum_range_succ_mk]
  simp [Finset.sum_range_succ]

/-- `Exp(xy)` evaluated at `(a, b)`, as a polynomial in `x`. -/
noncomputable def EP (y : FreeAlgebra ℚ (Fin 2)) (K : ℕ) (a b : R) : R[X] :=
  ∑ k ∈ Finset.range K, C (eval a b (expTerm y k)) * X ^ k

theorem evq_EP (y : FreeAlgebra ℚ (Fin 2)) (K : ℕ) (a b : R) (x : ℚ) :
    evq x (EP y K a b) = eval a b (expPoly (x • y) K) := by
  rw [EP, expPoly_smul, map_sum, map_sum]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [map_mul, map_pow, evq_C, evq_X, ← map_pow, mul_algebraMap_eq_smul, map_smul]

theorem coeff_EP (y : FreeAlgebra ℚ (Fin 2)) (K : ℕ) (a b : R) (j : ℕ) :
    (EP y K a b).coeff j = if j < K then eval a b (expTerm y j) else 0 := by
  simp only [EP, finset_sum_coeff, coeff_C_mul_X_pow]
  rw [Finset.sum_ite_eq]
  simp [Finset.mem_range]

theorem coeff_zero_EP (y : FreeAlgebra ℚ (Fin 2)) {K : ℕ} (hK : 2 ≤ K) (a b : R) :
    (EP y K a b).coeff 0 = 1 := by
  rw [coeff_EP, if_pos (by omega), expTerm_zero, map_one]

theorem coeff_one_EP (y : FreeAlgebra ℚ (Fin 2)) {K : ℕ} (hK : 2 ≤ K) (a b : R) :
    (EP y K a b).coeff 1 = eval a b y := by
  rw [coeff_EP, if_pos (by omega), expTerm_one]

end Doubling

/-! ### The `grt` predicate and the defects of `Exp(xy)` in `U4 N` -/

section U4

variable {N : ℕ}

/-- **`grt` in `U4 N`.** The `x`-linear parts of the four conditions of `GRT1U4 N` at
`g = 1 + x y`: Drinfeld's (5.17), (5.18) at the universal family, the linearisation of
(5.14) in the form `TCompatPoly`, and (5.20) at the universal family, with `ε(y) = 0`. -/
structure GrtU4 (N : ℕ) (y : FreeAlgebra ℚ (Fin 2)) : Prop where
  const : FreeAlgebra.algebraMapInv y = 0
  lin512 : ∀ a b : U4 N, a ∈ Fil N 1 → b ∈ Fil N 1 → eval a b y + eval b a y = 0
  lin513 : eval (t N 1) (t N 0) y + eval (t N 3) (t N 1) y + eval (t N 0) (t N 3) y = 0
  lin514 : ∀ u v w : U4 N, u ∈ Fil N 1 → v ∈ Fil N 1 → w ∈ Fil N 1 → DK3 u v w →
    eval v w y * v + v * eval w v y = eval u w y * (v + w) + (v + w) * eval w u y
  lin515 : eval (t N 0) (t N 3 + t N 4) y + eval (t N 1 + t N 3) (t N 5) y =
    eval (t N 3) (t N 5) y + eval (t N 0 + t N 1) (t N 4 + t N 5) y + eval (t N 0) (t N 3) y

/-- The instances of the four `GRT1U4` conditions: (5.12) and (5.14) at admissible arguments,
(5.13) and (5.15) at the universal family. -/
inductive GRTDefect (N : ℕ) : Type
  | inv (a b : U4 N) (ha : a ∈ Fil N 1) (hb : b ∈ Fil N 1)
  | hex
  | tc (u v w : U4 N) (hu : u ∈ Fil N 1) (hv : v ∈ Fil N 1) (hw : w ∈ Fil N 1) (h : DK3 u v w)
  | pent

/-- The defect of each condition for `Exp(xy)`, as a polynomial in `x`. -/
noncomputable def defectPoly (y : FreeAlgebra ℚ (Fin 2)) (K : ℕ) : GRTDefect N → (U4 N)[X]
  | .inv a b _ _ => EP y K a b * EP y K b a - 1
  | .hex => EP y K (t N 1) (t N 0) * EP y K (t N 3) (t N 1) * EP y K (t N 0) (t N 3) - 1
  | .tc u v w _ _ _ _ => EP y K v w * C v * EP y K w v - (EP y K u w * C (v + w) * EP y K w u - C w)
  | .pent => EP y K (t N 0) (t N 3 + t N 4) * EP y K (t N 1 + t N 3) (t N 5) -
      EP y K (t N 3) (t N 5) * EP y K (t N 0 + t N 1) (t N 4 + t N 5) * EP y K (t N 0) (t N 3)

/-- The `x`-linear coefficients of the defects are the `GrtU4` expressions, so they vanish
for `y ∈ grt`. -/
theorem coeff_one_defectPoly {y : FreeAlgebra ℚ (Fin 2)} (hy : GrtU4 N y) {K : ℕ} (hK : 2 ≤ K)
    (i : GRTDefect N) : (defectPoly y K i).coeff 1 = 0 := by
  have c0 := coeff_zero_EP (R := U4 N) y hK
  have c1 := coeff_one_EP (R := U4 N) y hK
  cases i with
  | inv a b ha hb =>
    simp only [defectPoly, coeff_sub, coeff_one_mul, c0, c1, coeff_one]
    simpa [add_comm] using hy.lin512 a b ha hb
  | hex =>
    simp only [defectPoly, coeff_sub, coeff_one_mul, mul_coeff_zero, c0, c1, coeff_one]
    simp only [one_mul, mul_one]
    convert hy.lin513 using 1; abel_nf
  | tc u v w hu hv hw h =>
    simp only [defectPoly, coeff_sub, coeff_one_mul, mul_coeff_zero, c0, c1, coeff_C]
    have := hy.lin514 u v w hu hv hw h
    simp only [one_mul, mul_one, if_neg one_ne_zero, if_true, sub_zero,
      zero_add]
    rw [sub_eq_zero]
    convert this using 1 <;> abel
  | pent =>
    simp only [defectPoly, coeff_sub, coeff_one_mul, mul_coeff_zero, c0, c1]
    have := hy.lin515
    simp only [one_mul, mul_one]
    rw [sub_eq_zero]
    convert this using 1 <;> abel

/-- **Conditional (S4).** If `y ∈ grt` (`GrtU4 N y`) and the defects of `Exp(xy)` satisfy the
doubling hypothesis — what the one-parameter law (P) and top-defect additivity (A) of §10 would
give — then `Exp(xy)` satisfies the four `GRT₁` conditions in `U4 N`, for every `x ∈ ℚ`. -/
theorem grt1U4_expPoly_of_doubling {y : FreeAlgebra ℚ (Fin 2)} (hy : GrtU4 N y) {K : ℕ}
    (hK : 2 ≤ K)
    (hdouble : ∀ d, (∀ i x, evq x (defectPoly (N := N) y K i) ∈ Fil N d) →
      ∀ i x, evq (2 * x) (defectPoly (N := N) y K i) - (2 : ℚ) • evq x (defectPoly y K i) ∈
        Fil N (d + 1)) (x : ℚ) :
    GRT1U4 N (expPoly (x • y) K) := by
  have hz := eval_eq_zero_of_doubling (Fil N) mem_Fil_zero N (fun r hr => eq_zero_of_mem_Fil hr)
    (defectPoly y K) (coeff_one_defectPoly hy hK) hdouble
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · apply algebraMapInv_expPoly _ _ (by omega)
    rw [map_smul, hy.const, smul_zero]
  · intro a b ha hb
    have := hz (.inv a b ha hb) x
    simp only [defectPoly, map_sub, map_mul, map_one, evq_EP] at this
    exact sub_eq_zero.1 this
  · have := hz .hex x
    simp only [defectPoly, map_sub, map_mul, map_one, evq_EP] at this
    unfold Hexagon
    simp only [map_one, mul_one]
    exact (sub_eq_zero.1 this).symm
  · intro u v w hu hv hw h
    have := hz (.tc u v w hu hv hw h) x
    simp only [defectPoly, map_sub, map_mul, evq_C, evq_EP] at this
    exact sub_eq_zero.1 this
  · have := hz .pent x
    simp only [defectPoly, map_sub, map_mul, evq_EP] at this
    exact sub_eq_zero.1 this

end U4

end QOU.BraidsAndKnots.RationalAssociator
