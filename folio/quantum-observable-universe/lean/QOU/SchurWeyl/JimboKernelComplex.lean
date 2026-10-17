import QOU.Mass.KohnoAssembly
import QOU.Mass.IdempotentTraceRigidity
import QOU.SchurWeyl.TraceQuotGeneric

/-!
# The Jimbo action over `ℂ`: kernel = trace radical, image of dimension `catalan`

`JimboActionKernel` proves, over an **ordered** field, that the Jimbo action
`jimbo q : H_{m+1}(q) →ₐ M_{2^{m+1}}` kills exactly the trace radical of the Ocneanu trace
`wtrace` (equivalently: exactly the seminormal blocks with three or more rows), and that its
image has dimension `catalan (m+1)` (over `ℝ`). The one non-formal step there is positivity
of the weighted trace form `X ↦ Tr(K^{⊗N} X Xᵀ)`, which needs a positive `q`.

This file proves the same statements over `ℂ`, for every `q ≠ 0` that is not a root of unity.

## The argument

* **⊆ (formal).** If `jimbo q x = 0` then `jimboTrace q (x y) = 0` for all `y`, and
  `jimboTrace = wtrace` holds over any field (`jimboTrace_eq_wtrace`); so `x` is in the
  radical, and `TraceQuotGeneric.mem_rad_iff_twoRow_blocks_vanish` (any `CharZero` field)
  says its two-row blocks vanish.
* **⊇ (rigidity).** It suffices that every three-row Wedderburn idempotent `E^λ_{TT}` acts by
  zero. Write `q = e^{2πiκ}`. On the set `S` of couplings where the `q²`-integers
  `[d]_{q²}`, `|d| ≤ m`, are distinct, the image `P(κ)` of `E^λ_{TT}` is a fixed polynomial
  in the Jimbo generator matrices (`JMProjector.projFamily`): continuous, and idempotent on
  `S` because generic couplings are dense in it. `S` contains the complement of the countable
  set of root-of-unity couplings, so it is preconnected; the rank of a continuous idempotent
  family is constant on a preconnected set (`IdempotentTraceRigidity`). At the real coupling
  with `q = e` the projector is the complexification of the real one, which vanishes by the
  ordered-field theorem. Hence `rank P(κ) = 0` on all of `S`, i.e. `P(κ) = 0`.

The base-change step needs only that the JM projector, a polynomial in the generators with
coefficients rational in `q`, commutes with a ring homomorphism of coefficients
(`jmProjIn_mapMatrix`).
-/

namespace QOU.SchurWeyl.JimboKernelComplex

open QOU.SchurWeyl QOU.SchurWeyl.JMProjector QOU.SchurWeyl.JimboActionKernel
open QOU.Mass.KohnoAssembly QOU.IwahoriHecke.TensorEmbed
open QOU.Mathlib (StandardYoungTableau partitionShape)
open YoungDiagram SeminormalRep Complex

/-! ## The JM projector commutes with a change of coefficients -/

section BaseChange

variable {K L : Type*} [Field K] [Field L] (f : K →+* L)
  {ι : Type*} [Fintype ι] [DecidableEq ι] {n : ℕ}

theorem qInt2_map (q : K) (c : ℤ) : f (qInt2 q c) = qInt2 (f q) c := by
  unfold qInt2
  split_ifs <;> simp [map_sum, map_pow, map_neg, map_inv₀]

theorem mapMatrix_smul (k : K) (M : Matrix ι ι K) :
    f.mapMatrix (k • M) = f k • f.mapMatrix M := by
  ext i j
  simp

theorem mapMatrix_algebraMap (k : K) :
    f.mapMatrix (algebraMap K (Matrix ι ι K) k) = algebraMap L (Matrix ι ι L) (f k) := by
  rw [Algebra.algebraMap_eq_smul_one, Algebra.algebraMap_eq_smul_one, mapMatrix_smul, map_one]

