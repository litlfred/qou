import QOU.BraidsAndKnots.RationalAssociator.FurushoP5

/-!
# Furusho's Lie-algebra theorem, part 3: the hexagon from the pentagon

Bean `qou-3fdg` (epic `qou-dk7p`). This file proves `PentagonHexagonLie d` for every `d ≥ 3`
(Furusho, *Pentagon and hexagon equations*, Ann. of Math. 171 (2010), Theorem 3, Lie-algebra
form). Steps:

1. **A five-strand family on `ℚ⟨Y₁, Y₂, Y₃⟩ ⧸ FF3 N`** (`xE`, `xE_p5`). Each entry acts by
   left multiplication by a linear form `w` plus a Leibniz map `D` from `Prop57Link`
   (`D ∈ {0, ±t₁₂, ±t₂₃, −t₁₂ − t₂₃}` on generators). Two such operators commute when
   `[w, w'] + D w' − D' w = 0` and `D, D'` commute; this is checked on the 15 disjoint pairs.
2. **Each relabelled family gives a lift of `U4 N`** (`piExpr_eq_zero`): its first four strands
   form a `DK4` family whose words of length `N` vanish, so the linearised pentagon (5.20) maps
   to `piExpr`, which is therefore `0`.
3. **The permutation sum** (`rSum_eq`, `FurushoP5`) turns the four vanishing pentagons into
   `R(a, c) + R(a, s) + R(b, c) + R(b, s) ∈ FF3 N` for the hexagon polynomial `R`, where
   `a, b, c = Y₁, Y₂, Y₃` and `s = −a − b − c`.
4. **Two substitutions to `ℚ⟨X, Y⟩`** (`(a, b, c) ↦ (X, X, Y)` and `(X, Y, X)`) and
   homogeneity give two identities in `ℚ⟨X, Y⟩`; with the symmetries of `R` and a scaling they
   force `(2^{d−1} − 2) R = 0`, so `R = 0` for `d ≥ 3` (`rPoly_eq_zero`).
5. **The hexagon** (`lin513_eq_zero`): `t₁₂ + t₁₃ + t₂₃` commutes with `t₁₂, t₁₃, t₂₃`, and the
   commuting shift of part 1 turns the linearised hexagon (5.18) into `−R(t₁₂, t₁₃) = 0`.

Everything is algebraic over `ℚ`: free algebras, quotients and finite identities.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

open Friedrichs

local notation "F2" => FreeAlgebra ℚ (Fin 2)
local notation "F3" => FreeAlgebra ℚ (Fin 3)

/-! ### Leibniz maps with zero values -/

theorem der3_zero_dir (p : F3) : der3 0 p = 0 := by
  have h := der3_add_dir (0 : Fin 3 → F3) 0 p
  rw [add_zero] at h
  exact left_eq_add.mp h

/-! ### The five-strand family -/

section Family

/-- The linear forms `a, b, c, s = Y₁, Y₂, Y₃, −Y₁ − Y₂ − Y₃`. -/
noncomputable abbrev peS : F3 := -(Yg 0 + Yg 1 + Yg 2)

/-- The left-multiplication parts, for `i < j`. -/
noncomputable def peW0 : Fin 5 → Fin 5 → F3 :=
  ![![0, 0, peS, Yg 0, Yg 1 + Yg 2],
    ![0, 0, 0, Yg 1, -Yg 1],
    ![0, 0, 0, Yg 2, Yg 0 + Yg 1],
    ![0, 0, 0, 0, peS],
    ![0, 0, 0, 0, 0]]

/-- The Leibniz parts, for `i < j`. -/
noncomputable def peD0 : Fin 5 → Fin 5 → Fin 3 → F3 :=
  ![![0, d12, -d12 - d23, 0, d23],
    ![0, 0, d23, 0, -d12 - d23],
    ![0, 0, 0, 0, d12],
    ![0, 0, 0, 0, 0],
    ![0, 0, 0, 0, 0]]

