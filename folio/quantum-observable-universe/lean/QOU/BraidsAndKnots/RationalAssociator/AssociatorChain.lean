import QOU.BraidsAndKnots.RationalAssociator.GroupLikeK

/-!
# Chaining the induction: a rational associator modulo `N` from a `K`-associator modulo `N`

`inductionStep_of_groupLike` (`GroupLikeK`) raises the degree of agreement between a rational
`Φ` and a group-like `K`-associator `Ψ` by one. This file iterates it, starting from `Φ = 1` in
degree `1`, up to degree `N`.

* `sub_evK_zero_mem_FFK`: every `x ∈ K ⊗ ℚ⟨X, Y⟩` agrees with its constant term `evK 0 0 x`
  modulo `FFK K 1`. This is the base case: a `K`-associator `Ψ₀` satisfies `Ψ₀ − 1 ∈ FFK K 1`.
* `exists_lTensor_of_mem_FFK`: membership in `FFK K m` is, by definition, being an
  `lTensor`-image, which is the input form of the induction step.
* `chain_invariant`: the invariant at every degree `1 ≤ d ≤ N`.
* `rational_associator_of_groupLikeK`: **a group-like `K`-associator in `U4 N` gives a rational
  associator `Φ` in `U4 N` that is group-like modulo `FF2 N`.**
* `AssocU4.congr_exp`, `AssocK.congr_exp`: an associator in `U4 N` sees its exponential only
  modulo `FF N`.
* `ExpFamily`: a per-level exponential `E : ℕ → ℚ⟨X, Y⟩`, consecutive members agreeing modulo
  `FF N`.
* `GroupLikeKAssociatorTower` and `rational_associator_of_tower`: the conditional corollary for
  every `N ≥ 2`, with the exponential `E N` at level `N` (audit §17p).