theorem jmAddIn_mapMatrix (q : K) (g : Fin n → Matrix ι ι K) :
    ∀ k, f.mapMatrix (jmAddIn q g k) = jmAddIn (f q) (fun i => f.mapMatrix (g i)) k
  | 0 => by simp [jmAddIn]
  | k + 1 => by
      by_cases hk : k < n
      · rw [jmAddIn_succ q g hk, jmAddIn_succ (f q) _ hk, map_add, map_mul, map_mul,
          mapMatrix_smul, jmAddIn_mapMatrix q g k, map_inv₀]
      · rw [jmAddIn_succ_of_le q g (by omega), jmAddIn_succ_of_le (f q) _ (by omega),
          jmAddIn_mapMatrix q g k]

theorem jmFactorIn_mapMatrix (q : K) (g : Fin n → Matrix ι ι K) (k : ℕ) (c : ℤ) :
    f.mapMatrix (jmFactorIn q g k c) = jmFactorIn (f q) (fun i => f.mapMatrix (g i)) k c := by
  simp only [jmFactorIn, map_list_prod, List.map_map]
  congr 1
  refine List.map_congr_left fun d _ => ?_
  simp only [Function.comp_apply, mapMatrix_smul, map_sub, mapMatrix_algebraMap,
    jmAddIn_mapMatrix, qInt2_map, map_inv₀]

/-- **The JM projector commutes with change of coefficients.** -/
theorem jmProjIn_mapMatrix (q : K) (g : Fin n → Matrix ι ι K) (c : ℕ → ℤ) :
    f.mapMatrix (jmProjIn q g c) = jmProjIn (f q) (fun i => f.mapMatrix (g i)) c := by
  simp only [jmProjIn, map_list_prod, List.map_map]
  congr 1
  refine List.map_congr_left fun k _ => ?_
  simp only [Function.comp_apply, jmFactorIn_mapMatrix]

end BaseChange

/-- A matrix of rank zero is zero. -/
theorem eq_zero_of_rank_eq_zero {R : Type*} [Field R] {ι : Type*} [Fintype ι] [DecidableEq ι]
    {M : Matrix ι ι R} (h : M.rank = 0) : M = 0 := by
  have h1 : LinearMap.range M.mulVecLin = ⊥ := Submodule.finrank_eq_zero.mp h
  have h2 : M.mulVecLin = 0 := LinearMap.range_eq_bot.mp h1
  ext i j
  have h3 := congrArg (fun F => F (Pi.single j 1) i) h2
  simpa [Matrix.mulVecLin_apply, Matrix.mulVec_single_one] using h3

/-! ## Three-row blocks over an ordered field -/

section Ordered

variable {L : Type*} [Field L] [LinearOrder L] [IsStrictOrderedRing L] [CharZero L]

/-- A partition is *three-row* if its shape has a third row. -/
def ThreeRow {m : ℕ} (lam : Nat.Partition (m + 1)) : Prop := (partitionShape lam).rowLen 2 ≠ 0

/-- Over an ordered field, the Jimbo action kills the whole Wedderburn block of a three-row
partition. -/
theorem jimbo_wedderburn_threeRow_ordered (q : L) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) {lam : Nat.Partition (m + 1)}
    (hlam : ThreeRow lam)
    (M : Matrix (StandardYoungTableau (partitionShape lam))
      (StandardYoungTableau (partitionShape lam)) L) :
    jimbo q hq m ((heckeWedderburn q hq hq2 m).symm (Pi.single lam M)) = 0 := by
  refine jimbo_eq_zero_of_twoRow_blocks_vanish q hq hq2
    (TraceQuotGeneric.hgen_of_notRootOfUnity hq2) m _ fun d hd hrow => ?_
  obtain ⟨mu, rfl⟩ := QOU.Mathlib.exists_partitionShape_eq d hd
  have hne : mu ≠ lam := by
    rintro rfl
    exact hlam hrow
  have h1 : seminormalRep q hq hq2 m hd ((heckeWedderburn q hq hq2 m).symm (Pi.single lam M))
      = heckeWedderburn q hq hq2 m ((heckeWedderburn q hq hq2 m).symm (Pi.single lam M)) mu :=
    rfl
  rw [h1, AlgEquiv.apply_symm_apply, Pi.single_eq_of_ne hne]

