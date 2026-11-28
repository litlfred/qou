import QOU.BraidsAndKnots.RationalAssociator.AssociatorTower

/-!
# A compatible tower of rational associators from an unrelated tower of `K`-associators

`rational_associator_compatible_of_tower` (`AssociatorTower`) builds one compatible sequence of
rational associators, but needs the `K`-associators `Ψ_N` themselves to agree,
`Ψ_{N+1} − Ψ_N ∈ FFK K N` (`CompatibleGroupLikeKAssociatorTower`). This file removes that
hypothesis: one group-like `K`-associator per level `N`, unrelated across levels
(`GroupLikeKAssociatorTower`), already gives the compatible rational sequence.

The missing ingredient was the transitivity of the `GRT₁` action on group-like associators
(Drinfeld 1991, Prop. 5.5). Only its degree-by-degree form is needed, and it is proved here:

* `primDef_mem_of_GL_add`: if `A` and `A + y` (`y ∈ FF d`, `A ≡ 1`) are both group-like modulo
  `FF2 (d + 1)`, then `y` is primitive modulo `FF2 (d + 1)`.
* `exists_grt_layer` (**Prop. 5.5 at one degree**): two rational group-like associators
  `Φ + x`, `Φ + x'` in `U4 (d + 1)`, `x, x' ∈ FF d`, differ at degree `d` by a homogeneous
  primitive `h` that lies in `grt` in every `U4 M`. The linear equations of `x' − x` cancel
  (`assocU4_add_iff`), so `h` is in the kernel of `assocLin`, and `grtU4_of_lin_primitive`
  applies.
* `realign`: a group-like `K`-associator at level `N` that agrees with `1 ⊗ Φ` modulo `FFK d` can be
  moved, inside the group-like `K`-associators at level `N`, to agree with `1 ⊗ (Φ + x)` modulo
  `FFK (d + 1)`, for **any** prescribed rational group-like associator `Φ + x` in `U4 (d + 1)`.
  First `inductionStep_of_groupLike` gives some rational `x'`; then the shift by `exp(h)`, with
  `h` from `exists_grt_layer`, replaces `x'` by `x`.
* `LevelInv`, `levelStep`: the induction, with the `K`-associator chosen afresh at each level.
* `rational_associator_compatible_of_groupLikeTower`: the sequence.

What this does not prove: Prop. 5.5 in its full form (for two group-like associators modulo `N`
there is a single `g ∈ GRT₁` modulo `N` with `Φ' = Φ ∘ g`). The degree-by-degree statement is
all the tower needs.

**Per-level exponential (2026-11-28).** The tower now takes a family `E : ℕ → F2` with
`ExpFamily E` (constant term `1`, and `E (N + 1) − E N ∈ FF N`); `LevelInv K E d Φ` uses
`AssocK K N (E N)` at level `N`, and `levelStep` lands in `AssocU4 (d + 1) (E (d + 1))`.
A constant family `fun _ => E` recovers the previous statements (`expFamily_const`). Audit §17p.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

open TensorProduct Friedrichs

local notation "F2" => FreeAlgebra ℚ (Fin 2)

/-! ### Prop. 5.5 at one degree, over `ℚ` -/

/-- **Two group-likes differing in `FF d` differ by a primitive element modulo `FF2 (d + 1)`.** -/
theorem primDef_mem_of_GL_add {d : ℕ} (hd : 1 ≤ d) {A y : F2} (hA1 : A - 1 ∈ FF 1)
    (hy : y ∈ FF d) (hA : GL (d + 1) A) (hAy : GL (d + 1) (A + y)) :
    primDef y ∈ FF2 (d + 1) := by
  unfold GL at hA hAy
  have e : primDef y = (cop (A + y) - (A + y) ⊗ₜ (A + y)) - (cop A - A ⊗ₜ A) +
      (A - 1) ⊗ₜ y + y ⊗ₜ (A - 1) + y ⊗ₜ y := by
    simp only [primDef_apply, map_add, add_tmul, tmul_add, sub_tmul, tmul_sub]
    abel
  rw [e]
  refine add_mem (add_mem (add_mem (sub_mem hAy hA) ?_) ?_) ?_
  · exact FF2_anti (by omega) (tmul_mem_FF2 hA1 hy)
  · exact FF2_anti (by omega) (tmul_mem_FF2 hy hA1)
  · exact FF2_anti (by omega) (tmul_mem_FF2 hy hy)

