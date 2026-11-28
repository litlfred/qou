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
    fin_cases i <;> (simp [peW, peW0]; try abel)
  have hD : peD i 0 + peD i 1 + peD i 2 + peD i 3 + peD i 4 = 0 := by
    fin_cases i <;> (simp [peD, peD0]; try abel)
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

/-! ### The permutation sum lands in `FF3 N` -/

section Sum

variable (N : ℕ)

/-- Left multiplication: `ℚ⟨Y₁, Y₂, Y₃⟩ → End(M3 N)`. -/
noncomputable def psiL : F3 →ₐ[ℚ] Module.End ℚ (M3 N) :=
  FreeAlgebra.lift ℚ ![qL N 0, qL N 1, qL N 2]

variable {N}

theorem psiL_mk (c q : F3) :
    psiL N c (Submodule.Quotient.mk q) = Submodule.Quotient.mk (c * q) := by
  induction c using FreeAlgebra.induction generalizing q with
  | grade0 r =>
    rw [AlgHom.commutes, Module.algebraMap_end_apply, ← Submodule.Quotient.mk_smul,
      Algebra.smul_def]
  | grade1 i => fin_cases i <;> simp [psiL, qL_mk]
  | mul a b ha hb => rw [map_mul, Module.End.mul_apply, hb, ha, mul_assoc]
  | add a b ha hb => rw [map_add, LinearMap.add_apply, ha, hb, add_mul, Submodule.Quotient.mk_add]

theorem xE_eq_psiL {i j : Fin 5} {w : F3} (hw : peW i j = w) (hD : peD i j = 0) :
    xE N i j = psiL N w := by
  refine xE_ext fun p => ?_
  rw [xE_mk, hw, hD, der3_zero_dir, add_zero, psiL_mk]

/-- The relabelling `1 ↔ 3`. -/
def swp : Fin 5 → Fin 5 := ![0, 3, 2, 1, 4]

/-- The hexagon-polynomial sum of the permutation argument. -/
noncomputable def hexSum (g : F2) : F3 :=
  eval (Yg 0) (Yg 2) g + eval (Yg 0) peS g + eval (Yg 1) (Yg 2) g + eval (Yg 1) peS g

/-- **The permutation sum lies in `FF3 N`.** -/
theorem hexSum_mem {d : ℕ} {h : F2} (hd : 2 ≤ d) (hh : Homog d h) (hp : IsPrimitive h)
    (hsw : h + swapPoly h = 0) (hpent : lin515Expr N h = 0) : hexSum (rPoly h) ∈ FF3 N := by
  have hb : Function.Bijective swp := by decide
  have S := rSum_eq hd hh hp hsw ((xE_p5 (N := N)).comp hb)
  have z1 := piExpr_eq_zero (N := N) hpent (σ := swp) hb
  have z2 := piExpr_eq_zero (N := N) hpent (σ := fun i => swp (cyc2 i)) (by decide)
  have z3 := piExpr_eq_zero (N := N) hpent (σ := fun i => swp (cyc3 i)) (by decide)
  have z4 := piExpr_eq_zero (N := N) hpent (σ := fun i => swp (cyc4 i)) (by decide)
  simp only [] at S z1 z2 z3 z4
  rw [z1, z2, z3, z4] at S
  have e03 : xE N (swp 0) (swp 1) = psiL N (Yg 0) :=
    xE_eq_psiL (by simp [swp, peW, peW0]) (by simp [swp, peD, peD0])
  have e32 : xE N (swp 1) (swp 2) = psiL N (Yg 2) :=
    xE_eq_psiL (by simp [swp, peW, peW0]) (by simp [swp, peD, peD0])
  have e34 : xE N (swp 1) (swp 4) = psiL N peS :=
    xE_eq_psiL (by simp [swp, peW, peW0]) (by simp [swp, peD, peD0])
  have e31 : xE N (swp 1) (swp 3) = psiL N (Yg 1) :=
    xE_eq_psiL (by simp [swp, peW, peW0]) (by simp [swp, peD, peD0])
  rw [e03, e32, e34, e31, ← map_eval, ← map_eval, ← map_eval, ← map_eval, ← map_add, ← map_add,
    ← map_add] at S
  have := congrArg (fun φ : Module.End ℚ (M3 N) => φ (Submodule.Quotient.mk 1)) S
  simp only [psiL_mk, mul_one, add_zero, LinearMap.zero_apply] at this
  exact (Submodule.Quotient.mk_eq_zero _).1 this.symm

