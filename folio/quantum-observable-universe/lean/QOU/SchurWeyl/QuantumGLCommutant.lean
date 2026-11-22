/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.QuantumGLWeights
import QOU.SchurWeyl.QuantumGLHWBound
import Mathlib.LinearAlgebra.BilinearForm.Orthogonal
import Mathlib.LinearAlgebra.Matrix.DotProduct
import Mathlib.LinearAlgebra.FreeModule.Finite.Matrix

/-!
# The commutant of `E_i`, `lowerOp`, Cartan elements and weight projectors on `(K^d)^{⊗n}` is the
# Jimbo image (G3.4)

Bean `qou-gl34`. Scoping: `docs/audits/2026-11-15-gl34-qschur-shortcut-scoping.md`.

Let `B` be the operators `E_i = raiseOp`, `F_i = lowerOp`, the Cartan elements `cartan c` and the
weight projectors `weightProj μ` on `V = (K^d)^{⊗(m+1)}` (`uqGens`), and let `N_μ = hwSpace μ`.

* **F1** `lowerOp_eq_transpose_raiseOp`: `F_i = E_iᵀ`. Both are built by `siteOp` with the same
  tail weight, and `siteTerm` transposes site by site. So `uqGens` is closed under transpose
  (`transpose_mem_uqGens`). Over a linearly ordered field the dot product is anisotropic, so the
  orthogonal complement of an invariant subspace is an invariant complement
  (`isCompl_dotPerp`, `invariant_dotPerp`). This gives complete reducibility without Casimir
  elements or `sl₂` theory.
* **F2** `exists_ne_zero_mem_hwSpace`: a nonzero invariant subspace contains a nonzero
  highest-weight vector (maximise `f(μ) = Σ_x x·μ(x)`; `E_i` raises `f` by one). Hence
  `genClosure_hw_eq_top`: the highest-weight vectors generate `V`.
* **F3** `finrank_commutant_le`: restriction to the `N_μ` is injective on the commutant, so
  `dim B' ≤ Σ_μ (dim N_μ)²`.
