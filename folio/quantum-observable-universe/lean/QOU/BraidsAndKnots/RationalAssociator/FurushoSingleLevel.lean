import QOU.BraidsAndKnots.RationalAssociator.FurushoGroupStep

/-!
# The group-level Furusho step needs one associator one degree up, and nothing else

Bean `qou-3fdg`, audit §17m.

`FurushoGroupStep.lean` proves `FurushoGroupStep E d` (`d ≥ 3`) from a `K`-associator for `E`
at **every** level (`GroupLikeKAssociatorTower K E`), and unconditionally for `E = 1`. This file
shows that the step at degree `d` consumes **one** group-like `K`-associator, modulo `d + 1`,
and nothing about higher levels; and that over `ℚ` the step at `d` is **equivalent** to the
existence of a rational associator modulo `d + 1`, as soon as the hypothesis set of the step is
non-empty.

* `LevelInvAt K E d N Φ`: the level invariant of `AssociatorRealign.lean`, at the single level
  `N`.
* `levelInvAt_of_assoc`: one group-like `K`-associator modulo `N` gives `LevelInvAt K E d N Φ`
  for every rational associator `Φ` modulo `d` with `d ≤ N` (re-alignment by `realign`, one
  degree at a time, along the truncations of `Φ`).
* `assocU4_succ_of_pentagon_at`: the reduction step of `FurushoReduction.lean` from the
  single-level invariant at `N = d + 1`.
* `furushoGroupStep_of_exists_assocK`: `FurushoGroupStep E d` for `d ≥ 3` from one group-like
  `K`-associator for `E` modulo `d + 1`.
* `assocK_of_assocU4`: base change of a rational associator.
* `furushoGroupStep_iff_exists`: over `ℚ`, for `d ≥ 3` and a witness of the step's hypotheses,
  `FurushoGroupStep E d ↔ ∃ Ψ, AssocU4 (d + 1) E Ψ ∧ GL (d + 1) Ψ`.

## What this says about `μ ≠ 0`

For `E ≠ 1` the step at degree `d` is exactly one-degree existence of a rational associator for
`E` modulo `d + 1`. That existence is Drinfeld's theorem (KZ over `ℂ`, then descent); no
algebraic proof of it is in the repository, and this file does not supply one. So the
`μ ≠ 0` step is not proved here; it is reduced to the smallest existence statement it can be.

No `axiom`, no `sorry`, no analysis.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

open TensorProduct

local notation "F2" => FreeAlgebra ℚ (Fin 2)

variable {K : Type*} [Field K] [Algebra ℚ K]

variable (K) in
/-- **The level invariant at a single level `N`.** `ε(Φ) = 1` and some group-like
`K`-associator in `U4 N` agrees with `1 ⊗ Φ` modulo `FFK d`. -/
def LevelInvAt (E : F2) (d N : ℕ) (Φ : F2) : Prop :=
  FreeAlgebra.algebraMapInv Φ = 1 ∧
    ∃ Ψ : K ⊗[ℚ] F2, AssocK K N E Ψ ∧ GLK K N Ψ ∧ Ψ - (1 : K) ⊗ₜ Φ ∈ FFK K d

/-- The single-level invariant moves up one degree along an associator. -/
theorem LevelInvAt.succ_of_assoc {E Φ : F2} {d N : ℕ} (hd : 1 ≤ d) (hdN : d + 1 ≤ N)
    (hE : FreeAlgebra.algebraMapInv E = 1) (h : LevelInvAt K E d N Φ)
    (ha : AssocU4 (d + 1) E Φ) (hg : GL (d + 1) Φ) : LevelInvAt K E (d + 1) N Φ := by
  obtain ⟨hΦ, Ψ, hK, hGL, hm⟩ := h
  obtain ⟨Ψ', hK', hGL', hm'⟩ := realign (x := 0) hd hdN hE hΦ (zero_mem _)
    (by rwa [add_zero]) (by rwa [add_zero]) hK hGL hm
  exact ⟨hΦ, Ψ', hK', hGL', by rwa [add_zero] at hm'⟩

/-- **One `K`-associator modulo `N` aligns onto every rational associator modulo `d ≤ N`.** -/
theorem levelInvAt_of_assoc {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1) {N : ℕ}
    {Ψ : K ⊗[ℚ] F2} (hK : AssocK K N E Ψ) (hGL : GLK K N Ψ) {d : ℕ} (hd : 1 ≤ d)
    (hdN : d ≤ N) {Φ : F2} (hA : AssocU4 d E Φ) (hG : GL d Φ) : LevelInvAt K E d N Φ := by
  have hΦ := hA.const
  have key : ∀ j, 1 ≤ j → j ≤ d → LevelInvAt K E j N Φ := by
    intro j hj
    induction j, hj using Nat.le_induction with
    | base =>
      intro _
      refine ⟨hΦ, Ψ, hK, hGL, ?_⟩
      have e : Ψ - (1 : K) ⊗ₜ Φ = (Ψ - 1) - (1 : K) ⊗ₜ (Φ - 1) := by
        rw [tmul_sub, ← Algebra.TensorProduct.one_def]; abel
      rw [e]
      exact sub_mem hK.sub_one_mem_FFK (tmul_mem_FFK _ (sub_one_mem_FF_one hΦ))
    | succ j hj ih =>
      intro hjd
      exact (ih (by omega)).succ_of_assoc hj (by omega) hE (hA.trunc hjd) (FF2_anti hjd hG)
  exact key d hd le_rfl

