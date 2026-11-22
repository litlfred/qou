/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.JimboGL
import QOU.SchurWeyl.QuantumGLHWBranching
import QOU.SchurWeyl.QuantumGLCommutant
import QOU.SchurWeyl.QuantumGLHWDim

/-!
# Restricting `HW_μ` from `H_{m+2}` to `H_{m+1}`

G3.4c (bean `qou-gl343`), identification steps A and B.

**Step A.** Restrict the Jimbo action of `H_{m+2}` to `H_{m+1}` along `heckeIncl`.  The restricted
operator is `X ⊗ 1` on the last tensor factor (`jimbo_heckeIncl`), so it acts on each last-letter
slice `v_y(a) = v(a y)` separately:

`(ρ_{m+2}(ι x) v)_y = ρ_{m+1}(x) v_y`  (`slice_jimbo_heckeIncl`).

**Step B.** Hence the peel filtration `HW_μ = P_0 ⊇ P_1 ⊇ … ⊇ P_d = 0` of
`QuantumGLHWBranching` (`P_x` = highest-weight vectors whose slices below `x` vanish) is stable
under `H_{m+1}` (`jimbo_heckeIncl_mem_peelSpace`), and the `x`-slice `P_x → HW_{μ − e_x}` is
`H_{m+1}`-equivariant with kernel `P_{x+1}` (`finrank_ker_peelSlice`).  Since `dim HW = f` and
`f^μ = Σ_{corners} f^{μ − □}`, the branching bound is an equality (`finrank_hwSpace_succ_eq`),
and every slice is onto (`peelSlice_surjective`).  So `P_x / P_{x+1} ≅ HW_{μ − e_x}` as
`H_{m+1}`-modules.

## Base ring (§7c)

Steps A and B up to `finrank_ker_peelSlice`: any field, `q ≠ 0`.  The equality and
surjectivity use `dim HW = f`, so they need a linearly ordered field and `q` not a root of unity.
-/

namespace QOU.SchurWeyl.QuantumGL

open QOU.SchurWeyl.JimboGL QOU.SchurWeyl.HeckeInclusion Matrix

variable {K : Type*} [Field K] {d : ℕ} [NeZero d]

/-- **`X ⊗ 1` acts slice by slice.** -/
theorem slice_extLast_mulVec {N : ℕ} (X : Matrix (Fin N → Fin d) (Fin N → Fin d) K)
    (v : (Fin (N + 1) → Fin d) → K) (y : Fin d) :
    slice (extLast N X *ᵥ v) y = X *ᵥ slice v y := by
  classical
  funext a
  show ∑ b, extLast N X (Fin.snoc (α := fun _ => Fin d) a y) b * v b
    = ∑ b, X a b * v (Fin.snoc (α := fun _ => Fin d) b y)
  rw [sum_snoc]
  refine Finset.sum_congr rfl fun b _ => ?_
  rw [Finset.sum_eq_single y]
  · rw [extLast_snoc, if_pos rfl, mul_one]
  · intro x _ hx
    rw [extLast_snoc, if_neg (Ne.symm hx), mul_zero, zero_mul]
  · intro h; exact absurd (Finset.mem_univ y) h

/-- **Slices are `H_{m+1}`-equivariant** for the restricted Jimbo action. -/
theorem slice_jimbo_heckeIncl (q : K) (hq : q ≠ 0) (m : ℕ) (x : Hecke K q q⁻¹ m)
    (v : (Fin (m + 1 + 1) → Fin d) → K) (y : Fin d) :
    slice (jimbo d q hq (m + 1) (heckeIncl K q q⁻¹ m x) *ᵥ v) y
      = jimbo d q hq m x *ᵥ slice v y := by
  rw [jimbo_heckeIncl, slice_extLast_mulVec]

/-- **The peel filtration is `H_{m+1}`-stable**: the restricted action preserves each `P_x`. -/
theorem jimbo_heckeIncl_mem_peelSpace (q : K) (hq : q ≠ 0) (m : ℕ) (μ : Fin d → ℕ) (x : ℕ)
    (z : Hecke K q q⁻¹ m) {v : (Fin (m + 2) → Fin d) → K} (hv : v ∈ peelSpace q m μ x) :
    jimbo d q hq (m + 1) (heckeIncl K q q⁻¹ m z) *ᵥ v ∈ peelSpace q m μ x :=
  ⟨mulVec_mem_hwSpace (jimbo_mem_commutant q hq (m + 1) _) hv.1, fun y hy => by
    rw [slice_jimbo_heckeIncl, hv.2 y hy, mulVec_zero]⟩

omit [NeZero d] in
/-- **The kernel of the `x`-slice on `P_x` is `P_{x+1}`.** -/
theorem mem_peelSpace_succ_iff (q : K) (m : ℕ) (μ : Fin d → ℕ) {x : Fin d}
    {v : (Fin (m + 2) → Fin d) → K} (hv : v ∈ peelSpace q m μ x) :
    v ∈ peelSpace q m μ ((x : ℕ) + 1) ↔ slice v x = 0 := by
  refine ⟨fun h => h.2 x (Nat.lt_succ_self _), fun h => ⟨hv.1, fun y hy => ?_⟩⟩
  rcases Nat.lt_succ_iff_lt_or_eq.mp hy with hy | hy
  · exact hv.2 y hy
  · rw [show y = x from Fin.ext hy]; exact h

omit [NeZero d] in
theorem peelSpace_succ_le (q : K) (m : ℕ) (μ : Fin d → ℕ) (x : ℕ) :
    peelSpace q m μ (x + 1) ≤ peelSpace q m μ x :=
  fun _ hv => ⟨hv.1, fun y hy => hv.2 y (Nat.lt_succ_of_lt hy)⟩

