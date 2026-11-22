/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.JimboGL
import QOU.SchurWeyl.QuantumGLHWBranching
import QOU.SchurWeyl.QuantumGLCommutant
import QOU.SchurWeyl.QuantumGLHWDim
import Mathlib.LinearAlgebra.Trace
import Mathlib.LinearAlgebra.Projection

/-!
# Restricting `HW_μ` from `H_{m+2}` to `H_{m+1}`

G3.4c (bean `qou-gl343`), identification steps A, B and C.

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

**Step C.** Taking traces along the exact sequences `0 → P_{x+1} → P_x → HW_{μ − e_x} → 0`
(`trace_eq_add_of_exact`, proved here by choosing a complement) and telescoping gives the
character branching rule

`tr(ι z | HW_μ) = Σ_x tr(z | HW_{μ − e_x})`  (`hwTrace_heckeIncl`).

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

section TraceSES

open LinearMap

variable {K V U W : Type*} [Field K] [AddCommGroup V] [Module K V] [FiniteDimensional K V]
  [AddCommGroup U] [Module K U] [AddCommGroup W] [Module K W]

/-- **Trace is additive along an invariant subspace**: if `f` preserves `P = ker g` and
`g ∘ f = h ∘ g` with `g` onto, then `tr f = tr (f|_P) + tr h`. -/
theorem trace_eq_trace_restrict_add_of_ker (f : V →ₗ[K] V) (P : Submodule K V)
    (hP : ∀ v ∈ P, f v ∈ P) (g : V →ₗ[K] W) (hg : Function.Surjective g)
    (hker : LinearMap.ker g = P) (h : W →ₗ[K] W) (hgh : g ∘ₗ f = h ∘ₗ g) :
    trace K V f = trace K P (f.restrict hP) + trace K W h := by
  obtain ⟨C, hC⟩ := P.exists_isCompl
  set πP := P.linearProjOfIsCompl C hC
  set πC := C.linearProjOfIsCompl P hC.symm
  have hsum : P.subtype ∘ₗ πP + C.subtype ∘ₗ πC = LinearMap.id := by
    ext v
    exact Submodule.IsCompl.projection_add_projection_eq_self hC v
  have hv : ∀ v : V, ((πP v : P) : V) + ((πC v : C) : V) = v := fun v => by
    simpa using congrArg (fun F : V →ₗ[K] V => F v) hsum
  have h1 : trace K V f = trace K V ((f ∘ₗ P.subtype) ∘ₗ πP)
      + trace K V ((f ∘ₗ C.subtype) ∘ₗ πC) := by
    rw [← map_add, LinearMap.comp_assoc, LinearMap.comp_assoc, ← LinearMap.comp_add, hsum,
      LinearMap.comp_id]
  have hres : πP ∘ₗ (f ∘ₗ P.subtype) = f.restrict hP := by
    ext v
    simp only [LinearMap.comp_apply, Submodule.subtype_apply, LinearMap.restrict_coe_apply]
    rw [Submodule.linearProjOfIsCompl_apply_left hC ⟨f v, hP v v.2⟩]
  have hgP : ∀ v ∈ P, g v = 0 := fun v hv => by
    rw [← LinearMap.mem_ker, hker]; exact hv
  have hinj : Function.Injective (g ∘ₗ C.subtype) := by
    rw [← LinearMap.ker_eq_bot, LinearMap.ker_eq_bot']
    intro c hc
    have hcP : (c : V) ∈ P := by rw [← hker]; exact hc
    have : (c : V) ∈ P ⊓ C := ⟨hcP, c.2⟩
    rw [hC.inf_eq_bot, Submodule.mem_bot] at this
    exact Subtype.ext this
  have hgC : ∀ v : V, g ((πC v : C) : V) = g v := fun v => by
    conv_rhs => rw [← hv v]
    rw [map_add, hgP _ (πP v).2, zero_add]
  have hsurj : Function.Surjective (g ∘ₗ C.subtype) := by
    intro w
    obtain ⟨v, rfl⟩ := hg w
    exact ⟨πC v, hgC v⟩
  set e := LinearEquiv.ofBijective (g ∘ₗ C.subtype) ⟨hinj, hsurj⟩
  have hconj : πC ∘ₗ (f ∘ₗ C.subtype) = (e.symm.conj h : C →ₗ[K] C) := by
    refine LinearMap.ext fun c => ?_
    rw [LinearEquiv.conj_apply]
    apply e.injective
    simp only [LinearMap.comp_apply, LinearEquiv.coe_coe, LinearEquiv.apply_symm_apply,
      LinearEquiv.symm_symm]
    show g ((πC (f c) : C) : V) = h (g c)
    rw [hgC, ← LinearMap.comp_apply g f, hgh, LinearMap.comp_apply]
  have t1 : trace K V ((f ∘ₗ P.subtype) ∘ₗ πP) = trace K P (πP ∘ₗ (f ∘ₗ P.subtype)) :=
    trace_comp_comm' _ _
  have t2 : trace K V ((f ∘ₗ C.subtype) ∘ₗ πC) = trace K C (πC ∘ₗ (f ∘ₗ C.subtype)) :=
    trace_comp_comm' _ _
  rw [h1, t1, t2, hres, hconj, LinearMap.trace_conj']

/-- **Trace is additive along a short exact sequence** `0 → U → V → W → 0` of compatible
endomorphisms. -/
theorem trace_eq_add_of_exact (f : V →ₗ[K] V) (i : U →ₗ[K] V) (hi : Function.Injective i)
    (f' : U →ₗ[K] U) (hfi : f ∘ₗ i = i ∘ₗ f') (g : V →ₗ[K] W) (hg : Function.Surjective g)
    (hker : LinearMap.ker g = LinearMap.range i) (h : W →ₗ[K] W) (hgh : g ∘ₗ f = h ∘ₗ g) :
    trace K V f = trace K U f' + trace K W h := by
  haveI : FiniteDimensional K W := Module.Finite.of_surjective g hg
  haveI : FiniteDimensional K U := Module.Finite.of_injective i hi
  have hP : ∀ v ∈ LinearMap.range i, f v ∈ LinearMap.range i := by
    rintro _ ⟨u, rfl⟩
    exact ⟨f' u, by rw [← LinearMap.comp_apply i f', ← hfi, LinearMap.comp_apply]⟩
  rw [trace_eq_trace_restrict_add_of_ker f _ hP g hg hker h hgh]
  congr 1
  set e := LinearEquiv.ofInjective i hi
  have hconj : f.restrict hP = (e.conj f' : _ →ₗ[K] _) := by
    refine LinearMap.ext fun p => ?_
    obtain ⟨u, rfl⟩ := e.surjective p
    rw [LinearEquiv.conj_apply]
    apply Subtype.ext
    simp only [LinearMap.comp_apply, LinearEquiv.coe_coe, LinearEquiv.symm_apply_apply,
      LinearMap.restrict_coe_apply]
    show f (i u) = i (f' u)
    rw [← LinearMap.comp_apply f i, hfi, LinearMap.comp_apply]
  rw [hconj, LinearMap.trace_conj']

end TraceSES

section HWTrace

omit [NeZero d] in
theorem trace_restrict_congr {V : Type*} [AddCommGroup V] [Module K V] (f : V →ₗ[K] V)
    {P Q : Submodule K V} (h : P = Q) (hP : ∀ v ∈ P, f v ∈ P) (hQ : ∀ v ∈ Q, f v ∈ Q) :
    LinearMap.trace K P (f.restrict hP) = LinearMap.trace K Q (f.restrict hQ) := by
  subst h; rfl

/-- The character of `HW_μ`: the trace of `z ∈ H_{m+1}` on the highest-weight space. -/
noncomputable def hwTrace (q : K) (hq : q ≠ 0) (m : ℕ) (μ : Fin d → ℕ)
    (z : Hecke K q q⁻¹ m) : K :=
  LinearMap.trace K (hwSpace q m μ)
    ((Matrix.mulVecLin (jimbo d q hq m z)).restrict fun _ hv =>
      mulVec_mem_hwSpace (jimbo_mem_commutant q hq m z) hv)

/-- The trace of the restricted action `ι z` (`z ∈ H_{m+1}`) on the peel piece `P_k`. -/
noncomputable def peelTrace (q : K) (hq : q ≠ 0) (m : ℕ) (μ : Fin d → ℕ)
    (z : Hecke K q q⁻¹ m) (k : ℕ) : K :=
  LinearMap.trace K (peelSpace q m μ k)
    ((Matrix.mulVecLin (jimbo d q hq (m + 1) (heckeIncl K q q⁻¹ m z))).restrict fun _ hv =>
      jimbo_heckeIncl_mem_peelSpace q hq m μ k z hv)

theorem peelTrace_zero (q : K) (hq : q ≠ 0) (m : ℕ) (μ : Fin d → ℕ) (z : Hecke K q q⁻¹ m) :
    peelTrace q hq m μ z 0 = hwTrace q hq (m + 1) μ (heckeIncl K q q⁻¹ m z) := by
  unfold peelTrace hwTrace
  exact trace_restrict_congr _ (peelSpace_zero q m μ) _ _

theorem peelTrace_d (q : K) (hq : q ≠ 0) (m : ℕ) (μ : Fin d → ℕ) (z : Hecke K q q⁻¹ m) :
    peelTrace q hq m μ z d = 0 := by
  unfold peelTrace
  have h0 : ∀ v : peelSpace q m μ d, v = 0 := fun ⟨w, hw⟩ => Subtype.ext (by
    have hw' : w ∈ peelSpace q m μ d := hw
    rw [peelSpace_d, Submodule.mem_bot] at hw'
    exact hw')
  rw [show ((Matrix.mulVecLin (jimbo d q hq (m + 1) (heckeIncl K q q⁻¹ m z))).restrict
      fun _ hv => jimbo_heckeIncl_mem_peelSpace q hq m μ d z hv) = 0 from
    LinearMap.ext fun v => h0 _, map_zero]

end HWTrace

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

theorem sum_fin_add_last {M : Type*} [AddCommMonoid M] (g : ℕ → M) (n : ℕ) :
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

/-- **One step of the character recursion**: `tr(ι z | P_x) = tr(ι z | P_{x+1}) +
tr(z | HW_{μ − e_x})`, from the `H_{m+1}`-equivariant exact sequence
`0 → P_{x+1} → P_x → HW_{μ − e_x} → 0`. -/
theorem peelTrace_succ (q : L) (hq : q ≠ 0) (hgen : GenericParameter.NotRootOfUnity q)
    (m : ℕ) (μ : Fin d → ℕ) (hμ : IsDom μ) (hsum : ∑ y, μ y = m + 2)
    (z : Hecke L q q⁻¹ m) (x : Fin d) :
    peelTrace q hq m μ z x
      = peelTrace q hq m μ z ((x : ℕ) + 1) + hwTrace q hq m (μ - Pi.single x 1) z := by
  unfold peelTrace hwTrace
  refine trace_eq_add_of_exact _ (Submodule.inclusion (peelSpace_succ_le q m μ x))
    (Submodule.inclusion_injective _) _ ?_ (peelSlice q hq m μ x)
    (peelSlice_surjective q hq hgen m μ hμ hsum x) ?_ _ ?_
  · exact LinearMap.ext fun v => Subtype.ext rfl
  · ext v
    rw [LinearMap.mem_ker, LinearMap.mem_range]
    constructor
    · intro h
      exact ⟨⟨v.1, (mem_peelSpace_succ_iff q m μ v.2).mpr (congrArg Subtype.val h)⟩, rfl⟩
    · rintro ⟨u, rfl⟩
      exact Subtype.ext ((mem_peelSpace_succ_iff q m μ (peelSpace_succ_le q m μ x u.2)).mp u.2)
  · exact LinearMap.ext fun v => Subtype.ext (slice_jimbo_heckeIncl q hq m z v.1 x)

/-- **Branching of characters**: for dominant `μ` of total weight `m + 2` and `z ∈ H_{m+1}`,
`tr(ι z | HW_μ) = Σ_x tr(z | HW_{μ − e_x})`.  (Terms with `μ − e_x` not dominant vanish,
since then `HW_{μ − e_x} = 0`.) -/
theorem hwTrace_heckeIncl (q : L) (hq : q ≠ 0) (hgen : GenericParameter.NotRootOfUnity q)
    (m : ℕ) (μ : Fin d → ℕ) (hμ : IsDom μ) (hsum : ∑ y, μ y = m + 2)
    (z : Hecke L q q⁻¹ m) :
    hwTrace q hq (m + 1) μ (heckeIncl L q q⁻¹ m z)
      = ∑ x : Fin d, hwTrace q hq m (μ - Pi.single x 1) z := by
  rw [← peelTrace_zero]
  set a : ℕ → L := fun k => peelTrace q hq m μ z k with ha
  have htel := sum_fin_add_last a d
  have hstep : ∑ x : Fin d, a x
      = ∑ x : Fin d, a ((x : ℕ) + 1) + ∑ x : Fin d, hwTrace q hq m (μ - Pi.single x 1) z := by
    rw [← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl fun x _ => peelTrace_succ q hq hgen m μ hμ hsum z x
  have hd : a d = 0 := peelTrace_d q hq m μ z
  show a 0 = _
  linear_combination -htel + hstep + hd

end Generic

end QOU.SchurWeyl.QuantumGL
