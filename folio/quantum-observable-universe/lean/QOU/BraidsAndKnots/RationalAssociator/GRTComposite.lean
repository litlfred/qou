import QOU.BraidsAndKnots.RationalAssociator.GRTClosure

/-!
# The composite `g₁ ∘ g₂` as a polynomial, and closure of `GRT₁` in `U4 N`

Bean `qou-3fdg` (stage-4 blocker, epic `qou-dk7p`). Drinfeld's numbering (1991, §5).

Drinfeld's group law (5.16), `(g₁ ∘ g₂)(A,B) = g₁(g₂ A g₂⁻¹, B) · g₂`, is written as a
polynomial without inverses: by (5.12) the inverse of `g₂(A,B)` is `g₂(B,A)`, so

  `compPoly g₁ g₂ = g₁(g₂ · A · swapPoly g₂, B) · g₂`,  `swapPoly g (A,B) = g(B,A)`.

* `eval_compPoly`: `eval a b (compPoly g₁ g₂) = compEval g₁ g₂ a b` (no hypotheses).
* `algebraMapInv_compPoly`: the constant term of `compPoly g₁ g₂` is `ε(g₁) ε(g₂)`.
* `pentagon_compPoly_U4`, `hexagon_compPoly_U4`: the pentagon and hexagon action theorems of
  `NilpotentUnits.lean` / `HexagonUniversal.lean`, restated for the polynomial `compPoly`.
* `GRT1U4 N g`: the four `GRT₁` conditions in `U4 N`. `grt1U4_comp`: `GRT1U4` is closed under
  `compPoly`.

Nothing analytic is used.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

section Poly

variable {R : Type*} [Ring R] [Algebra ℚ R]

/-- `g(B, A)`: the two variables swapped. -/
noncomputable def swapPoly (g : FreeAlgebra ℚ (Fin 2)) : FreeAlgebra ℚ (Fin 2) :=
  FreeAlgebra.lift ℚ ![FreeAlgebra.ι ℚ 1, FreeAlgebra.ι ℚ 0] g

/-- Drinfeld's (5.16) as a polynomial, inverses written through (5.12). -/
noncomputable def compPoly (g1 g2 : FreeAlgebra ℚ (Fin 2)) : FreeAlgebra ℚ (Fin 2) :=
  FreeAlgebra.lift ℚ ![g2 * FreeAlgebra.ι ℚ 0 * swapPoly g2, FreeAlgebra.ι ℚ 1] g1 * g2

/-- Evaluation after substitution is evaluation at the substituted values. -/
theorem eval_lift (a b : R) (p q g : FreeAlgebra ℚ (Fin 2)) :
    eval a b (FreeAlgebra.lift ℚ ![p, q] g) = eval (eval a b p) (eval a b q) g := by
  have : (eval a b).comp (FreeAlgebra.lift ℚ ![p, q]) = eval (eval a b p) (eval a b q) := by
    apply FreeAlgebra.hom_ext
    funext i
    fin_cases i <;> simp [eval]
  exact congrArg (fun f : FreeAlgebra ℚ (Fin 2) →ₐ[ℚ] R => f g) this

theorem eval_swapPoly (a b : R) (g : FreeAlgebra ℚ (Fin 2)) :
    eval a b (swapPoly g) = eval b a g := by
  simp [swapPoly, eval_lift]

theorem eval_compPoly (g1 g2 : FreeAlgebra ℚ (Fin 2)) (a b : R) :
    eval a b (compPoly g1 g2) = compEval g1 g2 a b := by
  simp [compPoly, compEval, eval_lift, eval_swapPoly]

theorem algebraMapInv_compPoly (g1 g2 : FreeAlgebra ℚ (Fin 2)) :
    FreeAlgebra.algebraMapInv (compPoly g1 g2) =
      FreeAlgebra.algebraMapInv g1 * FreeAlgebra.algebraMapInv g2 := by
  have : (FreeAlgebra.algebraMapInv : FreeAlgebra ℚ (Fin 2) →ₐ[ℚ] ℚ).comp
      (FreeAlgebra.lift ℚ ![g2 * FreeAlgebra.ι ℚ 0 * swapPoly g2, FreeAlgebra.ι ℚ 1]) =
      FreeAlgebra.algebraMapInv := by
    apply FreeAlgebra.hom_ext
    funext i
    fin_cases i <;> simp [FreeAlgebra.algebraMapInv]
  simp only [compPoly, map_mul]
  rw [← AlgHom.comp_apply, this]

