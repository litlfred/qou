import QOU.BraidsAndKnots.RationalAssociator.GRTValued
import Mathlib.Algebra.DualNumber

/-!
# Stage 4 without the doubling hypothesis: the flow argument in the dual numbers

Bean `qou-3fdg` (stage 4, epic `qou-dk7p`). Drinfeld's numbering (1991, §5): (5.12) inversion,
(5.13) the `μ = 0` hexagon, (5.14) `t`-compatibility, (5.15) the pentagon, (5.16) the group law.

`GRTFlow.lean` proves `grt1U4_expPoly_of_doubling`: for `y ∈ grt` (`GrtU4 N y`), the truncated
(5.16)-exponential `Exp(xy) = expPoly (x • y) K` lies in `GRT1U4 N`, **given** a doubling
hypothesis on its defects. This file removes that hypothesis (`grt1U4_expPoly`), under
`N ≤ K`: the truncation of the exponential must reach the nilpotency order of `U4 N`.

## The argument

Let `D = U4 N[ε]` be the dual numbers over `U4 N` (`ε² = 0`, `ε` central). For `a, b ∈ Fil N 1`
put `Ĥ(a, b) = 1 + ε·y(a, b)`; by (5.17) these are units with `Ĥ(a, b)⁻¹ = Ĥ(b, a)`.

1. **Flow identity.** With `G = Exp(xy)`, the value of `Exp((x + ε)y)` at `(a, b)` is the
   (5.16)-composite `G ∘ Ĥ` at `(a, b)`: `G(Ĥ a Ĥ⁻¹, b)·Ĥ` (`evD_EP`). This is the
   Leibniz rule (`eval_dual`) together with `L_y(e_k) = (k+1)·e_{k+1}` and `e_K(a, b) = 0` for
   `K ≥ N` (`eval_expTerm_eq_zero`); the latter is where `N ≤ K` enters.
2. **Exactness of `Ĥ`.** The conditions on the values `Ĥ` that the action theorems of
   `GRTValued.lean` need are *exact* in `D`, because `ε² = 0`: they are the four `GrtU4`
   identities (5.17)–(5.20).
3. **Transport.** By the action theorems, each defect of `Exp((x + ε)y)` at the universal family
   is (a unit times) the image of the same defect of `Exp(xy)` under an algebra map
   `Λ : U4 N → D` sending each generator to an element with constant part in `Fil N 1` and
   `ε`-part in `Fil N 2`. Such a map sends `Fil N d` into `GoodAt d`: constant part in
   `Fil N d`, `ε`-part in `Fil N (d + 1)` (`goodAt_of_map`).
4. **Induction.** If the defect polynomial `P` lies in `Fil N d` at every `x`, the `ε`-part of
   `P(x + ε)`, which is `Σ_j j x^{j-1} P_j`, lies in `Fil N (d + 1)` at every `x`, so every
   coefficient `P_j` with `j ≥ 1` does (`coeff_mem_of_forall`); `P_0 = 0`. Hence
   `P(x) ∈ Fil N (d + 1)`, and at `d = N` the defect vanishes.

No doubling identity and no top-defect additivity is used. Each defect is handled on its own.

The hypothesis `N ≤ K` is not a weakening: for `K < N` the truncation `expPoly (x • y) K`
drops terms of `x`-degree `K` that need not vanish in `U4 N`, and (5.12) can fail at order
`x^K`. Everything is algebraic over `ℚ`.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

open Polynomial TrivSqZeroExt

/-! ### The word filtration of `ℚ⟨A, B⟩` -/

section FreeFil

/-- The span of the words of length at least `m` in `ℚ⟨A, B⟩`. -/
def FF (m : ℕ) : Submodule ℚ (FreeAlgebra ℚ (Fin 2)) :=
  Submodule.span ℚ {p | ∃ w : List (Fin 2), m ≤ w.length ∧ p = (w.map (FreeAlgebra.ι ℚ)).prod}

theorem word_mem_FF {m : ℕ} (w : List (Fin 2)) (hw : m ≤ w.length) :
    (w.map (FreeAlgebra.ι ℚ)).prod ∈ FF m :=
  Submodule.subset_span ⟨w, hw, rfl⟩

theorem FF_anti {m n : ℕ} (h : m ≤ n) : FF n ≤ FF m :=
  Submodule.span_mono fun _ ⟨w, hw, e⟩ => ⟨w, le_trans h hw, e⟩

