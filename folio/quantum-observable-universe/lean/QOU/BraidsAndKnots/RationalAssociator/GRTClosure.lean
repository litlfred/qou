import QOU.BraidsAndKnots.RationalAssociator.HexagonUniversal

/-!
# Drinfeld's (5.12) and (5.14) are preserved by the group law (5.16)

Bean `qou-3fdg` (stage-4 blocker, epic `qou-dk7p`). Drinfeld's numbering (1991, §5): (5.12)
`g(B,A) = g(A,B)⁻¹`, (5.14) `TCompat`.

Everything is stated at the level of evaluations in a `ℚ`-algebra `R` with a two-sided ideal `S`
(a `NilIdeal`, e.g. `Fil N 1` in `U4 N`), and with every condition quantified over `S`:

* `Inv512 S g`: `g(a,b) g(b,a) = 1` for all `a, b ∈ S`.
* `TCompatPoly g u v w`: `g(v,w) v g(w,v) = g(u,w) (v+w) g(w,u) − w`, which is `TCompat` with
  the inverses written through (5.12) (`tcompat_iff_poly`).
* `TComp514 S g`: `TCompatPoly g u v w` for every `DK3` family `(u,v,w)` in `S`.
* `compEval g₁ g₂ a b = g₁(G a G', b) · G` with `G = g₂(a,b)`, `G' = g₂(b,a)`: the value at
  `(a,b)` of `g₁ ∘ g₂` under (5.16); it equals `actEval g₁ a b G` when `G` is a unit with inverse
  `G'` (`compEval_eq_actEval`).

Main results: `comp_inv512` (closure of (5.12)) and `comp_tcompat` (closure of (5.14)). Nothing
analytic is used.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

section Closure

variable {R : Type*} [Ring R] [Algebra ℚ R]

/-- Drinfeld's (5.12) on all pairs from `S`. -/
def Inv512 (S : Submodule ℚ R) (g : FreeAlgebra ℚ (Fin 2)) : Prop :=
  ∀ a b : R, a ∈ S → b ∈ S → eval a b g * eval b a g = 1

/-- Drinfeld's (5.14) at `(u,v,w) = (t_ab, t_ac, t_bc)`, inverses written through (5.12). -/
def TCompatPoly (g : FreeAlgebra ℚ (Fin 2)) (u v w : R) : Prop :=
  eval v w g * v * eval w v g = eval u w g * (v + w) * eval w u g - w

/-- Drinfeld's (5.14) at every `DK3` family in `S`. -/
def TComp514 (S : Submodule ℚ R) (g : FreeAlgebra ℚ (Fin 2)) : Prop :=
  ∀ u v w : R, u ∈ S → v ∈ S → w ∈ S → DK3 u v w → TCompatPoly g u v w

/-- The value at `(a, b)` of `g₁ ∘ g₂` under (5.16). -/
noncomputable def compEval (g1 g2 : FreeAlgebra ℚ (Fin 2)) (a b : R) : R :=
  eval (eval a b g2 * a * eval b a g2) b g1 * eval a b g2

