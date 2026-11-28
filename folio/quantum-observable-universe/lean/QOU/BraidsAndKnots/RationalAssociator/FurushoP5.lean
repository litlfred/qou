import QOU.BraidsAndKnots.RationalAssociator.FurushoTwoCycle
import QOU.BraidsAndKnots.RationalAssociator.Prop57Link

/-!
# Furusho's Lie-algebra theorem, part 2: five-strand families and the permutation sum

Bean `qou-3fdg` (epic `qou-dk7p`). A **five-strand family** (`P5`) in a `ℚ`-algebra is a
symmetric matrix `x i j` (`i, j : Fin 5`) with zero diagonal and zero row sums, whose entries on
disjoint pairs commute. These are the relations of the infinitesimal pure braid algebra on five
points with the fifth row eliminated (Furusho, *Pentagon and hexagon equations*, Ann. of Math.
171 (2010), §4). This file proves, over any `ℚ`-algebra:

* `P5.comp`: relabelling by a bijection of `Fin 5` preserves the relations.
* `P5.tri`: every triangle sums to the complementary entry, `x₀₁ + x₀₂ + x₁₂ = x₃₄`.
* `P5.dk4`: the entries on the first four strands form a `DK4` family.
* `piExpr_eq` (Furusho's Lemma 5): for a Lie element `h` of degree `≥ 2` with the 2-cycle
  relation, the linearised pentagon (5.20) at a `P5` family is the sum of `h(x_{ij}, x_{jk})`
  over the five consecutive triples of the cycle `(0 1 2 3 4)`.
* `rSum_eq` (the permutation sum in the proof of Furusho's Theorem 3): the sum of the linearised
  pentagon over the four cycles `(0 1 2 3 4)`, `(4 3 1 2 0)`, `(0 2 3 1 4)`, `(3 2 0 1 4)` is the
  sum of four values of the hexagon polynomial `R = h + h(Y, −X − Y) + h(−X − Y, X)`.

Everything is algebraic; no analytic notion and no numerical value is used.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

open Friedrichs

local notation "F2" => FreeAlgebra ℚ (Fin 2)

section P5

variable {R : Type*} [Ring R] [Algebra ℚ R]

/-- A five-strand family: symmetric, zero diagonal, zero row sums, disjoint entries commute. -/
structure P5 (x : Fin 5 → Fin 5 → R) : Prop where
  symm : ∀ i j, x i j = x j i
  diag : ∀ i, x i i = 0
  row : ∀ i, ∑ j, x i j = 0
  far : ∀ i j k l, i ≠ k → i ≠ l → j ≠ k → j ≠ l → Commute (x i j) (x k l)

omit [Algebra ℚ R] in
/-- It suffices to check the far relations for `i < j`, `k < l`, `i < k`. -/
theorem P5.of_ordered {x : Fin 5 → Fin 5 → R} (hs : ∀ i j, x i j = x j i)
    (hd : ∀ i, x i i = 0) (hr : ∀ i, ∑ j, x i j = 0)
    (hf : ∀ i j k l, i < j → k < l → i < k → j ≠ k → j ≠ l → Commute (x i j) (x k l)) :
    P5 x := by
  refine ⟨hs, hd, hr, ?_⟩
  have key : ∀ i j k l, i < j → k < l → i ≠ k → i ≠ l → j ≠ k → j ≠ l →
      Commute (x i j) (x k l) := by
    intro i j k l hij hkl h1 h2 h3 h4
    rcases lt_or_gt_of_ne h1 with h | h
    · exact hf i j k l hij hkl h h3 h4
    · exact (hf k l i j hkl hij h h2.symm h4.symm).symm
  intro i j k l h1 h2 h3 h4
  rcases lt_trichotomy i j with hij | rfl | hij
  · rcases lt_trichotomy k l with hkl | rfl | hkl
    · exact key i j k l hij hkl h1 h2 h3 h4
    · rw [hd]; exact Commute.zero_right _
    · rw [hs k l]; exact key i j l k hij hkl h2 h1 h4 h3
  · rw [hd]; exact Commute.zero_left _
  · rcases lt_trichotomy k l with hkl | rfl | hkl
    · rw [hs i j]; exact key j i k l hij hkl h3 h4 h1 h2
    · rw [hd]; exact Commute.zero_right _
    · rw [hs i j, hs k l]; exact key j i l k hij hkl h4 h3 h2 h1

variable {x : Fin 5 → Fin 5 → R}

omit [Algebra ℚ R] in
/-- Relabelling by a bijection. -/
theorem P5.comp (hx : P5 x) {f : Fin 5 → Fin 5} (hf : Function.Bijective f) :
    P5 (fun i j => x (f i) (f j)) where
  symm i j := hx.symm _ _
  diag i := hx.diag _
  row i := by
    rw [hf.sum_comp (fun j => x (f i) j)]
    exact hx.row _
  far i j k l h1 h2 h3 h4 :=
    hx.far _ _ _ _ (hf.1.ne h1) (hf.1.ne h2) (hf.1.ne h3) (hf.1.ne h4)

/-- **Triangle identity.** `x₀₁ + x₀₂ + x₁₂ = x₃₄`. -/
theorem P5.tri (hx : P5 x) : x 0 1 + x 0 2 + x 1 2 = x 3 4 := by
  have r0 : x 0 1 + x 0 2 + x 0 3 + x 0 4 = 0 := by
    simpa [Fin.sum_univ_five, hx.diag] using hx.row 0
  have r1 : x 0 1 + x 1 2 + x 1 3 + x 1 4 = 0 := by
    simpa [Fin.sum_univ_five, hx.diag, hx.symm 1 0] using hx.row 1
  have r2 : x 0 2 + x 1 2 + x 2 3 + x 2 4 = 0 := by
    simpa [Fin.sum_univ_five, hx.diag, hx.symm 2 0, hx.symm 2 1] using hx.row 2
  have r3 : x 0 3 + x 1 3 + x 2 3 + x 3 4 = 0 := by
    simpa [Fin.sum_univ_five, hx.diag, hx.symm 3 0, hx.symm 3 1, hx.symm 3 2] using hx.row 3
  have r4 : x 0 4 + x 1 4 + x 2 4 + x 3 4 = 0 := by
    simpa [Fin.sum_univ_five, hx.diag, hx.symm 4 0, hx.symm 4 1, hx.symm 4 2, hx.symm 4 3]
      using hx.row 4
  have e : (2 : ℚ) • (x 0 1 + x 0 2 + x 1 2 - x 3 4) =
      (x 0 1 + x 0 2 + x 0 3 + x 0 4) + (x 0 1 + x 1 2 + x 1 3 + x 1 4) +
        (x 0 2 + x 1 2 + x 2 3 + x 2 4) - (x 0 3 + x 1 3 + x 2 3 + x 3 4) -
        (x 0 4 + x 1 4 + x 2 4 + x 3 4) := by module
  rw [r0, r1, r2, r3, r4] at e
  have e' := (smul_eq_zero.mp (e.trans (by abel))).resolve_left two_ne_zero
  exact sub_eq_zero.mp e'

/-- A relabelled triangle identity. -/
theorem P5.tri_of (hx : P5 x) {a b c d e : Fin 5} (hf : Function.Bijective ![a, b, c, d, e]) :
    x a b + x a c + x b c = x d e := by
  simpa using (hx.comp hf).tri

omit [Algebra ℚ R] in
theorem commute_of_add_eq {a s z : R} (h : a + s = z) (hz : Commute a z) : Commute a s := by
  have : s = z - a := by rw [← h]; abel
  rw [this]; exact hz.sub_right (Commute.refl a)

/-- **The first four strands form a `DK4` family.** -/
theorem P5.dk4 (hx : P5 x) : DK4 (x 0 1) (x 0 2) (x 0 3) (x 1 2) (x 1 3) (x 2 3) := by
  have T2 : x 0 1 + x 0 2 + x 1 2 = x 3 4 := hx.tri
  have T3 : x 0 1 + x 0 3 + x 1 3 = x 2 4 := hx.tri_of (by decide)
  have T1 : x 0 2 + x 0 3 + x 2 3 = x 1 4 := hx.tri_of (by decide)
  have T0 : x 1 2 + x 1 3 + x 2 3 = x 0 4 := hx.tri_of (by decide)
  have F := hx.far
  exact
  { f12_34 := F 0 1 2 3 (by decide) (by decide) (by decide) (by decide)
    f13_24 := F 0 2 1 3 (by decide) (by decide) (by decide) (by decide)
    f14_23 := F 0 3 1 2 (by decide) (by decide) (by decide) (by decide)
    n12_3 := commute_of_add_eq (by rw [← T2]; abel) (F 0 1 3 4 (by decide) (by decide) (by decide) (by decide))
    n13_2 := commute_of_add_eq (by rw [← T2]; abel) (F 0 2 3 4 (by decide) (by decide) (by decide) (by decide))
    n23_1 := commute_of_add_eq (by rw [← T2]; abel) (F 1 2 3 4 (by decide) (by decide) (by decide) (by decide))
    n12_4 := commute_of_add_eq (by rw [← T3]; abel) (F 0 1 2 4 (by decide) (by decide) (by decide) (by decide))
    n14_2 := commute_of_add_eq (by rw [← T3]; abel) (F 0 3 2 4 (by decide) (by decide) (by decide) (by decide))
    n24_1 := commute_of_add_eq (by rw [← T3]; abel) (F 1 3 2 4 (by decide) (by decide) (by decide) (by decide))
    n13_4 := commute_of_add_eq (by rw [← T1]; abel) (F 0 2 1 4 (by decide) (by decide) (by decide) (by decide))
    n14_3 := commute_of_add_eq (by rw [← T1]; abel) (F 0 3 1 4 (by decide) (by decide) (by decide) (by decide))
    n34_1 := commute_of_add_eq (by rw [← T1]; abel) (F 2 3 1 4 (by decide) (by decide) (by decide) (by decide))
    n23_4 := commute_of_add_eq (by rw [← T0]; abel) (F 1 2 0 4 (by decide) (by decide) (by decide) (by decide))
    n24_3 := commute_of_add_eq (by rw [← T0]; abel) (F 1 3 0 4 (by decide) (by decide) (by decide) (by decide))
    n34_2 := commute_of_add_eq (by rw [← T0]; abel) (F 2 3 0 4 (by decide) (by decide) (by decide) (by decide)) }

end P5

/-! ### Furusho's Lemma 5 and the permutation sum -/

section Cycles

variable {R : Type*} [Ring R] [Algebra ℚ R] {d : ℕ} {h : F2}

/-- The 2-cycle relation gives `h(u, v) = −h(v, u)` everywhere. -/
theorem eval_eq_neg_swap (hsw : h + swapPoly h = 0) (u v : R) : eval u v h = -eval v u h := by
  have := congrArg (eval u v) hsw
  rw [map_add, eval_swapPoly, map_zero] at this
  exact eq_neg_of_add_eq_zero_left this

/-- Shifting both arguments by a commuting element. -/
theorem eval_add_both (hd : 2 ≤ d) (hh : Homog d h) (hp : IsPrimitive h) {a b c : R}
    (ha : Commute c a) (hb : Commute c b) : eval (a + c) (b + c) h = eval a b h := by
  rw [eval_add_left hd hh hp ha (hb.add_right (Commute.refl c)), eval_add_right hd hh hp ha hb]

variable (h) in
/-- The linearised pentagon (5.20) at the `DK4` family of the first four strands. -/
noncomputable def piExpr (x : Fin 5 → Fin 5 → R) : R :=
  eval (x 1 2) (x 2 3) h + eval (x 0 1 + x 0 2) (x 1 3 + x 2 3) h + eval (x 0 1) (x 1 2) h -
    eval (x 0 1) (x 1 2 + x 1 3) h - eval (x 0 2 + x 1 2) (x 2 3) h

variable {x : Fin 5 → Fin 5 → R}

/-- **Furusho's Lemma 5.** At a `P5` family, the linearised pentagon is the sum of
`h(x_{ij}, x_{jk})` over the consecutive triples of the cycle `(0 1 2 3 4)`. -/
theorem piExpr_eq (hd : 2 ≤ d) (hh : Homog d h) (hp : IsPrimitive h)
    (hsw : h + swapPoly h = 0) (hx : P5 x) :
    piExpr h x = eval (x 1 2) (x 2 3) h + eval (x 3 4) (x 4 0) h + eval (x 0 1) (x 1 2) h +
      eval (x 4 0) (x 0 1) h + eval (x 2 3) (x 3 4) h := by
  have T012 : x 0 1 + x 0 2 + x 1 2 = x 3 4 := hx.tri
  have T123 : x 1 2 + x 1 3 + x 2 3 = x 0 4 := hx.tri_of (by decide)
  have F := hx.far
  have e1 : eval (x 0 1 + x 0 2) (x 1 3 + x 2 3) h = eval (x 3 4) (x 0 4) h := by
    rw [show x 0 1 + x 0 2 = x 3 4 + -x 1 2 by rw [← T012]; abel,
      show x 1 3 + x 2 3 = x 0 4 + -x 1 2 by rw [← T123]; abel]
    exact eval_add_both hd hh hp (F 1 2 3 4 (by decide) (by decide) (by decide) (by decide)).neg_left
      (F 1 2 0 4 (by decide) (by decide) (by decide) (by decide)).neg_left
  have e2 : eval (x 0 1) (x 1 2 + x 1 3) h = eval (x 0 1) (x 0 4) h := by
    rw [show x 1 2 + x 1 3 = x 0 4 + -x 2 3 by rw [← T123]; abel]
    exact eval_add_right hd hh hp
      (F 2 3 0 1 (by decide) (by decide) (by decide) (by decide)).neg_left
      (F 2 3 0 4 (by decide) (by decide) (by decide) (by decide)).neg_left
  have e3 : eval (x 0 2 + x 1 2) (x 2 3) h = eval (x 3 4) (x 2 3) h := by
    rw [show x 0 2 + x 1 2 = x 3 4 + -x 0 1 by rw [← T012]; abel]
    exact eval_add_left hd hh hp
      (F 0 1 3 4 (by decide) (by decide) (by decide) (by decide)).neg_left
      (F 0 1 2 3 (by decide) (by decide) (by decide) (by decide)).neg_left
  rw [piExpr, e1, e2, e3, eval_eq_neg_swap hsw (x 0 1) (x 0 4),
    eval_eq_neg_swap hsw (x 3 4) (x 2 3), hx.symm 4 0]
  abel

variable (h) in
/-- The hexagon polynomial `R = h(X, Y) + h(Y, −X − Y) + h(−X − Y, X)`. -/
noncomputable def rPoly : F2 :=
  h + eval (FreeAlgebra.ι ℚ 1) (-FreeAlgebra.ι ℚ 0 - FreeAlgebra.ι ℚ 1) h +
    eval (-FreeAlgebra.ι ℚ 0 - FreeAlgebra.ι ℚ 1) (FreeAlgebra.ι ℚ 0) h

theorem eval_eval (a b : R) (p q g : F2) : eval a b (eval p q g) = eval (eval a b p) (eval a b q) g :=
  eval_lift a b p q g

theorem eval_rPoly (u v : R) :
    eval u v (rPoly h) = eval u v h + eval v (-u - v) h + eval (-u - v) u h := by
  simp only [rPoly, map_add, eval_eval, map_sub, map_neg, eval_X, eval_Y]

/-- The four cycles of Furusho's permutation sum, besides `(0 1 2 3 4)`. -/
def cyc2 : Fin 5 → Fin 5 := ![4, 3, 1, 2, 0]
def cyc3 : Fin 5 → Fin 5 := ![0, 2, 3, 1, 4]
def cyc4 : Fin 5 → Fin 5 := ![3, 2, 0, 1, 4]

/-- **The permutation sum.** For a Lie element `h` of degree `≥ 2` with the 2-cycle relation
and a `P5` family `y`, the linearised pentagons over the four cycles `(0 1 2 3 4)`,
`(4 3 1 2 0)`, `(0 2 3 1 4)`, `(3 2 0 1 4)` add up to four values of the hexagon polynomial. -/
theorem rSum_eq (hd : 2 ≤ d) (hh : Homog d h) (hp : IsPrimitive h)
    (hsw : h + swapPoly h = 0) {y : Fin 5 → Fin 5 → R} (hy : P5 y) :
    piExpr h y + piExpr h (fun i j => y (cyc2 i) (cyc2 j)) +
        piExpr h (fun i j => y (cyc3 i) (cyc3 j)) + piExpr h (fun i j => y (cyc4 i) (cyc4 j)) =
      eval (y 0 1) (y 1 2) (rPoly h) + eval (y 0 1) (y 1 4) (rPoly h) +
        eval (y 1 3) (y 1 2) (rPoly h) + eval (y 1 3) (y 1 4) (rPoly h) := by
  have F := hy.far
  rw [piExpr_eq hd hh hp hsw hy,
    piExpr_eq hd hh hp hsw (hy.comp (show Function.Bijective cyc2 by decide)),
    piExpr_eq hd hh hp hsw (hy.comp (show Function.Bijective cyc3 by decide)),
    piExpr_eq hd hh hp hsw (hy.comp (show Function.Bijective cyc4 by decide))]
  simp only [cyc2, cyc3, cyc4, Matrix.cons_val]
  simp only [hy.symm 1 0, hy.symm 2 0, hy.symm 3 0, hy.symm 4 0, hy.symm 2 1, hy.symm 3 1,
    hy.symm 4 1, hy.symm 3 2, hy.symm 4 2, hy.symm 4 3]
  rw [eval_rPoly, eval_rPoly, eval_rPoly, eval_rPoly]
  have T012 : y 0 1 + y 0 2 + y 1 2 = y 3 4 := hy.tri
  have T014 : y 0 1 + y 0 4 + y 1 4 = y 2 3 := hy.tri_of (by decide)
  have T123 : y 1 2 + y 1 3 + y 2 3 = y 0 4 := hy.tri_of (by decide)
  have T134 : y 1 3 + y 1 4 + y 3 4 = y 0 2 := hy.tri_of (by decide)
  rw [show -y 0 1 - y 1 2 = y 0 2 + -y 3 4 by rw [← T012]; abel,
    show -y 0 1 - y 1 4 = y 0 4 + -y 2 3 by rw [← T014]; abel,
    show -y 1 3 - y 1 2 = y 2 3 + -y 0 4 by rw [← T123]; abel,
    show -y 1 3 - y 1 4 = y 3 4 + -y 0 2 by rw [← T134]; abel]
  rw [eval_add_right hd hh hp (F 3 4 1 2 (by decide) (by decide) (by decide) (by decide)).neg_left
      (F 3 4 0 2 (by decide) (by decide) (by decide) (by decide)).neg_left,
    eval_add_left hd hh hp (F 3 4 0 2 (by decide) (by decide) (by decide) (by decide)).neg_left
      (F 3 4 0 1 (by decide) (by decide) (by decide) (by decide)).neg_left,
    eval_add_right hd hh hp (F 2 3 1 4 (by decide) (by decide) (by decide) (by decide)).neg_left
      (F 2 3 0 4 (by decide) (by decide) (by decide) (by decide)).neg_left,
    eval_add_left hd hh hp (F 2 3 0 4 (by decide) (by decide) (by decide) (by decide)).neg_left
      (F 2 3 0 1 (by decide) (by decide) (by decide) (by decide)).neg_left,
    eval_add_right hd hh hp (F 0 4 1 2 (by decide) (by decide) (by decide) (by decide)).neg_left
      (F 0 4 2 3 (by decide) (by decide) (by decide) (by decide)).neg_left,
    eval_add_left hd hh hp (F 0 4 2 3 (by decide) (by decide) (by decide) (by decide)).neg_left
      (F 0 4 1 3 (by decide) (by decide) (by decide) (by decide)).neg_left,
    eval_add_right hd hh hp (F 0 2 1 4 (by decide) (by decide) (by decide) (by decide)).neg_left
      (F 0 2 3 4 (by decide) (by decide) (by decide) (by decide)).neg_left,
    eval_add_left hd hh hp (F 0 2 3 4 (by decide) (by decide) (by decide) (by decide)).neg_left
      (F 0 2 1 3 (by decide) (by decide) (by decide) (by decide)).neg_left]
  rw [eval_eq_neg_swap hsw (y 3 4) (y 2 3), eval_eq_neg_swap hsw (y 0 4) (y 3 4),
    eval_eq_neg_swap hsw (y 0 4) (y 0 2), eval_eq_neg_swap hsw (y 2 3) (y 0 2)]
  abel

end Cycles

end QOU.BraidsAndKnots.RationalAssociator