The only input that is not proved here is the existence of the `K`-associators themselves
(for `K = ℂ` this is Drinfeld's KZ associator, an analytic construction). It enters as the
hypothesis of the theorems, or as the fields of `GroupLikeKAssociatorTower`; it is never
asserted.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

open TensorProduct Friedrichs

local notation "F2" => FreeAlgebra ℚ (Fin 2)

variable {K : Type*} [Field K] [Algebra ℚ K]

/-! ### The two missing pieces -/

/-- Every `x ∈ K ⊗ ℚ⟨X, Y⟩` agrees with its constant term modulo `FFK K 1`. -/
theorem sub_evK_zero_mem_FFK (x : K ⊗[ℚ] F2) :
    x - evK (0 : K) 0 x ⊗ₜ (1 : F2) ∈ FFK K 1 := by
  induction x using TensorProduct.induction_on with
  | zero => simp
  | add u v hu hv =>
    have e : u + v - evK (0 : K) 0 (u + v) ⊗ₜ (1 : F2) =
        (u - evK (0 : K) 0 u ⊗ₜ (1 : F2)) + (v - evK (0 : K) 0 v ⊗ₜ (1 : F2)) := by
      rw [map_add, TensorProduct.add_tmul]; abel
    rw [e]; exact add_mem hu hv
  | tmul k p =>
    have e : k ⊗ₜ[ℚ] p - evK (0 : K) 0 (k ⊗ₜ p) ⊗ₜ (1 : F2) =
        k ⊗ₜ (p - algebraMap ℚ F2 (FreeAlgebra.algebraMapInv p)) := by
      rw [evK_tmul, eval_zero_zero, Algebra.algebraMap_self_apply, TensorProduct.tmul_sub,
        Algebra.algebraMap_eq_smul_one (A := F2), Algebra.algebraMap_eq_smul_one (A := K),
        mul_smul_comm, mul_one, TensorProduct.smul_tmul]
    rw [e]
    exact tmul_mem_FFK k (sub_algebraMapInv_mem_FF p)

/-- A `K`-associator is `1` modulo `FFK K 1`. -/
theorem AssocK.sub_one_mem_FFK {N : ℕ} {E : F2} {Ψ : K ⊗[ℚ] F2} (h : AssocK K N E Ψ) :
    Ψ - 1 ∈ FFK K 1 := by
  have := sub_evK_zero_mem_FFK Ψ
  rwa [h.const, ← Algebra.TensorProduct.one_def] at this

/-- Membership in `FFK K m` is being an `lTensor`-image (the input form of the step). -/
theorem exists_lTensor_of_mem_FFK {m : ℕ} {Φ : F2} {Ψ : K ⊗[ℚ] F2}
    (h : Ψ - (1 : K) ⊗ₜ Φ ∈ FFK K m) :
    ∃ z : K ⊗[ℚ] FF m, Ψ = (1 : K) ⊗ₜ Φ + LinearMap.lTensor K (FF m).subtype z := by
  obtain ⟨z, hz⟩ := h
  exact ⟨z, by rw [hz]; abel⟩

/-- Adding an element of `FF d`, `d ≥ 1`, keeps constant term `1`. -/
theorem algebraMapInv_add_of_mem_FF {d : ℕ} (hd : 1 ≤ d) {Φ x : F2}
    (hΦ : FreeAlgebra.algebraMapInv Φ = 1) (hx : x ∈ FF d) :
    FreeAlgebra.algebraMapInv (Φ + x) = 1 := by
  rw [map_add, hΦ, algebraMapInv_eq_zero_of_mem_FF hd hx, add_zero]

/-! ### The chain -/

/-- **The invariant of the chain.** Given a group-like `K`-associator in `U4 N`, for every
degree `1 ≤ d ≤ N` there is a rational `Φ` with constant term `1` that, from degree `2` on, is an
associator in `U4 d` and group-like modulo `FF2 d`, together with a group-like `K`-associator
`Ψ` in `U4 N` with `Ψ ≡ 1 ⊗ Φ (mod FFK K d)`. -/
theorem chain_invariant {N : ℕ} (hN : 2 ≤ N) {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    {Ψ₀ : K ⊗[ℚ] F2} (hK : AssocK K N E Ψ₀) (hGL : GLK K N Ψ₀) {d : ℕ} (hd : 1 ≤ d)
    (hdN : d ≤ N) :
    ∃ Φ : F2, FreeAlgebra.algebraMapInv Φ = 1 ∧ (2 ≤ d → AssocU4 d E Φ ∧ GL d Φ) ∧
      ∃ Ψ, AssocK K N E Ψ ∧ GLK K N Ψ ∧ Ψ - (1 : K) ⊗ₜ Φ ∈ FFK K d := by
  induction d, hd using Nat.le_induction with
  | base =>
    refine ⟨1, map_one _, fun h => absurd h (by omega), Ψ₀, hK, hGL, ?_⟩
    rw [← Algebra.TensorProduct.one_def]
    exact hK.sub_one_mem_FFK
  | succ d hd ih =>
    obtain ⟨Φ, hΦ, -, Ψ, hΨK, hΨGL, hmem⟩ := ih (by omega)
    obtain ⟨z, rfl⟩ := exists_lTensor_of_mem_FFK hmem
    obtain ⟨x, hx, ha, hgl, Ψ', hΨ'K, hΨ'GL, hm'⟩ :=
      inductionStep_of_groupLike hd hdN hN le_rfl hE hΦ z hΨK hΨGL
    exact ⟨Φ + x, algebraMapInv_add_of_mem_FF hd hΦ hx, fun _ => ⟨ha, hgl⟩, Ψ', hΨ'K, hΨ'GL,
      hm'⟩

/-- **A rational associator from a group-like `K`-associator.** Let `K/ℚ` be a field extension,
`N ≥ 2`, and `E ∈ ℚ⟨X, Y⟩` with constant term `1`. If some `Ψ₀ ∈ K ⊗ ℚ⟨X, Y⟩` is an associator
in `K ⊗ U4 N` for `E` (`AssocK`) and group-like modulo `FF2K N` (`GLK`), then there is a rational
`Φ ∈ ℚ⟨X, Y⟩` that is an associator in `U4 N` for `E` and group-like modulo `FF2 N`. -/
theorem rational_associator_of_groupLikeK {N : ℕ} (hN : 2 ≤ N) {E : F2}
    (hE : FreeAlgebra.algebraMapInv E = 1) {Ψ₀ : K ⊗[ℚ] F2} (hK : AssocK K N E Ψ₀)
    (hGL : GLK K N Ψ₀) :
    ∃ Φ : F2, AssocU4 N E Φ ∧ GL N Φ := by
  obtain ⟨Φ, -, h, -⟩ := chain_invariant hN hE hK hGL (by omega : 1 ≤ N) le_rfl
  exact ⟨Φ, h hN⟩

/-! ### Changing the exponential above the truncation degree -/

/-- Two polynomials that agree modulo `FF N` have the same evaluations at elements of
`Fil N 1` in `U4 N`. -/
theorem eval_congr_of_sub_mem_FF {N : ℕ} {E E' : F2} (h : E - E' ∈ FF N) {a b : U4 N}
    (ha : a ∈ Fil N 1) (hb : b ∈ Fil N 1) : eval a b E = eval a b E' := by
  rw [← sub_eq_zero, ← map_sub]
  exact eq_zero_of_mem_Fil (eval_mem_Fil ha hb h)

/-- **An associator in `U4 N` sees its exponential only modulo `FF N`.** -/
theorem AssocU4.congr_exp {N : ℕ} {E E' Φ : F2} (h : E - E' ∈ FF N) (hA : AssocU4 N E Φ) :
    AssocU4 N E' Φ where
  const := hA.const
  inv := hA.inv
  hex := by
    have h0 : (0 : U4 N) ∈ Fil N 1 := zero_mem _
    have hx := hA.hex
    unfold Hexagon at hx ⊢
    rwa [← eval_congr_of_sub_mem_FF h (add_mem (t_mem_Fil_one 1) (t_mem_Fil_one 3)) h0,
      ← eval_congr_of_sub_mem_FF h (t_mem_Fil_one 1) h0,
      ← eval_congr_of_sub_mem_FF h (t_mem_Fil_one 3) h0]
  pent := hA.pent

theorem assocU4_congr_exp {N : ℕ} {E E' Φ : F2} (h : E - E' ∈ FF N) :
    AssocU4 N E Φ ↔ AssocU4 N E' Φ :=
  ⟨AssocU4.congr_exp h, AssocU4.congr_exp (by rw [← neg_sub]; exact neg_mem h)⟩

/-- The `K`-form of `eval_congr_of_sub_mem_FF`, at images of `ιK`. -/
theorem eval_ιK_congr_of_sub_mem_FF {N : ℕ} {E E' : F2} (h : E - E' ∈ FF N) {a : U4 N}
    (ha : a ∈ Fil N 1) :
    eval (ιK K N a) 0 E = eval (ιK K N a) 0 E' := by
  rw [← map_zero (ιK K N), ← map_eval, ← map_eval,
    eval_congr_of_sub_mem_FF h ha (zero_mem _)]

/-- **A `K`-associator in `K ⊗ U4 N` sees its exponential only modulo `FF N`.** -/
theorem AssocK.congr_exp {N : ℕ} {E E' : F2} {Ψ : K ⊗[ℚ] F2} (h : E - E' ∈ FF N)
    (hA : AssocK K N E Ψ) : AssocK K N E' Ψ where
  const := hA.const
  inv := hA.inv
  hex := by
    have hx := hA.hex
    unfold HexagonF at hx ⊢
    rwa [← map_add, ← eval_ιK_congr_of_sub_mem_FF h
        (add_mem (t_mem_Fil_one 1) (t_mem_Fil_one 3)),
      ← eval_ιK_congr_of_sub_mem_FF h (t_mem_Fil_one 1),
      ← eval_ιK_congr_of_sub_mem_FF h (t_mem_Fil_one 3), map_add]
  pent := hA.pent

/-! ### Per-level exponentials -/

/-- **A compatible family of exponentials.** `E N` is the exponential used at level `N`: it has
constant term `1` from level `1` on, and consecutive members agree modulo `FF N`, so that
`E M` and `E N` give the same hexagon in `U4 N` for `M ≥ N`. A single polynomial `E` is the
constant family (`expFamily_const`); `exp(X/2)` truncated at degree `N`
(`expHalfTrunc`, `ExpHalfTrunc.lean`) is the family the KZ associator needs. -/
structure ExpFamily (E : ℕ → F2) : Prop where
  const : ∀ N, 1 ≤ N → FreeAlgebra.algebraMapInv (E N) = 1
  compat : ∀ N, E (N + 1) - E N ∈ FF N

theorem ExpFamily.sub_mem {E : ℕ → F2} (hE : ExpFamily E) {N M : ℕ} (h : N ≤ M) :
    E M - E N ∈ FF N := by
  induction M, h using Nat.le_induction with
  | base => rw [sub_self]; exact zero_mem _
  | succ M hNM ih =>
    have e : E (M + 1) - E N = (E (M + 1) - E M) + (E M - E N) := by abel
    rw [e]
    exact add_mem (FF_anti hNM (hE.compat M)) ih

/-- In `U4 N`, the exponential of any level `M ≥ N` may replace that of level `N`. -/
theorem ExpFamily.assocU4_iff {E : ℕ → F2} (hE : ExpFamily E) {N M : ℕ} (h : N ≤ M)
    {Φ : F2} : AssocU4 N (E M) Φ ↔ AssocU4 N (E N) Φ :=
  assocU4_congr_exp (hE.sub_mem h)

theorem ExpFamily.assocK {E : ℕ → F2} (hE : ExpFamily E) {N M : ℕ} (h : N ≤ M)
    {Ψ : K ⊗[ℚ] F2} (hA : AssocK K N (E N) Ψ) : AssocK K N (E M) Ψ :=
  hA.congr_exp (by rw [← neg_sub]; exact neg_mem (hE.sub_mem h))

/-- A single polynomial with constant term `1` is a (constant) compatible family. -/
theorem expFamily_const {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1) :
    ExpFamily (fun _ => E) :=
  ⟨fun _ _ => hE, fun _ => by simp⟩

/-! ### The conditional corollary -/

variable (K) in
/-- **The analytic input, as a hypothesis with content, with a per-level exponential.** For
every `N ≥ 2` there is a `K`-associator in `K ⊗ U4 N` for the level-`N` exponential `E N` that
is group-like modulo `FF2K N`. For `K = ℂ` and `E = expHalfTrunc` (`exp(X/2)` truncated at
degree `N`) this is what Drinfeld's KZ associator provides; nothing in this repository
constructs it, and it is not asserted here.

Until 2026-11-28 this structure took one polynomial `E` for all levels. For
`E = expHalfPoly = 1 + X/2 + X²/8` that hypothesis is false over every `K`
(`not_groupLikeKAssociatorTower_expHalfPoly`, audit §17o); the constant family
`fun _ => E` is the old form, and `E = 1` (the `GRT₁` case) is still inhabited
(`groupLikeKAssociatorTower_one`). Audit §17p. -/
structure GroupLikeKAssociatorTower (E : ℕ → F2) : Prop where
  exists_assoc : ∀ N : ℕ, 2 ≤ N → ∃ Ψ : K ⊗[ℚ] F2, AssocK K N (E N) Ψ ∧ GLK K N Ψ

/-- **Rational associators modulo every `N ≥ 2`, conditional on the `K`-associators.** If for
some field extension `K/ℚ` group-like `K`-associators for `E N` exist modulo every `N ≥ 2`, then
rational group-like associators for `E N` exist modulo every `N ≥ 2`. -/
theorem rational_associator_of_tower {E : ℕ → F2} (hE : ExpFamily E)
    (hT : GroupLikeKAssociatorTower K E) {N : ℕ} (hN : 2 ≤ N) :
    ∃ Φ : F2, AssocU4 N (E N) Φ ∧ GL N Φ := by
  obtain ⟨Ψ, hK, hGL⟩ := hT.exists_assoc N hN
  exact rational_associator_of_groupLikeK hN (hE.const N (by omega)) hK hGL

end QOU.BraidsAndKnots.RationalAssociator