end Poly

section U4

variable {N : ℕ}

/-- `x y z = 1` with `x` a unit gives `y z x = 1`. -/
theorem rotate_of_isUnit {R : Type*} [Ring R] {x y z : R} (hx : IsUnit x)
    (h : x * y * z = 1) : y * z * x = 1 := by
  obtain ⟨u, rfl⟩ := hx
  have e : (↑u⁻¹ : R) = y * z := Units.inv_eq_of_mul_eq_one_right (by rw [← mul_assoc]; exact h)
  rw [← e, Units.inv_mul]

/-- `eval` at a pair of sums of generators of the composite is `actEval` with `G = gU`. -/
theorem eval_compPoly_gU (g1 g2 : FreeAlgebra ℚ (Fin 2)) (hg1 : FreeAlgebra.algebraMapInv g2 = 1)
    (h512 : Inv512 (Fil N 1) g2) (l m : List (Fin 6)) :
    eval (tsum N l) (tsum N m) (compPoly g1 g2) =
      actEval g1 (tsum N l) (tsum N m) (gU N hg1 l m) := by
  rw [eval_compPoly]
  exact compEval_eq_actEval g1 g2 _ (by simp) (h512 _ _ (tsum_mem l) (tsum_mem m))

/-- `DK3` is invariant under reversing the triple. -/
theorem DK3.rev {R : Type*} [Ring R] {a b c : R} (h : DK3 a b c) : DK3 c b a :=
  ⟨by rw [add_comm]; exact h.n23_1, by rw [add_comm]; exact h.n13_2,
    by rw [add_comm]; exact h.n12_3⟩

/-- **The pentagon of the composite.** `g₁`'s pentagon and `g₂`'s (5.12), (5.14), pentagon and
constant term give the pentagon of `compPoly g₁ g₂` at the universal family of `U4 N`. -/
theorem pentagon_compPoly_U4 (g1 g2 : FreeAlgebra ℚ (Fin 2))
    (hg1 : FreeAlgebra.algebraMapInv g2 = 1) (h512 : Inv512 (Fil N 1) g2)
    (h514 : TComp514 (Fil N 1) g2)
    (hg : Pentagon g2 (t N 0) (t N 1) (t N 3) (t N 4) (t N 5))
    (hφ : Pentagon g1 (t N 0) (t N 1) (t N 3) (t N 4) (t N 5)) :
    Pentagon (compPoly g1 g2) (t N 0) (t N 1) (t N 3) (t N 4) (t N 5) := by
  have m := fun i => t_mem_Fil_one (N := N) i
  have hA : TCompat (t N 1) (t N 3) (gU N hg1 [0] [3]) (gU N hg1 [1] [3]) :=
    (tcompat_iff_poly g2 _ _ (by simp [tsum]) (by simp [tsum]) (h512 _ _ (m 0) (m 3))
      (h512 _ _ (m 1) (m 3))).2 (h514 _ _ _ (m 0) (m 1) (m 3) (dk4 N).d4)
  have hB : TCompat (t N 4) (t N 3) (gU N hg1 [5] [3]) (gU N hg1 [4] [3]) :=
    (tcompat_iff_poly g2 _ _ (by simp [tsum]) (by simp [tsum]) (h512 _ _ (m 5) (m 3))
      (h512 _ _ (m 4) (m 3))).2 (h514 _ _ _ (m 5) (m 4) (m 3) (dk4 N).d0.rev)
  have key := pentagon_act_U4 g1 g2 hg1 hg hφ (h512 _ _ (m 5) (m 3)) (h512 _ _ (m 4) (m 3))
    hA hB
  have e := fun l m' => eval_compPoly_gU (N := N) g1 g2 hg1 h512 l m'
  have e1 := e [0] [3, 4]
  have e2 := e [1, 3] [5]
  have e3 := e [3] [5]
  have e4 := e [0, 1] [4, 5]
  have e5 := e [0] [3]
  simp only [tsum, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, add_zero]
    at e1 e2 e3 e4 e5
  unfold Pentagon
  rw [e1, e2, e3, e4, e5]
  exact key