/-- **Drinfeld's Prop. 5.5 at one degree.** Let `ε(E) = ε(Φ) = 1`, `d ≥ 1`, and `x, x' ∈ FF d`
with `Φ + x` and `Φ + x'` both associators in `U4 (d + 1)` for `E` and group-like modulo
`FF2 (d + 1)`. Then `x' − x` agrees modulo `FF (d + 1)` with a homogeneous primitive `h` of
degree `d` that lies in `grt` in every `U4 M`. -/
theorem exists_grt_layer {d : ℕ} (hd : 1 ≤ d) {E Φ x x' : F2}
    (hE : FreeAlgebra.algebraMapInv E = 1) (hΦ : FreeAlgebra.algebraMapInv Φ = 1)
    (hx : x ∈ FF d) (hx' : x' ∈ FF d) (ha : AssocU4 (d + 1) E (Φ + x))
    (ha' : AssocU4 (d + 1) E (Φ + x')) (hg : GL (d + 1) (Φ + x)) (hg' : GL (d + 1) (Φ + x')) :
    ∃ h : F2, Homog d h ∧ x' - x - h ∈ FF (d + 1) ∧ IsPrimitive h ∧ ∀ M, GrtU4 M h := by
  have hy : x' - x ∈ FF d := sub_mem hx' hx
  have hA1 : Φ + x - 1 ∈ FF 1 := by
    have e : Φ + x - 1 = (Φ - algebraMap ℚ F2 (FreeAlgebra.algebraMapInv Φ)) + x := by
      rw [hΦ, map_one]; abel
    rw [e]
    exact add_mem (sub_algebraMapInv_mem_FF Φ) (FF_anti hd hx)
  have hδ : primDef (x' - x) ∈ FF2 (d + 1) := by
    refine primDef_mem_of_GL_add hd hA1 hy hg ?_
    rwa [show Φ + x + (x' - x) = Φ + x' by abel]
  obtain ⟨h, hh, hyh, hp⟩ := exists_primitive_layer hy hδ
  have hlin : assocLin (d + 1) (x' - x) = 0 := by
    rw [map_sub, (assocU4_add_iff hd hE hΦ hx').1 ha', (assocU4_add_iff hd hE hΦ hx).1 ha,
      sub_self]
  have hlinh : assocLin (d + 1) h = 0 := by
    have e : h = (x' - x) - ((x' - x) - h) := by abel
    rw [e, map_sub, hlin, assocLin_eq_zero_of_mem_FF hyh, sub_zero]
  exact ⟨h, hh, hyh, hp, fun M => grtU4_of_lin_primitive hh hlinh hp⟩

/-! ### Re-aligning a `K`-associator onto a prescribed rational one -/

variable {K : Type*} [Field K] [Algebra ℚ K]

/-- **Re-alignment.** Let `ε(E) = ε(Φ) = 1`, `1 ≤ d`, `d + 1 ≤ N`, and let `Φ + x` (`x ∈ FF d`)
be any rational associator in `U4 (d + 1)` for `E`, group-like modulo `FF2 (d + 1)`. Then every
group-like `K`-associator `Ψ` in `U4 N` with `Ψ ≡ 1 ⊗ Φ (mod FFK d)` can be replaced by a
group-like `K`-associator `Ψ'` in `U4 N` with `Ψ' ≡ 1 ⊗ (Φ + x) (mod FFK (d + 1))`. -/
theorem realign {d N : ℕ} (hd : 1 ≤ d) (hdN : d + 1 ≤ N) {E Φ x : F2}
    (hE : FreeAlgebra.algebraMapInv E = 1) (hΦ : FreeAlgebra.algebraMapInv Φ = 1)
    (hx : x ∈ FF d) (ha : AssocU4 (d + 1) E (Φ + x)) (hg : GL (d + 1) (Φ + x))
    {Ψ : K ⊗[ℚ] F2} (hK : AssocK K N E Ψ) (hGL : GLK K N Ψ)
    (hm : Ψ - (1 : K) ⊗ₜ Φ ∈ FFK K d) :
    ∃ Ψ' : K ⊗[ℚ] F2, AssocK K N E Ψ' ∧ GLK K N Ψ' ∧
      Ψ' - (1 : K) ⊗ₜ (Φ + x) ∈ FFK K (d + 1) := by
  obtain ⟨z, rfl⟩ := exists_lTensor_of_mem_FFK hm
  obtain ⟨x', hx', ha', hg', Ψ₁, hK₁, hGL₁, hm₁⟩ :=
    inductionStep_of_groupLike hd hdN (by omega : 2 ≤ N) le_rfl hE hΦ z hK hGL
  obtain ⟨h, -, hxh, hp, hgrt⟩ := exists_grt_layer hd hE hΦ hx' hx ha' ha hg' hg
  have hhF : h ∈ FF d := by
    have e : h = (x - x') - ((x - x') - h) := by abel
    rw [e]
    exact sub_mem (sub_mem hx hx') (FF_anti (by omega) hxh)
  obtain ⟨M, rfl⟩ : ∃ M, N = M + 1 := ⟨N - 1, by omega⟩
  have hgrt1 : ∀ r : ℚ, GRT1U4 (M + 1) (expPoly (r • h) (M + 1 + 2)) :=
    fun r => grt1U4_expPoly (hgrt (M + 1)) (by omega) (by omega) r
  refine ⟨compKK Ψ₁ (GK h (M + 1 + 2) 1), assocK_shiftK hK₁ hgrt1 1,
    GLK.compKK_GK hGL₁ (FF_anti hd hhF) hp (by omega) hgrt1 1, ?_⟩
  have hc := compKK_congr hd (n := M + 1 + 2) (by omega) hhF hK₁.sub_one_mem_FFK (1 : K)
  have e : compKK Ψ₁ (GK h (M + 1 + 2) 1) - (1 : K) ⊗ₜ (Φ + x) =
      (compKK Ψ₁ (GK h (M + 1 + 2) 1) - Ψ₁ - (1 : K) ⊗ₜ h) + (Ψ₁ - (1 : K) ⊗ₜ (Φ + x')) -
        (1 : K) ⊗ₜ (x - x' - h) := by
    simp only [tmul_add, tmul_sub]
    abel
  rw [e]
  exact sub_mem (add_mem hc hm₁) (tmul_mem_FFK _ hxh)

/-! ### The induction, with a fresh `K`-associator at each level -/

variable (K) in
/-- **The invariant at degree `d`.** `ε(Φ) = 1`, and for every level `N ≥ d + 1` there is
**some** group-like `K`-associator in `U4 N` for the level-`N` exponential `E N` agreeing with
`1 ⊗ Φ` modulo `FFK d`. Nothing ties the `K`-associators at different levels together. -/
def LevelInv (E : ℕ → F2) (d : ℕ) (Φ : F2) : Prop :=
  FreeAlgebra.algebraMapInv Φ = 1 ∧ ∀ N, d + 1 ≤ N →
    ∃ Ψ : K ⊗[ℚ] F2, AssocK K N (E N) Ψ ∧ GLK K N Ψ ∧ Ψ - (1 : K) ⊗ₜ Φ ∈ FFK K d

/-- **The induction step.** The correction `x` is chosen at level `d + 1`, for the exponential
`E (d + 1)`; `realign` then moves the `K`-associator of every higher level `N` onto `Φ + x`,
which is also an associator in `U4 (d + 1)` for `E N` because `E N ≡ E (d + 1)` modulo
`FF (d + 1)` (`ExpFamily.assocU4_iff`). -/
theorem levelStep {E : ℕ → F2} (hE : ExpFamily E) {d : ℕ} (hd : 1 ≤ d)
    {Φ : F2} (h : LevelInv K E d Φ) :
    ∃ x ∈ FF d, AssocU4 (d + 1) (E (d + 1)) (Φ + x) ∧ GL (d + 1) (Φ + x) ∧
      LevelInv K E (d + 1) (Φ + x) := by
  obtain ⟨hΦ, hT⟩ := h
  obtain ⟨Ψ, hK, hGL, hm⟩ := hT (d + 1) le_rfl
  obtain ⟨z, rfl⟩ := exists_lTensor_of_mem_FFK hm
  obtain ⟨x, hx, ha, hg, -⟩ := inductionStep_of_groupLike hd le_rfl (by omega : 2 ≤ d + 1)
    le_rfl (hE.const (d + 1) (by omega)) hΦ z hK hGL
  refine ⟨x, hx, ha, hg, algebraMapInv_add_of_mem_FF hd hΦ hx, fun N hN => ?_⟩
  obtain ⟨Ψ', hK', hGL', hm'⟩ := hT N (by omega)
  exact realign hd (by omega) (hE.const N (by omega)) hΦ hx
    ((hE.assocU4_iff (by omega)).2 ha) hg hK' hGL' hm'

/-- **A compatible sequence of rational associators from unrelated `K`-associators.** If for
some field extension `K/ℚ` there is, for every `N ≥ 2`, a group-like `K`-associator for `E N`
modulo `N` (`GroupLikeKAssociatorTower`, no compatibility between the `K`-associators), and `E`
is a compatible family of exponentials, then there is one sequence `Φ : ℕ → ℚ⟨X, Y⟩` with
`Φ N` an associator in `U4 N` for `E N` and group-like modulo `FF2 N` for every `N ≥ 2`, and
`Φ (N + 1) − Φ N ∈ FF N` for every `N ≥ 1`. This is the conclusion of
`rational_associator_compatible_of_tower` under the weaker hypothesis, and with a per-level
exponential. -/
theorem rational_associator_compatible_of_groupLikeTower {E : ℕ → F2}
    (hE : ExpFamily E) (hT : GroupLikeKAssociatorTower K E) :
    ∃ Φ : ℕ → F2, (∀ N, 2 ≤ N → AssocU4 N (E N) (Φ N) ∧ GL N (Φ N)) ∧
      ∀ N, 1 ≤ N → Φ (N + 1) - Φ N ∈ FF N := by
  have h₀ : LevelInv K E 1 1 := by
    refine ⟨map_one _, fun N hN => ?_⟩
    obtain ⟨Ψ, hK, hGL⟩ := hT.exists_assoc N hN
    refine ⟨Ψ, hK, hGL, ?_⟩
    rw [← Algebra.TensorProduct.one_def]
    exact hK.sub_one_mem_FFK
  obtain ⟨f, -, hf⟩ := exists_seq_of_step (α := F2)
    (fun k a => LevelInv K E (k + 1) a)
    (fun k a b => b - a ∈ FF (k + 1) ∧ AssocU4 (k + 2) (E (k + 2)) b ∧ GL (k + 2) b)
    (a₀ := 1) h₀ (fun k a ha => by
      obtain ⟨x, hx, hA, hG, h'⟩ := levelStep hE (by omega) ha
      exact ⟨a + x, h', by simpa using hx, hA, hG⟩)
  refine ⟨fun N => f (N - 1), fun N hN => ?_, fun N hN => ?_⟩
  · obtain ⟨k, rfl⟩ : ∃ k, N = k + 2 := ⟨N - 2, by omega⟩
    have := (hf k).2
    simpa using this.2
  · obtain ⟨k, rfl⟩ : ∃ k, N = k + 1 := ⟨N - 1, by omega⟩
    simpa using (hf k).2.1

/-- The compatibility hypothesis of `CompatibleGroupLikeKAssociatorTower` is not needed: the
two towers give the same conclusion (here for the constant family `fun _ => E`). -/
theorem rational_associator_compatible_of_tower_via_groupLike {E : F2}
    (hE : FreeAlgebra.algebraMapInv E = 1) (hT : CompatibleGroupLikeKAssociatorTower K E) :
    ∃ Φ : ℕ → F2, (∀ N, 2 ≤ N → AssocU4 N E (Φ N) ∧ GL N (Φ N)) ∧
      ∀ N, 1 ≤ N → Φ (N + 1) - Φ N ∈ FF N :=
  rational_associator_compatible_of_groupLikeTower (expFamily_const hE) hT.toTower

end QOU.BraidsAndKnots.RationalAssociator
