import QOU.BraidsAndKnots.RationalAssociator.GRTFlowExact
import QOU.BraidsAndKnots.RationalAssociator.Descent
import QOU.BraidsAndKnots.RationalAssociator.Linearization

/-!
# The rational-associator induction step

Bean `qou-3fdg` (epic `qou-dk7p`). Drinfeld's numbering (1991, §5): (5.12) inversion,
(5.13) the `μ = 0` hexagon, (5.14) `t`-compatibility, (5.15) the pentagon, (5.16) the group law.

This file proves three things, all algebraic over `ℚ`.

1. **The congruence `Φ ∘ g ≡ Φ + y`** (audit §9.2). If `ε(Φ) = 1`, `y ∈ FF n` and
   `g ≡ 1 + y` modulo `FF (n + 1)`, then the (5.16)-composite `compPoly Φ g ≡ Φ + y` modulo
   `FF (n + 1)` (`compPoly_congr`). For the (5.16)-exponential, `Exp(y) ≡ 1 + y` modulo
   `FF (n + 1)` when `n ≥ 1` (`expPoly_congr`).
2. **The `GRT₁(ℚ)` shift of a rational associator in `U4 N`** (`assocU4_shift`). If `Φ` is an
   associator in `U4 N` (`AssocU4`: constant term `1`, (5.12) on `Fil N 1`, the hexagon with a
   fixed exponential `E`, the pentagon) and `y ∈ grt` (`GrtU4 N y`), `y ∈ FF n`, `n ≥ 1`, then
   `Φ ∘ Exp(y)` is again an associator in `U4 N`, and `Φ ∘ Exp(y) ≡ Φ + y` modulo `FF (n + 1)`.
3. **The descent step** (`exists_rational_lift`). Let `Φ` have constant term `1` and `d ≥ 1`.
   The extensions `Φ + x`, `x ∈ FF d`, that are associators in `U4 (d + 1)` are exactly the
   solutions of an inhomogeneous `ℚ`-linear system `assocLin x = −assocDefect Φ`
   (`assocU4_add_iff`). If that system is solvable after base change to some field `K ⊇ ℚ`
   (the named hypothesis `SolvableOver K d E Φ`), it is solvable over `ℚ`; conversely a rational
   solution gives a `K`-solution for every `K` (`solvableOver_of_lift`).

## What is not proved here

The induction "associator mod degree `d` over `ℚ` ⟹ associator mod degree `d + 1` over `ℚ`"
needs `SolvableOver K d E Φ` at every step. It holds at the first step when `Φ` is the
truncation of an associator over `K`; keeping it true from one step to the next is what the
`GRT₁(K)`-shift of item 2 does in Drinfeld's argument (Prop. 5.8). Item 2 is proved only over
`ℚ`. Over `K` two things are missing, recorded in audit §13:

* every definition from `eval` to `GrtU4` and `GRT1U4` is over `ℚ`; the shift needs them with
  coefficients in `K`;