end Ordered

/-! ## Rigidity over `ℂ` -/

section Complex

variable {m : ℕ}

/-- Every nonzero complex number is `qC κ = e^{2πiκ}` for some coupling `κ`. -/
theorem exists_qC_eq {q : ℂ} (hq : q ≠ 0) : ∃ κ : ℂ, qC κ = q := by
  refine ⟨Complex.log q / (2 * (Real.pi * I)), ?_⟩
  have h : (2 * (Real.pi * I) : ℂ) ≠ 0 := by
    simp [Real.pi_ne_zero, I_ne_zero]
  unfold qC
  rw [show 2 * (Complex.log q / (2 * (Real.pi * I))) * (Real.pi * I) = Complex.log q by
    field_simp]
  exact Complex.exp_log hq

/-- The real base point: the coupling `kappa 1`, where `q = e`. -/
theorem qC_kappa_one : qC (kappa 1) = ((Real.exp 1 : ℝ) : ℂ) := qOf_eq 1

theorem exp_one_ne_one : Real.exp 1 ≠ 1 := by
  rw [Ne, Real.exp_eq_one_iff]
  exact one_ne_zero

theorem notRootOfUnity_exp_one : GenericParameter.NotRootOfUnity (Real.exp 1) := by
  intro k hk h
  exact exp_one_ne_one ((pow_eq_one_iff_of_nonneg (Real.exp_pos 1).le hk.ne').mp h)

/-- The family of Jimbo actions over the coupling plane. -/
noncomputable abbrev jimboFam (m : ℕ) (κ : ℂ) :
    Hecke ℂ (qC κ) (qC κ)⁻¹ m →ₐ[ℂ] Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ :=
  jimboRep (qC κ) (qC_ne_zero κ) m

/-- **At the real base point the three-row projector vanishes.** -/
theorem projFamily_kappa_one {lam : Nat.Partition (m + 1)} (hlam : ThreeRow lam)
    (T : StandardYoungTableau (partitionShape lam)) :
    projFamily (jimboFam m) T (kappa 1) = 0 := by
  set e : ℝ := Real.exp 1 with he
  have he0 : e ≠ 0 := (Real.exp_pos 1).ne'
  have hreal := jimbo_wedderburn_threeRow_ordered e he0 notRootOfUnity_exp_one m hlam
    (Matrix.single T T 1)
  rw [heckeWedderburn_symm_single, ← jimboRep_eq_jimbo, map_jmProjIn] at hreal
  simp only [jimboRep_σ] at hreal
  have hc := congrArg Complex.ofRealHom.mapMatrix hreal
  rw [jmProjIn_mapMatrix, map_zero] at hc
  simp only [RingHom.mapMatrix_apply, strandBraid_map, map_inv₀, Complex.ofRealHom_eq_coe] at hc
  unfold projFamily
  simp only [jimboFam, jimboRep_σ]
  rw [qC_kappa_one]
  exact hc

/-- **Rigidity.** At every coupling where `q = e^{2πiκ}` is not a root of unity, the
three-row JM projector acts by zero. -/
theorem projFamily_eq_zero {lam : Nat.Partition (m + 1)} (hlam : ThreeRow lam)
    (T : StandardYoungTableau (partitionShape lam)) {κ : ℂ}
    (hκ : GenericParameter.NotRootOfUnity (qC κ)) :
    projFamily (jimboFam m) T κ = 0 := by
  set G : Set ℂ := {κ : ℂ | ¬ GenericParameter.NotRootOfUnity (qC κ)}
  set S : Set ℂ := {κ : ℂ | Set.InjOn (qInt2 (qC κ)) {d | d ∈ contentRange m}}
  have hGc : G.Countable := countable_rootOfUnity_couplings
  have hrank : (1 : Cardinal) < Module.rank ℝ ℂ := by
    rw [Complex.rank_real_complex]; norm_num
  have hGcS : Gᶜ ⊆ S := fun x hx =>
    (qInt2_injective (qC x) (qC_ne_zero x) (by simpa [G] using hx)).injOn
  have hcl : closure Gᶜ = Set.univ := (hGc.dense_compl ℂ).closure_eq
  have hS : IsPreconnected S :=
    (hGc.isPathConnected_compl_of_one_lt_rank hrank).isConnected.isPreconnected.subset_closure
      hGcS (by rw [hcl]; exact Set.subset_univ _)
  have hdense : S ⊆ closure (S ∩ {x | GenericParameter.NotRootOfUnity (qC x)}) := by
    have : Gᶜ ⊆ S ∩ {x | GenericParameter.NotRootOfUnity (qC x)} := fun x hx =>
      ⟨hGcS hx, by simpa [G] using hx⟩
    calc S ⊆ closure Gᶜ := by rw [hcl]; exact Set.subset_univ _
      _ ⊆ _ := closure_mono this
  have h0 : kappa 1 ∈ S := by
    show Set.InjOn (qInt2 (qC (kappa 1))) _
    rw [qC_kappa_one]
    exact (qInt2_injective_ofReal (Real.exp_pos 1)).injOn
  have hκS : κ ∈ S := hGcS (by simpa [G] using hκ)
  have hcont := continuousOn_projFamily (S := S) (jimboFam m) continuous_qC.continuousOn
    (fun x _ => qC_ne_zero x) (fun x hx => hx)
    (fun j => (continuous_jimboRepC_σ j).continuousOn) T
  have hidem := isIdempotentElem_projFamily (S := S) (jimboFam m) continuous_qC.continuousOn
    (fun x _ => qC_ne_zero x) (fun x hx => hx)
    (fun j => (continuous_jimboRepC_σ j).continuousOn) hdense T
  have hr := QOU.Mass.IdempotentTraceRigidity.rank_const_of_isPreconnected hS hcont hidem hκS h0
  rw [projFamily_kappa_one hlam T, Matrix.rank_zero] at hr
  exact eq_zero_of_rank_eq_zero hr

/-- **Over `ℂ`, the Jimbo action kills every three-row Wedderburn matrix unit**, for every
`q ≠ 0` not a root of unity. -/
theorem jimbo_wedderburn_single_threeRow (q : ℂ) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) {lam : Nat.Partition (m + 1)}
    (hlam : ThreeRow lam) (T : StandardYoungTableau (partitionShape lam)) :
    jimbo q hq m ((heckeWedderburn q hq hq2 m).symm (Pi.single lam (Matrix.single T T 1)))
      = 0 := by
  obtain ⟨κ, rfl⟩ := exists_qC_eq hq
  rw [← jimboRep_eq_jimbo]
  have h := projFamily_eq_wedderburn (jimboFam m) T κ (qC_ne_zero κ) hq2
  rw [projFamily_eq_zero hlam T hq2] at h
  exact h

/-- **Over `ℂ`, the Jimbo action kills the whole three-row Wedderburn block.** -/
theorem jimbo_wedderburn_threeRow (q : ℂ) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) {lam : Nat.Partition (m + 1)}
    (hlam : ThreeRow lam)
    (M : Matrix (StandardYoungTableau (partitionShape lam))
      (StandardYoungTableau (partitionShape lam)) ℂ) :
    jimbo q hq m ((heckeWedderburn q hq hq2 m).symm (Pi.single lam M)) = 0 := by
  classical
  have h1 : (1 : Matrix (StandardYoungTableau (partitionShape lam))
      (StandardYoungTableau (partitionShape lam)) ℂ) = ∑ T, Matrix.single T T 1 := by
    ext i j
    rw [Matrix.sum_apply, Matrix.one_apply]
    by_cases hij : i = j
    · subst hij; simp [Matrix.single]
    · rw [if_neg hij]
      symm
      apply Finset.sum_eq_zero
      intro T _
      simp only [Matrix.single, Matrix.of_apply]
      rw [if_neg]
      rintro ⟨rfl, rfl⟩
      exact hij rfl
  have hM : Pi.single lam M
      = (∑ T, Pi.single lam (Matrix.single T T (1 : ℂ))) * Pi.single (M := fun lam =>
          Matrix (StandardYoungTableau (partitionShape lam))
            (StandardYoungTableau (partitionShape lam)) ℂ) lam M := by
    have hs := map_sum (AddMonoidHom.single (fun lam : Nat.Partition (m + 1) =>
        Matrix (StandardYoungTableau (partitionShape lam))
          (StandardYoungTableau (partitionShape lam)) ℂ) lam)
      (fun T => Matrix.single T T (1 : ℂ)) Finset.univ
    simp only [AddMonoidHom.single_apply] at hs
    rw [← hs, ← h1, ← Pi.single_mul, one_mul]
  rw [hM, map_mul, map_mul, map_sum, map_sum]
  rw [Finset.sum_eq_zero fun T _ => jimbo_wedderburn_single_threeRow q hq hq2 hlam T, zero_mul]