* **G3.4** `range_jimbo_eq_commutant`: with the bound (★) `hstar` as an explicit hypothesis,
  `ρ(H_{m+1}(q)) = B'`. (★) is supplied by sibling 7a (draft PRs #7870, #7873).

The weight projectors are among the generators. At generic `q` they are polynomials in the
Cartan elements, so the commutant is unchanged; that identification is not proved here.

## Base ring (§7c)

F1's transpose identities: any commutative ring. `exists_ne_zero_mem_hwSpace` and the commutant
machinery: any field. The complement, generation and dimension statements need a linearly
ordered field, because positivity of the dot product is the mechanism, as in `JimboGL`.

-- Ref: [jimbo1986] M. Jimbo, Lett. Math. Phys. 11 (1986) 247–252.
-/

namespace QOU.SchurWeyl.QuantumGL

open Matrix QOU.SchurWeyl.JimboGL

/-! ## F1: transposes -/

section Transpose

variable {R : Type*} [CommRing R] {d n : ℕ}

theorem siteTerm_transpose (X : Matrix (Fin d) (Fin d) R) (w : Fin d → R) (s : Fin n) :
    (siteTerm X w s)ᵀ = siteTerm Xᵀ w s := by
  ext a b
  simp only [transpose_apply, siteTerm, of_apply]
  by_cases h : ∀ k, k ≠ s → a k = b k
  · have h' : ∀ k, k ≠ s → b k = a k := fun k hk => (h k hk).symm
    rw [if_pos h', if_pos h]
    congr 1
    refine Finset.prod_congr rfl fun k hk => ?_
    rw [h k (ne_of_gt (Finset.mem_Ioi.mp hk))]
  · have h' : ¬ ∀ k, k ≠ s → b k = a k := fun h'' => h fun k hk => (h'' k hk).symm
    rw [if_neg h', if_neg h]

theorem siteOp_transpose (X : Matrix (Fin d) (Fin d) R) (w : Fin d → R) :
    (siteOp X w : Matrix (Fin n → Fin d) (Fin n → Fin d) R)ᵀ = siteOp Xᵀ w := by
  rw [siteOp, siteOp, transpose_sum]
  exact Finset.sum_congr rfl fun s _ => siteTerm_transpose X w s

/-- **F1: `F_i = E_iᵀ`.** -/
theorem lowerOp_eq_transpose_raiseOp (q qi : R) (i j : Fin d) :
    (lowerOp q qi i j : Matrix (Fin n → Fin d) (Fin n → Fin d) R) = (raiseOp q qi i j)ᵀ := by
  rw [raiseOp, lowerOp, siteOp_transpose, transpose_single]

theorem raiseOp_eq_transpose_lowerOp (q qi : R) (i j : Fin d) :
    (raiseOp q qi i j : Matrix (Fin n → Fin d) (Fin n → Fin d) R) = (lowerOp q qi i j)ᵀ := by
  rw [lowerOp_eq_transpose_raiseOp, transpose_transpose]

theorem weightProj_transpose (μ : Fin d → ℕ) :
    (weightProj μ : Matrix (Fin n → Fin d) (Fin n → Fin d) R)ᵀ = weightProj μ :=
  diagonal_transpose _

theorem cartan_transpose (c : Fin d → R) :
    (cartan c : Matrix (Fin n → Fin d) (Fin n → Fin d) R)ᵀ = cartan c :=
  diagonal_transpose _

end Transpose

/-! ## Invariant subspaces and orthogonal complements over an ordered field -/

section Perp

variable {L : Type*} [Field L] {ι : Type*} [Fintype ι]

/-- A submodule invariant under every matrix in `S`. -/
def Invariant (S : Set (Matrix ι ι L)) (W : Submodule L (ι → L)) : Prop :=
  ∀ X ∈ S, ∀ v ∈ W, X *ᵥ v ∈ W

/-- The dot-product orthogonal complement. -/
def dotPerp (W : Submodule L (ι → L)) : Submodule L (ι → L) where
  carrier := {v | ∀ w ∈ W, w ⬝ᵥ v = 0}
  add_mem' {v v'} hv hv' w hw := by rw [dotProduct_add, hv w hw, hv' w hw, add_zero]
  zero_mem' w _ := dotProduct_zero w
  smul_mem' c v hv w hw := by rw [dotProduct_smul, hv w hw, smul_zero]

theorem mem_dotPerp {W : Submodule L (ι → L)} {v : ι → L} :
    v ∈ dotPerp W ↔ ∀ w ∈ W, w ⬝ᵥ v = 0 := Iff.rfl

/-- The dot product as a bilinear form. -/
def dotForm : LinearMap.BilinForm L (ι → L) := dotProductBilin L L

theorem dotPerp_eq (W : Submodule L (ι → L)) :
    dotPerp W = (dotForm (ι := ι)).orthogonal W := by
  ext v
  simp [mem_dotPerp, LinearMap.BilinForm.mem_orthogonal_iff, LinearMap.BilinForm.IsOrtho,
    dotForm]

/-- **The dot-product complement is a complement** (anisotropy over an ordered field). -/
theorem isCompl_dotPerp [LinearOrder L] [IsStrictOrderedRing L] (W : Submodule L (ι → L)) :
    IsCompl W (dotPerp W) := by
  have hrefl : (dotForm (ι := ι)).IsRefl := fun (x y : ι → L) (h : dotForm x y = 0) => by
    change x ⬝ᵥ y = 0 at h
    change y ⬝ᵥ x = 0
    rw [dotProduct_comm]; exact h
  rw [dotPerp_eq, LinearMap.BilinForm.isCompl_orthogonal_iff_disjoint hrefl, ← dotPerp_eq,
    Submodule.disjoint_def]
  intro x hx hx'
  exact dotProduct_self_eq_zero.mp (hx' x hx)

/-- **F1: the complement of an invariant subspace is invariant**, for a transpose-closed `S`. -/
theorem invariant_dotPerp {S : Set (Matrix ι ι L)} (hS : ∀ X ∈ S, Xᵀ ∈ S)
    {W : Submodule L (ι → L)} (hW : Invariant S W) : Invariant S (dotPerp W) := by
  intro X hX v hv w hw
  rw [dotProduct_mulVec, ← mulVec_transpose]
  exact hv _ (hW _ (hS X hX) w hw)

/-- The smallest `S`-invariant submodule containing `N`. -/
def genClosure (S : Set (Matrix ι ι L)) (N : Submodule L (ι → L)) : Submodule L (ι → L) :=
  sInf {W | N ≤ W ∧ Invariant S W}

theorem le_genClosure (S : Set (Matrix ι ι L)) (N : Submodule L (ι → L)) :
    N ≤ genClosure S N :=
  le_sInf fun _ hW => hW.1

theorem invariant_genClosure (S : Set (Matrix ι ι L)) (N : Submodule L (ι → L)) :
    Invariant S (genClosure S N) := by
  intro X hX v hv
  rw [genClosure, Submodule.mem_sInf] at hv ⊢
  exact fun W hW => hW.2 X hX v (hv W hW)

theorem genClosure_le {S : Set (Matrix ι ι L)} {N W : Submodule L (ι → L)} (hN : N ≤ W)
    (hW : Invariant S W) : genClosure S N ≤ W :=
  sInf_le ⟨hN, hW⟩

/-- Matrices commuting with every element of `S`. -/
def commutant (S : Set (Matrix ι ι L)) : Submodule L (Matrix ι ι L) where
  carrier := {Y | ∀ X ∈ S, Y * X = X * Y}
  add_mem' {Y Y'} hY hY' X hX := by rw [add_mul, mul_add, hY X hX, hY' X hX]
  zero_mem' X _ := by rw [zero_mul, mul_zero]
  smul_mem' c Y hY X hX := by rw [smul_mul_assoc, mul_smul_comm, hY X hX]