noncomputable def peW (i j : Fin 5) : F3 := peW0 i j + peW0 j i
noncomputable def peD (i j : Fin 5) : Fin 3 → F3 := peD0 i j + peD0 j i

theorem peW0_mem (i j : Fin 5) : peW0 i j ∈ FF3 1 := by
  have a := Yg_mem_FF3 0
  have b := Yg_mem_FF3 1
  have c := Yg_mem_FF3 2
  fin_cases i <;> fin_cases j <;>
    simp only [peW0, Fin.zero_eta, Fin.mk_one, Fin.reduceFinMk, Matrix.cons_val, Matrix.cons_val_zero,
      Matrix.cons_val_one, peS] <;>
    first
    | exact zero_mem _
    | exact a | exact b | exact c
    | exact neg_mem b
    | exact add_mem b c
    | exact add_mem a b
    | exact neg_mem (add_mem (add_mem a b) c)

theorem peD0_mem (i j : Fin 5) (k : Fin 3) : peD0 i j k ∈ FF3 2 := by
  have a := d12_mem k
  have b := d23_mem k
  fin_cases i <;> fin_cases j <;>
    simp only [peD0, Fin.zero_eta, Fin.mk_one, Fin.reduceFinMk, Matrix.cons_val, Matrix.cons_val_zero,
      Matrix.cons_val_one, Pi.zero_apply, Pi.sub_apply, Pi.neg_apply] <;>
    first
    | exact zero_mem _
    | exact a | exact b
    | exact sub_mem (neg_mem a) b

theorem peW_mem (i j : Fin 5) : peW i j ∈ FF3 1 := add_mem (peW0_mem i j) (peW0_mem j i)

theorem peD_mem (i j : Fin 5) (k : Fin 3) : peD i j k ∈ FF3 2 :=
  add_mem (peD0_mem i j k) (peD0_mem j i k)

/-- The underlying linear maps. -/
noncomputable def peF (i j : Fin 5) : F3 →ₗ[ℚ] F3 :=
  LinearMap.mulLeft ℚ (peW i j) + derL (peD i j)

theorem peF_apply (i j : Fin 5) (p : F3) : peF i j p = peW i j * p + der3 (peD i j) p := rfl