/-- **⊇.** An element whose two-row seminormal blocks vanish is killed by the Jimbo action. -/
theorem jimbo_eq_zero_of_twoRow_blocks_vanish_complex (q : ℂ) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (x : Hecke ℂ q q⁻¹ m)
    (hx : ∀ (d : YoungDiagram) (hd : d.cells.card = m + 1), d.rowLen 2 = 0 →
      seminormalRep q hq hq2 m hd x = 0) :
    jimbo q hq m x = 0 := by
  classical
  have hx' : x = (heckeWedderburn q hq hq2 m).symm
      (∑ lam, Pi.single lam (heckeWedderburn q hq hq2 m x lam)) := by
    rw [Finset.univ_sum_single, AlgEquiv.symm_apply_apply]
  rw [hx', map_sum, map_sum]
  refine Finset.sum_eq_zero fun lam _ => ?_
  by_cases hrow : (partitionShape lam).rowLen 2 = 0
  · have h0 : heckeWedderburn q hq hq2 m x lam = 0 :=
      hx _ (partitionShape_card_succ lam) hrow
    rw [h0, Pi.single_zero, map_zero, map_zero]
  · exact jimbo_wedderburn_threeRow q hq hq2 hrow _

/-- **⊆.** If the Jimbo action kills `x`, so does every two-row seminormal block (formal: the
Jimbo trace is `wtrace` over any field). -/
theorem twoRow_blocks_vanish_of_jimbo_eq_zero_complex (q : ℂ) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (x : Hecke ℂ q q⁻¹ m) (h : jimbo q hq m x = 0) :
    ∀ (d : YoungDiagram) (hd : d.cells.card = m + 1), d.rowLen 2 = 0 →
      seminormalRep q hq hq2 m hd x = 0 := by
  refine (TraceQuotGeneric.mem_rad_iff_twoRow_blocks_vanish hq hq2 m x).mp fun b => ?_
  rw [← jimboTrace_eq_wtrace q hq hq2 (TraceQuotGeneric.hq21_of_notRootOfUnity hq2)
    (TraceQuotGeneric.hgen_of_notRootOfUnity hq2), jimboTrace_apply, map_mul, h, zero_mul,
    qtr_zero, mul_zero]

/-- **Kohno comparison at `sl₂` over `ℂ`, kernel form.** For `q ∈ ℂ`, `q ≠ 0` not a root of
unity, the Jimbo action kills `x` exactly when every seminormal block with at most two rows
does. -/
theorem jimbo_eq_zero_iff_twoRow_blocks_vanish_complex (q : ℂ) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (x : Hecke ℂ q q⁻¹ m) :
    jimbo q hq m x = 0 ↔ ∀ (d : YoungDiagram) (hd : d.cells.card = m + 1), d.rowLen 2 = 0 →
      seminormalRep q hq hq2 m hd x = 0 :=
  ⟨twoRow_blocks_vanish_of_jimbo_eq_zero_complex q hq hq2 x,
    jimbo_eq_zero_of_twoRow_blocks_vanish_complex q hq hq2 x⟩

open QOU.QBeta.MarkovTraceQuotient in
/-- **The kernel of the Jimbo action over `ℂ` is the trace radical of `wtrace`**, for every
`q ≠ 0` not a root of unity. -/
theorem ker_jimbo_eq_traceRadicalIdeal_complex (q : ℂ) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) :
    TwoSidedIdeal.ker (jimbo q hq m)
      = traceRadicalIdeal (wtrace q hq hq2 m) (wtrace_cyclic q hq hq2 m) := by
  ext x
  rw [TwoSidedIdeal.mem_ker, mem_traceRadicalIdeal,
    jimbo_eq_zero_iff_twoRow_blocks_vanish_complex q hq hq2,
    ← TraceQuotGeneric.mem_rad_iff_twoRow_blocks_vanish hq hq2 m x]
  rfl

