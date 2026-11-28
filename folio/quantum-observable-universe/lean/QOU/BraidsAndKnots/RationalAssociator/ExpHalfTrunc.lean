import QOU.BraidsAndKnots.RationalAssociator.FurushoSingleLevel

/-!
# The per-level exponential `exp(X/2)` truncated at degree `N`

Audit `docs/audits/2026-11-27-grt-action-pentagon-derivation.md` §17p (owner ruling
2026-11-28: the hexagon exponential is per level).

§17o showed that one fixed polynomial `E` for all levels gives no associator tower once `E` has
positive degree: `expHalfPoly = 1 + X/2 + X²/8` has no associator in `U4 N`, `N ≥ 4`. The tower
(`GroupLikeKAssociatorTower`, `AssociatorChain.lean`) now takes a family `E : ℕ → ℚ⟨X, Y⟩`, the
exponential of level `N` being `E N`. This file supplies the family the KZ associator needs,
`exp(X/2)` truncated at degree `N`, and the facts that make it fit the one-degree machinery.

* `expHalfTrunc N = Σ_{k<N} X^k / (2^k k!)`. It is a rational polynomial; nothing here is
  analytic. `expHalfTrunc_three`: at `N = 3` it is `expHalfPoly`.
* `expHalfTrunc_succ_sub`: consecutive members differ by the single monomial
  `X^N / (2^N N!)`, which lies in `FF N`. Hence `expFamily_expHalfTrunc`: it is a compatible
  family, and in `U4 N` every `expHalfTrunc M`, `M ≥ N`, gives the same hexagon
  (`ExpFamily.assocU4_iff`).
* `assocDefect_add_exp`: **what the change of exponential costs at the top degree.** If
  `D ∈ FF d`, the defects of `Φ` in `U4 (d + 1)` for `E + D` and for `E` differ only in the
  hexagon component, by `D(t₁₃ + t₂₃) − D(t₁₃) − D(t₂₃)`. For `E = expHalfTrunc d`,
  `D = X^d / (2^d d!)`: so passing from level `d` to level `d + 1` adds exactly that degree-`d`
  term to the right-hand side of the linear system of `assocU4_add_iff`.
* `assocU4_three`, `GL_three`: `1 + [X, Y]/24` is a rational associator for `expHalfTrunc 3`
  modulo `3`, group-like modulo `FF2 3`; `kzLevel_three`: its base change at every field `K`.
  `assocU4_three_expHalfTrunc_four`: the same `Φ` is an associator modulo `3` for the level-`4`
  exponential, so the hypotheses of the one-degree statements at `d = 3` for
  `E = expHalfTrunc` are met (they are not vacuous).
* `exists_lift_expHalfTrunc_of_tower`, `obstructionVanishesAt_expHalfTrunc_of_tower`,
  `furushoGroupStep_expHalfTrunc_of_tower`: the one-degree results of `FurushoGroupStep.lean`
  for `E = expHalfTrunc`, **conditional on** `GroupLikeKAssociatorTower K expHalfTrunc`.

No `axiom`, no `sorry`, no analysis.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

open TensorProduct Friedrichs

local notation "F2" => FreeAlgebra ℚ (Fin 2)

/-! ### 1. The family -/

/-- `exp(X/2)` truncated at degree `N`: `Σ_{k<N} X^k / (2^k k!)`. In `U4 N` (words of length
`N` vanish) its evaluations are those of the full exponential. -/
noncomputable def expHalfTrunc (N : ℕ) : F2 :=
  ∑ k ∈ Finset.range N, ((2 ^ k * k.factorial : ℕ) : ℚ)⁻¹ • FreeAlgebra.ι ℚ 0 ^ k

theorem expHalfTrunc_three : expHalfTrunc 3 = expHalfPoly := by
  simp only [expHalfTrunc, expHalfPoly, Finset.sum_range_succ, Finset.sum_range_zero]
  norm_num [Nat.factorial, pow_two]

