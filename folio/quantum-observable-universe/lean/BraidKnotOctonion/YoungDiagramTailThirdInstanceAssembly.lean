import BraidKnotOctonion.DepthTwoHookClassification
import BraidKnotOctonion.DepthTwoBinomialMoments
import BraidKnotOctonion.YoungDiagramTailThirdInstance

/-!
# The depth-2 tail `ν_{n−2}(n)` in closed form

`nuV n (n − 2) = nuDepthTwoClosedForm n` for every `n ≥ 6`.

The proof restricts the Plancherel sum to the depth-2 shapes
(`DepthTwoHookClassification`), evaluates `f^λ` and `ω₃` on each shape, folds the shapes into one
sum over `k ∈ [0, n]`, and collapses that sum (`DepthTwoBinomialMoments`).

Audit: `docs/audits/2026-11-27-covariance-kernel-depth-two-tail.md`; bean `qou-swk4`.
-/

set_option autoImplicit false

namespace QOU.BraidsAndKnots.YoungDiagramTailThirdInstanceAssembly

open QOU.BraidsAndKnots.YoungDiagramKernel
open QOU.BraidsAndKnots.YoungDiagramTransposeBridge
open QOU.BraidsAndKnots.YoungDiagramKernelPincer
open QOU.BraidsAndKnots.DepthTwoHookClassification
open QOU.BraidsAndKnots.DepthTwoBinomialMoments
open QOU.BraidsAndKnots.SecondMomentKernelVanishes

/-! ## Family A: `(a, 3, 1^c)` -/

/-- Family A is a weakly decreasing list when `a ≥ 3`. -/
theorem sorted_famA (a c : ℕ) (ha : 3 ≤ a) : (a :: 3 :: List.replicate c 1).Sorted (· ≥ ·) := by
  simp [List.Sorted, List.pairwise_cons, List.pairwise_replicate, List.mem_replicate]
  omega

/-- Family A has positive parts. -/
theorem pos_famA (a c : ℕ) (ha : 3 ≤ a) : ∀ x ∈ a :: 3 :: List.replicate c 1, 0 < x := by
  simp [List.mem_replicate]
  omega

