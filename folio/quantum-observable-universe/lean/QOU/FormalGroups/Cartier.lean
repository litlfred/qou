import QOU.FormalGroups.Distributions
import Mathlib.RingTheory.Bialgebra.Basic
import Mathlib.LinearAlgebra.TensorProduct.Basis

/-!
# The Cartier step: a divided-power bialgebra is `Dist(G)` of a formal group law

Stage 1 of the formalisation of [fred2005, Thm 3.7]
([`thm:skew-poisson-integration`](../../../quantum-observable-universe/models-of-qous/skew-poisson-integration.md)).

Let `U` be a bialgebra over a commutative ring `R` with a basis `b = (δx^J)_{J ∈ ι →₀ ℕ}`
such that `δx^0 = 1` and the coproduct is the divided-power one,
`Δ(δx^J) = Σ_{A + B = J} δx^A ⊗ δx^B`. Write the structure constants as
`δx^A · δx^B = Σ_M c(A, B, M) δx^M` and put

    F_j(X, Y) = Σ_{A, B} c(A, B, e_j) X^A Y^B.

**Theorem (`cartier`).** `F` is a formal group law, and `b.repr : U ≃ Dist(F)` carries the
product of `U` to the convolution of `Dist(F)` and `1` to the unit `δ_0`.

The proof has two halves.

* **Separation (`FormalGroupLaw.ofConv`).** For a tuple `F` with zero constant terms, the
  convolution `⟨μ * ν, f⟩ = ⟨μ ⊠ ν, f(F)⟩` is defined without any axiom on `F`. If it is
  associative and `δ_0` is a two-sided unit, then `F` satisfies the axioms. This is the
  converse of `conv_assoc`, `one_conv`, `conv_one`: pairing with point distributions
  `δ_D` reads off every coefficient of both sides of each axiom.
* **Transport.** The coproduct formula and `Δ(uv) = Δ(u)Δ(v)` give
  `c(A, B, M + N) = Σ c(A₁, B₁, M) c(A₂, B₂, N)`, i.e. the series
  `P_M = Σ c(A, B, M) X^A Y^B` satisfy `P_{M+N} = P_M P_N` and `P_0 = 1` (the second from
  the counit). So `P_M = F^M`, which says exactly `δx^A · δx^B ↦ (δ_A ⊠ δ_B) ∘ F^*`, i.e.
  `b.repr (u v) = b.repr u * b.repr v` in `Dist(F)`. Associativity and units of `U` then
  give the axioms by separation.

Everything is sorry-free and over a general commutative ring.

-- Ref: [fred2005]
-/

namespace QOU.FormalGroups
open MvPowerSeries

noncomputable section

variable {R : Type*} [CommRing R] {ι : Type*} [Finite ι]

/-! ### Convolution for a tuple without axioms -/

section RawConv
variable {F : ι → MvPowerSeries (Fin 2 × ι) R} (hF : NoConst F)

/-- Convolution along a tuple `F` with zero constant terms (no group-law axioms assumed). -/
def convF (μ ν : Dist R ι) : Dist R ι :=
  pullback (hasSubst_of_constantCoeff_zero hF) (tensor2 μ ν)

lemma pair_convF (μ ν : Dist R ι) (f : MvPowerSeries ι R) :
    pair (convF hF μ ν) f = pair (tensor2 μ ν) (subst F f) := pair_pullback _ _ _

lemma conv_eq_convF (G : FormalGroupLaw R ι) : conv G = convF G.noConst := rfl

lemma convF_zero_left (ν : Dist R ι) : convF hF 0 ν = 0 := by
  simp [convF, tensor2]

lemma convF_zero_right (μ : Dist R ι) : convF hF μ 0 = 0 := by
  simp [convF, tensor2]