/-- A commutant element killing `N` kills the invariant closure of `N`. -/
theorem mulVec_eq_zero_of_genClosure {S : Set (Matrix ι ι L)} {N : Submodule L (ι → L)}
    {Y : Matrix ι ι L} (hY : Y ∈ commutant S) (hN : ∀ v ∈ N, Y *ᵥ v = 0) :
    ∀ v ∈ genClosure S N, Y *ᵥ v = 0 := by
  have hle : genClosure S N ≤ LinearMap.ker (Matrix.mulVecLin Y) := by
    refine genClosure_le (fun v hv => hN v hv) ?_
    intro X hX v hv
    rw [LinearMap.mem_ker, Matrix.mulVecLin_apply] at hv ⊢
    rw [mulVec_mulVec, hY X hX, ← mulVec_mulVec, hv, mulVec_zero]
  intro v hv
  simpa using hle hv

end Perp

/-! ## The generators on `(K^d)^{⊗(m+1)}` -/

section Gens

variable {K : Type*} [Field K] {d : ℕ}

/-- The `U_q(gl_d)` operators: `E_i`, `F_i`, every Cartan element and every weight projector. -/
def uqGens (q : K) (m : ℕ) : Set (Matrix (Fin (m + 1) → Fin d) (Fin (m + 1) → Fin d) K) :=
  {X | (∃ i j : Fin d, (j : ℕ) = i + 1 ∧
        (X = raiseOp q q⁻¹ i j ∨ X = lowerOp q q⁻¹ i j)) ∨
      (∃ c : Fin d → K, X = cartan c) ∨ ∃ μ : Fin d → ℕ, X = weightProj μ}