theorem algebraMapInv_expHalfTrunc {N : ℕ} (hN : 1 ≤ N) :
    FreeAlgebra.algebraMapInv (expHalfTrunc N) = 1 := by
  obtain ⟨M, rfl⟩ : ∃ M, N = M + 1 := ⟨N - 1, by omega⟩
  rw [expHalfTrunc, map_sum, Finset.sum_range_succ', Finset.sum_eq_zero (fun i _ => ?_), zero_add]
  · simp [FreeAlgebra.algebraMapInv]
  · simp [pow_succ, FreeAlgebra.algebraMapInv]

/-- `X ^ N` is a word of length `N`. -/
theorem ι_zero_pow_mem_FF (N : ℕ) : FreeAlgebra.ι ℚ (0 : Fin 2) ^ N ∈ FF N := by
  have h := word_mem_FF (m := N) (List.replicate N (0 : Fin 2)) (by simp)
  simpa [List.map_replicate, List.prod_replicate] using h

/-- **Consecutive levels differ by one monomial of degree `N`.** -/
theorem expHalfTrunc_succ_sub (N : ℕ) :
    expHalfTrunc (N + 1) - expHalfTrunc N =
      ((2 ^ N * N.factorial : ℕ) : ℚ)⁻¹ • FreeAlgebra.ι ℚ 0 ^ N := by
  rw [expHalfTrunc, expHalfTrunc, Finset.sum_range_succ, add_sub_cancel_left]

theorem expHalfTrunc_succ_sub_mem_FF (N : ℕ) : expHalfTrunc (N + 1) - expHalfTrunc N ∈ FF N := by
  rw [expHalfTrunc_succ_sub]
  exact Submodule.smul_mem _ _ (ι_zero_pow_mem_FF N)

/-- **`expHalfTrunc` is a compatible family of exponentials.** -/
theorem expFamily_expHalfTrunc : ExpFamily expHalfTrunc :=
  ⟨fun _ hN => algebraMapInv_expHalfTrunc hN, expHalfTrunc_succ_sub_mem_FF⟩

/-! ### 2. The top-degree change of the defect -/

section TopDegree

variable {N : ℕ}

private theorem sub_one_mul_mem {x y : U4 N} (hx : x - 1 ∈ Fil N 1) (hy : y - 1 ∈ Fil N 1) :
    x * y - 1 ∈ Fil N 1 := by
  have e : x * y - 1 = (x - 1) * (y - 1) + (x - 1) + (y - 1) := by
    simp only [mul_sub, sub_mul, mul_one, one_mul]; abel
  rw [e]
  exact add_mem (add_mem (Fil_anti (by norm_num) (mul_mem_Fil' (by norm_num : 1 + 1 = 2) hx hy))
    hx) hy

private theorem mul_left_sub_mem {d : ℕ} {x δ : U4 N} (hx : x - 1 ∈ Fil N 1)
    (hδ : δ ∈ Fil N d) : x * δ - δ ∈ Fil N (d + 1) := by
  have e : x * δ - δ = (x - 1) * δ := by rw [sub_mul, one_mul]
  rw [e]; exact mul_mem_Fil' (by omega) hx hδ

private theorem mul_right_sub_mem {d : ℕ} {x δ : U4 N} (hx : x - 1 ∈ Fil N 1)
    (hδ : δ ∈ Fil N d) : δ * x - δ ∈ Fil N (d + 1) := by
  have e : δ * x - δ = δ * (x - 1) := by rw [mul_sub, mul_one]
  rw [e]; exact mul_mem_Fil' rfl hδ hx

private theorem eval_sub_one_mem {p : F2} (hp : FreeAlgebra.algebraMapInv p = 1) {a b : U4 N}
    (ha : a ∈ Fil N 1) (hb : b ∈ Fil N 1) : eval a b p - 1 ∈ Fil N 1 := by
  have := eval_mem_Fil ha hb (sub_one_mem_FF_one hp)
  rwa [map_sub, map_one] at this

/-- In `U4 (d + 1)`, `a δ b`, with `a, b ≡ 1` and `δ` of filtration `d`, is `δ`. -/
private theorem sandwich_eq {d : ℕ} {a δ b : U4 (d + 1)} (ha : a - 1 ∈ Fil (d + 1) 1)
    (hb : b - 1 ∈ Fil (d + 1) 1) (hδ : δ ∈ Fil (d + 1) d) : a * δ * b = δ := by
  have h1 := mul_left_sub_mem ha hδ
  have h2 : a * δ ∈ Fil (d + 1) d := by
    have e : a * δ = (a * δ - δ) + δ := by abel
    rw [e]; exact add_mem (Fil_anti (by omega) h1) hδ
  have h3 := mul_right_sub_mem hb h2
  rw [← sub_eq_zero]
  have e : a * δ * b - δ = (a * δ * b - a * δ) + (a * δ - δ) := by abel
  rw [e, eq_zero_of_mem_Fil h3, eq_zero_of_mem_Fil h1, add_zero]

/-- **Changing the exponential by `D ∈ FF d` changes the degree-`(d + 1)` defect only in the
hexagon component, by `D(t₁₃ + t₂₃) − D(t₁₃) − D(t₂₃)`.** Here `ε(E) = ε(Φ) = 1` and `d ≥ 1`.
(In the coordinates of `assocDefect`, `t₁₂ = t 0`, `t₁₃ = t 1`, `t₂₃ = t 3`.) -/
theorem assocDefect_add_exp {d : ℕ} (hd : 1 ≤ d) {E D Φ : F2}
    (hE : FreeAlgebra.algebraMapInv E = 1) (hΦ : FreeAlgebra.algebraMapInv Φ = 1)
    (hD : D ∈ FF d) :
    assocDefect (d + 1) (E + D) Φ = assocDefect (d + 1) E Φ +
      (0, eval (t (d + 1) 1 + t (d + 1) 3) 0 D - eval (t (d + 1) 1) 0 D -
        eval (t (d + 1) 3) 0 D, 0) := by
  set N := d + 1
  have h0 : (0 : U4 N) ∈ Fil N 1 := zero_mem _
  have ht := fun i => (t_mem_Fil_one (N := N) i)
  set a := eval (t N 1) (t N 0) Φ with ha_def
  set b := eval (t N 3) (t N 1) Φ with hb_def
  set c := eval (t N 0) (t N 3) Φ with hc_def
  set e1 := eval (t N 1) 0 E with he1_def
  set e2 := eval (t N 3) 0 E with he2_def
  set δ1 := eval (t N 1) 0 D with hδ1_def
  set δ2 := eval (t N 3) 0 D with hδ2_def
  have ha : a - 1 ∈ Fil N 1 := eval_sub_one_mem hΦ (ht 1) (ht 0)
  have hb : b - 1 ∈ Fil N 1 := eval_sub_one_mem hΦ (ht 3) (ht 1)
  have hc : c - 1 ∈ Fil N 1 := eval_sub_one_mem hΦ (ht 0) (ht 3)
  have he1 : e1 - 1 ∈ Fil N 1 := eval_sub_one_mem hE (ht 1) h0
  have he2 : e2 - 1 ∈ Fil N 1 := eval_sub_one_mem hE (ht 3) h0
  have hδ1 : δ1 ∈ Fil N d := eval_mem_Fil (ht 1) h0 hD
  have hδ2 : δ2 ∈ Fil N d := eval_mem_Fil (ht 3) h0 hD
  -- the three cross terms
  have k1 : a * δ1 * b * e2 * c = δ1 := by
    have := sandwich_eq ha (sub_one_mul_mem (sub_one_mul_mem hb he2) hc) hδ1
    simpa only [mul_assoc] using this
  have k2 : a * e1 * b * δ2 * c = δ2 := by
    have := sandwich_eq (sub_one_mul_mem (sub_one_mul_mem ha he1) hb) hc hδ2
    simpa only [mul_assoc] using this
  have k3 : a * δ1 * b * δ2 * c = 0 := by
    have hm : δ1 * b * δ2 ∈ Fil N (d + d) :=
      mul_mem_Fil' rfl (mul_mem_Fil' (add_zero d) hδ1 (mem_Fil_zero b)) hδ2
    have hm' : a * (δ1 * b * δ2) * c ∈ Fil N (0 + (d + d) + 0) :=
      mul_mem_Fil' rfl (mul_mem_Fil' rfl (mem_Fil_zero a) hm) (mem_Fil_zero c)
    have hm'' : a * (δ1 * b * δ2) * c ∈ Fil N N :=
      Fil_anti (show N ≤ 0 + (d + d) + 0 by omega) hm'
    have := eq_zero_of_mem_Fil hm''
    simpa only [mul_assoc] using this
  have key : a * (e1 + δ1) * b * (e2 + δ2) * c = a * e1 * b * e2 * c + δ1 + δ2 := by
    simp only [mul_add, add_mul, k1, k2, k3, add_zero]
  refine Prod.ext ?_ (Prod.ext ?_ ?_)
  · simp [assocDefect]
  · simp only [assocDefect, Prod.snd_add, Prod.fst_add, map_add, ← ha_def, ← hb_def, ← hc_def,
      ← he1_def, ← he2_def, ← hδ1_def, ← hδ2_def, key]
    abel
  · simp [assocDefect]

/-- For the family `expHalfTrunc`, passing from level `d` to level `d + 1` adds to the
hexagon defect exactly the homogeneous degree-`d` term
`((t₁₃ + t₂₃)^d − t₁₃^d − t₂₃^d) / (2^d d!)`. -/
theorem assocDefect_expHalfTrunc_succ {d : ℕ} (hd : 1 ≤ d) {Φ : F2}
    (hΦ : FreeAlgebra.algebraMapInv Φ = 1) :
    assocDefect (d + 1) (expHalfTrunc (d + 1)) Φ = assocDefect (d + 1) (expHalfTrunc d) Φ +
      (0, ((2 ^ d * d.factorial : ℕ) : ℚ)⁻¹ • ((t (d + 1) 1 + t (d + 1) 3) ^ d -
        t (d + 1) 1 ^ d - t (d + 1) 3 ^ d), 0) := by
  have e : expHalfTrunc (d + 1) =
      expHalfTrunc d + ((2 ^ d * d.factorial : ℕ) : ℚ)⁻¹ • FreeAlgebra.ι ℚ 0 ^ d := by
    rw [← expHalfTrunc_succ_sub, add_sub_cancel]
  rw [e, assocDefect_add_exp hd (algebraMapInv_expHalfTrunc hd) hΦ
    (Submodule.smul_mem _ _ (ι_zero_pow_mem_FF d))]
  congr 2
  simp only [map_smul, map_pow, eval_X, smul_sub]

end TopDegree

/-! ### 3. Level `3`, unconditionally -/

/-- The commutator of two primitive elements is primitive. -/
theorem IsPrimitive.commutator {p q : F2} (hp : IsPrimitive p) (hq : IsPrimitive q) :
    IsPrimitive (p * q - q * p) := by
  unfold IsPrimitive at *
  rw [map_sub, map_mul, map_mul, hp, hq]
  simp only [add_mul, mul_add, Algebra.TensorProduct.tmul_mul_tmul, mul_one, one_mul,
    sub_tmul, tmul_sub]
  abel

theorem isPrimitive_ι (i : Fin 2) : IsPrimitive (FreeAlgebra.ι ℚ i) := by
  unfold IsPrimitive; exact cop_g i

/-- `[X, Y]` lies in `FF 2`. -/
theorem commutator_mem_FF2 :
    FreeAlgebra.ι ℚ 0 * FreeAlgebra.ι ℚ 1 - FreeAlgebra.ι ℚ 1 * FreeAlgebra.ι ℚ 0 ∈ FF 2 :=
  sub_mem (mul_mem_FF' (a := 1) (b := 1) (c := 2) rfl (ι_mem_FF_one 0) (ι_mem_FF_one 1))
    (mul_mem_FF' (a := 1) (b := 1) (c := 2) rfl (ι_mem_FF_one 1) (ι_mem_FF_one 0))

/-- `φ_c = 1 + c·[X, Y]` is group-like modulo `FF2 3`, for every `c`. -/
theorem GL_three (c : ℚ) : GL 3 (phiPoly c) := by
  have hp : IsPrimitive (c • (FreeAlgebra.ι ℚ 0 * FreeAlgebra.ι ℚ 1 -
      FreeAlgebra.ι ℚ 1 * FreeAlgebra.ι ℚ 0)) :=
    Friedrichs.IsPrimitive.smul
      (IsPrimitive.commutator (isPrimitive_ι 0) (isPrimitive_ι 1)) c
  exact GL.add_primitive (d := 2) (by norm_num) (map_one _) (GL_one 3)
    (Submodule.smul_mem _ c commutator_mem_FF2) hp

/-- In `U4 3`, any set of elements of filtration `≥ 1` has vanishing triple products. -/
private theorem trunc3_of_fil {S : Set (U4 3)} (hS : ∀ w ∈ S, w ∈ Fil 3 1) : Trunc3 S :=
  fun hx hy hz => eq_zero_of_mem_Fil (mul_mem_Fil' (a := 2) (b := 1) (c := 3) rfl
    (mul_mem_Fil' (a := 1) (b := 1) (c := 2) rfl (hS _ hx) (hS _ hy)) (hS _ hz))

/-- **A rational associator modulo `3`**: `1 + [X, Y]/24` for `expHalfPoly`. -/
theorem assocU4_three : AssocU4 3 expHalfPoly (phiPoly (1 / 24)) where
  const := by simp [phiPoly, FreeAlgebra.algebraMapInv]
  inv := fun a b ha hb => by
    rw [eval_phiPoly, eval_phiPoly]
    refine inversion _ (trunc3_of_fil ?_)
    intro w hw; rcases hw with rfl | rfl <;> assumption
  hex := by
    have dk := dk4 3
    have hT : Trunc3 ({t 3 0, t 3 1, t 3 3} : Set (U4 3)) := by
      refine trunc3_of_fil ?_
      intro w hw; rcases hw with rfl | rfl | rfl <;> exact t_mem_Fil_one _
    rw [hexagon_expHalfPoly_iff, hexagon_iff _ hT dk.n12_3 dk.n13_2]
    simp
  pent := by
    refine pentagon_phiPoly _ (trunc3_of_fil ?_) (dk4 3)
    intro w hw; rcases hw with rfl | rfl | rfl | rfl | rfl | rfl <;> exact t_mem_Fil_one _

/-- The same `Φ`, read with the level-`4` exponential: in `U4 3` it does not matter. -/
theorem assocU4_three_expHalfTrunc_four : AssocU4 3 (expHalfTrunc 4) (phiPoly (1 / 24)) :=
  (expFamily_expHalfTrunc.assocU4_iff (by norm_num : 3 ≤ 4)).2
    (by rw [expHalfTrunc_three]; exact assocU4_three)

variable {K : Type*} [Field K] [Algebra ℚ K]

/-- **The KZ field at level `3`, with no analysis.** Over every field `K` there is a
group-like `K`-associator modulo `3` for `expHalfTrunc 3`: the base change of `1 + [X, Y]/24`. -/
theorem kzLevel_three :
    ∃ Ψ : K ⊗[ℚ] F2, AssocK K 3 (expHalfTrunc 3) Ψ ∧ GLK K 3 Ψ := by
  rw [expHalfTrunc_three]
  exact ⟨(1 : K) ⊗ₜ phiPoly (1 / 24), assocK_of_assocU4 assocU4_three, GLK_of_GL (GL_three _)⟩

/-! ### 4. The one-degree results for `expHalfTrunc`, conditional on the tower -/

/-- **One degree up, with `exp(X/2)` at both levels**, conditional on the tower: for `d ≥ 3`, a
rational associator modulo `d` for `expHalfTrunc d`, group-like modulo `FF2 d`, extends by some
`x ∈ FF d` to one modulo `d + 1` for `expHalfTrunc (d + 1)`. At `d = 3` the hypotheses are met by
`1 + [X, Y]/24` (`assocU4_three`, `GL_three`). -/
theorem exists_lift_expHalfTrunc_of_tower (hT : GroupLikeKAssociatorTower K expHalfTrunc)
    {d : ℕ} (hd : 3 ≤ d) {Φ : F2} (hA : AssocU4 d (expHalfTrunc d) Φ) (hG : GL d Φ) :
    ∃ x ∈ FF d, AssocU4 (d + 1) (expHalfTrunc (d + 1)) (Φ + x) ∧ GL (d + 1) (Φ + x) :=
  exists_lift_of_tower expFamily_expHalfTrunc hT hd hA hG

theorem obstructionVanishesAt_expHalfTrunc_of_tower
    (hT : GroupLikeKAssociatorTower K expHalfTrunc) {d : ℕ} (hd : 3 ≤ d) :
    ObstructionVanishesAt (expHalfTrunc (d + 1)) d :=
  obstructionVanishesAt_of_tower expFamily_expHalfTrunc hT hd

theorem furushoGroupStep_expHalfTrunc_of_tower
    (hT : GroupLikeKAssociatorTower K expHalfTrunc) {d : ℕ} (hd : 3 ≤ d) :
    FurushoGroupStep (expHalfTrunc (d + 1)) d :=
  furushoGroupStep_of_tower expFamily_expHalfTrunc hT hd

theorem pentagonLiftVanishes_expHalfTrunc_of_tower
    (hT : GroupLikeKAssociatorTower K expHalfTrunc) {d : ℕ} (hd : 3 ≤ d) :
    PentagonLiftVanishes (expHalfTrunc (d + 1)) d :=
  pentagonLiftVanishes_of_tower expFamily_expHalfTrunc hT hd

end QOU.BraidsAndKnots.RationalAssociator