lemma convF_add_left (μ μ' ν : Dist R ι) :
    convF hF (μ + μ') ν = convF hF μ ν + convF hF μ' ν := by
  simp only [convF, tensor2, tensor_add_left, pullback_add]

lemma convF_add_right (μ ν ν' : Dist R ι) :
    convF hF μ (ν + ν') = convF hF μ ν + convF hF μ ν' := by
  simp only [convF, tensor2, tensor_add_right, pullback_add]

lemma pullback_smul {σ τ : Type*} {a : σ → MvPowerSeries τ R} (ha : HasSubst a) (c : R)
    (μ : Dist R τ) : pullback ha (c • μ) = c • pullback ha μ :=
  ext_pair fun f => by rw [pair_pullback, pair_smul, pair_smul, pair_pullback]

lemma convF_smul_left (c : R) (μ ν : Dist R ι) :
    convF hF (c • μ) ν = c • convF hF μ ν := by
  simp only [convF, tensor2, tensor_smul_left, pullback_smul]

lemma convF_smul_right (c : R) (μ ν : Dist R ι) :
    convF hF μ (c • ν) = c • convF hF μ ν := by
  simp only [convF, tensor2, tensor_smul_right, pullback_smul]

lemma convF_single_single (A B : ι →₀ ℕ) :
    convF hF (Finsupp.single A 1) (Finsupp.single B 1) =
      pullDelta (hasSubst_of_constantCoeff_zero hF)
        (Finsupp.mapDomain (blk 0) A + Finsupp.mapDomain (blk 1) B) := by
  rw [convF, tensor2, tensor_single_single, mul_one, pullback_single, one_smul]

end RawConv

/-! ### Separation: associativity and units of `convF` force the axioms -/

section Separation
variable {F : ι → MvPowerSeries (Fin 2 × ι) R} (hF : NoConst F)

lemma embed_X {σ τ : Type*} [Finite σ] (e : σ → τ) (s : σ) :
    embed e (X s : MvPowerSeries σ R) = X (e s) := by
  rw [embed, subst_X (hasSubst_X_comp e)]

lemma exists_blk0 (D : Fin 1 × ι →₀ ℕ) : ∃ n, Finsupp.mapDomain (blk 0) n = D := by
  obtain ⟨d, n, h⟩ := exists_decomp (i₁ := blk (ι := ι) 0) (i₂ := (Empty.elim : Empty → Fin 1 × ι))
    (fun t => Or.inl ⟨t.2, by obtain ⟨k, i⟩ := t; fin_cases k; rfl⟩) D
  refine ⟨d, ?_⟩
  rw [← h, Subsingleton.elim n 0, Finsupp.mapDomain_zero, add_zero]

lemma coeff_mapDomain_blk0_X (n : ι →₀ ℕ) (j : ι) :
    coeff (Finsupp.mapDomain (blk 0) n) (coords (m := 1) 0 j : MvPowerSeries (Fin 1 × ι) R) =
      coeff n (X j : MvPowerSeries ι R) := by
  show coeff _ (X (blk 0 j)) = _
  rw [← embed_X, coeff_embed_mapDomain (blk_injective 0)]

lemma pair_convF_one_right (μ : Dist R ι) (f : MvPowerSeries ι R) :
    pair (convF hF μ one) f =
      pair (tensor (Empty.elim : Empty → Fin 1 × ι) (blk 0) (Finsupp.single 0 1) μ)
        (subst (fun s => subst2 (coords (m := 1) 0) 0 (F s)) f) := by
  have hb := hasSubst2 (noConst_coords (R := R) (ι := ι) (m := 1) 0) noConst_zero
  rw [pair_convF, tensor2, tensor_comm, ← pullback_zero_empty,
    pair_tensor_pullback hasSubst_zero_empty hb
      (j₁ := (Empty.elim : Empty → Fin 1 × ι)) (j₂ := blk 0)
      (fun s => by simp [blk, embed_zero'])
      (fun k => by simp [coords, blk])
      (blk_injective 1) (blk_injective 0) (blk_disjoint (by decide))
      cover2 (fun x => x.elim) (blk_injective 0) (fun x => x.elim),
    subst_comp_subst_apply (hasSubst_of_constantCoeff_zero hF) hb]
  rfl

lemma pair_convF_one_left (μ : Dist R ι) (f : MvPowerSeries ι R) :
    pair (convF hF one μ) f =
      pair (tensor (Empty.elim : Empty → Fin 1 × ι) (blk 0) (Finsupp.single 0 1) μ)
        (subst (fun s => subst2 0 (coords (m := 1) 0) (F s)) f) := by
  have hb := hasSubst2 (noConst_zero (R := R) (ι := ι) (τ := Fin 1 × ι)) (noConst_coords 0)
  rw [pair_convF, tensor2, ← pullback_zero_empty,
    pair_tensor_pullback hasSubst_zero_empty hb
      (j₁ := (Empty.elim : Empty → Fin 1 × ι)) (j₂ := blk 0)
      (fun s => by simp [blk, embed_zero'])
      (fun k => by simp [coords, blk])
      (blk_injective 0) (blk_injective 1) (blk_disjoint (by decide))
      (fun t => (cover2 t).symm) (fun x => x.elim) (blk_injective 0) (fun x => x.elim),
    subst_comp_subst_apply (hasSubst_of_constantCoeff_zero hF) hb]
  rfl

/-- Reading off coefficients of a one-block tuple from its pairings with `δ_0 ⊠ δ_n`. -/
lemma unit_of_pair {V : ι → MvPowerSeries (Fin 1 × ι) R} (hV : NoConst V)
    (h : ∀ (n : ι →₀ ℕ) (j : ι),
      pair (tensor (Empty.elim : Empty → Fin 1 × ι) (blk 0) (Finsupp.single 0 1)
        (Finsupp.single n 1)) (subst V (X j : MvPowerSeries ι R)) = coeff n (X j : MvPowerSeries ι R)) :
    V = coords (m := 1) 0 := by
  funext j
  ext D
  obtain ⟨n, rfl⟩ := exists_blk0 D
  have e := h n j
  rw [subst_X (hasSubst_of_constantCoeff_zero hV), tensor_single_single, mul_one,
    Finsupp.mapDomain_zero, zero_add, pair_single, one_mul] at e
  rw [e, coeff_mapDomain_blk0_X]

lemma unitLeft_of_convF (h : ∀ n : ι →₀ ℕ, convF hF (Finsupp.single n 1) one = Finsupp.single n 1) :
    (fun j => subst2 (coords 0) 0 (F j)) = (coords (m := 1) 0 : ι → MvPowerSeries _ R) := by
  refine unit_of_pair (noConst_subst2 (noConst_coords 0) noConst_zero hF) fun n j => ?_
  rw [← pair_convF_one_right hF, h n, pair_single, one_mul]

lemma unitRight_of_convF (h : ∀ n : ι →₀ ℕ, convF hF one (Finsupp.single n 1) = Finsupp.single n 1) :
    (fun j => subst2 0 (coords 0) (F j)) = (coords (m := 1) 0 : ι → MvPowerSeries _ R) := by
  refine unit_of_pair (noConst_subst2 noConst_zero (noConst_coords 0) hF) fun n j => ?_
  rw [← pair_convF_one_left hF, h n, pair_single, one_mul]

lemma pair_convF_assoc_left (μ ν ρ : Dist R ι) (f : MvPowerSeries ι R) :
    pair (convF hF (convF hF μ ν) ρ) f =
      pair (tensor J₁ (blk 2) (tensor2 μ ν) ρ)
        (subst (fun s => subst2 (fun i => subst2 (coords (m := 3) 0) (coords 1) (F i))
          (coords 2) (F s)) f) := by
  have hu : NoConst (fun i => subst2 (coords (m := 3) 0) (coords 1) (F i)) :=
    noConst_subst2 (noConst_coords 0) (noConst_coords 1) hF
  have hbL := hasSubst2 hu (noConst_coords (m := 3) 2)
  rw [pair_convF, tensor2, convF,
    pair_tensor_pullback (hasSubst_of_constantCoeff_zero hF) hbL
      (fun s => by simp only [blk, Matrix.cons_val_zero]; exact subst2_coords01 _)
      (fun k => by simp [coords, blk])
      (blk_injective 0) (blk_injective 1) (blk_disjoint (by decide))
      (fun t => (cover2 t).symm) J₁_injective (blk_injective 2)
      (fun x y h => by obtain ⟨k, i⟩ := x; fin_cases k <;> simp [J₁, blk] at h),
    subst_comp_subst_apply (hasSubst_of_constantCoeff_zero hF) hbL]
  rfl

lemma pair_convF_assoc_right (μ ν ρ : Dist R ι) (f : MvPowerSeries ι R) :
    pair (convF hF μ (convF hF ν ρ)) f =
      pair (tensor J₁ (blk 2) (tensor2 μ ν) ρ)
        (subst (fun s => subst2 (coords (m := 3) 0)
          (fun i => subst2 (coords 1) (coords 2) (F i)) (F s)) f) := by
  have hv : NoConst (fun i => subst2 (coords (m := 3) 1) (coords 2) (F i)) :=
    noConst_subst2 (noConst_coords 1) (noConst_coords 2) hF
  have hbR := hasSubst2 (noConst_coords (m := 3) 0) hv
  rw [tensor3_eq, pair_convF, tensor2, convF, tensor_comm,
    pair_tensor_pullback (hasSubst_of_constantCoeff_zero hF) hbR
      (fun s => by simp only [blk, Matrix.cons_val_one]; exact subst2_coords12 _)
      (fun k => by simp [coords, blk])
      (blk_injective 1) (blk_injective 0) (blk_disjoint (by decide))
      cover2 K₁_injective (blk_injective 0)
      (fun x y h => by obtain ⟨k, i⟩ := x; fin_cases k <;> simp [K₁, blk] at h),
    subst_comp_subst_apply (hasSubst_of_constantCoeff_zero hF) hbR]
  rfl

omit [Finite ι] in
lemma cover3 (t : Fin 3 × ι) : (∃ s, J₁ s = t) ∨ (∃ k, blk 2 k = t) := by
  obtain ⟨k, i⟩ := t; fin_cases k
  · exact Or.inl ⟨(0, i), rfl⟩
  · exact Or.inl ⟨(1, i), rfl⟩
  · exact Or.inr ⟨i, rfl⟩

/-- Reading off coefficients of a three-block tuple from its pairings with
`δ_a ⊠ δ_b ⊠ δ_c`. -/
lemma eq_of_pair3 {V W : ι → MvPowerSeries (Fin 3 × ι) R} (hV : NoConst V) (hW : NoConst W)
    (h : ∀ (a b c : ι →₀ ℕ) (j : ι),
      pair (tensor J₁ (blk 2) (tensor2 (Finsupp.single a 1) (Finsupp.single b 1))
        (Finsupp.single c 1)) (subst V (X j : MvPowerSeries ι R)) =
      pair (tensor J₁ (blk 2) (tensor2 (Finsupp.single a 1) (Finsupp.single b 1))
        (Finsupp.single c 1)) (subst W (X j : MvPowerSeries ι R))) :
    V = W := by
  funext j
  ext D
  obtain ⟨d, c, rfl⟩ := exists_decomp cover3 D
  obtain ⟨b, a, rfl⟩ := exists_decomp (fun t => cover2 t) d
  have e := h a b c j
  rw [subst_X (hasSubst_of_constantCoeff_zero hV), subst_X (hasSubst_of_constantCoeff_zero hW),
    tensor2, tensor_single_single, tensor_single_single, mul_one, mul_one, pair_single,
    pair_single, one_mul, one_mul] at e
  rwa [add_comm (Finsupp.mapDomain (blk 1) b)]

lemma assoc_of_convF (h : ∀ μ ν ρ : Dist R ι,
      convF hF (convF hF μ ν) ρ = convF hF μ (convF hF ν ρ)) :
    (fun j => subst2 (fun i => subst2 (coords 0) (coords 1) (F i)) (coords 2) (F j)) =
      (fun j => subst2 (coords (m := 3) 0) (fun i => subst2 (coords 1) (coords 2) (F i)) (F j)) := by
  have hu : NoConst (fun i => subst2 (coords (m := 3) 0) (coords 1) (F i)) :=
    noConst_subst2 (noConst_coords 0) (noConst_coords 1) hF
  have hv : NoConst (fun i => subst2 (coords (m := 3) 1) (coords 2) (F i)) :=
    noConst_subst2 (noConst_coords 1) (noConst_coords 2) hF
  refine eq_of_pair3 (noConst_subst2 hu (noConst_coords 2) hF)
    (noConst_subst2 (noConst_coords 0) hv hF) fun a b c j => ?_
  rw [← pair_convF_assoc_left hF, ← pair_convF_assoc_right hF, h]

/-- **Separation.** A tuple with zero constant terms whose convolution is associative with
two-sided unit `δ_0` is a formal group law. -/
def FormalGroupLaw.ofConv
    (hassoc : ∀ μ ν ρ : Dist R ι, convF hF (convF hF μ ν) ρ = convF hF μ (convF hF ν ρ))
    (hone_left : ∀ n : ι →₀ ℕ, convF hF one (Finsupp.single n 1) = Finsupp.single n 1)
    (hone_right : ∀ n : ι →₀ ℕ, convF hF (Finsupp.single n 1) one = Finsupp.single n 1) :
    FormalGroupLaw R ι where
  F := F
  noConst := hF
  unit_left := unitLeft_of_convF hF hone_right
  unit_right := unitRight_of_convF hF hone_left
  assoc := assoc_of_convF hF hassoc

end Separation

/-! ### Splitting multi-indices on two blocks -/

section Split

/-- The `k`-th block of a multi-index on `Fin 2 × ι`. -/
def split (k : Fin 2) (D : Fin 2 × ι →₀ ℕ) : ι →₀ ℕ :=
  D.comapDomain (blk k) (blk_injective k).injOn

/-- The multi-index on `Fin 2 × ι` with blocks `A`, `B`. -/
def join (A B : ι →₀ ℕ) : Fin 2 × ι →₀ ℕ :=
  Finsupp.mapDomain (blk 0) A + Finsupp.mapDomain (blk 1) B

@[simp] lemma split_apply (k : Fin 2) (D : Fin 2 × ι →₀ ℕ) (i : ι) : split k D i = D (k, i) :=
  Finsupp.comapDomain_apply _ _ _ _

@[simp] lemma join_apply_zero (A B : ι →₀ ℕ) (i : ι) : join A B (0, i) = A i := by
  rw [join, Finsupp.add_apply, show ((0 : Fin 2), i) = blk 0 i from rfl,
    Finsupp.mapDomain_apply (blk_injective 0),
    Finsupp.mapDomain_notin_range _ _ (by rintro ⟨x, hx⟩; exact blk_disjoint (by decide) x i hx),
    add_zero]

@[simp] lemma join_apply_one (A B : ι →₀ ℕ) (i : ι) : join A B (1, i) = B i := by
  rw [join, Finsupp.add_apply, show ((1 : Fin 2), i) = blk 1 i from rfl,
    Finsupp.mapDomain_apply (blk_injective 1),
    Finsupp.mapDomain_notin_range _ _ (by rintro ⟨x, hx⟩; exact blk_disjoint (by decide) x i hx),
    zero_add]

lemma split_join_zero (A B : ι →₀ ℕ) : split 0 (join A B) = A := by ext i; simp

lemma split_join_one (A B : ι →₀ ℕ) : split 1 (join A B) = B := by ext i; simp

lemma join_split (D : Fin 2 × ι →₀ ℕ) : join (split 0 D) (split 1 D) = D := by
  ext ⟨k, i⟩; fin_cases k <;> simp

lemma join_add (A B A' B' : ι →₀ ℕ) : join (A + A') (B + B') = join A B + join A' B' := by
  ext ⟨k, i⟩; fin_cases k <;> simp

lemma split_add (k : Fin 2) (D D' : Fin 2 × ι →₀ ℕ) : split k (D + D') = split k D + split k D' := by
  ext i; simp

end Split

/-! ### The Cartier step -/

section Cartier
variable [DecidableEq ι] {U : Type*} [Ring U] [Bialgebra R U] (b : Module.Basis (ι →₀ ℕ) R U)
  (hΔ : ∀ J, Coalgebra.comul (R := R) (b J) = ∑ p ∈ Finset.antidiagonal J, b p.1 ⊗ₜ[R] b p.2)

open Coalgebra TensorProduct

include hΔ in
lemma repr_comul (w : U) (M N : ι →₀ ℕ) :
    (b.tensorProduct b).repr (comul (R := R) w) (M, N) = b.repr w (M + N) := by
  classical
  have hb : ∀ J, (b.tensorProduct b).repr (comul (R := R) (b J)) (M, N) = b.repr (b J) (M + N) := by
    intro J
    have hp : ∀ p : (ι →₀ ℕ) × (ι →₀ ℕ),
        (b.tensorProduct b).repr (b p.1 ⊗ₜ[R] b p.2) (M, N) = if p = (M, N) then 1 else 0 := by
      rintro ⟨A, B⟩
      rw [Module.Basis.tensorProduct_repr_tmul_apply, Module.Basis.repr_self,
        Module.Basis.repr_self, Finsupp.single_apply, Finsupp.single_apply, smul_eq_mul]
      by_cases hA : A = M <;> by_cases hB : B = N <;> simp [hA, hB]
    rw [hΔ, map_sum, Finsupp.finset_sum_apply, Module.Basis.repr_self, Finsupp.single_apply]
    simp only [hp, Finset.sum_ite_eq', Finset.mem_antidiagonal]
    by_cases h : M + N = J
    · simp [h]
    · rw [if_neg h, if_neg (Ne.symm h)]
  have := b.ext (f₁ := (Finsupp.lapply (M, N)) ∘ₗ (b.tensorProduct b).repr.toLinearMap ∘ₗ comul)
    (f₂ := Finsupp.lapply (M + N) ∘ₗ b.repr.toLinearMap) hb
  exact LinearMap.congr_fun this w

include hΔ in
/-- The counit on the basis: `ε(δx^J) = [J = 0]`. -/
lemma counit_basis (J : ι →₀ ℕ) : counit (R := R) (b J) = if J = 0 then 1 else 0 := by
  classical
  have h := congrArg (fun x => b.repr (TensorProduct.lid R U x) 0)
    (rTensor_counit_comul (R := R) (b J))
  simp only [hΔ, map_sum, LinearMap.rTensor_tmul, TensorProduct.lid_tmul,
    Finsupp.finset_sum_apply, map_smul, Finsupp.smul_apply, Module.Basis.repr_self,
    Finsupp.single_apply, smul_eq_mul, one_smul] at h
  rw [Finset.sum_eq_single (J, 0)] at h
  · simpa using h
  · rintro ⟨A, B⟩ hp hne
    by_cases hB : B = 0
    · subst hB
      rw [Finset.mem_antidiagonal, add_zero] at hp
      exact absurd (by rw [← hp]) hne
    · simp [hB]
  · intro h; exact absurd (Finset.mem_antidiagonal.mpr (add_zero J)) h

include hΔ in
lemma counit_eq_repr (w : U) : counit (R := R) w = b.repr w 0 := by
  have := b.ext (f₁ := counit (R := R) (A := U)) (f₂ := Finsupp.lapply 0 ∘ₗ b.repr.toLinearMap)
    fun J => by
      simp only [LinearMap.coe_comp, Function.comp_apply, LinearEquiv.coe_coe,
        Finsupp.lapply_apply, Module.Basis.repr_self, Finsupp.single_apply, counit_basis b hΔ]
  exact LinearMap.congr_fun this w

include hΔ in
/-- Structure constants under the coproduct:
`c(A, B, M + N) = Σ_{A₁+A₂=A} Σ_{B₁+B₂=B} c(A₁, B₁, M) c(A₂, B₂, N)`. -/
lemma repr_mul_add (A B M N : ι →₀ ℕ) :
    b.repr (b A * b B) (M + N) = ∑ p ∈ Finset.antidiagonal A, ∑ q ∈ Finset.antidiagonal B,
      b.repr (b p.1 * b q.1) M * b.repr (b p.2 * b q.2) N := by
  rw [← repr_comul b hΔ, Bialgebra.comul_mul, hΔ, hΔ, Finset.sum_mul_sum, map_sum,
    Finsupp.finset_sum_apply]
  refine Finset.sum_congr rfl fun p _ => ?_
  rw [map_sum, Finsupp.finset_sum_apply]
  refine Finset.sum_congr rfl fun q _ => ?_
  rw [Algebra.TensorProduct.tmul_mul_tmul, Module.Basis.tensorProduct_repr_tmul_apply,
    smul_eq_mul, mul_comm]

/-- `P_M = Σ_{A, B} c(A, B, M) X^A Y^B`. -/
def cartierP (M : ι →₀ ℕ) : MvPowerSeries (Fin 2 × ι) R :=
  fun D => b.repr (b (split 0 D) * b (split 1 D)) M

lemma coeff_cartierP (M : ι →₀ ℕ) (D : Fin 2 × ι →₀ ℕ) :
    coeff D (cartierP b M) = b.repr (b (split 0 D) * b (split 1 D)) M := rfl

include hΔ in
lemma cartierP_add (M N : ι →₀ ℕ) : cartierP b (M + N) = cartierP b M * cartierP b N := by
  ext D
  rw [coeff_mul, coeff_cartierP, repr_mul_add b hΔ, ← Finset.sum_product']
  refine Finset.sum_nbij' (fun x => (join x.1.1 x.2.1, join x.1.2 x.2.2))
    (fun y => ((split 0 y.1, split 0 y.2), (split 1 y.1, split 1 y.2))) ?_ ?_ ?_ ?_ ?_
  · rintro ⟨⟨a₁, a₂⟩, ⟨b₁, b₂⟩⟩ h
    simp only [Finset.mem_product, Finset.mem_antidiagonal] at h ⊢
    rw [← join_add, h.1, h.2, join_split]
  · rintro ⟨D₁, D₂⟩ h
    simp only [Finset.mem_product, Finset.mem_antidiagonal] at h ⊢
    rw [← split_add, ← split_add, h]; exact ⟨rfl, rfl⟩
  · rintro ⟨⟨a₁, a₂⟩, ⟨b₁, b₂⟩⟩ _
    simp only [split_join_zero, split_join_one]
  · rintro ⟨D₁, D₂⟩ _
    simp only [join_split]
  · rintro ⟨⟨a₁, a₂⟩, ⟨b₁, b₂⟩⟩ _
    simp only [coeff_cartierP, split_join_zero, split_join_one]

include hΔ in
lemma cartierP_zero : cartierP b 0 = 1 := by
  ext D
  rw [coeff_cartierP, ← counit_eq_repr b hΔ, Bialgebra.counit_mul, counit_basis b hΔ,
    counit_basis b hΔ, coeff_one]
  have hD : D = 0 ↔ split 0 D = 0 ∧ split 1 D = 0 := by
    constructor
    · rintro rfl; exact ⟨by ext; simp, by ext; simp⟩
    · rintro ⟨h0, h1⟩; rw [← join_split D, h0, h1]; simp [join]
  by_cases h0 : split 0 D = 0 <;> by_cases h1 : split 1 D = 0 <;> simp [h0, h1, hD]

/-- The Cartier tuple `F_j = P_{e_j} = Σ_{A, B} c(A, B, e_j) X^A Y^B`. -/
def cartierF : ι → MvPowerSeries (Fin 2 × ι) R := fun j => cartierP b (Finsupp.single j 1)

lemma cartierF_noConst (hb0 : b 0 = 1) : NoConst (cartierF b) := fun j => by
  have s0 : ∀ k : Fin 2, split (ι := ι) k 0 = 0 := fun k => by ext; simp
  rw [← coeff_zero_eq_constantCoeff_apply, cartierF, coeff_cartierP, s0, s0, hb0, mul_one,
    ← hb0, Module.Basis.repr_self, Finsupp.single_apply,
    if_neg (Finsupp.single_ne_zero.mpr one_ne_zero).symm]

include hΔ in
lemma cartierP_single (j : ι) (n : ℕ) : cartierP b (Finsupp.single j n) = cartierF b j ^ n := by
  induction n with
  | zero => rw [Finsupp.single_zero, cartierP_zero b hΔ, pow_zero]
  | succ n ih => rw [Finsupp.single_add, cartierP_add b hΔ, ih, pow_succ]; rfl

include hΔ in
lemma prod_cartierF (M : ι →₀ ℕ) : (M.prod fun j n => cartierF b j ^ n) = cartierP b M := by
  induction M using Finsupp.induction_linear with
  | zero => rw [Finsupp.prod_zero_index, cartierP_zero b hΔ]
  | add M M' h h' =>
    rw [Finsupp.prod_add_index' (fun _ => pow_zero _) (fun _ _ _ => pow_add _ _ _), h, h',
      cartierP_add b hΔ]
  | single j n =>
    rw [Finsupp.prod_single_index (h := fun j n => cartierF b j ^ n) (pow_zero _),
      cartierP_single b hΔ]

include hΔ in
lemma repr_basis_mul (hb0 : b 0 = 1) (A B : ι →₀ ℕ) :
    b.repr (b A * b B) =
      convF (cartierF_noConst b hb0) (Finsupp.single A 1) (Finsupp.single B 1) := by
  rw [convF_single_single]
  ext M
  rw [pullDelta_apply, prod_cartierF b hΔ, coeff_cartierP]
  change _ = b.repr (b (split 0 (join A B)) * b (split 1 (join A B))) M
  rw [split_join_zero, split_join_one]

include hΔ in
/-- **Transport.** `b.repr` carries the product of `U` to the convolution along `F`. -/
theorem repr_mul (hb0 : b 0 = 1) (u v : U) :
    b.repr (u * v) = convF (cartierF_noConst b hb0) (b.repr u) (b.repr v) := by
  have key : ∀ c d : (ι →₀ ℕ) →₀ R, b.repr (b.repr.symm c * b.repr.symm d) =
      convF (cartierF_noConst b hb0) c d := by
    intro c d
    induction c using Finsupp.induction_linear with
    | zero => simp [convF_zero_left]
    | add c c' h h' => rw [map_add, add_mul, map_add, h, h', convF_add_left]
    | single A a =>
      induction d using Finsupp.induction_linear with
      | zero => simp [convF_zero_right]
      | add d d' h h' => rw [map_add, mul_add, map_add, h, h', convF_add_right]
      | single B c' =>
        rw [Module.Basis.repr_symm_single, Module.Basis.repr_symm_single, smul_mul_assoc,
          mul_smul_comm, map_smul, map_smul, repr_basis_mul b hΔ hb0,
          ← Finsupp.smul_single_one A a, ← Finsupp.smul_single_one B c', convF_smul_left,
          convF_smul_right, smul_smul]
  simpa using key (b.repr u) (b.repr v)

include hΔ in
/-- **Cartier step of [fred2005, Thm 3.7].** A bialgebra `U` with a basis `δx^J` such that
`δx^0 = 1` and `Δ(δx^J) = Σ_{A+B=J} δx^A ⊗ δx^B` is the distribution algebra of a formal
group law: the tuple `F_j = Σ c(A, B, e_j) X^A Y^B` built from its structure constants is a
formal group law, and `b.repr : U ≃ Dist(F)` is multiplicative and unital. -/
theorem cartier (hb0 : b 0 = 1) :
    ∃ G : FormalGroupLaw R ι, G.F = cartierF b ∧
      (∀ u v : U, b.repr (u * v) = conv G (b.repr u) (b.repr v)) ∧ b.repr 1 = one := by
  have hF := cartierF_noConst b hb0
  have hm : ∀ μ ν : Dist R ι, convF hF μ ν = b.repr (b.repr.symm μ * b.repr.symm ν) :=
    fun μ ν => by rw [repr_mul b hΔ hb0]; simp
  have h1 : b.repr 1 = (one : Dist R ι) := by rw [← hb0, Module.Basis.repr_self]; rfl
  refine ⟨FormalGroupLaw.ofConv hF (fun μ ν ρ => ?_) (fun n => ?_) (fun n => ?_), rfl,
    fun u v => repr_mul b hΔ hb0 u v, h1⟩
  · simp only [hm, LinearEquiv.symm_apply_apply, mul_assoc]
  · rw [← h1, hm]; simp
  · rw [← h1, hm]; simp

end Cartier

end
end QOU.FormalGroups