* the element `y = ψ − Φ_K,d` (rational solution minus the `K`-associator's degree-`d` part)
  satisfies the linearised (5.12), (5.13), (5.15), but `GrtU4` also asks for the linearised
  (5.14). Drinfeld's Prop. 5.7 proves it, but only for Lie elements `y`; there is no Lie or
  group-like structure on associators in this repository.

No analysis and no numerical value is used.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

open TensorProduct

/-! ### 1. The congruence `Φ ∘ g ≡ Φ + y` in the word filtration -/

section Congruence

/-- Substituting `A ↦ A + δ₀`, `B ↦ B + δ₁` with `δᵢ ∈ FF m` changes a polynomial by an element
of `FF m`. -/
theorem eval_perturb_mem_FF {m : ℕ} {δ0 δ1 : FreeAlgebra ℚ (Fin 2)} (h0 : δ0 ∈ FF m)
    (h1 : δ1 ∈ FF m) (p : FreeAlgebra ℚ (Fin 2)) :
    eval (FreeAlgebra.ι ℚ 0 + δ0) (FreeAlgebra.ι ℚ 1 + δ1) p - p ∈ FF m := by
  induction p using FreeAlgebra.induction with
  | grade0 r => simp
  | grade1 i =>
    fin_cases i
    · simpa [eval] using h0
    · simpa [eval] using h1
  | mul a b ha hb =>
    have e : eval (FreeAlgebra.ι ℚ 0 + δ0) (FreeAlgebra.ι ℚ 1 + δ1) (a * b) - a * b =
        (eval (FreeAlgebra.ι ℚ 0 + δ0) (FreeAlgebra.ι ℚ 1 + δ1) a - a) *
            eval (FreeAlgebra.ι ℚ 0 + δ0) (FreeAlgebra.ι ℚ 1 + δ1) b +
          a * (eval (FreeAlgebra.ι ℚ 0 + δ0) (FreeAlgebra.ι ℚ 1 + δ1) b - b) := by
      rw [map_mul]; noncomm_ring
    rw [e]
    exact add_mem (mul_mem_FF' (by omega) ha (mem_FF_zero _))
      (mul_mem_FF' (by omega) (mem_FF_zero _) hb)
  | add a b ha hb =>
    have e : eval (FreeAlgebra.ι ℚ 0 + δ0) (FreeAlgebra.ι ℚ 1 + δ1) (a + b) - (a + b) =
        (eval (FreeAlgebra.ι ℚ 0 + δ0) (FreeAlgebra.ι ℚ 1 + δ1) a - a) +
          (eval (FreeAlgebra.ι ℚ 0 + δ0) (FreeAlgebra.ι ℚ 1 + δ1) b - b) := by
      rw [map_add]; abel
    rw [e]; exact add_mem ha hb

theorem ι_mem_FF_one (i : Fin 2) : FreeAlgebra.ι ℚ i ∈ FF 1 := by
  simpa using word_mem_FF (m := 1) [i] (by simp)

/-- Evaluation at two elements of `FF 1` preserves the word filtration. -/
theorem evalF_mem_FF {a b : FreeAlgebra ℚ (Fin 2)} (ha : a ∈ FF 1) (hb : b ∈ FF 1) {m : ℕ}
    {p : FreeAlgebra ℚ (Fin 2)} (hp : p ∈ FF m) : eval a b p ∈ FF m := by
  have hw : ∀ w : List (Fin 2), eval a b (w.map (FreeAlgebra.ι ℚ)).prod ∈ FF w.length := by
    intro w
    induction w with
    | nil => simpa using mem_FF_zero (1 : FreeAlgebra ℚ (Fin 2))
    | cons i w ih =>
      rw [List.map_cons, List.prod_cons, map_mul]
      have hi : eval a b (FreeAlgebra.ι ℚ i) ∈ FF 1 := by
        fin_cases i
        · simpa using ha
        · simpa using hb
      simpa [Nat.add_comm] using mul_mem_FF hi ih
  induction hp using Submodule.span_induction with
  | mem p h =>
    obtain ⟨w, hw', rfl⟩ := h
    exact FF_anti hw' (hw w)
  | zero => simp
  | add p q _ _ hp hq => rw [map_add]; exact add_mem hp hq
  | smul r p _ hp => rw [map_smul]; exact Submodule.smul_mem _ r hp

/-- A polynomial in `FF m` with `m ≥ 1` has constant term `0`. -/
theorem algebraMapInv_eq_zero_of_mem_FF {m : ℕ} (hm : 1 ≤ m) {p : FreeAlgebra ℚ (Fin 2)}
    (hp : p ∈ FF m) : FreeAlgebra.algebraMapInv p = 0 := by
  induction hp using Submodule.span_induction with
  | mem p h =>
    obtain ⟨w, hw, rfl⟩ := h
    cases w with
    | nil => simp at hw; omega
    | cons i w => simp [FreeAlgebra.algebraMapInv]
  | zero => simp
  | add p q _ _ hp hq => rw [map_add, hp, hq, add_zero]
  | smul r p _ hp => rw [map_smul, hp, smul_zero]

/-- **The congruence `Φ ∘ g ≡ Φ + y` (audit §9.2).** If `ε(Φ) = 1`, `y ∈ FF n` and
`g ≡ 1 + y (mod FF (n + 1))`, then the (5.16)-composite satisfies
`compPoly Φ g ≡ Φ + y (mod FF (n + 1))`. -/
theorem compPoly_congr {n : ℕ} {φ g y : FreeAlgebra ℚ (Fin 2)}
    (hφ : FreeAlgebra.algebraMapInv φ = 1) (hy : y ∈ FF n) (hg : g - 1 - y ∈ FF (n + 1)) :
    compPoly φ g - (φ + y) ∈ FF (n + 1) := by
  have hg1 : g - 1 ∈ FF n := by
    have := add_mem hy (FF_anti (Nat.le_succ n) hg)
    convert this using 1; abel
  have hs : swapPoly g - 1 ∈ FF n := by
    have e : swapPoly g - 1 = eval (FreeAlgebra.ι ℚ 1) (FreeAlgebra.ι ℚ 0) (g - 1) := by
      rw [map_sub, map_one]; rfl
    rw [e]; exact evalF_mem_FF (ι_mem_FF_one 1) (ι_mem_FF_one 0) hg1
  have hA := ι_mem_FF_one 0
  have hδ : g * FreeAlgebra.ι ℚ 0 * swapPoly g - FreeAlgebra.ι ℚ 0 ∈ FF (n + 1) := by
    have e : g * FreeAlgebra.ι ℚ 0 * swapPoly g - FreeAlgebra.ι ℚ 0 =
        (g - 1) * FreeAlgebra.ι ℚ 0 * swapPoly g + FreeAlgebra.ι ℚ 0 * (swapPoly g - 1) := by
      noncomm_ring
    rw [e]
    exact add_mem (mul_mem_FF' (by omega) (mul_mem_FF hg1 hA) (mem_FF_zero _))
      (mul_mem_FF' (by omega) hA hs)
  have hr : eval (g * FreeAlgebra.ι ℚ 0 * swapPoly g) (FreeAlgebra.ι ℚ 1) φ - φ ∈ FF (n + 1) := by
    have := eval_perturb_mem_FF hδ (zero_mem _) φ
    simpa using this
  have hφ1 : φ - 1 ∈ FF 1 := by simpa [hφ] using sub_algebraMapInv_mem_FF φ
  have e : compPoly φ g - (φ + y) =
      (eval (g * FreeAlgebra.ι ℚ 0 * swapPoly g) (FreeAlgebra.ι ℚ 1) φ - φ) * g +
        (φ - 1) * (g - 1) + (g - 1 - y) := by
    rw [show compPoly φ g =
      eval (g * FreeAlgebra.ι ℚ 0 * swapPoly g) (FreeAlgebra.ι ℚ 1) φ * g from rfl]
    noncomm_ring
  rw [e]
  exact add_mem (add_mem (mul_mem_FF' (by omega) hr (mem_FF_zero g))
    (mul_mem_FF' (by omega) hφ1 hg1)) hg

/-- A Leibniz map whose values on the generators lie in `FF (j + 1)` raises the word
filtration by `j`. -/
theorem leibD_mem_FF_add (d : Fin 2 → FreeAlgebra ℚ (Fin 2)) {j : ℕ} (hd : ∀ i, d i ∈ FF (j + 1))
    {m : ℕ} {p : FreeAlgebra ℚ (Fin 2)} (hp : p ∈ FF m) : leibD d p ∈ FF (m + j) := by
  have hw : ∀ w : List (Fin 2), leibD d (w.map (FreeAlgebra.ι ℚ)).prod ∈ FF (w.length + j) := by
    intro w
    induction w with
    | nil => simp [leibD_one]
    | cons i w ih =>
      rw [List.map_cons, List.prod_cons, leibD_mul, leibD_ι]
      refine add_mem ?_ ?_
      · exact mul_mem_FF' (by simp; omega) (ι_mem_FF_one i) ih
      · exact mul_mem_FF' (by simp; omega) (hd i) (word_mem_FF w le_rfl)
  induction hp using Submodule.span_induction with
  | mem p h =>
    obtain ⟨w, hw', rfl⟩ := h
    exact FF_anti (by omega) (hw w)
  | zero =>
    rw [show leibD d 0 = 0 by simpa using leibD_smul d 0 0]; exact zero_mem _
  | add p q _ _ hp hq => rw [leibD_add]; exact add_mem hp hq
  | smul r p _ hp => rw [leibD_smul]; exact Submodule.smul_mem _ r hp

/-- `L_y` raises the word filtration by `n` when `y ∈ FF n`. -/
theorem Ly_mem_FF_add {n : ℕ} {y : FreeAlgebra ℚ (Fin 2)} (hy : y ∈ FF n) {m : ℕ}
    {z : FreeAlgebra ℚ (Fin 2)} (hz : z ∈ FF m) : Ly y z ∈ FF (m + n) := by
  have hd : ∀ i, dY y i ∈ FF (n + 1) := by
    intro i
    fin_cases i
    · simp only [dY, Fin.zero_eta, Matrix.cons_val_zero]
      exact sub_mem (mul_mem_FF hy (ι_mem_FF_one 0))
        (mul_mem_FF' (by omega) (ι_mem_FF_one 0) hy)
    · simp [dY]
  exact add_mem (leibD_mem_FF_add _ hd hz) (mul_mem_FF hz hy)

theorem expTerm_mem_FF_mul {n : ℕ} {y : FreeAlgebra ℚ (Fin 2)} (hy : y ∈ FF n) (k : ℕ) :
    expTerm y k ∈ FF (k * n) := by
  have : ∀ k, (Ly y)^[k] 1 ∈ FF (k * n) := by
    intro k
    induction k with
    | zero => simpa using mem_FF_zero (1 : FreeAlgebra ℚ (Fin 2))
    | succ k ih =>
      rw [Function.iterate_succ_apply']
      exact (show (k + 1) * n = k * n + n by ring) ▸ Ly_mem_FF_add hy ih
  exact Submodule.smul_mem _ _ (this k)

/-- **`Exp(y) ≡ 1 + y`.** For `y ∈ FF n` with `n ≥ 1` and `K ≥ 2`,
`expPoly y K − 1 − y ∈ FF (n + 1)`. -/
theorem expPoly_congr {n K : ℕ} (hn : 1 ≤ n) (hK : 2 ≤ K) {y : FreeAlgebra ℚ (Fin 2)}
    (hy : y ∈ FF n) : expPoly y K - 1 - y ∈ FF (n + 1) := by
  obtain ⟨K, rfl⟩ : ∃ K', K = K' + 2 := ⟨K - 2, by omega⟩
  rw [expPoly, Finset.sum_range_succ', Finset.sum_range_succ', expTerm_zero]
  simp only [zero_add, expTerm_one, add_sub_cancel_right]
  refine Submodule.sum_mem _ fun k _ => FF_anti ?_ (expTerm_mem_FF_mul hy (k + 1 + 1))
  nlinarith

/-- **`Φ ∘ Exp(y) ≡ Φ + y`.** -/
theorem compPoly_expPoly_congr {n K : ℕ} (hn : 1 ≤ n) (hK : 2 ≤ K)
    {φ y : FreeAlgebra ℚ (Fin 2)} (hφ : FreeAlgebra.algebraMapInv φ = 1) (hy : y ∈ FF n) :
    compPoly φ (expPoly y K) - (φ + y) ∈ FF (n + 1) :=
  compPoly_congr hφ hy (expPoly_congr hn hK hy)

end Congruence

/-! ### 2. Associators in `U4 N` and the `GRT₁(ℚ)` shift -/

section Shift

variable {N : ℕ}

/-- `Φ` is an associator in `U4 N` (an associator modulo words of length `N`) for the exponential
`E`: constant term `1`, (5.12) on all of `Fil N 1`, the hexagon with `E` at the universal
three-strand family, and the pentagon at the universal four-strand family. -/
structure AssocU4 (N : ℕ) (E Φ : FreeAlgebra ℚ (Fin 2)) : Prop where
  const : FreeAlgebra.algebraMapInv Φ = 1
  inv : Inv512 (Fil N 1) Φ
  hex : Hexagon Φ E (t N 0) (t N 1) (t N 3)
  pent : Pentagon Φ (t N 0) (t N 1) (t N 3) (t N 4) (t N 5)

/-- **`GRT₁` acts on associators in `U4 N`** (Drinfeld's right action, (5.16) form). -/
theorem assocU4_compPoly {E Φ g : FreeAlgebra ℚ (Fin 2)} (hΦ : AssocU4 N E Φ)
    (hg : GRT1U4 N g) : AssocU4 N E (compPoly Φ g) where
  const := by rw [algebraMapInv_compPoly, hΦ.const, hg.const, one_mul]
  inv := fun a b ha hb => by
    rw [eval_compPoly, eval_compPoly]; exact comp_inv512 nilIdeal_Fil hΦ.inv hg.inv512 ha hb
  hex := hexagon_compPoly_U4 Φ g E hg.const hg.inv512 hg.hex513 hg.tc514 hΦ.hex
  pent := pentagon_compPoly_U4 Φ g hg.const hg.inv512 hg.tc514 hg.pent515 hΦ.pent

/-- **The `GRT₁(ℚ)` shift.** For an associator `Φ` in `U4 N` and `y ∈ grt` (`GrtU4 N y`) lying
in `FF n` with `n ≥ 1`, the shifted element `Φ ∘ Exp(y)` is again an associator in `U4 N`, and
`Φ ∘ Exp(y) ≡ Φ + y (mod FF (n + 1))`. The truncation order `K` of `Exp` must satisfy
`2 ≤ K` and `N ≤ K`, as in `grt1U4_expPoly`. -/
theorem assocU4_shift {E Φ y : FreeAlgebra ℚ (Fin 2)} (hΦ : AssocU4 N E Φ) (hy : GrtU4 N y)
    {n K : ℕ} (hyn : y ∈ FF n) (hn : 1 ≤ n) (hK : 2 ≤ K) (hNK : N ≤ K) :
    AssocU4 N E (compPoly Φ (expPoly y K)) ∧
      compPoly Φ (expPoly y K) - (Φ + y) ∈ FF (n + 1) := by
  have hg := grt1U4_expPoly hy hK hNK 1
  rw [one_smul] at hg
  exact ⟨assocU4_compPoly hΦ hg, compPoly_expPoly_congr hn hK hΦ.const hyn⟩

end Shift

/-! ### 3. The descent step: the next degree is an inhomogeneous linear system over `ℚ` -/

section DescentStep

variable {N : ℕ}

/-- The pairs at which (5.12) is imposed. -/
def InvIdx (N : ℕ) : Type := {p : U4 N × U4 N // p.1 ∈ Fil N 1 ∧ p.2 ∈ Fil N 1}

/-- The target of the associator equations in `U4 N`: (5.12) at each pair, the hexagon, the
pentagon. -/
abbrev AssocTarget (N : ℕ) : Type := (InvIdx N → U4 N) × U4 N × U4 N

/-- The defects of the associator equations for `Φ` in `U4 N`. -/
noncomputable def assocDefect (N : ℕ) (E Φ : FreeAlgebra ℚ (Fin 2)) : AssocTarget N :=
  (fun p => eval p.1.1 p.1.2 Φ * eval p.1.2 p.1.1 Φ - 1,
    eval (t N 1 + t N 3) 0 E - eval (t N 1) (t N 0) Φ * eval (t N 1) 0 E *
      eval (t N 3) (t N 1) Φ * eval (t N 3) 0 E * eval (t N 0) (t N 3) Φ,
    eval (t N 3) (t N 5) Φ * eval (t N 0 + t N 1) (t N 4 + t N 5) Φ * eval (t N 0) (t N 3) Φ -
      eval (t N 0) (t N 3 + t N 4) Φ * eval (t N 1 + t N 3) (t N 5) Φ)

/-- The associator equations linearised at `Φ = 1`: Drinfeld's (5.17), (5.18), (5.20) in
`U4 N` (the hexagon with sign `−`). -/
noncomputable def assocLin (N : ℕ) : FreeAlgebra ℚ (Fin 2) →ₗ[ℚ] AssocTarget N where
  toFun x :=
    (fun p => eval p.1.1 p.1.2 x + eval p.1.2 p.1.1 x,
      -(eval (t N 1) (t N 0) x + eval (t N 3) (t N 1) x + eval (t N 0) (t N 3) x),
      eval (t N 3) (t N 5) x + eval (t N 0 + t N 1) (t N 4 + t N 5) x + eval (t N 0) (t N 3) x -
        eval (t N 0) (t N 3 + t N 4) x - eval (t N 1 + t N 3) (t N 5) x)
  map_add' x y := by
    refine Prod.ext (funext fun p => ?_) (Prod.ext ?_ ?_) <;>
      simp only [map_add, Prod.fst_add, Prod.snd_add, Pi.add_apply] <;> abel
  map_smul' r x := by
    refine Prod.ext (funext fun p => ?_) (Prod.ext ?_ ?_) <;>
      simp [map_smul, smul_add, smul_sub, smul_neg]

theorem assocU4_iff {E Φ : FreeAlgebra ℚ (Fin 2)} :
    AssocU4 N E Φ ↔ FreeAlgebra.algebraMapInv Φ = 1 ∧ assocDefect N E Φ = 0 := by
  constructor
  · intro h
    refine ⟨h.const, Prod.ext (funext fun p => ?_) (Prod.ext ?_ ?_)⟩
    · simpa [assocDefect, sub_eq_zero] using h.inv _ _ p.2.1 p.2.2
    · simpa [assocDefect, sub_eq_zero] using h.hex
    · simpa [assocDefect, sub_eq_zero] using h.pent.symm
  · rintro ⟨hc, hd⟩
    have h1 := congrArg Prod.fst hd
    have h2 := congrArg (fun z => z.2.1) hd
    have h3 := congrArg (fun z => z.2.2) hd
    simp only [assocDefect, Prod.fst_zero, Prod.snd_zero] at h1 h2 h3
    refine ⟨hc, fun a b ha hb => ?_, ?_, ?_⟩
    · have := congrFun h1 ⟨(a, b), ha, hb⟩
      simpa [sub_eq_zero] using this
    · exact sub_eq_zero.1 h2
    · exact (sub_eq_zero.1 h3).symm

/-- `Fil N 1` as a two-sided ideal. -/
def filIdeal (N : ℕ) : TwoSidedIdeal (U4 N) :=
  TwoSidedIdeal.mk' (Fil N 1 : Set (U4 N)) (zero_mem _) add_mem neg_mem
    (fun {x y} hy => by simpa using mul_mem_Fil (mem_Fil_zero x) hy)
    (fun {x y} hx => by simpa using mul_mem_Fil hx (mem_Fil_zero y))

theorem mem_filIdeal {x : U4 N} : x ∈ filIdeal N ↔ x ∈ Fil N 1 := by
  simp [filIdeal]

/-- In `U4 (d + 1)` with `d ≥ 1`, `Fil d` is a top layer for `Fil 1`. -/
theorem isTop_Fil {d : ℕ} (hd : 1 ≤ d) :
    IsTop (filIdeal (d + 1)) (Fil (d + 1) d).toAddSubgroup where
  le x hx := mem_filIdeal.2 (Fil_anti hd hx)
  mul_left x hx z hz := eq_zero_of_mem_Fil (mul_mem_Fil' rfl hx (mem_filIdeal.1 hz))
  mul_right x hx z hz := eq_zero_of_mem_Fil (mul_mem_Fil' (by omega) (mem_filIdeal.1 hz) hx)

/-- **The degree-`d` correction is linear.** For `ε(Φ) = ε(E) = 1`, `d ≥ 1` and `x ∈ FF d`, the
defects of `Φ + x` in `U4 (d + 1)` are the defects of `Φ` plus `assocLin x`. -/
theorem assocDefect_add {d : ℕ} (hd : 1 ≤ d) {E Φ x : FreeAlgebra ℚ (Fin 2)}
    (hE : FreeAlgebra.algebraMapInv E = 1) (hΦ : FreeAlgebra.algebraMapInv Φ = 1)
    (hx : x ∈ FF d) :
    assocDefect (d + 1) E (Φ + x) = assocDefect (d + 1) E Φ + assocLin (d + 1) x := by
  have hJ := isTop_Fil hd
  have hI : ∀ {a b : U4 (d + 1)}, a ∈ Fil (d + 1) 1 → b ∈ Fil (d + 1) 1 →
      ∀ {p : FreeAlgebra ℚ (Fin 2)}, FreeAlgebra.algebraMapInv p = 1 →
        eval a b p - 1 ∈ filIdeal (d + 1) := by
    intro a b ha hb p hp
    have := eval_sub_mem nilIdeal_Fil ha hb p
    rw [hp, map_one] at this
    exact mem_filIdeal.2 this
  have hX : ∀ {a b : U4 (d + 1)}, a ∈ Fil (d + 1) 1 → b ∈ Fil (d + 1) 1 →
      eval a b x ∈ (Fil (d + 1) d).toAddSubgroup :=
    fun ha hb => eval_mem_Fil ha hb hx
  have m := fun i => t_mem_Fil_one (N := d + 1) i
  have m0 : (0 : U4 (d + 1)) ∈ Fil (d + 1) 1 := zero_mem _
  refine Prod.ext (funext fun p => ?_) (Prod.ext ?_ ?_)
  · simp only [assocDefect, assocLin, LinearMap.coe_mk, AddHom.coe_mk, Prod.fst_add,
      Pi.add_apply, map_add]
    exact inversion_linear hJ (hI p.2.1 p.2.2 hΦ) (hI p.2.2 p.2.1 hΦ) (hX p.2.1 p.2.2)
      (hX p.2.2 p.2.1)
  · simp only [assocDefect, assocLin, LinearMap.coe_mk, AddHom.coe_mk, Prod.snd_add,
      Prod.fst_add, map_add]
    rw [hexagon_linear hJ (hI (m 1) (m 0) hΦ) (hI (m 3) (m 1) hΦ) (hI (m 0) (m 3) hΦ)
      (hI (m 1) m0 hE) (hI (m 3) m0 hE) (hX (m 1) (m 0)) (hX (m 3) (m 1)) (hX (m 0) (m 3))]
    abel
  · simp only [assocDefect, assocLin, LinearMap.coe_mk, AddHom.coe_mk, Prod.snd_add, map_add]
    rw [pentagon_linear hJ (hI (m 0) (m 3) hΦ) (hI (m 0) (add_mem (m 3) (m 4)) hΦ)
      (hI (add_mem (m 0) (m 1)) (add_mem (m 4) (m 5)) hΦ) (hI (add_mem (m 1) (m 3)) (m 5) hΦ)
      (hI (m 3) (m 5) hΦ) (hX (m 0) (m 3)) (hX (m 0) (add_mem (m 3) (m 4)))
      (hX (add_mem (m 0) (m 1)) (add_mem (m 4) (m 5))) (hX (add_mem (m 1) (m 3)) (m 5))
      (hX (m 3) (m 5))]

/-- **The next degree as a linear system.** For `ε(Φ) = ε(E) = 1`, `d ≥ 1` and `x ∈ FF d`,
`Φ + x` is an associator in `U4 (d + 1)` iff `assocLin x = −assocDefect Φ`. -/
theorem assocU4_add_iff {d : ℕ} (hd : 1 ≤ d) {E Φ x : FreeAlgebra ℚ (Fin 2)}
    (hE : FreeAlgebra.algebraMapInv E = 1) (hΦ : FreeAlgebra.algebraMapInv Φ = 1)
    (hx : x ∈ FF d) :
    AssocU4 (d + 1) E (Φ + x) ↔ assocLin (d + 1) x = -assocDefect (d + 1) E Φ := by
  have hc : FreeAlgebra.algebraMapInv (Φ + x) = 1 := by
    rw [map_add, hΦ, algebraMapInv_eq_zero_of_mem_FF hd hx, add_zero]
  rw [assocU4_iff, assocDefect_add hd hE hΦ hx, eq_neg_iff_add_eq_zero]
  exact ⟨fun h => (add_comm _ _).trans h.2, fun h => ⟨hc, (add_comm _ _).trans h⟩⟩

/-- `assocLin` on `FF d`, the unknowns of the degree-`d` step. -/
noncomputable def linFF (d : ℕ) : FF d →ₗ[ℚ] AssocTarget (d + 1) :=
  (assocLin (d + 1)).domRestrict (FF d)

/-- **The named descent hypothesis.** The degree-`d` linear system for extending `Φ` is
solvable after base change to `K`. This is the condition Bar-Natan's descent needs; a
`K`-associator whose truncation agrees with `Φ` modulo `FF d` would supply a solution, but
that implication needs `U4` and `eval` over `K` and is not formalised here. -/
def SolvableOver (K : Type*) [CommRing K] [Algebra ℚ K] (d : ℕ) (E Φ : FreeAlgebra ℚ (Fin 2)) :
    Prop :=
  ∃ z : K ⊗[ℚ] FF d, (linFF d).baseChange K z = (1 : K) ⊗ₜ (-assocDefect (d + 1) E Φ)

/-- **Descent step.** If the degree-`d` system is solvable over a nontrivial `ℚ`-algebra `K`
(for instance a field `K ⊇ ℚ`), there is a rational `x ∈ FF d` with `Φ + x` an associator in
`U4 (d + 1)`. -/
theorem exists_rational_lift {d : ℕ} (hd : 1 ≤ d) {E Φ : FreeAlgebra ℚ (Fin 2)}
    (hE : FreeAlgebra.algebraMapInv E = 1) (hΦ : FreeAlgebra.algebraMapInv Φ = 1)
    (K : Type*) [CommRing K] [Nontrivial K] [Algebra ℚ K] (hsolv : SolvableOver K d E Φ) :
    ∃ x ∈ FF d, AssocU4 (d + 1) E (Φ + x) := by
  obtain ⟨v, hv⟩ := exists_of_baseChange (linFF d) _ hsolv
  exact ⟨v.1, v.2, (assocU4_add_iff hd hE hΦ v.2).2 hv⟩

/-- **The hypothesis is necessary.** A rational extension gives a solution over every `K`. -/
theorem solvableOver_of_lift {d : ℕ} (hd : 1 ≤ d) {E Φ x : FreeAlgebra ℚ (Fin 2)}
    (hE : FreeAlgebra.algebraMapInv E = 1) (hΦ : FreeAlgebra.algebraMapInv Φ = 1)
    (hx : x ∈ FF d) (h : AssocU4 (d + 1) E (Φ + x)) (K : Type*) [CommRing K] [Algebra ℚ K] :
    SolvableOver K d E Φ := by
  refine ⟨(1 : K) ⊗ₜ ⟨x, hx⟩, ?_⟩
  rw [LinearMap.baseChange_tmul]
  congr 1
  exact (assocU4_add_iff hd hE hΦ hx).1 h

end DescentStep

/-! ### 4. The linearised `t`-compatibility of `GrtU4` is Drinfeld's (5.19) on zero-sum triples -/

section Drinfeld519

/-- A triple with sum `0` is a `DK3` family. -/
theorem dk3_of_sum_zero {R : Type*} [Ring R] {u v w : R} (h : u + v + w = 0) : DK3 u v w where
  n12_3 := by rw [show v + w = -u from eq_neg_of_add_eq_zero_right (by rw [← h]; abel)]; exact (Commute.neg_right (Commute.refl u))
  n13_2 := by rw [show u + w = -v from eq_neg_of_add_eq_zero_right (by rw [← h]; abel)]; exact (Commute.neg_right (Commute.refl v))
  n23_1 := by rw [show u + v = -w from eq_neg_of_add_eq_zero_right (by rw [← h]; abel)]; exact (Commute.neg_right (Commute.refl w))

variable {R : Type*} [Ring R] [Algebra ℚ R]

/-- On a triple `(u, v, w)` with `u + v + w = 0`, and given (5.17) at the pairs `(v, w)` and
`(u, w)`, the `lin514` identity of `GrtU4` is Drinfeld's (5.19)
`[B, ψ(A, B)] + [C, ψ(A, C)] = 0` at `(A, B, C) = (w, v, u)`. -/
theorem lin514_iff_drinfeld519 (y : FreeAlgebra ℚ (Fin 2)) {u v w : R} (hsum : u + v + w = 0)
    (h1 : eval w v y = -eval v w y) (h2 : eval w u y = -eval u w y) :
    (eval v w y * v + v * eval w v y = eval u w y * (v + w) + (v + w) * eval w u y) ↔
      (v * eval w v y - eval w v y * v) + (u * eval w u y - eval w u y * u) = 0 := by
  have hvw : v + w = -u := eq_neg_of_add_eq_zero_right (by rw [← hsum]; abel)
  have key : (v * eval w v y - eval w v y * v) + (u * eval w u y - eval w u y * u) =
      (eval v w y * v + v * eval w v y) - (eval u w y * (v + w) + (v + w) * eval w u y) := by
    rw [hvw, h1, h2]; noncomm_ring
  rw [key, sub_eq_zero]

variable {N : ℕ}

/-- **`GrtU4` implies Drinfeld's (5.19)** at every pair `(A, B)` of `Fil N 1`, with
`C = −A − B`: `[B, y(A, B)] + [C, y(A, C)] = 0`. -/
theorem drinfeld519_of_grtU4 {y : FreeAlgebra ℚ (Fin 2)} (hy : GrtU4 N y) {A B : U4 N}
    (hA : A ∈ Fil N 1) (hB : B ∈ Fil N 1) :
    (B * eval A B y - eval A B y * B) + (-(A + B) * eval A (-(A + B)) y -
      eval A (-(A + B)) y * -(A + B)) = 0 := by
  have hC : -(A + B) ∈ Fil N 1 := neg_mem (add_mem hA hB)
  have hsum : -(A + B) + B + A = 0 := by abel
  have h1 : eval A B y = -eval B A y := eq_neg_of_add_eq_zero_left (hy.lin512 A B hA hB)
  have h2 : eval A (-(A + B)) y = -eval (-(A + B)) A y :=
    eq_neg_of_add_eq_zero_left (hy.lin512 A _ hA hC)
  exact (lin514_iff_drinfeld519 y hsum h1 h2).1
    (hy.lin514 _ _ _ hC hB hA (dk3_of_sum_zero hsum))

/-- **Conversely**, (5.17) on `Fil N 1` and (5.19) at every pair of `Fil N 1` give the `lin514`
identity at every zero-sum triple of `Fil N 1`. `GrtU4` asks for `lin514` at every `DK3`
triple; for a triple with nonzero central sum the two forms agree only after removing the
centre, which needs `y` to be a Lie element. -/
theorem lin514_of_drinfeld519 {y : FreeAlgebra ℚ (Fin 2)}
    (h512 : ∀ a b : U4 N, a ∈ Fil N 1 → b ∈ Fil N 1 → eval a b y + eval b a y = 0)
    (h519 : ∀ A B : U4 N, A ∈ Fil N 1 → B ∈ Fil N 1 →
      (B * eval A B y - eval A B y * B) + (-(A + B) * eval A (-(A + B)) y -
        eval A (-(A + B)) y * -(A + B)) = 0)
    {u v w : U4 N} (hu : u ∈ Fil N 1) (hv : v ∈ Fil N 1) (hw : w ∈ Fil N 1)
    (hsum : u + v + w = 0) :
    eval v w y * v + v * eval w v y = eval u w y * (v + w) + (v + w) * eval w u y := by
  have hu' : u = -(w + v) := eq_neg_of_add_eq_zero_left (by rw [← hsum]; abel)
  have h1 : eval w v y = -eval v w y := eq_neg_of_add_eq_zero_left (h512 w v hw hv)
  have h2 : eval w u y = -eval u w y := eq_neg_of_add_eq_zero_left (h512 w u hw hu)
  refine (lin514_iff_drinfeld519 y hsum h1 h2).2 ?_
  have := h519 w v hw hv
  rw [← hu'] at this
  exact this

end Drinfeld519

end QOU.BraidsAndKnots.RationalAssociator