/-- **The hexagon of the composite**, for any exponential `E`: `g₁`'s hexagon at the universal
family and `g₂`'s constant term, (5.12), (5.13) (the `μ = 0` hexagon at the universal family)
and (5.14) give the hexagon of `compPoly g₁ g₂` there. -/
theorem hexagon_compPoly_U4 (g1 g2 E : FreeAlgebra ℚ (Fin 2))
    (hg1 : FreeAlgebra.algebraMapInv g2 = 1) (h512 : Inv512 (Fil N 1) g2)
    (h513 : Hexagon g2 1 (t N 0) (t N 1) (t N 3)) (h514 : TComp514 (Fil N 1) g2)
    (hφ : Hexagon g1 E (t N 0) (t N 1) (t N 3)) :
    Hexagon (compPoly g1 g2) E (t N 0) (t N 1) (t N 3) := by
  have m := fun i => t_mem_Fil_one (N := N) i
  have hcyc : eval (t N 3) (t N 1) g2 * eval (t N 0) (t N 3) g2 * eval (t N 1) (t N 0) g2 = 1 := by
    apply rotate_of_isUnit (isUnit_eval nilIdeal_Fil (m 1) (m 0) hg1)
    have := h513
    simp only [Hexagon, map_one, mul_one] at this
    rw [← this]
  have htc : TCompat (t N 1) (t N 0) (gU N hg1 [3] [0]) (gU N hg1 [1] [0]) :=
    (tcompat_iff_poly g2 _ _ (by simp [tsum]) (by simp [tsum]) (h512 _ _ (m 3) (m 0))
      (h512 _ _ (m 1) (m 0))).2 (h514 _ _ _ (m 3) (m 1) (m 0) (dk4 N).d4.rev)
  have key := hexagon_act_U4_universal g1 g2 E hg1 (h512 _ _ (m 3) (m 0)) hcyc htc hφ
  have e := fun l m' => eval_compPoly_gU (N := N) g1 g2 hg1 h512 l m'
  have e1 := e [1] [0]
  have e2 := e [3] [1]
  have e3 := e [0] [3]
  simp only [tsum, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, add_zero]
    at e1 e2 e3
  unfold Hexagon
  rw [e1, e2, e3]
  exact key

/-- The four `GRT₁` conditions (Drinfeld (5.12)–(5.15)) in `U4 N`, with constant term `1`.
(5.12) and (5.14) are required on all of `Fil N 1`; (5.13) and (5.15) at the universal family. -/
structure GRT1U4 (N : ℕ) (g : FreeAlgebra ℚ (Fin 2)) : Prop where
  const : FreeAlgebra.algebraMapInv g = 1
  inv512 : Inv512 (Fil N 1) g
  hex513 : Hexagon g 1 (t N 0) (t N 1) (t N 3)
  tc514 : TComp514 (Fil N 1) g
  pent515 : Pentagon g (t N 0) (t N 1) (t N 3) (t N 4) (t N 5)

/-- **`GRT₁` in `U4 N` is closed under Drinfeld's group law (5.16).** -/
theorem grt1U4_comp {g1 g2 : FreeAlgebra ℚ (Fin 2)} (h1 : GRT1U4 N g1) (h2 : GRT1U4 N g2) :
    GRT1U4 N (compPoly g1 g2) where
  const := by rw [algebraMapInv_compPoly, h1.const, h2.const, mul_one]
  inv512 := fun a b ha hb => by
    rw [eval_compPoly, eval_compPoly]; exact comp_inv512 nilIdeal_Fil h1.inv512 h2.inv512 ha hb
  hex513 := hexagon_compPoly_U4 g1 g2 1 h2.const h2.inv512 h2.hex513 h2.tc514 h1.hex513
  tc514 := fun u v w hu hv hw hDK => by
    unfold TCompatPoly
    simp only [eval_compPoly]
    exact comp_tcompat nilIdeal_Fil h2.inv512 h1.tc514 h2.tc514 hu hv hw hDK
  pent515 := pentagon_compPoly_U4 g1 g2 h2.const h2.inv512 h2.tc514 h2.pent515 h1.pent515

end U4

end QOU.BraidsAndKnots.RationalAssociator