/-- **The reduction step from the single-level invariant at `N = d + 1`.** -/
theorem assocU4_succ_of_pentagon_at {d : ℕ} (hd : 1 ≤ d) (hFL : PentagonHexagonLie d)
    {E Φ : F2} (hE : FreeAlgebra.algebraMapInv E = 1) (h : LevelInvAt K E d (d + 1) Φ)
    (hp : Pentagon Φ (t (d + 1) 0) (t (d + 1) 1) (t (d + 1) 3) (t (d + 1) 4) (t (d + 1) 5))
    (hg : GL (d + 1) Φ) : AssocU4 (d + 1) E Φ := by
  obtain ⟨hΦ, Ψ, hK, hGL, hm⟩ := h
  obtain ⟨z, rfl⟩ := exists_lTensor_of_mem_FFK hm
  obtain ⟨x, hx, ha, hgx, -⟩ :=
    inductionStep_of_groupLike hd le_rfl (by omega : 2 ≤ d + 1) le_rfl hE hΦ z hK hGL
  have hA1 : Φ + x - 1 ∈ FF 1 := by
    have e : Φ + x - 1 = (Φ - 1) + x := by abel
    rw [e]
    exact add_mem (sub_one_mem_FF_one hΦ) (FF_anti hd hx)
  have hδ : primDef (-x) ∈ FF2 (d + 1) :=
    primDef_mem_of_GL_add hd hA1 (neg_mem hx) hgx (by rwa [add_neg_cancel_right])
  obtain ⟨k, hk, hxk, hkp⟩ := exists_primitive_layer (neg_mem hx) hδ
  have hdef : assocDefect (d + 1) E Φ = -assocLin (d + 1) x := by
    have h0 := (assocU4_iff.1 ha).2
    rw [assocDefect_add hd hE hΦ hx] at h0
    exact eq_neg_of_add_eq_zero_left h0
  have hlk : assocLin (d + 1) k = -assocLin (d + 1) x := by
    have e : k = -x - (-x - k) := by abel
    rw [e, map_sub, assocLin_eq_zero_of_mem_FF hxk, sub_zero, map_neg]
  have hpk : (assocLin (d + 1) k).2.2 = 0 := by
    rw [hlk, ← hdef]; exact assocDefect_pent_eq_zero hp
  have hk0 := hFL k hk hkp hpk
  refine assocU4_iff.2 ⟨hΦ, ?_⟩
  have hx0 : assocLin (d + 1) x = 0 := by rw [← neg_eq_zero, ← hlk, hk0]
  rw [hdef, hx0, neg_zero]

/-- **Furusho's group-level step at `d ≥ 3` from one group-like `K`-associator for `E` modulo
`d + 1`.** No other level is used. -/
theorem furushoGroupStep_of_exists_assocK {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    {d : ℕ} (hd : 3 ≤ d) {Ψ : K ⊗[ℚ] F2} (hK : AssocK K (d + 1) E Ψ)
    (hGL : GLK K (d + 1) Ψ) : FurushoGroupStep E d := by
  intro Φ hA hG hp
  exact assocU4_succ_of_pentagon_at (by omega) (pentagonHexagonLie_of_three_le d hd) hE
    (levelInvAt_of_assoc hE hK hGL (by omega) (by omega) hA (FF2_anti (by omega) hG)) hp hG

/-- A rational associator in `U4 N` is a `K`-associator after base change. -/
theorem assocK_of_assocU4 {N : ℕ} {E Φ : F2} (h : AssocU4 N E Φ) :
    AssocK K N E ((1 : K) ⊗ₜ Φ) where
  const := by rw [evK_one_tmul, eval_zero_zero, h.const, map_one]
  inv a b ha hb := by
    rw [evK_one_tmul, evK_one_tmul, ← map_eval, ← map_eval, ← map_mul, h.inv a b ha hb, map_one]
  hex := by
    have := congrArg (ιK K N) h.hex
    simp only [map_mul, map_eval, map_add, map_zero] at this
    simp only [HexagonF, evK_one_tmul]
    exact this
  pent := by
    have := congrArg (ιK K N) h.pent
    simp only [map_mul, map_eval, map_add] at this
    simp only [PentagonF, evK_one_tmul]
    exact this

/-- **Over `ℚ`, the step at `d ≥ 3` is one-degree existence.** Given one `Φ` satisfying the
hypotheses of `FurushoGroupStep E d`, the step holds iff some rational associator for `E`
modulo `d + 1`, group-like modulo `FF2 (d + 1)`, exists. -/
theorem furushoGroupStep_iff_exists {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1) {d : ℕ}
    (hd : 3 ≤ d) {Φ₀ : F2} (hA₀ : AssocU4 d E Φ₀) (hG₀ : GL (d + 1) Φ₀)
    (hp₀ : Pentagon Φ₀ (t (d + 1) 0) (t (d + 1) 1) (t (d + 1) 3) (t (d + 1) 4) (t (d + 1) 5)) :
    FurushoGroupStep E d ↔ ∃ Ψ : F2, AssocU4 (d + 1) E Ψ ∧ GL (d + 1) Ψ := by
  constructor
  · intro hF
    exact ⟨Φ₀, hF Φ₀ hA₀ hG₀ hp₀, hG₀⟩
  · rintro ⟨Ψ, hA, hG⟩
    exact furushoGroupStep_of_exists_assocK (K := ℚ) hE hd (assocK_of_assocU4 hA) (GLK_of_GL hG)

end QOU.BraidsAndKnots.RationalAssociator