/-- Conjugation by a two-sided inverse pair passes through evaluation. -/
theorem eval_conj' {G G' : R} (h : G * G' = 1) (h' : G' * G = 1) (x y : R)
    (p : FreeAlgebra ℚ (Fin 2)) : eval (G * x * G') (G * y * G') p = G * eval x y p * G' := by
  have := eval_conj (⟨G', G, h', h⟩ : Rˣ) x y p
  simpa using this

/-- With (5.12), `TCompat` (unit form) is `TCompatPoly`. -/
theorem tcompat_iff_poly (g : FreeAlgebra ℚ (Fin 2)) {u v w : R} (Guw Gvw : Rˣ)
    (huw : (Guw : R) = eval u w g) (hvw : (Gvw : R) = eval v w g)
    (iuw : eval u w g * eval w u g = 1) (ivw : eval v w g * eval w v g = 1) :
    TCompat v w Guw Gvw ↔ TCompatPoly g u v w := by
  have e1 : (↑Guw⁻¹ : R) = eval w u g := by
    rw [← mul_one (↑Guw⁻¹ : R), ← iuw, ← huw, ← mul_assoc, Units.inv_mul, one_mul]
  have e2 : (↑Gvw⁻¹ : R) = eval w v g := by
    rw [← mul_one (↑Gvw⁻¹ : R), ← ivw, ← hvw, ← mul_assoc, Units.inv_mul, one_mul]
  unfold TCompat TCompatPoly
  rw [e1, e2, huw, hvw]

/-- `compEval` is `actEval` when `g₂(a,b)` is a unit with inverse `g₂(b,a)`. -/
theorem compEval_eq_actEval (g1 g2 : FreeAlgebra ℚ (Fin 2)) {a b : R} (G : Rˣ)
    (hG : (G : R) = eval a b g2) (hi : eval a b g2 * eval b a g2 = 1) :
    compEval g1 g2 a b = actEval g1 a b G := by
  have e : (↑G⁻¹ : R) = eval b a g2 := by
    rw [← mul_one (↑G⁻¹ : R), ← hi, ← hG, ← mul_assoc, Units.inv_mul, one_mul]
  simp only [compEval, actEval, e, hG]

variable {S : Submodule ℚ R}

/-- **(5.12) is preserved by (5.16).** -/
theorem comp_inv512 (hS : NilIdeal S) {g1 g2 : FreeAlgebra ℚ (Fin 2)} (h1 : Inv512 S g1)
    (h2 : Inv512 S g2) {a b : R} (ha : a ∈ S) (hb : b ∈ S) :
    compEval g1 g2 a b * compEval g1 g2 b a = 1 := by
  set G := eval a b g2
  set G' := eval b a g2
  have hGG : G * G' = 1 := h2 a b ha hb
  have hGG' : G' * G = 1 := h2 b a hb ha
  have hx : G * a * G' ∈ S := hS.mul_right _ (hS.mul_left _ ha)
  have key : G * eval (G' * b * G) a g1 * G' = eval b (G * a * G') g1 := by
    have hb' : G * (G' * b * G) * G' = b := by
      calc G * (G' * b * G) * G' = (G * G') * b * (G * G') := by noncomm_ring
        _ = b := by rw [hGG]; simp
    rw [← eval_conj' hGG hGG', hb']
  calc compEval g1 g2 a b * compEval g1 g2 b a
      = eval (G * a * G') b g1 * (G * eval (G' * b * G) a g1 * G') := by
        simp only [compEval, G, G']; noncomm_ring
    _ = 1 := by rw [key]; exact h1 _ _ hx hb

omit [Algebra ℚ R] in
/-- `DK3` from commutation with the total. -/
theorem dk3_of_total {u v w : R} (hu : Commute u (u + v + w)) (hv : Commute v (u + v + w))
    (hw : Commute w (u + v + w)) : DK3 u v w := by
  refine ⟨?_, ?_, ?_⟩
  · have := hu.sub_right (Commute.refl u)
    rwa [show u + v + w - u = v + w by abel] at this
  · have := hv.sub_right (Commute.refl v)
    rwa [show u + v + w - v = u + w by abel] at this
  · have := hw.sub_right (Commute.refl w)
    rwa [show u + v + w - w = u + v by abel] at this

/-- `g(x, y) · x · g(y, x)` for the composite, rewritten through `g₁` at the transported pair. -/
theorem compEval_conj (g1 g2 : FreeAlgebra ℚ (Fin 2)) {x y z : R}
    (hi : eval x y g2 * eval y x g2 = 1) (hi' : eval y x g2 * eval x y g2 = 1) :
    compEval g1 g2 x y * z * compEval g1 g2 y x =
      eval (eval x y g2 * x * eval y x g2) y g1 * (eval x y g2 * z * eval y x g2) *
        eval y (eval x y g2 * x * eval y x g2) g1 := by
  set G := eval x y g2
  set G' := eval y x g2
  have key : G * eval (G' * y * G) x g1 * G' = eval y (G * x * G') g1 := by
    have hb' : G * (G' * y * G) * G' = y := by
      calc G * (G' * y * G) * G' = (G * G') * y * (G * G') := by noncomm_ring
        _ = y := by rw [hi]; simp
    rw [← eval_conj' hi hi', hb']
  calc compEval g1 g2 x y * z * compEval g1 g2 y x
      = eval (G * x * G') y g1 * (G * z * G') * (G * eval (G' * y * G) x g1 * G') := by
        have e : eval (G * x * G') y g1 * (G * z * G') * (G * eval (G' * y * G) x g1 * G') =
            eval (G * x * G') y g1 * G * z * (G' * G) * eval (G' * y * G) x g1 * G' := by
          noncomm_ring
        rw [e, hi', mul_one]
        simp only [compEval, G, G']
        noncomm_ring
    _ = _ := by rw [key]

/-- **(5.14) is preserved by (5.16).** If `g₁` and `g₂` satisfy (5.12) on `S` and (5.14) at
every `DK3` family in `S`, so does `g₁ ∘ g₂` (at the level of evaluations). -/
theorem comp_tcompat (hS : NilIdeal S) {g1 g2 : FreeAlgebra ℚ (Fin 2)}
    (i2 : Inv512 S g2) (c1 : TComp514 S g1) (c2 : TComp514 S g2) {u v w : R} (hu : u ∈ S)
    (hv : v ∈ S) (hw : w ∈ S) (hDK : DK3 u v w) :
    compEval g1 g2 v w * v * compEval g1 g2 w v =
      compEval g1 g2 u w * (v + w) * compEval g1 g2 w u - w := by
  rw [compEval_conj g1 g2 (i2 v w hv hw) (i2 w v hw hv),
    compEval_conj g1 g2 (i2 u w hu hw) (i2 w u hw hu)]
  set Gu := eval u w g2
  set Gu' := eval w u g2
  set Gv := eval v w g2
  set Gv' := eval w v g2
  set u' := Gu * u * Gu'
  set v' := Gv * v * Gv'
  -- g₂'s (5.14): v' = Gu (v+w) Gu' − w
  have t2 : v' = Gu * (v + w) * Gu' - w := c2 u v w hu hv hw hDK
  have hvw : Gu * (v + w) * Gu' = v' + w := by rw [t2]; abel
  -- the total is central for the family and fixed by `Gu`
  set c := u + v + w with hc
  have cu : Commute u c := by
    rw [hc, add_assoc]; exact (Commute.refl u).add_right hDK.n12_3
  have cv : Commute v c := by
    rw [hc, show u + v + w = v + (u + w) by abel]; exact (Commute.refl v).add_right hDK.n13_2
  have cw : Commute w c := hDK.n23_1.add_right (Commute.refl w)
  have cGu : Commute Gu c := commute_eval cu cw g2
  have cGu' : Commute Gu' c := commute_eval cw cu g2
  have cGv : Commute Gv c := commute_eval cv cw g2
  have cGv' : Commute Gv' c := commute_eval cw cv g2
  have hcu : Gu * c * Gu' = c := by
    rw [cGu.eq, mul_assoc, i2 u w hu hw, mul_one]
  have hu' : u' = c - (v' + w) := by
    rw [← hvw, ← hcu]
    simp only [u', hc]; noncomm_ring
  have cu' : Commute u' c := (cGu.mul_left cu).mul_left cGu'
  have cv' : Commute v' c := (cGv.mul_left cv).mul_left cGv'
  have htot : u' + v' + w = c := by rw [hu']; abel
  have dk' : DK3 u' v' w := by
    apply dk3_of_total <;> rw [htot]
    · exact cu'
    · exact cv'
    · exact cw
  have hu'S : u' ∈ S := hS.mul_right _ (hS.mul_left _ hu)
  have hv'S : v' ∈ S := hS.mul_right _ (hS.mul_left _ hv)
  have t1 := c1 u' v' w hu'S hv'S hw dk'
  unfold TCompatPoly at t1
  rw [hvw]
  exact t1

end Closure

end QOU.BraidsAndKnots.RationalAssociator