theorem mul_mem_FF {a b : ℕ} {p q : FreeAlgebra ℚ (Fin 2)} (hp : p ∈ FF a) (hq : q ∈ FF b) :
    p * q ∈ FF (a + b) := by
  have h := Submodule.mul_mem_mul hp hq
  rw [FF, FF, Submodule.span_mul_span] at h
  refine Submodule.span_le.mpr ?_ h
  rintro _ ⟨u, ⟨w1, h1, rfl⟩, v, ⟨w2, h2, rfl⟩, rfl⟩
  refine Submodule.subset_span ⟨w1 ++ w2, by simp; omega, ?_⟩
  simp [List.map_append, List.prod_append]

theorem mul_mem_FF' {a b c : ℕ} (h : a + b = c) {p q : FreeAlgebra ℚ (Fin 2)} (hp : p ∈ FF a)
    (hq : q ∈ FF b) : p * q ∈ FF c := h ▸ mul_mem_FF hp hq

theorem mem_FF_zero (p : FreeAlgebra ℚ (Fin 2)) : p ∈ FF 0 := by
  induction p using FreeAlgebra.induction with
  | grade0 r =>
    rw [Algebra.algebraMap_eq_smul_one]
    exact Submodule.smul_mem _ r (by simpa using word_mem_FF (m := 0) [] le_rfl)
  | grade1 i => simpa using word_mem_FF (m := 0) [i] (by simp)
  | mul a b ha hb => simpa using mul_mem_FF ha hb
  | add a b ha hb => exact add_mem ha hb

/-- Every element is its constant term plus an element of `FF 1`. -/
theorem sub_algebraMapInv_mem_FF (p : FreeAlgebra ℚ (Fin 2)) :
    p - algebraMap ℚ _ (FreeAlgebra.algebraMapInv p) ∈ FF 1 := by
  induction p using FreeAlgebra.induction with
  | grade0 r => simp
  | grade1 i =>
    simpa [FreeAlgebra.algebraMapInv] using word_mem_FF (m := 1) [i] (by simp)
  | mul a b ha hb =>
    have e : a * b - algebraMap ℚ _ (FreeAlgebra.algebraMapInv (a * b)) =
        (a - algebraMap ℚ _ (FreeAlgebra.algebraMapInv a)) * b +
          FreeAlgebra.algebraMapInv a •
            (b - algebraMap ℚ _ (FreeAlgebra.algebraMapInv b)) := by
      rw [map_mul, map_mul, Algebra.smul_def]; noncomm_ring
    rw [e]
    exact add_mem (by simpa using mul_mem_FF ha (mem_FF_zero b)) (Submodule.smul_mem _ _ hb)
  | add a b ha hb =>
    have e : a + b - algebraMap ℚ _ (FreeAlgebra.algebraMapInv (a + b)) =
        (a - algebraMap ℚ _ (FreeAlgebra.algebraMapInv a)) +
          (b - algebraMap ℚ _ (FreeAlgebra.algebraMapInv b)) := by
      rw [map_add, map_add]; abel
    rw [e]; exact add_mem ha hb

theorem mem_FF_one_of_const {p : FreeAlgebra ℚ (Fin 2)} (hp : FreeAlgebra.algebraMapInv p = 0) :
    p ∈ FF 1 := by
  simpa [hp] using sub_algebraMapInv_mem_FF p

/-- A Leibniz map whose values on the generators lie in `FF 2` raises the word filtration. -/
theorem leibD_mem_FF (d : Fin 2 → FreeAlgebra ℚ (Fin 2)) (hd : ∀ i, d i ∈ FF 2) {m : ℕ}
    {p : FreeAlgebra ℚ (Fin 2)} (hp : p ∈ FF m) : leibD d p ∈ FF (m + 1) := by
  have hw : ∀ w : List (Fin 2), leibD d (w.map (FreeAlgebra.ι ℚ)).prod ∈ FF (w.length + 1) := by
    intro w
    induction w with
    | nil => simp [leibD_one]
    | cons i w ih =>
      rw [List.map_cons, List.prod_cons, leibD_mul, leibD_ι]
      refine add_mem ?_ ?_
      · have := mul_mem_FF (word_mem_FF (m := 1) [i] (by simp)) ih
        simp only [List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, mul_one] at this
        exact FF_anti (by simp; omega) this
      · exact FF_anti (by simp; omega) (mul_mem_FF (hd i) (word_mem_FF w le_rfl))
  induction hp using Submodule.span_induction with
  | mem p h =>
    obtain ⟨w, hw', rfl⟩ := h
    exact FF_anti (by omega) (hw w)
  | zero =>
    rw [show leibD d 0 = 0 by simpa using leibD_smul d 0 0]; exact zero_mem _
  | add p q _ _ hp hq => rw [leibD_add]; exact add_mem hp hq
  | smul r p _ hp => rw [leibD_smul]; exact Submodule.smul_mem _ r hp