theorem transpose_mem_uqGens {q : K} {m : ℕ} {X : Matrix (Fin (m + 1) → Fin d) _ K}
    (hX : X ∈ uqGens q m) : Xᵀ ∈ uqGens q m := by
  rcases hX with ⟨i, j, hij, rfl | rfl⟩ | ⟨c, rfl⟩ | ⟨μ, rfl⟩
  · exact Or.inl ⟨i, j, hij, Or.inr (lowerOp_eq_transpose_raiseOp _ _ _ _).symm⟩
  · exact Or.inl ⟨i, j, hij, Or.inl (raiseOp_eq_transpose_lowerOp _ _ _ _).symm⟩
  · exact Or.inr (Or.inl ⟨c, cartan_transpose c⟩)
  · exact Or.inr (Or.inr ⟨μ, weightProj_transpose μ⟩)

theorem raiseOp_mem_uqGens (q : K) (m : ℕ) {i j : Fin d} (hij : (j : ℕ) = i + 1) :
    raiseOp q q⁻¹ i j ∈ uqGens (d := d) q m :=
  Or.inl ⟨i, j, hij, Or.inl rfl⟩

theorem weightProj_mem_uqGens (q : K) (m : ℕ) (μ : Fin d → ℕ) :
    weightProj μ ∈ uqGens (d := d) q m :=
  Or.inr (Or.inr ⟨μ, rfl⟩)

theorem sum_weightProj (m : ℕ) :
    ∑ μ ∈ occWeights d m, (weightProj μ : Matrix (Fin (m + 1) → Fin d) _ K) = 1 := by
  classical
  ext a b
  rw [Matrix.sum_apply, Matrix.one_apply]
  simp only [weightProj, Matrix.diagonal_apply]
  by_cases hab : a = b
  · subst hab
    simp only [if_true]
    rw [Finset.sum_ite_eq]
    simp [occWeights]
  · simp [hab]

theorem weightProj_eq_zero_of_not_mem {m : ℕ} {μ : Fin d → ℕ} (hμ : μ ∉ occWeights d m) :
    (weightProj μ : Matrix (Fin (m + 1) → Fin d) _ K) = 0 := by
  ext a b
  simp only [weightProj, Matrix.diagonal_apply, Matrix.zero_apply]
  have : content a ≠ μ := fun h => hμ (h ▸ Finset.mem_image_of_mem _ (Finset.mem_univ a))
  simp [this]

theorem jimbo_mem_commutant (q : K) (hq : q ≠ 0) (m : ℕ) (x : Hecke K q q⁻¹ m) :
    jimbo d q hq m x ∈ commutant (uqGens q m) := by
  rintro X (⟨i, j, hij, rfl | rfl⟩ | ⟨c, rfl⟩ | ⟨μ, rfl⟩)
  · exact jimbo_commute_raise q hq m hij x
  · exact jimbo_commute_lower q hq m hij x
  · exact jimbo_commute_cartan q hq m c x
  · exact jimbo_commute_weightProj q hq m μ x

end Gens

/-! ## F2: highest-weight vectors generate -/

section Generate

variable {L : Type*} [Field L] {d : ℕ}

/-- The potential `Σ_x x·μ(x)`, raised by one by every `E_i`. -/
def potential (μ : Fin d → ℕ) : ℕ := ∑ x : Fin d, (x : ℕ) * μ x

