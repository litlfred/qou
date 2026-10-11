import Mathlib.Analysis.ODE.PicardLindelof
import Mathlib.Analysis.ODE.Gronwall
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Analysis.Normed.Operator.Mul

/-!
# Linear ODEs `U' = X U` in a Banach algebra on `[0,1]`

Let `A` be a complete normed `ℝ`-algebra and `X : ℝ → A` continuous on `[0,1]`.
We prove that the linear initial value problem `U' = X U`, `U 0 = 1`, has a
(unique) solution on `[0,1]` — the *fundamental solution* or path-ordered
exponential of `X` — and that its values are units of `A`.

The argument is carried out first for a general linear field `W' = B t (W t)`
with `B : ℝ → (E →L[ℝ] E)` continuous on `[0,1]` in a Banach space `E`:

* **Uniqueness** follows from Grönwall's inequality
  (`ODE_solution_unique_of_mem_Icc_right`), since `B t` is `‖B t‖`-Lipschitz and
  `‖B t‖` is bounded on the compact interval.
* **Existence** is global: Picard–Lindelöf gives a solution on any subinterval
  `[s, s']` of length `≤ 1/(2C)` (where `‖B t‖ ≤ C`) from *any* initial value,
  because the field is linear (take the ball radius `‖x₀‖ + 1`).  Gluing finitely
  many such pieces covers `[0,1]`.

Specialising `B t = X t * ·` gives the fundamental solution.  Invertibility:
the solution `L` of `L' = -(L X)`, `L 0 = 1` (again a linear field, by right
multiplication) satisfies `(L U)' = 0`, so `L U = 1`; and `Z = U L` solves
`Z' = X Z - Z X` with `Z 0 = 1`, as does the constant `1`, so `U L = 1`.
-/

open Set NNReal

namespace QOU.Mass.KZHolonomy

section General

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E]