end Sum

/-! ### Back to `ℚ⟨X, Y⟩` -/

section ToF2

local notation "𝕏" => FreeAlgebra.ι ℚ (0 : Fin 2)
local notation "𝕐" => FreeAlgebra.ι ℚ (1 : Fin 2)

/-- The substitution `Yᵢ ↦ X_{g i}` from `ℚ⟨Y₁, Y₂, Y₃⟩` to `ℚ⟨X, Y⟩`. -/
noncomputable def qmap (g : Fin 3 → Fin 2) : F3 →ₐ[ℚ] F2 :=
  FreeAlgebra.lift ℚ fun i => FreeAlgebra.ι ℚ (g i)

/-- The substitution preserves word length, so it maps `FF3 m` into `FF m`. -/
theorem qmap_FF3 (g : Fin 3 → Fin 2) {m : ℕ} {p : F3} (hp : p ∈ FF3 m) : qmap g p ∈ FF m := by
  induction hp using Submodule.span_induction with
  | mem x hx =>
    obtain ⟨w, hw, rfl⟩ := hx
    have e : qmap g (w.map (FreeAlgebra.ι ℚ)).prod = ((w.map g).map (FreeAlgebra.ι ℚ)).prod := by
      rw [map_list_prod, List.map_map, List.map_map]
      congr 1
      exact List.map_congr_left fun i _ => by simp [qmap]
    rw [e]
    exact word_mem_FF _ (by simpa using hw)
  | zero => rw [map_zero]; exact zero_mem _
  | add x y _ _ hx hy => rw [map_add]; exact add_mem hx hy
  | smul r x _ hx => rw [map_smul]; exact Submodule.smul_mem _ r hx

/-- `u` is homogeneous of degree one. -/
def IsLin (u : F2) : Prop := ∀ r : ℚ, scF r u = r • u

theorem isLin_ι (i : Fin 2) : IsLin (FreeAlgebra.ι ℚ i) := fun r => by simp [scF]

theorem IsLin.add {u v : F2} (hu : IsLin u) (hv : IsLin v) : IsLin (u + v) := fun r => by
  rw [map_add, hu, hv, smul_add]

theorem IsLin.neg {u : F2} (hu : IsLin u) : IsLin (-u) := fun r => by
  rw [map_neg, hu, smul_neg]

theorem IsLin.sub {u v : F2} (hu : IsLin u) (hv : IsLin v) : IsLin (u - v) := fun r => by
  rw [map_sub, hu, hv, smul_sub]

theorem homog_eval {d : ℕ} {p u v : F2} (hp : Homog d p) (hu : IsLin u) (hv : IsLin v) :
    Homog d (eval u v p) := fun r => by
  rw [map_eval, hu, hv, eval_smul_of_homog hp]

theorem homog_rPoly {d : ℕ} {h : F2} (hh : Homog d h) : Homog d (rPoly h) :=
  (hh.add (homog_eval hh (isLin_ι 1) ((isLin_ι 0).neg.sub (isLin_ι 1)))).add
    (homog_eval hh ((isLin_ι 0).neg.sub (isLin_ι 1)) (isLin_ι 0))

theorem rPoly_anti {h : F2} (hsw : h + swapPoly h = 0) (u v : F2) :
    eval u v (rPoly h) = -eval v u (rPoly h) := by
  rw [eval_rPoly, eval_rPoly, show -v - u = -u - v by abel, eval_eq_neg_swap hsw v u,
    eval_eq_neg_swap hsw u (-u - v), eval_eq_neg_swap hsw (-u - v) v]
  abel