theorem potential_shift {i j : Fin d} (hij : (j : ℕ) = i + 1) {μ ν : Fin d → ℕ}
    (h1 : ν j = μ j + 1) (h2 : ν i + 1 = μ i) (h3 : ∀ x, x ≠ i → x ≠ j → ν x = μ x) :
    potential ν = potential μ + 1 := by
  have hji : j ≠ i := fun e => by rw [e] at hij; omega
  have key : ∀ x : Fin d, (x : ℕ) * ν x + (if x = i then (x : ℕ) else 0)
      = (x : ℕ) * μ x + (if x = j then (x : ℕ) else 0) := by
    intro x
    by_cases hxi : x = i
    · subst hxi; rw [if_pos rfl, if_neg (Ne.symm hji), ← h2]; ring
    · by_cases hxj : x = j
      · subst hxj; rw [if_neg hxi, if_pos rfl, h1]; ring
      · rw [if_neg hxi, if_neg hxj, h3 x hxi hxj]
  have hsum := Finset.sum_congr rfl fun x (_ : x ∈ Finset.univ) => key x
  rw [Finset.sum_add_distrib, Finset.sum_add_distrib, Finset.sum_ite_eq',
    Finset.sum_ite_eq'] at hsum
  simp only [Finset.mem_univ, if_true] at hsum
  unfold potential
  omega

/-- **F2: a nonzero invariant subspace contains a nonzero highest-weight vector.** -/
theorem exists_ne_zero_mem_hwSpace (q : L) (m : ℕ) {W : Submodule L ((Fin (m + 1) → Fin d) → L)}
    (hW : Invariant (uqGens q m) W) (hne : W ≠ ⊥) :
    ∃ μ, ∃ v ∈ W, v ≠ 0 ∧ v ∈ hwSpace q m μ := by
  classical
  -- weights carrying a nonzero vector of `W`
  set T := (occWeights d m).filter
    (fun μ => ∃ v ∈ W, v ≠ 0 ∧ weightProj μ *ᵥ v = v) with hT
  have hTne : T.Nonempty := by
    obtain ⟨v, hvW, hv0⟩ := Submodule.exists_mem_ne_zero_of_ne_bot hne
    by_contra hemp
    rw [Finset.not_nonempty_iff_eq_empty] at hemp
    apply hv0
    have hsplit : v = ∑ μ ∈ occWeights d m, weightProj μ *ᵥ v := by
      rw [← Matrix.sum_mulVec, sum_weightProj, one_mulVec]
    rw [hsplit]
    refine Finset.sum_eq_zero fun μ hμ => ?_
    by_contra hne0
    have hmem : μ ∈ T := by
      rw [hT, Finset.mem_filter]
      refine ⟨hμ, weightProj μ *ᵥ v, hW _ (weightProj_mem_uqGens q m μ) v hvW, hne0, ?_⟩
      rw [mulVec_mulVec, weightProj_mul_self]
    rw [hemp] at hmem; exact absurd hmem (Finset.notMem_empty μ)
  obtain ⟨μ, hμT, hmax⟩ := T.exists_max_image potential hTne
  obtain ⟨-, v, hvW, hv0, hvμ⟩ := (Finset.mem_filter.mp hμT)
  refine ⟨μ, v, hvW, hv0, hvμ, fun i j hij => ?_⟩
  set u := raiseOp q q⁻¹ i j *ᵥ v with hu
  have huW : u ∈ W := hW _ (raiseOp_mem_uqGens q m hij) v hvW
  rw [show u = ∑ ν ∈ occWeights d m, weightProj ν *ᵥ u by
    rw [← Matrix.sum_mulVec, sum_weightProj, one_mulVec]]
  refine Finset.sum_eq_zero fun ν hν => ?_
  by_cases hshift : ν j = μ j + 1 ∧ ν i + 1 = μ i ∧ ∀ x, x ≠ i → x ≠ j → ν x = μ x
  · by_contra hne0
    have hνT : ν ∈ T := by
      rw [hT, Finset.mem_filter]
      refine ⟨hν, weightProj ν *ᵥ u, hW _ (weightProj_mem_uqGens q m ν) u huW, hne0, ?_⟩
      rw [mulVec_mulVec, weightProj_mul_self]
    have := hmax ν hνT
    rw [potential_shift hij hshift.1 hshift.2.1 hshift.2.2] at this
    omega
  · rw [hu, ← hvμ, mulVec_mulVec, mulVec_mulVec,
      weightProj_mul_raiseOp_mul_weightProj q q⁻¹ hij hshift, zero_mulVec]

/-- The span of all highest-weight spaces. -/
def hwAll (q : L) (m : ℕ) : Submodule L ((Fin (m + 1) → Fin d) → L) := ⨆ μ, hwSpace q m μ

/-- **F2: the highest-weight vectors generate `V`.** -/
theorem genClosure_hw_eq_top [LinearOrder L] [IsStrictOrderedRing L] (q : L) (m : ℕ) :
    genClosure (uqGens q m) (hwAll (d := d) q m) = ⊤ := by
  set C := genClosure (uqGens q m) (hwAll (d := d) q m)
  have hC : Invariant (uqGens q m) C := invariant_genClosure _ _
  have hP : Invariant (uqGens q m) (dotPerp C) :=
    invariant_dotPerp (fun X hX => transpose_mem_uqGens hX) hC
  have hbot : dotPerp C = ⊥ := by
    by_contra hne
    obtain ⟨μ, v, hvP, hv0, hvμ⟩ := exists_ne_zero_mem_hwSpace q m hP hne
    have hvC : v ∈ C := le_genClosure _ _ (Submodule.mem_iSup_of_mem μ hvμ)
    exact hv0 ((Submodule.disjoint_def.mp (isCompl_dotPerp C).disjoint) v hvC hvP)
  have := (isCompl_dotPerp C).sup_eq_top
  rwa [hbot, sup_bot_eq] at this

end Generate

/-! ## F3: the dimension bound, and G3.4 -/

section Bound

variable {L : Type*} [Field L] {d : ℕ}

theorem mulVec_mem_hwSpace {q : L} {m : ℕ} {Y : Matrix (Fin (m + 1) → Fin d) _ L}
    (hY : Y ∈ commutant (uqGens q m)) {μ : Fin d → ℕ} {v : (Fin (m + 1) → Fin d) → L}
    (hv : v ∈ hwSpace q m μ) : Y *ᵥ v ∈ hwSpace q m μ := by
  refine ⟨?_, fun i j hij => ?_⟩
  · rw [mulVec_mulVec, ← hY _ (weightProj_mem_uqGens q m μ), ← mulVec_mulVec, hv.1]
  · rw [mulVec_mulVec, ← hY _ (raiseOp_mem_uqGens q m hij), ← mulVec_mulVec, hv.2 i j hij,
      mulVec_zero]

/-- Restriction of a commutant element to the highest-weight spaces. -/
def resHW (q : L) (m : ℕ) :
    commutant (uqGens (d := d) q m) →ₗ[L]
      ((μ : occWeights d m) → (hwSpace q m μ.1 →ₗ[L] hwSpace q m μ.1)) where
  toFun Y μ := (Matrix.mulVecLin Y.1).restrict fun _ hv => mulVec_mem_hwSpace Y.2 hv
  map_add' Y Y' := by
    funext μ; ext v
    simp
  map_smul' c Y := by
    funext μ; ext v
    simp

theorem resHW_injective [LinearOrder L] [IsStrictOrderedRing L] (q : L) (m : ℕ) :
    Function.Injective (resHW (d := d) q m) := by
  classical
  refine (injective_iff_map_eq_zero (resHW (d := d) q m)).mpr ?_
  intro Y hY
  have hN : ∀ v ∈ hwAll (d := d) q m, Y.1 *ᵥ v = 0 := by
    intro v hv
    refine Submodule.iSup_induction (motive := fun v => Y.1 *ᵥ v = 0)
      (fun μ => hwSpace q m μ) hv (fun μ w hw => ?_)
      (mulVec_zero _) (fun x y hx hy => by simp only at hx hy ⊢; rw [mulVec_add, hx, hy, add_zero])
    by_cases hμ : μ ∈ occWeights d m
    · have := congrArg (fun f => ((f ⟨μ, hμ⟩) ⟨w, hw⟩ : (Fin (m + 1) → Fin d) → L)) hY
      simpa [resHW] using this
    · show Y.1 *ᵥ w = 0
      rw [← hw.1, weightProj_eq_zero_of_not_mem hμ, zero_mulVec, mulVec_zero]
  have hall := mulVec_eq_zero_of_genClosure Y.2 hN
  rw [genClosure_hw_eq_top] at hall
  apply Subtype.ext
  ext a b
  have := congrFun (hall (Pi.single b 1) Submodule.mem_top) a
  simpa [mulVec_single_one] using this

/-- **F3: `dim B' ≤ Σ_μ (dim N_μ)²`.** -/
theorem finrank_commutant_le [LinearOrder L] [IsStrictOrderedRing L] (q : L) (m : ℕ) :
    Module.finrank L (commutant (uqGens (d := d) q m))
      ≤ ∑ μ ∈ occWeights d m, Module.finrank L (hwSpace q m μ) ^ 2 := by
  have h := LinearMap.finrank_le_finrank_of_injective (resHW_injective (d := d) q m)
  rw [Module.finrank_pi_fintype] at h
  refine h.trans (le_of_eq ?_)
  rw [← Finset.sum_coe_sort (occWeights d m)]
  refine Finset.sum_congr rfl fun μ _ => ?_
  rw [Module.finrank_linearMap, sq]

open YoungDiagram QOU.Mathlib

/-- **G3.4 from (★)**: the Jimbo image is the full commutant, given the bound (★) as the
hypothesis `hstar`. `range_jimbo_eq_commutant` discharges it with `hstar_occWeights`. -/
theorem range_jimbo_eq_commutant_of_hstar [LinearOrder L] [IsStrictOrderedRing L] [NeZero d]
    (q : L) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ)
    (hstar : ∑ μ ∈ occWeights d m, Module.finrank L (hwSpace q m μ) ^ 2
      ≤ ∑ lam : RowCapIdx d m,
          Fintype.card (StandardYoungTableau (partitionShape lam.1)) ^ 2) :
    LinearMap.range (jimbo d q hq m).toLinearMap = commutant (uqGens q m) := by
  have hle : LinearMap.range (jimbo d q hq m).toLinearMap ≤ commutant (uqGens q m) := by
    rintro _ ⟨x, rfl⟩
    exact jimbo_mem_commutant q hq m x
  refine Submodule.eq_of_le_of_finrank_le hle ?_
  rw [finrank_range_jimbo q hq hq2 m]
  exact (finrank_commutant_le q m).trans hstar