/-- Hook product of `(b + 3, 3, 1^c)`. -/
theorem hookProd_famA (b c : ℕ) :
    hookProd ((b + 3) :: 3 :: List.replicate c 1)
      = (b + c + 4) * (b + 3) * (b + 2) * b.factorial * ((c + 3) * 2) * c.factorial := by
  set l := (b + 3) :: 3 :: List.replicate c 1
  have hs : l.Sorted (· ≥ ·) := sorted_famA (b + 3) c (by omega)
  have hc := QOU.BraidsAndKnots.DepthOneHookClassification.countP_pos_replicate_one
  have hcj0 : (conj l).getD 0 0 = c + 2 := by
    rw [conj_getD _ hs]
    simp [l, hc]
  have hcj1 : (conj l).getD 1 0 = 2 := by
    rw [conj_getD _ hs]
    simp [l]
  have hcj2 : (conj l).getD 2 0 = 2 := by
    rw [conj_getD _ hs]
    simp [l]
  have hcjj : ∀ j, 3 ≤ j → j < b + 3 → (conj l).getD j 0 = 1 := by
    intro j hj3 hjb
    rw [conj_getD _ hs]
    have h1 : ¬ j < 3 := by omega
    have h2 : 1 ≤ j := by omega
    simp [l, hjb, h1, h2]
  rw [hookProd_eq_finset_prod]
  have hlen : l.length = c + 2 := by simp [l]
  rw [hlen, Finset.prod_range_succ', Finset.prod_range_succ']
  have hrows : ∀ i ∈ Finset.range c,
      (∏ j ∈ Finset.range (l.getD (i + 1 + 1) 0),
        (l.getD (i + 1 + 1) 0 + (conj l).getD j 0 - j - (i + 1 + 1) - 1))
      = c - i := by
    intro i hi
    have hgd : l.getD (i + 1 + 1) 0 = 1 := by
      simp only [l, List.getD_cons_succ]
      exact getD_replicate_of_lt 1 0 c i (Finset.mem_range.mp hi)
    rw [hgd, Finset.prod_range_one, hcj0]
    omega
  rw [Finset.prod_congr rfl hrows, prod_range_sub_eq_factorial]
  have hrow1 :
      (∏ j ∈ Finset.range (l.getD 1 0),
        (l.getD 1 0 + (conj l).getD j 0 - j - 1 - 1))
      = (c + 3) * 2 := by
    have hgd1 : l.getD 1 0 = 3 := rfl
    rw [hgd1, Finset.prod_range_succ', Finset.prod_range_succ', Finset.prod_range_one, hcj0,
      hcj1, hcj2]
    have e : 3 + (c + 2) - 0 - 1 - 1 = c + 3 := by omega
    rw [e]
    norm_num
    ring
  have hrow0 :
      (∏ j ∈ Finset.range (l.getD 0 0),
        (l.getD 0 0 + (conj l).getD j 0 - j - 0 - 1))
      = (b + c + 4) * (b + 3) * (b + 2) * b.factorial := by
    have hgd0 : l.getD 0 0 = b + 3 := rfl
    rw [hgd0, Finset.prod_range_succ', Finset.prod_range_succ', Finset.prod_range_succ']
    have hgj : ∀ j ∈ Finset.range b,
        (b + 3 + (conj l).getD (j + 1 + 1 + 1) 0 - (j + 1 + 1 + 1) - 0 - 1) = b - j := by
      intro j hj
      rw [hcjj (j + 1 + 1 + 1) (by omega) (by have := Finset.mem_range.mp hj; omega)]
      omega
    rw [Finset.prod_congr rfl hgj, prod_range_sub_eq_factorial, hcj0, hcj1, hcj2]
    have e0 : b + 3 + (c + 2) - 0 - 0 - 1 = b + c + 4 := by omega
    have e1 : b + 3 + 2 - (0 + 1) - 0 - 1 = b + 3 := by omega
    have e2 : b + 3 + 2 - (0 + 1 + 1) - 0 - 1 = b + 2 := by omega
    rw [e0, e1, e2]
    ring
  rw [hrow1, hrow0]
  ring

/-- Dimension of `(b + 3, 3, 1^c)`, division-free:
`2(n − 2)·f = (b + 1)(c + 2)(c + 1)·C(n, c + 3)` with `n = b + c + 6`. -/
theorem mul_sytDim_famA (b c : ℕ) :
    2 * (b + c + 4) * sytDim ((b + 3) :: 3 :: List.replicate c 1)
      = (b + 1) * (c + 2) * (c + 1) * (b + c + 6).choose (c + 3) := by
  set l := (b + 3) :: 3 :: List.replicate c 1
  have hs : l.Sorted (· ≥ ·) := sorted_famA (b + 3) c (by omega)
  have hpos : ∀ x ∈ l, 0 < x := pos_famA (b + 3) c (by omega)
  have hsum : l.sum = b + c + 6 := by
    simp only [l, List.sum_cons, sum_replicate_one]
    omega
  have hmul : sytDim l * hookProd l = (b + c + 6).factorial := by
    rw [YoungDiagramKernelDimPos.sytDim_eq_numSYTenum l hs hpos,
      YoungDiagramKernelDimPos.hookProd_eq_prodHooks l hs, ← hsum]
    exact QOU.Mathlib.SYTEnum.numSYTenum_mul_prodHooks l hs hpos
  have hhp := hookProd_famA b c
  have hfc : (c + 3).factorial = (c + 3) * (c + 2) * (c + 1) * c.factorial := by
    simp [Nat.factorial_succ]
    ring
  have hfb : (b + 3).factorial = (b + 3) * (b + 2) * (b + 1) * b.factorial := by
    simp [Nat.factorial_succ]
    ring
  have hchoose :
      (b + c + 6).choose (c + 3) * (c + 3).factorial * (b + 3).factorial
        = (b + c + 6).factorial := by
    have h := Nat.choose_mul_factorial_mul_factorial (show c + 3 ≤ b + c + 6 by omega)
    rwa [show b + c + 6 - (c + 3) = b + 3 by omega] at h
  have hF : 0 < (c + 3).factorial * (b + 3).factorial :=
    Nat.mul_pos (Nat.factorial_pos _) (Nat.factorial_pos _)
  apply Nat.mul_right_cancel hF
  calc 2 * (b + c + 4) * sytDim l * ((c + 3).factorial * (b + 3).factorial)
      = (sytDim l * hookProd l) * ((b + 1) * (c + 2) * (c + 1)) := by
        rw [hfc, hfb, hhp]; ring
    _ = (b + 1) * (c + 2) * (c + 1)
          * ((b + c + 6).choose (c + 3) * (c + 3).factorial * (b + 3).factorial) := by
        rw [hmul, hchoose]; ring
    _ = (b + 1) * (c + 2) * (c + 1) * (b + c + 6).choose (c + 3)
          * ((c + 3).factorial * (b + 3).factorial) := by ring

/-- Content squares of `(a, 3, 1^c)`. -/
theorem contentSq_famA (a c : ℕ) :
    contentSq (a :: 3 :: List.replicate c 1)
      = (∑ j ∈ Finset.range a, ((j : ℤ)) ^ 2) + 2
        + ∑ t ∈ Finset.range c, ((t : ℤ) + 2) ^ 2 := by
  rw [contentSq_eq_finset_sum]
  have hlen : (a :: 3 :: List.replicate c 1).length = c + 2 := by simp
  rw [hlen, Finset.sum_range_succ', Finset.sum_range_succ']
  have hrow0 : (a :: 3 :: List.replicate c 1).getD 0 0 = a := rfl
  have hrow1 : (a :: 3 :: List.replicate c 1).getD 1 0 = 3 := rfl
  have htail : ∑ i ∈ Finset.range c,
      ∑ j ∈ Finset.range ((a :: 3 :: List.replicate c 1).getD (i + 1 + 1) 0),
        ((j : ℤ) - ((i + 1 + 1 : ℕ) : ℤ)) ^ 2
      = ∑ i ∈ Finset.range c, ((i : ℤ) + 2) ^ 2 := by
    refine Finset.sum_congr rfl fun i hi => ?_
    have hgd : (a :: 3 :: List.replicate c 1).getD (i + 1 + 1) 0 = 1 := by
      rw [List.getD_cons_succ, List.getD_cons_succ]
      exact getD_replicate_of_lt 1 0 c i (Finset.mem_range.mp hi)
    rw [hgd, Finset.sum_range_one]
    push_cast
    ring
  rw [hrow0, hrow1, htail]
  have h3 : ∑ j ∈ Finset.range 3, ((j : ℤ) - ((1 : ℕ) : ℤ)) ^ 2 = 2 := by decide
  rw [h3]
  simp only [Nat.cast_zero, sub_zero]
  ring

/-- `6·ω₃` of `(a, 3, 1^c)` with `n = a + c + 3`. -/
theorem six_mul_omega3_famA (n a c : ℕ) (hn : n = a + c + 3) :
    6 * omega3 n (a :: 3 :: List.replicate c 1)
      = ((a : ℤ) - 1) * a * (2 * a - 1) + 12 + ((c : ℤ) + 1) * ((c : ℤ) + 2) * (2 * c + 3) - 6
        - 3 * (n : ℤ) * ((n : ℤ) - 1) := by
  have harm := six_mul_sum_range_sq a
  have hleg : 6 * ∑ t ∈ Finset.range c, ((t : ℤ) + 2) ^ 2
      = ((c : ℤ) + 1) * ((c : ℤ) + 2) * (2 * c + 3) - 6 := by
    have h := six_mul_sum_range_sq (c + 2)
    rw [Finset.sum_range_succ', Finset.sum_range_succ'] at h
    have hcongr : ∑ k ∈ Finset.range c, (((k + 1 + 1 : ℕ) : ℤ)) ^ 2
        = ∑ t ∈ Finset.range c, ((t : ℤ) + 2) ^ 2 := by
      refine Finset.sum_congr rfl fun t _ => ?_
      push_cast
      ring
    rw [hcongr] at h
    push_cast at h
    linarith
  have hcentre : ((n * (n - 1) / 2 : ℕ) : ℤ) * 2 = (n : ℤ) * ((n : ℤ) - 1) := by
    have hZ : ((2 * (n * (n - 1) / 2) : ℕ) : ℤ) = ((n * (n - 1) : ℕ) : ℤ) :=
      congrArg (fun m : ℕ => (m : ℤ)) (two_mul_choose_two n)
    rw [Nat.cast_mul, Nat.cast_ofNat, Nat.cast_mul, Nat.cast_sub (by omega : 1 ≤ n),
      Nat.cast_one] at hZ
    linarith
  unfold omega3
  rw [contentSq_famA a c]
  linarith

/-- The transpose of family B `(b + 2, 2, 2, 1^c)` is family A `(c + 3, 3, 1^b)`. -/
theorem conj_famB (b c : ℕ) :
    conj ((b + 2) :: 2 :: 2 :: List.replicate c 1) = (c + 3) :: 3 :: List.replicate b 1 := by
  have hc := QOU.BraidsAndKnots.DepthOneHookClassification.countP_pos_replicate_one
  unfold conj
  rw [List.headD_cons, show b + 2 = b + 1 + 1 from rfl, List.range_succ_eq_map,
    List.range_succ_eq_map]
  simp only [List.map_cons, List.map_map]
  congr 1
  · simp [hc]
  congr 1
  · simp
  · refine List.eq_replicate_iff.mpr ⟨by simp, fun x hx => ?_⟩
    simp only [List.mem_map, List.mem_range, Function.comp_apply] at hx
    obtain ⟨j, hj, rfl⟩ := hx
    have h1 : j + 1 + 1 < b + 1 + 1 := by omega
    have h2 : ¬ j + 1 + 1 < 2 := by omega
    simp [h1, h2]

/-! ## Each shape's term -/

/-- The weight `(f^λ)²·6ω₃(λ)` of a shape in the depth-2 sum. -/
noncomputable def shapeTerm (n : ℕ) (l : List ℕ) : ℤ := (sytDim l : ℤ) ^ 2 * (6 * omega3 n l)

/-- Family A at `k = i + 3`: `4(n − 2)²·(f²·6ω₃) = g(k)²·W(k)·C(n,k)²`. -/
theorem four_mul_shapeTerm_row (m i : ℕ) (hi : i ≤ m) :
    4 * (((m + 6 : ℕ) : ℤ) - 2) ^ 2 * shapeTerm (m + 6) (rowShape (m + 6) i)
      = depthTwoTerm (m + 6) (i + 3) := by
  have hrow : rowShape (m + 6) i = (m - i + 3) :: 3 :: List.replicate i 1 := by
    unfold rowShape
    congr 1
    omega
  rw [hrow]
  unfold shapeTerm depthTwoTerm depthTwoG depthTwoW
  have hdim := congrArg (fun x : ℕ => (x : ℤ)) (mul_sytDim_famA (m - i) i)
  have hN : m - i + i + 6 = m + 6 := by omega
  rw [hN] at hdim
  push_cast [Nat.cast_sub hi] at hdim
  rw [six_mul_omega3_famA (m + 6) (m - i + 3) i (by omega)]
  push_cast [Nat.cast_sub hi]
  have key : 2 * (((m : ℤ) + 6) - 2) * (sytDim ((m - i + 3) :: 3 :: List.replicate i 1) : ℤ)
      = (((m : ℤ) + 6) - ((i : ℤ) + 3) - 2) * (((i : ℤ) + 3) - 1) * (((i : ℤ) + 3) - 2)
        * ((m + 6).choose (i + 3) : ℤ) := by
    linear_combination hdim
  linear_combination
    (2 * (((m : ℤ) + 6) - 2) * (sytDim ((m - i + 3) :: 3 :: List.replicate i 1) : ℤ)
      + (((m : ℤ) + 6) - ((i : ℤ) + 3) - 2) * (((i : ℤ) + 3) - 1) * (((i : ℤ) + 3) - 2)
        * ((m + 6).choose (i + 3) : ℤ))
    * ((((m : ℤ) - (i : ℤ) + 3) - 1) * ((m : ℤ) - (i : ℤ) + 3) * (2 * ((m : ℤ) - (i : ℤ) + 3) - 1)
        + 12 + ((i : ℤ) + 1) * ((i : ℤ) + 2) * (2 * (i : ℤ) + 3) - 6
        - 3 * ((m : ℤ) + 6) * (((m : ℤ) + 6) - 1)) * key

/-- Family B carries the same term as its transpose in family A. -/
theorem shapeTerm_col_eq_row (m i : ℕ) (hi : i ≤ m) :
    shapeTerm (m + 6) (colShape (m + 6) i) = shapeTerm (m + 6) (rowShape (m + 6) i) := by
  have hcol : colShape (m + 6) i = (i + 2) :: 2 :: 2 :: List.replicate (m - i) 1 := by
    unfold colShape
    rw [show m + 6 - 6 - i = m - i by omega]
  have hrow : rowShape (m + 6) i = conj (colShape (m + 6) i) := by
    rw [hcol, conj_famB]
    unfold rowShape
    congr 1
    omega
  have hs : (colShape (m + 6) i).Sorted (· ≥ ·) := by
    rw [hcol]
    simp [List.Sorted, List.pairwise_cons, List.pairwise_replicate, List.mem_replicate]
  have hpos : ∀ x ∈ colShape (m + 6) i, 0 < x := by
    rw [hcol]
    simp [List.mem_replicate]
  unfold shapeTerm
  rw [hrow, sytDim_conj _ hs hpos, omega3_conj _ _ hs]

/-! ## The six boundary shapes -/

/-- `[m + 6]`. -/
theorem shapeTerm_singleRow (m : ℕ) :
    shapeTerm (m + 6) [m + 6]
      = 2 * ((m : ℤ) + 6) * ((m : ℤ) + 6 - 1) * ((m : ℤ) + 6 - 2) := by
  unfold shapeTerm
  rw [QOU.BraidsAndKnots.DepthOneHookClassification.sytDim_singleRow (m + 6) (by omega),
    QOU.BraidsAndKnots.YoungDiagramTailSecondInstance.six_mul_omega3_singleRow (m + 6) (by omega)]
  push_cast
  ring

/-- `1^{m + 6}`. -/
theorem shapeTerm_singleCol (m : ℕ) :
    shapeTerm (m + 6) (List.replicate (m + 6) 1)
      = 2 * ((m : ℤ) + 6) * ((m : ℤ) + 6 - 1) * ((m : ℤ) + 6 - 2) := by
  unfold shapeTerm
  rw [QOU.BraidsAndKnots.DepthOneHookClassification.sytDim_singleCol (m + 6) (by omega),
    QOU.BraidsAndKnots.YoungDiagramTailSecondInstance.six_mul_omega3_singleCol (m + 6) (by omega)]
  push_cast
  ring

/-- `(2, 1^{m + 4})`. -/
theorem shapeTerm_hookTwo (m : ℕ) :
    shapeTerm (m + 6) (2 :: List.replicate (m + 4) 1)
      = ((m : ℤ) + 5) ^ 2 * (2 * ((m : ℤ) + 6) * ((m : ℤ) + 4) * ((m : ℤ) + 2)) := by
  unfold shapeTerm
  have hd := sytDim_hookShape 2 (m + 4) (by omega)
  rw [show 2 + (m + 4) - 1 = m + 5 by omega, show 2 - 1 = 1 by rfl, Nat.choose_one_right] at hd
  have ho := six_mul_omega3_hookShape (m + 6) 1 (by omega)
  rw [show m + 6 - 1 - 1 = m + 4 by omega] at ho
  rw [hd, ho]
  push_cast
  ring

/-- `(2, 2, 1^{m + 2})`, as `4·f²·6ω₃ = n²(n − 3)²·W(n, n − 1)`. -/
theorem four_mul_shapeTerm_twoTwo (m : ℕ) :
    4 * shapeTerm (m + 6) (2 :: 2 :: List.replicate (m + 2) 1)
      = ((m : ℤ) + 6) ^ 2 * ((m : ℤ) + 3) ^ 2
        * (((m : ℤ) + 3) * ((m : ℤ) + 4) * (2 * ((m : ℤ) + 6) - 5) + 6
          - 3 * ((m : ℤ) + 6) * ((m : ℤ) + 5)) := by
  unfold shapeTerm
  have hd := QOU.BraidsAndKnots.YoungDiagramTailSecondInstance.mul_sytDim_twoCorner (m + 6) 0
    (by omega)
  have ho := QOU.BraidsAndKnots.DepthOneHookClassification.six_mul_omega3_twoCorner (m + 6) 0
    (by omega)
  rw [show m + 6 - 4 - 0 = m + 2 by omega, show (0 : ℕ) + 2 = 2 by rfl] at hd ho
  have hc : 2 * (m + 6).choose 2 = (m + 6) * (m + 5) := by
    have h := Nat.succ_mul_choose_eq (m + 5) 1
    simp only [Nat.succ_eq_add_one, Nat.choose_one_right] at h
    ring_nf at h ⊢
    linarith
  have hdZ := congrArg (fun x : ℕ => (x : ℤ)) hd
  have hcZ := congrArg (fun x : ℕ => (x : ℤ)) hc
  push_cast [show m + 6 - 1 = m + 5 by omega, show m + 6 - 3 - 0 = m + 3 by omega] at hdZ hcZ
  have h2f : 2 * (sytDim (2 :: 2 :: List.replicate (m + 2) 1) : ℤ)
      = ((m : ℤ) + 6) * ((m : ℤ) + 3) := by
    have hne : ((m : ℤ) + 5) ≠ 0 := by positivity
    apply mul_left_cancel₀ hne
    linear_combination 2 * hdZ + ((m : ℤ) + 3) * hcZ
  rw [ho]
  push_cast
  linear_combination
    (2 * (sytDim (2 :: 2 :: List.replicate (m + 2) 1) : ℤ) + ((m : ℤ) + 6) * ((m : ℤ) + 3))
    * ((0 + 1) * (0 + 2) * (2 * 0 + 3) + (((m : ℤ) + 6) - 3 - 0) * (((m : ℤ) + 6) - 2 - 0)
        * (2 * (((m : ℤ) + 6) - 3 - 0) + 1) - 3 * ((m : ℤ) + 6) * (((m : ℤ) + 6) - 1)) * h2f

/-- The transpose of `(2, 1^c)` is `[c + 1, 1]`. -/
theorem conj_hookTwo (c : ℕ) : conj (2 :: List.replicate c 1) = [c + 1, 1] := by
  have hc := QOU.BraidsAndKnots.DepthOneHookClassification.countP_pos_replicate_one
  simp [conj, List.range_succ, hc]

/-- The transpose of `(2, 2, 1^c)` is `[c + 2, 2]`. -/
theorem conj_twoTwo (c : ℕ) : conj (2 :: 2 :: List.replicate c 1) = [c + 2, 2] := by
  have hc := QOU.BraidsAndKnots.DepthOneHookClassification.countP_pos_replicate_one
  simp [conj, List.range_succ, hc]

/-- A shape and its transpose carry the same term. -/
theorem shapeTerm_conj (n : ℕ) (l : List ℕ) (hs : l.Sorted (· ≥ ·)) (hpos : ∀ x ∈ l, 0 < x) :
    shapeTerm n (conj l) = shapeTerm n l := by
  unfold shapeTerm
  rw [sytDim_conj l hs hpos, omega3_conj n l hs]

/-! ## The unified sum -/

/-- The boundary terms of the binomial sum, `k ∈ {0, 1, 2, n − 2, n − 1, n}`. -/
theorem depthTwoTerm_boundary (m : ℕ) :
    depthTwoTerm (m + 6) 0 = 4 * ((m : ℤ) + 4) ^ 2 * (2 * ((m : ℤ) + 6) * ((m : ℤ) + 5) * ((m : ℤ) + 4))
    ∧ depthTwoTerm (m + 6) 1 = 0 ∧ depthTwoTerm (m + 6) 2 = 0 ∧ depthTwoTerm (m + 6) (m + 4) = 0
    ∧ depthTwoTerm (m + 6) (m + 5) = ((m : ℤ) + 4) ^ 2 * ((m : ℤ) + 3) ^ 2 * ((m : ℤ) + 6) ^ 2
        * (((m : ℤ) + 3) * ((m : ℤ) + 4) * (2 * ((m : ℤ) + 6) - 5) + 6
          - 3 * ((m : ℤ) + 6) * ((m : ℤ) + 5))
    ∧ depthTwoTerm (m + 6) (m + 6) = 4 * ((m : ℤ) + 5) ^ 2 * ((m : ℤ) + 4) ^ 2
        * (2 * ((m : ℤ) + 6) * ((m : ℤ) + 4) * ((m : ℤ) + 2)) := by
  have hc : (m + 6).choose (m + 5) = m + 6 := by
    rw [show m + 6 = (m + 5) + 1 by omega, Nat.choose_succ_self_right]
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    simp only [depthTwoTerm, depthTwoG, depthTwoW, Nat.choose_zero_right, Nat.choose_self, hc] <;>
    push_cast <;> ring

/-- **Unified sum.** `4(n − 2)²·Σ_shapes f²·6ω₃ = 2·Σ_{k=0}^{n} g(k)²·W(k)·C(n,k)²`, `n = m + 6`. -/
theorem shapes_sum_identity (m : ℕ) :
    4 * (((m + 6 : ℕ) : ℤ) - 2) ^ 2 * ((depthTwoShapes (m + 6)).map (shapeTerm (m + 6))).sum
      = 2 * ∑ k ∈ Finset.range (m + 6 + 1), depthTwoTerm (m + 6) k := by
  have hs2 : (2 :: List.replicate (m + 4) 1).Sorted (· ≥ ·) := by
    simp [List.Sorted, List.pairwise_cons, List.pairwise_replicate, List.mem_replicate]
  have hp2 : ∀ x ∈ 2 :: List.replicate (m + 4) 1, 0 < x := by simp [List.mem_replicate]
  have hs22 : (2 :: 2 :: List.replicate (m + 2) 1).Sorted (· ≥ ·) := by
    simp [List.Sorted, List.pairwise_cons, List.pairwise_replicate, List.mem_replicate]
  have hp22 : ∀ x ∈ 2 :: 2 :: List.replicate (m + 2) 1, 0 < x := by simp [List.mem_replicate]
  have e1 : shapeTerm (m + 6) [m + 6 - 1, 1] = shapeTerm (m + 6) (2 :: List.replicate (m + 4) 1) := by
    rw [show m + 6 - 1 = m + 4 + 1 by omega, ← conj_hookTwo, shapeTerm_conj _ _ hs2 hp2]
  have e2 : shapeTerm (m + 6) [m + 6 - 2, 2]
      = shapeTerm (m + 6) (2 :: 2 :: List.replicate (m + 2) 1) := by
    rw [show m + 6 - 2 = m + 2 + 2 by omega, ← conj_twoTwo, shapeTerm_conj _ _ hs22 hp22]
  have hcol : ∀ i ∈ Finset.range (m + 1),
      shapeTerm (m + 6) (colShape (m + 6) i) = shapeTerm (m + 6) (rowShape (m + 6) i) :=
    fun i hi => shapeTerm_col_eq_row m i (by have := Finset.mem_range.mp hi; omega)
  have hrow : 4 * (((m + 6 : ℕ) : ℤ) - 2) ^ 2
        * ∑ i ∈ Finset.range (m + 1), shapeTerm (m + 6) (rowShape (m + 6) i)
      = ∑ i ∈ Finset.range (m + 1), depthTwoTerm (m + 6) (i + 1 + 1 + 1) := by
    rw [Finset.mul_sum]
    exact Finset.sum_congr rfl fun i hi =>
      four_mul_shapeTerm_row m i (by have := Finset.mem_range.mp hi; omega)
  have hR : ∑ k ∈ Finset.range (m + 6 + 1), depthTwoTerm (m + 6) k
      = ∑ i ∈ Finset.range (m + 1), depthTwoTerm (m + 6) (i + 1 + 1 + 1)
        + depthTwoTerm (m + 6) 0 + depthTwoTerm (m + 6) 1 + depthTwoTerm (m + 6) 2
        + depthTwoTerm (m + 6) (m + 4) + depthTwoTerm (m + 6) (m + 5)
        + depthTwoTerm (m + 6) (m + 6) := by
    rw [Finset.sum_range_succ, Finset.sum_range_succ, Finset.sum_range_succ,
      Finset.sum_range_succ', Finset.sum_range_succ', Finset.sum_range_succ']
    simp only [zero_add]
    ring
  have hL : ((depthTwoShapes (m + 6)).map (shapeTerm (m + 6))).sum
      = shapeTerm (m + 6) [m + 6] + shapeTerm (m + 6) (2 :: List.replicate (m + 4) 1)
        + shapeTerm (m + 6) (2 :: 2 :: List.replicate (m + 2) 1)
        + shapeTerm (m + 6) (List.replicate (m + 6) 1)
        + shapeTerm (m + 6) (2 :: List.replicate (m + 4) 1)
        + shapeTerm (m + 6) (2 :: 2 :: List.replicate (m + 2) 1)
        + 2 * ∑ i ∈ Finset.range (m + 1), shapeTerm (m + 6) (rowShape (m + 6) i) := by
    unfold depthTwoShapes
    rw [List.map_cons, List.map_cons, List.map_cons, List.map_cons, List.map_cons,
      List.map_cons, List.sum_cons, List.sum_cons, List.sum_cons, List.sum_cons, List.sum_cons,
      List.sum_cons, List.map_append, List.sum_append, List.map_map, List.map_map,
      QOU.BraidsAndKnots.YoungDiagramTailSecondInstance.list_sum_map_range_int,
      QOU.BraidsAndKnots.YoungDiagramTailSecondInstance.list_sum_map_range_int,
      show m + 6 - 5 = m + 1 by omega, e1, e2, show m + 6 - 2 = m + 4 by omega,
      show m + 6 - 4 = m + 2 by omega]
    simp only [Function.comp_apply]
    rw [Finset.sum_congr rfl hcol]
    ring
  obtain ⟨h0, h1, h2, h4, h5, h6⟩ := depthTwoTerm_boundary m
  rw [hR, hL, ← hrow, h0, h1, h2, h4, h5, h6]
  have hA := shapeTerm_singleRow m
  have hB := shapeTerm_singleCol m
  have hC := shapeTerm_hookTwo m
  have hD := four_mul_shapeTerm_twoTwo m
  push_cast
  linear_combination (4 * ((m : ℤ) + 4) ^ 2) * hA + (4 * ((m : ℤ) + 4) ^ 2) * hB
    + (8 * ((m : ℤ) + 4) ^ 2) * hC + (2 * ((m : ℤ) + 4) ^ 2) * hD

/-- The shape sum in closed form: `(n − 3)·Σ_shapes f²·6ω₃ = (n − 2)(n − 5)·Q(n)·C(2n−8, n−4)`. -/
theorem shapes_sum_closed (m : ℕ) :
    ((m : ℤ) + 3) * ((depthTwoShapes (m + 6)).map (shapeTerm (m + 6))).sum
      = ((m : ℤ) + 4) * ((m : ℤ) + 1) * sexticZ ((m : ℤ) + 6)
        * (((2 * (m + 6) - 8).choose (m + 2) : ℕ) : ℤ) := by
  have h1 := shapes_sum_identity m
  have h2 := depthTwo_sum_collapse (m + 6) (by omega)
  push_cast at h1 h2
  have hne : (4 * ((m : ℤ) + 4) ^ 2) ≠ 0 := by positivity
  apply mul_left_cancel₀ hne
  linear_combination ((m : ℤ) + 3) * h1 + 2 * h2

/-- **The depth-2 tail in closed form.** For `n ≥ 6` the hook-`(n − 2)` covariance equals
`(n−2)(n−5)·Q(n)·C(2n−8, n−4) / (6(n−3)·n!)`. Derivation in
`docs/audits/2026-11-27-covariance-kernel-depth-two-tail.md`; bean `qou-swk4`. -/
theorem nuV_depthTwo_closed_form (n : ℕ) (hn : 6 ≤ n) :
    nuV n (n - 2) = QOU.BraidsAndKnots.YoungDiagramTailThirdInstance.nuDepthTwoClosedForm
      (R := ℝ) n := by
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 6 := ⟨n - 6, by omega⟩
  unfold nuV QOU.BraidsAndKnots.YoungDiagramTailThirdInstance.nuDepthTwoClosedForm
    QOU.BraidsAndKnots.YoungDiagramTailThirdInstance.depthTwoSexticFactor
  rw [tiltedMean_zero (m + 6), mul_zero, sub_zero]
  unfold nuMixedMoment
  rw [depthTwo_mixedMoment_eq_shapes_sum (m + 6) (by omega),
    PlancherelNormalisation.tiltNorm_zero_eq_factorial (m + 6)]
  have hcast : 6 * (((depthTwoShapes (m + 6)).map
        (fun l => tilt 0 (sytDim l) * (omega3 (m + 6) l : ℝ))).sum)
      = ((((depthTwoShapes (m + 6)).map (shapeTerm (m + 6))).sum : ℤ) : ℝ) := by
    rw [Int.cast_list_sum, List.map_map, ← list_sum_map_mul_left]
    refine congrArg List.sum (List.map_congr_left fun l _ => ?_)
    simp only [Function.comp_apply, shapeTerm]
    rw [tilt_zero]
    push_cast
    ring
  have hS := congrArg (fun z : ℤ => (z : ℝ)) (shapes_sum_closed m)
  simp only at hS
  push_cast at hS hcast
  have hfac : (0 : ℝ) < (Nat.factorial (m + 6) : ℝ) := by
    exact_mod_cast Nat.factorial_pos (m + 6)
  have h3 : ((m : ℝ) + 6 - 3) ≠ 0 := by
    have : (0 : ℝ) ≤ m := Nat.cast_nonneg m
    exact ne_of_gt (by linarith)
  rw [show m + 6 - 4 = m + 2 by omega]
  push_cast
  rw [div_eq_div_iff (ne_of_gt hfac) (mul_ne_zero (mul_ne_zero (by norm_num) h3) (ne_of_gt hfac))]
  unfold sexticZ at hS
  push_cast at hS
  linear_combination (Nat.factorial (m + 6) : ℝ) * hS + ((m : ℝ) + 3) * (Nat.factorial (m + 6) : ℝ) * hcast

/-- **Sign of the depth-2 tail.** For `n ≥ 6`, `ν_{n−2}(n) > 0` iff `n = 6` or `n ≥ 10`. -/
theorem nuV_depthTwo_pos_iff (n : ℕ) (hn : 6 ≤ n) : 0 < nuV n (n - 2) ↔ n = 6 ∨ 10 ≤ n := by
  rw [nuV_depthTwo_closed_form n hn]
  exact QOU.BraidsAndKnots.YoungDiagramTailThirdInstance.nuDepthTwo_pos_iff n (by omega)

/-- The depth-2 tail does not vanish for `n ≥ 6` (its only zero with `n ≥ 4` is `n = 5`). -/
theorem nuV_depthTwo_ne_zero (n : ℕ) (hn : 6 ≤ n) : nuV n (n - 2) ≠ 0 := by
  rw [nuV_depthTwo_closed_form n hn]
  intro h
  have := (QOU.BraidsAndKnots.YoungDiagramTailThirdInstance.nuDepthTwo_eq_zero_iff
    (R := ℝ) n (by omega)).mp h
  omega

end QOU.BraidsAndKnots.YoungDiagramTailThirdInstanceAssembly