/-- **The kernel of the Jimbo action over `ℂ` is the kernel of the two-row projection.** -/
theorem ker_jimbo_eq_ker_twoRowProduct_complex (q : ℂ) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) :
    LinearMap.ker (jimbo q hq m).toLinearMap
      = LinearMap.ker (TraceQuotGeneric.twoRowProduct q hq hq2 m).toLinearMap := by
  ext x
  simp only [LinearMap.mem_ker, AlgHom.toLinearMap_apply]
  rw [jimbo_eq_zero_iff_twoRow_blocks_vanish_complex q hq hq2,
    ← TraceQuotGeneric.twoRow_blocks_vanish_iff hq hq2 m x]
  have := TraceQuotGeneric.mem_ker_twoRowProduct_iff hq hq2 m x
  rw [TwoSidedIdeal.mem_ker] at this
  exact this.symm

/-- **Dimension of the image of the Jimbo action over `ℂ`** = `∑_{ℓ(λ) ≤ 2} (#SYT λ)²`. -/
theorem finrank_range_jimbo_complex (q : ℂ) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) :
    Module.finrank ℂ (LinearMap.range (jimbo q hq m).toLinearMap)
      = ∑ lam : TraceQuotGeneric.TwoRowIdx m,
          Fintype.card (StandardYoungTableau (partitionShape lam.1))
            * Fintype.card (StandardYoungTableau (partitionShape lam.1)) := by
  haveI := finiteDimensional_hecke q q⁻¹ m
  have h1 := LinearMap.finrank_range_add_finrank_ker (jimbo q hq m).toLinearMap
  have h2 := LinearMap.finrank_range_add_finrank_ker
    (TraceQuotGeneric.twoRowProduct q hq hq2 m).toLinearMap
  have hr : LinearMap.range (TraceQuotGeneric.twoRowProduct q hq hq2 m).toLinearMap = ⊤ :=
    LinearMap.range_eq_top.mpr (TraceQuotGeneric.twoRowProduct_surjective q hq hq2 m)
  rw [hr, finrank_top, Module.finrank_pi_fintype] at h2
  rw [ker_jimbo_eq_ker_twoRowProduct_complex q hq hq2] at h1
  have h3 : Module.finrank ℂ (LinearMap.range (jimbo q hq m).toLinearMap)
      = ∑ lam : TraceQuotGeneric.TwoRowIdx m, Module.finrank ℂ
          (Matrix (StandardYoungTableau (partitionShape lam.1))
            (StandardYoungTableau (partitionShape lam.1)) ℂ) := by omega
  rw [h3]
  refine Finset.sum_congr rfl fun lam _ => ?_
  rw [Module.finrank_matrix, Module.finrank_self, mul_one]

/-- **The image of the Jimbo action over `ℂ` has dimension `catalan (m+1)`**, for every
`q ≠ 0` not a root of unity. -/
theorem finrank_range_jimbo_eq_catalan_complex (q : ℂ) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) :
    Module.finrank ℂ (LinearMap.range (jimbo q hq m).toLinearMap) = catalan (m + 1) := by
  have h := TraceQuotGeneric.finrank_traceQuot_eq_catalan hq hq2 m
  rw [TraceQuotGeneric.finrank_traceQuot hq hq2 m] at h
  rw [finrank_range_jimbo_complex q hq hq2]
  exact_mod_cast h

end Complex

end QOU.SchurWeyl.JimboKernelComplex