theorem sub_inv_ne_zero_of_notRootOfUnity {q : L} (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) : q - q⁻¹ ≠ 0 := by
  intro h
  have h1 : q = q⁻¹ := sub_eq_zero.mp h
  apply hq2 2 two_pos
  rw [sq]
  nth_rewrite 2 [h1]
  exact mul_inv_cancel₀ hq

/-- **G3.4**: over a linearly ordered field and for `q` not a root of unity, the image of
`H_{m+1}(q)` under the `gl_d` Jimbo action is exactly the commutant of the operators in `uqGens`:
`E_i = raiseOp`, `lowerOp`, the Cartan elements and the weight projectors on `(L^d)^{⊗(m+1)}`.
Scope: this is not yet the commutant of `U_q(gl_d)` itself. That needs (1) the weight projectors to
be polynomials in the Cartan elements at generic `q`, and (2) `lowerOp` and the standard `Δ(F)` to
generate the same algebra with the Cartan elements. Both are open (bean `qou-gl34`). -/
theorem range_jimbo_eq_commutant [LinearOrder L] [IsStrictOrderedRing L] [NeZero d]
    (q : L) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) :
    LinearMap.range (jimbo d q hq m).toLinearMap = commutant (uqGens q m) :=
  range_jimbo_eq_commutant_of_hstar q hq hq2 m
    (hstar_occWeights q hq (sub_inv_ne_zero_of_notRootOfUnity hq hq2) hq2 m)

end Bound

end QOU.SchurWeyl.QuantumGL
