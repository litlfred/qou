import QOU.Mass.KohnoAssembly
import QOU.IwahoriHecke.BraidGroup
import QOU.IwahoriHecke.QuantumTrace

/-!
# The weighted trace of the KZ holonomy is the weighted trace of Jimbo's R-matrix action

`QOU.Mass.KohnoAssembly.kz_conj_jimbo_complex` gives an invertible `U` with
`U · KZ(h) = Jimbo(h) · U`. An arbitrary `U` does not transport a *weighted* trace
`Tr(D · X)`, `D = K^{⊗n}`. This file supplies the missing step, which is what the mass identity
(`QOU.Torsion.MassTraceMarkov`, PR #7632) consumes.

* **Both families preserve total weight.** The weight of a basis vector `a : Fin N → Fin 2` of
  `V^{⊗N}` is `cnt a = Σ_s a_s`. The permutation action preserves it, hence so does every KZ
  coefficient and, by uniqueness for the transport ODE, every KZ transport
  (`commute_kzBraidRep`: anything commuting with `ρ(S_N)` commutes with the KZ holonomy). The
  Jimbo `Ř` preserves it entrywise (`cnt_eq_of_embedPair_ne_zero`).
* **Rigidity runs on each weight space separately** (`resHom`, `trace_res_kz_eq_jimbo`): the
  restrictions to `V_k = span{a : cnt a = k}` are again two continuous families of
  representations of `H_{N}(q)`, equal at `κ = 0`, hence conjugate at every `κ` with `q` not a
  root of unity; so their traces agree.
* **Weighted traces agree** (`weighted_trace_kz_eq_jimbo`): for every `D = diag(f(cnt a))`,
  `Tr(D · KZ(h)) = Tr(D · Jimbo(h))`. The site weight `K^{⊗N}`, `K = diag(w₀, w₁)`, is such a
  `D` (`siteWeight_eq_diag_cnt`).
* **The mass identity on the KZ side** (`braidTrace_eq_kz`): the normalised Markov trace of a
  braid (`QOU.IwahoriHecke.BraidGroup.braidTrace`, the left side of
  `MassTraceMarkov.braidTrace_wordBraid`) equals `wi^{m+1} · Tr(K^{⊗(m+1)} · KZ(x_β))`, where
  `x_β ∈ H_{m+1}(q)` is the braid's image and `KZ` the continuous KZ holonomy representation.

Scope: every complex coupling `κ` with `q = e^{2πiκ}` not a root of unity, every weight `w`.
-/

namespace QOU.Mass.KohnoWeighted

open QOU.Mass.KohnoAssembly QOU.IwahoriHecke.TensorEmbed QOU.IwahoriHecke.RMatrix
open QOU.SchurWeyl QOU.Mass.KZHolonomy QOU.Mass.BraidHeckeFactor QOU.MathlibExt.Braid
open Complex Set Matrix

/-! ## KZ equivariance -/

section Equivariance

variable {A : Type*} [NormedRing A] [NormedAlgebra ℂ A] [CompleteSpace A]

omit [CompleteSpace A] in
theorem commute_kzForm {n : ℕ} (ρ : Equiv.Perm (Fin n) →* A) (κ c : ℂ) {Z : A}
    (hZ : ∀ σ, Commute Z (ρ σ)) (z u : Fin n → ℂ) : Commute Z (kzForm ρ κ c z u) := by
  rw [kzForm_apply, kzOp]
  refine Commute.smul_right ?_ κ
  refine Commute.sum_right _ _ _ fun a _ => Commute.sum_right _ _ _ fun b _ => ?_
  exact ((hZ _).sub_right (Algebra.commute_algebraMap_right c Z)).smul_right _

variable {m : ℕ} (ρ : Equiv.Perm (Fin (m + 1)) →* A) (κ c : ℂ)

/-- Anything commuting with the permutation action commutes with every KZ transport: both
`Z U(t)` and `U(t) Z` solve the transport equation with initial value `Z`. -/
theorem commute_genFund {Z : A} (hZ : ∀ σ, Commute Z (ρ σ)) (j : Fin m) {t : ℝ}
    (ht : t ∈ Icc (0 : ℝ) 1) : Commute Z (genFund ρ κ c j t) := by
  have hU := genFund_spec ρ κ c j
  unfold IsTransport IsFundSol at hU
  have hX := continuousOn_genCoeff ρ κ c j
  have h := linear_eqOn_of_hasDerivWithinAt hX
    (W := fun t => Z * genFund ρ κ c j t) (W' := fun t => genFund ρ κ c j t * Z)
    (fun t ht => by
      have := (hU.2 t ht).const_mul Z
      convert this using 1
      rw [← mul_assoc, ← mul_assoc, (commute_kzForm ρ κ c hZ _ _).eq])
    (fun t ht => by
      have := (hU.2 t ht).mul_const Z
      convert this using 1
      rw [mul_assoc])
    (by simp [hU.1])
  exact h ht

/-- **KZ equivariance.** Anything commuting with `ρ(S_{m+1})` commutes with the whole KZ
holonomy representation. -/
theorem commute_kzBraidRep {Z : A} (hZ : ∀ σ, Commute Z (ρ σ)) (b : BraidGroup m) :
    Commute Z (kzBraidRep ρ κ c b : A) := by
  let H : Subgroup (BraidGroup m) :=
    { carrier := {b | Commute Z (kzBraidRep ρ κ c b : A)}
      mul_mem' := fun {a b} ha hb => by
        simpa only [Set.mem_setOf_eq, map_mul, Units.val_mul] using ha.mul_right hb
      one_mem' := by simp
      inv_mem' := fun {a} ha => by
        simpa only [Set.mem_setOf_eq, map_inv] using ha.units_inv_right }
  have hgen : ∀ j : Fin m, PresentedGroup.of j ∈ H := fun j => by
    show Commute Z (kzBraidRep ρ κ c (σ j) : A)
    rw [kzBraidRep_σ]
    exact (hZ _).mul_right (commute_genFund ρ κ c hZ j ⟨zero_le_one, le_rfl⟩)
  exact PresentedGroup.generated_by _ H hgen b

end Equivariance

/-- Everything in the image of a map out of `H_m(q)` lies in any subalgebra containing the
generator images. -/
theorem hecke_mem {K : Type*} [CommRing K] {q qi : K} {m : ℕ} {B : Type*} [Ring B] [Algebra K B]
    (φ : Hecke K q qi m →ₐ[K] B) (S : Subalgebra K B) (h : ∀ j, φ (Hecke.σ K q qi m j) ∈ S)
    (x : Hecke K q qi m) : φ x ∈ S := by
  have hx : x ∈ Algebra.adjoin K (Set.range (Hecke.σ K q qi m)) := by
    rw [HeckeInclusion.adjoin_range_σ_eq_top K q qi m]; trivial
  have h2 : φ x ∈ (Algebra.adjoin K (Set.range (Hecke.σ K q qi m))).map φ :=
    Subalgebra.mem_map.mpr ⟨x, hx, rfl⟩
  rw [AlgHom.map_adjoin] at h2
  refine Algebra.adjoin_le ?_ h2
  rintro _ ⟨_, ⟨i, rfl⟩, rfl⟩
  exact h i

/-! ## Total weight on `V^{⊗N}` -/

section Weight

variable {N : ℕ}

/-- The total weight of a basis vector: the number of sites in state `1`. -/
def cnt (a : Fin N → Fin 2) : ℕ := ∑ s, ((a s : Fin 2) : ℕ)

theorem cnt_le (a : Fin N → Fin 2) : cnt a ≤ N := by
  unfold cnt
  calc ∑ s, ((a s : Fin 2) : ℕ) ≤ ∑ _s : Fin N, 1 :=
        Finset.sum_le_sum fun s _ => Nat.lt_succ_iff.mp (a s).isLt
    _ = N := by simp

theorem cnt_comp_perm (a : Fin N → Fin 2) (σ : Equiv.Perm (Fin N)) : cnt (a ∘ σ) = cnt a :=
  Equiv.sum_comp σ (fun s => ((a s : Fin 2) : ℕ))

theorem cnt_eq_of_embedPair_ne_zero {K : Type*} [Field K] {q qi : K} {i j : Fin N} (hij : i ≠ j)
    {a b : Fin N → Fin 2} (h : embedPair i j (rCheck q qi) a b ≠ 0) : cnt a = cnt b := by
  classical
  rw [embedPair_apply] at h
  by_cases hab : ∀ k, k ≠ i → k ≠ j → a k = b k
  · rw [if_pos hab] at h
    have hpair : ((a i : Fin 2) : ℕ) + ((a j : Fin 2) : ℕ) = ((b i : Fin 2) : ℕ) + ((b j : Fin 2) : ℕ) := by
      rcases JimboActionKernel.rCheck_ne_zero h with e | e
      · simp only [Prod.ext_iff] at e; rw [e.1, e.2]
      · simp only [Prod.ext_iff] at e; rw [e.1, e.2, add_comm]
    unfold cnt
    rw [← Finset.sum_add_sum_compl {i, j} (fun s => ((a s : Fin 2) : ℕ)),
      ← Finset.sum_add_sum_compl {i, j} (fun s => ((b s : Fin 2) : ℕ)),
      Finset.sum_pair hij, Finset.sum_pair hij, hpair]
    congr 1
    refine Finset.sum_congr rfl fun s hs => ?_
    simp only [Finset.mem_compl, Finset.mem_insert, Finset.mem_singleton, not_or] at hs
    rw [hab s hs.1 hs.2]
  · rw [if_neg hab] at h; exact absurd rfl h

/-- `X` preserves total weight: its entries vanish between basis vectors of different weight. -/
def WP (X : Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ) : Prop :=
  ∀ a b, cnt a ≠ cnt b → X a b = 0

/-- The weight-preserving matrices form a subalgebra. -/
def wpSub (N : ℕ) : Subalgebra ℂ (Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ) where
  carrier := {X | WP X}
  mul_mem' := by
    intro X Y hX hY a b hab
    rw [Matrix.mul_apply]
    refine Finset.sum_eq_zero fun c _ => ?_
    by_cases hac : cnt a = cnt c
    · rw [hY c b (hac ▸ hab), mul_zero]
    · rw [hX a c hac, zero_mul]
  add_mem' := by
    intro X Y hX hY a b hab
    rw [Matrix.add_apply, hX a b hab, hY a b hab, add_zero]
  algebraMap_mem' := by
    intro r a b hab
    have hne : a ≠ b := fun h => hab (by rw [h])
    show (algebraMap ℂ (Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ) r) a b = 0
    rw [Algebra.algebraMap_eq_smul_one, Matrix.smul_apply, Matrix.one_apply_ne hne, smul_zero]

/-- The projector onto the weight-`k` subspace `V_k`. -/
def wproj (N k : ℕ) : Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ :=
  Matrix.diagonal fun a => if cnt a = k then 1 else 0

theorem commute_wproj_of_WP {X : Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ} (hX : WP X) (k : ℕ) :
    Commute (wproj N k) X := by
  show wproj N k * X = X * wproj N k
  ext a b
  rw [wproj, Matrix.diagonal_mul, Matrix.mul_diagonal]
  by_cases hab : cnt a = cnt b
  · rw [hab]; ring
  · rw [hX a b hab]; ring

theorem WP_of_commute_wproj {X : Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ}
    (h : ∀ k, Commute (wproj N k) X) : WP X := by
  intro a b hab
  have e := congrFun (congrFun (h (cnt a)).eq a) b
  rw [wproj, Matrix.diagonal_mul, Matrix.mul_diagonal, if_pos rfl, if_neg (Ne.symm hab)] at e
  simpa using e

theorem WP_permRep (σ : Equiv.Perm (Fin N)) : WP (permRep σ : Matrix _ _ ℂ) := by
  intro a b hab
  rw [permRep_apply, if_neg]
  rintro rfl
  exact hab (cnt_comp_perm a σ).symm

theorem WP_strandBraid {m : ℕ} (q : ℂ) (j : Fin m) :
    WP (strandBraid q q⁻¹ j) := by
  intro a b hab
  by_contra h
  exact hab (cnt_eq_of_embedPair_ne_zero (by simp [Fin.ext_iff]) h)

end Weight

/-! ## Restriction to a weight space -/

section Restrict

variable {N : ℕ} (k : ℕ)

/-- The weight-`k` basis vectors. -/
abbrev Wt (N k : ℕ) := {a : Fin N → Fin 2 // cnt a = k}

/-- Restriction of a matrix to `V_k`. -/
def res (X : Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ) : Matrix (Wt N k) (Wt N k) ℂ :=
  X.submatrix Subtype.val Subtype.val

theorem res_mul {X : Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ} (hX : WP X)
    (Y : Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ) : res k (X * Y) = res k X * res k Y := by
  ext a b
  simp only [res, Matrix.submatrix_apply, Matrix.mul_apply]
  rw [← Finset.sum_filter_of_ne (p := fun c => cnt c = k)]
  · exact Finset.sum_subtype _ (fun c => by simp) (fun c => X a.1 c * Y c b.1)
  · intro c _ hc
    by_contra hck
    exact hc (by rw [hX a.1 c (by rw [a.2]; exact Ne.symm hck), zero_mul])

/-- The restriction to `V_k` of a weight-preserving representation. -/
noncomputable def resHom {B : Type*} [Ring B] [Algebra ℂ B]
    (φ : B →ₐ[ℂ] Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ) (h : ∀ x, WP (φ x)) :
    B →ₐ[ℂ] Matrix (Wt N k) (Wt N k) ℂ where
  toFun x := res k (φ x)
  map_one' := by
    ext a b
    simp [res, Matrix.one_apply, Subtype.ext_iff]
  map_mul' x y := by rw [map_mul, res_mul k (h x)]
  map_zero' := by ext a b; simp [res]
  map_add' x y := by ext a b; simp [res]
  commutes' r := by
    ext a b
    simp [res, Algebra.algebraMap_eq_smul_one, Matrix.one_apply, Subtype.ext_iff]

@[simp] theorem resHom_apply {B : Type*} [Ring B] [Algebra ℂ B]
    (φ : B →ₐ[ℂ] Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ) (h : ∀ x, WP (φ x)) (x : B) :
    resHom k φ h x = res k (φ x) := rfl

theorem continuous_res {X : Type*} [TopologicalSpace X]
    {F : X → Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ} (hF : Continuous F) :
    Continuous fun x => res k (F x) :=
  hF.matrix_submatrix _ _

/-- **Weighted traces split over weight spaces.** -/
theorem trace_diag_mul (f : ℕ → ℂ) (X : Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ) :
    (Matrix.diagonal (fun a => f (cnt a)) * X).trace =
      ∑ k ∈ Finset.range (N + 1), f k * (res k X).trace := by
  simp only [Matrix.trace, Matrix.diag, Matrix.diagonal_mul]
  rw [← Finset.sum_fiberwise_of_maps_to (g := cnt) (t := Finset.range (N + 1))
    (fun a _ => Finset.mem_range.mpr (Nat.lt_succ_of_le (cnt_le a)))]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [Finset.mul_sum]
  simp only [res, Matrix.submatrix_apply]
  rw [← Finset.sum_subtype (Finset.univ.filter fun a => cnt a = k) (fun a => by simp)
    (fun a => f k * X a a)]
  refine Finset.sum_congr rfl fun a ha => ?_
  rw [(Finset.mem_filter.mp ha).2]

end Restrict

theorem trace_eq_of_conj {M : Type*} [Fintype M] [DecidableEq M] {A B : Matrix M M ℂ}
    (U : (Matrix M M ℂ)ˣ) (h : (U : Matrix M M ℂ) * A = B * U) : A.trace = B.trace := by
  have hB : B = (U : Matrix M M ℂ) * A * ((U⁻¹ : (Matrix M M ℂ)ˣ) : Matrix M M ℂ) := by
    rw [h, mul_assoc, Units.mul_inv, mul_one]
  rw [hB, Matrix.trace_mul_comm, ← mul_assoc, Units.inv_mul, one_mul]

/-! ## Rigidity for two families over the complex coupling plane -/

section Rigid

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

variable {n : ℕ} {M : Type*} [Fintype M] [DecidableEq M]

/-- Two families of representations of `H_{n+1}(q(κ))` on `ℂ^M`, with generator matrices
continuous in `κ` and equal at `κ = 0`, are conjugate at every `κ` with `q(κ)` not a root of
unity. (The argument of `kz_conj_jimbo_complex`, for arbitrary families.) -/
theorem conj_of_eq_at_zero (ρ ρ' : ∀ κ : ℂ, Hecke ℂ (qC κ) (qC κ)⁻¹ n →ₐ[ℂ] Matrix M M ℂ)
    (hρ : ∀ j, Continuous fun κ => ρ κ (Hecke.σ ℂ (qC κ) (qC κ)⁻¹ n j))
    (hρ' : ∀ j, Continuous fun κ => ρ' κ (Hecke.σ ℂ (qC κ) (qC κ)⁻¹ n j))
    (h0 : ∀ j, ρ 0 (Hecke.σ ℂ (qC 0) (qC 0)⁻¹ n j) = ρ' 0 (Hecke.σ ℂ (qC 0) (qC 0)⁻¹ n j))
    {κ : ℂ} (hκ : GenericParameter.NotRootOfUnity (qC κ)) :
    ∃ U : (Matrix M M ℂ)ˣ, ∀ h, (U : Matrix M M ℂ) * ρ κ h = ρ' κ h * U := by
  set G : Set ℂ := {κ : ℂ | ¬ GenericParameter.NotRootOfUnity (qC κ)}
  set S : Set ℂ := {κ : ℂ | Set.InjOn (JMProjector.qInt2 (qC κ)) {d | d ∈ JMProjector.contentRange n}}
  have hGc : G.Countable := countable_rootOfUnity_couplings
  have hrank : (1 : Cardinal) < Module.rank ℝ ℂ := by
    rw [Complex.rank_real_complex]; norm_num
  have hGcS : Gᶜ ⊆ S := fun x hx =>
    (JMProjector.qInt2_injective (qC x) (qC_ne_zero x) (by simpa [G] using hx)).injOn
  have hcl : closure Gᶜ = Set.univ := (hGc.dense_compl ℂ).closure_eq
  have hS : IsPreconnected S :=
    (hGc.isPathConnected_compl_of_one_lt_rank hrank).isConnected.isPreconnected.subset_closure
      hGcS (by rw [hcl]; exact Set.subset_univ _)
  have hdense : S ⊆ closure (S ∩ {x | GenericParameter.NotRootOfUnity (qC x)}) := by
    have : Gᶜ ⊆ S ∩ {x | GenericParameter.NotRootOfUnity (qC x)} := fun x hx =>
      ⟨hGcS hx, by simpa [G] using hx⟩
    calc S ⊆ closure Gᶜ := by rw [hcl]; exact Set.subset_univ _
      _ ⊆ _ := closure_mono this
  have hz : (0 : ℂ) ∈ S := by
    show Set.InjOn (JMProjector.qInt2 (qC 0)) _
    rw [qC_zero]
    exact (JMProjector.qInt2_one_injective (K := ℂ)).injOn
  have hκS : κ ∈ S := hGcS (by simpa [G] using hκ)
  exact conj_of_isPreconnected_hecke hS continuous_qC.continuousOn
    (fun x _ => qC_ne_zero x) (fun x hx => hx) hdense ρ ρ'
    (fun j => (hρ j).continuousOn) (fun j => (hρ' j).continuousOn)
    (fun _ => Classical.arbitrary _) (x₀ := 0) hz 1
    (fun j => by rw [h0 j]; simp) hκS hκ

end Rigid

/-! ## The weighted trace identity -/

section Main

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

variable {m : ℕ}

theorem WP_kzBraidRep (κ c : ℂ) (b : BraidGroup m) :
    WP ((kzBraidRep (permRep (R := ℂ) (k := m + 1)) κ c b :
      (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ) :
      Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ) :=
  WP_of_commute_wproj fun k =>
    commute_kzBraidRep (A := Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)
      (permRep (R := ℂ) (k := m + 1)) κ c
      (fun σ => commute_wproj_of_WP (WP_permRep σ) k) b

theorem WP_kzHeckeC (c κ : ℂ) (x : Hecke ℂ (qC κ) (qC κ)⁻¹ m) : WP (kzHeckeC m c κ x) :=
  hecke_mem (kzHeckeC m c κ) (wpSub (m + 1)) (fun j => by
    rw [kzHeckeC_σ]
    exact (wpSub (m + 1)).smul_mem (WP_kzBraidRep κ c (σ j)) _) x

theorem WP_jimboRep (q : ℂ) (hq : q ≠ 0) (x : Hecke ℂ q q⁻¹ m) : WP (jimboRep q hq m x) :=
  hecke_mem (jimboRep q hq m) (wpSub (m + 1)) (fun j => by
    rw [jimboRep_σ]; exact WP_strandBraid q j) x

/-- **On each weight space the KZ and Jimbo representations have the same trace**, at every
complex coupling with `q` not a root of unity. -/
theorem trace_res_kz_eq_jimbo (c κ : ℂ) (hκ : GenericParameter.NotRootOfUnity (qC κ)) (k : ℕ)
    (x : Hecke ℂ (qC κ) (qC κ)⁻¹ m) :
    (res k (kzHeckeC m c κ x)).trace = (res k (jimboRep (qC κ) (qC_ne_zero κ) m x)).trace := by
  obtain ⟨U, hU⟩ := conj_of_eq_at_zero (n := m)
    (fun κ => resHom k (kzHeckeC m c κ) (WP_kzHeckeC c κ))
    (fun κ => resHom k (jimboRep (qC κ) (qC_ne_zero κ) m) (WP_jimboRep _ _))
    (fun j => by
      simp only [resHom_apply]
      exact continuous_res k (continuous_kzHeckeC_σ c j))
    (fun j => by
      simp only [resHom_apply]
      exact continuous_res k (continuous_jimboRepC_σ j))
    (fun j => by simp only [resHom_apply, kzHeckeC_zero_σ c j]) hκ
  exact trace_eq_of_conj U (hU x)

/-- **The weighted-trace identity.** For every complex coupling `κ` with `q = e^{2πiκ}` not a
root of unity, every `h ∈ H_{m+1}(q)` and every operator `D` acting by a scalar `f(k)` on each
weight space, `Tr(D · KZ(h)) = Tr(D · Jimbo(h))`. -/
theorem weighted_trace_kz_eq_jimbo (c κ : ℂ) (hκ : GenericParameter.NotRootOfUnity (qC κ))
    (f : ℕ → ℂ) (x : Hecke ℂ (qC κ) (qC κ)⁻¹ m) :
    (Matrix.diagonal (fun a => f (cnt a)) * kzHeckeC m c κ x).trace =
      (Matrix.diagonal (fun a => f (cnt a)) * jimboRep (qC κ) (qC_ne_zero κ) m x).trace := by
  rw [trace_diag_mul, trace_diag_mul]
  exact Finset.sum_congr rfl fun k _ => by rw [trace_res_kz_eq_jimbo c κ hκ k x]

/-! ## Matching the mass identity of `MassTraceMarkov` -/

/-- The site weight `K^{⊗N}`, `K = diag(w₀, w₁)`, acts by `w₀^{N−k} w₁^k` on `V_k`. -/
theorem prod_weight_eq {R : Type*} [CommRing R] (w : Fin 2 → R) :
    ∀ {N : ℕ} (a : Fin N → Fin 2), ∏ s, w (a s) = w 0 ^ (N - cnt a) * w 1 ^ cnt a
  | 0, a => by simp [cnt]
  | N + 1, a => by
      have hc : cnt a = ((a 0 : Fin 2) : ℕ) + cnt (fun s : Fin N => a s.succ) := by
        simp only [cnt, Fin.sum_univ_succ]
      have hle := cnt_le (fun s : Fin N => a s.succ)
      rw [Fin.prod_univ_succ, prod_weight_eq w (fun s : Fin N => a s.succ), hc]
      rcases (by decide : ∀ x : Fin 2, x = 0 ∨ x = 1) (a 0) with h | h
      · rw [h]
        simp only [Fin.val_zero, zero_add]
        rw [show N + 1 - cnt (fun s : Fin N => a s.succ) = (N - cnt (fun s : Fin N => a s.succ)) + 1
          by omega, pow_succ]
        ring
      · rw [h]
        simp only [Fin.val_one]
        rw [show N + 1 - (1 + cnt (fun s : Fin N => a s.succ)) =
          N - cnt (fun s : Fin N => a s.succ) by omega, pow_add, pow_one]
        ring

theorem siteWeight_eq_diag_cnt {N : ℕ} (w : Fin 2 → ℂ) :
    (QOU.IwahoriHecke.QuantumTrace.siteWeight w : Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ) =
      Matrix.diagonal (fun a => (fun k => w 0 ^ (N - k) * w 1 ^ k) (cnt a)) := by
  unfold QOU.IwahoriHecke.QuantumTrace.siteWeight
  congr 1
  funext a
  exact prod_weight_eq w a

/-- **The site-weighted trace of the KZ holonomy is that of Jimbo's R-matrix action.** -/
theorem siteWeight_trace_kz_eq_jimbo (c κ : ℂ) (hκ : GenericParameter.NotRootOfUnity (qC κ))
    (w : Fin 2 → ℂ) (x : Hecke ℂ (qC κ) (qC κ)⁻¹ m) :
    (QOU.IwahoriHecke.QuantumTrace.siteWeight w * kzHeckeC m c κ x).trace =
      (QOU.IwahoriHecke.QuantumTrace.siteWeight w * jimboRep (qC κ) (qC_ne_zero κ) m x).trace := by
  rw [siteWeight_eq_diag_cnt (N := m + 1)]
  exact weighted_trace_kz_eq_jimbo c κ hκ (fun k => w 0 ^ (m + 1 - k) * w 1 ^ k) x

open QOU.IwahoriHecke.Balanced QOU.IwahoriHecke.BraidGroup in
/-- **The mass identity on the KZ side.** The normalised Markov trace of a braid `β`
(`braidTrace`, the left side of `MassTraceMarkov.braidTrace_wordBraid`) is the site-weighted
trace of the continuous KZ holonomy representation on `β`'s image in `H_{m+1}(q)`:
`tr_M(β) = wi^{m+1} · Tr(K^{⊗(m+1)} · KZ(x_β))`. -/
theorem braidTrace_eq_kz (c κ : ℂ) (hκ : GenericParameter.NotRootOfUnity (qC κ))
    (w : Fin 2 → ℂ) (wi : ℂ) (β : BraidGroupN m) :
    braidTrace (qC κ) (qC κ)⁻¹ (mul_inv_cancel₀ (qC_ne_zero κ)) w wi β =
      wi ^ (m + 1) * (QOU.IwahoriHecke.QuantumTrace.siteWeight w *
        kzHeckeC m c κ ((JimboActionKernel.skeinCoxAEquiv (qC κ) (qC_ne_zero κ) m).symm
          ((heckeRep (coxA m) (mul_inv_cancel₀ (qC_ne_zero κ)) coxA_symm β :
            (BalancedHecke (coxA m) (qC κ))ˣ) : BalancedHecke (coxA m) (qC κ)))).trace := by
  rw [siteWeight_trace_kz_eq_jimbo c κ hκ, jimboRep_eq_jimbo, JimboActionKernel.jimbo_apply,
    AlgEquiv.apply_symm_apply, braidTrace, QOU.IwahoriHecke.MarkovNormalized.markovTr,
    QOU.IwahoriHecke.QuantumTrace.qTrace]

end Main

end QOU.Mass.KohnoWeighted
