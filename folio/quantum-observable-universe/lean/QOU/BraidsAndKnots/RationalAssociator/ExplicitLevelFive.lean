import QOU.BraidsAndKnots.RationalAssociator.ExplicitLevelFiveAlg

/-!
# An explicit rational associator modulo `5`, for the level-`5` exponential

Audit `docs/audits/2026-11-27-grt-action-pentagon-derivation.md` §17q.

* `assocU4_five`: with `L = [X, Y]`,
  `Φ₅ = 1 + L/24 + L²/1152 − [X,[X,L]]/1440 − [Y,[X,L]]/5760 − [Y,[Y,L]]/1440`
  is a rational associator in `U4 5` for `expHalfTrunc 5 = Σ_{k<5} X^k/(2^k k!)`.
* `GL_five`: `Φ₅` is group-like modulo `FF2 5` (its degree-`4` part is `(L/24)²/2` plus a
  Lie element).
* `exists_assoc_GL_five`: `∃ Φ, AssocU4 5 (expHalfTrunc 5) Φ ∧ GL 5 Φ`.

The degree-`4` coefficients are not chosen: the degree-`4` linear system for `φ + x`, `x`
homogeneous of degree `4` in the `16` words, has exactly one solution over `ℚ`, and the
degree-`3` system is solved by `α·([X,[X,Y]] + [Y,[X,Y]])` for every `α` (`α = 0` here). Both
were solved in exact `Fraction` arithmetic by
`computations/audits/rational_associator_level4_probe.py`; the Lean proof does not use it.
(For comparison only, not used: `1/1440 = ζ(4)/(2π)⁴`, the KZ value; nothing analytic enters.)

Method. In `U4 5` every product of five elements of `Fil 1` vanishes (`trunc5_fil`). Eleven
Drinfeld–Kohno consequences, each read off one relation of `DK4`, form a rewriting system
pushing `t₁₂, t₁₃, t₂₃` to the right of `t₁₄, t₂₄, t₃₄`, and `t₂₃` to the right of `t₁₂, t₁₃`;
its normal words are those of the PBW basis `U(𝔣₃) ⊗ U(𝔣₂) ⊗ U(𝔣₁)`. `hexagon5` and `pentagon5`
expand, truncate, rewrite to normal form and compare coefficients (`module`), in any
`ℚ`-algebra satisfying the rewriting rules.

No `axiom`, no `sorry`, no analysis.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

open TensorProduct Friedrichs

local notation "F2" => FreeAlgebra ℚ (Fin 2)


/-! ### The polynomial and its evaluation -/

/-- `[X, Y]`. -/
noncomputable abbrev LXY : F2 :=
  FreeAlgebra.ι ℚ 0 * FreeAlgebra.ι ℚ 1 - FreeAlgebra.ι ℚ 1 * FreeAlgebra.ι ℚ 0

/-- The commutator in `ℚ⟨X, Y⟩`. -/
noncomputable def brF (p q : F2) : F2 := p * q - q * p

/-- The degree-`4` part of `Φ₅`. -/
noncomputable def phi5Deg4 : F2 :=
  (1 / 1152 : ℚ) • (LXY * LXY)
    - (1 / 1440 : ℚ) • brF (FreeAlgebra.ι ℚ 0) (brF (FreeAlgebra.ι ℚ 0) LXY)
    - (1 / 5760 : ℚ) • brF (FreeAlgebra.ι ℚ 1) (brF (FreeAlgebra.ι ℚ 0) LXY)
    - (1 / 1440 : ℚ) • brF (FreeAlgebra.ι ℚ 1) (brF (FreeAlgebra.ι ℚ 1) LXY)

/-- `Φ₅ = 1 + [X, Y]/24 + (degree 4)`. -/
noncomputable def phi5Poly : F2 := phiPoly (1 / 24) + phi5Deg4

theorem eval_phi5Poly {R : Type*} [Ring R] [Algebra ℚ R] (a b : R) :
    eval a b phi5Poly = phi5 a b := by
  simp only [phi5Poly, phi5Deg4, phiPoly, brF, phi5, u2, q4, brk, map_add, map_sub, map_mul,
    map_smul, map_one, eval_X, eval_Y]