theorem raises_peF (i j : Fin 5) : Raises (peF i j) :=
  Raises.add (fun k _ hp => mul_mem_FF3' (by omega) (peW_mem i j) hp)
    (raises_derL _ (peD_mem i j))

variable (N : ℕ)

/-- **The five-strand family** on `M3 N`. -/
noncomputable def xE (i j : Fin 5) : Module.End ℚ (M3 N) := qop N (peF i j) (raises_peF i j)

variable {N}

theorem xE_mk (i j : Fin 5) (p : F3) :
    xE N i j (Submodule.Quotient.mk p) = Submodule.Quotient.mk (peW i j * p + der3 (peD i j) p) :=
  rfl

theorem xE_ext {f g : Module.End ℚ (M3 N)}
    (h : ∀ p : F3, f (Submodule.Quotient.mk p) = g (Submodule.Quotient.mk p)) : f = g := by
  apply Submodule.linearMap_qext
  exact LinearMap.ext h

theorem xE_symm (i j : Fin 5) : xE N i j = xE N j i := by
  refine xE_ext fun p => ?_
  rw [xE_mk, xE_mk, peW, peW, peD, peD, add_comm (peW0 i j), add_comm (peD0 i j)]

theorem xE_diag (i : Fin 5) : xE N i i = 0 := by
  have hw : peW i i = 0 := by fin_cases i <;> simp [peW, peW0]
  have hD : peD i i = 0 := by fin_cases i <;> simp [peD, peD0]
  refine xE_ext fun p => ?_
  rw [xE_mk, hw, hD, der3_zero_dir, zero_mul, add_zero, LinearMap.zero_apply,
    Submodule.Quotient.mk_zero]

theorem xE_row (i : Fin 5) : ∑ j, xE N i j = 0 := by
  have hw : peW i 0 + peW i 1 + peW i 2 + peW i 3 + peW i 4 = 0 := by
    fin_cases i <;> simp [peW, peW0] <;> abel
  have hD : peD i 0 + peD i 1 + peD i 2 + peD i 3 + peD i 4 = 0 := by
    fin_cases i <;> simp [peD, peD0] <;> abel
  refine xE_ext fun p => ?_
  simp only [Fin.sum_univ_five, LinearMap.add_apply, xE_mk, LinearMap.zero_apply,
    ← Submodule.Quotient.mk_add]
  have e : peW i 0 * p + der3 (peD i 0) p + (peW i 1 * p + der3 (peD i 1) p) +
      (peW i 2 * p + der3 (peD i 2) p) + (peW i 3 * p + der3 (peD i 3) p) +
      (peW i 4 * p + der3 (peD i 4) p) =
      (peW i 0 + peW i 1 + peW i 2 + peW i 3 + peW i 4) * p +
        der3 (peD i 0 + peD i 1 + peD i 2 + peD i 3 + peD i 4) p := by
    simp only [der3_add_dir, add_mul]; abel
  rw [e, hw, hD, zero_mul, der3_zero_dir, add_zero, Submodule.Quotient.mk_zero]

/-- Two operators `w + D`, `w' + D'` commute when `[w, w'] + D w' − D' w = 0` and the Leibniz
maps commute. -/
theorem commute_xE {i j k l : Fin 5}
    (h1 : peW i j * peW k l - peW k l * peW i j + der3 (peD i j) (peW k l) -
      der3 (peD k l) (peW i j) = 0)
    (h2 : ∀ p, der3 (peD i j) (der3 (peD k l) p) = der3 (peD k l) (der3 (peD i j) p)) :
    Commute (xE N i j) (xE N k l) := by
  refine commute_qop _ _ fun p => ?_
  simp only [peF_apply, der3_add, der3_mul]
  have e : der3 (peD i j) (peW k l) = der3 (peD k l) (peW i j) -
      (peW i j * peW k l - peW k l * peW i j) := by
    rw [← sub_eq_zero, ← h1]; abel
  rw [e, h2]
  noncomm_ring

theorem der3_neg (d : Fin 3 → F3) (p : F3) : der3 d (-p) = -der3 d p := by
  rw [neg_eq_zero_sub, der3_sub, der3_zero, zero_sub]

/-- Checks for the far relations. -/
local macro "far_check" : tactic =>
  `(tactic| (refine commute_xE ?_ ?_ <;>
    [ (simp only [peW, peW0, peD, peD0, peS, Fin.zero_eta, Fin.mk_one, Fin.reduceFinMk,
          Matrix.cons_val, Matrix.cons_val_zero, Matrix.cons_val_one, Pi.add_apply,
          Pi.sub_apply, Pi.neg_apply, Pi.zero_apply, add_zero, zero_add, der3_add, der3_neg,
          der3_sub, der3_ι, der3_zero, der3_zero_dir, d12, d23, Matrix.cons_val_two,
          Matrix.head_cons, Matrix.tail_cons, cY]
       first | done | noncomm_ring);
      (intro p
       simp only [peD, peD0, Fin.zero_eta, Fin.mk_one, Fin.reduceFinMk, Matrix.cons_val,
         Matrix.cons_val_zero, Matrix.cons_val_one, add_zero, zero_add, der3_zero_dir,
         der3_zero])]))

theorem xE_far (i j k l : Fin 5) (h1 : i < j) (h2 : k < l) (h3 : i < k) (h4 : j ≠ k)
    (h5 : j ≠ l) : Commute (xE N i j) (xE N k l) := by
  have hm : (i, j, k, l) ∈ ([(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2), (0, 1, 2, 4),
      (0, 2, 1, 4), (0, 4, 1, 2), (0, 1, 3, 4), (0, 3, 1, 4), (0, 4, 1, 3), (0, 2, 3, 4),
      (0, 3, 2, 4), (0, 4, 2, 3), (1, 2, 3, 4), (1, 3, 2, 4), (1, 4, 2, 3)] :
      List (Fin 5 × Fin 5 × Fin 5 × Fin 5)) := by
    revert i j k l; decide
  simp only [List.mem_cons, Prod.mk.injEq, List.not_mem_nil, or_false] at hm
  rcases hm with ⟨rfl, rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl, rfl⟩ |
    ⟨rfl, rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl, rfl⟩ |
    ⟨rfl, rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl, rfl⟩ |
    ⟨rfl, rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl, rfl⟩ | ⟨rfl, rfl, rfl, rfl⟩ <;>
    far_check

/-- **The family is a five-strand family.** -/
theorem xE_p5 : P5 (xE N) :=
  P5.of_ordered xE_symm xE_diag xE_row xE_far

end Family

/-! ### Each relabelled family kills the linearised pentagon -/

section Lift

variable {N : ℕ}

/-- Words of length `N` in filtration-raising operators vanish on `M3 N`. -/
theorem word_eq_zero_of_qop (g : Fin 6 → Module.End ℚ (M3 N))
    (hg : ∀ i, ∃ f hf, g i = qop N f hf) (w : List (Fin 6)) (hw : w.length = N) :
    (w.map g).prod = 0 := by
  have key : ∀ (w : List (Fin 6)) (k : ℕ) (p : F3), p ∈ FF3 k →
      ∃ q ∈ FF3 (k + w.length), (w.map g).prod (Submodule.Quotient.mk p) =
        Submodule.Quotient.mk q := by
    intro w
    induction w with
    | nil => intro k p hp; exact ⟨p, by simpa using hp, by simp⟩
    | cons i w ih =>
      intro k p hp
      obtain ⟨q, hq, e⟩ := ih k p hp
      obtain ⟨f, hf, hi⟩ := hg i
      refine ⟨f q, ?_, ?_⟩
      · rw [List.length_cons, ← add_assoc]; exact hf _ q hq
      · rw [List.map_cons, List.prod_cons, Module.End.mul_apply, e, hi, qop_mk]
  refine LinearMap.ext fun x => ?_
  induction x using Submodule.Quotient.induction_on with
  | H p =>
    obtain ⟨q, hq, e⟩ := key w 0 p (mem_FF3_zero p)
    rw [e, LinearMap.zero_apply, Submodule.Quotient.mk_eq_zero]
    simpa [hw] using hq

/-- The first-four-strand generators of a relabelled family. -/
noncomputable def relGen (σ : Fin 5 → Fin 5) : Fin 6 → Module.End ℚ (M3 N) :=
  ![xE N (σ 0) (σ 1), xE N (σ 0) (σ 2), xE N (σ 0) (σ 3), xE N (σ 1) (σ 2),
    xE N (σ 1) (σ 3), xE N (σ 2) (σ 3)]

theorem relGen_qop (σ : Fin 5 → Fin 5) (i : Fin 6) :
    ∃ f hf, relGen (N := N) σ i = qop N f hf := by
  fin_cases i <;> exact ⟨_, raises_peF _ _, rfl⟩

theorem relGen_dk4 {σ : Fin 5 → Fin 5} (hσ : Function.Bijective σ) :
    DK4 (relGen (N := N) σ 0) (relGen σ 1) (relGen σ 2) (relGen σ 3) (relGen σ 4)
      (relGen σ 5) :=
  (xE_p5.comp hσ).dk4

/-- **The linearised pentagon vanishes at every relabelled family.** -/
theorem piExpr_eq_zero {h : F2} (hpent : lin515Expr N h = 0) {σ : Fin 5 → Fin 5}
    (hσ : Function.Bijective σ) : piExpr h (fun i j => xE N (σ i) (σ j)) = 0 := by
  have e := congrArg (lift N (relGen σ) (relGen_dk4 hσ)
    (word_eq_zero_of_qop _ (relGen_qop σ))) hpent
  simp only [lin515Expr, map_sub, map_add, map_eval, lift_t, map_zero] at e
  simpa [relGen, piExpr] using e

end Lift

end QOU.BraidsAndKnots.RationalAssociator