theorem Ly_mem_FF {y : FreeAlgebra ℚ (Fin 2)} (hy : y ∈ FF 1) {m : ℕ}
    {z : FreeAlgebra ℚ (Fin 2)} (hz : z ∈ FF m) : Ly y z ∈ FF (m + 1) := by
  have hd : ∀ i, dY y i ∈ FF 2 := by
    intro i
    fin_cases i
    · simp only [dY, Fin.zero_eta, Matrix.cons_val_zero]
      have h0 : FreeAlgebra.ι ℚ (0 : Fin 2) ∈ FF 1 := by
        simpa using word_mem_FF (m := 1) [0] (by simp)
      have h1 : y * FreeAlgebra.ι ℚ (0 : Fin 2) ∈ FF 2 := mul_mem_FF' (by norm_num) hy h0
      have h2 : FreeAlgebra.ι ℚ (0 : Fin 2) * y ∈ FF 2 := mul_mem_FF' (by norm_num) h0 hy
      exact sub_mem h1 h2
    · simp [dY]
  exact add_mem (leibD_mem_FF _ hd hz) (mul_mem_FF hz hy)

theorem expTerm_mem_FF {y : FreeAlgebra ℚ (Fin 2)} (hy : y ∈ FF 1) (k : ℕ) :
    expTerm y k ∈ FF k := by
  have : ∀ k, (Ly y)^[k] 1 ∈ FF k := by
    intro k
    induction k with
    | zero => exact mem_FF_zero _
    | succ k ih => rw [Function.iterate_succ_apply']; exact Ly_mem_FF hy ih
  exact Submodule.smul_mem _ _ (this k)

end FreeFil

/-! ### The filtration of `U4 N` under evaluation -/

section EvalFil

variable {N : ℕ}

theorem Fil_anti {m n : ℕ} (h : m ≤ n) : Fil N n ≤ Fil N m :=
  Submodule.span_mono fun _ ⟨w, hw, e⟩ => ⟨w, le_trans h hw, e⟩

theorem eval_mem_Fil {a b : U4 N} (ha : a ∈ Fil N 1) (hb : b ∈ Fil N 1) {m : ℕ}
    {p : FreeAlgebra ℚ (Fin 2)} (hp : p ∈ FF m) : eval a b p ∈ Fil N m := by
  have hw : ∀ w : List (Fin 2), eval a b (w.map (FreeAlgebra.ι ℚ)).prod ∈ Fil N w.length := by
    intro w
    induction w with
    | nil => simpa using mem_Fil_zero (1 : U4 N)
    | cons i w ih =>
      rw [List.map_cons, List.prod_cons, map_mul]
      have hi : eval a b (FreeAlgebra.ι ℚ i) ∈ Fil N 1 := by
        fin_cases i
        · simpa using ha
        · simpa using hb
      simpa [Nat.add_comm] using mul_mem_Fil hi ih
  induction hp using Submodule.span_induction with
  | mem p h =>
    obtain ⟨w, hw', rfl⟩ := h
    exact Fil_anti hw' (hw w)
  | zero => simp
  | add p q _ _ hp hq => rw [map_add]; exact add_mem hp hq
  | smul r p _ hp => rw [map_smul]; exact Submodule.smul_mem _ r hp

/-- `e_K(a, b) = 0` for `K ≥ N`: the term of `x`-degree `K` of `Exp(xy)` vanishes in `U4 N`. -/
theorem eval_expTerm_eq_zero {y : FreeAlgebra ℚ (Fin 2)} (hy : FreeAlgebra.algebraMapInv y = 0)
    {a b : U4 N} (ha : a ∈ Fil N 1) (hb : b ∈ Fil N 1) {K : ℕ} (hNK : N ≤ K) :
    eval a b (expTerm y K) = 0 :=
  eq_zero_of_mem_Fil (Fil_anti hNK (eval_mem_Fil ha hb (expTerm_mem_FF (mem_FF_one_of_const hy) K)))

end EvalFil

/-! ### Dual numbers -/

section Dual

variable {R : Type*} [Ring R] [Algebra ℚ R]

theorem one_add_inr_mul (A B : R) :
    ((1 + inr A) * (1 + inr B) : DualNumber R) = 1 + inr (A + B) := by
  ext <;> simp [add_comm]

theorem conj_one_add_inr (A a : R) :
    ((1 + inr A) * inl a * (1 + inr (-A)) : DualNumber R) = inl a + inr (A * a - a * A) := by
  ext
  · simp
  · simp [snd_mul, sub_eq_add_neg, add_comm]

/-- **Leibniz rule in the dual numbers.** -/
theorem eval_dual (d : Fin 2 → FreeAlgebra ℚ (Fin 2)) (a b : R) (p : FreeAlgebra ℚ (Fin 2)) :
    eval (inl a + inr (eval a b (d 0)) : DualNumber R) (inl b + inr (eval a b (d 1))) p =
      inl (eval a b p) + inr (eval a b (leibD d p)) := by
  induction p using FreeAlgebra.induction with
  | grade0 r =>
    rw [AlgHom.commutes, AlgHom.commutes, leibD_algebraMap, map_zero, inr_zero, add_zero,
      algebraMap_eq_inl']
  | grade1 i =>
    fin_cases i
    · simp [leibD_ι]
    · simp [leibD_ι]
  | mul p q hp hq =>
    rw [map_mul, hp, hq, leibD_mul, map_mul, map_add, map_mul, map_mul]
    ext <;> simp [add_comm]
  | add p q hp hq =>
    rw [map_add, hp, hq, leibD_add, map_add, map_add, inl_add, inr_add]
    abel

/-- The point `x + ε`. -/
noncomputable def xiD (x : ℚ) : DualNumber R := inl (algebraMap ℚ R x) + inr 1

theorem commute_inl_xiD (x : ℚ) (a : R) : Commute (inl a : DualNumber R) (xiD x) := by
  ext <;> simp [xiD, Algebra.commutes]

/-- Evaluation of a polynomial over `R` at `x + ε`. -/
noncomputable def evD (x : ℚ) : R[X] →+* DualNumber R :=
  eval₂RingHom' (inlHom R R) (xiD x) (commute_inl_xiD x)

@[simp] theorem evD_C (x : ℚ) (a : R) : evD x (C a) = inl a := by simp [evD]

@[simp] theorem evD_X (x : ℚ) : evD x (X : R[X]) = xiD x := by simp [evD]

theorem fst_xiD_pow (x : ℚ) (j : ℕ) : ((xiD x : DualNumber R) ^ j).fst = algebraMap ℚ R (x ^ j) := by
  rw [fst_pow]; simp [xiD]

theorem snd_xiD_pow (x : ℚ) (j : ℕ) :
    ((xiD x : DualNumber R) ^ j).snd = algebraMap ℚ R ((j : ℚ) * x ^ (j - 1)) := by
  induction j with
  | zero => simp
  | succ j ih =>
    rw [pow_succ, snd_mul, ih, fst_xiD_pow]
    have e1 : (xiD x : DualNumber R).snd = 1 := by simp [xiD]
    have e2 : (xiD x : DualNumber R).fst = algebraMap ℚ R x := by simp [xiD]
    rw [e1, e2, smul_eq_mul, MulOpposite.smul_eq_mul_unop, MulOpposite.unop_op, mul_one,
      ← map_mul, ← map_add]
    congr 1
    rcases j with _ | j
    · simp
    · simp only [Nat.add_sub_cancel, Nat.cast_add, Nat.cast_one, Nat.cast_succ]; ring

theorem evD_C_mul_X_pow (x : ℚ) (c : R) (j : ℕ) :
    evD x (C c * X ^ j) = inl (x ^ j • c) + inr (((j : ℚ) * x ^ (j - 1)) • c) := by
  rw [map_mul, map_pow, evD_C, evD_X]
  ext
  · rw [fst_mul, fst_xiD_pow, fst_inl, fst_add, fst_inl, fst_inr, add_zero,
      mul_algebraMap_eq_smul]
  · rw [snd_mul, snd_xiD_pow, snd_inl, fst_inl, smul_zero, add_zero, smul_eq_mul,
      mul_algebraMap_eq_smul, snd_add, snd_inl, snd_inr, zero_add]

theorem evD_eq_sum (x : ℚ) (P : R[X]) {n : ℕ} (hn : P.natDegree < n) :
    evD x P = ∑ j ∈ Finset.range n, evD x (C (P.coeff j) * X ^ j) := by
  change eval₂ (inlHom R R) (xiD x) P = _
  rw [eval₂_eq_sum_range' _ hn]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [map_mul, map_pow, evD_C, evD_X]; rfl

theorem fst_evD (x : ℚ) (P : R[X]) : (evD x P).fst = evq x P := by
  rw [evD_eq_sum x P (Nat.lt_succ_self _), fst_sum, evq_eq_sum]
  simp [evD_C_mul_X_pow]

theorem snd_evD (x : ℚ) (P : R[X]) {n : ℕ} (hn : P.natDegree < n) :
    (evD x P).snd = ∑ j ∈ Finset.range n, ((j : ℚ) * x ^ (j - 1)) • P.coeff j := by
  rw [evD_eq_sum x P hn, snd_sum]
  simp [evD_C_mul_X_pow]

/-- If `Σ_{j<n} x^j c_j ∈ F` for every `x ∈ ℚ`, then every `c_j ∈ F`. -/
theorem coeff_mem_of_forall {M : Type*} [AddCommGroup M] [Module ℚ M] (F : Submodule ℚ M)
    (c : ℕ → M) (n : ℕ) (h : ∀ x : ℚ, ∑ j ∈ Finset.range n, x ^ j • c j ∈ F)
    {j : ℕ} (hj : j < n) : c j ∈ F := by
  rw [← Submodule.Quotient.mk_eq_zero, ← Module.forall_dual_apply_eq_zero_iff ℚ]
  intro φ
  set P : ℚ[X] := ∑ i ∈ Finset.range n, C (φ (Submodule.Quotient.mk (c i))) * X ^ i with hPdef
  haveI : Infinite ℚ := Infinite.of_injective (Nat.cast : ℕ → ℚ) Nat.cast_injective
  have hP : P = 0 := by
    apply Polynomial.funext
    intro r
    have h0 : φ (F.mkQ (∑ i ∈ Finset.range n, r ^ i • c i)) = 0 := by
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
  exact hc

/-- **The induction step.** If `P_0 = 0` and the `ε`-part of `P(x + ε)` lies in `F` for every
`x`, then `P(x) ∈ F` for every `x`. -/
theorem evq_mem_of_snd_mem (F : Submodule ℚ R) (P : R[X]) (h0 : P.coeff 0 = 0)
    (h : ∀ x : ℚ, (evD x P).snd ∈ F) (x : ℚ) : evq x P ∈ F := by
  set m := P.natDegree
  have hc : ∀ i < m, P.coeff (i + 1) ∈ F := by
    have hx : ∀ x : ℚ, ∑ i ∈ Finset.range m, x ^ i • (((i : ℚ) + 1) • P.coeff (i + 1)) ∈ F := by
      intro x
      have := h x
      rw [snd_evD x P (Nat.lt_succ_self m), Finset.sum_range_succ'] at this
      simpa [smul_smul, mul_comm] using this
    intro i hi
    have := coeff_mem_of_forall F (fun i => ((i : ℚ) + 1) • P.coeff (i + 1)) m hx hi
    have h' := Submodule.smul_mem F (((i : ℚ) + 1)⁻¹) this
    rwa [smul_smul, inv_mul_cancel₀ (by positivity), one_smul] at h'
  rw [evq_eq_sum, Finset.sum_range_succ']
  refine add_mem (Submodule.sum_mem _ fun i hi => Submodule.smul_mem _ _
    (hc i (Finset.mem_range.1 hi))) ?_
  simp [h0]

end Dual

/-! ### Constant part in `Fil N d`, `ε`-part in `Fil N (d + 1)` -/

section Good

variable {N : ℕ}

/-- `z ∈ U4 N[ε]` has constant part in `Fil N d` and `ε`-part in `Fil N (d + 1)`. -/
def GoodAt (d : ℕ) (z : DualNumber (U4 N)) : Prop :=
  z.fst ∈ Fil N d ∧ z.snd ∈ Fil N (d + 1)

theorem mul_mem_Fil' {a b c : ℕ} (h : a + b = c) {x y : U4 N} (hx : x ∈ Fil N a)
    (hy : y ∈ Fil N b) : x * y ∈ Fil N c := h ▸ mul_mem_Fil hx hy

theorem GoodAt.mul {a b c : ℕ} (h : a + b = c) {z w : DualNumber (U4 N)} (hz : GoodAt a z)
    (hw : GoodAt b w) : GoodAt c (z * w) := by
  refine ⟨?_, ?_⟩
  · rw [fst_mul]; exact mul_mem_Fil' h hz.1 hw.1
  · rw [snd_mul, smul_eq_mul, MulOpposite.smul_eq_mul_unop, MulOpposite.unop_op]
    exact add_mem (mul_mem_Fil' (by omega) hz.1 hw.2) (mul_mem_Fil' (by omega) hz.2 hw.1)

theorem GoodAt.add {d : ℕ} {z w : DualNumber (U4 N)} (hz : GoodAt d z) (hw : GoodAt d w) :
    GoodAt d (z + w) :=
  ⟨by rw [fst_add]; exact add_mem hz.1 hw.1, by rw [snd_add]; exact add_mem hz.2 hw.2⟩

theorem GoodAt.neg {d : ℕ} {z : DualNumber (U4 N)} (hz : GoodAt d z) : GoodAt d (-z) :=
  ⟨by rw [fst_neg]; exact neg_mem hz.1, by rw [snd_neg]; exact neg_mem hz.2⟩

theorem GoodAt.sub {d : ℕ} {z w : DualNumber (U4 N)} (hz : GoodAt d z) (hw : GoodAt d w) :
    GoodAt d (z - w) := by
  rw [sub_eq_add_neg]; exact hz.add hw.neg

theorem GoodAt.smul {d : ℕ} {z : DualNumber (U4 N)} (r : ℚ) (hz : GoodAt d z) :
    GoodAt d (r • z) :=
  ⟨by rw [fst_smul]; exact Submodule.smul_mem _ r hz.1,
    by rw [snd_smul]; exact Submodule.smul_mem _ r hz.2⟩

theorem GoodAt.mono {d d' : ℕ} (h : d' ≤ d) {z : DualNumber (U4 N)} (hz : GoodAt d z) :
    GoodAt d' z :=
  ⟨Fil_anti h hz.1, Fil_anti (by omega) hz.2⟩

theorem goodAt_zero (d : ℕ) : GoodAt d (0 : DualNumber (U4 N)) :=
  ⟨by simp, by simp⟩

theorem goodAt_one : GoodAt 0 (1 : DualNumber (U4 N)) :=
  ⟨mem_Fil_zero _, by simp⟩

theorem goodAt_inl {d : ℕ} {a : U4 N} (h : a ∈ Fil N d) : GoodAt d (inl a : DualNumber (U4 N)) :=
  ⟨by simpa using h, by simp⟩

theorem goodAt_one_add_inr {A : U4 N} (h : A ∈ Fil N 1) :
    GoodAt 0 (1 + inr A : DualNumber (U4 N)) :=
  ⟨mem_Fil_zero _, by simpa using h⟩

theorem goodAt_prod_word (s : Fin 6 → DualNumber (U4 N)) (hs : ∀ i, GoodAt 1 (s i))
    (w : List (Fin 6)) : GoodAt w.length (w.map s).prod := by
  induction w with
  | nil => simpa using (goodAt_one (N := N))
  | cons i w ih =>
    rw [List.map_cons, List.prod_cons]
    exact GoodAt.mul (by simp [Nat.add_comm]) (hs i) ih

theorem eq_zero_of_goodAt {z : DualNumber (U4 N)} (h : GoodAt N z) : z = 0 :=
  TrivSqZeroExt.ext (by simpa using eq_zero_of_mem_Fil h.1)
    (by simpa using eq_zero_of_mem_Fil (Fil_anti (by omega) h.2))

/-- An algebra map `U4 N → U4 N[ε]` whose values on the generators are `GoodAt 1` sends
`Fil N d` into `GoodAt d`. -/
theorem goodAt_of_map (Λ : U4 N →ₐ[ℚ] DualNumber (U4 N)) (hΛ : ∀ i, GoodAt 1 (Λ (t N i)))
    {d : ℕ} {z : U4 N} (hz : z ∈ Fil N d) : GoodAt d (Λ z) := by
  induction hz using Submodule.span_induction with
  | mem p h =>
    obtain ⟨w, hw, rfl⟩ := h
    rw [map_list_prod, List.map_map]
    exact (goodAt_prod_word (fun i => Λ (t N i)) hΛ w).mono hw
  | zero => rw [map_zero]; exact goodAt_zero d
  | add p q _ _ hp hq => rw [map_add]; exact hp.add hq
  | smul r p _ hp => rw [map_smul]; exact hp.smul r

/-- The universal property of `U4 N` for a `DK4` family of `GoodAt 1` elements of `U4 N[ε]`. -/
noncomputable def liftD (s : Fin 6 → DualNumber (U4 N))
    (hdk : DK4 (s 0) (s 1) (s 2) (s 3) (s 4) (s 5)) (hs : ∀ i, GoodAt 1 (s i)) :
    U4 N →ₐ[ℚ] DualNumber (U4 N) :=
  lift N s hdk (fun w hw => eq_zero_of_goodAt (by
    have := goodAt_prod_word s hs w; rwa [hw] at this))

@[simp] theorem liftD_t (s : Fin 6 → DualNumber (U4 N)) (hdk) (hs) (i : Fin 6) :
    liftD s hdk hs (t N i) = s i := by
  simp [liftD]

theorem goodAt_liftD (s : Fin 6 → DualNumber (U4 N)) (hdk) (hs : ∀ i, GoodAt 1 (s i))
    {d : ℕ} {z : U4 N} (hz : z ∈ Fil N d) : GoodAt d (liftD s hdk hs z) :=
  goodAt_of_map _ (fun i => by rw [liftD_t]; exact hs i) hz

/-- A `DK3` family of `GoodAt 1` elements, extended by zeros, as an algebra map. -/
noncomputable def liftD3 (u v w : DualNumber (U4 N)) (h : DK3 u v w) (hu : GoodAt 1 u)
    (hv : GoodAt 1 v) (hw : GoodAt 1 w) : U4 N →ₐ[ℚ] DualNumber (U4 N) :=
  liftD ![u, v, 0, w, 0, 0] (by simpa using h.toDK4) (by
    intro i; fin_cases i <;> simp [hu, hv, hw, goodAt_zero])

@[simp] theorem liftD3_t0 (u v w : DualNumber (U4 N)) (h hu hv hw) :
    liftD3 u v w h hu hv hw (t N 0) = u := by simp [liftD3]

@[simp] theorem liftD3_t1 (u v w : DualNumber (U4 N)) (h hu hv hw) :
    liftD3 u v w h hu hv hw (t N 1) = v := by simp [liftD3]

@[simp] theorem liftD3_t3 (u v w : DualNumber (U4 N)) (h hu hv hw) :
    liftD3 u v w h hu hv hw (t N 3) = w := by simp [liftD3]

theorem goodAt_liftD3 (u v w : DualNumber (U4 N)) (h hu hv hw) {d : ℕ} {z : U4 N}
    (hz : z ∈ Fil N d) : GoodAt d (liftD3 u v w h hu hv hw z) :=
  goodAt_liftD _ _ _ hz

end Good

/-! ### The units `Ĥ(a, b) = 1 + ε·y(a, b)` and the flow identity -/

section Flow

variable {N : ℕ} {y : FreeAlgebra ℚ (Fin 2)}

/-- `1 + ε·y(a, b)`. -/
noncomputable def gam (y : FreeAlgebra ℚ (Fin 2)) (a b : U4 N) : DualNumber (U4 N) :=
  1 + inr (eval a b y)

/-- `γ(p, q) = 1 + ε·y(p₀, q₀)` on `U4 N[ε]`, `p₀` the constant part. -/
noncomputable def gamD (y : FreeAlgebra ℚ (Fin 2)) (p q : DualNumber (U4 N)) :
    DualNumber (U4 N) :=
  gam y p.fst q.fst

theorem commProp_gamD (y : FreeAlgebra ℚ (Fin 2)) : CommProp (gamD (N := N) y) := by
  intro p q z hp hq
  have hp' : Commute p.fst z.fst := by
    have := congrArg TrivSqZeroExt.fst hp.eq
    simpa [fst_mul] using this
  have hq' : Commute q.fst z.fst := by
    have := congrArg TrivSqZeroExt.fst hq.eq
    simpa [fst_mul] using this
  have hY := (commute_eval hp' hq' y).eq
  show gam y p.fst q.fst * z = z * gam y p.fst q.fst
  ext
  · simp [gam]
  · simp only [gam, snd_mul, fst_add, fst_one, fst_inr, snd_add, snd_one, snd_inr, add_zero,
      zero_add, smul_eq_mul, MulOpposite.smul_eq_mul_unop, MulOpposite.unop_op, one_mul, mul_one]
    rw [hY]; abel

theorem gam_mul (a b c d : U4 N) :
    gam y a b * gam y c d = 1 + inr (eval a b y + eval c d y) :=
  one_add_inr_mul _ _

/-- The unit `Ĥ(a, b)`, with inverse `Ĥ(b, a)` by (5.17). -/
noncomputable def Hh (hy : GrtU4 N y) (a b : U4 N) (ha : a ∈ Fil N 1) (hb : b ∈ Fil N 1) :
    (DualNumber (U4 N))ˣ where
  val := gam y a b
  inv := gam y b a
  val_inv := by rw [gam_mul, hy.lin512 a b ha hb, inr_zero, add_zero]
  inv_val := by rw [gam_mul, hy.lin512 b a hb ha, inr_zero, add_zero]

@[simp] theorem val_Hh (hy : GrtU4 N y) (a b : U4 N) (ha hb) :
    (Hh hy a b ha hb : DualNumber (U4 N)) = gam y a b := rfl

@[simp] theorem val_inv_Hh (hy : GrtU4 N y) (a b : U4 N) (ha hb) :
    (↑(Hh hy a b ha hb)⁻¹ : DualNumber (U4 N)) = gam y b a := rfl

theorem Hh_inv (hy : GrtU4 N y) (a b : U4 N) (ha hb) :
    (Hh hy a b ha hb)⁻¹ = Hh hy b a hb ha := Units.ext rfl

theorem goodAt_gam (hy : GrtU4 N y) {a b : U4 N} (ha : a ∈ Fil N 1) (hb : b ∈ Fil N 1) :
    GoodAt 0 (gam y a b) :=
  goodAt_one_add_inr (eval_mem_Fil ha hb (mem_FF_one_of_const hy.const))

theorem Ly_add (y z w : FreeAlgebra ℚ (Fin 2)) : Ly y (z + w) = Ly y z + Ly y w := by
  rw [Ly, Ly, Ly, leibD_add, add_mul]; abel

/-- `L_y` as a `ℚ`-linear map. -/
noncomputable def LyL (y : FreeAlgebra ℚ (Fin 2)) :
    FreeAlgebra ℚ (Fin 2) →ₗ[ℚ] FreeAlgebra ℚ (Fin 2) where
  toFun := Ly y
  map_add' := Ly_add y
  map_smul' := Ly_smul_right y

theorem Ly_expTerm (y : FreeAlgebra ℚ (Fin 2)) (k : ℕ) :
    Ly y (expTerm y k) = ((k : ℚ) + 1) • expTerm y (k + 1) := by
  rw [expTerm, Ly_smul_right, expTerm, Function.iterate_succ_apply', smul_smul]
  congr 1
  rw [Nat.factorial_succ]
  push_cast
  have : ((k : ℚ) + 1) ≠ 0 := by positivity
  rw [mul_inv, ← mul_assoc, mul_inv_cancel₀ this, one_mul]

theorem eval_Ly_expPoly (hy : GrtU4 N y) {a b : U4 N} (ha : a ∈ Fil N 1) (hb : b ∈ Fil N 1)
    {K : ℕ} (hK : 1 ≤ K) (hNK : N ≤ K) (x : ℚ) :
    eval a b (Ly y (expPoly (x • y) K)) =
      ∑ j ∈ Finset.range K, ((j : ℚ) * x ^ (j - 1)) • eval a b (expTerm y j) := by
  obtain ⟨M, rfl⟩ : ∃ M, K = M + 1 := ⟨K - 1, by omega⟩
  rw [expPoly_smul]
  change eval a b (LyL y (∑ k ∈ Finset.range (M + 1), x ^ k • expTerm y k)) = _
  rw [map_sum, map_sum]
  simp only [LyL, LinearMap.coe_mk, AddHom.coe_mk, Ly_smul_right, Ly_expTerm, map_smul,
    smul_smul]
  rw [Finset.sum_range_succ, Finset.sum_range_succ',
    eval_expTerm_eq_zero hy.const ha hb hNK, smul_zero, add_zero]
  simp only [Nat.cast_zero, zero_mul, zero_smul, add_zero]
  refine Finset.sum_congr rfl fun k _ => ?_
  congr 1
  push_cast
  ring

theorem snd_evD_EP (K : ℕ) (x : ℚ) (a b : U4 N) :
    (evD x (EP y K a b)).snd =
      ∑ j ∈ Finset.range K, ((j : ℚ) * x ^ (j - 1)) • eval a b (expTerm y j) := by
  rw [EP, map_sum, snd_sum]
  simp [evD_C_mul_X_pow]

/-- **The flow identity.** At `(a, b)`, `Exp((x + ε)y) = Exp(xy) ∘ Ĥ` in the sense of (5.16). -/
theorem evD_EP (hy : GrtU4 N y) {K : ℕ} (hK : 1 ≤ K) (hNK : N ≤ K) (x : ℚ) {a b : U4 N}
    (ha : a ∈ Fil N 1) (hb : b ∈ Fil N 1) :
    evD x (EP y K a b) =
      actEval (expPoly (x • y) K) (inl a) (inl b) (Hh hy a b ha hb) := by
  have h512 := hy.lin512 a b ha hb
  have hconj : ((Hh hy a b ha hb : DualNumber (U4 N)) * inl a *
      (↑(Hh hy a b ha hb)⁻¹ : DualNumber (U4 N))) =
      inl a + inr (eval a b (dY y 0)) := by
    have hba : eval b a y = -eval a b y := eq_neg_of_add_eq_zero_right h512
    rw [val_Hh, val_inv_Hh, gam, gam, hba, conj_one_add_inr]
    simp [dY]
  have hb' : (inl b : DualNumber (U4 N)) = inl b + inr (eval a b (dY y 1)) := by simp [dY]
  unfold actEval
  rw [hconj, hb', eval_dual, val_Hh, gam]
  ext
  · rw [fst_evD, evq_EP]; simp
  · rw [snd_evD_EP, ← eval_Ly_expPoly hy ha hb hK hNK x, Ly, map_add, map_mul]
    simp [snd_mul]; abel

end Flow

end QOU.BraidsAndKnots.RationalAssociator