theorem phi5Deg4_mem_FF : phi5Deg4 ∈ FF 4 := by
  have hL : LXY ∈ FF 2 := commutator_mem_FF2
  have hb : ∀ {p q : F2} {i j c : ℕ}, i + j = c → p ∈ FF i → q ∈ FF j → brF p q ∈ FF c :=
    fun h hp hq => sub_mem (mul_mem_FF' h hp hq) (mul_mem_FF' ((add_comm _ _).trans h) hq hp)
  have h3 : ∀ i : Fin 2, brF (FreeAlgebra.ι ℚ i) LXY ∈ FF 3 := fun i =>
    hb (i := 1) (j := 2) (c := 3) rfl (ι_mem_FF_one i) hL
  have h4 : ∀ i k : Fin 2, brF (FreeAlgebra.ι ℚ k) (brF (FreeAlgebra.ι ℚ i) LXY) ∈ FF 4 :=
    fun i k => hb (i := 1) (j := 3) (c := 4) rfl (ι_mem_FF_one k) (h3 i)
  unfold phi5Deg4
  refine sub_mem (sub_mem (sub_mem ?_ ?_) ?_) ?_
  · exact Submodule.smul_mem _ _ (mul_mem_FF' (a := 2) (b := 2) (c := 4) rfl hL hL)
  · exact Submodule.smul_mem _ _ (h4 0 0)
  · exact Submodule.smul_mem _ _ (h4 0 1)
  · exact Submodule.smul_mem _ _ (h4 1 1)

theorem eval_phi5Deg4 {R : Type*} [Ring R] [Algebra ℚ R] (a b : R) :
    eval a b phi5Deg4 = q4 a b := by
  simp only [phi5Deg4, brF, q4, brk, map_sub, map_mul, map_smul, eval_X, eval_Y]

/-! ### In `U4 5` -/

theorem trunc5_fil {S : Set (U4 5)} (hS : ∀ w ∈ S, w ∈ Fil 5 1) : Trunc5 S :=
  fun hx hy hz hw hv => eq_zero_of_mem_Fil (mul_mem_Fil' (a := 1) (b := 4) (c := 5) rfl
    (hS _ hx) (mul_mem_Fil' (a := 1) (b := 3) (c := 4) rfl (hS _ hy)
      (mul_mem_Fil' (a := 1) (b := 2) (c := 3) rfl (hS _ hz)
        (mul_mem_Fil' (a := 1) (b := 1) (c := 2) rfl (hS _ hw) (hS _ hv)))))

theorem eval_expHalfTrunc_five {R : Type*} [Ring R] [Algebra ℚ R] (x : R) :
    eval x 0 (expHalfTrunc 5) = expHalf5 x := by
  simp only [expHalfTrunc, Finset.sum_range_succ, Finset.sum_range_zero, zero_add, map_add,
    map_smul, map_pow, eval_X, expHalf5]
  norm_num [Nat.factorial, pow_succ, mul_assoc]

theorem inv512_five : Inv512 (Fil 5 1) phi5Poly := fun a b ha hb => by
  rw [eval_phi5Poly, eval_phi5Poly]
  refine inversion5 (trunc5_fil ?_)
  intro w hw; rcases hw with rfl | rfl <;> assumption

theorem hexagon_five : Hexagon phi5Poly (expHalfTrunc 5) (t 5 0) (t 5 1) (t 5 3) := by
  have dk := dk4 5
  have c1 : Commute (t 5 0) (t 5 3 + t 5 1) := by rw [add_comm]; exact dk.n12_3
  have c2 : Commute (t 5 1) (t 5 3 + t 5 0) := by rw [add_comm]; exact dk.n13_2
  unfold Hexagon
  simp only [eval_phi5Poly, eval_expHalfTrunc_five]
  refine hexagon5 (trunc5_fil ?_) (rule_of_commute_w c1) (rule_of_commute_w c2)
    (rule_of_commute c1) (rule_of_commute c2)
  intro w hw; rcases hw with rfl | rfl | rfl <;> exact t_mem_Fil_one _

/-- Expanding a product of three truncated factors (abstract). -/
theorem mul_three_of {R : Type*} [Ring R] {P Q P' Q' S T : R} (k1 : P * T = 0)
    (k2 : Q * S = 0) (k3 : Q * T = 0) (k4 : P' * T = 0) (k5 : Q' * S = 0) (k6 : Q' * T = 0)
    (k7 : P * P' * S = 0) (k8 : P * P' * T = 0) :
    (1 + (P + Q) + (P' + Q') + P * P') * (1 + S + T) =
      1 + (P + Q) + (P' + Q') + (S + T) + P * P' + P * S + P' * S := by
  simp only [mul_add, add_mul, one_mul, mul_one, k1, k2, k3, k4, k5, k6, k7, k8, add_zero]
  abel

theorem glue5 {R : Type*} [Ring R] {x1 x2 x3 y1 y2 y3 y4 y5 y6 : R}
    (h : x1 + x2 + x3 = y1 + y2 + y3 + y4 + y5 + y6) :
    1 + x1 + x2 + x3 = 1 + y1 + y2 + y3 + y4 + y5 + y6 := by
  simp only [add_assoc] at h ⊢; rw [h]

theorem u2_mem_Fil5 {a b : U4 5} (ha : a ∈ Fil 5 1) (hb : b ∈ Fil 5 1) :
    u2 a b ∈ Fil 5 2 := by
  have h : a * b - b * a ∈ Fil 5 2 :=
    sub_mem (mul_mem_Fil' (a := 1) (b := 1) (c := 2) rfl ha hb)
      (mul_mem_Fil' (a := 1) (b := 1) (c := 2) rfl hb ha)
  exact Submodule.smul_mem (Fil 5 2) (1 / 24 : ℚ) h

theorem q4_mem_Fil5 {a b : U4 5} (ha : a ∈ Fil 5 1) (hb : b ∈ Fil 5 1) :
    q4 a b ∈ Fil 5 4 := by
  have := eval_mem_Fil ha hb phi5Deg4_mem_FF
  rwa [eval_phi5Deg4] at this

theorem mul_eq_zero_Fil5 {i j : ℕ} (hij : 5 ≤ i + j) {x y : U4 5}
    (hx : x ∈ Fil 5 i) (hy : y ∈ Fil 5 j) : x * y = 0 := by
  have h : x * y ∈ Fil 5 (i + j) := mul_mem_Fil' (a := i) (b := j) (c := i + j) rfl hx hy
  exact eq_zero_of_mem_Fil (N := 5) (SetLike.le_def.mp (Fil_anti (N := 5) hij) h)

theorem pentagon_five : Pentagon phi5Poly (t 5 0) (t 5 1) (t 5 3) (t 5 4) (t 5 5) := by
  have dk := dk4 5
  have c1 : Commute (t 5 0) (t 5 3 + t 5 1) := by rw [add_comm]; exact dk.n12_3
  have c2 : Commute (t 5 1) (t 5 3 + t 5 0) := by rw [add_comm]; exact dk.n13_2
  have a1 : t 5 0 ∈ Fil 5 1 := t_mem_Fil_one _
  have b1 : t 5 3 + t 5 4 ∈ Fil 5 1 := add_mem (t_mem_Fil_one _) (t_mem_Fil_one _)
  have a2 : t 5 1 + t 5 3 ∈ Fil 5 1 := add_mem (t_mem_Fil_one _) (t_mem_Fil_one _)
  have b2 : t 5 5 ∈ Fil 5 1 := t_mem_Fil_one _
  have a3 : t 5 3 ∈ Fil 5 1 := t_mem_Fil_one _
  have a4 : t 5 0 + t 5 1 ∈ Fil 5 1 := add_mem (t_mem_Fil_one _) (t_mem_Fil_one _)
  have b4 : t 5 4 + t 5 5 ∈ Fil 5 1 := add_mem (t_mem_Fil_one _) (t_mem_Fil_one _)
  unfold Pentagon
  simp only [eval_phi5Poly, phi5]
  rw [mul_two_of
    (mul_eq_zero_Fil5 (i := 2) (j := 4) (by norm_num) (u2_mem_Fil5 a1 b1) (q4_mem_Fil5 a2 b2))
    (mul_eq_zero_Fil5 (i := 4) (j := 2) (by norm_num) (q4_mem_Fil5 a1 b1) (u2_mem_Fil5 a2 b2))
    (mul_eq_zero_Fil5 (i := 4) (j := 4) (by norm_num) (q4_mem_Fil5 a1 b1) (q4_mem_Fil5 a2 b2))]
  rw [mul_two_of
    (mul_eq_zero_Fil5 (i := 2) (j := 4) (by norm_num) (u2_mem_Fil5 a3 b2) (q4_mem_Fil5 a4 b4))
    (mul_eq_zero_Fil5 (i := 4) (j := 2) (by norm_num) (q4_mem_Fil5 a3 b2) (u2_mem_Fil5 a4 b4))
    (mul_eq_zero_Fil5 (i := 4) (j := 4) (by norm_num) (q4_mem_Fil5 a3 b2) (q4_mem_Fil5 a4 b4))]
  have hPP : u2 (t 5 3) (t 5 5) * u2 (t 5 0 + t 5 1) (t 5 4 + t 5 5) ∈ Fil 5 4 :=
    mul_mem_Fil' (a := 2) (b := 2) (c := 4) rfl (u2_mem_Fil5 a3 b2) (u2_mem_Fil5 a4 b4)
  rw [mul_three_of
    (mul_eq_zero_Fil5 (i := 2) (j := 4) (by norm_num) (u2_mem_Fil5 a3 b2) (q4_mem_Fil5 a1 a3))
    (mul_eq_zero_Fil5 (i := 4) (j := 2) (by norm_num) (q4_mem_Fil5 a3 b2) (u2_mem_Fil5 a1 a3))
    (mul_eq_zero_Fil5 (i := 4) (j := 4) (by norm_num) (q4_mem_Fil5 a3 b2) (q4_mem_Fil5 a1 a3))
    (mul_eq_zero_Fil5 (i := 2) (j := 4) (by norm_num) (u2_mem_Fil5 a4 b4) (q4_mem_Fil5 a1 a3))
    (mul_eq_zero_Fil5 (i := 4) (j := 2) (by norm_num) (q4_mem_Fil5 a4 b4) (u2_mem_Fil5 a1 a3))
    (mul_eq_zero_Fil5 (i := 4) (j := 4) (by norm_num) (q4_mem_Fil5 a4 b4) (q4_mem_Fil5 a1 a3))
    (mul_eq_zero_Fil5 (i := 4) (j := 2) (by norm_num) hPP (u2_mem_Fil5 a1 a3))
    (mul_eq_zero_Fil5 (i := 4) (j := 4) (by norm_num) hPP (q4_mem_Fil5 a1 a3))]
  have key := pentagon5_lin (t14 := t 5 2)
    (rule_of_commute_w dk.n14_2) (rule_of_commute dk.n14_2)
    (rule_of_commute_w dk.n24_1) (rule_of_commute dk.n24_1)
    (rule_of_commute' dk.f12_34.symm) dk.f12_34.eq
    (rule_of_commute_w dk.n14_3) (rule_of_commute dk.n14_3)
    (rule_of_commute_w dk.n34_1) (rule_of_commute dk.n34_1)
    (rule_of_commute' dk.f13_24.symm) dk.f13_24.eq
    (rule_of_commute' dk.f14_23) dk.f14_23.symm.eq
    (rule_of_commute_w dk.n24_3) (rule_of_commute dk.n24_3)
    (rule_of_commute_w dk.n34_2) (rule_of_commute dk.n34_2)
    (rule_of_commute_w c1) (rule_of_commute c1)
    (rule_of_commute_w c2) (rule_of_commute c2)
  exact glue5 key


/-- **A rational associator modulo `5`** for the level-`5` exponential. -/
theorem assocU4_five : AssocU4 5 (expHalfTrunc 5) phi5Poly where
  const := by
    rw [phi5Poly, map_add, assocU4_four.const,
      algebraMapInv_eq_zero_of_mem_FF (by norm_num) phi5Deg4_mem_FF, add_zero]
  inv := inv512_five
  hex := hexagon_five
  pent := pentagon_five

/-! ### Group-likeness -/

theorem brF_isPrimitive {p q : F2} (hp : IsPrimitive p) (hq : IsPrimitive q) :
    IsPrimitive (brF p q) := IsPrimitive.commutator hp hq

/-- **`Φ₅` is group-like modulo `FF2 5`.** -/
theorem GL_five : GL 5 phi5Poly := by
  have hΦ : phiPoly (1 / 24) - 1 ∈ FF 1 := by
    rw [show phiPoly (1 / 24) - 1 = (1 / 24 : ℚ) • LXY by simp [phiPoly]]
    exact Submodule.smul_mem _ _ (FF_anti (by norm_num) commutator_mem_FF2)
  rw [phi5Poly, GL_add_iff (d := 4) (by norm_num) hΦ phi5Deg4_mem_FF]
  have hp : cop LXY = LXY ⊗ₜ 1 + 1 ⊗ₜ LXY := isPrimitive_commXY
  have hX := isPrimitive_ι 0
  have hY := isPrimitive_ι 1
  have hLp : IsPrimitive LXY := isPrimitive_commXY
  have p1 := (isPrimitive_iff _).1 (brF_isPrimitive hX (brF_isPrimitive hX hLp))
  have p2 := (isPrimitive_iff _).1 (brF_isPrimitive hY (brF_isPrimitive hX hLp))
  have p3 := (isPrimitive_iff _).1 (brF_isPrimitive hY (brF_isPrimitive hY hLp))
  have e : glDefect (phiPoly (1 / 24)) + primDef phi5Deg4 = 0 := by
    rw [phi5Deg4, map_sub, map_sub, map_sub, map_smul, map_smul, map_smul, map_smul, p1, p2, p3,
      primDef_apply, glDefect, show phiPoly (1 / 24) = 1 + (1 / 24 : ℚ) • LXY from rfl]
    rw [map_add, map_one, map_smul, map_mul, hp]
    simp only [add_tmul, tmul_add, ← smul_tmul', tmul_smul, smul_add, smul_smul, mul_add, add_mul,
      Algebra.TensorProduct.tmul_mul_tmul, one_mul, mul_one, Algebra.TensorProduct.one_def,
      smul_zero, sub_zero]
    module
  rw [e]; exact zero_mem _

/-- **Level `5`, unconditionally**: a rational associator modulo `5` for `expHalfTrunc 5`,
group-like modulo `FF2 5`. -/
theorem exists_assoc_GL_five : ∃ Φ : F2, AssocU4 5 (expHalfTrunc 5) Φ ∧ GL 5 Φ :=
  ⟨phi5Poly, assocU4_five, GL_five⟩

end QOU.BraidsAndKnots.RationalAssociator