theorem rPoly_cyc {h : F2} (u v : F2) : eval v (-u - v) (rPoly h) = eval u v (rPoly h) := by
  rw [eval_rPoly, eval_rPoly, show -v - (-u - v) = u by abel]
  abel

theorem q1_hexSum (p : F2) :
    qmap ![0, 0, 1] (hexSum p) =
      eval 𝕏 𝕐 p + eval 𝕏 (-(𝕏 + 𝕏 + 𝕐)) p + eval 𝕏 𝕐 p + eval 𝕏 (-(𝕏 + 𝕏 + 𝕐)) p := by
  simp only [hexSum, peS, map_add, map_neg, map_eval, qmap, FreeAlgebra.lift_ι_apply]
  rfl

theorem q2_hexSum (p : F2) :
    qmap ![0, 1, 0] (hexSum p) =
      eval 𝕏 𝕏 p + eval 𝕏 (-(𝕏 + 𝕐 + 𝕏)) p + eval 𝕐 𝕏 p + eval 𝕐 (-(𝕏 + 𝕐 + 𝕏)) p := by
  simp only [hexSum, peS, map_add, map_neg, map_eval, qmap, FreeAlgebra.lift_ι_apply]
  rfl

/-- **The pure `ℚ⟨X, Y⟩` step.** A homogeneous `g` of degree `d ≥ 3` with the symmetries of the
hexagon polynomial and the two substituted permutation-sum relations is zero. -/
theorem eq_zero_of_hex_relations {d : ℕ} {g : F2} (hd : 3 ≤ d) (hg : Homog d g)
    (anti : ∀ u v : F2, eval u v g = -eval v u g)
    (cyc : ∀ u v : F2, eval v (-u - v) g = eval u v g)
    (F1 : eval 𝕏 𝕐 g + eval 𝕏 (-(𝕏 + 𝕏 + 𝕐)) g + eval 𝕏 𝕐 g + eval 𝕏 (-(𝕏 + 𝕏 + 𝕐)) g = 0)
    (F2' : eval 𝕏 𝕏 g + eval 𝕏 (-(𝕏 + 𝕐 + 𝕏)) g + eval 𝕐 𝕏 g + eval 𝕐 (-(𝕏 + 𝕐 + 𝕏)) g = 0) :
    g = 0 := by
  have eXY : eval 𝕏 𝕐 g = g := eval_ι_ι g
  have two : ∀ z : F2, z + z = 0 → z = 0 := fun z hz => by
    have : (2 : ℚ) • z = 0 := by rw [two_smul, hz]
    exact (smul_eq_zero.mp this).resolve_left (by norm_num)
  have hS : -(𝕏 + 𝕐 + 𝕏) = -(𝕏 + 𝕏 + 𝕐) := by abel
  have h1 : eval 𝕏 (-(𝕏 + 𝕏 + 𝕐)) g = -g := by
    have : g + eval 𝕏 (-(𝕏 + 𝕏 + 𝕐)) g = 0 := two _ (by rw [← F1, eXY]; abel)
    exact eq_neg_of_add_eq_zero_right this
  have hXX : eval 𝕏 𝕏 g = 0 := by
    have e := anti 𝕏 𝕏
    exact two _ (by nth_rewrite 1 [e]; abel)
  have hYX : eval 𝕐 𝕏 g = -g := by rw [anti, eXY]
  have h2X : eval ((2 : ℚ) • 𝕏) 𝕐 g = g + g := by
    have e := cyc ((2 : ℚ) • 𝕏) 𝕐
    rw [show -((2 : ℚ) • 𝕏) - 𝕐 = -(𝕏 + 𝕏 + 𝕐) by rw [two_smul]; abel] at e
    rw [hS, hXX, h1, hYX, e] at F2'
    calc eval ((2 : ℚ) • 𝕏) 𝕐 g = (0 + -g + -g + eval ((2 : ℚ) • 𝕏) 𝕐 g) + g + g := by abel
      _ = g + g := by rw [F2']; abel
  -- `m = g(X/2, Y)`
  have half : eval ((1 / 2 : ℚ) • 𝕏) 𝕐 g + eval ((1 / 2 : ℚ) • 𝕏) 𝕐 g = g := by
    have e := congrArg (eval ((1 / 2 : ℚ) • 𝕏) 𝕐) h2X
    rw [map_eval, map_add, map_smul, eval_X, eval_Y, smul_smul,
      show (2 : ℚ) * (1 / 2) = 1 by norm_num, one_smul, eXY] at e
    exact e.symm
  have hom : eval 𝕏 ((2 : ℚ) • 𝕐) g = (2 : ℚ) ^ d • eval ((1 / 2 : ℚ) • 𝕏) 𝕐 g := by
    have e := eval_smul_of_homog hg (2 : ℚ) ((1 / 2 : ℚ) • 𝕏) 𝕐
    rw [smul_smul, show (2 : ℚ) * (1 / 2) = 1 by norm_num, one_smul] at e
    exact e
  have swp2 : eval ((2 : ℚ) • 𝕐) 𝕏 g = -g + -g := by
    have e := congrArg (eval 𝕐 𝕏) h2X
    rw [map_eval, map_add, map_smul, eval_X, eval_Y, hYX] at e
    exact e
  have key : (2 : ℚ) ^ d • eval ((1 / 2 : ℚ) • 𝕏) 𝕐 g = g + g := by
    rw [← hom, anti, swp2, neg_add, neg_neg]
  set m := eval ((1 / 2 : ℚ) • 𝕏) 𝕐 g
  have k4 : ((2 : ℚ) ^ d - 4) • m = 0 := by
    rw [sub_smul, key, ← half, show (4 : ℚ) = 1 + 1 + 1 + 1 by norm_num, add_smul, add_smul,
      add_smul, one_smul]
    abel
  have hne : (2 : ℚ) ^ d - 4 ≠ 0 := by
    have : (2 : ℚ) ^ 3 ≤ 2 ^ d := pow_le_pow_right₀ (by norm_num) hd
    intro h0; norm_num at this; linarith
  have hm : m = 0 := (smul_eq_zero.mp k4).resolve_left hne
  rw [← half, hm, add_zero]

/-- **`R = 0`.** For a homogeneous primitive `h` of degree `d ≥ 3` with the 2-cycle relation,
whose permutation sum lies in `FF3 (d + 1)`, the hexagon polynomial vanishes. -/
theorem rPoly_eq_zero {d : ℕ} {h : F2} (hd : 3 ≤ d) (hh : Homog d h)
    (hsw : h + swapPoly h = 0) (hmem : hexSum (rPoly h) ∈ FF3 (d + 1)) : rPoly h = 0 := by
  have hR : Homog d (rPoly h) := homog_rPoly hh
  have lX := isLin_ι 0
  have lY := isLin_ι 1
  have m1 := qmap_FF3 ![0, 0, 1] hmem
  have m2 := qmap_FF3 ![0, 1, 0] hmem
  rw [q1_hexSum] at m1
  rw [q2_hexSum] at m2
  refine eq_zero_of_hex_relations hd hR (rPoly_anti hsw) rPoly_cyc
    (eq_zero_of_homog_mem_FF ?_ m1) (eq_zero_of_homog_mem_FF ?_ m2)
  · exact (((homog_eval hR lX lY).add (homog_eval hR lX ((lX.add lX).add lY).neg)).add
      (homog_eval hR lX lY)).add (homog_eval hR lX ((lX.add lX).add lY).neg)
  · exact (((homog_eval hR lX lX).add (homog_eval hR lX ((lX.add lY).add lX).neg)).add
      (homog_eval hR lY lX)).add (homog_eval hR lY ((lX.add lY).add lX).neg)

end ToF2

/-! ### The hexagon, and Furusho's theorem -/

section Hexagon

/-- **The linearised hexagon from `R = 0`.** -/
theorem lin513_eq_zero {M d : ℕ} {h : F2} (hd : 2 ≤ d) (hh : Homog d h) (hp : IsPrimitive h)
    (hsw : h + swapPoly h = 0) (hR : rPoly h = 0) : lin513Expr M h = 0 := by
  obtain ⟨c0, c1, c3⟩ := DK3.commute_sum (dk4 M).d4
  have k1 : eval (t M 1) (t M 3) h = eval (t M 1) (-t M 0 - t M 1) h := by
    conv_lhs => rw [show t M 3 = (-t M 0 - t M 1) + (t M 0 + t M 1 + t M 3) by abel]
    exact eval_add_right hd hh hp c1 (c0.neg_right.sub_right c1)
  have k2 : eval (t M 3) (t M 0) h = eval (-t M 0 - t M 1) (t M 0) h := by
    conv_lhs => rw [show t M 3 = (-t M 0 - t M 1) + (t M 0 + t M 1 + t M 3) by abel]
    exact eval_add_left hd hh hp (c0.neg_right.sub_right c1) c0
  have e := congrArg (eval (t M 0) (t M 1)) hR
  rw [eval_rPoly, map_zero] at e
  rw [lin513Expr, eval_eq_neg_swap hsw (t M 1) (t M 0), eval_eq_neg_swap hsw (t M 3) (t M 1),
    eval_eq_neg_swap hsw (t M 0) (t M 3), k1, k2, ← neg_add, ← neg_add, e, neg_zero]

/-- **Furusho's theorem, Lie-algebra form** (Furusho 2010, Theorem 3): for every `d ≥ 3`, a
homogeneous primitive element of degree `d` whose linearised pentagon (5.20) vanishes in
`U4 (d + 1)` has every linearised associator equation vanish there. -/
theorem pentagonHexagonLie_of_three_le : ∀ d, 3 ≤ d → PentagonHexagonLie d := by
  intro d hd3 h hh hp hpent
  have hd : 2 ≤ d := by omega
  have h515 : lin515Expr (d + 1) h = 0 := by
    simpa only [assocLin, LinearMap.coe_mk, AddHom.coe_mk] using hpent
  have hsw := add_swap_eq_zero_of_pentagon hd hh hp h515
  have hR := rPoly_eq_zero hd3 hh hsw (hexSum_mem hd hh hp hsw h515)
  have h513 := lin513_eq_zero (M := d + 1) hd hh hp hsw hR
  refine Prod.ext (funext fun p => ?_) (Prod.ext ?_ ?_)
  · simp only [assocLin, LinearMap.coe_mk, AddHom.coe_mk, Prod.fst_zero, Pi.zero_apply]
    rw [eval_eq_neg_swap hsw p.1.1 p.1.2, neg_add_cancel]
  · simp only [assocLin, LinearMap.coe_mk, AddHom.coe_mk, Prod.snd_zero, Prod.fst_zero]
    rw [lin513Expr] at h513
    rw [h513, neg_zero]
  · exact hpent

variable {K : Type*} [Field K] [Algebra ℚ K]

/-- **Pentagon implies hexagon**, with the Lie statement discharged: `assocU4_of_pentagon`
without its `PentagonHexagonLie` hypothesis. -/
theorem assocU4_of_pentagon' {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    (hT : GroupLikeKAssociatorTower K E) {N : ℕ} (hN : 3 ≤ N) {Φ : F2} (h3 : AssocU4 3 E Φ)
    (hp : Pentagon Φ (t N 0) (t N 1) (t N 3) (t N 4) (t N 5)) (hg : GL N Φ) :
    AssocU4 N E Φ :=
  assocU4_of_pentagon hE hT pentagonHexagonLie_of_three_le hN h3 hp hg

/-- `assocU4_iff_pentagon` without its `PentagonHexagonLie` hypothesis. -/
theorem assocU4_iff_pentagon' {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    (hT : GroupLikeKAssociatorTower K E) {N : ℕ} (hN : 3 ≤ N) {Φ : F2} (hg : GL N Φ) :
    AssocU4 N E Φ ↔
      AssocU4 3 E Φ ∧ Pentagon Φ (t N 0) (t N 1) (t N 3) (t N 4) (t N 5) :=
  assocU4_iff_pentagon hE hT pentagonHexagonLie_of_three_le hN hg

end Hexagon

end QOU.BraidsAndKnots.RationalAssociator