omit [NeZero d] in
/-- The `x`-slice of `P_x`, landing in `HW_{μ − e_x}`. -/
def peelSlice (q : K) (hq : q ≠ 0) (m : ℕ) (μ : Fin d → ℕ) (x : Fin d) :
    peelSpace q m μ x →ₗ[K] hwSpace q m (μ - Pi.single x 1) where
  toFun v := ⟨slice v.1 x, slice_mem_hwSpace q hq m μ v.2⟩
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

omit [NeZero d] in
theorem finrank_ker_peelSlice (q : K) (hq : q ≠ 0) (m : ℕ) (μ : Fin d → ℕ) (x : Fin d) :
    Module.finrank K (LinearMap.ker (peelSlice q hq m μ x))
      = Module.finrank K (peelSpace q m μ ((x : ℕ) + 1)) := by
  have hker : LinearMap.ker (peelSlice q hq m μ x)
      = (peelSpace q m μ ((x : ℕ) + 1)).comap (peelSpace q m μ x).subtype := by
    ext v
    rw [LinearMap.mem_ker, Submodule.mem_comap, Submodule.subtype_apply,
      mem_peelSpace_succ_iff q m μ v.2]
    exact ⟨fun h => congrArg Subtype.val h, fun h => Subtype.ext h⟩
  rw [hker]
  exact LinearEquiv.finrank_eq (Submodule.comapSubtypeEquivOfLe (peelSpace_succ_le q m μ x))

section Generic

variable {L : Type*} [Field L] [LinearOrder L] [IsStrictOrderedRing L] {d : ℕ} [NeZero d]

/-- **Branching is an equality**: `dim HW_μ(m+1) = Σ_x dim HW_{μ − e_x}(m)` for dominant `μ` of
total weight `m + 2`. -/
theorem finrank_hwSpace_succ_eq (q : L) (hq : q ≠ 0) (hgen : GenericParameter.NotRootOfUnity q)
    (m : ℕ) (μ : Fin d → ℕ) (hμ : IsDom μ) (hsum : ∑ y, μ y = m + 2) :
    Module.finrank L (hwSpace q (m + 1) μ)
      = ∑ x : Fin d, Module.finrank L (hwSpace q m (μ - Pi.single x 1)) := by
  have hq2 := sub_inv_ne_zero_of_notRootOfUnity hq hgen
  refine le_antisymm (finrank_hwSpace_succ_le q hq m μ) ?_
  rw [finrank_hwSpace_eq_numSYT q hq hgen (m + 1) μ hμ hsum]
  exact sum_finrank_hwSpace_sub_le_numSYT q hq hq2 hgen m μ hμ hsum
    (finrank_hwSpace_le_numSYT q hq hq2 hgen m)

theorem sum_fin_add_last (g : ℕ → ℕ) (n : ℕ) :
    ∑ x : Fin n, g x + g n = g 0 + ∑ x : Fin n, g ((x : ℕ) + 1) := by
  rw [Fin.sum_univ_eq_sum_range (fun k => g k) n,
    Fin.sum_univ_eq_sum_range (fun k => g (k + 1)) n, ← Finset.sum_range_succ,
    Finset.sum_range_succ', add_comm]

/-- **Every graded piece of the peel filtration is all of `HW_{μ − e_x}`**: the `x`-slice
`P_x → HW_{μ − e_x}` is onto. -/
theorem peelSlice_surjective (q : L) (hq : q ≠ 0) (hgen : GenericParameter.NotRootOfUnity q)
    (m : ℕ) (μ : Fin d → ℕ) (hμ : IsDom μ) (hsum : ∑ y, μ y = m + 2) (x : Fin d) :
    Function.Surjective (peelSlice q hq m μ x) := by
  classical
  set a : ℕ → ℕ := fun k => Module.finrank L (peelSpace q m μ k) with ha
  set b : Fin d → ℕ := fun x => Module.finrank L (hwSpace q m (μ - Pi.single x 1)) with hb
  set r : Fin d → ℕ := fun x => Module.finrank L (LinearMap.range (peelSlice q hq m μ x)) with hr
  have hrk : ∀ x : Fin d, a x = a ((x : ℕ) + 1) + r x := fun x => by
    have := LinearMap.finrank_range_add_finrank_ker (peelSlice q hq m μ x)
    rw [finrank_ker_peelSlice] at this
    simp only [ha, hr]; omega
  have hrb : ∀ x : Fin d, r x ≤ b x := fun x => Submodule.finrank_le _
  have h0 : a 0 = ∑ x, b x := by
    simp only [ha, hb]
    rw [peelSpace_zero]; exact finrank_hwSpace_succ_eq q hq hgen m μ hμ hsum
  have hd : a d = 0 := by simp only [ha]; rw [peelSpace_d, finrank_bot]
  have htel := sum_fin_add_last a d
  have hle : ∀ x ∈ (Finset.univ : Finset (Fin d)), a x ≤ a ((x : ℕ) + 1) + b x := fun x _ => by
    rw [hrk x]; exact Nat.add_le_add_left (hrb x) _
  have hsumeq : ∑ x : Fin d, a x = ∑ x : Fin d, (a ((x : ℕ) + 1) + b x) := by
    rw [Finset.sum_add_distrib, ← h0]; omega
  have hx := (Finset.sum_eq_sum_iff_of_le hle).mp hsumeq x (Finset.mem_univ _)
  have hrx : r x = b x := by have := hrk x; omega
  rw [← LinearMap.range_eq_top]
  exact Submodule.eq_top_of_finrank_eq hrx

end Generic

end QOU.SchurWeyl.QuantumGL