omit [CompleteSpace E] in
/-- Restrict a derivative within `Icc 0 1` to a derivative within `Ici t` for `t ∈ Ico 0 1`. -/
lemma hasDerivWithinAt_Ici_of_Icc {f : ℝ → E} {f' : E} {t : ℝ} (ht : t ∈ Ico (0:ℝ) 1)
    (h : HasDerivWithinAt f f' (Icc 0 1) t) : HasDerivWithinAt f f' (Ici t) t := by
  have hmem : Icc (0:ℝ) 1 ∈ nhdsWithin t (Ici t) :=
    Filter.mem_of_superset (Icc_mem_nhdsGE ht.2) (Icc_subset_Icc_left ht.1)
  exact (hasDerivWithinAt_inter' hmem).1 (h.mono inter_subset_right)

omit [CompleteSpace E] in
/-- Uniqueness for a linear ODE `W' = B t (W t)` on `[0,1]`. -/
theorem clm_eqOn_of_hasDerivWithinAt {B : ℝ → E →L[ℝ] E} (hB : ContinuousOn B (Icc 0 1))
    {W W' : ℝ → E}
    (hW : ∀ t ∈ Icc (0:ℝ) 1, HasDerivWithinAt W (B t (W t)) (Icc 0 1) t)
    (hW' : ∀ t ∈ Icc (0:ℝ) 1, HasDerivWithinAt W' (B t (W' t)) (Icc 0 1) t)
    (h0 : W 0 = W' 0) : EqOn W W' (Icc 0 1) := by
  obtain ⟨C, hC⟩ := (isCompact_Icc (a := (0:ℝ)) (b := 1)).exists_bound_of_continuousOn hB
  have hlip : ∀ t ∈ Ico (0:ℝ) 1,
      LipschitzOnWith C.toNNReal (fun x => B t x) (univ : Set E) := by
    intro t ht
    refine (LipschitzWith.of_dist_le_mul fun x y => ?_).lipschitzOnWith
    rw [dist_eq_norm, dist_eq_norm, ← map_sub]
    refine ((B t).le_opNorm _).trans ?_
    gcongr
    exact (hC t (Ico_subset_Icc_self ht)).trans (Real.le_coe_toNNReal C)
  exact ODE_solution_unique_of_mem_Icc_right (v := fun t x => B t x) (s := fun _ => univ) hlip
    (fun t ht => (hW t ht).continuousWithinAt)
    (fun t ht => hasDerivWithinAt_Ici_of_Icc ht (hW t (Ico_subset_Icc_self ht)))
    (fun _ _ => trivial)
    (fun t ht => (hW' t ht).continuousWithinAt)
    (fun t ht => hasDerivWithinAt_Ici_of_Icc ht (hW' t (Ico_subset_Icc_self ht)))
    (fun _ _ => trivial) h0

/-- Local existence for a linear ODE from any initial value, on an interval of length
`≤ 1/(2C)`. -/
lemma clm_local_exists {B : ℝ → E →L[ℝ] E} (hB : ContinuousOn B (Icc 0 1)) {C : ℝ≥0}
    (hC : ∀ t ∈ Icc (0:ℝ) 1, ‖B t‖ ≤ C) {s s' : ℝ} (hs : 0 ≤ s) (hss' : s ≤ s')
    (hs' : s' ≤ 1) (hlen : 2 * (C:ℝ) * (s' - s) ≤ 1) (x₀ : E) :
    ∃ φ : ℝ → E, φ s = x₀ ∧
      ∀ t ∈ Icc s s', HasDerivWithinAt φ (B t (φ t)) (Icc s s') t := by
  have hsub : Icc s s' ⊆ Icc (0:ℝ) 1 := Icc_subset_Icc hs hs'
  have hPL : IsPicardLindelof (fun t x => B t x) (⟨s, left_mem_Icc.2 hss'⟩ : Icc s s') x₀
      (‖x₀‖₊ + 1) 0 (C * (2 * ‖x₀‖₊ + 1)) C := by
    refine ⟨fun t ht => ?_, fun x _ => ?_, fun t ht x hx => ?_, ?_⟩
    · refine (LipschitzWith.of_dist_le_mul fun x y => ?_).lipschitzOnWith
      rw [dist_eq_norm, dist_eq_norm, ← map_sub]
      refine ((B t).le_opNorm _).trans ?_
      gcongr
      exact hC t (hsub ht)
    · exact (hB.mono hsub).clm_apply continuousOn_const
    · have hx' : ‖x‖ ≤ 2 * ‖x₀‖ + 1 := by
        have h1 : ‖x - x₀‖ ≤ ‖x₀‖ + 1 := by
          simpa [Metric.mem_closedBall, dist_eq_norm] using hx
        have h2 := norm_le_insert' x x₀
        linarith
      have hBt := hC t (hsub ht)
      calc ‖B t x‖ ≤ ‖B t‖ * ‖x‖ := (B t).le_opNorm x
        _ ≤ C * (2 * ‖x₀‖ + 1) := by gcongr
        _ = _ := by push_cast; ring
    · simp only [NNReal.coe_mul, NNReal.coe_add, NNReal.coe_ofNat, NNReal.coe_one, coe_nnnorm,
        sub_self, NNReal.coe_zero, sub_zero]
      have hmax : max (s' - s) 0 = s' - s := max_eq_left (by linarith)
      rw [hmax]
      have hC0 : (0:ℝ) ≤ C := C.2
      have hn : 0 ≤ ‖x₀‖ := norm_nonneg _
      have hd : 0 ≤ s' - s := by linarith
      have : 0 ≤ (C:ℝ) * (s' - s) := mul_nonneg hC0 hd
      nlinarith
  obtain ⟨φ, hφ0, hφ⟩ := hPL.exists_eq_forall_mem_Icc_hasDerivWithinAt₀
  exact ⟨φ, hφ0, hφ⟩

/-- Global existence on `[0,1]` for a linear ODE with continuous coefficients. -/
theorem clm_exists {B : ℝ → E →L[ℝ] E} (hB : ContinuousOn B (Icc 0 1)) (x₀ : E) :
    ∃ W : ℝ → E, W 0 = x₀ ∧
      ∀ t ∈ Icc (0:ℝ) 1, HasDerivWithinAt W (B t (W t)) (Icc 0 1) t := by
  obtain ⟨C₀, hC₀⟩ := (isCompact_Icc (a := (0:ℝ)) (b := 1)).exists_bound_of_continuousOn hB
  set C : ℝ≥0 := C₀.toNNReal
  have hC : ∀ t ∈ Icc (0:ℝ) 1, ‖B t‖ ≤ C := fun t ht =>
    (hC₀ t ht).trans (Real.le_coe_toNNReal C₀)
  have hC0 : (0:ℝ) ≤ C := C.2
  set h : ℝ := 1 / (2 * C + 1) with hh
  have hpos : 0 < 2 * (C:ℝ) + 1 := by linarith
  have hh0 : 0 < h := by positivity
  have hlen : 2 * (C:ℝ) * h ≤ 1 := by
    rw [hh, mul_one_div, div_le_one hpos]; linarith
  let P : ℝ → Prop := fun σ => ∃ W : ℝ → E, W 0 = x₀ ∧
      ∀ t ∈ Icc (0:ℝ) σ, HasDerivWithinAt W (B t (W t)) (Icc 0 σ) t
  -- gluing step
  have step : ∀ s s' : ℝ, 0 ≤ s → s ≤ s' → s' ≤ 1 → 2 * (C:ℝ) * (s' - s) ≤ 1 →
      P s → P s' := by
    intro s s' hs hss' hs' hl ⟨W, hW0, hW⟩
    obtain ⟨φ, hφs, hφ⟩ := clm_local_exists hB hC hs hss' hs' hl (W s)
    classical
    refine ⟨fun t => if t ≤ s then W t else φ t, by simp [hs, hW0], fun t ht => ?_⟩
    rw [← Icc_union_Icc_eq_Icc hs hss']
    apply HasDerivWithinAt.union
    · by_cases hts : t ≤ s
      · have := hW t ⟨ht.1, hts⟩
        simp only [hts, if_true]
        exact this.congr (fun y hy => if_pos hy.2) (if_pos hts)
      · apply HasFDerivWithinAt.of_notMem_closure
        rw [closure_Icc]
        exact fun h' => hts h'.2
    · by_cases hts : s ≤ t
      · have := hφ t ⟨hts, ht.2⟩
        have hval : (if t ≤ s then W t else φ t) = φ t := by
          split_ifs with h'
          · rw [le_antisymm h' hts, hφs]
          · rfl
        simp only [hval]
        refine this.congr (fun y hy => ?_) hval
        split_ifs with h'
        · rw [le_antisymm h' hy.1, hφs]
        · rfl
      · apply HasFDerivWithinAt.of_notMem_closure
        rw [closure_Icc]
        exact fun h' => hts h'.1
  -- induction
  have key : ∀ k : ℕ, P (min (((k:ℝ) + 1) * h) 1) := by
    intro k
    induction k with
    | zero =>
      have hm : min ((((0:ℕ):ℝ) + 1) * h) 1 ≤ 1 := min_le_right _ _
      have hm0 : 0 ≤ min ((((0:ℕ):ℝ) + 1) * h) 1 := le_min (by positivity) zero_le_one
      have hmh : min ((((0:ℕ):ℝ) + 1) * h) 1 ≤ h := (min_le_left _ _).trans (by simp)
      obtain ⟨φ, hφ0, hφ⟩ := clm_local_exists hB hC le_rfl hm0 hm
        (by nlinarith) x₀
      exact ⟨φ, hφ0, hφ⟩
    | succ k ih =>
      refine step _ _ (le_min (by positivity) zero_le_one) ?_ (min_le_right _ _) ?_ ih
      · apply min_le_min_right; push_cast; nlinarith
      · push_cast
        rcases min_cases (((k:ℝ) + 1) * h) 1 with ⟨h1, _⟩ | ⟨h1, _⟩
        · rw [h1]
          have : min (((k:ℝ) + 1 + 1) * h) 1 ≤ ((k:ℝ) + 1 + 1) * h := min_le_left _ _
          nlinarith
        · rw [h1]
          have : min (((k:ℝ) + 1 + 1) * h) 1 ≤ 1 := min_le_right _ _
          nlinarith
  obtain ⟨W, hW0, hW⟩ := key ⌈2 * (C:ℝ)⌉₊
  have hone : min ((((⌈2 * (C:ℝ)⌉₊ : ℕ) : ℝ) + 1) * h) 1 = 1 := by
    apply min_eq_right
    have hc := Nat.le_ceil (2 * (C:ℝ))
    rw [hh, ← div_eq_mul_one_div, le_div_iff₀ hpos]
    linarith
  rw [hone] at hW
  exact ⟨W, hW0, hW⟩

end General

variable {A : Type*} [NormedRing A] [NormedAlgebra ℝ A] [CompleteSpace A] [NormOneClass A]

/-- `U` is the fundamental solution of `U' = X U` on `[0,1]` with `U 0 = 1`. -/
def IsFundSol (X : ℝ → A) (U : ℝ → A) : Prop :=
  U 0 = 1 ∧ ∀ t ∈ Icc (0:ℝ) 1, HasDerivWithinAt U (X t * U t) (Icc 0 1) t

omit [CompleteSpace A] [NormOneClass A] in
lemma continuousOn_mulLeft {X : ℝ → A} (hX : ContinuousOn X (Icc 0 1)) :
    ContinuousOn (fun t => ContinuousLinearMap.mul ℝ A (X t)) (Icc 0 1) :=
  (ContinuousLinearMap.mul ℝ A).continuous.comp_continuousOn hX

omit [CompleteSpace A] [NormOneClass A] in
lemma continuousOn_mulRight {X : ℝ → A} (hX : ContinuousOn X (Icc 0 1)) :
    ContinuousOn (fun t => (ContinuousLinearMap.mul ℝ A).flip (X t)) (Icc 0 1) :=
  (ContinuousLinearMap.mul ℝ A).flip.continuous.comp_continuousOn hX

omit [CompleteSpace A] [NormOneClass A] in
/-- Uniqueness for the linear equation `W' = X W` (any initial value). -/
theorem linear_eqOn_of_hasDerivWithinAt {X : ℝ → A} (hX : ContinuousOn X (Icc 0 1))
    {W W' : ℝ → A}
    (hW : ∀ t ∈ Icc (0:ℝ) 1, HasDerivWithinAt W (X t * W t) (Icc 0 1) t)
    (hW' : ∀ t ∈ Icc (0:ℝ) 1, HasDerivWithinAt W' (X t * W' t) (Icc 0 1) t)
    (h0 : W 0 = W' 0) : EqOn W W' (Icc 0 1) :=
  clm_eqOn_of_hasDerivWithinAt (B := fun t => ContinuousLinearMap.mul ℝ A (X t))
    (continuousOn_mulLeft hX) (by simpa using hW) (by simpa using hW') h0

omit [NormOneClass A] in
/-- Global existence on `[0,1]` for continuous coefficients. -/
theorem exists_isFundSol {X : ℝ → A} (hX : ContinuousOn X (Icc 0 1)) : ∃ U, IsFundSol X U := by
  obtain ⟨U, hU0, hU⟩ := clm_exists (continuousOn_mulLeft hX) (1 : A)
  exact ⟨U, hU0, by simpa using hU⟩

omit [CompleteSpace A] [NormOneClass A] in
theorem IsFundSol.continuousOn {X U : ℝ → A} (hU : IsFundSol X U) :
    ContinuousOn U (Icc 0 1) :=
  fun t ht => (hU.2 t ht).continuousWithinAt

omit [NormOneClass A] in
/-- Two-sided inverse of the fundamental solution: `L U = U L = 1` where `L' = -(L X)`. -/
theorem IsFundSol.exists_inverse {X U : ℝ → A} (hX : ContinuousOn X (Icc 0 1))
    (hU : IsFundSol X U) :
    ∃ L : ℝ → A, ∀ t ∈ Icc (0:ℝ) 1, L t * U t = 1 ∧ U t * L t = 1 := by
  obtain ⟨L, hL0, hL⟩ := clm_exists (B := fun t => -((ContinuousLinearMap.mul ℝ A).flip (X t)))
    (continuousOn_mulRight hX).neg (1 : A)
  simp only [ContinuousLinearMap.neg_apply, ContinuousLinearMap.flip_apply,
    ContinuousLinearMap.mul_apply'] at hL
  refine ⟨L, fun t ht => ⟨?_, ?_⟩⟩
  · -- `(L U)' = 0`
    have hP : ∀ τ ∈ Icc (0:ℝ) 1,
        HasDerivWithinAt (fun τ => L τ * U τ) ((fun _ => (0:A)) τ * (L τ * U τ)) (Icc 0 1) τ := by
      intro τ hτ
      refine ((hL τ hτ).mul (hU.2 τ hτ)).congr_deriv ?_
      simp only [zero_mul]
      rw [neg_mul, ← mul_assoc, mul_assoc (L τ), neg_add_cancel]
    have h1 : ∀ τ ∈ Icc (0:ℝ) 1,
        HasDerivWithinAt (fun _ => (1:A)) ((fun _ => (0:A)) τ * 1) (Icc 0 1) τ := by
      intro τ _
      simpa using hasDerivWithinAt_const τ (Icc (0:ℝ) 1) (1:A)
    have := linear_eqOn_of_hasDerivWithinAt (X := fun _ => (0:A)) continuousOn_const hP h1
      (by simp [hL0, hU.1]) ht
    simpa using this
  · -- `Z = U L` solves `Z' = X Z - Z X`
    let B : ℝ → A →L[ℝ] A := fun τ =>
      ContinuousLinearMap.mul ℝ A (X τ) - (ContinuousLinearMap.mul ℝ A).flip (X τ)
    have hB : ContinuousOn B (Icc 0 1) := (continuousOn_mulLeft hX).sub (continuousOn_mulRight hX)
    have hBapp : ∀ τ (z : A), B τ z = X τ * z - z * X τ := by
      intro τ z
      simp [B]
    have hZ : ∀ τ ∈ Icc (0:ℝ) 1,
        HasDerivWithinAt (fun τ => U τ * L τ) (B τ (U τ * L τ)) (Icc 0 1) τ := by
      intro τ hτ
      refine ((hU.2 τ hτ).mul (hL τ hτ)).congr_deriv ?_
      rw [hBapp, mul_neg, mul_assoc, ← mul_assoc (U τ) (L τ) (X τ)]
      abel
    have h1 : ∀ τ ∈ Icc (0:ℝ) 1,
        HasDerivWithinAt (fun _ => (1:A)) (B τ 1) (Icc 0 1) τ := by
      intro τ _
      rw [hBapp, mul_one, one_mul, sub_self]
      exact hasDerivWithinAt_const τ (Icc (0:ℝ) 1) (1:A)
    have := clm_eqOn_of_hasDerivWithinAt hB hZ h1 (by simp [hL0, hU.1]) ht
    simpa using this

omit [NormOneClass A] in
theorem IsFundSol.isUnit {X U : ℝ → A} (hX : ContinuousOn X (Icc 0 1)) (hU : IsFundSol X U) :
    ∀ t ∈ Icc (0:ℝ) 1, IsUnit (U t) := by
  obtain ⟨L, hL⟩ := hU.exists_inverse hX
  intro t ht
  exact ⟨⟨U t, L t, (hL t ht).2, (hL t ht).1⟩, rfl⟩

end QOU.Mass.KZHolonomy
